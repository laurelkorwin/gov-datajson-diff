# Change History for usaid.json

### Changes from 31606f9 to dd2190f (Part 1/2)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/usaid.json b/usaid.json
index 2ece115..468a4bc 100644
--- a/usaid.json
+++ b/usaid.json
@@ -3,7 +3,6 @@
     "dataset": [
         {
             "accessLevel": "public",
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
             "bureauCode": [
                 "184:15"
             ],
@@ -11,19 +10,7 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2018-10-04",
             "description": "Provides a list of all data assets maintained by USAID",
-            "title": "USAID Enterprise Data Inventory",
-            "keyword": [
-                "USAID"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "4a3eea16-c278-4b42-9713-a877c7c5ec43",
-            "programCode": [
-                "184:036"
-            ],
             "distribution": [
                 {
                     "downloadURL": "https://www.usaid.gov/data.json",
@@ -31,13 +18,25 @@
                     "mediaType": "application/json"
                 }
             ],
+            "identifier": "4a3eea16-c278-4b42-9713-a877c7c5ec43",
+            "keyword": [
+                "USAID"
+            ],
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2018-10-04",
+            "programCode": [
+                "184:036"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "title": "USAID Enterprise Data Inventory"
         },
         {
             "accessLevel": "public",
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
             "bureauCode": [
                 "184:15"
             ],
@@ -45,16 +44,21 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2018-10-04",
             "description": "Version 4.2.20181004",
-            "title": "USAID Public Data Listing",
+            "distribution": [
+                {
+                    "downloadURL": "http://www.usaid.gov/data.json",
+                    "format": "json",
+                    "mediaType": "application/json",
+                    "title": "USAID Public Data Listing"
+                }
+            ],
+            "identifier": "0101010101010011010000010100100101000100",
             "keyword": [
                 "catalog"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0101010101010011010000010100100101000100",
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2018-10-04",
             "programCode": [
                 "184:001",
                 "184:002",
@@ -94,14 +98,10 @@
                 "184:036",
                 "184:037"
             ],
-            "distribution": [
-                {
-                    "downloadURL": "http://www.usaid.gov/data.json",
-                    "format": "json",
-                    "mediaType": "application/json",
+            "publisher": {
+                "name": "USAID"
+            },
             "title": "USAID Public Data Listing"
-                }
-            ]
         },
         {
             "accessLevel": "public",
@@ -112,21 +112,7 @@
                 "fn": "Jay Mahanand",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-08-10",
             "description": "The IT Policy Archive is published in accordance with direction from the Office of Management and Budget for the August 2015 Integrated Data Collection.",
-            "title": "Agency IT Policy Archive",
-            "keyword": [
-                "FITARA",
-                "IT Policy"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "b6a77efa-8100-4947-8dde-e8d19c1c5a38",
-            "programCode": [
-                "184:000"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
             "distribution": [
                 {
                     "description": "List of IT Policies",
@@ -143,13 +129,26 @@
                     "title": "Agency IT Policy Archive"
                 }
             ],
+            "identifier": "b6a77efa-8100-4947-8dde-e8d19c1c5a38",
+            "keyword": [
+                "FITARA",
+                "IT Policy"
+            ],
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2015-08-10",
+            "programCode": [
+                "184:000"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "title": "Agency IT Policy Archive"
         },
         {
             "accessLevel": "public",
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
             "bureauCode": [
                 "184:15"
             ],
@@ -157,42 +156,43 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-11-24",
+            "dataQuality": true,
+            "describedByType": "application/rtf",
             "description": "The Office of the Chief Information Officer in the Management Bureau of USAID launched initiatives designed for IT cost savings and avoidance.  This dataset includes those initiatives where some or all planned cost savings and avoidance has been realized and the total by year of the realized cost savings and avoidance.  The dataset will be updated periodically to reflect new initiatives or adjustments to the totals.",
-            "title": "USAID IT Reform Cost Savings/Avoidance",
-            "keyword": [
-                "information technology",
-                "CIO",
-                "IT reform",
-                "cost savings",
-                "cost avoidance"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "1959692e-8ea5-4ccc-b40c-9429f0cab9ef",
-            "programCode": [
-                "184:036"
-            ],
             "distribution": [
                 {
+                    "describedBy": "https://management.cio.gov/schemaexamples/costSavingsAvoidanceSchema.json",
+                    "describedByType": "application/json",
                     "description": "The Office of the Chief Information Officer in the Management Bureau of USAID launched initiatives designed for IT cost savings and avoidance.  This dataset includes those initiatives where some or all planned cost savings and avoidance has been realized and the total by year of the realized cost savings and avoidance.  The dataset will be updated periodically to reflect new initiatives or adjustments to the totals.",
                     "downloadURL": "http://www.usaid.gov/digitalstrategy/costsavings.json",
                     "format": "JSON",
                     "mediaType": "application/json",
-                    "title": "USAID IT Reform Cost Savings/Avoidance",
-                    "describedBy": "https://management.cio.gov/schemaexamples/costSavingsAvoidanceSchema.json",
-                    "describedByType": "application/json"
+                    "title": "USAID IT Reform Cost Savings/Avoidance"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "1959692e-8ea5-4ccc-b40c-9429f0cab9ef",
+            "keyword": [
+                "information technology",
+                "CIO",
+                "IT reform",
+                "cost savings",
+                "cost avoidance"
+            ],
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2015-11-24",
+            "programCode": [
+                "184:036"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "https://management.cio.gov/schema/"
             ],
-            "describedByType": "application/rtf"
+            "title": "USAID IT Reform Cost Savings/Avoidance"
         },
         {
             "accessLevel": "public",
@@ -203,19 +203,28 @@
                 "fn": "Brian Bingham",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-01-09",
             "description": "AidData is a research and innovation lab making information on development finance more accessible and actionable. Tracking more than $6 trillion dollars from 90+ donor agencies, AidData undertakes cutting-edge research on aid distribution and impact, geocodes and crowdsources aid information, and develops applications and custom data solutions for diverse stakeholders. The AidData team works with a wide range of partner organizations to collect, visualize, and analyze development finance for more effective development policy, practice, and research.",
-            "title": "AidData",
+            "distribution": [
+                {
+                    "accessURL": "http://aiddata.org/use-aiddatas-api",
+                    "description": "The AidData API allows for programmatic access to the catalogue of AidData information.",
+                    "format": "API",
+                    "title": "AIDDATA API"
+                }
+            ],
+            "identifier": "49fc4b3c-c556-4552-8551-797c1a84c83c",
             "keyword": [
                 "partners",
                 "financial",
                 "impact",
                 "distribution"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "49fc4b3c-c556-4552-8551-797c1a84c83c",
+            "landingPage": "http://aiddata.org",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-01-09",
             "programCode": [
                 "184:016",
                 "184:017",
@@ -225,20 +234,11 @@
                 "184:033",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "distribution": [
-                {
-                    "description": "The AidData API allows for programmatic access to the catalogue of AidData information.",
-                    "accessURL": "http://aiddata.org/use-aiddatas-api",
-                    "format": "API",
-                    "title": "AIDDATA API"
-                }
-            ],
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "http://aiddata.org",
-            "rights": "Owned and maintained by Development Gateway, www.developmentgateway.org."
+            "publisher": {
+                "name": "USAID"
+            },
+            "rights": "Owned and maintained by Development Gateway, www.developmentgateway.org.",
+            "title": "AidData"
         },
         {
             "accessLevel": "public",
@@ -249,19 +249,22 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-04-27",
             "description": "The AmericasBarometer survey implemented by the Latin American Public Opinion Project (LAPOP) is the only scientifically rigorous comparative survey that covers 28 nations including all of North, Central, and South America, as well as a significant number of countries in the Caribbean. (See the individual entries to retrieve data for the country surveys.) The surveys are conducted by Vanderbilt University with partners in participating countries.  The surveys receive generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The Collection of AmericasBarometer Surveys by the Latin American Public Opinion Project (LAPOP)",
+            "identifier": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Brazil"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US",
+                "pt",
+                "es"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-04-27",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -269,17 +272,14 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
             ],
-            "language": [
-                "en-US",
-                "pt",
-                "es"
-            ]
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "The Collection of AmericasBarometer Surveys by the Latin American Public Opinion Project (LAPOP)"
         },
         {
             "accessLevel": "public",
@@ -290,51 +290,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-04-27",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Brazil survey was carried out between March 21st and April 27th of 2014.  It is a follow-up of the national surveys of 2006, and 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University and Universidade de Brasilia. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Brazil"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "f6336b6f-b6bd-44ce-a448-8690e90174b9",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/brazil.php",
-            "spatial": "Brazil",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Brazil_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "This survey was carried out between March 21st and April 27th of 2014, as part of the LAPOP AmericasBarometer 2014 wave of surveys. It is a follow-up of the national surveys of 2006, and 2008, 2010 and 2012 carried out by the LAPOP. The 2014 survey was conducted by Vanderbilt University and Universidade de Brasilia. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Brazil_Data_LAPOP_americasbarometer_2014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Brazil_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2014"
                 }
             ],
+            "identifier": "f6336b6f-b6bd-44ce-a448-8690e90174b9",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Brazil"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/brazil.php",
             "language": [
                 "en-US",
                 "pt"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-04-27",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Brazil_14_Questionnaire_Por_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Brazil_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Brazil",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2014"
         },
         {
             "accessLevel": "public",
@@ -345,19 +345,33 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-05-05",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Colombia survey was carried out between March 28st and May 5th of 2014.  It is a follow-up of the national surveys since 1991.  The 2014 survey was conducted by Vanderbilt University and the Universidad de los Andes and the Observatorio de la Democracia with the field work being carried out by the Centro Nacional de Consultoria (CNC). The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2014",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Colombia_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Colombia survey was carried out between March 28st and May 5th of 2014.  It is a follow-up of the national surveys since 1991.  The 2014 survey was conducted by Vanderbilt University and the Universidad de los Andes and the Observatorio de la Democracia with the field work being carried out by the Centro Nacional de Consultoria (CNC). The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Colombia_Data_LAPOP_americasbarometer_2014.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2014"
+                }
+            ],
+            "identifier": "057b9ff1-29c3-4a6c-be52-11d0060e8789",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Colombia"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "057b9ff1-29c3-4a6c-be52-11d0060e8789",
+            "landingPage": "http://www.vanderbilt.edu/lapop/colombia.php",
+            "language": [
+                "en-US",
+                "es"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-05-05",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -365,31 +379,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/colombia.php",
-            "spatial": "Colombia",
-            "distribution": [
-                {
-                    "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Colombia survey was carried out between March 28st and May 5th of 2014.  It is a follow-up of the national surveys since 1991.  The 2014 survey was conducted by Vanderbilt University and the Universidad de los Andes and the Observatorio de la Democracia with the field work being carried out by the Centro Nacional de Consultoria (CNC). The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Colombia_Data_LAPOP_americasbarometer_2014.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Colombia_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US",
-                "es"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Colombia_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Colombia_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Colombia",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2014"
         },
         {
             "accessLevel": "public",
@@ -400,51 +400,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-05-06",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Costa Rica survey was carried out between March 4th and May 6th of 2014.  It is a follow-up of the national surveys of 2004,2006,2008,2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the field work being carried out by Borge y Asociados. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Costa Rica"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "1d1c83dc-9b6c-4682-af4d-39d4738b571e",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/costa-rica.php",
-            "spatial": "Costa Rica",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Costa Rica survey was carried out between March 4th and May 6th of 2014.  It is a follow-up of the national surveys of 2004,2006,2008,2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the field work being carried out by Borge y Asociados. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/CostaRica%20_Data_LAPOP_americasbarometer%202014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-CostaRica, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-CostaRica, 2014"
                 }
             ],
+            "identifier": "1d1c83dc-9b6c-4682-af4d-39d4738b571e",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Costa Rica"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/costa-rica.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-05-06",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/CostaRica_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Costa Rica",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2014"
         },
         {
             "accessLevel": "public",
@@ -455,51 +455,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-03-25",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Dominican Republic survey was carried out between March 11th and March 25th of 2014.  It is a follow-up of the national surveys of 2004,2006,2008,2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the field work being carried out by Gallup Republica Dominica. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Dominican Republic"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "c9e00b1b-3179-4ee9-ae80-39be092b2db9",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/dominican-republic.php",
-            "spatial": "Dominican Republic",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Dominican Republic survey was carried out between March 11th and March 25th of 2014.  It is a follow-up of the national surveys of 2004,2006,2008,2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the field work being carried out by Gallup Republica Dominica. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_DATA_LAPOP_americasbarometer-2014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-DominicanRepublic, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-DominicanRepublic, 2014"
                 }
             ],
+            "identifier": "c9e00b1b-3179-4ee9-ae80-39be092b2db9",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Dominican Republic"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/dominican-republic.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-03-25",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Dominican Republic",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2014"
         },
         {
             "accessLevel": "public",
@@ -510,51 +510,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-04-30",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the El Salvador survey was carried out between March 28th and April 30th of 2014.  It is a follow-up of the national surveys since 1991.  The 2014 survey was conducted by Vanderbilt University and FUNDAUNGO. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "El Salvador"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "ce0cbbf5-a8ea-4cd5-8aaf-4b04336f03f4",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/el-salvador.php",
-            "spatial": "El Salvador",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the El Salvador survey was carried out between March 28th and April 30th of 2014.  It is a follow-up of the national surveys since 1991.  The 2014 survey was conducted by Vanderbilt University and FUNDAUNGO. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Data_LAPOP_americasbarometer_2014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-ElSalvador, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-ElSalvador, 2014"
                 }
             ],
+            "identifier": "ce0cbbf5-a8ea-4cd5-8aaf-4b04336f03f4",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "El Salvador"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/el-salvador.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-04-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "El Salvador",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2014"
         },
         {
             "accessLevel": "public",
@@ -565,51 +565,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-05-10",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Guatemala survey was carried out between April 1st and May 10th of 2014.  It is a follow-up of the national surveys since 1992.  The 2014 survey was conducted by Vanderbilt University and Asociation de Investigacion y Estudios Sociales (ASIES). The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Guatemala"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "bd2906ee-7880-4f39-9aff-7c8876d0403b",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/guatemala.php",
-            "spatial": "Guatemala",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Guatemala survey was carried out between April 1st and May 10th of 2014.  It is a follow-up of the national surveys since 1992.  The 2014 survey was conducted by Vanderbilt University and Asociation de Investigacion y Estudios Sociales (ASIES). The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Data_LAPOP_americasbarometer_2014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2014"
                 }
             ],
+            "identifier": "bd2906ee-7880-4f39-9aff-7c8876d0403b",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Guatemala"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/guatemala.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-05-10",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Guatemala",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2014"
         },
         {
             "accessLevel": "public",
@@ -620,19 +620,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-07-12",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Guyana survey was carried out between June 4th and July 12th of 2014.  It is a follow-up of the national surveys of 2006, 2009, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the field work being carried out by Development Policy and Management Consultants (DPMC). The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2014",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guyana_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Guyana survey was carried out between June 4th and July 12th of 2014.  It is a follow-up of the national surveys of 2006, 2009, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the field work being carried out by Development Policy and Management Consultants (DPMC). The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guyana_Data_LAPOP_americasbarometer_2014.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2014"
+                }
+            ],
+            "identifier": "41aaf419-1f2c-4284-b213-25c30d8c7b19",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Guyana"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "41aaf419-1f2c-4284-b213-25c30d8c7b19",
+            "landingPage": "http://www.vanderbilt.edu/lapop/guyana.php",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-07-12",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -640,31 +653,18 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/Guyana_14_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
+                "http://www.usaid.gov/opengov/developer/datasets/Guyana_Tech_Info_LAPOP_americasbarometer_2014.pdf",
+                "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
+            ],
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/guyana.php",
             "spatial": "Guyana",
-            "distribution": [
-                {
-                    "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Guyana survey was carried out between June 4th and July 12th of 2014.  It is a follow-up of the national surveys of 2006, 2009, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the field work being carried out by Development Policy and Management Consultants (DPMC). The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guyana_Data_LAPOP_americasbarometer_2014.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guyana_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/Guyana_14_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
-                "http://www.usaid.gov/opengov/developer/datasets/Guyana_Tech_Info_LAPOP_americasbarometer_2014.pdf",
-                "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
-        },
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2014"
+        },
         {
             "accessLevel": "public",
             "bureauCode": [
@@ -674,19 +674,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-03-08",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Haiti survey was carried out between February 18th and March 8th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the field work being carried out by Borges y Asociados. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2014",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Haiti survey was carried out between February 18th and March 8th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the field work being carried out by Borges y Asociados. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Haiti_Data_LAPOP_americasbarometer_2014.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2014"
+                }
+            ],
+            "identifier": "767769b9-60fe-4bc6-bf10-9171f60b0530",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Haiti"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "767769b9-60fe-4bc6-bf10-9171f60b0530",
+            "landingPage": "http://www.vanderbilt.edu/lapop/haiti.php",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-03-08",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -694,30 +707,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/haiti.php",
-            "spatial": "Haiti",
-            "distribution": [
-                {
-                    "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Haiti survey was carried out between February 18th and March 8th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the field work being carried out by Borges y Asociados. The 2014 AmericasBarometer received generous support from many sources, including USAID, UNDP, IADB, Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Haiti_Data_LAPOP_americasbarometer_2014.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "language": [
-                "en-US"
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Haiti_14_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Haiti_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Haiti",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2014"
         },
         {
             "accessLevel": "public",
@@ -728,51 +728,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-05-09",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Honduras survey was carried out between March 8th and May 9th of 2014.  It is a follow-up of the national surveys of 2004, 2006, 2008, 2010 and 2012.  The 2014 survey was conducted with the field work being carried out by Le Vote. Funding came from the United States Agency for International Development (USAID).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Honduras"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "34369d11-52c7-419a-8654-0940ad5fea47",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/honduras.php",
-            "spatial": "Honduras",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Honduras survey was carried out between March 8th and May 9th of 2014.  It is a follow-up of the national surveys of 2004, 2006, 2008, 2010 and 2012.  The 2014 survey was conducted with the field work being carried out by Le Vote. Funding came from the United States Agency for International Development (USAID).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Honduras_Data_LAPOP_americasbarometer_2014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2014"
                 }
             ],
+            "identifier": "34369d11-52c7-419a-8654-0940ad5fea47",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Honduras"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/honduras.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-05-09",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Honduras",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2014"
         },
         {
             "accessLevel": "public",
@@ -783,19 +783,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-03-20",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Jamaica survey was carried out between February 25th and March 20th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by the University of West Indies. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2014",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Jamaica survey was carried out between February 25th and March 20th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by the University of West Indies. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Data_LAPOP_americasbarometer_2014.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2014"
+                }
+            ],
+            "identifier": "698cacd4-af49-482a-aa4c-72eb674e41a9",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Jamaica"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "698cacd4-af49-482a-aa4c-72eb674e41a9",
+            "landingPage": "http://www.vanderbilt.edu/lapop/jamaica.php",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-03-20",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -803,30 +816,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/jamaica.php",
-            "spatial": "Jamaica",
-            "distribution": [
-                {
-                    "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Jamaica survey was carried out between February 25th and March 20th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by the University of West Indies. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Data_LAPOP_americasbarometer_2014.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "language": [
-                "en-US"
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Jamaica_14_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Jamaica",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2014"
         },
         {
             "accessLevel": "public",
@@ -837,51 +837,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-02-24",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Mexico survey was carried out between January 24th and February 24th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the fieldwork being carried out by Data Opinion Publica y Mercados. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Mexico"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "f2f47904-00f1-44e3-ac3a-60af7d6ef7c7",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/mexico.php",
-            "spatial": "Mexico",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Mexico survey was carried out between January 24th and February 24th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the fieldwork being carried out by Data Opinion Publica y Mercados. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Mexico_Data_LAPOP_americasbarometer_2014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2014"
                 }
             ],
+            "identifier": "f2f47904-00f1-44e3-ac3a-60af7d6ef7c7",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Mexico"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/mexico.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-02-24",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Mexico",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2014"
         },
         {
             "accessLevel": "public",
@@ -892,51 +892,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-03-22",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Nicaragua survey was carried out between February 25th and March 22nd of 2014.  It is a follow-up of the national surveys of 1999, 2004, 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the fieldwork being carried out by Borge y Asociados. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Nicaragua"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "eff51ff1-c653-48a8-8eea-0b2529b77dce",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/nicaragua.php",
-            "spatial": "Nicaragua",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Nicaragua survey was carried out between February 25th and March 22nd of 2014.  It is a follow-up of the national surveys of 1999, 2004, 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the fieldwork being carried out by Borge y Asociados. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Data_LAPOP_americasbarometer_2014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2014"
                 }
             ],
+            "identifier": "eff51ff1-c653-48a8-8eea-0b2529b77dce",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Nicaragua"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/nicaragua.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-03-22",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Nicaragua",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2014"
         },
         {
             "accessLevel": "public",
@@ -947,51 +947,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-05-03",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Panama survey was carried out between March 13th and May 3rd of 2014.  It is a follow-up of the national surveys of 2004, 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the fieldwork being carried out by Borge y Asociados. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Panama"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "7a1a875c-b198-44e3-be66-16e3e94c2915",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/panama.php",
-            "spatial": "Panama",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometer-2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Panama survey was carried out between March 13th and May 3rd of 2014.  It is a follow-up of the national surveys of 2004, 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the fieldwork being carried out by Borge y Asociados. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Panama_Data_LAPOP_americasbarometer%202014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometer-2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2014"
                 }
             ],
+            "identifier": "7a1a875c-b198-44e3-be66-16e3e94c2915",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Panama"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/panama.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-05-03",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Panama_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Panama_Tech_Info_LAPOP_americsbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Panama",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2014"
         },
         {
             "accessLevel": "public",
@@ -1002,51 +1002,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-02-08",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Paraguay survey was carried out between January 18th and February 8th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the fieldwork being carried out by Centro de Informacion y Recursos para el (Desarrollo (CIRD). The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Paraguay"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "91eb630e-7a77-4cdd-b3fc-4fb05a717580",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/paraguay.php",
-            "spatial": "Paraguay",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Paraguay survey was carried out between January 18th and February 8th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University with the fieldwork being carried out by Centro de Informacion y Recursos para el (Desarrollo (CIRD). The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_Data_LAPOP_americasbarometer_2014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2014"
                 }
             ],
+            "identifier": "91eb630e-7a77-4cdd-b3fc-4fb05a717580",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Paraguay"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/paraguay.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-02-08",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Paraguay_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Paraguay_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Paraguay",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2014"
         },
         {
             "accessLevel": "public",
@@ -1057,51 +1057,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-02-08",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Peru survey was carried out between January 23rd and February 8th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University and the Instituto de Estudios Peruanos. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Peru"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "f8e81635-c4bd-4b9f-a853-abb4b9dba041",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/peru.php",
-            "spatial": "Peru",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Peru_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Peru survey was carried out between January 23rd and February 8th of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University and the Instituto de Estudios Peruanos. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Peru_Data_LAPOP_americasbarometer_2014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Peru_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2014"
                 }
             ],
+            "identifier": "f8e81635-c4bd-4b9f-a853-abb4b9dba041",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Peru"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/peru.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-02-08",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Peru_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Peru_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Peru",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2014"
         },
         {
             "accessLevel": "public",
@@ -1112,51 +1112,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-04-23",
             "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Uruguay survey was carried out between March 8th and April 23rd of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University, CIFRA, Gonzales Raga & Associates and la Universidad de Montevideo. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Uruguay, 2014",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Uruguay"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "b57363b2-e3e2-421c-9e07-92960b03f57e",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/uruguay.php",
-            "spatial": "Uruguay",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Uruguay_codebook_LAPOP_americasbarometer_2014.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A part of the 2014 round of public opinion surveys implemented by LAPOP, the Uruguay survey was carried out between March 8th and April 23rd of 2014.  It is a follow-up of the national surveys of 2006, 2008, 2010 and 2012.  The 2014 survey was conducted by Vanderbilt University, CIFRA, Gonzales Raga & Associates and la Universidad de Montevideo. The 2014 AmericasBarometer received generous support from many sources including USAID, UNDP, IADB,Vanderbilt U., Princeton U., Universite Laval, U. of Notre Dame, among others.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Uruguay_Data_LAPOP_americasbarometer_2014.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Uruguay, 2014",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Uruguay_codebook_LAPOP_americasbarometer_2014.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Uruguay, 2014"
                 }
             ],
+            "identifier": "b57363b2-e3e2-421c-9e07-92960b03f57e",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Uruguay"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/uruguay.php",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-04-23",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Uruguay_14_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Uruguay_Tech_Info_LAPOP_americasbarometer_2014.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Uruguay",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Uruguay, 2014"
         },
         {
             "accessLevel": "public",
@@ -1167,51 +1167,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-09-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Bolivia as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and Encuesta y Estudios (Gallup) Bolivia and funded by USAID.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Bolivia, 2004",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Bolivia"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "49cc839e-3742-472d-bf18-e9b24260c5a9",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Bolivia",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Bolivia_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Bolivia as part of its 2004 round of surveys.  The 2004 survey was conducted by Vanderbilt University and Encuesta y Estudios (Gallup) Bolivia and funded by USAID.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Bolivia_Data_LAPOP_americasbarometer_2004.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Bolivia, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Bolivia_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Bolivia, 2004"
                 }
             ],
+            "identifier": "49cc839e-3742-472d-bf18-e9b24260c5a9",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Bolivia"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-09-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Bolivia_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Bolivia_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Bolivia",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Bolivia, 2004"
         },
         {
             "accessLevel": "public",
@@ -1222,51 +1222,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-04-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Colombia as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and the Centro Nacional de Consultoria in Colombia.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2004",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Colombia"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "bf6c58ab-b995-41fc-96a4-fc21c3367e26",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Colombia",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Colombia_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Colombia as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and the Centro Nacional de Consultoria in Colombia.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Colombia_Data_LAPOP_americasbarometer_2004.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Colombia_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2004"
                 }
             ],
+            "identifier": "bf6c58ab-b995-41fc-96a4-fc21c3367e26",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Colombia"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-04-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Colombia_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Colombia_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Colombia",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2004"
         },
         {
             "accessLevel": "public",
@@ -1277,51 +1277,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2004 round surveys.  The 2004 survey was conducted by the Central American Population Center de CCP of the University of Costa Rica.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2004",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Costa Rica"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "69640e68-4637-4193-af0d-3fdcf90195bc",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Costa Rica",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2004 round surveys.  The 2004 survey was conducted by the Central American Population Center de CCP of the University of Costa Rica.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Data_LAPOP_americasbarometer_2004.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2004"
                 }
             ],
+            "identifier": "69640e68-4637-4193-af0d-3fdcf90195bc",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Costa Rica"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/CostaRica_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Costa Rica",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2004"
         },
         {
             "accessLevel": "public",
@@ -1332,51 +1332,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2004 round surveys.  The 2004 survey was conducted by El Centro Universitario de Estudios Politicos y Sociales (CUEPS) of the Potificia Universidad Catolica Madre y Maestra and the Centro de Estudios Sociales y Demograficos (CESDEM).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2004",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Dominican Republic"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "9efa6f28-41fa-4bbd-9e3e-9015037be520",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Dominican Republic",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2004 round surveys.  The 2004 survey was conducted by El Centro Universitario de Estudios Politicos y Sociales (CUEPS) of the Potificia Universidad Catolica Madre y Maestra and the Centro de Estudios Sociales y Demograficos (CESDEM).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Data_LAPOP_americasbarometer_2004.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2004"
                 }
             ],
+            "identifier": "9efa6f28-41fa-4bbd-9e3e-9015037be520",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Dominican Republic"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Dominican Republic",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2004"
         },
         {
             "accessLevel": "public",
@@ -1387,51 +1387,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-04-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Ecuador as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and Cedatos.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2004",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Ecuador"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "c7199de3-605d-43d2-a87a-8b7a352739c0",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Ecuador",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Ecuador_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Ecuador as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and Cedatos.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Ecuador_Data_LAPOP_americasbarometer_2004.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Ecuador_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2004"
                 }
             ],
+            "identifier": "c7199de3-605d-43d2-a87a-8b7a352739c0",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Ecuador"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-04-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Ecuador_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Ecuador_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Ecuador",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2004"
         },
         {
             "accessLevel": "public",
@@ -1442,51 +1442,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in El Salvador as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and FundaUngo.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2004",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "ElSalvador"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "c02b7383-035c-48e2-9dc0-d2d0f221837d",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "ElSalvador",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in El Salvador as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and FundaUngo.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Data_LAPOP_americasbarometer_2004.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2004"
                 }
             ],
+            "identifier": "c02b7383-035c-48e2-9dc0-d2d0f221837d",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "ElSalvador"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "ElSalvador",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2004"
         },
         {
             "accessLevel": "public",
@@ -1497,51 +1497,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and Cedatos.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2004",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and Cedatos.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Data_LAPOP_americasbarometer_2004.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2004"
+                }
+            ],
+            "identifier": "c375b41a-28c3-446d-81b0-7f590522808b",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Guatemala"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "c375b41a-28c3-446d-81b0-7f590522808b",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Guatemala",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and Cedatos.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Data_LAPOP_americasbarometer_2004.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Guatemala",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2004"
         },
         {
             "accessLevel": "public",
@@ -1552,51 +1552,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Honduras as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University with FundaUngo and IUDOP, the public opinion arm of the Universidad Centroamericana Simeon Canas (UCA) of El Salvador.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2004",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Honduras"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "93a3d38c-7cde-4a4c-8d5d-722a5f29fc21",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Honduras",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Honduras as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University with FundaUngo and IUDOP, the public opinion arm of the Universidad Centroamericana Simeon Canas (UCA) of El Salvador.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Honduras_Data_LAPOP_americasbarometer_2004.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2004"
                 }
             ],
+            "identifier": "93a3d38c-7cde-4a4c-8d5d-722a5f29fc21",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Honduras"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Honduras",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2004"
         },
         {
             "accessLevel": "public",
@@ -1607,51 +1607,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Mexico as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and ITAM.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2004",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Mexico"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "87e56dfe-848b-44db-9889-105401231b7f",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Mexico",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Mexico as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and ITAM.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Mexico_Data_LAPOP_americasbarometer_2004.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2004"
                 }
             ],
+            "identifier": "87e56dfe-848b-44db-9889-105401231b7f",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Mexico"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Mexico",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2004"
         },
         {
             "accessLevel": "public",
@@ -1662,51 +1662,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Nicaragua as part of its 2004 round surveys.   The 2004 survey was conducted by Universidad Centroamericana (UCA) with support from USAID.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2004",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Nicaragua"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "139dce51-c4b2-43ea-811c-a0301b84672c",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Nicaragua",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Nicaragua as part of its 2004 round surveys.   The 2004 survey was conducted by Universidad Centroamericana (UCA) with support from USAID.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Data_LAPOP_americasbarometer_2004.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2004"
                 }
             ],
+            "identifier": "139dce51-c4b2-43ea-811c-a0301b84672c",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Nicaragua"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Nicaragua",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2004"
         },
         {
             "accessLevel": "public",
@@ -1717,51 +1717,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2004-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and CELA.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2004",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Panama"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "138cbb31-08bb-40cb-b1e1-617f035ca1b6",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Panama",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometer_2004.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2004 round surveys.   The 2004 survey was conducted by Vanderbilt University and CELA.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Panama_Data_LAPOP_americasbarometer_2004.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2004",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometer_2004.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2004"
                 }
             ],
+            "identifier": "138cbb31-08bb-40cb-b1e1-617f035ca1b6",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Panama"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2004-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Panama_04_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Panama_Tech_Info_LAPOP_americasbarometer_2004.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Panama",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2004"
         },
         {
             "accessLevel": "public",
@@ -1772,19 +1772,33 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Brazil as part of its 2006 round surveys.   The 2006 survey was conducted by Universidade Federal de Goias (UFG), with scientific direction being provided by Mitchell A. Seligson.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2006",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Brazil_codebook_LAPOP_americasbarometer_2007.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Brazil as part of its 2006 round surveys.   The 2006 survey was conducted by Universidade Federal de Goias (UFG), with scientific direction being provided by Mitchell A. Seligson.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Brazil_Data_LAPOP_americasbarometer_2007.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2006"
+                }
+            ],
+            "identifier": "b4002c20-6149-4cb3-a63e-86ae647f21c1",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Brazil"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "b4002c20-6149-4cb3-a63e-86ae647f21c1",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US",
+                "pt"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -1792,31 +1806,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Brazil",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Brazil as part of its 2006 round surveys.   The 2006 survey was conducted by Universidade Federal de Goias (UFG), with scientific direction being provided by Mitchell A. Seligson.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Brazil_Data_LAPOP_americasbarometer_2007.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Brazil_codebook_LAPOP_americasbarometer_2007.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US",
-                "pt"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Brazil_07_Questionnaire_PORT_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Brazil_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Brazil",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2006"
         },
         {
             "accessLevel": "public",
@@ -1827,51 +1827,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2006 round of surveys.  The 2006 survey was conducted by Vanderbilt University, and the field work was carried out by Central American Population Center (CCP) of the University of Costa Rica.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Costa Rica"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0b643675-9e7e-4581-8ff8-ead4047e3234",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Costa Rica",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2006 round of surveys.  The 2006 survey was conducted by Vanderbilt University, and the field work was carried out by Central American Population Center (CCP) of the University of Costa Rica.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2006"
                 }
             ],
+            "identifier": "0b643675-9e7e-4581-8ff8-ead4047e3234",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Costa Rica"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/CostaRica_06_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Costa Rica",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2006"
         },
         {
             "accessLevel": "public",
@@ -1882,51 +1882,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2006 round of surveys.  The 2006 survey was conducted by Vanderbilt University, and the field work was carried out by Gallup Dominican Republic, S.A.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Dominican Republic"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "d5b11ae8-e419-4933-b743-aa2ddcf1d953",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Dominican Republic",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2006 round of surveys.  The 2006 survey was conducted by Vanderbilt University, and the field work was carried out by Gallup Dominican Republic, S.A.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2006"
                 }
             ],
+            "identifier": "d5b11ae8-e419-4933-b743-aa2ddcf1d953",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Dominican Republic"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_06_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Dominican Republic",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2006"
         },
         {
             "accessLevel": "public",
@@ -1937,51 +1937,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in El Salvador as part of its 2006 round of surveys.   The 2006 survey was conducted by Vanderbilt University and IUDOP-UCA.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "ElSalvador"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "07f260ed-5fe1-40cd-a831-de046c88d672",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "ElSalvador",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalavador_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in El Salvador as part of its 2006 round of surveys.   The 2006 survey was conducted by Vanderbilt University and IUDOP-UCA.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalavador_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2006"
                 }
             ],
+            "identifier": "07f260ed-5fe1-40cd-a831-de046c88d672",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "ElSalvador"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalavador_06_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "ElSalvador",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2006"
         },
         {
             "accessLevel": "public",
@@ -1992,51 +1992,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2006 round of surveys.   The 2006 survey was conducted by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Guatemala"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "b70fbd8e-4d72-4b88-bd0a-a3c9a441f3a4",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Guatemala",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2006 round of surveys.   The 2006 survey was conducted by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2006"
                 }
             ],
+            "identifier": "b70fbd8e-4d72-4b88-bd0a-a3c9a441f3a4",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Guatemala"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_06_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Guatemala",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2006"
         },
         {
             "accessLevel": "public",
@@ -2047,19 +2047,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2006 of round surveys.   The 2006 survey was conducted by Vanderbilt University and the Institute of Development Studies (IDS) of the University of Guyana funded by USAID.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2006",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guyana_codebook_LAPOP_americasbarometer_2007.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2006 round of surveys.  The 2006 survey was conducted by Vanderbilt University and the Institute of Development Studies (IDS) of the University of Guyana funded by USAID.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guyana_Data_LAPOP_americasbarometer_2007.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2006"
+                }
+            ],
+            "identifier": "4aec1ccc-3bd1-4207-b103-09b1490aa954",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Guyana"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "4aec1ccc-3bd1-4207-b103-09b1490aa954",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -2067,31 +2080,18 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/Guyana_06_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
+                "http://www.usaid.gov/opengov/developer/datasets/Guyana_Tech_Info_LAPOP_americasbarometer_2006.pdf",
+                "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
+            ],
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "spatial": "Guyana",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2006 round of surveys.  The 2006 survey was conducted by Vanderbilt University and the Institute of Development Studies (IDS) of the University of Guyana funded by USAID.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guyana_Data_LAPOP_americasbarometer_2007.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guyana_codebook_LAPOP_americasbarometer_2007.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/Guyana_06_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
-                "http://www.usaid.gov/opengov/developer/datasets/Guyana_Tech_Info_LAPOP_americasbarometer_2006.pdf",
-                "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
-        },
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2006"
+        },
         {
             "accessLevel": "public",
             "bureauCode": [
@@ -2101,51 +2101,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2006 of round surveys.   The 2006 survey was conducted by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Haiti"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "2a9772f0-26d2-44e5-a05a-3a722500b25f",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Haiti",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2006 round of surveys.  The 2006 survey was conducted by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Haiti_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2006"
                 }
             ],
+            "identifier": "2a9772f0-26d2-44e5-a05a-3a722500b25f",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Haiti"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "ht"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Haiti_06_Questionnaire_CREOLE_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Haiti_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Haiti",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2006"
         },
         {
             "accessLevel": "public",
@@ -2156,51 +2156,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Honduras as part of its 2006 round of surveys.   The 2006 survey was conducted by Vanderbilt University and Borge y Asociados",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Honduras"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "22584693-9a3e-44b3-8d5a-96b4e110f95b",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Honduras",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Honduras as part of its 2006 round of surveys.   The 2006 survey was conducted by Vanderbilt University and Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Honduras_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2006"
                 }
             ],
+            "identifier": "22584693-9a3e-44b3-8d5a-96b4e110f95b",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Honduras"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_06_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Honduras",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2006"
         },
         {
             "accessLevel": "public",
@@ -2211,19 +2211,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2006 of round surveys.   The 2006 survey was conducted by the Department of Sociology, Psychology and Social Work of the University of the West Indies (UWI).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2006",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2006 round of surveys.  The 2006 survey was conducted by the Department of Sociology, Psychology and Social Work of the University of the West Indies (UWI).",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Data_LAPOP_americasbarometer_2006.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2006"
+                }
+            ],
+            "identifier": "bdaf2d7a-51be-4672-a05c-cea6a0da6c74",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Jamaica"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "bdaf2d7a-51be-4672-a05c-cea6a0da6c74",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -2231,30 +2244,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Jamaica",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2006 round of surveys.  The 2006 survey was conducted by the Department of Sociology, Psychology and Social Work of the University of the West Indies (UWI).",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Data_LAPOP_americasbarometer_2006.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Jamaica_06_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Jamaica",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2006"
         },
         {
             "accessLevel": "public",
@@ -2265,51 +2265,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Mexico as part of its 2006 round of surveys.   The 2006 survey was conducted by Vanderbilt University and ITAM.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Mexico"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0776f173-7e62-4e2c-a430-b20f6c2d76b9",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Mexico",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Mexico as part of its 2006 round of surveys.   The 2006 survey was conducted by Vanderbilt University and ITAM.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Mexico_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2006"
                 }
             ],
+            "identifier": "0776f173-7e62-4e2c-a430-b20f6c2d76b9",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Mexico"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_06_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Mexico",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2006"
         },
         {
             "accessLevel": "public",
@@ -2320,51 +2320,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Nicaragua as part of its 2006 round of surveys.   The 2006 survey was conducted by Vanderbilt University and Centro de Analisis Sociocultural (CASC) of the Centroamericana University (UCA) of Nicaragua.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Nicaragua"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "00a3b29b-0dd2-45f6-b036-0bee850f700e",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Nicaragua",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Nicaragua as part of its 2006 round of surveys.   The 2006 survey was conducted by Vanderbilt University and Centro de Analisis Sociocultural (CASC) of the Centroamericana University (UCA) of Nicaragua.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2006"
                 }
             ],
+            "identifier": "00a3b29b-0dd2-45f6-b036-0bee850f700e",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Nicaragua"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_06_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Nicaragua",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2006"
         },
         {
             "accessLevel": "public",
@@ -2375,51 +2375,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2006 round of surveys.   The 2006 survey was conducted by Vanderbilt University and Borge y Asociados",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Panama"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0660b0ba-b9a1-411e-853f-66d1faa83b90",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Panama",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2006 round of surveys.   The 2006 survey was conducted by Vanderbilt University and Borge y Asociados",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Panama_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2006"
                 }
             ],
+            "identifier": "0660b0ba-b9a1-411e-853f-66d1faa83b90",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Panama"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Panama_06_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Panama_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Panama",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2006"
         },
         {
             "accessLevel": "public",
@@ -2430,51 +2430,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Paraguay as part of its 2006 of round surveys.   The 2006 survey was conducted by Centro de Informacion y Recursos para el Desarollo (CIRD).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Paraguay"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "fabf68a8-7ace-4550-9f0f-1936b5c44888",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Paraguay",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Paraguay as part of its 2006 round of surveys.  The 2006 survey was conducted by Centro de Informacion y Recursos para el Desarollo (CIRD).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2006"
                 }
             ],
+            "identifier": "fabf68a8-7ace-4550-9f0f-1936b5c44888",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Paraguay"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Paraguay_06_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Paraguay_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Paraguay",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2006"
         },
         {
             "accessLevel": "public",
@@ -2485,51 +2485,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Peru as part of its 2006 of round surveys.   The 2006 survey was conducted by Vanderbilt University with the Instituto de Estudios Peruanos and APOYO Opinion y Mercadeo",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Peru"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "77b37e13-b86a-48e7-b56d-cae9f58771fb",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Peru",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Peru_codebook_LAPOP_americasbarometer_2006.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Peru as part of its 2006 round of surveys.  The 2006 survey was conducted by Vanderbilt University with the Instituto de Estudios Peruanos and APOYO Opinion y Mercadeo.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Peru_Data_LAPOP_americasbarometer_2006.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Peru_codebook_LAPOP_americasbarometer_2006.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2006"
                 }
             ],
+            "identifier": "77b37e13-b86a-48e7-b56d-cae9f58771fb",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Peru"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Peru_06_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Peru_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Peru",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2006"
         },
         {
             "accessLevel": "public",
@@ -2540,51 +2540,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2006-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Uruguay as part of its 2006 of round surveys.   The 2006 survey was conducted by Cifra, Gonzalez Raga & Associates",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Uruguay, 2006",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Uruguay"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "3e46439c-1073-46aa-88ad-bda6415fd229",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Uruguay",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Uruguay_codebook_LAPOP_americasbarometer_2007.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Uruguay as part of its 2006 round of surveys.  The 2006 survey was conducted by Cifra, Gonzalez Raga & Associates.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Uruguay_Data_LAPOP_americasbarometer_2007.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Uruguay, 2006",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Uruguay_codebook_LAPOP_americasbarometer_2007.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Uruguay, 2006"
                 }
             ],
+            "identifier": "3e46439c-1073-46aa-88ad-bda6415fd229",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Uruguay"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2006-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Uruguay_07_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Uruguay_Tech_Info_LAPOP_americasbarometer_2006.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Uruguay",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Uruguay, 2006"
         },
         {
             "accessLevel": "public",
@@ -2595,51 +2595,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-05-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Brazil as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University and Universidade de Brasilia with the field work being done by Cedatos.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2008",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Brazil"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "f540d123-374c-497e-a222-174be87961cf",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Brazil",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Brazil_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Brazil as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University and Universidade de Brasilia with the field work being done by Cedatos.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Brazil_Data_LAPOP_americasbarometer_2008.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Brazil_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2008"
                 }
             ],
+            "identifier": "f540d123-374c-497e-a222-174be87961cf",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Brazil"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "pt"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-05-31",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Brazil_08_Questionnaire_PORT_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Brazil_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Brazil",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2008"
         },
         {
             "accessLevel": "public",
@@ -2650,51 +2650,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2008 round of surveys.  The 2008 survey was conducted by Vanderbilt University, the Central American Population Center (CCP) of the University of Costa Rica and the field work was carried out by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2008",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Costa Rica"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "15dd4891-056b-4957-994f-db4d56a17029",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Costa Rica",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2008 round surveys.  The 2008 survey was conducted by Vanderbilt University, the Central American Population Center (CCP) of the University of Costa Rica and the field work was carried out by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Data_LAPOP_americasbarometer_2008.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2008"
                 }
             ],
+            "identifier": "15dd4891-056b-4957-994f-db4d56a17029",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Costa Rica"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/CostaRica_08_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Costa Rica",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2008"
         },
         {
             "accessLevel": "public",
@@ -2705,51 +2705,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-03-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2008 round of surveys.  The 2008 survey was conducted by Vanderbilt University and the field work was carried out by Gallup Dominican Republic, S.A..",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2008",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Dominican Republic"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "319c8139-ac20-466a-92af-56bf91c8f7df",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Dominican Republic",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2008 of round surveys.  The 2008 survey was conducted by Vanderbilt University and the field work was carried out by Gallup Dominican Republic, S.A..",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Data_LAPOP_americasbarometer_2008.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2008"
                 }
             ],
+            "identifier": "319c8139-ac20-466a-92af-56bf91c8f7df",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Dominican Republic"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-03-31",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_08_Questionnaire_SPAN_LAPOPamericasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Dominican Republic",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2008"
         },
         {
             "accessLevel": "public",
@@ -2760,51 +2760,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in El Salvador as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University and IUDOP-UCA.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2008",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "ElSalvador"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "62549c3b-5326-4bb8-a9ea-5e661e203d7c",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "ElSalvador",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in El Salvador as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University and IUDOP-UCA.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Data_LAPOP_americasbarometer_2008.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2008"
                 }
             ],
+            "identifier": "62549c3b-5326-4bb8-a9ea-5e661e203d7c",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "ElSalvador"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-11-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_08_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "ElSalvador",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2008"
         },
         {
             "accessLevel": "public",
@@ -2815,51 +2815,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-03-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University and Asociacion de Investigacion y Estudios Sociales (ASIES) with funding by USAID.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2008",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Guatemala"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "3c2cf9f6-167c-4acc-8396-67ac9d3553c2",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Guatemala",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2008 round surveys.   The 2008 survey was conducted by Vanderbilt University and Asociacion de Investigacion y Estudios Sociales (ASIES) with funding by USAID.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Data_LAPOP_americasbarometer_2008.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2008"
                 }
             ],
+            "identifier": "3c2cf9f6-167c-4acc-8396-67ac9d3553c2",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Guatemala"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-03-31",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_08_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Guatemala",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2008"
         },
         {
             "accessLevel": "public",
@@ -2870,19 +2870,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2009-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2008 of round surveys.   The 2008 survey was conducted by Vanderbilt University funded by USAID.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2008",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guyana_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2008 round of surveys.  The 2008 survey was conducted by Vanderbilt University funded by USAID.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guyana_Data_LAPOP_americasbarometer_2008.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2008"
+                }
+            ],
+            "identifier": "224af625-28ff-4d8e-9b66-beb2f25e5d05",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Guyana"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "224af625-28ff-4d8e-9b66-beb2f25e5d05",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2009-11-30",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -2890,30 +2903,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Guyana",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2008 round of surveys.  The 2008 survey was conducted by Vanderbilt University funded by USAID.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guyana_Data_LAPOP_americasbarometer_2008.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guyana_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Guyana_08_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Guyana_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Guyana",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2008"
         },
         {
             "accessLevel": "public",
@@ -2924,19 +2924,33 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-11-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2008 of round surveys.   The 2008 survey was conducted by Vanderbilt University and Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2008",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2008 round of surveys.  The 2008 survey was conducted by Vanderbilt University and Borge y Asociados.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Haiti_Data_LAPOP_americasbarometer_2008.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2008"
+                }
+            ],
+            "identifier": "fcd88fe7-3219-4848-b94c-150e0640afaf",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Haiti"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "fcd88fe7-3219-4848-b94c-150e0640afaf",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US",
+                "ht"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-11-30",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -2944,31 +2958,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Haiti",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2008 round of surveys.  The 2008 survey was conducted by Vanderbilt University and Borge y Asociados.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Haiti_Data_LAPOP_americasbarometer_2008.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US",
-                "ht"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Haiti_08_Questionnaire_CREOLE_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Haiti_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Haiti",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2008"
         },
         {
             "accessLevel": "public",
@@ -2979,51 +2979,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Honduras as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University and Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2008",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Honduras"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "80f876ee-0755-40c6-ada8-9b285fbf3260",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Honduras",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Honduras as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University and Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Honduras_Data_LAPOP_americasbarometer_2008.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2008"
                 }
             ],
+            "identifier": "80f876ee-0755-40c6-ada8-9b285fbf3260",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Honduras"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_08_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Honduras",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2008"
         },
         {
             "accessLevel": "public",
@@ -3034,19 +3034,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-03-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2008 of round surveys.   The 2008 survey was conducted by Vanderbilt University and the Center for Leadership and Governance of the University of the West Indies (UWI) with funding by USAID.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2008",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2008 round of surveys.  The 2008 survey was conducted by Vanderbilt University and the Center for Leadership and Governance of the University of the West Indies (UWI) with funding by USAID.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Data_LAPOP_americasbarometer_2008.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2008"
+                }
+            ],
+            "identifier": "b34011ac-1a2c-44ef-bf34-594949bdeeba",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Jamaica"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "b34011ac-1a2c-44ef-bf34-594949bdeeba",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-03-31",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -3054,30 +3067,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Jamaica",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2008 round of surveys.  The 2008 survey was conducted by Vanderbilt University and the Center for Leadership and Governance of the University of the West Indies (UWI) with funding by USAID.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Data_LAPOP_americasbarometer_2008.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Jamaica_08_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Jamaica",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2008"
         },
         {
             "accessLevel": "public",
@@ -3088,51 +3088,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Mexico as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University and ITAM with field work done by DATA Opinion Publica y Mercados with funding by USAID.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2008",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Mexico"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "8f8bf8f6-dd4d-4eb7-8e09-62a628df6c32",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Mexico",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Mexico as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University and ITAM with field work done by DATA Opinion Publica y Mercados with funding by USAID.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Mexico_Data_LAPOP_americasbarometer_2008.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2008"
                 }
             ],
+            "identifier": "8f8bf8f6-dd4d-4eb7-8e09-62a628df6c32",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Mexico"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_08_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Mexico",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2008"
         },
         {
             "accessLevel": "public",
@@ -3143,51 +3143,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Nicaragua as part of its 2008 round surveys.   The 2008 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2008",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Nicaragua"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "fd911e52-c063-41b0-89de-b3117c857d39",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Nicaragua",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Nicaragua as part of its 2008 round surveys.   The 2008 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Data_LAPOP_americasbarometer_2008.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2008"
                 }
             ],
+            "identifier": "fd911e52-c063-41b0-89de-b3117c857d39",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Nicaragua"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_08_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Nicaragua",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2008"
         },
         {
             "accessLevel": "public",
@@ -3198,19 +3198,33 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University and Alianza Ciudadana Pro Justicia with field work done by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2008",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometers_2008.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University Alianza Ciudadana Pro Justicia with field work done by Borge y Asociados.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Panama_Data_LAPOP_americasbarometer_2008.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2008"
+                }
+            ],
+            "identifier": "50cde4c1-ea53-4917-b2b2-d565c72a5992",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Panama"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "50cde4c1-ea53-4917-b2b2-d565c72a5992",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US",
+                "es"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-02-28",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -3218,32 +3232,18 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/Panama_08_Questionnaire_SPAN_LAPOP_americasbarometer%20revised.pdf",
+                "http://www.usaid.gov/opengov/developer/datasets/Panama_Tech_Info_LAPOP_americasbarometer_2008.pdf",
+                "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
+            ],
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "spatial": "Panama",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2008 round of surveys.   The 2008 survey was conducted by Vanderbilt University Alianza Ciudadana Pro Justicia with field work done by Borge y Asociados.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Panama_Data_LAPOP_americasbarometer_2008.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometers_2008.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US",
-                "es"
-            ],
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/Panama_08_Questionnaire_SPAN_LAPOP_americasbarometer%20revised.pdf",
-                "http://www.usaid.gov/opengov/developer/datasets/Panama_Tech_Info_LAPOP_americasbarometer_2008.pdf",
-                "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
-        },
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2008"
+        },
         {
             "accessLevel": "public",
             "bureauCode": [
@@ -3253,51 +3253,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Paraguay as part of its 2008 of round surveys.   The 2008 survey was conducted by Vanderbilt University and Centro de Informacion y Recursos para el Desarollo (CIRD).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2008",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Paraguay"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "bd5022ed-6407-4a1f-a6d5-f1ad1da00c78",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Paraguay",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Paraguay as part of its 2008 round of surveys.  The 2008 survey was conducted by Vanderbilt University and Centro de Informacion y Recursos para el Desarollo (CIRD).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_Data_LAPOP_americasbarometer_2008.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2008"
                 }
             ],
+            "identifier": "bd5022ed-6407-4a1f-a6d5-f1ad1da00c78",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Paraguay"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Paraguay_08_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Paraguay_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Paraguay",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2008"
         },
         {
             "accessLevel": "public",
@@ -3308,51 +3308,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2008-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Peru as part of its 2008 of round surveys.   The 2008 survey was conducted by Vanderbilt University with the Instituto de Estudios Peruanos and APOYO Opinion y Mercadeo with funding by USAID.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2008",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Peru"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "8922847d-fcb4-4dd8-ad27-d8f3b54c1e30",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Peru",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Peru_codebook_LAPOP_americasbarometer_2008.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Peru as part of its 2008 round of surveys.  The 2008 survey was conducted by Vanderbilt University with the Instituto de Estudios Peruanos and APOYO Opinion y Mercadeo with funding by USAID.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Peru_Data_LAPOP_americasbarometer_2008.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2008",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Peru_codebook_LAPOP_americasbarometer_2008.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2008"
                 }
             ],
+            "identifier": "8922847d-fcb4-4dd8-ad27-d8f3b54c1e30",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Peru"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2008-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Peru_08_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Peru_Tech_Info_LAPOP_americasbarometer_2008.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Peru",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2008"
         },
         {
             "accessLevel": "public",
@@ -3363,51 +3363,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-04-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Brazil as part of its 2010 round of surveys.   The 2010 survey was conducted by Vanderbilt University and Universidade de Brasilia.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Brazil"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "a5a6d7eb-da3d-49e1-be9f-ae891c0ba125",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Brazil",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Brazil_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Brazil as part of its 2010 round of surveys.   The 2010 survey was conducted by Vanderbilt University and Universidade de Brasilia.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Brazil_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Brazil_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2010"
                 }
             ],
+            "identifier": "a5a6d7eb-da3d-49e1-be9f-ae891c0ba125",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Brazil"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "pt"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-04-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Brazil_10_Questionnaire_PORT_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Brazil_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Brazil",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2010"
         },
         {
             "accessLevel": "public",
@@ -3418,51 +3418,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-05-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Colombia as part of its 2010 round surveys.   The 2010 survey was conducted by Vanderbilt University and Universidad de los Andes, and the Observatorio de la Democracia with the field work being carried out by the Centro Nacional de Consultoria.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Colombia"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "45cc3c80-8f2d-49b1-a723-541cd918e8f3",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Colombia",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Colombia_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Colombia as part of its 2010 round surveys.   The 2010 survey was conducted by Vanderbilt University and Universidad de los Andes, and the Observatorio de la Democracia with the field work being carried out by the Centro Nacional de Consultoria.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Colombia_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Colombia_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2010"
                 }
             ],
+            "identifier": "45cc3c80-8f2d-49b1-a723-541cd918e8f3",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Colombia"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-05-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Colombia_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Colombia_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Colombia",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2010"
         },
         {
             "accessLevel": "public",
@@ -3473,19 +3473,33 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2010 round of surveys.  The 2010 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2010",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2010 round surveys.  The 2010 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Data_LAPOP_americasbarometer_2010.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2010"
+                }
+            ],
+            "identifier": "47c563f0-7495-4cf3-b809-723241873439",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Costa Rica"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "47c563f0-7495-4cf3-b809-723241873439",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US",
+                "es"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-02-28",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -3493,32 +3507,18 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/CostaRica_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
+                "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Tech_Info_LAPOP_americasbarometer_2010.pdf",
+                "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
+            ],
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "spatial": "Costa Rica",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2010 round surveys.  The 2010 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Data_LAPOP_americasbarometer_2010.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US",
-                "es"
-            ],
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/CostaRica_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
-                "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Tech_Info_LAPOP_americasbarometer_2010.pdf",
-                "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
-        },
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2010"
+        },
         {
             "accessLevel": "public",
             "bureauCode": [
@@ -3528,51 +3528,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-03-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2010 round of surveys.  The 2010 survey was conducted by Vanderbilt University and the field work was carried out by Gallup Dominican Republic, S.A.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Dominican Republic"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "acbae5ea-360f-4e7f-ab3a-864efae0bc60",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Dominican Republic",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2010 of round surveys.  The 2010 survey was conducted by Vanderbilt University and the field work was carried out by Gallup Dominican Republic, S.A.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2010"
                 }
             ],
+            "identifier": "acbae5ea-360f-4e7f-ab3a-864efae0bc60",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Dominican Republic"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-03-31",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Dominican Republic",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2010"
         },
         {
             "accessLevel": "public",
@@ -3583,51 +3583,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-03-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Ecuador as part of its 2010 round surveys.   The 2010 survey was conducted by Vanderbilt University and Cedatos.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Ecuador"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "f10803ad-692f-4917-9bd4-4f17c56dbe07",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Ecuador",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Ecuador_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Ecuador as part of its 2010 round surveys.   The 2010 survey was conducted by Vanderbilt University and Cedatos.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Ecuador_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Ecuador_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2010"
                 }
             ],
+            "identifier": "f10803ad-692f-4917-9bd4-4f17c56dbe07",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Ecuador"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-03-31",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Ecuador_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Ecuador_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Ecuador",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2010"
         },
         {
             "accessLevel": "public",
@@ -3638,51 +3638,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-03-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in El Salvador as part of its 2010 round of surveys.   The 2010 survey was conducted by Vanderbilt University and IUDOP-UCA.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "ElSalvador"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "f95e5430-f3c4-4a00-bdf8-1010fb572861",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "ElSalvador",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in El Salvador as part of its 2010 round of surveys.   The 2010 survey was conducted by Vanderbilt University and IUDOP-UCA.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2010"
                 }
             ],
+            "identifier": "f95e5430-f3c4-4a00-bdf8-1010fb572861",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "ElSalvador"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-03-31",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "ElSalvador",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2010"
         },
         {
             "accessLevel": "public",
@@ -3693,51 +3693,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-03-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2010 round of surveys.   The 2010 survey was conducted by Vanderbilt University and Asociacion de Investigacion y Estudios Sociales (ASIES).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Guatemala"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "ee33ffab-c5ca-427d-bf7a-b2c322adcf23",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Guatemala",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2010 round surveys.   The 2010 survey was conducted by Vanderbilt University and Asociacion de Investigacion y Estudios Sociales (ASIES).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2010"
                 }
             ],
+            "identifier": "ee33ffab-c5ca-427d-bf7a-b2c322adcf23",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Guatemala"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-03-31",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Guatemala",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2010"
         },
         {
             "accessLevel": "public",
@@ -3748,19 +3748,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2009-03-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2010 of round surveys.   The 2010 survey was conducted by Vanderbilt University with the field work being carried out by Development Policy and Management Consultants (DPMC).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2010",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guyana_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2010 round of surveys.  The 2010 survey was conducted by Vanderbilt University with the field work being carried out by Development Policy and Management Consultants (DPMC).",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guyana_Data_LAPOP_americasbarometer_2010.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2010"
+                }
+            ],
+            "identifier": "95152ac3-c36a-4530-95d3-0a559e05742e",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Guyana"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "95152ac3-c36a-4530-95d3-0a559e05742e",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2009-03-31",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -3768,30 +3781,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Guyana",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2010 round of surveys.  The 2010 survey was conducted by Vanderbilt University with the field work being carried out by Development Policy and Management Consultants (DPMC).",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guyana_Data_LAPOP_americasbarometer_2010.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guyana_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Guyana_10_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Guyana_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Guyana",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2010"
         },
         {
             "accessLevel": "public",
@@ -3802,19 +3802,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-08-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2010 of round surveys.   The 2010 survey was conducted by Vanderbilt University with the field work being carried out by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2010",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2010 round of surveys.  The 2010 survey was conducted by Vanderbilt University with the field work being carried out by Borge y Asociados.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Haiti_Data_LAPOP_americasbarometer_2010.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2010"
+                }
+            ],
+            "identifier": "a53d7e2c-8835-41aa-8648-4daad57c9fea",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Haiti"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "a53d7e2c-8835-41aa-8648-4daad57c9fea",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-08-30",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -3822,30 +3835,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Haiti",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2010 round of surveys.  The 2010 survey was conducted by Vanderbilt University with the field work being carried out by Borge y Asociados.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Haiti_Data_LAPOP_americasbarometer_2010.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Haiti_10_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Haiti_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Haiti",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2010"
         },
         {
             "accessLevel": "public",
@@ -3856,51 +3856,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Honduras as part of its 2010 round of surveys.   The field work for the 2010 survey was Field work by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Honduras"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "cb585702-4349-4f80-8f6c-b4e0da0c8dab",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Honduras",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Honduras as part of its 2010 round of surveys.  The field work for the 2010 survey was Field work by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Honduras_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2010"
                 }
             ],
+            "identifier": "cb585702-4349-4f80-8f6c-b4e0da0c8dab",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Honduras"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Honduras",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2010"
         },
         {
             "accessLevel": "public",
@@ -3911,19 +3911,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-03-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2010 of round surveys.   The 2010 survey was conducted by Vanderbilt University and the Center for Leadership and Governance of the University of the West Indies (UWI).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2010",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2010 round of surveys.  The 2010 survey was conducted by Vanderbilt University and the Center for Leadership and Governance of the University of the West Indies (UWI).",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Data_LAPOP_americasbarometer_2010.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2010"
+                }
+            ],
+            "identifier": "3925daca-1956-497f-8556-d72b8fbc6057",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Jamaica"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "3925daca-1956-497f-8556-d72b8fbc6057",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-03-31",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -3931,30 +3944,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Jamaica",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2010 round of surveys.  The 2010 survey was conducted by Vanderbilt University and the Center for Leadership and Governance of the University of the West Indies (UWI).",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Data_LAPOP_americasbarometer_2010.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Jamaica_10_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Jamaica",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2010"
         },
         {
             "accessLevel": "public",
@@ -3965,51 +3965,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Mexico as part of its 2010 round of surveys.   The 2010 survey was conducted by Vanderbilt University and ITAM with field work done by DATA Opinion Publica y Mercados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Mexico"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "5b1bc0af-e2e0-4d45-8704-1ccb4e84b230",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Mexico",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Mexico as part of its 2010 round of surveys.   The 2010 survey was conducted by Vanderbilt University and ITAM with field work done by DATA Opinion Publica y Mercados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Mexico_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2010"
                 }
             ],
+            "identifier": "5b1bc0af-e2e0-4d45-8704-1ccb4e84b230",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Mexico"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Mexico",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2010"
         },
         {
             "accessLevel": "public",
@@ -4020,51 +4020,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Nicaragua as part of its 2010 round surveys.   The 2010 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Nicaragua"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "9217af91-2953-401e-b17c-7637afc3617c",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Nicaragua",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Nicaragua as part of its 2010 round surveys.   The 2010 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2010"
                 }
             ],
+            "identifier": "9217af91-2953-401e-b17c-7637afc3617c",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Nicaragua"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Nicaragua",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2010"
         },
         {
             "accessLevel": "public",
@@ -4075,19 +4075,33 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2010 round of surveys.   The 2010 survey was conducted by Vanderbilt University and Alianza Ciudadana Pro Justicia with field work done by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2010",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2010 round of surveys.   The 2010 survey was conducted by Vanderbilt University and Alianza Ciudadana Pro Justicia with field work done by Borge y Asociados.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Panama_Data_LAPOP_americasbarometer_2010.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2010"
+                }
+            ],
+            "identifier": "23c7d329-8043-4407-b64a-0e3e7e4c6b71",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Panama"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "23c7d329-8043-4407-b64a-0e3e7e4c6b71",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US",
+                "es"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-02-28",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -4095,31 +4109,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Panama",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2010 round of surveys.   The 2010 survey was conducted by Vanderbilt University and Alianza Ciudadana Pro Justicia with field work done by Borge y Asociados.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Panama_Data_LAPOP_americasbarometer_2010.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US",
-                "es"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Panama_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Panama_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Panama",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2010"
         },
         {
             "accessLevel": "public",
@@ -4130,51 +4130,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Paraguay as part of its 2010 of round surveys.   The 2010 survey was conducted by Vanderbilt University and Centro de Informacion y Recursos para el Desarollo (CIRD).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Paraguay"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "15e5c291-a3e3-4bac-9e2c-a390fabaff4f",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Paraguay",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Paraguay as part of its 2010 round of surveys.  The 2010 survey was conducted by Vanderbilt University and Centro de Informacion y Recursos para el Desarollo (CIRD).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2010"
                 }
             ],
+            "identifier": "15e5c291-a3e3-4bac-9e2c-a390fabaff4f",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Paraguay"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Paraguay_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Paraguay_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Paraguay",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2010"
         },
         {
             "accessLevel": "public",
@@ -4185,51 +4185,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2010-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Peru as part of its 2010 of round surveys.   The 2010 survey was conducted by Vanderbilt University with the Instituto de Estudios Peruanos and APOYO Opinion y Mercadeo with funding by USAID.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2010",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Peru"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "13602c2c-5aef-4526-94c9-faa462d1af06",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Peru",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Peru_codebook_LAPOP_americasbarometer_2010.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Peru as part of its 2010 round of surveys.  The 2010 survey was conducted by Vanderbilt University with the Instituto de Estudios Peruanos and APOYO Opinion y Mercadeo with funding by USAID.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Peru_Data_LAPOP_americasbarometer_2010.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2010",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Peru_codebook_LAPOP_americasbarometer_2010.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2010"
                 }
             ],
+            "identifier": "13602c2c-5aef-4526-94c9-faa462d1af06",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Peru"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2010-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Peru_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Peru_Tech_Info_LAPOP_americasbarometer_2010.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Peru",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2010"
         },
         {
             "accessLevel": "public",
@@ -4240,51 +4240,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-04-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Brazil as part of its 2012 round of surveys.   The 2012 survey was conducted by Vanderbilt University and Universidade de Brasilia.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Brazil"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "9d7e3d2f-2497-4a30-8127-4032eca9e410",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Brazil",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Brazil_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Brazil as part of its 2012 round of surveys.   The 2012 survey was conducted by Vanderbilt University and Universidade de Brasilia.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Brazil_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Brazil_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2012"
                 }
             ],
+            "identifier": "9d7e3d2f-2497-4a30-8127-4032eca9e410",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Brazil"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "pt"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-04-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Brazil_12_Questionnaire_PORT_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Brazil_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Brazil",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Brazil, 2012"
         },
         {
             "accessLevel": "public",
@@ -4295,51 +4295,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-04-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Colombia as part of its 2012 round surveys.   The 2012 survey was conducted by Vanderbilt University and Universidad de los Andes, and the Observatorio de la Democracia with the field work being carried out by the Centro Nacional de Consultoria.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Colombia"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "8222f245-21fc-41f9-b14d-e0cd3a24f7bd",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Colombia",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Colombia_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Colombia as part of its 2012 round surveys.   The 2012 survey was conducted by Vanderbilt University and Universidad de los Andes, and the Observatorio de la Democracia with the field work being carried out by the Centro Nacional de Consultoria.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Colombia_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Colombia_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2012"
                 }
             ],
+            "identifier": "8222f245-21fc-41f9-b14d-e0cd3a24f7bd",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Colombia"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-04-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Colombia_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Colombia_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Colombia",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Colombia, 2012"
         },
         {
             "accessLevel": "public",
@@ -4350,106 +4350,106 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-02-29",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2012 round of surveys.  The 2012 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Costa Rica"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "ec85c0c1-ed29-4402-a621-5c8f7f8298d4",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Costa Rica",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Costa Rica as part of its 2012 round surveys.  The 2012 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/CostaRica_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2012"
                 }
             ],
+            "identifier": "ec85c0c1-ed29-4402-a621-5c8f7f8298d4",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Costa Rica"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-02-29",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/CostaRica_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/CostaRica_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Costa Rica",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Costa Rica, 2012"
         },
         {
             "accessLevel": "public",
             "bureauCode": [
-                "184:15"
-            ],
-            "contactPoint": {
-                "fn": "Joe Cabino",
-                "hasEmail": "mailto:opendata@usaid.gov"
-            },
-            "modified": "2012-02-28",
-            "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2012 round of surveys.  The 2012 survey was conducted by Vanderbilt University and the field work was carried out by Gallup Dominican Republic, S.A.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Dominican Republic"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0e408334-b521-4db5-8341-0f6dc98cf287",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
+                "184:15"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Dominican Republic",
+            "contactPoint": {
+                "fn": "Joe Cabino",
+                "hasEmail": "mailto:opendata@usaid.gov"
+            },
+            "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2012 round of surveys.  The 2012 survey was conducted by Vanderbilt University and the field work was carried out by Gallup Dominican Republic, S.A.",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Dominican Republic as part of its 2012 of round surveys.  The 2012 survey was conducted by Vanderbilt University and the field work was carried out by Gallup Dominican Republic, S.A.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2012"
                 }
             ],
+            "identifier": "0e408334-b521-4db5-8341-0f6dc98cf287",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Dominican Republic"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/DominicanRepublic_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Dominican Republic",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Dominican Republic, 2012"
         },
         {
             "accessLevel": "public",
@@ -4460,51 +4460,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Ecuador as part of its 2012 round surveys.   The 2012 survey was conducted by Vanderbilt University with the field work carried out by Prime Consulting.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Ecuador"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "4e60d952-6d96-40bb-a000-1ca62a646f03",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Ecuador",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Ecuador_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Ecuador as part of its 2012 round surveys.   The 2012 survey was conducted by Vanderbilt University with the field work carried out by Prime Consulting.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Ecuador_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Ecuador_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2012"
                 }
             ],
+            "identifier": "4e60d952-6d96-40bb-a000-1ca62a646f03",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Ecuador"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Ecuador_10_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Ecuador_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Ecuador",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Ecuador, 2012"
         },
         {
             "accessLevel": "public",
@@ -4515,51 +4515,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-05-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in El Salvador as part of its 2012 round of surveys.   The 2012 survey was conducted by Vanderbilt University and FUNDAUNGO.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "ElSalvador"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "ea26df8e-55b8-45d5-8c27-82ef36d12ace",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "ElSalvador",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in El Salvador as part of its 2012 round of surveys.   The 2012 survey was conducted by Vanderbilt University and FUNDAUNGO.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2012"
                 }
             ],
+            "identifier": "ea26df8e-55b8-45d5-8c27-82ef36d12ace",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "ElSalvador"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-05-31",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/ElSalvador_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "ElSalvador",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-El Salvador, 2012"
         },
         {
             "accessLevel": "public",
@@ -4570,51 +4570,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-04-30",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2012 round of surveys.   The 2012 survey was conducted by Vanderbilt University and Asociacion de Investigacion y Estudios Sociales (ASIES).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Guatemala"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "5287dde8-de98-4830-96f4-d6a32ea3d62c",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Guatemala",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guatemala as part of its 2012 round surveys.   The 2012 survey was conducted by Vanderbilt University and Asociacion de Investigacion y Estudios Sociales (ASIES).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guatemala_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2012"
                 }
             ],
+            "identifier": "5287dde8-de98-4830-96f4-d6a32ea3d62c",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Guatemala"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-04-30",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Guatemala_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Guatemala",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guatemala, 2012"
         },
         {
             "accessLevel": "public",
@@ -4625,19 +4625,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2009-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2012 of round surveys.   The 2012 survey was conducted by Vanderbilt University with the field work being carried out by Development Policy and Management Consultants (DPMC).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2012",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guyana_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2012 round of surveys.  The 2012 survey was conducted by Vanderbilt University with the field work being carried out by Development Policy and Management Consultants (DPMC).",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guyana_Data_LAPOP_americasbarometer_2012.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2012"
+                }
+            ],
+            "identifier": "78e878fa-610a-41aa-a659-54bb4a24b227",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Guyana"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "78e878fa-610a-41aa-a659-54bb4a24b227",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2009-02-28",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -4645,30 +4658,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Guyana",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Guyana as part of its 2012 round of surveys.  The 2012 survey was conducted by Vanderbilt University with the field work being carried out by Development Policy and Management Consultants (DPMC).",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Guyana_Data_LAPOP_americasbarometer_2012.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Guyana_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Guyana_12_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Guyana_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Guyana",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Guyana, 2012"
         },
         {
             "accessLevel": "public",
@@ -4677,52 +4677,52 @@
             ],
             "contactPoint": {
                 "fn": "Joe Cabino",
-                "hasEmail": "mailto:opendata@usaid.gov"
-            },
-            "modified": "2012-02-28",
-            "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2012 of round surveys.   The 2012 survey was conducted by Vanderbilt University with the field work being carried out by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Haiti"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "70a02773-214b-48bb-8591-15557ecec92d",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Haiti",
+                "hasEmail": "mailto:opendata@usaid.gov"
+            },
+            "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2012 of round surveys.   The 2012 survey was conducted by Vanderbilt University with the field work being carried out by Borge y Asociados.",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Haiti as part of its 2012 round of surveys.  The 2012 survey was conducted by Vanderbilt University with the field work being carried out by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Haiti_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2012"
                 }
             ],
+            "identifier": "70a02773-214b-48bb-8591-15557ecec92d",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Haiti"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Haiti_12_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Haiti_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Haiti",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Haiti, 2012"
         },
         {
             "accessLevel": "public",
@@ -4733,51 +4733,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Honduras as part of its 2012 round of surveys.   The field work for the 2012 survey was done by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Honduras"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "2e64ce0f-9cf3-423c-bd00-6cec8579fdb3",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Honduras",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Honduras as part of its 2012 round of surveys.  The field work for the 2012 survey was done by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Honduras_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Honduras_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2012"
                 }
             ],
+            "identifier": "2e64ce0f-9cf3-423c-bd00-6cec8579fdb3",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Honduras"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Honduras_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Honduras",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Honduras, 2012"
         },
         {
             "accessLevel": "public",
@@ -4788,19 +4788,32 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-05-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2012 of round surveys.   The 2012 survey was conducted by The University of the West Indies (UWI).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2012",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2012 round of surveys.  The 2012 survey was conducted by The University of the West Indies (UWI).",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Data_LAPOP_americasbarometer_2012.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2012"
+                }
+            ],
+            "identifier": "af4ad6f0-0440-4f33-9923-373f9a579f8d",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
             "keyword": [
                 "Opinion Survey",
                 "Crime",
                 "Corruption",
                 "Jamaica"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "af4ad6f0-0440-4f33-9923-373f9a579f8d",
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-05-31",
             "programCode": [
                 "184:008",
                 "184:010",
@@ -4808,30 +4821,17 @@
                 "184:031",
                 "184:033"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Jamaica",
-            "distribution": [
-                {
-                    "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Jamaica as part of its 2012 round of surveys.  The 2012 survey was conducted by The University of the West Indies (UWI).",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Data_LAPOP_americasbarometer_2012.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Jamaica_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Jamaica_12_Questionnaire_ENG_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Jamaica_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Jamaica",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Jamaica, 2012"
         },
         {
             "accessLevel": "public",
@@ -4842,51 +4842,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Mexico as part of its 2012 round of surveys.   The 2012 survey was conducted by Vanderbilt University with field work done by DATA Opinion Publica y Mercados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Mexico"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "2f926f13-2272-4e56-9361-b7237f8c45b0",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Mexico",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Mexico as part of its 2012 round of surveys.   The 2012 survey was conducted by Vanderbilt University with field work done by DATA Opinion Publica y Mercados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Mexico_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Mexico_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2012"
                 }
             ],
+            "identifier": "2f926f13-2272-4e56-9361-b7237f8c45b0",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Mexico"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Mexico_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Mexico",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Mexico, 2012"
         },
         {
             "accessLevel": "public",
@@ -4897,51 +4897,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Nicaragua as part of its 2012 round surveys.   The 2012 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Nicaragua"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "c4f8a5a3-0f4c-43e9-935b-78a75cf31478",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Nicaragua",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Nicaragua as part of its 2012 round surveys.   The 2012 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2012"
                 }
             ],
+            "identifier": "c4f8a5a3-0f4c-43e9-935b-78a75cf31478",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Nicaragua"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Nicaragua_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Nicaragua",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Nicaragua, 2012"
         },
         {
             "accessLevel": "public",
@@ -4952,51 +4952,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-03-31",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2012 round of surveys.   The 2012 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Panama"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "7a804bec-214c-46a5-bce1-7584a47a1e4b",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Panama",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Panama as part of its 2012 round of surveys.   The 2012 survey was conducted by Vanderbilt University with field work done by Borge y Asociados.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Panama_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Panama_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2012"
                 }
             ],
-            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "identifier": "7a804bec-214c-46a5-bce1-7584a47a1e4b",
+            "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Panama"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-03-31",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Panama_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Panama_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Panama",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Panama, 2012"
         },
         {
             "accessLevel": "public",
@@ -5007,51 +5007,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Paraguay as part of its 2012 of round surveys.   The 2012 survey was conducted by Vanderbilt University and Centro de Informacion y Recursos para el Desarollo (CIRD).",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Paraguay"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "51fa62f7-a5a5-4659-8a8f-ebf26ebe0e56",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Paraguay",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Paraguay as part of its 2012 round of surveys.  The 2012 survey was conducted by Vanderbilt University and Centro de Informacion y Recursos para el Desarollo (CIRD).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Paraguay_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2012"
                 }
             ],
+            "identifier": "51fa62f7-a5a5-4659-8a8f-ebf26ebe0e56",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Paraguay"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Paraguay_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Paraguay_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Paraguay",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Paraguay, 2012"
         },
         {
             "accessLevel": "public",
@@ -5062,39 +5062,39 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-11-24",
             "description": "Statistical data on the number of downloads from USAID's Development Data Library (DDL) at www.usaid.gov/data from March 1, 2015 to November 14, 2015.",
-            "title": "Development Data Library (DDL) Download Statistics",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DDLDownLoadStatsCodebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
+                    "description": "Statistical data on the number of downloads from USAID's Development Data Library (DDL) at www.usaid.gov/data from March 1, 2015 to November 14, 2015.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DDLDownLoadStats_2015_03_01-2015_11_14.ods",
+                    "format": "ODS",
+                    "mediaType": "application/vnd.oasis.opendocument.spreadsheet",
+                    "title": "Development Data Library (DDL) Download Statistics"
+                }
+            ],
+            "identifier": "8f6d860a-f16f-448a-b06e-24ac6364e555",
             "keyword": [
                 "DDL",
                 "Development Data Library",
                 "download statistics"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "8f6d860a-f16f-448a-b06e-24ac6364e555",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2015-11-24",
             "programCode": [
                 "184:029",
                 "184:019",
                 "184:031",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "distribution": [
-                {
-                    "description": "Statistical data on the number of downloads from USAID's Development Data Library (DDL) at www.usaid.gov/data from March 1, 2015 to November 14, 2015.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DDLDownLoadStats_2015_03_01-2015_11_14.ods",
-                    "format": "ODS",
-                    "mediaType": "application/vnd.oasis.opendocument.spreadsheet",
-                    "title": "Development Data Library (DDL) Download Statistics",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/DDLDownLoadStatsCodebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
-                }
-            ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "name": "USAID"
+            },
+            "title": "Development Data Library (DDL) Download Statistics"
         },
         {
             "accessLevel": "public",
@@ -5105,51 +5105,51 @@
                 "fn": "Joe Cabino",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-02-28",
             "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Peru as part of its 2012 of round surveys.   The 2012 survey was conducted by Vanderbilt University with the Instituto de Estudios Peruanos",
-            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2012",
-            "keyword": [
-                "Opinion Survey",
-                "Crime",
-                "Corruption",
-                "Peru"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "fe01e7e4-0040-446c-886a-ff90e5dd5180",
-            "programCode": [
-                "184:008",
-                "184:010",
-                "184:022",
-                "184:031",
-                "184:033"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.vanderbilt.edu/lapop/",
-            "spatial": "Peru",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Peru_codebook_LAPOP_americasbarometer_2012.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The Latin America Public Opinion Project (LAPOP) implemented this survey in Peru as part of its 2012 round of surveys.  The 2012 survey was conducted by Vanderbilt University with the Instituto de Estudios Peruanos.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Peru_Data_LAPOP_americasbarometer_2012.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2012",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Peru_codebook_LAPOP_americasbarometer_2012.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2012"
                 }
             ],
+            "identifier": "fe01e7e4-0040-446c-886a-ff90e5dd5180",
             "isPartOf": "0b6672be-b6c2-4669-ac64-86443d7dc3a7",
+            "keyword": [
+                "Opinion Survey",
+                "Crime",
+                "Corruption",
+                "Peru"
+            ],
+            "landingPage": "http://www.vanderbilt.edu/lapop/",
             "language": [
                 "en-US",
                 "es"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-02-28",
+            "programCode": [
+                "184:008",
+                "184:010",
+                "184:022",
+                "184:031",
+                "184:033"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Peru_12_Questionnaire_SPAN_LAPOP_americasbarometer.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Peru_Tech_Info_LAPOP_americasbarometer_2012.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pdacu123.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Peru",
+            "title": "The AmericasBarometer by the Latin American Public Opinion Project (LAPOP)-Peru, 2012"
         },
         {
             "accessLevel": "public",
@@ -5160,9 +5160,8 @@
                 "fn": "Jill Moss",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-04-27",
             "description": "USAID's Office of Food for Peace (FFP) awards funding to private voluntary organizations (PVOs) to design and implement multi-year Title II development food assistance programs.  The main purpose of the Title II program is to improve long-term food security of chronically food insecure population in the targeted regions. As countries start new programs, USAID conducts baseline surveys to assess the current status of key indicators, develop a better understanding of prevailing conditions and perceptions of the population in the targeted areas, and serve as a point of comparison for future final evaluations.  Results are also used to further refine program targeting and, where possible, to understand the relationship between variables to inform program design.",
-            "title": "Collection of Baseline Studies of the Food for Peace Title II Development Food Assistance Programs",
+            "identifier": "beb742b0-7da7-4258-bb28-7e9fdf794851",
             "keyword": [
                 "Baseline Survey",
                 "Food for Peace",
@@ -5170,10 +5169,12 @@
                 "Title II Development Program",
                 "Food Security"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "beb742b0-7da7-4258-bb28-7e9fdf794851",
+            "landingPage": "http://www.usaid.gov/developer/FFPBaselineStudies",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2012-04-27",
             "programCode": [
                 "184:016",
                 "184:018",
@@ -5181,14 +5182,15 @@
                 "184:029",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.usaid.gov/developer/FFPBaselineStudies",
-            "language": [
-                "en-US"
-            ]
+            "title": "Collection of Baseline Studies of the Food for Peace Title II Development Food Assistance Programs"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00009",
+            "USAIDsubmittingOrganization": "ICF International, Inc",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -5197,124 +5199,79 @@
                 "fn": "Jill Moss",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-10-15",
             "description": "In fiscal year 2012, USAID's Office of Food for Peace (FFP) awarded funding to private voluntary organizations (PVOs) to design and implement a multi-year Title II development food assistance program in Uganda. The main purpose of the Title II program is to improve long-term food security of chronically food insecure population in the target regions. FFP contracted a firm, ICF International to conduct a baseline study in targeted areas of the country prior to the start of the new program.  The purpose of the study was to assess the current status of key indicators, have a better understanding of prevailing conditions and perceptions of the population in the implementation areas, and serve as a point of comparison for future final evaluations.  Results would also be used to further refine program targeting and, where possible, to understand the relationship between variables to inform program design.  The study was conducted in 2013, while FFP expects to conduct final evaluations as close as possible to the end of the program five years later.",
-            "title": "Baseline Study of Food for Peace Title II Development Food Assistance Program in Uganda",
-            "keyword": [
-                "Uganda",
-                "Baseline Survey",
-                "Food for Peace",
-                "FFP",
-                "Title II Development Program",
-                "Food Security",
-                "Karamoja"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "3c32504d-ffba-46c9-8c7b-30449def4143",
-            "programCode": [
-                "184:016",
-                "184:018",
-                "184:019",
-                "184:029",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.usaid.gov/developer/FFPBaselineStudies",
-            "spatial": "Uganda",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Agric_Practices_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on agricultural practices in Karamoja, Uganda",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Agric%20Practices_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Uganda Agricultural Practices Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Agric_Practices_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Uganda Agricultural Practices Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Child_Health_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on child health in Karamoja, Uganda",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Child%20Health_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Uganda Child Health Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Child_Health_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Uganda Child Health Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Food_Consumption_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on food consumption in Karamoja, Uganda",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Food%20Consumption_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Uganda Food Consumption Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Food_Consumption_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Uganda Food Consumption Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_HH_Description_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data describing the households in Karamoja, Uganda",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Uganda_HH%20Description_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Uganda Household Description Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_HH_Description_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Uganda Household Description Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Maternal_Health_and_HH_Sanitation_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on maternal health and household sanitation in Karamoja, Uganda",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Maternal%20Health%20and%20HH%20Sanitation_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Uganda Maternal Health and Household Sanitation Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_Maternal_Health_and_HH_Sanitation_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Uganda Maternal Health and Household Sanitation Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_weights_description.csv",
                     "description": "Data on the anthropometry of mothers and children in Karamoja, Uganda",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Uganda_weights_annotated.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Uganda Mother and Child Anthropometry",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_weights_description.csv"
+                    "title": "Uganda Mother and Child Anthropometry"
                 }
             ],
+            "identifier": "3c32504d-ffba-46c9-8c7b-30449def4143",
             "isPartOf": "beb742b0-7da7-4258-bb28-7e9fdf794851",
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "http://pdf.usaid.gov/pdf_docs/pnaed238.pdf"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00009",
-            "USAIDsubmittingOrganization": "ICF International, Inc"
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "184:15"
-            ],
-            "contactPoint": {
-                "fn": "Jill Moss",
-                "hasEmail": "mailto:opendata@usaid.gov"
-            },
-            "modified": "2013-10-15",
-            "description": "In fiscal year 2012, USAID's Office of Food for Peace (FFP) awarded funding to private voluntary organizations (PVOs) to design and implement a multi-year Title II development food assistance program in Guatemala. The main purpose of the Title II program is to improve long-term food security of chronically food insecure population in the target regions. FFP contracted a firm, ICF International to conduct a baseline study in targeted areas of the country prior to the start of the new program.  The purpose of the study was to assess the current status of key indicators, have a better understanding of prevailing conditions and perceptions of the population in the implementation areas, and serve as a point of comparison for future final evaluations.  Results would also be used to further refine program targeting and, where possible, to understand the relationship between variables to inform program design.  The study was conducted in 2013, while FFP expects to conduct final evaluations as close as possible to the end of the program five years later.",
-            "title": "Baseline Study of Food for Peace Title II Development Food Assistance Program in Guatemala",
             "keyword": [
-                "Guatemala",
+                "Uganda",
                 "Baseline Survey",
                 "Food for Peace",
                 "FFP",
                 "Title II Development Program",
                 "Food Security",
-                "Segamil",
-                "Paisano"
+                "Karamoja"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "beafc8ed-c5cf-41a0-84a4-19303c309516",
+            "landingPage": "http://www.usaid.gov/developer/FFPBaselineStudies",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-10-15",
             "programCode": [
                 "184:016",
                 "184:018",
@@ -5322,77 +5279,122 @@
                 "184:029",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.usaid.gov/developer/FFPBaselineStudies",
-            "spatial": "Guatemala",
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://pdf.usaid.gov/pdf_docs/pnaed238.pdf"
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Uganda",
+            "title": "Baseline Study of Food for Peace Title II Development Food Assistance Program in Uganda"
+        },
+        {
+            "USAIDawardNumber": "AID-OAA-M-12-00009",
+            "USAIDsubmittingOrganization": "ICF International, Inc",
+            "accessLevel": "public",
+            "bureauCode": [
+                "184:15"
+            ],
+            "contactPoint": {
+                "fn": "Jill Moss",
+                "hasEmail": "mailto:opendata@usaid.gov"
+            },
+            "description": "In fiscal year 2012, USAID's Office of Food for Peace (FFP) awarded funding to private voluntary organizations (PVOs) to design and implement a multi-year Title II development food assistance program in Guatemala. The main purpose of the Title II program is to improve long-term food security of chronically food insecure population in the target regions. FFP contracted a firm, ICF International to conduct a baseline study in targeted areas of the country prior to the start of the new program.  The purpose of the study was to assess the current status of key indicators, have a better understanding of prevailing conditions and perceptions of the population in the implementation areas, and serve as a point of comparison for future final evaluations.  Results would also be used to further refine program targeting and, where possible, to understand the relationship between variables to inform program design.  The study was conducted in 2013, while FFP expects to conduct final evaluations as close as possible to the end of the program five years later.",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Guat_Agric_Practices_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on agricultural practices in Segamil and Paisano in Guatemala",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Guatemala_Agric%20Practices_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Guatemala Agricultural Practices Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Guat_Agric_Practices_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Guatemala Agricultural Practices Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Guat_Child_Health_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on child health in Segamil and Paisano in Guatemala",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Guatemala_ChildHealth_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Guatemala Child Health Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Guat_Child_Health_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Guatemala Child Health Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Guat_Food_Consumption_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on food consumption in Segamil and Paisano in Guatemala",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Guatemala_Food%20Consumption_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Guatemala Food Consumption Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Guat_Food_Consumption_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Guatemala Food Consumption Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Guat_HH_Description_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data describing the households in Segamil and Paisano in Guatemala",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Guatemala_HH%20Description_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Guatemala Household Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Guat_HH_Description_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Guatemala Household Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Guat_HH_Sanitation_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on maternal Health and household sanitation in Segamil and Paisano in Guatemala",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Guatemala_Maternal%20Health%20and%20HH%20Sanitation_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Guatemala Maternal health and Sanitation Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Guat_HH_Sanitation_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Guatemala Maternal health and Sanitation Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/GUATEMALA_weights_description.csv",
+                    "describedByType": "text/csv",
                     "description": "Data describing the anthropometry in Segamil and Paisano in Guatemala",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/GUATEMALA_weights_annotated.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Guatemala Anthropometry Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/GUATEMALA_weights_description.csv",
-                    "describedByType": "text/csv"
+                    "title": "Guatemala Anthropometry Data"
                 }
             ],
+            "identifier": "beafc8ed-c5cf-41a0-84a4-19303c309516",
             "isPartOf": "beb742b0-7da7-4258-bb28-7e9fdf794851",
+            "keyword": [
+                "Guatemala",
+                "Baseline Survey",
+                "Food for Peace",
+                "FFP",
+                "Title II Development Program",
+                "Food Security",
+                "Segamil",
+                "Paisano"
+            ],
+            "landingPage": "http://www.usaid.gov/developer/FFPBaselineStudies",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-10-15",
+            "programCode": [
+                "184:016",
+                "184:018",
+                "184:019",
+                "184:029",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://pdf.usaid.gov/pdf_docs/pnaed236.pdf"
             ],
-            "USAIDawardNumber": "AID-OAA-M-12-00009",
-            "USAIDsubmittingOrganization": "ICF International, Inc"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Guatemala",
+            "title": "Baseline Study of Food for Peace Title II Development Food Assistance Program in Guatemala"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00009",
+            "USAIDsubmittingOrganization": "ICF International, Inc",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -5401,108 +5403,106 @@
                 "fn": "Jill Moss",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-10-15",
             "description": "In fiscal year 2012, USAID's Office of Food for Peace (FFP) awarded funding to private voluntary organizations (PVOs) to design and implement a multi-year Title II development food assistance program in Niger. The main purpose of the Title II program is to improve long-term food security of chronically food insecure population in the target regions. FFP contracted a firm, ICF International to conduct a baseline study in targeted areas of the country prior to the start of the new program.  The purpose of the study was to assess the current status of key indicators, have a better understanding of prevailing conditions and perceptions of the population in the implementation areas, and serve as a point of comparison for future final evaluations.  Results would also be used to further refine program targeting and, where possible, to understand the relationship between variables to inform program design.  The study was conducted in 2013, while FFP expects to conduct final evaluations as close as possible to the end of the program five years later.",
-            "title": "Baseline Study of Food for Peace Title II Development Food Assistance Program in Niger",
-            "keyword": [
-                "Niger",
-                "Baseline Survey",
-                "Food for Peace",
-                "FFP",
-                "Title II Development Program",
-                "Food Security",
-                "Maradi",
-                "Zinder"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "08ee315f-c339-4c2f-8ae8-8988c9ef05ff",
-            "programCode": [
-                "184:016",
-                "184:018",
-                "184:019",
-                "184:029",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.usaid.gov/developer/FFPBaselineStudies",
-            "spatial": "Niger",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Access%20Health%20Services_Codebook_Values.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on access to health services in Zinder and Maradi in Niger",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Niger_Access%20Health%20Services_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Niger Access to Health Services Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Access%20Health%20Services_Codebook_Values.csv",
-                    "describedByType": "text/csv"
+                    "title": "Niger Access to Health Services Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Agric_Practices_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on agricultural practices in Zinder and Maradi in Niger",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Niger_Agric%20Practices_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Niger Agricultural Practices Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Agric_Practices_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Niger Agricultural Practices Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Child_Health_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on child health in Zinder and Maradi in Niger",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Niger_Child%20Health_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Niger Child Health Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Child_Health_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Niger Child Health Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Food_Consumption_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on food consumption in Zinder and Maradi in Niger",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Niger_Food%20Consumption_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Niger Food Consumption Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Food_Consumption_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Niger Food Consumption Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_HH_Description_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data describing the households in Zinder and Maradi in Niger",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Niger_HH%20Description_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Niger Households Description Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_HH_Description_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Niger Households Description Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Mother_Pregnancy_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data on mothers pregnancy in Zinder and Maradi in Niger",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Niger_Mothers%20Pregnancy_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Niger Mothers Pregnancy Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Mother_Pregnancy_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Niger Mothers Pregnancy Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Sanitation_and_Maternal_Health_Codebook_wValues.csv",
+                    "describedByType": "text/csv",
                     "description": "Data describing sanitation and maternal health in Zinder and Maradi in Niger",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Niger_Sanitation%20and%20Maternal%20Health_Data.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Niger Sanitation and Maternal Health Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Niger_Sanitation_and_Maternal_Health_Codebook_wValues.csv",
-                    "describedByType": "text/csv"
+                    "title": "Niger Sanitation and Maternal Health Data"
                 }
             ],
+            "identifier": "08ee315f-c339-4c2f-8ae8-8988c9ef05ff",
             "isPartOf": "beb742b0-7da7-4258-bb28-7e9fdf794851",
+            "keyword": [
+                "Niger",
+                "Baseline Survey",
+                "Food for Peace",
+                "FFP",
+                "Title II Development Program",
+                "Food Security",
+                "Maradi",
+                "Zinder"
+            ],
+            "landingPage": "http://www.usaid.gov/developer/FFPBaselineStudies",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-10-15",
+            "programCode": [
+                "184:016",
+                "184:018",
+                "184:019",
+                "184:029",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://pdf.usaid.gov/pdf_docs/pnaed237.pdf"
             ],
-            "USAIDawardNumber": "AID-OAA-M-12-00009",
-            "USAIDsubmittingOrganization": "ICF International, Inc"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Niger",
+            "title": "Baseline Study of Food for Peace Title II Development Food Assistance Program in Niger"
         },
         {
             "accessLevel": "public",
@@ -5513,22 +5513,7 @@
                 "fn": "Jay Mahanand",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-08-10",
             "description": "The list of governance boards on which the CIO is a member, playing a role with IT Acquisition when the IT will be used for USAID operations.",
-            "title": "CIO Governance Board Membership List",
-            "keyword": [
-                "FITARA",
-                "CIO Governance",
-                "IT Acquisition"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "2f55567d-6d92-488c-9347-f4bec9b833a7",
-            "programCode": [
-                "184:000"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
             "distribution": [
                 {
                     "description": "The list of governance boards on which the CIO is a member, playing a role with IT Acquisition when the IT will be used for USAID operations.",
@@ -5538,11 +5523,27 @@
                     "title": "CIO Governance Board Membership List"
                 }
             ],
+            "identifier": "2f55567d-6d92-488c-9347-f4bec9b833a7",
+            "keyword": [
+                "FITARA",
+                "CIO Governance",
+                "IT Acquisition"
+            ],
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2015-08-10",
+            "programCode": [
+                "184:000"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "title": "CIO Governance Board Membership List"
         },
         {
+            "USAIDawardNumber": "EM-I-00-07-00005",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -5551,142 +5552,141 @@
                 "fn": "Steven Rozner",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-12-31",
+            "describedByType": "application/pdf",
             "description": "The Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
-            "title": "Collecting Taxes Database",
-            "keyword": [
-                "tax systems",
-                "tax revenues",
-                "VAT rates",
-                "tax system performance"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "cdeb8a1b-3440-4e88-b6cb-81b2428f8cea",
-            "programCode": [
-                "184:027"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2007-2008 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2007-08.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Collecting Taxes Database-2007-2008, CSV Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2007-2008, CSV Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2007-2008 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2007-08.xls",
                     "format": "Excel",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Collecting Taxes Database-2007-2008, EXCEL Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2007-2008, EXCEL Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2008-2009 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2008-09.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Collecting Taxes Database-2008-2009, CSV Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2008-2009, CSV Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2008-2009 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2008-09.xls",
                     "format": "Excel",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Collecting Taxes Database-2008-2009, EXCEL Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2008-2009, EXCEL Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2009-2010 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2009-10.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Collecting Taxes Database-2009-2010, CSV Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2009-2010, CSV Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2009-2010 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2009-10.xls",
                     "format": "Excel",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Collecting Taxes Database-2009-2010, EXCEL Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2009-2010, EXCEL Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2010-2011 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2010-11.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Collecting Taxes Database-2010-2011, CSV Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2010-2011, CSV Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2010-2011 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2010-11.xls",
                     "format": "Excel",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Collecting Taxes Database-2010-2011, EXCEL Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2010-2011, EXCEL Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2011-2012 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2011-12.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Collecting Taxes Database-2011-2012, CSV Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2011-2012, CSV Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2011-2012 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2011-12.xls",
                     "format": "Excel",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Collecting Taxes Database-2011-2012, EXCEL Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2011-2012, EXCEL Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2012-2013 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2012-13.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Collecting Taxes Database-2012-2013, CSV Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2012-2013, CSV Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
+                    "describedByType": "text/csv",
                     "description": "The 2012-2013 Collecting Taxes Database contains performance and structural indicators about national tax systems.  The database contains quantitative revenue performance indicators, such as how well a particular tax performs in generating revenues for the treasury, given its overall rate structure, and how well the overall tax system produces revenues, given the costs of administering the tax system.  The database also provides tax rate information, such as the general VAT rate or the general corporate income tax rate.  Other indicators describe the main features of tax administrations and economic indicators are included so that performance, rate competitiveness, and structure can be compared given the levels of country development and other factors.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes-Full_Data_2012-13.xls",
                     "format": "Excel",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Collecting Taxes Database-2012-2013, EXCEL Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Collecting_Taxes_Geo_and_Income_Codes.csv",
-                    "describedByType": "text/csv"
+                    "title": "Collecting Taxes Database-2012-2013, EXCEL Format"
                 }
             ],
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/Collecting%20Taxes_About%20the%20indicators.pdf"
+            "identifier": "cdeb8a1b-3440-4e88-b6cb-81b2428f8cea",
+            "keyword": [
+                "tax systems",
+                "tax revenues",
+                "VAT rates",
+                "tax system performance"
             ],
-            "describedByType": "application/pdf",
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "EM-I-00-07-00005"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-12-31",
+            "programCode": [
+                "184:027"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/Collecting%20Taxes_About%20the%20indicators.pdf"
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Collecting Taxes Database"
         },
         {
             "accessLevel": "public",
@@ -5697,22 +5697,7 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-02-09",
             "description": "This dataset is the USAID portion of a larger dataset developed by OMB to better understand and to quanity the carbon footprint of the daily commute of government workers.",
-            "title": "Commuter Survey-2014",
-            "keyword": [
-                "commuter",
-                "mode of travel",
-                "time spent commuting"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "477033d2-5f68-40c4-bb29-ae765751759d",
-            "programCode": [
-                "184:036"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
             "distribution": [
                 {
                     "description": "This dataset is the USAID portion of a larger dataset developed by OMB to better understand and to quanity the carbon footprint of the daily commute of government workers.",
@@ -5722,14 +5707,29 @@
                     "title": "Commuter Survey-2014"
                 }
             ],
+            "identifier": "477033d2-5f68-40c4-bb29-ae765751759d",
+            "keyword": [
+                "commuter",
+                "mode of travel",
+                "time spent commuting"
+            ],
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2015-02-09",
+            "programCode": [
+                "184:036"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/USAID_2014_Commuter_Survey_Report.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/2014_Commuter_Survey_Questionnaire.docx",
                 "http://www.gsa.gov/portal/content/162265"
-            ]
+            ],
+            "title": "Commuter Survey-2014"
         },
         {
             "accessLevel": "public",
@@ -5740,19 +5740,28 @@
                 "fn": "Jason Wucinski",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-11-21",
             "description": "The DHS Program STATcompiler allows users to make custom tables based on hundreds of demographic and health indicators across more than 70 countries.  Access to complete country datasets may be granted to individuals who register at www.dhsprogram.com and create a new research project request.",
-            "title": "DHS STATCompiler",
+            "distribution": [
+                {
+                    "accessURL": "http://api.dhsprogram.com",
+                    "description": "Key health and family planning indicators derived from national Demographic and Health Surveys.  Access to complete country datasets may be granted to individuals who register at www.dhsprogram.com and create a new research project request.",
+                    "format": "API",
+                    "title": "DHS STATCompiler"
+                }
+            ],
+            "identifier": "62a927d0-74e7-4802-96c2-90e78c85608c",
             "keyword": [
                 "demographics",
                 "health",
                 "survey",
                 "international"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "62a927d0-74e7-4802-96c2-90e78c85608c",
+            "landingPage": "http://statcompiler.com",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-11-21",
             "programCode": [
                 "184:011",
                 "184:012",
@@ -5764,22 +5773,16 @@
                 "184:018",
                 "184:019"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://statcompiler.com",
-            "distribution": [
-                {
-                    "description": "Key health and family planning indicators derived from national Demographic and Health Surveys.  Access to complete country datasets may be granted to individuals who register at www.dhsprogram.com and create a new research project request.",
-                    "accessURL": "http://api.dhsprogram.com",
-                    "format": "API",
             "title": "DHS STATCompiler"
-                }
-            ],
-            "language": [
-                "en-US"
-            ]
         },
         {
+            "USAIDawardNumber": "AID-OAA-A-16-00032",
+            "USAIDinitiative": "President's Emergency Plan for AIDS Relief (PEPFAR)",
+            "USAIDsubmittingOrganization": "International AIDS Vaccine Initiative",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -5788,27 +5791,7 @@
                 "fn": "Jason Wucinski",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-01-01",
             "description": "Table for Prediction of extended high viremia among newly HIV-1-infected persons in sub-Saharan Africa",
-            "title": "Table for Prediction of extended high viremia among newly HIV-1-infected persons in sub-Saharan Africa",
-            "keyword": [
-                "sustained high viremia",
-                "Acute HIV",
-                "HIV risk score algorithm",
-                "Africa antiretroviral therapy viral load",
-                "Epidemiology"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "e18332ed-70fa-47e2-a066-597892212cda",
-            "programCode": [
-                "184:011"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "https://figshare.com/articles/Table_for_Prediction_of_extended_high_viremia_among_newly_HIV-1-infected_persons_in_sub-Saharan_Africa/5727083",
-            "spatial": "Sub-saharan Africa",
             "distribution": [
                 {
                     "description": "Table for Prediction of extended high viremia among newly HIV-1-infected persons in sub-Saharan Africa",
@@ -5818,15 +5801,32 @@
                     "title": "Table for Prediction of extended high viremia among newly HIV-1-infected persons in sub-Saharan Africa"
                 }
             ],
+            "identifier": "e18332ed-70fa-47e2-a066-597892212cda",
+            "keyword": [
+                "sustained high viremia",
+                "Acute HIV",
+                "HIV risk score algorithm",
+                "Africa antiretroviral therapy viral load",
+                "Epidemiology"
+            ],
+            "landingPage": "https://figshare.com/articles/Table_for_Prediction_of_extended_high_viremia_among_newly_HIV-1-infected_persons_in_sub-Saharan_Africa/5727083",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-01-01",
+            "programCode": [
+                "184:011"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0192785"
             ],
-            "USAIDawardNumber": "AID-OAA-A-16-00032",
-            "USAIDsubmittingOrganization": "International AIDS Vaccine Initiative",
-            "USAIDinitiative": "President's Emergency Plan for AIDS Relief (PEPFAR)"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Sub-saharan Africa",
+            "title": "Table for Prediction of extended high viremia among newly HIV-1-infected persons in sub-Saharan Africa"
         },
         {
             "accessLevel": "public",
@@ -5837,16 +5837,17 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-11-26",
             "description": "The DEC is a publicly available document repository for over 160,000 technical and programmatic documents related to USAID programming that is managed by USAID's Knowledge Services Center in the CIO. Users can search and view the majority of documents that are submitted by both implementing partners and USAID staff.",
-            "title": "Development Experience Clearinghouse (DEC)",
+            "identifier": "4a7dd2fa-4138-4367-9adf-40448b74a408",
             "keyword": [
                 "USAID"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "4a7dd2fa-4138-4367-9adf-40448b74a408",
+            "landingPage": "http://dec.usaid.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2013-11-26",
             "programCode": [
                 "184:001",
                 "184:002",
@@ -5886,11 +5887,10 @@
                 "184:036",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "http://dec.usaid.gov",
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "name": "USAID"
+            },
+            "title": "Development Experience Clearinghouse (DEC)"
         },
         {
             "accessLevel": "public",
@@ -5901,16 +5901,26 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-11-26",
             "description": "The DEC is a publicly available document repository for over 160,000 technical and programmatic documents related to USAID programming that is managed by USAID's Knowledge Services Center in M/CIO. Users can search and view the majority of documents that are submitted by both implementing partners and USAID staff.",
-            "title": "Development Experience Clearinghouse (DEC) - document repository",
+            "distribution": [
+                {
+                    "accessURL": "http://www.usaid.gov/developer/development-experience-clearinghouse-dec-api",
+                    "description": "The API facilitates searching the DEC, USAID's publicly available document repository that is managed by USAID's Knowledge Services Center in M/CIO.",
+                    "format": "API",
+                    "title": "Development Experience Clearinghouse (DEC) - document repository"
+                }
+            ],
+            "identifier": "dd4fe488-3c50-4d57-92f7-48a4e6578069",
+            "isPartOf": "4a7dd2fa-4138-4367-9adf-40448b74a408",
             "keyword": [
                 "USAID"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "dd4fe488-3c50-4d57-92f7-48a4e6578069",
+            "landingPage": "http://dec.usaid.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2013-11-26",
             "programCode": [
                 "184:001",
                 "184:002",
@@ -5950,20 +5960,10 @@
                 "184:036",
                 "184:037"
             ],
-            "landingPage": "http://dec.usaid.gov",
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "distribution": [
-                {
-                    "description": "The API facilitates searching the DEC, USAID's publicly available document repository that is managed by USAID's Knowledge Services Center in M/CIO.",
-                    "accessURL": "http://www.usaid.gov/developer/development-experience-clearinghouse-dec-api",
-                    "format": "API",
+            "publisher": {
+                "name": "USAID"
+            },
             "title": "Development Experience Clearinghouse (DEC) - document repository"
-                }
-            ],
-            "isPartOf": "4a7dd2fa-4138-4367-9adf-40448b74a408",
-            "language": [
-                "en-US"
-            ]
         },
         {
             "accessLevel": "public",
@@ -5974,18 +5974,29 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-11-26",
             "description": "This dataset is a machine readable extraction of publications stored in USAID's Development Experience Clearinghouse as of June 23, 2014.  It is a snapshot taken at a single point in time.",
-            "title": "Development Experience Clearinghouse (DEC) - Machine Readable",
+            "distribution": [
+                {
+                    "description": "This dataset is a machine readable extraction of documents in the DEC at a single point in time.",
+                    "downloadURL": "http://www.usaid.gov/cdn/opendata/DEC_Readable.v01.json.gz",
+                    "format": "gzip",
+                    "mediaType": "application/gzip",
+                    "title": "Development Experience Clearinghouse (DEC) - Machine Readable"
+                }
+            ],
+            "identifier": "432bccb4-a7d3-4e11-b532-d84f1934547d",
+            "isPartOf": "4a7dd2fa-4138-4367-9adf-40448b74a408",
             "keyword": [
                 "USAID",
                 "document repository",
                 "library"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "432bccb4-a7d3-4e11-b532-d84f1934547d",
+            "landingPage": "http://dec.usaid.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2013-11-26",
             "programCode": [
                 "184:001",
                 "184:002",
@@ -6025,26 +6036,18 @@
                 "184:036",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "http://dec.usaid.gov",
-            "distribution": [
-                {
-                    "description": "This dataset is a machine readable extraction of documents in the DEC at a single point in time.",
-                    "downloadURL": "http://www.usaid.gov/cdn/opendata/DEC_Readable.v01.json.gz",
-                    "format": "gzip",
-                    "mediaType": "application/gzip",
-                    "title": "Development Experience Clearinghouse (DEC) - Machine Readable"
-                }
-            ],
-            "isPartOf": "4a7dd2fa-4138-4367-9adf-40448b74a408",
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/WorkingwithDECJSONfiles.pdf"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Development Experience Clearinghouse (DEC) - Machine Readable"
         },
         {
+            "USAIDawardNumber": "AID-BFS-IO-14-00002",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "International Food Policy Research Institute",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -6053,9 +6056,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-12-20",
             "description": "Smallholders in rural Mozambique are typically characterized by low agricultural productivity, which is in part caused by very low levels of input usage.  In the study area, four districts of Nampula province, farmers are generally far from towns where agricultural input providers are based and formal banking services are not available.  Lacking these services, smallholders typically face liquidity constraints during the planting season when returns to input usage are the highest.  In order to explore potential policy solutions to this challenge, the project combined training and incentives to use mobile money technology alongside targeted input marketing visits to promote formal saving strategies and increase take-up of basic inputs, primarily seeds, and fertilizer.   The goal of the pilot project was to determine whether combining group-level trainings in mobile money technology with targeted direct marketing could increase input usage, and consequently boost agricultural productivity.  In collaboration with Vodacom, IFPRI organized a series of trainings, first at the individual level with farm group leaders carried out in Nampula city in June 2014. This was followed by group trainings at local sites to which all farm group members were invited in July-August 2014.  Input marketing visits were carried out by a local input provider, IKURU from October 2014-January 2015.  This dataset is a baseline survey conducted in October 2014-January 2015 in which a sample of households (irrespective of whether a member attained training) were interviewed.  The endline survey was conducted in October-November 2015 (see https://www.usaid.gov/data/dataset/3ada3313-4481-4fe5-99f3-6e638b79e10a.)",
-            "title": "Mozambique Cell Phone Savings Project: Baseline Survey",
+            "identifier": "c824964b-6701-4b52-81e8-520949fec55f",
             "keyword": [
                 "households",
                 "smallholders",
@@ -6066,28 +6068,29 @@
                 "Africa South of Sahara",
                 "Africa"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "c824964b-6701-4b52-81e8-520949fec55f",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "landingPage": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KEXZ0S",
-            "spatial": "Mozambique",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-12-20",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://ebrary.ifpri.org/cdm/singleitem/collection/p15738coll3/id/242/rec/1"
             ],
-            "USAIDawardNumber": "AID-BFS-IO-14-00002",
-            "USAIDsubmittingOrganization": "International Food Policy Research Institute",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Mozambique",
+            "title": "Mozambique Cell Phone Savings Project: Baseline Survey"
         },
         {
+            "USAIDawardNumber": "AID-BFS-IO-14-00002",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "International Food Policy Research Institute",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -6096,9 +6099,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-12-20",
             "description": "Smallholders in rural Mozambique are typically characterized by low agricultural productivity, which is in part caused by very low levels of input usage.  In the study area, four districts of Nampula province, farmers are generally far from towns where agricultural input providers are based and formal banking services are not available.  Lacking these services, smallholders typically face liquidity constraints during the planting season when returns to input usage are the highest.  In order to explore potential policy solutions to this challenge, the project combined training and incentives to use mobile money technology alongside targeted input marketing visits to promote formal saving strategies and increase take-up of basic inputs, primarily seeds, and fertilizer.   The goal of the pilot project was to determine whether combining group-level trainings in mobile money technology with targeted direct marketing could increase input usage, and consequently boost agricultural productivity.  In  collaboration with Vodacom, IFPRI organized a series of trainings, first at the individual level with farm group leaders carried out in Nampula city in June 2014. This was followed by group trainings at local sites to which all farm group members were invited in July-August 2014.  Input marketing visits were carried out by a local input provider, IKURU from October 2014-January 2015.  This dataset is an endline survey conducted in October-November 2015 in which a sample of households (irrespective of whether a member attained training) were interviewed.  The baseline survey was conducted in October 2014-January 2015 (see https://www.usaid.gov/data/dataset/c824964b-6701-4b52-81e8-520949fec55f.)",
-            "title": "Mozambique Cell Phone Savings Project: Endline Survey",
+            "identifier": "3ada3313-4481-4fe5-99f3-6e638b79e10a",
             "keyword": [
                 "households",
                 "smallholders",
@@ -6109,28 +6111,28 @@
                 "Africa South of Sahara",
                 "Africa"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "3ada3313-4481-4fe5-99f3-6e638b79e10a",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "landingPage": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PTKJ1J",
-            "spatial": "Mozambique",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-12-20",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://ebrary.ifpri.org/cdm/singleitem/collection/p15738coll3/id/242/rec/2"
             ],
-            "USAIDawardNumber": "AID-BFS-IO-14-00002",
-            "USAIDsubmittingOrganization": "International Food Policy Research Institute",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Mozambique",
+            "title": "Mozambique Cell Phone Savings Project: Endline Survey"
         },
         {
+            "USAIDawardNumber": "AID-OAA-A-13-00004",
+            "USAIDsubmittingOrganization": "Duke University",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -6139,51 +6141,49 @@
                 "fn": "Emmanuella Delva",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-01-03",
+            "describedByType": "application/pdf",
             "description": "The Global Health Investment Landsacping project database consists of information about impact-oriented and global health-supporting investment funds or capital providers with a focus on East Africa and India.  The data is basic information about the organizations identified including size , geographic focus, and type of organization as well as descriptions about their deals and investments.",
-            "title": "Landscape of Global Health Relevant Investment With a Focus on East Africa and India",
-            "keyword": [
-                "global health",
-                "investment",
-                "investor",
-                "fund",
-                "foundation",
-                "deal"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "59c580e8-22b1-43e1-ac02-7efb6167216c",
-            "programCode": [
-                "184:016",
-                "184:017",
-                "184:026",
-                "184:027",
-                "184:031"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Data_Dictionary_SEAD_Global_Health_Investment_Landscaping_Project_2015.csv",
+                    "describedByType": "text/csv",
                     "description": "The Global Health Investment Landsacping project database consists of information about impact-oriented and global health-supporting investment funds or capital providers with a focus on East Africa and India.  The data is basic information about the organizations identified including size , geographic focus, and type of organization as well as descriptions about their deals and investments.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/SEAD_Global_Health_Investment_Landscaping_Project_dataset.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Landscape of Global Health Relevant Investment With a Focus on East Africa and India",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Data_Dictionary_SEAD_Global_Health_Investment_Landscaping_Project_2015.csv",
-                    "describedByType": "text/csv"
+                    "title": "Landscape of Global Health Relevant Investment With a Focus on East Africa and India"
                 }
             ],
+            "identifier": "59c580e8-22b1-43e1-ac02-7efb6167216c",
+            "keyword": [
+                "global health",
+                "investment",
+                "investor",
+                "fund",
+                "foundation",
+                "deal"
+            ],
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-01-03",
+            "programCode": [
+                "184:016",
+                "184:017",
+                "184:026",
+                "184:027",
+                "184:031"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/SEAD_GHILP_executive_summary.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/SEAD_GHILP_Slide_set.pdf"
             ],
-            "describedByType": "application/pdf",
-            "USAIDawardNumber": "AID-OAA-A-13-00004",
-            "USAIDsubmittingOrganization": "Duke University"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Landscape of Global Health Relevant Investment With a Focus on East Africa and India"
         },
         {
             "accessLevel": "public",
@@ -6194,9 +6194,24 @@
                 "fn": "Chris Murphy",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-01-06",
             "description": "USAID's Development Credit Authority (DCA) works with investors, local financial institutions, and development organizations to design and deliver investment alternatives that unlock financing for U.S. Government priorities. USAID guarantees encourage private lenders to extend financing to underserved borrowers in new sectors and regions. This dataset is the complete list of all private loans made under USAID's DCA since it was established in 1999. To protect the personal information of borrowers and bank partners, all strategic and personal identifiable information was removed.",
-            "title": "Development Credit Authority (DCA) Data Set: Loan Transactions",
+            "distribution": [
+                {
+                    "description": "This dataset is the complete list of all private loans made under USAID's DCA since it was established in 1999, as a csv file.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DCA_Dataset_Loan_Transactions.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "Development Credit Authority (DCA): Loan Transactions - csv"
+                },
+                {
+                    "description": "This dataset is the complete list of all private loans made under USAID's DCA since it was established in 1999, as an EXCEL file.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DCA_Dataset_Loan_Transactions.xlsx",
+                    "format": "EXCEL",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Development Credit Authority (DCA): Loan Transactions - EXCEL"
+                }
+            ],
+            "identifier": "854d1b81-a517-4966-957c-5428fb4c1821",
             "keyword": [
                 "dca",
                 "credit",
@@ -6211,38 +6226,23 @@
                 "loans",
                 "entrepreneurs"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "854d1b81-a517-4966-957c-5428fb4c1821",
+            "landingPage": "http://www.usaid.gov/results-and-data/progress-data/data/dca",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2017-01-06",
             "programCode": [
                 "184:027",
                 "184:031"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "http://www.usaid.gov/results-and-data/progress-data/data/dca",
-            "distribution": [
-                {
-                    "description": "This dataset is the complete list of all private loans made under USAID's DCA since it was established in 1999, as a csv file.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DCA_Dataset_Loan_Transactions.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "Development Credit Authority (DCA): Loan Transactions - csv"
+            "publisher": {
+                "name": "USAID"
             },
-                {
-                    "description": "This dataset is the complete list of all private loans made under USAID's DCA since it was established in 1999, as an EXCEL file.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DCA_Dataset_Loan_Transactions.xlsx",
-                    "format": "EXCEL",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Development Credit Authority (DCA): Loan Transactions - EXCEL"
-                }
-            ],
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Loans_Transactions_Column_Definitions.csv"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Development Credit Authority (DCA) Data Set: Loan Transactions"
         },
         {
             "accessLevel": "public",
@@ -6253,9 +6253,24 @@
                 "fn": "Chris Murphy",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-01-06",
             "description": "USAID's Development Credit Authority (DCA) works with investors, local financial institutions, and development organizations to design and deliver investment alternatives that unlock financing for U.S. Government priorities. Whether it's getting working capital to promising entrepreneurs or input financing to small farmers, DCA seeks to prove the commercial viability of underserved markets so that lending and investment continues long after we exit. The Development Credit Authority (DCA) uses partial credit guarantees to mobilize local financing in developing countries. Guarantee agreements encourage private lenders to extend financing to underserved borrowers in new sectors and regions. By opening up local channels of financing, USAID is empowering entrepreneurs in developing countries at a minimal cost to the U.S. taxpayer. This USAID dataset shows the partial credit guarantees that USAID has issued since the development credit authority program was founded in 1999. The spreadsheet reflects the full facility size of each guarantee, how much was lent under the guarantee, the status of the guarantee (i.e., active or expired), how much in claims the bank submitted due to losses it incurred for loans placed under the guarantee, and how many loans were placed under coverage of the guarantee. The data also shows the sector and country for each guarantee.",
-            "title": "Development Credit Authority (DCA) Data Set: Guarantee Utilization and Claims",
+            "distribution": [
+                {
+                    "description": "This USAID dataset shows the partial credit guarantees that USAID has issued since the development credit authority program was founded in 1999 as a csv file.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DCA_Dataset_Utilization_and_Claims.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "Development Credit Authority (DCA): Guarantee Utilization and Claims - csv"
+                },
+                {
+                    "description": "This USAID dataset shows the partial credit guarantees that USAID has issued since the development credit authority program was founded in 1999 as an EXCEL file.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DCA_Dataset_Utilization_and_Claims.xlsx",
+                    "format": "EXCEL",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Development Credit Authority (DCA): Guarantee Utilization and Claims - EXCEL"
+                }
+            ],
+            "identifier": "31fbe412-d87a-41b1-bf62-259895057f79",
             "keyword": [
                 "dca",
                 "credit",
@@ -6270,38 +6285,23 @@
                 "loans",
                 "entrepreneurs"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "31fbe412-d87a-41b1-bf62-259895057f79",
+            "landingPage": "http://www.usaid.gov/results-and-data/progress-data/data/dca",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2017-01-06",
             "programCode": [
                 "184:027",
                 "184:031"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "http://www.usaid.gov/results-and-data/progress-data/data/dca",
-            "distribution": [
-                {
-                    "description": "This USAID dataset shows the partial credit guarantees that USAID has issued since the development credit authority program was founded in 1999 as a csv file.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DCA_Dataset_Utilization_and_Claims.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "Development Credit Authority (DCA): Guarantee Utilization and Claims - csv"
+            "publisher": {
+                "name": "USAID"
             },
-                {
-                    "description": "This USAID dataset shows the partial credit guarantees that USAID has issued since the development credit authority program was founded in 1999 as an EXCEL file.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/DCA_Dataset_Utilization_and_Claims.xlsx",
-                    "format": "EXCEL",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Development Credit Authority (DCA): Guarantee Utilization and Claims - EXCEL"
-                }
-            ],
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Utilization_and_Claims_Column_Definitions.csv"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Development Credit Authority (DCA) Data Set: Guarantee Utilization and Claims"
         },
         {
             "accessLevel": "public",
@@ -6312,18 +6312,28 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-02-15",
             "description": "Dollars to Results shows spending in a fiscal year alongside results reported for that same year.  Data are illustrative and do not reflect the entirety of impact achieved from the overall funds disbursed.  This file contains three years of data for 43 USAID Operating Units.",
-            "title": "Dollars to Results: Linking Spending to Outputs and Outcomes",
+            "distribution": [
+                {
+                    "description": "Dollars to Results shows spending in a fiscal year alongside results reported for that same year.  Data are illustrative and do not reflect the entirety of impact achieved from the overall funds disbursed.  This file contains three years of data for 43 USAID Operating Units.",
+                    "downloadURL": "https://results.usaid.gov/USAID-DTR-fulldataset.zip",
+                    "format": "zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "Dollars to Results: Linking Spending to Outputs and Outcomes"
+                }
+            ],
+            "identifier": "a1ca9979-901c-4771-abe5-8ffb68223467",
             "keyword": [
                 "disbursements",
                 "outputs",
                 "outcomes"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "a1ca9979-901c-4771-abe5-8ffb68223467",
+            "landingPage": "http://results.usaid.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2015-02-15",
             "programCode": [
                 "184:001",
                 "184:002",
@@ -6363,20 +6373,10 @@
                 "184:036",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "http://results.usaid.gov",
-            "distribution": [
-                {
-                    "description": "Dollars to Results shows spending in a fiscal year alongside results reported for that same year.  Data are illustrative and do not reflect the entirety of impact achieved from the overall funds disbursed.  This file contains three years of data for 43 USAID Operating Units.",
-                    "downloadURL": "https://results.usaid.gov/USAID-DTR-fulldataset.zip",
-                    "format": "zipped CSV",
-                    "mediaType": "application/zip",
+            "publisher": {
+                "name": "USAID"
+            },
             "title": "Dollars to Results: Linking Spending to Outputs and Outcomes"
-                }
-            ],
-            "language": [
-                "en-US"
-            ]
         },
         {
             "accessLevel": "public",
@@ -6387,25 +6387,7 @@
                 "fn": "Jill Moss",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-04-29",
             "description": "This dataset from the Famine Early Warning System Network (FEWS NET) documents ten years, from 2002 to 2012, of cereal price fluctuations across twenty-five African countries. These numbers provide a month-by-month record of the degree and scope of price crises as well as undisturbed cereal markets in Africa.",
-            "title": "FEWS NET Price Volatility Data 2002-2012",
-            "keyword": [
-                "disbursements",
-                "outputs",
-                "outcomes"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "8357a7f6-2514-42ea-8069-ae260c9a4d98",
-            "programCode": [
-                "184:027",
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.fews.net",
             "distribution": [
                 {
                     "description": "This dataset from the Famine Early Warning System Network (FEWS NET) documents ten years, from 2002 to 2012, of cereal price fluctuations across twenty-five African countries. These numbers provide a month-by-month record of the degree and scope of price crises as well as undisturbed cereal markets in Africa.",
@@ -6415,11 +6397,31 @@
                     "title": "FEWS NET Price Volatility Data 2002-2012"
                 }
             ],
+            "identifier": "8357a7f6-2514-42ea-8069-ae260c9a4d98",
+            "keyword": [
+                "disbursements",
+                "outputs",
+                "outcomes"
+            ],
+            "landingPage": "http://www.fews.net",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-04-29",
+            "programCode": [
+                "184:027",
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "FEWS NET Price Volatility Data 2002-2012"
         },
         {
+            "USAIDawardNumber": "AID-278-LA-14-00001",
+            "USAIDsubmittingOrganization": "FHI 360",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -6428,223 +6430,221 @@
                 "fn": "Reem Omar",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-05-27",
+            "describedByType": "application/pdf",
             "description": "The USAID Jordan Local Enterprise Support Project (LENS) conducted a survey of MSEs in 2014-2015 to better understand Jordanian enterprises and to assess the major barriers and opportunities for growth. The study covers general demographics, workforce trends, firm performance, access to finance, processes and networks, and the impact of the Syrian refugee crisis.  The survey consists of 86 questions in a double sampling design with stratification. The data gathers representative information for all MSEs operating in the governorates of Amman (excluding the Greater AmmanMunicipality), Zarqa, Irbid, Karak, Tafilah, and Aqaba (excluding the ASEZA free zone). Although the study is not intended to be national in scope, the target population of the six areas collectively capture 60% of the kingdom?s population.",
-            "title": "Survey of Micro- and Small Enterprises in Jordan (2015) [PUBLIC]",
-            "keyword": [
-                "MSE",
-                "survey",
-                "economy",
-                "Jordan",
-                "enterprise",
-                "small",
-                "micro",
-                "SME",
-                "Middle East"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "d5b66dcb-9ba9-4c08-acdd-bbab6a02ed3a",
-            "programCode": [
-                "184:031"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.jordanlens.org/research",
-            "spatial": "Jordan",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- EXCEL format, one sheet with missing data coded and one without codes for missing data in Arabic.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_AR.xlsx",
                     "format": "EXCEL",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- EXCEL format, one sheet with missing data coded and one without codes for missing data in English.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_EN.xlsx",
                     "format": "EXCEL",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- CSV format,  in Arabic, without codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_NO_MISS_AR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- STATA format,  in Arabic, without codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_NO_MISS_AR.dta",
                     "format": "STATA",
                     "mediaType": "application/x-stata",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, STATA Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, STATA Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- SPSS format,  in Arabic, without codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_NO_MISS_AR.sav",
                     "format": "SPSS",
                     "mediaType": "application/SPSS",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, SPSS Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, SPSS Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- TSV format, in Arabic, without codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_NO_MISS_AR.tsv",
                     "format": "ARFF",
                     "mediaType": "text/tsv",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, TSV Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, TSV Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- ARFF format, in English, without codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_NO_MISS_EN.arff",
                     "format": "ARFF",
                     "mediaType": "text/arff",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, ARFF Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, ARFF Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- CSV format,  in English, without codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_NO_MISS_EN.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- STATA format,  in English, without codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_NO_MISS_EN.dta",
                     "format": "STATA",
                     "mediaType": "application/x-stata",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, STATA Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, STATA Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- SPSS format,  in English, without codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_NO_MISS_EN.sav",
                     "format": "SPSS",
                     "mediaType": "application/SPSS",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, SPSS Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, SPSS Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- TSV format, in English, without codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_NO_MISS_EN.tsv",
                     "format": "ARFF",
                     "mediaType": "text/tsv",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, TSV Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, TSV Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- CSV format, in Arabic, with codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_WITH_MISS_AR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- with Missing Data Codes",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- with Missing Data Codes"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- STATA format,  in Arabic, with missing data codes.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_WITH_MISS_AR.dta",
                     "format": "STATA",
                     "mediaType": "application/x-stata",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, STATA Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, STATA Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- SPSS format,  in Arabic, with missing data codes.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_WITH_MISS_AR.sav",
                     "format": "SPSS",
                     "mediaType": "application/SPSS",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, SPSS Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, SPSS Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- TSV format, in Arabic, with missing data codes.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_WITH_MISS_AR.tsv",
                     "format": "ARFF",
                     "mediaType": "text/tsv",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, TSV Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, Arabic -- No Missing Data Codes, TSV Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- ARFF format, in English, with missing data codes.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_WITH_MISS_EN.arff",
                     "format": "ARFF",
                     "mediaType": "text/arff",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- With Missing Data Codes, ARFF Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- With Missing Data Codes, ARFF Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- CSV format, in English, with codes for missing data.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_WITH_MISS_EN.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- With Missing Data Codes",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- With Missing Data Codes"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- STATA format,  in English, with missing data codes.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_WITH_MISS_EN.dta",
                     "format": "STATA",
                     "mediaType": "application/x-stata",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, STATA Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, STATA Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- SPSS format,  in English, with missing data codes.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_WITH_MISS_EN.sav",
                     "format": "SPSS",
                     "mediaType": "application/SPSS",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, SPSS Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, SPSS Format"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Data from the 2014-2015 LENS survey of MSEs in Jordan -- TSV format, in English, with missing data codes.",
                     "downloadURL": "https://github.com/jordanlens/research/blob/master/data/MSE_SURVEY_PUBLIC/2015/MSE_SURVEY_PUBLIC_WITH_MISS_EN.tsv",
                     "format": "ARFF",
                     "mediaType": "text/tsv",
-                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, TSV Format",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/public_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "The 2015 Survey of Micro- and Small Enterprises in Jordan, English -- No Missing Data Codes, TSV Format"
                 }
             ],
+            "identifier": "d5b66dcb-9ba9-4c08-acdd-bbab6a02ed3a",
+            "keyword": [
+                "MSE",
+                "survey",
+                "economy",
+                "Jordan",
+                "enterprise",
+                "small",
+                "micro",
+                "SME",
+                "Middle East"
+            ],
+            "landingPage": "http://www.jordanlens.org/research",
             "language": [
                 "en-US",
                 "ar"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-05-27",
+            "programCode": [
+                "184:031"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/mse_survey_questionnaire_en_v2.pdf"
             ],
-            "describedByType": "application/pdf",
-            "USAIDawardNumber": "AID-278-LA-14-00001",
-            "USAIDsubmittingOrganization": "FHI 360"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Jordan",
+            "title": "Survey of Micro- and Small Enterprises in Jordan (2015) [PUBLIC]"
         },
         {
             "accessLevel": "public",
@@ -6655,9 +6655,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-07-20",
             "description": "Led by USAID, Feed the Future is the U.S. Government?s global hunger and food security initiative, which establishes a foundation for lasting progress against global hunger. (See the individual entries to retrieve data for the country surveys.) With a focus on smallholder farmers, particularly women, Feed the Future supports partner countries in developing their agriculture sectors to spur economic growth that increases incomes and reduces hunger, poverty and undernutrition. Focus countries in the Feed the Future initiative administer baseline surveys to: establish the starting point for indicators to be used for program monitoring and evaluation, reveal information about the nature, magnitude and severity of problems to be addressed, serve as the basis for determining appropriate amounts of intervention, and determine targets for selected indicators of program progress.",
-            "title": "Collection of Country-level Baseline Surveys Implemented as Part of the Feed the Future Initiative",
+            "identifier": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
             "keyword": [
                 "agriculture",
                 "consumption",
@@ -6669,23 +6668,27 @@
                 "gender",
                 "WEAI"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
+            "landingPage": "http://www.feedthefuture.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-07-20",
             "programCode": [
                 "184:029",
                 "184:019",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov",
-            "language": [
-                "en-US"
-            ]
+            "title": "Collection of Country-level Baseline Surveys Implemented as Part of the Feed the Future Initiative"
         },
         {
+            "USAIDawardNumber": "EEM-G-00-04-00013-00",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "International Food Policy Research Institute (IFPRI)",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -6694,28 +6697,7 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-04-23",
             "description": "The Bangladesh Integrated Household Survey dataset is a thorough assessment of current standard of food security in Bangladesh taken from 2011-2012. The dataset includes all baseline household surveys made under the USAID-led Feed the Future initiative, a collaborative effort that supports country-owned processes and plans for improving food security and promoting transparency, and within the Zones of Influence as outlined by the Feed the Future Bangladesh plan. The survey was designed and supervised by the International Food Policy Research Institute (IFPRI). The survey was administered by Data Analysis and Technical Assistance, Dhaka, Bangladesh. Funding for the survey was provided by United States Agency for International Development (USAID). To protect the personal information of respondents, all personal identifiable information was removed, and the final dataset has been approved for publication by the Government of Bangladesh.",
-            "title": "Feed the Future Bangladesh: Baseline Integrated Household Survey",
-            "keyword": [
-                "agriculture",
-                "food",
-                "feed the future",
-                "survey",
-                "analysis"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "d6ac2eb7-85f5-4f35-9b45-5777a98972e3",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:031"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov/country/bangladesh",
             "distribution": [
                 {
                     "description": "The Bangladesh Integrated Household Survey dataset is the baseline for the USAID-led Feed the Future program in Bangladesh",
@@ -6725,19 +6707,40 @@
                     "title": "Feed the Future Bangladesh: Baseline Integrated Household Survey"
                 }
             ],
+            "identifier": "d6ac2eb7-85f5-4f35-9b45-5777a98972e3",
             "isPartOf": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
+            "keyword": [
+                "agriculture",
+                "food",
+                "feed the future",
+                "survey",
+                "analysis"
+            ],
+            "landingPage": "http://www.feedthefuture.gov/country/bangladesh",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-04-23",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:031"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.feedthefuture.gov/sites/default/files/resource/files/Bangladesh_Feed_the_Future_Baseline_Country_Report_English.pdf",
                 "http://www.ifpri.org/publication/how-does-womens-time-reproductive-work-and-agriculture-affect-maternal-and-child"
             ],
-            "USAIDawardNumber": "EEM-G-00-04-00013-00",
-            "USAIDsubmittingOrganization": "International Food Policy Research Institute (IFPRI)",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Feed the Future Bangladesh: Baseline Integrated Household Survey"
         },
         {
+            "USAIDawardNumber": "EEM-G-00-04-00013",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "International Food Policy Research Institute",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -6746,9 +6749,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-12-12",
             "description": "This dataset is the second round of Bangladesh Integrated Household Survey (BIHS). The BIHS is the only nationally representative survey in Bangladesh that collects detailed data on (1) plot-level agricultural production and practices, (2) dietary intake of individual household members, (3) anthropometric measurements (height and weight) of all household members, and (4) data to measure women?s empowerment in agriculture index (WEAI). A community survey supplements the BIHS data to provide information on area-specific contextual factors. The BIHS covers 6500 households in 325 primary sampling units. The sample is statistically representative at following levels: (a) nationally representative of rural Bangladesh; (b) representative of rural areas of each of the seven administrative divisions of the country: Barisal, Chittagong, Dhaka, Khulna, Rajshahi, Rangpur, and Sylhet; and (c) representative of the Feed the Future (FTF) zone of influence.  To retrieve the data, navigate to the landing page.",
-            "title": "Bangladesh Integrated Household Survey (BIHS) 2015",
+            "identifier": "2296b12a-1b9d-42ae-a32e-a8c5cc121f99",
             "keyword": [
                 "agriculture",
                 "agriculture extension",
@@ -6771,10 +6773,12 @@
                 "WEAI",
                 "Bangladesh"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "2296b12a-1b9d-42ae-a32e-a8c5cc121f99",
+            "landingPage": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/BXSYEL",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-12-12",
             "programCode": [
                 "184:016",
                 "184:019",
@@ -6789,21 +6793,19 @@
                 "184:029",
                 "184:031"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/BXSYEL",
-            "spatial": "Bangladesh",
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://ebrary.ifpri.org/cdm/singleitem/collection/p15738coll3/id/242/rec/1"
             ],
-            "USAIDawardNumber": "EEM-G-00-04-00013",
-            "USAIDsubmittingOrganization": "International Food Policy Research Institute",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Bangladesh",
+            "title": "Bangladesh Integrated Household Survey (BIHS) 2015"
         },
         {
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Kansas State University",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -6812,28 +6814,7 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-04-23",
             "description": "The Ghana Household Survey dataset is the baseline survey for the USAID-led Feed the Future initiative, a collaborative effort that supports country-owned processes and plans for improving food security and promoting transparency within the project Zones of Influence.",
-            "title": "Feed the Future Ghana: Baseline Household Survey",
-            "keyword": [
-                "agriculture",
-                "food",
-                "feed the future",
-                "survey",
-                "analysis"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "f722cc77-3e00-4a78-9211-90044db5740a",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:031"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov/country/ghana",
             "distribution": [
                 {
                     "description": "These baseline surveys of nearly 5,000 households in Ghana capture all indicators outlined by the Feed the Future Initiative, and will be used to measure progress over the next five years.",
@@ -6843,18 +6824,40 @@
                     "title": "Feed the Future Ghana: Baseline Household Survey"
                 }
             ],
+            "identifier": "f722cc77-3e00-4a78-9211-90044db5740a",
             "isPartOf": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
+            "keyword": [
+                "agriculture",
+                "food",
+                "feed the future",
+                "survey",
+                "analysis"
+            ],
+            "landingPage": "http://www.feedthefuture.gov/country/ghana",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-04-23",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:031"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.metss-ghana.k-state.edu/PBS_Items/PBSReport22814export.pdf",
                 "http://www.ifpri.org/publication/how-does-womens-time-reproductive-work-and-agriculture-affect-maternal-and-child"
             ],
-            "USAIDsubmittingOrganization": "Kansas State University",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Feed the Future Ghana: Baseline Household Survey"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -6863,90 +6866,47 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-10-11",
             "description": "The Malawi Population-Based Survey (PBS) provides a comprehensive assessment of the current status of agriculture and food security in seven districts in the Central and Southern Regions: Mchinji, Lilongwe, Dedza, Ntcheu, Balaka, Machinga, and Mangochi.  The PBS was conducted from November 14 to December 22, 2012.  The overall objective of the survey is to provide baseline on data living standards, nutritional status, and women's empowerment in agriculture in the Zone Of Influence.",
-            "title": "Feed the Future Malawi: Baseline Household Survey",
-            "keyword": [
-                "agriculture",
-                "consumption",
-                "poverty",
-                "hunger",
-                "feed the future",
-                "food insecurity",
-                "women's empowerment",
-                "Malawi"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "7eb4c66f-3f68-4ac1-9ce9-b2240e81d66f",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:031"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov/country/Malawi",
-            "spatial": "Malawi",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140320%20(1).xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five CSV files from the Malawi Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Malawi_CSVs.zip",
                     "format": "Zipped CSV",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Malawi: Baseline Household Survey, in CSV format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140320%20(1).xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Malawi: Baseline Household Survey, in CSV format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140320%20(1).xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five SAS files from the Malawi Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Malawi_SAS.zip",
                     "format": "Zipped SAS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Malawi: Baseline Household Survey, in SAS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140320%20(1).xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Malawi: Baseline Household Survey, in SAS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140320%20(1).xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five SPSS files from the Malawi Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Malawi_SPSS.zip",
                     "format": "Zipped SPSS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Malawi: Baseline Household Survey, in SPSS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140320%20(1).xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Malawi: Baseline Household Survey, in SPSS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140320%20(1).xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five STATA files from the Malawi Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Malawi_STATA.zip",
                     "format": "Zipped STATA",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Malawi: Baseline Household Survey, in STATA format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140320%20(1).xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Malawi: Baseline Household Survey, in STATA format"
                 }
             ],
+            "identifier": "7eb4c66f-3f68-4ac1-9ce9-b2240e81d66f",
             "isPartOf": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "184:15"
-            ],
-            "contactPoint": {
-                "fn": "Anna Brenes",
-                "hasEmail": "mailto:opendata@usaid.gov"
-            },
-            "modified": "2013-10-11",
-            "description": "The Mozambique Population-Based Survey (PBS) provides a comprehensive assessment of the current status of agriculture and food security in two provinces, Zambizia and Nampula.  These areas were selected based on national estimates that indicate that the incidence of poverty, malnutrition, and stunting among children less than five years of age is disproportionately high.  These provinces are adjacent to three of the country's main trade corridors: Nacala (linking Mozambique to Malawi and Zambia), Beira (linking Mozambique to Zimbabwe), and the N1 (key North-South road connecting Nacala and Beira corridors). The PBS was conducted in 2013 with a focus on Household Hunger; Women's Dietary Diversity; Children's Minimum Acceptable Diet;WEAI (Women's Empowerment in Agriculture Index);and Household Expenditure in the two provinces.",
-            "title": "Feed the Future Mozambique: Baseline Household Survey",
             "keyword": [
                 "agriculture",
                 "consumption",
@@ -6955,84 +6915,80 @@
                 "feed the future",
                 "food insecurity",
                 "women's empowerment",
-                "Mozambique"
+                "Malawi"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "75b19d18-202c-45b9-9f49-200a52c785ea",
+            "landingPage": "http://www.feedthefuture.gov/country/Malawi",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-10-11",
             "programCode": [
                 "184:029",
                 "184:019",
                 "184:031"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov/country/Mozambique",
-            "spatial": "Mozambique",
+            "spatial": "Malawi",
+            "title": "Feed the Future Malawi: Baseline Household Survey"
+        },
+        {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
+            "accessLevel": "public",
+            "bureauCode": [
+                "184:15"
+            ],
+            "contactPoint": {
+                "fn": "Anna Brenes",
+                "hasEmail": "mailto:opendata@usaid.gov"
+            },
+            "describedByType": "application/pdf",
+            "description": "The Mozambique Population-Based Survey (PBS) provides a comprehensive assessment of the current status of agriculture and food security in two provinces, Zambizia and Nampula.  These areas were selected based on national estimates that indicate that the incidence of poverty, malnutrition, and stunting among children less than five years of age is disproportionately high.  These provinces are adjacent to three of the country's main trade corridors: Nacala (linking Mozambique to Malawi and Zambia), Beira (linking Mozambique to Zimbabwe), and the N1 (key North-South road connecting Nacala and Beira corridors). The PBS was conducted in 2013 with a focus on Household Hunger; Women's Dietary Diversity; Children's Minimum Acceptable Diet;WEAI (Women's Empowerment in Agriculture Index);and Household Expenditure in the two provinces.",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MozambiqueFTFCodebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of twelve CSV files from the Mozambique Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, several files describing consumption, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Mozambique_CSVs.zip",
                     "format": "Zipped CSV",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Mozambique: Baseline Household Survey, in CSV Format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MozambiqueFTFCodebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Mozambique: Baseline Household Survey, in CSV Format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MozambiqueFTFCodebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of twelve SAS files from the Mozambique Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, several files describing consumption, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Mozambique_SAS.zip",
                     "format": "Zipped SAS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Mozambique: Baseline Household Survey, in SAS Format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MozambiqueFTFCodebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Mozambique: Baseline Household Survey, in SAS Format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MozambiqueFTFCodebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of twelve SPSS files from the Mozambique Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, several files describing consumption, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Mozambique_SPSS.zip",
                     "format": "Zipped SPSS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Mozambique: Baseline Household Survey, in SPSS Format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MozambiqueFTFCodebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Mozambique: Baseline Household Survey, in SPSS Format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MozambiqueFTFCodebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of twelve STATA files from the Mozambique Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, several files describing consumption, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Mozambique_STATA.zip",
                     "format": "Zipped STATA",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Mozambique: Baseline Household Survey, in STATA Format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MozambiqueFTFCodebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Mozambique: Baseline Household Survey, in STATA Format"
                 }
             ],
+            "identifier": "75b19d18-202c-45b9-9f49-200a52c785ea",
             "isPartOf": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/MozambiqueBaselineReport-July2014.pdf",
-                "http://www.ifpri.org/publication/how-does-womens-time-reproductive-work-and-agriculture-affect-maternal-and-child"
-            ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "184:15"
-            ],
-            "contactPoint": {
-                "fn": "Anna Brenes",
-                "hasEmail": "mailto:opendata@usaid.gov"
-            },
-            "modified": "2013-07-13",
-            "description": "The Nepal Population-Based Survey (PBS) provides a comprehensive assessment of the current status of agriculture and food security in 20 districts across the western, mid-western and far-western development regions of the country. These districts make up the zone of influence for USAID/Nepal's Feed the Future (FTF) initiative.  The PBS, which was conducted in May and April 2013, measured: household demographic information, dwelling characteristics, prevalence of poverty, consumption expenditure, hunger, and women's empowerment in Agriculture Index (WEAI).",
-            "title": "Feed the Future Nepal: Baseline Household Survey",
             "keyword": [
                 "agriculture",
                 "consumption",
@@ -7041,83 +6997,84 @@
                 "feed the future",
                 "food insecurity",
                 "women's empowerment",
-                "Nepal"
+                "Mozambique"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "92fa242f-07b3-4ec4-9e98-84ab09e1078b",
+            "landingPage": "http://www.feedthefuture.gov/country/Mozambique",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-10-11",
             "programCode": [
                 "184:029",
                 "184:019",
                 "184:031"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/MozambiqueBaselineReport-July2014.pdf",
+                "http://www.ifpri.org/publication/how-does-womens-time-reproductive-work-and-agriculture-affect-maternal-and-child"
+            ],
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov/country/Nepal",
-            "spatial": "Nepal",
+            "spatial": "Mozambique",
+            "title": "Feed the Future Mozambique: Baseline Household Survey"
+        },
+        {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
+            "accessLevel": "public",
+            "bureauCode": [
+                "184:15"
+            ],
+            "contactPoint": {
+                "fn": "Anna Brenes",
+                "hasEmail": "mailto:opendata@usaid.gov"
+            },
+            "describedByType": "application/pdf",
+            "description": "The Nepal Population-Based Survey (PBS) provides a comprehensive assessment of the current status of agriculture and food security in 20 districts across the western, mid-western and far-western development regions of the country. These districts make up the zone of influence for USAID/Nepal's Feed the Future (FTF) initiative.  The PBS, which was conducted in May and April 2013, measured: household demographic information, dwelling characteristics, prevalence of poverty, consumption expenditure, hunger, and women's empowerment in Agriculture Index (WEAI).",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140505%20(1).xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five CSV files from the Nepal Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Nepal_CSVs.zip",
                     "format": "Zipped CSV",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Nepal: Baseline Household Survey, in CSV format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140505%20(1).xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Nepal: Baseline Household Survey, in CSV format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140505%20(1).xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five SAS files from the Nepal Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Nepal_SAS.zip",
                     "format": "Zipped SAS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Nepal: Baseline Household Survey, in SAS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140505%20(1).xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Nepal: Baseline Household Survey, in SAS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140505%20(1).xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five SPSS files from the Nepal Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Nepal_SPSS.zip",
                     "format": "Zipped SPSS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Nepal: Baseline Household Survey, in SPSS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140505%20(1).xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Nepal: Baseline Household Survey, in SPSS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140505%20(1).xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five STATA files from the Nepal Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Nepal_STATA.zip",
                     "format": "Zipped STATA",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Nepal: Baseline Household Survey, in STATA format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140505%20(1).xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Nepal: Baseline Household Survey, in STATA format"
                 }
             ],
+            "identifier": "92fa242f-07b3-4ec4-9e98-84ab09e1078b",
             "isPartOf": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/Nepal%202013%20FTF%20ZOI%20PBS%20Country%20Report%20-%2020140505.pdf"
-            ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "184:15"
-            ],
-            "contactPoint": {
-                "fn": "Anna Brenes",
-                "hasEmail": "mailto:opendata@usaid.gov"
-            },
-            "modified": "2013-10-11",
-            "description": "The Rwanda Population-Based Survey (PBS) provides a comprehensive assessment of the current status of agriculture and food security in almost the entire country, including all four provinces and all of rural Rwanda.  The Zone of Influence (ZOI) comprises 27 of the 30 districts in Rwanda, with the exception of the three districts of Kigali City. The PBS, which was conducted from December 22, 2012 to January 11, 2013.  The overall objective of the survey is to provide baseline on data living standards, nutritional status, and women's empowerment in agriculture in the ZOI.",
-            "title": "Feed the Future Rwanda: Baseline Household Survey",
             "keyword": [
                 "agriculture",
                 "consumption",
@@ -7126,72 +7083,118 @@
                 "feed the future",
                 "food insecurity",
                 "women's empowerment",
-                "Rwanda"
+                "Nepal"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "314fbe77-7bab-4508-965b-5408b060b5ff",
+            "landingPage": "http://www.feedthefuture.gov/country/Nepal",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-07-13",
             "programCode": [
                 "184:029",
                 "184:019",
                 "184:031"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/Nepal%202013%20FTF%20ZOI%20PBS%20Country%20Report%20-%2020140505.pdf"
+            ],
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov/country/Rwanda",
-            "spatial": "Rwanda",
+            "spatial": "Nepal",
+            "title": "Feed the Future Nepal: Baseline Household Survey"
+        },
+        {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
+            "accessLevel": "public",
+            "bureauCode": [
+                "184:15"
+            ],
+            "contactPoint": {
+                "fn": "Anna Brenes",
+                "hasEmail": "mailto:opendata@usaid.gov"
+            },
+            "describedByType": "application/pdf",
+            "description": "The Rwanda Population-Based Survey (PBS) provides a comprehensive assessment of the current status of agriculture and food security in almost the entire country, including all four provinces and all of rural Rwanda.  The Zone of Influence (ZOI) comprises 27 of the 30 districts in Rwanda, with the exception of the three districts of Kigali City. The PBS, which was conducted from December 22, 2012 to January 11, 2013.  The overall objective of the survey is to provide baseline on data living standards, nutritional status, and women's empowerment in agriculture in the ZOI.",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook-Variables%20.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five CSV files from the Rwanda Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Rwanda_CSVs.zip",
                     "format": "Zipped CSV",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Rwanda: Baseline Household Survey, in CSV format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook-Variables%20.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Rwanda: Baseline Household Survey, in CSV format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook-Variables%20.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five SAS files from the Rwanda Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Rwanda_SAS.zip",
                     "format": "Zipped SAS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Rwanda: Baseline Household Survey, in SAS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook-Variables%20.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Rwanda: Baseline Household Survey, in SAS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook-Variables%20.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five SPSS files from the Rwanda Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Rwanda_SPSS.zip",
                     "format": "Zipped SPSS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Rwanda: Baseline Household Survey, in SPSS Format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook-Variables%20.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Rwanda: Baseline Household Survey, in SPSS Format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook-Variables%20.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of five STATA files from the Rwanda Population-Based Survey (PBS) includes: a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Rwanda_STATA.zip",
                     "format": "Zipped STATA",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Rwanda: Baseline Household Survey, in STATA format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook-Variables%20.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Rwanda: Baseline Household Survey, in STATA format"
                 }
             ],
+            "identifier": "314fbe77-7bab-4508-965b-5408b060b5ff",
             "isPartOf": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/Rwanda%202013%20FTF%20ZOI%20PBS%20Country%20Report%20-%2020140509.pdf"
+            "keyword": [
+                "agriculture",
+                "consumption",
+                "poverty",
+                "hunger",
+                "feed the future",
+                "food insecurity",
+                "women's empowerment",
+                "Rwanda"
             ],
-            "describedByType": "application/pdf",
+            "landingPage": "http://www.feedthefuture.gov/country/Rwanda",
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-10-11",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:031"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/Rwanda%202013%20FTF%20ZOI%20PBS%20Country%20Report%20-%2020140509.pdf"
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Rwanda",
+            "title": "Feed the Future Rwanda: Baseline Household Survey"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -7200,89 +7203,89 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-01-23",
+            "describedByType": "application/pdf",
             "description": "Feed the Future (FtF) seeks to reduce poverty and undernutrition in 19 developing countries by focusing on accelerating growth of the agricultural sector, addressing the root causes of undernutrition, and reducing gender inequality.  The baseline survey in Tajikistan captures data in the Feed the Future Zones of Influence (ZOI), comprised of 12 of the 24 districts in Khatlon province.  A total of 2,000 households in the ZOI were surveyed for the PBS data collection activity. These households are spread across 100 standard enumeration areas in the targeted districts.",
-            "title": "Feed the Future Tajikistan: Baseline Household Survey",
-            "keyword": [
-                "agriculture",
-                "consumption",
-                "poverty",
-                "hunger",
-                "feed the future",
-                "food security",
-                "women's empowerment",
-                "gender",
-                "WEAI",
-                "Khatlon",
-                "Tajikistan"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "90402143-38c7-477c-b9ac-6fcf0640883d",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov/country/tajikistan-0",
-            "spatial": "Tajikistan",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_Codebook-20140630.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "This set of ten CSV files from the Tajikistan Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, several files describing consumption, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Tajikistan_CSVs.zip",
                     "format": "Zipped CSV",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Tajikistan: Baseline Household Survey, in CSV format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_Codebook-20140630.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Tajikistan: Baseline Household Survey, in CSV format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_Codebook-20140630.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "This set of ten SAS files from the Tajikistan Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, several files describing consumption, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Tajikistan_SAS.zip",
                     "format": "Zipped SAS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Tajikistan: Baseline Household Survey, in SAS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_Codebook-20140630.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Tajikistan: Baseline Household Survey, in SAS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_Codebook-20140630.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "This set of ten SPSS files from the Tajikistan Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, several files describing consumption, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Tajikistan_SPSS.zip",
                     "format": "Zipped SPSS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Tajikistan: Baseline Household Survey, in SPSS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_Codebook-20140630.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Tajikistan: Baseline Household Survey, in SPSS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_Codebook-20140630.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "This set of ten STATA files from the Tajikistan Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, several files describing consumption, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Tajikistan_STATA.zip",
                     "format": "Zipped STATA",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Tajikistan: Baseline Household Survey, in STATA format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_Codebook-20140630.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Tajikistan: Baseline Household Survey, in STATA format"
                 }
             ],
+            "identifier": "90402143-38c7-477c-b9ac-6fcf0640883d",
             "isPartOf": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
+            "keyword": [
+                "agriculture",
+                "consumption",
+                "poverty",
+                "hunger",
+                "feed the future",
+                "food security",
+                "women's empowerment",
+                "gender",
+                "WEAI",
+                "Khatlon",
+                "Tajikistan"
+            ],
+            "landingPage": "http://www.feedthefuture.gov/country/tajikistan-0",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-01-23",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_Disclosure_Analysis_Plan-20140630.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_README-20140630.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Tajikistan_Baseline_Report_20140804_Final.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Tajikistan_2013_Public_Release_Privacy_Assurance_Statement-20140630.pdf"
             ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Tajikistan",
+            "title": "Feed the Future Tajikistan: Baseline Household Survey"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -7291,94 +7294,48 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-10-11",
+            "describedByType": "application/pdf",
             "description": "The Uganda Population-Based Survey (PBS) provides a comprehensive assessment of the current status of agriculture and food security in 38 districts across eight regions of the country.  The PBS was conducted from October 25 to December 30, 2012.  The overall objective of the survey is to provide baseline on data living standards, nutritional status, and women's empowerment in agriculture in the Zone Of Influence.",
-            "title": "Feed the Future Uganda: Baseline Household Survey",
-            "keyword": [
-                "agriculture",
-                "consumption",
-                "poverty",
-                "hunger",
-                "feed the future",
-                "food insecurity",
-                "women's empowerment",
-                "Uganda"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "983036f6-9490-4b25-bb1e-14c459431694",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:031"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov/country/Uganda",
-            "spatial": "Uganda",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/UgandaFTFCodebook.xls",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of six CSV files from the Uganda Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Uganda_CSVs.zip",
                     "format": "Zipped CSV",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Uganda: Baseline Household Survey, in CSV format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/UgandaFTFCodebook.xls",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Uganda: Baseline Household Survey, in CSV format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/UgandaFTFCodebook.xls",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of six SAS files from the Uganda Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Uganda_SAS.zip",
                     "format": "Zipped SAS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Uganda: Baseline Household Survey, in SAS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/UgandaFTFCodebook.xls",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Uganda: Baseline Household Survey, in SAS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/UgandaFTFCodebook.xls",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of six SPSS files from the Uganda Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Uganda_SPSS.zip",
                     "format": "Zipped SPSS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Uganda: Baseline Household Survey, in SPSS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/UgandaFTFCodebook.xls",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Uganda: Baseline Household Survey, in SPSS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/UgandaFTFCodebook.xls",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of six STATA files from the Uganda Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Uganda_STATA.zip",
                     "format": "Zipped STATA",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Uganda: Baseline Household Survey, in STATA format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/UgandaFTFCodebook.xls",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Uganda: Baseline Household Survey, in STATA format"
                 }
             ],
+            "identifier": "983036f6-9490-4b25-bb1e-14c459431694",
             "isPartOf": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/UgandaBaselineReport-March2014.pdf"
-            ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "184:15"
-            ],
-            "contactPoint": {
-                "fn": "Anna Brenes",
-                "hasEmail": "mailto:opendata@usaid.gov"
-            },
-            "modified": "2013-07-13",
-            "description": "The Zambia Population-Based Survey (PBS) provides a comprehensive assessment of the current status of agriculture and food security in five districts, Chipata, Katete, Lundazi, Nyimba, and Petauke in Zambia. The PBS, which was conducted in November and December of 2012, measured: household demographic information, dwelling characteristics, prevalence of poverty, consumption expenditure, hunger, and women's empowerment in Agriculture Index (WEAI).",
-            "title": "Feed the Future Zambia: Baseline Household Survey",
             "keyword": [
                 "agriculture",
                 "consumption",
@@ -7387,70 +7344,113 @@
                 "feed the future",
                 "food insecurity",
                 "women's empowerment",
-                "Zambia"
+                "Uganda"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "adefe530-02d1-4867-8b3b-1309c2fb16b7",
+            "landingPage": "http://www.feedthefuture.gov/country/Uganda",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-10-11",
             "programCode": [
                 "184:029",
                 "184:019",
                 "184:031"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/UgandaBaselineReport-March2014.pdf"
+            ],
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov/country/zambia",
-            "spatial": "Zambia",
+            "spatial": "Uganda",
+            "title": "Feed the Future Uganda: Baseline Household Survey"
+        },
+        {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
+            "accessLevel": "public",
+            "bureauCode": [
+                "184:15"
+            ],
+            "contactPoint": {
+                "fn": "Anna Brenes",
+                "hasEmail": "mailto:opendata@usaid.gov"
+            },
+            "describedByType": "application/pdf",
+            "description": "The Zambia Population-Based Survey (PBS) provides a comprehensive assessment of the current status of agriculture and food security in five districts, Chipata, Katete, Lundazi, Nyimba, and Petauke in Zambia. The PBS, which was conducted in November and December of 2012, measured: household demographic information, dwelling characteristics, prevalence of poverty, consumption expenditure, hunger, and women's empowerment in Agriculture Index (WEAI).",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140407.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of six CSV files from the Zambia Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Zambia_CSVs.zip",
                     "format": "Zipped CSV",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Zambia: Baseline Household Survey, in CSV format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140407.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Zambia: Baseline Household Survey, in CSV format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140407.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of six SAS files from the Zambia Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Zambia_SAS.zip",
                     "format": "Zipped SAS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Zambia: Baseline Household Survey, in SAS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140407.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Zambia: Baseline Household Survey, in SAS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140407.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of six SPSS files from the Zambia Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Zambia_SPSS.zip",
                     "format": "Zipped SPSS",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Zambia: Baseline Household Survey, in SPSS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140407.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Zambia: Baseline Household Survey, in SPSS format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140407.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This set of six STATA files from the Zambia Population-Based Survey (PBS) includes: a children's file, a household-level file, a household member level file, a women's file, and two files used to construct the Women's Empowerment in Agriculture Index.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Zambia_STATA.zip",
                     "format": "Zipped STATA",
                     "mediaType": "application/zip",
-                    "title": "Feed the Future Zambia: Baseline Household Survey, in STATA format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia%202013%20FTF%20ZOI%20PBS%20Public%20Release%20Codebook%20-%2020140407.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Zambia: Baseline Household Survey, in STATA format"
                 }
             ],
+            "identifier": "adefe530-02d1-4867-8b3b-1309c2fb16b7",
             "isPartOf": "42629c02-5f16-4618-9db4-3a0e2b090e9b",
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/Zambia%202013%20FTF%20ZOI%20PBS%20Country%20Report%20-%2020140404.pdf"
+            "keyword": [
+                "agriculture",
+                "consumption",
+                "poverty",
+                "hunger",
+                "feed the future",
+                "food insecurity",
+                "women's empowerment",
+                "Zambia"
             ],
-            "describedByType": "application/pdf",
+            "landingPage": "http://www.feedthefuture.gov/country/zambia",
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-07-13",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:031"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/Zambia%202013%20FTF%20ZOI%20PBS%20Country%20Report%20-%2020140404.pdf"
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Zambia",
+            "title": "Feed the Future Zambia: Baseline Household Survey"
         },
         {
             "accessLevel": "public",
@@ -7461,9 +7461,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-06-27",
             "description": "Led by USAID, Feed the Future is the U.S. Government?s global hunger and food security initiative, which establishes a foundation for lasting progress against global hunger. (See the individual entries to retrieve data for the country surveys.) With a focus on smallholder farmers, particularly women, Feed the Future supports partner countries in developing their agriculture sectors to spur economic growth that increases incomes and reduces hunger, poverty and undernutrition.  Focus countries in the Feed the Future initiative administer interim population-based surveys in their target geographic areas (zones of influence or ZOI) to monitor country program performance across a number of standardized indicators.",
-            "title": "Collection of Country-level Interim Surveys Implemented as Part of the Feed the Future Initiative",
+            "identifier": "0429cb38-8d7a-40f4-8459-a5c17cf7a0f5",
             "keyword": [
                 "agriculture",
                 "consumption",
@@ -7475,23 +7474,27 @@
                 "gender",
                 "WEAI"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0429cb38-8d7a-40f4-8459-a5c17cf7a0f5",
+            "landingPage": "http://www.feedthefuture.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-06-27",
             "programCode": [
                 "184:029",
                 "184:019",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov",
-            "language": [
-                "en-US"
-            ]
+            "title": "Collection of Country-level Interim Surveys Implemented as Part of the Feed the Future Initiative"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -7500,200 +7503,200 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-09-18",
+            "describedByType": "application/pdf",
             "description": "Feed the Future monitors its performance in part by periodic assessments of a number of standardized indicators. These indicators reflect data collected through population-based surveys (PBS) in the geographic areas targeted by Feed the Future interventions, known as the Feed the Future Zones of Influence (ZOI).  The northern Kenya ZOI is comprised of five counties: Marsabit, Garissa, Isiolo, Wajir, and Turkana.  Of these, only three counties (Marsabit, Isiolo, and Turkana) were included in the baseline survey. Garissa and Wajir were inaccessible during the baseline, because of security issues. Feed the Future REGAL-IR programming covers all five counties of the ZOI, while REGAL-AG covers Marsabit and Isiolo. Differences in the values of indicators can be compared by the intensity of the program (REGAL-IR only versus REGAL-IR plus REGAL-AG) in the REGAL IE report.  Kimetrica, Westat?s subcontractor in northern Kenya, interviewed eligible respondents in a total of 1,837 households in nine counties (Garissa, Isiolo, Marsabit, Turkana, Wajir, Baringo, Mandera, Samburu, and Tana River). Data collection took place from 14 May to 13 June 2015. The sample is large enough to measure differences among intensity levels of REGAL and humanitarian assistance (HA) programming for the IE, as well as provide point estimates for Feed the Future indicators at the ZOI level. This interim assessment uses data from 1,193 households in the five counties of the ZOI (Garissa, Isiolo, Marsabit, Turkana, and Wajir).  The report of the survey including the complete questionnaire can be found in the reference PA00MNZB.pdf.  Versions of the dataset in SAS, SPSS and STATA are available on request by sending an email to opendata@usaid.gov.",
-            "title": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence",
-            "keyword": [
-                "agriculture",
-                "nutrition",
-                "Feed the Future",
-                "food security",
-                "zone of influence",
-                "interim survey",
-                "Northern Kenya"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "776e0a88-ed0e-4201-81a6-73f38524be49",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "landingPage": "http://www.feedthefuture.gov/country/Kenya",
-            "spatial": "Kenya",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset is a household-level file with records for each sampled household with a completed interview (n=1837, variables=102).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_HOUSEHOLD_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence, Household File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence, Household File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset is the household roster file with one record per household member captured in Module C of the questionnaire (n=8,555, vars=35).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_HHMEMBERS_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence, Household Members File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence, Household Members File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset is an individual -dataset with all women age 15-49 with a completed interview in Module H of the questionnaire (n=1,476, vars=140)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_WOMEN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Women's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Women's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset contains records for all children under 5 years of age in the sampled households (n=1,435, vars=217) .",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_CHILDREN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence, Children's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence, Children's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset  (n=1,573, var=167) is the first of two datasets needed to calculate the WEAI-related measures. It contains Module G data from the primary adult (18+) female decisionmaker within each household (for the sub-sample of households with a primary adult female decisionmaker).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_WEAI_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-File 1",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-File 1"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset  (n=28,314, vars=113) is the second of two datasets needed to calculate the WEAI-related measures.  It includes the 24-hour time allocation data from Module G6, the time use questionnaire, and thus each respondent on Module G has multiple records, one for each of the 18 time use activities (28,314 activities divided by 18 activities = 1,573 Module G respondents with time use data in the file.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_WEAI_TIMEUSE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Time Use File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Time Use File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=1,573, vars=169) contains the analytical variables derived in the WEAI analysis.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_WEAI_RECODE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Recode File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Recode File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=1,837, vars=66) contains variables from Module E, the Household Consumption Expenditures module used to calculate the poverty and expenditure indicators.  It includes household-level derived variables (including the expenditure and poverty indicator variables), as well as variables from sub-module E6:Housing Expenditures",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_EXP_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Household Consumption Expenditures",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Household Consumption Expenditures"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=243,789, vars=28) contains variables from Module E1, Food Consumption Over Past 7 Days.  Each household with food consumption data has multiple records (for the 133 food items in sub-Module E1).  (243,789 records divided by 133 food items =1,833 Module E households with sub-Module E1 data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_EXP_E1_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Food Consumption-Past 7 Days ",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Food Consumption-Past 7 Days "
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=18,300, vars=17) contains variables from sub-Module E2, Non-Food Expenditures over Past 7 Days.  Each household with data for non-food expenditurs over the past week has multiple records (for the 10 non-food items in sub-Module E2)  (18,300 records divided by 10 non-food items=1,830 Module E households with sub-Module E2 data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_EXP_E2_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Non-Food Expenditures Over the Past 7 Days",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Non-Food Expenditures Over the Past 7 Days"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=53,070, vars=17) contains data from sub-Module E3: Non-Food Expenditures Over Past One Month. Each household with data for non-food expenditures over the past month has multiple records (for the 29 non-food items in sub-Module E3). (53,070 records divided by 29 non-food items = 1,830 Module E households with sub-Module E3 data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_EXP_E3_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past One Month",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past One Month"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=69,540, vars=17) contains data from sub-Module E4: Non-Food Expenditures Over Past Three Months. Each household with data for non-food expenditures over the past three months has multiple records (for the 38 non-food items in sub-Module E4). (69,540 records divided by 38 non-food items = 1,830 Module E households with sub-Module E4 data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_EXP_E4_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past Three Months",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past Three Months"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=53,070, vars=18) contains data from sub-Module E5: Non-Food Expenditures Over Past 12 Months. Each household with data for non-food expenditures over the past 12 months has multiple records (for the 29 non-food items in sub-Module E5).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_EXP_E5_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past 12 Months",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past 12 Months"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=3,662, vars=15) contain data from sub-Module E5 regarding non-food items that may or may not have been purchased (e.g., construction items such as wood poles and thatching grass). Each household with data for these construction items over the past 12 months has multiple records (for the two construction items in sub-Module E5). (3,662 records divided by 2 construction items = 1,831 Module E households with sub-Module E5 construction data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_EXP_E5CONS_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Construction Expenditures Over Past 12 Months",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Construction Expenditures Over Past 12 Months"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=69,540, vars=23) contains data from sub-Module E7: Durable Goods Expenditures. Each household with data for durable goods expenditures has multiple records (for the 38 durable goods in sub-Module E7). (69,540 records divided by 38 non-food items = 1,830 Module E households with sub-Module E7 data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_EXP_E7_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Durable Goods Expenditures",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Durable Goods Expenditures"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=1,837, vars=84) is a wide file with variables for social capital, adaptive capacity, and asset sales/recovery from the Resilience module in the survey (a portion of Module F). This dataset has one record per household, and contains the derived variables from the Resilience module.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_Resilience1_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Resilience",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Resilience"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence: This dataset (n=34,903, vars=13) is a long file with variables for household resources, and their ranking and availability from the Resilience module (a portion of Module F). This dataset includes 19 records (the number of resources asked about in F201) per household (19 x 1,837 households = 34,903 total records).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NKEN_Resilience2_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Household Resources, Ranking and Availability From the Resilience Module",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Northern Kenya Interim Survey in the Zone of Influence, Household Resources, Ranking and Availability From the Resilience Module"
                 }
             ],
+            "identifier": "776e0a88-ed0e-4201-81a6-73f38524be49",
             "isPartOf": "0429cb38-8d7a-40f4-8459-a5c17cf7a0f5",
-            "references": [
-                "http://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_ReadMe.pdf",
-                "http://pdf.usaid.gov/pdf_docs/PA00MNZB.pdf",
-                "http://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Privacy_Assurance_Statement.pdf"
+            "keyword": [
+                "agriculture",
+                "nutrition",
+                "Feed the Future",
+                "food security",
+                "zone of influence",
+                "interim survey",
+                "Northern Kenya"
             ],
-            "describedByType": "application/pdf",
+            "landingPage": "http://www.feedthefuture.gov/country/Kenya",
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-09-18",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_ReadMe.pdf",
+                "http://pdf.usaid.gov/pdf_docs/PA00MNZB.pdf",
+                "http://www.usaid.gov/opengov/developer/datasets/NorthernKenya_ZOI_Interim_Privacy_Assurance_Statement.pdf"
+            ],
+            "spatial": "Kenya",
+            "title": "Feed the Future Northern Kenya Interim Survey in the Zone of Influence"
         },
         {
+            "USAIDawardNumber": "AID-486-I-14-00001",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Social Impact, Inc.",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -7702,29 +7705,7 @@
                 "fn": "Peoulida Ros",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-12-27",
             "description": "This is the interim population based survey of Feed the Future in Cambodia for 2015.  The data is split into survey modules.  Modules A through C includes location information, informed consent, and the household roster.  Module D includes household characteristics.  Module E is the expenditures module broken up into 8 different parts.  Modules F and G include the hunger scale data and WEIA index data.  Data in modules H and I include mother and child dietary diversity. The report of the survey can be found in the reference pa00kv15.pdf.",
-            "title": "Interim Feed The Future Population Based Assessment of Cambodia",
-            "keyword": [
-                "Feed the Future",
-                "FTF",
-                "Interim Assessment",
-                "2015",
-                "Cambodia"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "4a48f5c4-f10b-47ff-a997-edfdda851bc1",
-            "programCode": [
-                "184:016",
-                "184:019",
-                "184:029",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "spatial": "Cambodia",
             "distribution": [
                 {
                     "description": "Modules A through C of the interim population based survey of Feed the Future in Cambodia, 2015--CSV Format.  To get the definitions of the columns, see the questionnaire.",
@@ -7895,18 +7876,40 @@
                     "title": "Interim Feed The Future Population Based Assessment of Cambodia, Module H-I -- STATA Format"
                 }
             ],
+            "identifier": "4a48f5c4-f10b-47ff-a997-edfdda851bc1",
+            "keyword": [
+                "Feed the Future",
+                "FTF",
+                "Interim Assessment",
+                "2015",
+                "Cambodia"
+            ],
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-12-27",
+            "programCode": [
+                "184:016",
+                "184:019",
+                "184:029",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/FTF_Questionnaire_EN_FINAL.docx",
                 "http://pdf.usaid.gov/pdf_docs/PA00KV15.pdf"
             ],
-            "USAIDawardNumber": "AID-486-I-14-00001",
-            "USAIDsubmittingOrganization": "Social Impact, Inc.",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Cambodia",
+            "title": "Interim Feed The Future Population Based Assessment of Cambodia"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -7915,168 +7918,170 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-11-20",
+            "describedByType": "application/pdf",
             "description": "Feed the Future monitors its performance in part by periodic assessments of a number of standardized indicators. These indicators reflect data collected through population-based surveys (PBS) in the geographic areas targeted by Feed the Future interventions, known as the Feed the Future Zones of Influence (ZOI).  The Malawi ZOI interim assessment was conducted by FTF FEEDBACK in conjunction with its data collection partner, the National Statistical Office of Malawi (NSO), in the rural areas of the ZOI districts of Dedza, Lilongwe, Mangochi, Mchinji, and Ntcheu.  FTF FEEDBACK and NSO interviewed 813 households and ICF International and CARD interviewed 208 households. A total of 1,021 households were interviewed, which provided data for the target sample size of 1,007 households and ensured the sample is representative of the seven districts covered in the interim assessment.  The report of the survey including the commplete questionnaire can be found in the reference pa00mjmr.pdf.  Versions of the dataset in SAS, SPSS and STATA are available on request by sending an email to opendata@usaid.gov.",
-            "title": "Feed the Future Malawi Interim Survey in the Zone of Influence",
-            "keyword": [
-                "agriculture",
-                "nutrition",
-                "Feed the Future",
-                "food security",
-                "zone of influence",
-                "interim survey",
-                "Malawi"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0fdca8d9-c756-4071-a911-37f26c667fd1",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "landingPage": "http://www.feedthefuture.gov/country/Malawi",
-            "spatial": "Malawi",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset is a household-level file with records for each sampled household with a completed interview (n=1,021, variables=90).  The file includes variables from Modules A,D, and F as well as key household-level derived variables from the household dataset.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_HOUSEHOLD_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Malawi Interim Survey in the Zone of Influence, Household File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Malawi Interim Survey in the Zone of Influence, Household File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset is the household member roster file with one record per household member captured in Module C of the questionnaire (n=4,779, vars=36).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_HHMEMBERS_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Malawi Interim Survey in the Zone of Influence,Household Members File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Malawi Interim Survey in the Zone of Influence,Household Members File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset is an individual -dataset with all women age 15-49 with a completed interview in Module H of the questionnaire (n=942, vars=75)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_WOMEN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Women's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Women's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset contains records for all children under 5 years of age in the sampled households (n=843, vars=120) .  It includes data from Module I of the questionnaire for children's anthropometry and infant and young child feeding practices.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_CHILDREN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Malawi Interim Survey in the Zone of Influence, Children's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Malawi Interim Survey in the Zone of Influence, Children's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset  (n=948, var=166) is the first of two datasets needed to calculate the WEAI-related measures. It contains Module G data from the primary adult (18+) female decisionmaker within each household (for the sub-sample of households with a primary adult female decisionmaker).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_WEAI_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Malawi Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-File 1",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Malawi Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-File 1"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset  (n=17,064, vars=117) is the second of two datasets needed to calculate the WEAI-related measures.  It includes the 24-hour time allocation data from Module G6, the time use questionnaire, and thus each respondent on Module G has multiple records, one for each of the 18 time use activities (17,064 activities divided by 18 activities = 948 respondents with time use data in the file.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_WEAI_TIMEUSE_pr.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Time Use File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Time Use File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset (n=948, vars=168) contains the analytical variables derived in the WEAI analysis.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_WEAI_RECODE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Recode File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Recode File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset (n=1,021, vars=73) contains variables from Module E, the Household Consumption Expenditures module used to calculate the poverty and expenditure indicators.  It includes household-level derived variables (including the expenditure and poverty indicator variables), as well as variables from sub-module E6:Housing Expenditures",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_EXP_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Household Consumption Expenditures",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Household Consumption Expenditures"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset (n=115,373, vars=26) contains variables from Module E1, Food Consumption Over Past 7 Days.  Each household with food consumption data has multiple records (for the 113 food items in sub-Module E1).  (115,373 records divided by 113 food items =1,021 Module E households with sub-Module E1 data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_EXP_E1_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Food Consumption-Past 7 Days ",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Food Consumption-Past 7 Days "
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset (n=10,210, vars=16) contains variables from sub-Module E2, Non-Food Expenditures over Past 7 Days.  Each household with data for non-food expenditurs over the past week has multiple records (for the 10 non-food items in sub-Module E2)  (10,210 records divided by 10 non-food items=1,021 Module E households with sub-Module E2 data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_EXP_E2_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Non-Food Expenditures Over the Past 7 Days",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Non-Food Expenditures Over the Past 7 Days"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset (n=26,546, vars=16) contains data from sub-Module E3: Non-Food Expenditures Over Past One Month. Each household with data for non-food expenditures over the past month has multiple records (for the 26 non-food items in sub-Module E3). (26,546 records divided by 26 non-food items = 1,021 Module E households with sub-Module E3 data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_EXP_E3_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past One Month",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past One Month"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset (n=39,819, vars=16) contains data from sub-Module E4: Non-Food Expenditures Over Past Three Months. Each household with data for non-food expenditures over the past three months has multiple records (for the 39 non-food items in sub-Module E4). (39,819 records divided by 39 non-food items = 1,021 Module E households with sub-Module E4 data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_EXP_E4_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past Three Months",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past Three Months"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset (n=32,672, vars=16) contains data from sub-Module E5: Non-Food Expenditures Over Past 12 Months. Each household with data for non-food expenditures over the past 12 months has multiple records (for the 32 non-food items in sub-Module E5).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_EXP_E5_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past 12 Months",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Non-Food Expenditures Over Past 12 Months"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset (n=2,250, vars=20) contain data from sub-Module E5 regarding non-food items that may or may not have been purchased (e.g., construction items such as wood poles and thatching grass). Each household with data for these 2-3 construction items over the past 12 months has multiple records ",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_EXP_E5CONS_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Construction Expenditures Over Past 12 Months",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Construction Expenditures Over Past 12 Months"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Malawi Interim Survey in the Zone of Influence: This dataset (n=31,651, vars=20) contains data from sub-Module E7: Durable Goods Expenditures. Each household with data for durable goods expenditures has multiple records (for the 31 durable goods in sub-Module E7). (31,651 records divided by 31 non-food items = 1,021 Module E households with sub-Module E7 data.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MWI_EXP_E7_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Durable Goods Expenditures",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Malawi Interim Survey in the Zone of Influence, Durable Goods Expenditures"
                 }
             ],
+            "identifier": "0fdca8d9-c756-4071-a911-37f26c667fd1",
             "isPartOf": "0429cb38-8d7a-40f4-8459-a5c17cf7a0f5",
+            "keyword": [
+                "agriculture",
+                "nutrition",
+                "Feed the Future",
+                "food security",
+                "zone of influence",
+                "interim survey",
+                "Malawi"
+            ],
+            "landingPage": "http://www.feedthefuture.gov/country/Malawi",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-11-20",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Malawi_ZOI_Interim_ReadMe.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pa00mjmr.pdf",
@@ -8084,15 +8089,13 @@
                 "http://www.usaid.gov/opengov/developer/datasets/2015_Interim_PBS_Questionnaire_ModulesAthruE.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/2015_Interim_PBS_Questionnaire_ModulesFthruI.pdf"
             ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "spatial": "Malawi",
+            "title": "Feed the Future Malawi Interim Survey in the Zone of Influence"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -8101,111 +8104,111 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-11-10",
+            "describedByType": "application/pdf",
             "description": "Feed the Future monitors its performance in part by periodic assessments of a number of standardized indicators. These indicators reflect data collected through population-based surveys (PBS) in the geographic areas targeted by Feed the Future interventions, known as the Feed the Future Zones of Influence (ZOI).  The objective of the Nepal Feed the Future program is to maximize the number of Nepalis lifted out of poverty and increase the number of children and women with improved nutritional status. This first interim assessment will provide the U.S. Government (USG) interagency partners, USAID BFS, USAID Missions, host country governments, and development partners with information about short-term progress of the ZOI indicators. The assessment is designed for use as a monitoring tool, and as such provides point estimates of the indicators with an acceptable level of statistical precision.  For the interim survey, the FTF FEEDBACK team interviewed a total of 880 households in the ZOI. These households were spread across 44 clusters in the targeted districts, with a sample consisting of 20 households per cluster.  The report of the survey including the complete questionnaire can be found in the reference pa00mm3r.pdf.  Versions of the dataset in SAS, SPSS and STATA are available on request by sending an email to opendata@usaid.gov.",
-            "title": "Feed the Future Nepal Interim Survey in the Zone of Influence",
-            "keyword": [
-                "agriculture",
-                "nutrition",
-                "Feed the Future",
-                "food security",
-                "zone of influence",
-                "interim survey",
-                "Nepal"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "81868011-5bc5-463a-bc43-99a7a51b914c",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "landingPage": "http://www.feedthefuture.gov/country/Nepal",
-            "spatial": "Nepal",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Nepal Interim Survey in the Zone of Influence: This dataset is a household-level file with records for each sampled household with a completed interview (n=838, variables=99).  The file contains one record per household including data from Modules A, D, and F.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NPL_HOUSEHOLD_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Nepal Interim Survey in the Zone of Influence, Household File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Nepal Interim Survey in the Zone of Influence, Household File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Nepal Interim Survey in the Zone of Influence: This dataset is the household roster file with one record per household member captured in Module C of the questionnaire (n=4,002, vars=35).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NPL_HHMEMBERS_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Nepal Interim Survey in the Zone of Influence,Household Members File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Nepal Interim Survey in the Zone of Influence,Household Members File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Nepal Interim Survey in the Zone of Influence: This dataset is the data for all women age 15-49 with a completed interview captured in Module H of the questionnaire (n=994, vars=137)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NPL_WOMEN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Nepal Interim Survey in the Zone of Influence, Women's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Nepal Interim Survey in the Zone of Influence, Women's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Nepal Interim Survey in the Zone of Influence: This dataset contains records for all children under 3 years of age (0-35 months) (n=229, vars=49) . This file includes data in Module I for children's consumption of the Nepal-specific nutrient rich value chain commodities (NRVCC)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NPL_CHILDREN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Nepal Interim Survey in the Zone of Influence, Children's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Nepal Interim Survey in the Zone of Influence, Children's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Nepal Interim Survey in the Zone of Influence: This dataset  (n=800, var=163) is the first of two datasets needed to calculate the WEAI-related measures. It is a household-level file and contains the records for Module G data from the primary adult (18+) female decisionmaker within each household (for the sub-sample of households with a primary adult female decisionmaker).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NPL_WEAI_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Nepal Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-File 1",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Nepal Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-File 1"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Nepal Interim Survey in the Zone of Influence: This dataset  (n=14,400, vars=113) is the second of two datasets needed to calculate the WEAI-related measures.  It includes the 24-hour time allocation data from Module G6, the time use module, and thus each respondent on Module G has multiple records, one for each of the 18 time use activities (800 respondents x 18 activities = 14,400 records.) ",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NPL_WEAI_TIMEUSE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Nepal Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Time Use File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Nepal Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Time Use File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Nepal Interim Survey in the Zone of Influence: This dataset (n=800, vars=166) contains the analytical variables derived in the WEAI analysis.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/NPL_WEAI_RECODE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Nepal Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Recode File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Nepal Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Recode File"
                 }
             ],
+            "identifier": "81868011-5bc5-463a-bc43-99a7a51b914c",
             "isPartOf": "0429cb38-8d7a-40f4-8459-a5c17cf7a0f5",
+            "keyword": [
+                "agriculture",
+                "nutrition",
+                "Feed the Future",
+                "food security",
+                "zone of influence",
+                "interim survey",
+                "Nepal"
+            ],
+            "landingPage": "http://www.feedthefuture.gov/country/Nepal",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-11-10",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_ReadMe.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pa00mm3r.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Nepal_ZOI_Interim_Privacy_Assurance_Statement.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/2015_Interim_PBS_Questionnaire_Nepal.pdf"
             ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "spatial": "Nepal",
+            "title": "Feed the Future Nepal Interim Survey in the Zone of Influence"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -8214,111 +8217,111 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-10-30",
+            "describedByType": "application/pdf",
             "description": "Feed the Future monitors its performance in part by periodic assessments of a number of standardized indicators. These indicators reflect data collected through population-based surveys (PBS) in the geographic areas targeted by Feed the Future interventions, known as the Feed the Future Zones of Influence (ZOI). This particular dataset contains the data from the first interim assessment of Feed the Future?s population-based indicators for the ZOI in Rwanda. In Rwanda, the ZOI covers the entire country excluding Kigali, encompassing rural, periurban and urban areas in 27 districts out of a total of 30.  The report of the survey including the entire questionnaire can be found in the reference PA00MHSW.pdf.  Versions of the dataset in SAS, SPSS and STATA are available on request by sending an email to opendata@usaid.gov.",
-            "title": "Feed the Future Rwanda Interim Survey in the Zone of Influence",
-            "keyword": [
-                "agriculture",
-                "nutrition",
-                "Feed the Future",
-                "food security",
-                "zone of influence",
-                "interim survey",
-                "Rwanda"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "b15a2533-09e5-4421-a847-5ee3d1919a20",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "landingPage": "http://www.feedthefuture.gov/country/Rwanda",
-            "spatial": "Rwanda",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Rwanda Interim Survey in the Zone of Influence: This dataset is a household-level file with records for each sampled household with a completed interview (n=1,066, variables=89).  The file contains one record per household including data from Modules A, D, and F.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/RWA_HOUSEHOLD_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Rwanda Interim Survey in the Zone of Influence, Household File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Rwanda Interim Survey in the Zone of Influence, Household File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Rwanda Interim Survey in the Zone of Influence: This dataset is the household roster file with one record per household member captured in Module C of the questionnaire (n=4,890, vars=34).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/RWA_HHMEMBERS_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Rwanda Interim Survey in the Zone of Influence,Household Members File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Rwanda Interim Survey in the Zone of Influence,Household Members File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Rwanda Interim Survey in the Zone of Influence: This dataset is an individual-level dataset with the data for all women age 15-49 with a completed interview captured in Module H of the questionnaire (n=1,155, vars=31)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/RWA_WOMEN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Rwanda Interim Survey in the Zone of Influence, Women's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Rwanda Interim Survey in the Zone of Influence, Women's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Rwanda Interim Survey in the Zone of Influence: This dataset contains records for all children under 3 years of age (0-35 months) (n=438, vars=31) . This file includes data in Module I.   Note that the children's anthropometry indicators and dietary intake indicators were calculated with secondary data, the 2014-2015 Rwanda Demographic and Health Survey.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/RWA_CHILDREN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Rwanda Interim Survey in the Zone of Influence, Children's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Rwanda Interim Survey in the Zone of Influence, Children's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Rwanda Interim Survey in the Zone of Influence: This dataset  (n=998, var=162) is the first of two datasets needed to calculate the WEAI-related measures. It contains Module G data from the primary adult (18+) female decisionmaker within each household (for the sub-sample of households with a primary adult female decisionmaker).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/RWA_WEAI_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Rwanda Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-File 1",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Rwanda Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-File 1"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Rwanda Interim Survey in the Zone of Influence: This dataset  (n=17,964, vars=112) is the second of two datasets needed to calculate the WEAI-related measures.  It includes the 24-hour time allocation data from Module G6, the time use module, and thus each respondent on Module G has multiple records, one for each of the 18 time use activities (998 respondents x 18 activities = 17,964 records.) ",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/RWA_WEAI_TIMEUSE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Rwanda Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Time Use File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Rwanda Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Time Use File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Rwanda Interim Survey in the Zone of Influence: This dataset (n=998, vars=164) contains the analytical variables derived in the WEAI analysis.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/RWA_WEAI_RECODE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Rwanda Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Recode File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Rwanda Interim Survey in the Zone of Influence, Women's Empowerment in Agriculture Index-Recode File"
                 }
             ],
-            "isPartOf": "0429cb38-8d7a-40f4-8459-a5c17cf7a0f5",
+            "identifier": "b15a2533-09e5-4421-a847-5ee3d1919a20",
+            "isPartOf": "0429cb38-8d7a-40f4-8459-a5c17cf7a0f5",
+            "keyword": [
+                "agriculture",
+                "nutrition",
+                "Feed the Future",
+                "food security",
+                "zone of influence",
+                "interim survey",
+                "Rwanda"
+            ],
+            "landingPage": "http://www.feedthefuture.gov/country/Rwanda",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-10-30",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_ReadMe.pdf",
                 "http://pdf.usaid.gov/pdf_docs/PA00MHSW.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Rwanda_ZOI_Interim_Privacy_Assurance_Statement.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/2015_Interim_Survey_PBS_Questionnaire_Rwanda.pdf"
             ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "spatial": "Rwanda",
+            "title": "Feed the Future Rwanda Interim Survey in the Zone of Influence"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -8327,129 +8330,129 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-07-01",
+            "describedByType": "application/pdf",
             "description": "Feed the Future monitors its performance in part by periodic assessments of a number of standardized indicators. These indicators reflect data collected through population-based surveys (PBS) in the geographic areas targeted by Feed the Future interventions, known as the Feed the Future Zones of Influence (ZOI).  This particular dataset contains the data from the first interim assessment of Feed the Future?s population-based indicators for the ZOI in Uganda. The ZOI comprises 38 districts distributed across eight regions: Central 1, Central 2, East Central, Mid-Eastern, North, Southwest, West Nile and Western. The regions were further combined into four strata in survey design: Central 1/2, East Central/Mid-Eastern, North, and Southwest/West Nile/Western.  Sampling was based on a two-stage design, with stratification by region and urban/rural. In the first stage, enumeration areas (EAs) were selected from the 2014 national census sampling frame in 38 districts with probability proportional to size (PPS) sampling. EAs with total number of households less than 80 in the frame were combined with one or two adjacent EAs to form a larger cluster for selection. Forty-two clusters were selected with 60 EAs within these clusters. Twenty households within each selected cluster were selected randomly from a list of eligible households in the second stage. The assessment is designed for use as a monitoring tool, and as such provides point estimates of the indicators with an acceptable level of statistical precision.  However, Feed the Future ZOI sample calculations are not designed to support conclusions of causality or program attribution, nor is the interim assessment designed to measure change from the baseline.  The report of the survey including the complete questionnaire can be found in the reference pa00mfbj.pdf.  Versions of the dataset in SAS, SPSS and STATA are available on request by sending an email to opendata@usaid.gov.",
-            "title": "Feed the Future Uganda Interim Survey in the Zone of Infuence",
-            "keyword": [
-                "agriculture",
-                "nutrition",
-                "Feed the Future",
-                "food security",
-                "zone of influence",
-                "interim survey",
-                "Uganda"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "db9ce503-78ac-4627-b923-f61bca6cc90e",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "landingPage": "http://www.feedthefuture.gov/country/Uganda",
-            "spatial": "Uganda",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Uganda Interim Survey in the Zone of Infuence: This dataset is a household-level file with records for each sampled household with a completed interview (n=778, variables=92).  The file contains one record per household including data from modules A, D, and F in the questionnaire.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/UGA_HOUSEHOLD_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Uganda Interim Survey in the Zone of Infuence, Household File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Uganda Interim Survey in the Zone of Infuence, Household File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Uganda Interim Survey in the Zone of Infuence: This dataset is the household roster file with one record per household member captured in Module C of the questionnaire (n=4,140, vars=35).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/UGA_HHMEMBERS_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Uganda Interim Survey in the Zone of Infuence,Household Members File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Uganda Interim Survey in the Zone of Infuence,Household Members File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Uganda Interim Survey in the Zone of Infuence: This dataset is an individual-level dataset for all women age 15-49 with a completed interview captured in Module H of the questionnaire (n=760, vars=112)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/UGA_WOMEN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Uganda Interim Survey in the Zone of Infuence, Women's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Uganda Interim Survey in the Zone of Infuence, Women's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Uganda Interim Survey in the Zone of Infuence: This dataset contains records for all children under 5 years of age in the sampled households (n=691, vars=181) .  In includes data in Module I for children's anthropometry, and infant and young child feeding practices. ",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/UGA_CHILDREN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Uganda Interim Survey in the Zone of Infuence, Children's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Uganda Interim Survey in the Zone of Infuence, Children's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Uganda Interim Survey in the Zone of Infuence: This dataset  (n=664, var=163) is the first of two datasets needed to calculate the WEAI-related measures. It contains Module G data from the primary adult (18+) female decisionmaker within each household (for the sub-sample of households with a primary adult female decisionmaker).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/UGA_WEAI_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Uganda Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-File 1",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Uganda Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-File 1"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Uganda Interim Survey in the Zone of Infuence: This dataset  (n=11,952, vars=113) is the second of two datasets needed to calculate the WEAI-related measures.  It includes the 24-hour time allocation data from Module G6, the time use module, and thus each respondent on Module G has multiple records, one for each of the 18 time use activities.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/UGA_WEAI_TIMEUSE_pr.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Uganda Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-Time Use File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Uganda Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-Time Use File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Uganda Interim Survey in the Zone of Infuence: This dataset  (n=778, vars=237) is a country-specific module requested by the USAID/Uganda Mission regarding the use of agricultural technologies in the production of maize, beans and coffee.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/UGA_MODJ_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Uganda Interim Survey in the Zone of Infuence, Use of Agricultural Technologies",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Uganda Interim Survey in the Zone of Infuence, Use of Agricultural Technologies"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Uganda Interim Survey in the Zone of Infuence: This dataset (n=664, vars=162) contains the analytical variables derived in the WEAI analysis.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/UGA_WEAI_RECODE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Uganda Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-Recode File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Uganda Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-Recode File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Uganda Interim Survey in the Zone of Infuence: This recode dataset  (n=2,334, vars=92) contaions the analytical variables derived from the Agricultural technology (Module J) analysis.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/UGA_MODJ_RECODE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Uganda Interim Survey in the Zone of Infuence, Analytical Variables Created About the Use of Agricultural Technologies",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Uganda Interim Survey in the Zone of Infuence, Analytical Variables Created About the Use of Agricultural Technologies"
                 }
             ],
+            "identifier": "db9ce503-78ac-4627-b923-f61bca6cc90e",
             "isPartOf": "0429cb38-8d7a-40f4-8459-a5c17cf7a0f5",
+            "keyword": [
+                "agriculture",
+                "nutrition",
+                "Feed the Future",
+                "food security",
+                "zone of influence",
+                "interim survey",
+                "Uganda"
+            ],
+            "landingPage": "http://www.feedthefuture.gov/country/Uganda",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-07-01",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "https://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Survey_README.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pa00mfbj.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Uganda_2015_ZOI_Interim_Assurance_Statement.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/2015_Interim_Survey_PBS_Questionnaire_Uganda.pdf"
             ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "spatial": "Uganda",
+            "title": "Feed the Future Uganda Interim Survey in the Zone of Infuence"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -8458,109 +8461,106 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-03-07",
+            "describedByType": "application/pdf",
             "description": "Feed the Future monitors its performance in part by periodic assessments of a number of standardized indicators. These indicators reflect data collected through population-based surveys (PBS) in the geographic areas targeted by Feed the Future interventions, known as the Feed the Future Zones of Influence (ZOI).  The Zambia interim ZOI survey covers only the rural and peri-urban population in the five districts, which reflects the Rural Agricultural Livelihoods Survey (RALS) sample frame.  Classification of rural and peri-urban standard enumeration areas (EAs) draws on information from Zambia?s 2000 Census of Population and Housing, the approach established for Zambia Post Harvest Surveys (PHS), and the RALS sample frame. Agricultural households are those reporting any crop production, livestock production, poultry production, or fish farming; rural EAs are those that include at least 30 agricultural households; and peri-urban EAs are urban EAs with at least 70 percent of their households classified as agricultural. The ZOI population that resides in the urban areas excluded from the Zambia ZOI survey represents approximately 10 percent of the total ZOI population. The Zambia ZOI interim survey was conducted by Feed the Future FEEDBACK (FTF FEEDBACK) in conjunction with its data collection partner, Palm Associates Limited. Fieldwork for the ZOI interim survey took place from November 25 to December 21, 2015.  The report of the survey including the complete questionnaire can be found in the reference PA00MJMB.pdf.  Versions of the dataset in SAS, SPSS and STATA are available on request by sending an email to opendata@usaid.gov.",
-            "title": "Feed the Future Zambia Interim Survey in the Zone of Infuence",
-            "keyword": [
-                "agriculture",
-                "nutrition",
-                "Feed the Future",
-                "food security",
-                "zone of influence",
-                "interim survey",
-                "Zambia"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "754fb143-9cfd-47b6-a026-f7c635494f0b",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "landingPage": "http://www.feedthefuture.gov/country/Zambia",
-            "spatial": "Zambia",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Zambia Interim Survey in the Zone of Infuence: This dataset is a household-level file with records for each sampled household with a completed interview (n=768, variables=88).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ZMB_HOUSEHOLD_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Zambia Interim Survey in the Zone of Infuence, Household File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Zambia Interim Survey in the Zone of Infuence, Household File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Zambia Interim Survey in the Zone of Infuence: This dataset is the household roster file with one record per household member captured in Module C of the questionnaire (n=4,779, vars=32).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ZMB_HHMEMBERS_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Zambia Interim Survey in the Zone of Infuence,Household Members File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Zambia Interim Survey in the Zone of Infuence,Household Members File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Zambia Interim Survey in the Zone of Infuence: This dataset is the data for all women age 15-49 with a completed interview captured in Module H of the questionnaire (n=932, vars=112)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ZMB_WOMEN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Zambia Interim Survey in the Zone of Infuence, Women's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Zambia Interim Survey in the Zone of Infuence, Women's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Zambia Interim Survey in the Zone of Infuence: This dataset contains records for all children under 5 years of age in the sampled households (n=705, vars=208) .",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ZMB_CHILDREN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Zambia Interim Survey in the Zone of Infuence, Children's File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Zambia Interim Survey in the Zone of Infuence, Children's File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Zambia Interim Survey in the Zone of Infuence: This dataset  (n=739, var=163) is the first of two datasets needed to calculate the WEAI-related measures. It contains Module G data from the primary adult (18+) female decisionmaker within each household (for the sub-sample of households with a primary adult female decisionmaker).",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ZMB_WEAI_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Zambia Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-File 1",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future Zambia Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-File 1"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Zambia Interim Survey in the Zone of Infuence: This dataset  (n=13,203, vars=111) is the second of two datasets needed to calculate the WEAI-related measures.  It includes the 24-hour time allocation data from Module G6, the time use module, and thus each respondent on Module G has multiple records, one for each of the 18 time use activities (13,301 records divided by 18 activities = 739 Module G respondents with time use data in the file.)",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ZMB_WEAI_TIMEUSE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Zambia Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-Time Use File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Zambia Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-Time Use File"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
+                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet",
                     "description": "Feed the Future Zambia Interim Survey in the Zone of Infuence: This dataset (n=739, vars=165) contains the analytical variables derived in the WEAI analysis.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ZMB_WEAI_RECODE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future: Zambia Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-Recode File",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Codebook.ods",
-                    "describedByType": "application/vnd.oasis.opendocument.spreadsheet"
+                    "title": "Feed the Future: Zambia Interim Survey in the Zone of Infuence, Women's Empowerment in Agriculture Index-Recode File"
                 }
             ],
+            "identifier": "754fb143-9cfd-47b6-a026-f7c635494f0b",
             "isPartOf": "0429cb38-8d7a-40f4-8459-a5c17cf7a0f5",
+            "keyword": [
+                "agriculture",
+                "nutrition",
+                "Feed the Future",
+                "food security",
+                "zone of influence",
+                "interim survey",
+                "Zambia"
+            ],
+            "landingPage": "http://www.feedthefuture.gov/country/Zambia",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-03-07",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_ReadMe.pdf",
                 "http://pdf.usaid.gov/pdf_docs/PA00MJMB.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Zambia_ZOI_Interim_Privacy_Assurance_Statement.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/2015_Interim_PBS_Questionnaire_Zambia.pdf"
             ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "spatial": "Zambia",
+            "title": "Feed the Future Zambia Interim Survey in the Zone of Infuence"
         },
         {
             "accessLevel": "public",
@@ -8571,31 +8571,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2018-08-22",
+            "describedByType": "application/pdf",
             "description": "This Dataset consists of three files and is an update to the previous FTF_Summary_Data_2011-2014.csv file: FTFMS Data by OU and Indicator 2011-2017.xls, README_FTFMS, and FTFMS Centrally Funded Mechanism Locations March 2017.csv. The machine readable CSV files to be generated from Feed the Future's Monitoring System platform where data is entered by Operating Unit (OU) and indicator will be available in December 2018 and will accompany the Excel report file. The FTFMS Data by Indicator_2011_2017.csv file will aggregate reported indicator values to the national levels. The FTFMS Data by OU_2011_2017.csv will aggregate reported values to the national level.  Feed the Future is known for its rigorous monitoring, evaluation and learning system, which measures the results of our whole-of-government efforts. The Global Food Security Act sparked an update to this system to align it with our new strategy and  strengthen how we are learning, adapting to challenges, and effectively tracking our progress. The revision of our monitoring, evaluation and learning system included an update to our performance indicators to align with our new results framework.  For 2018 and 2019, we will continue to report on the original set of Feed the Future indicators, while collecting targets and baseline data for Feed the Future\udc92s updated indicators. Feed the Future will also continue to track progress against poverty and hunger in our original 19 Feed the Future focus countries to complete reporting on the initiative\udc92s first phase.  Please refer to the READ_ME.txt file for more details about this dataset.",
-            "title": "Feed the Future Monitoring System Aggregate Data 2011-2017",
-            "keyword": [
-                "agriculture",
-                "consumption",
-                "poverty",
-                "hunger",
-                "Feed the Future",
-                "food security",
-                "women's empowerment",
-                "monitoring and evaluation",
-                "FTFMS"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "d03994db-4fc5-4b6c-9206-f17d1ce68f79",
-            "programCode": [
-                "184:029",
-                "184:031"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.feedthefuture.gov",
             "distribution": [
                 {
                     "description": "This summary data file in EXCEL format is derived from the Feed the Future Monitoring System (FTFMS) and contains program-related indicator values for the years 2011-2017 for all FTF Countries.  The  FTFMS collects and stores information at the implementing mechanism (IM) level for all USAID Missions receiving Agriculture, Nutrition (Focus countries only), or Food for Peace development funding (all countries).",
@@ -8612,18 +8589,44 @@
                     "title": "Feed the Future Centrally Funded Mechanisms as of March 2017"
                 }
             ],
+            "identifier": "d03994db-4fc5-4b6c-9206-f17d1ce68f79",
+            "keyword": [
+                "agriculture",
+                "consumption",
+                "poverty",
+                "hunger",
+                "Feed the Future",
+                "food security",
+                "women's empowerment",
+                "monitoring and evaluation",
+                "FTFMS"
+            ],
+            "landingPage": "http://www.feedthefuture.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2018-08-22",
+            "programCode": [
+                "184:029",
+                "184:031"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/README_FTFMS.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/FY13FTFMSGuidance.pdf",
                 "https://www.feedthefuture.gov/resource/feed-the-future-handbook-of-indicator-definitions/",
                 "http://www.usaid.gov/opengov/developer/datasets/Description_of_Tags_locations_prime_partners_data_set.docx"
             ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ]
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Feed the Future Monitoring System Aggregate Data 2011-2017"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -8632,133 +8635,133 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-02-25",
             "description": "This baseline survey serves as the first stage of an impact evaluation designed to determine the impact of the project's interventions on households? resilience to shocks and, thus, on well-being outcomes, including poverty, food security, and children?s nutritional status.  The survey was administered from November 19 to December 24, 2013 in two of the three sub-regions within the PRIME project?s area of implementation, Borena and Jijiga. The evaluation was designed to focus on a sub-set of participants in two focus areas rather than the entire target population to allow for a closer measurement of a smaller group of households, saving costs and producing more valuable insights. The evaluation design team was also encouraged by USAID/Ethiopia to select these areas to carry out a dual-focused impact evaluation, where one dimension would focus on natural resource management (in Borena) and the second would focus on improvements in livelihoods and market-enabling conditions (in Jijiga).  The baseline survey has two quantitative components?a household survey and a community survey.  Sample selection was based on a two-stage, stratified random sampling design.  In stage one of sample selection, sample enumeration areas were selected within each stratum using probability proportional to size sampling. In the second stage, households within each enumeration area were selected randomly from household listings.  Note that the planned empirical technique for the impact evaluation necessitated that within each of the two study areas, one-third of the households be selected from the High Intensity intervention stratum and two-thirds from the Low Intensity intervention stratum.  The questionnaire can be found in pb-aac-190.pdf and the main report can be found in pb-aac-189.pdf in the references.  Versions of the dataset in SAS, SPSS and STATA are available on request by sending an email to opendata@usaid.gov.",
-            "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE",
-            "keyword": [
-                "Ethiopia",
-                "impact evaluations",
-                "resilience",
-                "PRIME",
-                "Agriculture"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "ff502261-df5c-4f54-b996-084f59e72855",
-            "programCode": [
-                "184:029",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "spatial": "Ethiopia",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This dataset contains the data on children collected as part of the baseline survey generated in support of an impact evaluation of the Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_CHILDREN_FILE_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Children File",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Children File"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This dataset contains the data describing the communities in the program collected as part of the baseline survey generated in support of an impact evaluation of the Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_COMMUNITY_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Community Information File",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Community Information File"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This dataset contains the data describing on food consumption over the 7 Days prior tothe survey collected as part of the baseline survey generated in support of an impact evaluation of the Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_EXP_E1_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Food Consumption Last 7 Days",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Food Consumption Last 7 Days"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This dataset contains the data describing non-food expenditures over the 7 Days prior to the survey collected as part of the baseline survey generated in support of an impact evaluation of the Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_EXP_E2_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Non-Food Expenditures Last 7 Days",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Non-Food Expenditures Last 7 Days"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This dataset contains the data describing non-food expenditures over the month prior to the survey collected as part of the baseline survey generated in support of an impact evaluation of the Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_EXP_E3_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Non-Food Expenditures Last Month",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Non-Food Expenditures Last Month"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This dataset contains the data describing non-food expenditures over the  three months prior to the survey collected as part of the baseline survey generated in support of an impact evaluation of the Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_EXP_E4_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Non-Food Expenditures Last Three Months",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Non-Food Expenditures Last Three Months"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This dataset contains the data describing non-food expenditures over the  twelve months prior to the survey collected as part of the baseline survey generated in support of an impact evaluation of the Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_EXP_E5_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Non-Food Expenditures Last Twelve Months",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Non-Food Expenditures Last Twelve Months"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This dataset contains the data describing the household roster collected as part of the baseline survey generated in support of an impact evaluation of the Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_HHMEMBERS_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Household Roster",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Household Roster"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This dataset contains the data describing the households collected as part of the baseline survey generated in support of an impact evaluation of the Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_HOUSEHOLD_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Household Information",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Household Information"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "This dataset contains the data containing the child anthropometry and milk consumption behavior collected as part of the baseline survey generated in support of an impact evaluation of the Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_MILKFEEDINGS_PR.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Child Anthropometry and Child Milk Consumption",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE--Child Anthropometry and Child Milk Consumption"
                 }
             ],
+            "identifier": "ff502261-df5c-4f54-b996-084f59e72855",
+            "keyword": [
+                "Ethiopia",
+                "impact evaluations",
+                "resilience",
+                "PRIME",
+                "Agriculture"
+            ],
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-02-25",
+            "programCode": [
+                "184:029",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://pdf.usaid.gov/pdf_docs/pbaac190.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pbaac89.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_PAS.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_BaselineIE_README.pdf"
             ],
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Ethiopia",
+            "title": "Ethiopia Pastoralist Areas Resilience Improvement and Market Expansion (PRIME) Project IE"
         },
         {
+            "USAIDawardNumber": "AID-OAA-M-12-00006",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Westat",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -8767,50 +8770,52 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-04-05",
+            "describedByType": "application/pdf",
             "description": "Feed the Future monitors its performance in part by periodic assessments of a number of standardized indicators. These indicators reflect data collected through population-based surveys (PBS) in the geographic areas targeted by Feed the Future interventions, known as the Feed the Future Zones of Influence (ZOI).  The two surveys included in this dataset contain the quantitative data from each of the interim monitoring surveys carried out as part of the Ethiopia PRIME project.  The surveys were administered to a sample of over 400 households in 17 kebeles (communities) once a month over a 6-month period creating for a total of six rounds of data for each survey.  The report of the first interim survey can be found in the reference PA00MGHS.pdf.  Versions of the dataset in SAS, SPSS and STATA are available on request by sending an email to opendata@usaid.gov.",
-            "title": "Feed the Future Ethiopia-PRIME Interim Surveys",
-            "keyword": [
-                "agriculture",
-                "nutrition",
-                "Feed the Future",
-                "food security",
-                "interim survey",
-                "Ethiopia"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "3c016398-9513-4338-8009-f4b0e5886dca",
-            "programCode": [
-                "184:029",
-                "184:019",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "landingPage": "http://www.feedthefuture.gov/country/Ethiopia",
-            "spatial": "Ethiopia",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_IE_IMSph1_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Feed the Future Future Ethiopia-PRIME Interim Surveys: This dataset is the first of two interim surveys administered from October 2014 through April 2015.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_IE_HOUSEHOLD.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Ethiopia-PRIME Interim Survey-October 2014 through April 2015",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_IE_IMSph1_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Ethiopia-PRIME Interim Survey-October 2014 through April 2015"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_IMS2_IE_Codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "Feed the Future Future Ethiopia-PRIME Interim Surveys: This dataset is the second of two interim surveys administered from October 2015 through October 2016.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ETH_IE_HOUSEHOLD_P2.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Feed the Future Ethiopia-PRIME Interim Survey-October 2015 through October 2016",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_IMS2_IE_Codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel"
+                    "title": "Feed the Future Ethiopia-PRIME Interim Survey-October 2015 through October 2016"
                 }
             ],
+            "identifier": "3c016398-9513-4338-8009-f4b0e5886dca",
             "isPartOf": "0429cb38-8d7a-40f4-8459-a5c17cf7a0f5",
+            "keyword": [
+                "agriculture",
+                "nutrition",
+                "Feed the Future",
+                "food security",
+                "interim survey",
+                "Ethiopia"
+            ],
+            "landingPage": "http://www.feedthefuture.gov/country/Ethiopia",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-04-05",
+            "programCode": [
+                "184:029",
+                "184:019",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/Ethiopia_PRIME_IE_IMS1_ReadMe.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_InterimIE_PAS.pdf",
@@ -8820,15 +8825,13 @@
                 "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_IE_IMS_Phase1_Questionnaire.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/EthiopiaPRIME_IE_IMS_Phase2_Questionnaire.pdf"
             ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-M-12-00006",
-            "USAIDsubmittingOrganization": "Westat",
-            "USAIDinitiative": "Feed the Future"
+            "spatial": "Ethiopia",
+            "title": "Feed the Future Ethiopia-PRIME Interim Surveys"
         },
         {
+            "USAIDawardNumber": "AID-442-LA-12-00001",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Michigan State University",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -8837,9 +8840,37 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-04-30",
             "description": "Helping Address Rural Vulnerabilities and Ecosystem Stability (Cambodia-HARVEST) was a five-year program (2011-2016) supported under the Global Hunger and Food Security Initiative (GHFSI) and the Global Climate Change (GCC) and Biodiversity program. Cambodia-HARVEST set strategic goals to improve food security, strengthen natural resource management and resilience to climate change, and increase the capacity of the public and private sectors and civil society to support agricultural competitiveness.  Implemented in four targeted provinces of Cambodia -- Kampong Thom, Siem Reap, Pursat, and Battambang -- Cambodia-HARVEST had five major components: Agribusiness Value Chains; Aquaculture and Fisheries; Natural Resource Management; Biodiversity, and Climate Change, Social Inclusion, Business Development Services; and Capacity Development.  Cambodia-Harvest worked with local partners and government to initiate policy reforms and eliminate obstacles to development.  This data asset enables the evaluation of the program.  It is comprised of a baseline, endline and community level survey.  A report on the baseline survey can be found in the reference pa00k123.pdf",
-            "title": "An Impact Evaluation of Feed the Future Cambodia HARVEST project",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Cambodia-HARVEST_Baseline_Survey_Metadata-Codebook.docx",
+                    "describedByType": "application/msword",
+                    "description": "This dataset is the baseline survey generated in support of an impact evaluation of the Cambodia-Harvest program.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Harvest-Baseline.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "An Impact Evaluation of Feed the Future Cambodia HARVEST Project-Baseline Survey"
+                },
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Cambodia-HARVEST_Endline_Survey_Metadata-Codebook.docx",
+                    "describedByType": "application/msword",
+                    "description": "This dataset is the endline survey generated in support of an impact evaluation of the Cambodia-Harvest program.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Harvest-Endline.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "An Impact Evaluation of Feed the Future Cambodia HARVEST Project-Endline Survey"
+                },
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Cambodia-HARVEST_Community_Survey_Metadata-Codebook.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "The village level community survey on the agriculture, health and nutrition status of the village was conducted by interviewing 2-4 people that were knowledgeable about the village including, mostly village chief, leader of farmer groups, head of the community health center, extension staff, progressive farmer, and community health worker.  The questionnaire collected information on different amenities, facilities and infrastructure present in the community, and various programs of Cambodia-HARVEST focused on increasing incomes to influence nutrition outcomes.  The data provide contextual information about the communities that helps interpretation of the changes at the individual level demonstrated by the baseline-endline pair of surveys.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Harvest-Community.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "An Impact Evaluation of Feed the Future Cambodia HARVEST Project-Community Survey"
+                }
+            ],
+            "identifier": "bab3ccd2-6913-4ab7-af1f-450b975d447f",
             "keyword": [
                 "Cambodia",
                 "HARVEST project",
@@ -8854,48 +8885,20 @@
                 "rice",
                 "aquaculture"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "bab3ccd2-6913-4ab7-af1f-450b975d447f",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2017-04-30",
             "programCode": [
                 "184:029",
                 "184:019",
                 "184:031",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "spatial": "Cambodia",
-            "distribution": [
-                {
-                    "description": "This dataset is the baseline survey generated in support of an impact evaluation of the Cambodia-Harvest program.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Harvest-Baseline.zip",
-                    "format": "Zipped CSV",
-                    "mediaType": "application/zip",
-                    "title": "An Impact Evaluation of Feed the Future Cambodia HARVEST Project-Baseline Survey",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Cambodia-HARVEST_Baseline_Survey_Metadata-Codebook.docx",
-                    "describedByType": "application/msword"
-                },
-                {
-                    "description": "This dataset is the endline survey generated in support of an impact evaluation of the Cambodia-Harvest program.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Harvest-Endline.zip",
-                    "format": "Zipped CSV",
-                    "mediaType": "application/zip",
-                    "title": "An Impact Evaluation of Feed the Future Cambodia HARVEST Project-Endline Survey",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Cambodia-HARVEST_Endline_Survey_Metadata-Codebook.docx",
-                    "describedByType": "application/msword"
+            "publisher": {
+                "name": "USAID"
             },
-                {
-                    "description": "The village level community survey on the agriculture, health and nutrition status of the village was conducted by interviewing 2-4 people that were knowledgeable about the village including, mostly village chief, leader of farmer groups, head of the community health center, extension staff, progressive farmer, and community health worker.  The questionnaire collected information on different amenities, facilities and infrastructure present in the community, and various programs of Cambodia-HARVEST focused on increasing incomes to influence nutrition outcomes.  The data provide contextual information about the communities that helps interpretation of the changes at the individual level demonstrated by the baseline-endline pair of surveys.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Harvest-Community.csv",
-                    "format": "CSV",
-                    "mediaType": "text/csv",
-                    "title": "An Impact Evaluation of Feed the Future Cambodia HARVEST Project-Community Survey",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Cambodia-HARVEST_Community_Survey_Metadata-Codebook.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/English_Cambodia-Harvest_FTF_Baseline_Questionnaire_2008-12-20.docx",
                 "http://www.usaid.gov/opengov/developer/datasets/Khmer_Cambodia-Harvest_FTF_Baseline_Questionnaire_2008-12-20.docx",
@@ -8905,14 +8908,14 @@
                 "http://www.usaid.gov/opengov/developer/datasets/Khmer_Cambodia-Harvest_FTF_Community_Questionnaire_2016-08-30.docx",
                 "http://pdf.usaid.gov/pdf_docs/pa00k123.pdf"
             ],
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-442-LA-12-00001",
-            "USAIDsubmittingOrganization": "Michigan State University",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Cambodia",
+            "title": "An Impact Evaluation of Feed the Future Cambodia HARVEST project"
         },
         {
+            "USAIDInitiative": "Feed the Future",
+            "USAIDawardNumber": "AID-OAA-L-14-00006",
+            "USAIDsubmittingOrganization": "University of California, Davis",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -8921,9 +8924,17 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-04-04",
             "description": "The dataset displays Elevation, Slope, Aspect, Topographic Position Index, Terrain Ruggedness, and Roughness based on Shuttle Radar Topography Mission (SRTM) (3 arc-second) resolution data on a near-global scale (between 56 degrees South and 60 degrees North latitude) and 30 meter (1 arc-second) resolution over United States.",
-            "title": "Tanzania Elevation and Surface Characteristics",
+            "distribution": [
+                {
+                    "description": "The dataset displays Elevation, Slope, Aspect, Topographic Position Index, Terrain Ruggedness, and Roughness based on Shuttle Radar Topography Mission (SRTM) (3 arc-second) resolution data on a near-global scale (between 56 degrees South and 60 degrees North latitude) and 30 meter (1 arc-second) resolution over United States.",
+                    "downloadURL": "http://gfc.ucdavis.edu/data/tza/TZA_topo.zip",
+                    "format": "Zipped Files",
+                    "mediaType": "application/zip",
+                    "title": "Tanzania Elevation and Surface Characteristics"
+                }
+            ],
+            "identifier": "2468acfb-f3ee-401f-98d8-a4ee174ab30c",
             "keyword": [
                 "Elevation",
                 "Slope",
@@ -8933,33 +8944,25 @@
                 "Roughness",
                 "Tanzania"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "2468acfb-f3ee-401f-98d8-a4ee174ab30c",
+            "landingPage": "http://gfc.ucdavis.edu",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2017-04-04",
             "programCode": [
                 "184:029"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "distribution": [
-                {
-                    "description": "The dataset displays Elevation, Slope, Aspect, Topographic Position Index, Terrain Ruggedness, and Roughness based on Shuttle Radar Topography Mission (SRTM) (3 arc-second) resolution data on a near-global scale (between 56 degrees South and 60 degrees North latitude) and 30 meter (1 arc-second) resolution over United States.",
-                    "downloadURL": "http://gfc.ucdavis.edu/data/tza/TZA_topo.zip",
-                    "format": "Zipped Files",
-                    "mediaType": "application/zip",
             "title": "Tanzania Elevation and Surface Characteristics"
-                }
-            ],
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "http://gfc.ucdavis.edu",
-            "USAIDawardNumber": "AID-OAA-L-14-00006",
-            "USAIDsubmittingOrganization": "University of California, Davis",
-            "USAIDInitiative": "Feed the Future"
         },
         {
+            "USAIDawardNumber": "AID-ECG-A-00-07-0001",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Innovation Lab for Collaborative Research on Peanut",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -8968,9 +8971,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-04-06",
             "description": "The data was produced as part of the Feed the Future Innovation Lab for Collaborative Research on Peanut Productivity and Aflatoxin Control (the Peanut & Mycotoxin Innovation Lab, PMIL) subaward to the USDA Agricultural Research Service's National Peanut Research Lab in Dawson, GA entitled, Silencing of Aflatoxin Synthesis through RNA Interfence (RNAi) in Peanut Plants. The project has two main objectives, to study the genetic diversity of Aspergillus species collected in PMIL target countries and the USA, and to develop peanut lines containing RNAi gene constructs to reduce aflatoxin contamination by Aspergillus flavus infection. The data were produced as part of the first objective on genetic diversity. The genomes are available at National Center for Biotechnology Information (NCBI) database found at the landing page identified below using the numbers listed in the reference AccessionNumbers.txt.",
-            "title": "Genomic sequences of Aspergillus flavus accessions in Georgia USA",
+            "identifier": "a20ff98b-b355-443c-8d1d-570ef2517990",
             "keyword": [
                 "genome",
                 " aspergillus flavus",
@@ -8978,30 +8980,31 @@
                 " peanut",
                 "agriculture"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "a20ff98b-b355-443c-8d1d-570ef2517990",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "landingPage": "http://www.ncbi.nlm.nih.gov/",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-04-06",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/AccessionNumbers.txt",
                 "http://www.usaid.gov/opengov/developer/datasets/Publication_Journal_Faustinelli_USDA201_Arias_2016-04-14_GenomeSequencesofEightAspergillusFlavusSPPAndOneAParasiticusSPIsolatedFromPeanutSeedsInGA,pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Publication_Journal_Arias_USDA201_Arias_2015-RNAi-medicatedControlOfAflatoxinInPeanutMethodToAnalyzeMycotoxinProductionAndTransgeneExpressionInThePeanut.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Publication_Abstract_Faustinelli_USDA201_Arias_2016-03-05_WorkflowToStudyGeneticBiodiversityOfAflatoxigenicAspergillusSPP.pdf"
             ],
-            "USAIDawardNumber": "AID-ECG-A-00-07-0001",
-            "USAIDsubmittingOrganization": "Innovation Lab for Collaborative Research on Peanut",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Genomic sequences of Aspergillus flavus accessions in Georgia USA"
         },
         {
+            "USAIDawardNumber": "BFS-G-11-00002",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "US Borlaug Fellows in Global Food Security",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9010,9 +9013,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-07-12",
             "description": "This dataset will contain phenotypic observations of a large number of wheat genotypes evaluated in 2016-2017 and 2017-2018 at the International Maize and Wheat Improvement Center in Ciudad Obregon, Mexico.",
-            "title": "Wheat Breeding Technologies for a Shifting Global Climate",
+            "identifier": "7ddcc326-b09d-4702-bd45-79b766301e6b",
             "keyword": [
                 "wheat",
                 "plant breeding",
@@ -9021,24 +9023,24 @@
                 "abiotic stress",
                 "climate change"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "7ddcc326-b09d-4702-bd45-79b766301e6b",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "landingPage": "https://www.ncbi.nlm.nih.gov/sra/?term=SRP056743",
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "BFS-G-11-00002",
-            "USAIDsubmittingOrganization": "US Borlaug Fellows in Global Food Security",
-            "USAIDinitiative": "Feed the Future"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-07-12",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Wheat Breeding Technologies for a Shifting Global Climate"
         },
         {
+            "USAIDawardNumber": "BFS-G-11-00002",
+            "USAIDsubmittingOrganization": "US Borlaug Fellows in Global Food Security",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9047,91 +9049,91 @@
                 "fn": "Clara Cohen",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-01-13",
             "description": "A set of recent CIMMYT era hybrids - spanning from the early 1990s to the late 2000s - was analyzed. The hybrids were grown in four different environments in two locations in Mexico: High nitrogen (HN) and low nitrogen (LN) in Agua Fria, and well watered (WW) and water stressed (WS) in Tlaltizapan. A hyperspectral spectrometer was used to take leaf level reflectance data weekly on all plots from late vegetative stages to maturity. In addition, other typical agronomic traits were recorded: grain yield, plant height, ear height, root and stalk lodging, etc. This dataset also contains vegetation indices that have already been calculated for each plot on each sampling date. The data was used to see how traits changed in CIMMYT hybrids over time.",
-            "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids",
-            "keyword": [
-                "agriculture",
-                "CIMMYT",
-                "era hybrids",
-                "maize",
-                "vegetation indices",
-                "hyperspectral sensor",
-                "water stress",
-                "nitrogen stress"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "90fe43bb-2bca-49b2-b0f4-15bb6c8cd4d1",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
+                    "describedByType": "text/csv",
                     "description": "A set of recent CIMMYT era hybrids - spanning from the early 1990s to the late 2000s - was analyzed. These data are the results of a hyperspectral spectrometer analysis done in a high nitrogen environment in Agua Fria.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/AFHNReflectance.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Leaf Level Reflectance Data in a High Nitrogen Environment in Agua Fria",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
-                    "describedByType": "text/csv"
+                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Leaf Level Reflectance Data in a High Nitrogen Environment in Agua Fria"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
+                    "describedByType": "text/csv",
                     "description": "A set of recent CIMMYT era hybrids - spanning from the early 1990s to the late 2000s - was analyzed. These data are the results of a hyperspectral spectrometer analysis done in a high nitrogen environment in Agua Fria.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/AFLNReflectance.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Leaf Level Reflectance Data in a Low Nitrogen Environment in Agua Fria",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
-                    "describedByType": "text/csv"
+                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Leaf Level Reflectance Data in a Low Nitrogen Environment in Agua Fria"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
+                    "describedByType": "text/csv",
                     "description": "A set of recent CIMMYT era hybrids - spanning from the early 1990s to the late 2000s - was analyzed. These data are the results of a hyperspectral spectrometer analysis done in a water stressed environment in Tlaltizapan.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/TLWSReflectance.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Leaf Level Reflectance Data in a Water Stressed Environment in Tlaltizapan",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
-                    "describedByType": "text/csv"
+                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Leaf Level Reflectance Data in a Water Stressed Environment in Tlaltizapan"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
+                    "describedByType": "text/csv",
                     "description": "A set of recent CIMMYT era hybrids - spanning from the early 1990s to the late 2000s - was analyzed. These data are the results of a hyperspectral spectrometer analysis done in a well watered environment in Tlaltizapan.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/TLWWReflectance.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Leaf Level Reflectance Data in a Well Watered Environment in Tlaltizapan.",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
-                    "describedByType": "text/csv"
+                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Leaf Level Reflectance Data in a Well Watered Environment in Tlaltizapan."
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
+                    "describedByType": "text/csv",
                     "description": "A set of recent CIMMYT era hybrids - spanning from the early 1990s to the late 2000s - was analyzed. These data show the agronomic traits for maize hybrids in Agua Fria.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/AguaFriaera.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Agronomic Traits for Maize Hybrids in Agua Fria.",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
-                    "describedByType": "text/csv"
+                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Agronomic Traits for Maize Hybrids in Agua Fria."
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
+                    "describedByType": "text/csv",
                     "description": "A set of recent CIMMYT era hybrids - spanning from the early 1990s to the late 2000s - was analyzed. These data show the agronomic traits for maize hybrids in Tlaltizapan.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Tlaltiera.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Agronomic Traits for Maize Hybrids in Agua Fria.",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Leaf-level_Hyperspectral_Reflectance_Codebook.csv",
-                    "describedByType": "text/csv"
+                    "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids - Agronomic Traits for Maize Hybrids in Agua Fria."
                 }
             ],
+            "identifier": "90fe43bb-2bca-49b2-b0f4-15bb6c8cd4d1",
+            "keyword": [
+                "agriculture",
+                "CIMMYT",
+                "era hybrids",
+                "maize",
+                "vegetation indices",
+                "hyperspectral sensor",
+                "water stress",
+                "nitrogen stress"
+            ],
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "BFS-G-11-00002",
-            "USAIDsubmittingOrganization": "US Borlaug Fellows in Global Food Security"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2017-01-13",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Using Leaf-level Hyperspectral Reflectance Data to Analyze Genetic Gain in CIMMYT Maize Hybrids"
         },
         {
+            "USAIDawardNumber": "BFS-G-11-00002",
+            "USAIDsubmittingOrganization": "US Borlaug Fellows in Global Food Security",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9140,9 +9142,19 @@
                 "fn": "Clara Cohen",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-10-22",
             "description": "The data are the phenotypic host reactions of a recombinant inbred line population of Capsicum annuum developed to differentiate races of Phytophthora capsici. The New Mexico Recombinant Inbred Line (NMRIL) is an F8 population derived from a hybridization between ?Early Jalapeno? (susceptible parent) and Criollo de Morelos 334 (CM334) (resistant parent). The controls include CM334 (negative control) and New Mexico Capsicum Accession 10399 (NMCA10399) (positive control). Also included are the World Vegetable Center host differentials including ?Early Calwonder? (EC), PI 201234, PBC137, and PBC602. The host differentials were screened with isolates of P. capsici that were collected from chile pepper production regions of Taiwan (Republic of China) in 2016 as well as Race 1, 2, and 3 of P. capsici from the World Vegetable Center collection at a concentration of 10,000 zoospores per plant. The plants were scored at ~2 weeks after inoculation and only those with an average score of = 1 were considered resistant. The experiment included 6 plants per replication with two replications and each test was repeated twice. The data would be best used by individuals interested in population structure, virulence, or sources of resistance to the oomycetes plant pathogen Phytophthora capsici.  ",
-            "title": "Disease Severity Rating of Chile Pepper Plants Inoculated with Phytophthora Capsici Collected in Taiwan",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Disease_Severity_Ratings_Codebook.docx",
+                    "describedByType": "text/csv",
+                    "description": "The data are the phenotypic host reactions of a recombinant inbred line population of Capsicum annuum developed to differentiate races of Phytophthora capsici. The New Mexico Recombinant Inbred Line (NMRIL) is an F8 population derived from a hybridization between ?Early Jalapeno? (susceptible parent) and Criollo de Morelos 334 (CM334) (resistant parent). The controls include CM334 (negative control) and New Mexico Capsicum Accession 10399 (NMCA10399) (positive control). Also included are the World Vegetable Center host differentials including ?Early Calwonder? (EC), PI 201234, PBC137, and PBC602. The host differentials were screened with isolates of P. capsici that were collected from chile pepper production regions of Taiwan (Republic of China) in 2016 as well as Race 1, 2, and 3 of P. capsici from the World Vegetable Center collection at a concentration of 10,000 zoospores per plant. The plants were scored at ~2 weeks after inoculation and only those with an average score of = 1 were considered resistant. The experiment included 6 plants per replication with two replications and each test was repeated twice. The data would be best used by individuals interested in population structure, virulence, or sources of resistance to the oomycetes plant pathogen Phytophthora capsici.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Disease_Severity_Ratings_Data.CSV",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "Disease Severity Rating of Chile Pepper Plants Inoculated with Phytophthora Capsici Collected in Taiwan"
+                }
+            ],
+            "identifier": "135210fd-86e2-4ec3-877d-a2fbaffbb9f9",
             "keyword": [
                 "chile pepper",
                 "Phytophthora capsici",
@@ -9158,33 +9170,24 @@
                 "root-rot",
                 "recombination inbred lines"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "135210fd-86e2-4ec3-877d-a2fbaffbb9f9",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-10-22",
             "programCode": [
                 "184:029"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "distribution": [
-                {
-                    "description": "The data are the phenotypic host reactions of a recombinant inbred line population of Capsicum annuum developed to differentiate races of Phytophthora capsici. The New Mexico Recombinant Inbred Line (NMRIL) is an F8 population derived from a hybridization between ?Early Jalapeno? (susceptible parent) and Criollo de Morelos 334 (CM334) (resistant parent). The controls include CM334 (negative control) and New Mexico Capsicum Accession 10399 (NMCA10399) (positive control). Also included are the World Vegetable Center host differentials including ?Early Calwonder? (EC), PI 201234, PBC137, and PBC602. The host differentials were screened with isolates of P. capsici that were collected from chile pepper production regions of Taiwan (Republic of China) in 2016 as well as Race 1, 2, and 3 of P. capsici from the World Vegetable Center collection at a concentration of 10,000 zoospores per plant. The plants were scored at ~2 weeks after inoculation and only those with an average score of = 1 were considered resistant. The experiment included 6 plants per replication with two replications and each test was repeated twice. The data would be best used by individuals interested in population structure, virulence, or sources of resistance to the oomycetes plant pathogen Phytophthora capsici.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Disease_Severity_Ratings_Data.CSV",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "Disease Severity Rating of Chile Pepper Plants Inoculated with Phytophthora Capsici Collected in Taiwan",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Disease_Severity_Ratings_Codebook.docx",
-                    "describedByType": "text/csv"
-                }
-            ],
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "BFS-G-11-00002",
-            "USAIDsubmittingOrganization": "US Borlaug Fellows in Global Food Security"
+            "title": "Disease Severity Rating of Chile Pepper Plants Inoculated with Phytophthora Capsici Collected in Taiwan"
         },
         {
+            "USAIDInitiative": "Feed the Future",
+            "USAIDawardNumber": "BFS-G-11-00002",
+            "USAIDsubmittingOrganization": "US Borlaug Fellows in Global Food Security",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9193,24 +9196,7 @@
                 "fn": "Clara Cohen",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-02-24",
             "description": "Fresh weight and leaf area measurements were taken of 12 varieties of amaranth (Amaranthus cruentus) and nightshade (Solanum spp.) each after field plots were harvested.  Plants were arranged in a randomized complete block design with two replicates.  Six of the twelve varieties of each species were formal seed while the others were purchased through informal networks.",
-            "title": "Supporting Formal and Informal Seed Systems for African Leafy Vegetables",
-            "keyword": [
-                "Seed systems",
-                "African leafy vegetables",
-                "Fresh weight",
-                "Leaf Area"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "28b63453-0d47-4915-b0bd-d4785f054bc5",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
                     "description": "Fresh weight and leaf area measurements were taken of 12 varieties of amaranth (Amaranthus cruentus) and nightshade (Solanum spp.) each after field plots were harvested.  This is the first replicate of a randomized complete block design as a CSV file.",
@@ -9234,14 +9220,31 @@
                     "title": "Supporting Formal and Informal Seed Systems for African Leafy Vegetables"
                 }
             ],
+            "identifier": "28b63453-0d47-4915-b0bd-d4785f054bc5",
+            "keyword": [
+                "Seed systems",
+                "African leafy vegetables",
+                "Fresh weight",
+                "Leaf Area"
+            ],
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "BFS-G-11-00002",
-            "USAIDsubmittingOrganization": "US Borlaug Fellows in Global Food Security",
-            "USAIDInitiative": "Feed the Future"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-02-24",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Supporting Formal and Informal Seed Systems for African Leafy Vegetables"
         },
         {
+            "USAIDawardNumber": "AID-OAA-A-13-00070",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "University of California, Riverside",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9250,9 +9253,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-06-29",
             "description": "Nucleotide sequences were generated from 37 cowpea (Vigna unguiculata L. Walp.) accessions relevant to Africa, China and the USA to discover at type of genetic variation called single nucleotide polymorphism (SNP). These accessions were chosen to represent the geographic, phenotypic and genetic diversity of cultivated cowpea. Approximately 1 million SNPs were identified, from which a research tool was developed for genetic fingerprinting using 51,128 of these SNPs.  This tool is call the Cowpea iSelect Consortium Array and is available from the US company Illumina (Illumina Inc., San Diego, CA, USA; http://www.illumina.com/areas-of-interest/agrigenomics/consortia.html)",
-            "title": "Nucleotide sequences from the genomes of diverse cowpea accessions for discovery of genetic variation as part of the Feed the Future Innovation Lab for Climate Resilient Cowpea",
+            "identifier": "9ee1bb76-0698-45ad-b253-addae2542d98",
             "keyword": [
                 "Cowpea",
                 "food security",
@@ -9265,29 +9267,30 @@
                 "resilience",
                 "agriculture"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "9ee1bb76-0698-45ad-b253-addae2542d98",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/sra/?term=SRP077082",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-06-29",
             "programCode": [
                 "184:019",
                 "184:021",
                 "184:029"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/sra/?term=SRP077082",
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://onlinelibrary.wiley.com/doi/10.1111/tpj.13404/full"
             ],
-            "USAIDawardNumber": "AID-OAA-A-13-00070",
-            "USAIDsubmittingOrganization": "University of California, Riverside",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Nucleotide sequences from the genomes of diverse cowpea accessions for discovery of genetic variation as part of the Feed the Future Innovation Lab for Climate Resilient Cowpea"
         },
         {
+            "USAIDInitiative": "Feed the Future",
+            "USAIDawardNumber": "EDH-A-00-07-00005",
+            "USAIDsubmittingOrganization": "Michigan State University",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9296,9 +9299,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-06-24",
             "description": "This dataset contains the complete mitochondrial genome of Anoplocnemis curvipes F. (Coreinea, Coreidae, Heteroptera), a pest of fresh cowpea pods.  To get to the data please navigate to: https://www.ncbi.nlm.nih.gov/nuccore/KY906099, https://www.ncbi.nlm.nih.gov/nuccore/KY274846, https://www.ncbi.nlm.nih.gov/nuccore/KX447141 and https://www.ncbi.nlm.nih.gov/nuccore/KX447142",
-            "title": "Genomics Data for Cowpea Pests in Africa",
+            "identifier": "3eeb2d9c-44aa-4572-8649-6b6f5bf95dfc",
             "keyword": [
                 "Anoplocnemis curvipes",
                 "mitochondrial genome",
@@ -9307,18 +9309,17 @@
                 "Africa",
                 "Cowpea pests"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "3eeb2d9c-44aa-4572-8649-6b6f5bf95dfc",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2017-06-24",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.tandfonline.com/doi/abs/10.1080/23802359.2017.1347829",
                 "http://www.usaid.gov/opengov/developer/datasets/The_mitogenome_of_the_brown_pod-sucking_bug_Clavigralla_tomentosicollis.rtf",
@@ -9329,11 +9330,13 @@
                 "http://www.usaid.gov/opengov/developer/datasets/readmeClavigralla_tomentosicollisMit102717.txt",
                 "http://www.usaid.gov/opengov/developer/datasets/readMeMaruca_vitrata_Mit102717"
             ],
-            "USAIDawardNumber": "EDH-A-00-07-00005",
-            "USAIDsubmittingOrganization": "Michigan State University",
-            "USAIDInitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Genomics Data for Cowpea Pests in Africa"
         },
         {
+            "USAIDawardNumber": "AID-OAA-A-13-00080",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "University of California, Davis",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9342,9 +9345,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-09-29",
             "description": "To determine the gender impact on the immune response of chickens, the mRNA was isolated and sequenced from the lungs of 48 chickens of 2 lines as three time-points post-infection (2,6, and 10 days post-infection), and in two treatment groups. The data can be retrieved by navigating to https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-5859/.",
-            "title": "Lung Transcriptome Data from Chickens with Newcastle Disease Virus--Impact of  Gender Immune Response",
+            "identifier": "fcf6cefe-3dc9-43d6-bb9e-b4705ea4b2ee",
             "keyword": [
                 "chicken",
                 "poultry",
@@ -9354,27 +9356,28 @@
                 "virus",
                 "gender"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "fcf6cefe-3dc9-43d6-bb9e-b4705ea4b2ee",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "landingPage": "https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-5859/",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2017-09-29",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://lib.dr.iastate.edu/ans_air/vol663/iss1/50/"
             ],
-            "USAIDawardNumber": "AID-OAA-A-13-00080",
-            "USAIDsubmittingOrganization": "University of California, Davis",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Lung Transcriptome Data from Chickens with Newcastle Disease Virus--Impact of  Gender Immune Response"
         },
         {
+            "USAIDawardNumber": "AID-OAA-A-13-00080",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "University of California, Davis",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9383,9 +9386,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-09-29",
             "description": "Males and females from resistant Fayoumi and susceptible Leghorn chicken lines were either challenged with a lentogenic strain of Newcastle Disease virus or given a mock infection at 3 weeks of age.  The lung transcriptomes generated by RNA-sequencing were studied using contrasts across the challenged and non-challenged birds, the two lines, and three time points (2,6, and 10 days post-infection) using Weighted Gene Co-expression Network Analysis (WGNCA).  The data can be retrieved by navigating to https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-5859/.",
-            "title": "Lung Transcriptome of Newcastle Disease Virus Infected Chickens--Different Immune Response in Two Types of Chicken",
+            "identifier": "bf0809bb-516c-4dbc-895e-0cf302360bcf",
             "keyword": [
                 "chicken",
                 "poultry",
@@ -9394,27 +9396,27 @@
                 "RNA",
                 "transcriptome"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "bf0809bb-516c-4dbc-895e-0cf302360bcf",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "landingPage": "https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-5859/",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2017-09-29",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://rdcu.be/Dx0E"
             ],
-            "USAIDawardNumber": "AID-OAA-A-13-00080",
-            "USAIDsubmittingOrganization": "University of California, Davis",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Lung Transcriptome of Newcastle Disease Virus Infected Chickens--Different Immune Response in Two Types of Chicken"
         },
         {
+            "USAIDawardNumber": "AID-OAA-A-13-00002",
+            "USAIDsubmittingOrganization": "University of California, San Diego",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9423,26 +9425,7 @@
                 "fn": "Tim Essam",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-12-11",
             "description": "The dataset contains the following. 1) Voltammograms of PBS spiked with various concentrations of Ferro/Ferri, a commonly used  reversible redox pair, measured using both a benchtop tool and smartphone-based biosensor.  2) Voltammograms (N=3) of different concentrations of Secretory leukocyte protease inhibitor (SLPI) in PBS along with extracted and averaged peak data.  SLPI is a biomarker that plays anti-microbial and anti-inflammatory roles within the body. It has been shown that decreased levels of SLPI in sputum, the mucus coughed out of the lungs of individuals with cystic fibrosis, indicates a Pseudomonas aeruginosa infection. For more information, refer to Sun, Alexander C., et al. An efficient power harvesting mobile phone-based electrochemical biosensor for point-of-care health monitoring. Sensors and Actuators B- Chemical 235 (2016): 126-135.",
-            "title": "Secretory Leukocyte Protease Inhibitor Assay Measurement Results Taken By a  Mobile Phone-based Biosensor",
-            "keyword": [
-                "smartphone",
-                "mHealth",
-                "point-of-care",
-                "electrochemical biosensor",
-                "secretory leukocyte protease inhibitor",
-                "cystic fibrosis"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "357d98b1-4374-4f12-914e-07e9a45dc54a",
-            "programCode": [
-                "184:021"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
                     "description": "This dataset consists of a zipped file which, when unzipped, yields four distinct files.  1) Voltammograms of PBS spiked with various concentrations of Ferro/Ferri, a commonly used  reversible redox pair, measured using both a benchtop tool and smartphone-based biosensor.  2) Voltammograms (N=3) of different concentrations of Secretory leukocyte protease inhibitor (SLPI) in PBS along with extracted and averaged peak data.  SLPI is a biomarker that plays anti-microbial and anti-inflammatory roles within the body. It has been shown that decreased levels of SLPI in sputum, the mucus coughed out of the lungs of individuals with cystic fibrosis, indicates a Pseudomonas aeruginosa infection. For more information, refer to Sun, Alexander C., et al. An efficient power harvesting mobile phone-based electrochemical biosensor for point-of-care health monitoring. Sensors and Actuators B- Chemical 235 (2016): 126-135.",
@@ -9452,14 +9435,33 @@
                     "title": "Secretory Leukocyte Protease Inhibitor Assay Measurement Results Taken By a  Mobile Phone-based Biosensor"
                 }
             ],
+            "identifier": "357d98b1-4374-4f12-914e-07e9a45dc54a",
+            "keyword": [
+                "smartphone",
+                "mHealth",
+                "point-of-care",
+                "electrochemical biosensor",
+                "secretory leukocyte protease inhibitor",
+                "cystic fibrosis"
+            ],
+            "landingPage": "https://osf.io/zhu89",
             "language": [
                 "en-US"
             ],
-            "landingPage": "https://osf.io/zhu89",
-            "USAIDawardNumber": "AID-OAA-A-13-00002",
-            "USAIDsubmittingOrganization": "University of California, San Diego"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-12-11",
+            "programCode": [
+                "184:021"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Secretory Leukocyte Protease Inhibitor Assay Measurement Results Taken By a  Mobile Phone-based Biosensor"
         },
         {
+            "USAIDawardNumber": "AID-OAA-A-13-00002",
+            "USAIDsubmittingOrganization": "University of California, San Diego",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9468,9 +9470,13 @@
                 "fn": "Tim Essam",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2018-03-19",
             "description": "Portable and easy-to-use point-of-care (POC) diagnostic devices hold high promise for dramatically improving public health and wellness. In this paper, we present a mobile health immunoassay platform based on audio jack-embedded devices, such as smartphones and laptops, that uses electrochemical impedance spectroscopy to detect binding of target biomolecules. This platform is intended to be used as a plug-and-play peripheral that reuses existing hardware in the mobile device, and does not require an external battery, thereby improving upon its convenience and portability. Experimental data using a passive circuit network to mimic an electrochemical cell demonstrate that the device performs comparable to laboratory grade instrumentation with 0.3% and 0.5\udcb0 magnitude and phase error, respectively, over a 17 Hz-17 kHz frequency range. The measured power consumption is 2.5 mW with a dynamic range of 60 dB. This platform was verified by monitoring the real-time formation of a NeutrAvidin self-assembled monolayer on a gold electrode demonstrating the potential for POC diagnostics.",
-            "title": "An Audio Jack-Based Electrochemical Impedance Spectroscopy Sensor for Point-of-Care Diagnostics",
+            "distribution": [
+                {
+                    "description": "Portable and easy-to-use point-of-care (POC) diagnostic devices hold high promise for dramatically improving public health and wellness. In this paper, we present a mobile health immunoassay platform based on audio jack-embedded devices, such as smartphones and laptops, that uses electrochemical impedance spectroscopy to detect binding of target biomolecules. This platform is intended to be used as a plug-and-play peripheral that reuses existing hardware in the mobile device, and does not require an external battery, thereby improving upon its convenience and portability. Experimental data using a passive circuit network to mimic an electrochemical cell demonstrate that the device performs comparable to laboratory grade instrumentation with 0.3% and 0.5\udcb0 magnitude and phase error, respectively, over a 17 Hz-17 kHz frequency range. The measured power consumption is 2.5 mW with a dynamic range of 60 dB. This platform was verified by monitoring the real-time formation of a NeutrAvidin self-assembled monolayer on a gold electrode demonstrating the potential for POC diagnostics.",
+                    "downloadURL": "https://osf.io/xkun8/download",
+                    "format": "Zipped Files",
+                    "identifier": "639ca81a-3e3c-49ca-82cd-6000e6801db1",
                     "keyword": [
                         "Electrochemical impedance spectroscopy",
                         "mHealth",
@@ -9478,18 +9484,14 @@
                         "point-of-care testing",
                         "electrochemical sensors"
                     ],
+                    "mediaType": "application/zip",
                     "publisher": {
                         "name": "USAID"
                     },
-            "identifier": "639ca81a-3e3c-49ca-82cd-6000e6801db1",
-            "programCode": [
-                "184:021"
+                    "title": "An Audio Jack-Based Electrochemical Impedance Spectroscopy Sensor for Point-of-Care Diagnostics"
+                }
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "distribution": [
-                {
-                    "description": "Portable and easy-to-use point-of-care (POC) diagnostic devices hold high promise for dramatically improving public health and wellness. In this paper, we present a mobile health immunoassay platform based on audio jack-embedded devices, such as smartphones and laptops, that uses electrochemical impedance spectroscopy to detect binding of target biomolecules. This platform is intended to be used as a plug-and-play peripheral that reuses existing hardware in the mobile device, and does not require an external battery, thereby improving upon its convenience and portability. Experimental data using a passive circuit network to mimic an electrochemical cell demonstrate that the device performs comparable to laboratory grade instrumentation with 0.3% and 0.5\udcb0 magnitude and phase error, respectively, over a 17 Hz-17 kHz frequency range. The measured power consumption is 2.5 mW with a dynamic range of 60 dB. This platform was verified by monitoring the real-time formation of a NeutrAvidin self-assembled monolayer on a gold electrode demonstrating the potential for POC diagnostics.",
+            "identifier": "639ca81a-3e3c-49ca-82cd-6000e6801db1",
             "keyword": [
                 "Electrochemical impedance spectroscopy",
                 "mHealth",
@@ -9497,24 +9499,25 @@
                 "point-of-care testing",
                 "electrochemical sensors"
             ],
+            "landingPage": "https://osf.io/xkun8",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2018-03-19",
+            "programCode": [
+                "184:021"
+            ],
             "publisher": {
                 "name": "USAID"
             },
-                    "identifier": "639ca81a-3e3c-49ca-82cd-6000e6801db1",
-                    "downloadURL": "https://osf.io/xkun8/download",
-                    "format": "Zipped Files",
-                    "mediaType": "application/zip",
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "title": "An Audio Jack-Based Electrochemical Impedance Spectroscopy Sensor for Point-of-Care Diagnostics"
-                }
-            ],
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://osf.io/xkun8",
-            "USAIDawardNumber": "AID-OAA-A-13-00002",
-            "USAIDsubmittingOrganization": "University of California, San Diego"
         },
         {
+            "USAIDawardNumber": "BFS-G-11-00002",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "Columbia University",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9523,31 +9526,7 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-11-02",
             "description": "This dataset is comprosed of three distinct spreadsheets covering regional production from the Ministry of Agricuture, household-level production data, and  crop nutrient data for Kedougou, Senegal.",
-            "title": "Kedougou Nutrient Diversity",
-            "keyword": [
-                "nutrition",
-                "Senegal",
-                "Kedougou",
-                "agriculture",
-                "Fonio",
-                "Green Revolution",
-                "nutrition indicators",
-                "agroecology",
-                "smallholder agriculture",
-                "crop diversity"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0ff1182f-148f-4f33-a23d-6676ba674c3d",
-            "programCode": [
-                "184:019",
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
                     "description": "This dataset contains regional-scale production data from the Ministry of Agriculture office in Kedougou, Senegal. Production estimates are collected annually for the region by extension agents who combine survey-based yield estimates with direct, in-field yield measurements. Data are aggregated to the department and regional level.  The data covers the years 2010-2012 because before 2010 data were only available for a small number of crops and/or had missing data points.",
@@ -9571,19 +9550,43 @@
                     "title": "Kedougou Nutrient Diversity, Crop Nutrient Data"
                 }
             ],
+            "identifier": "0ff1182f-148f-4f33-a23d-6676ba674c3d",
+            "keyword": [
+                "nutrition",
+                "Senegal",
+                "Kedougou",
+                "agriculture",
+                "Fonio",
+                "Green Revolution",
+                "nutrition indicators",
+                "agroecology",
+                "smallholder agriculture",
+                "crop diversity"
+            ],
             "landingPage": "https://knb.ecoinformatics.org/#view/doi:10.5063/F11Z42JX",
-            "spatial": "Senegal",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2017-11-02",
+            "programCode": [
+                "184:019",
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://onlinelibrary.wiley.com/doi/10.1111/1365-2664.13026/full"
             ],
-            "USAIDawardNumber": "BFS-G-11-00002",
-            "USAIDsubmittingOrganization": "Columbia University",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Senegal",
+            "title": "Kedougou Nutrient Diversity"
         },
         {
+            "USAIDawardNumber": "AID-OAA-A-13-00080",
+            "USAIDinitiative": "Feed the Future",
+            "USAIDsubmittingOrganization": "University of California, Davis",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9592,9 +9595,8 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-07-06",
             "description": "At 21 days of age, chickens were infected with Newcastle Disease virus (or a mock injection as controls), and spleens were harvested at 2 and 6 days post infection.  Messenger RNA (mRNA) was sequenced.  The data can be retrieved by navigating to https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-5851/.",
-            "title": "RNA Sequence of Spleen of Newcastle Disease Infected Chickens",
+            "identifier": "9d0bd27b-cd54-4d77-9079-e4852009bebe",
             "keyword": [
                 "chicken",
                 "spleen",
@@ -9604,25 +9606,23 @@
                 "virus",
                 "genetics"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "9d0bd27b-cd54-4d77-9079-e4852009bebe",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "landingPage": "https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-5851/",
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2017-07-06",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=2291&context=ans_air"
             ],
-            "USAIDawardNumber": "AID-OAA-A-13-00080",
-            "USAIDsubmittingOrganization": "University of California, Davis",
-            "USAIDinitiative": "Feed the Future"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "RNA Sequence of Spleen of Newcastle Disease Infected Chickens"
         },
         {
             "accessLevel": "public",
@@ -9633,9 +9633,19 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-03-24",
             "description": "Aflatoxins (AFs) are hepatocarcinogenic mycotoxins that can contaminate grains and oil seeds in tropical and sub-tropical areas and have been detected in maize and peanut products of Haiti. The first objective of the study was to assess human exposure to AFs among Haitians at an urban hospital (GHESKIO) and a rural health centre (HCBH). The second objective was to test the association between AF exposure and reported dietary intake of potentially contaminated foods, such as maize, peanut products and milk. Subjects were recruited at the Groupe Haitien d?Etude du Sarcome de Kaposi et des Infections Opportunistes Health Centre in Port-au-Prince (GHESKIO, n = 147) from 9?24 July 2012, and at the H?pital Convention Baptiste d?Ha?ti in Quartier Morin (HCBH, n = 191) from 9 September 2013 to 7 February 2014. At HCBH, study subjects also included minors (1?17.9 years of age, n = 28). Intake of dairy, other animal-sourced foods, peanut products and maize was assessed using a dietary recall survey. Aflatoxin exposure was assessed by measurement of urinary Aflatoxin M1 using high pressure liquid chromatography.",
-            "title": "Cross-sectional Survey of Urinary Aflatoxins and Diet Recall in Haiti",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_Urine_Biomarker_and_Diet_Survey_Key.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "Aflatoxins (AFs) are hepatocarcinogenic mycotoxins that can contaminate grains and oil seeds in tropical and sub-tropical areas and have been detected in maize and peanut products of Haiti. The first objective of the study was to assess human exposure to AFs among Haitians at an urban hospital (GHESKIO) and a rural health centre (HCBH). The second objective was to test the association between AF exposure and reported dietary intake of potentially contaminated foods, such as maize, peanut products and milk. Subjects were recruited at the Groupe Haitien d?Etude du Sarcome de Kaposi et des Infections Opportunistes Health Centre in Port-au-Prince (GHESKIO, n = 147) from 9?24 July 2012, and at the H?pital Convention Baptiste d?Ha?ti in Quartier Morin (HCBH, n = 191) from 9 September 2013 to 7 February 2014. At HCBH, study subjects also included minors (1?17.9 years of age, n = 28). Intake of dairy, other animal-sourced foods, peanut products and maize was assessed using a dietary recall survey. Aflatoxin exposure was assessed by measurement of urinary Aflatoxin M1 using high pressure liquid chromatography.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/AFM1_Survey_and_HPLC_data-2012-2013_RECALIBRATED.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "Cross-sectional Survey of Urinary Aflatoxins and Diet Recall in Haiti"
+                }
+            ],
+            "identifier": "1d03206b-8fba-4518-87d5-bd0412f7ffe3",
             "keyword": [
                 "Nutrition",
                 "Aflatoxin",
@@ -9644,36 +9654,29 @@
                 "Biomarkers",
                 "Nutritional Toxicology"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "1d03206b-8fba-4518-87d5-bd0412f7ffe3",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-03-24",
             "programCode": [
                 "184:019",
                 "184:029"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "spatial": "Haiti",
-            "distribution": [
-                {
-                    "description": "Aflatoxins (AFs) are hepatocarcinogenic mycotoxins that can contaminate grains and oil seeds in tropical and sub-tropical areas and have been detected in maize and peanut products of Haiti. The first objective of the study was to assess human exposure to AFs among Haitians at an urban hospital (GHESKIO) and a rural health centre (HCBH). The second objective was to test the association between AF exposure and reported dietary intake of potentially contaminated foods, such as maize, peanut products and milk. Subjects were recruited at the Groupe Haitien d?Etude du Sarcome de Kaposi et des Infections Opportunistes Health Centre in Port-au-Prince (GHESKIO, n = 147) from 9?24 July 2012, and at the H?pital Convention Baptiste d?Ha?ti in Quartier Morin (HCBH, n = 191) from 9 September 2013 to 7 February 2014. At HCBH, study subjects also included minors (1?17.9 years of age, n = 28). Intake of dairy, other animal-sourced foods, peanut products and maize was assessed using a dietary recall survey. Aflatoxin exposure was assessed by measurement of urinary Aflatoxin M1 using high pressure liquid chromatography.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/AFM1_Survey_and_HPLC_data-2012-2013_RECALIBRATED.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "Cross-sectional Survey of Urinary Aflatoxins and Diet Recall in Haiti",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Haiti_Urine_Biomarker_and_Diet_Survey_Key.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/SOPs_and_dietary_survey.pdf"
-            ]
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Haiti",
+            "title": "Cross-sectional Survey of Urinary Aflatoxins and Diet Recall in Haiti"
         },
         {
+            "USAIDInitiative": "Feed the Future",
+            "USAIDawardNumber": "AID-OAA-A-13-00047",
+            "USAIDsubmittingOrganization": "Centre de coop?ration internationale en recherche agronomique pour le d?veloppement (CIRAD)",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9682,24 +9685,7 @@
                 "fn": "Anna Brenes",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-09-13",
             "description": "Polymorphism of SNP Markers (single nucleotide polymorphisms) was assessed on 24 parental lines of the ISRA sorghum breeding program .  About 1300 SNP have been used in this survey.",
-            "title": "SNP Polymorphism Survey of the Parental Lines of ISRA Sorghum Breeding Program as Part of the Feed the Future",
-            "keyword": [
-                "Sorghum",
-                "SNP markers",
-                "Polymorphism",
-                "breeding"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "b6c11260-bd00-44aa-aeca-af0fd3ac8283",
-            "programCode": [
-                "184:029"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
                     "description": "Polymorphism of SNP Markers (single nucleotide polymorphisms) was assessed on 24 parental lines of the ISRA sorghum breeding program .  About 1300 SNP have been used in this survey.",
@@ -9709,12 +9695,26 @@
                     "title": "SNP Polymorphism Survey of the Parental Lines of ISRA Sorghum Breeding Program as Part of the Feed the Future"
                 }
             ],
+            "identifier": "b6c11260-bd00-44aa-aeca-af0fd3ac8283",
+            "keyword": [
+                "Sorghum",
+                "SNP markers",
+                "Polymorphism",
+                "breeding"
+            ],
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "AID-OAA-A-13-00047",
-            "USAIDsubmittingOrganization": "Centre de coop?ration internationale en recherche agronomique pour le d?veloppement (CIRAD)",
-            "USAIDInitiative": "Feed the Future"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-09-13",
+            "programCode": [
+                "184:029"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "SNP Polymorphism Survey of the Parental Lines of ISRA Sorghum Breeding Program as Part of the Feed the Future"
         },
         {
             "accessLevel": "public",
@@ -9725,9 +9725,19 @@
                 "fn": "Jessica Klein",
                 "hasEmail": "mailto:foreignassistanceweb@state.gov"
             },
-            "modified": "2014-10-09",
             "description": "ForeignAssistance.gov provides a view of U.S. Government foreign assistance funds across agencies and enables users to explore, analyze, and review aid investments in a standard and easy-to-understand format.",
-            "title": "ForeignAssistance.gov",
+            "distribution": [
+                {
+                    "accessURL": "http://beta.foreignassistance.gov/developers",
+                    "describedBy": "http://beta.foreignassistance.gov/assets/data-dictionary.xlsx",
+                    "description": "ForeignAssistance.gov provides a view of U.S. Government foreign assistance funds across agencies and enables users to explore, analyze, and review aid investments in a standard and easy-to-understand format.",
+                    "downloadURL": "http://beta.foreignassistance.gov/assets/Agency/U.S.%20Agency%20for%20International%20Development.csv",
+                    "format": "CSV",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ForeignAssistance.gov"
+                }
+            ],
+            "identifier": "4c1a03a6-ae64-4749-8a81-6267afbb7bc3",
             "keyword": [
                 "fad",
                 "foreign assistance",
@@ -9735,10 +9745,12 @@
                 "research",
                 "aid"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "4c1a03a6-ae64-4749-8a81-6267afbb7bc3",
+            "landingPage": "http://foreignassistance.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2014-10-09",
             "programCode": [
                 "184:001",
                 "184:002",
@@ -9772,33 +9784,19 @@
                 "184:030",
                 "184:031",
                 "184:032",
-                "184:033",
-                "184:034",
-                "184:035",
-                "184:036",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "http://foreignassistance.gov",
-            "distribution": [
-                {
-                    "description": "ForeignAssistance.gov provides a view of U.S. Government foreign assistance funds across agencies and enables users to explore, analyze, and review aid investments in a standard and easy-to-understand format.",
-                    "downloadURL": "http://beta.foreignassistance.gov/assets/Agency/U.S.%20Agency%20for%20International%20Development.csv",
-                    "format": "CSV",
-                    "mediaType": "application/vnd.ms-excel",
-                    "describedBy": "http://beta.foreignassistance.gov/assets/data-dictionary.xlsx",
-                    "title": "ForeignAssistance.gov",
-                    "accessURL": "http://beta.foreignassistance.gov/developers"
-                }
+                "184:033",
+                "184:034",
+                "184:035",
+                "184:036",
+                "184:037"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "name": "USAID"
+            },
+            "title": "ForeignAssistance.gov"
         },
         {
             "accessLevel": "restricted public",
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Preliminary access level determination.  Final access level under review.",
             "bureauCode": [
                 "184:15"
             ],
@@ -9806,17 +9804,18 @@
                 "fn": "Jason Wucinski",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "R/P1M",
             "description": "The MEASURE Evaluation Dataverse is a collection of innovative evaluation data sets assembled in order to increase the evidence-base on program impact and evaluate the strengths and weaknesses of recent evaluation methodological developments.  Some datasets are available without restriction while others may be made available by submitting a request through the public-facing web-site, http://arc.irss.unc.edu/dvn/dv/MEP3.  MEASURE Evaluation is the USAID Global Health Bureau's primary vehicle for supporting improvements in monitoring and evaluation in population, health and nutrition worldwide.",
-            "title": "Measure Evaluation Dataverse",
+            "identifier": "0768db12-fef1-4fbc-aece-160262ec1f0b",
             "keyword": [
                 "innovative evaluation data",
                 "health decision making"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0768db12-fef1-4fbc-aece-160262ec1f0b",
+            "landingPage": "http://arc.irss.unc.edu/dvn/dv/MEP3",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "R/P1M",
             "programCode": [
                 "184:037",
                 "184:011",
@@ -9826,12 +9825,15 @@
                 "184:017",
                 "184:019"
             ],
-            "landingPage": "http://arc.irss.unc.edu/dvn/dv/MEP3",
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "name": "USAID"
+            },
+            "rights": "Preliminary access level determination.  Final access level under review.",
+            "title": "Measure Evaluation Dataverse"
         },
         {
+            "USAIDawardNumber": "AID-OAA-I-10-00002",
+            "USAIDsubmittingOrganization": "Management Systems International",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9840,54 +9842,56 @@
                 "fn": "Kat Walsh",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-11-30",
+            "describedByType": "application/pdf",
             "description": "The raw data from the Measuring Impact of Stabilization Initiatives (MISTI) project is the largest and most comprehensive evaluations of stabilization interventions ever undertaken by USAID.  The MISTI dataset contains five semi-annual iterations or 'waves' of surveys conducted by Management Systems International (MSI) from September 2012 through November 2014 to assess the impact of USAID projects on stability and resilience at the district and village levels in Afghanistan.  The main objective of the stabilization projects covered by the surveys, including the Stability in Key Areas (SIKA) programs, the Community Cohesion Initiative (CCI), the Afghan Civilian Assistance Program II, and the Kandahar Food Zone (KFZ), was to promote good governance and stability by building connections between government leaders and local communities.  USAID's efforts in these projects included training local government officials on how to manage projects, producing manuals that informed the public on how to tap into government services, and providing support for small-scale public works projects.  MISTI data analysis included village demographic characteristics, violent incident counts, stabilization and the National Solidarity Programme (NSP) project activities.  Perception indicators from interviews of 190,264 people conducted in 5,093 villages across 130 districts and 23 provinces in Afghanistan, has already yielded important insights that will inform U.S. and Afghan Government policy and practice related to transition. You can find all the MISTI Impact Evaluation reports on USAID?s Development Experience Clearinghouse (DEC) by clicking on the references below.  And, you can find a more complete description of the project by looking at the Fact Sheet included in that same list of references. Please note, an issue arose with the SPSS version of the survey file that had been posted here previously.  That file is currently being reconstituted and will be restored an the near future.",
-            "title": "Measuring Impact of Stabilization Initiatives Survey Data (MISTI)",
-            "keyword": [
-                "Impact Evaluation",
-                "Survey",
-                "Stability Index",
-                "Stability",
-                "Afghanistan"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "programCode": [
-                "184:003"
-            ],
-            "identifier": "2cafcb62-00da-4f83-ac7b-471bccf8528f",
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MISTI_Survey_Codebook.pdf",
+                    "describedByType": "application/pdf",
                     "description": "This MISTI survey data file contains the combined response data from five semi-annual iterations or ?waves? of surveys conducted from September 2012 through November 2014 to determine whether USAID project activities caused changes in stability and resilience at the district and village levels.  At the start, MISTI compiled a baseline stabilization and impact evaluation and survey. For the five waves of surveys, each of which was conducted over several months, a total of 190,264 individual interviews were undertaken in 5,093 different villages across 130 districts of the 23 provinces where stabilization initiatives were being implemented or considered. These data were compiled into one file to facilitate easy access for international development practitioners, researchers and other interested parties in accordance with the USAID?s Open Data Policy. As part of this process, village names and locations have been replaced with unique village identifiers to ensure the safety of Afghan stakeholders. This preserves a researcher's ability to access granular data and see trends at the village-level, but prevents data consumers from attributing responses to a named Afghan village.  The datasets supplied here are in CSV format. These data were analyzed for the MISTI impact evaluation of USAID stabilization programming in Afghanistan, 2012-2014.  USAID/Afghanistan?s MISTI ranks as the largest and most comprehensive trends analysis and impact evaluation of stabilization interventions that the U.S. Government has ever undertaken. It is also the only one to date subjected to peer review; in addition, three peer review papers for publication in leading journals and a presentation for the 2015 annual conference of the American Evaluation Association are in preparation.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MISTI_Survey_Data.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Measuring Impact of Stabilization Initiatives Survey Data (MISTI), Survey-response data in csv format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MISTI_Survey_Codebook.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "Measuring Impact of Stabilization Initiatives Survey Data (MISTI), Survey-response data in csv format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MISTI_Village_Data_Codebook.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The MISTI village-level dataset (MISTI_Village_Data) is a supplement to the response-level dataset. Each row of this dataset contains data from one unique village surveyed by MISTI in Waves 1-5. The dataset is in wide format. Each variable is identified by a wave number and a proximity to the village.  Data include village demographic characteristics, violent incident counts, stabilization and NSP project activities, and perception indicators from individual survey interviews aggregated to the village mean.  These data were analyzed for the MISTI impact evaluation of USAID stabilization programming in Afghanistan, 2012-2014.  USAID/Afghanistan?s MISTI ranks as the largest and most comprehensive trends analysis and impact evaluation of stabilization interventions that the U.S. Government has ever undertaken. It is also the only one to date subjected to peer review; in addition, three peer review papers for publication in leading journals and a presentation for the 2015 annual conference of the American Evaluation Association are in preparation.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MISTI_Village_Data.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Measuring Impact of Stabilization Initiatives Survey Data (MISTI), Village-level data in csv format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MISTI_Village_Data_Codebook.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "Measuring Impact of Stabilization Initiatives Survey Data (MISTI), Village-level data in csv format"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MISTI_Survey_Codebook.pdf",
+                    "describedByType": "application/pdf",
                     "description": "This MISTI survey data file contains the combined response data from five semi-annual iterations or ?waves? of surveys conducted from September 2012 through November 2014 to determine whether USAID project activities caused changes in stability and resilience at the district and village levels.  At the start, MISTI compiled a baseline stabilization and impact evaluation and survey. For the five waves of surveys, each of which was conducted over several months, a total of 190,264 individual interviews were undertaken in 5,093 different villages across 130 districts of the 23 provinces where stabilization initiatives were being implemented or considered. These data were compiled into one file to facilitate easy access for international development practitioners, researchers and other interested parties in accordance with the USAID?s Open Data Policy. As part of this process, village names and locations have been replaced with unique village identifiers to ensure the safety of Afghan stakeholders. This preserves a researcher's ability to access granular data and see trends at the village-level, but prevents data consumers from attributing responses to a named Afghan village.  The datasets supplied here are in CSV format. These data were analyzed for the MISTI impact evaluation of USAID stabilization programming in Afghanistan, 2012-2014.  USAID/Afghanistan?s MISTI ranks as the largest and most comprehensive trends analysis and impact evaluation of stabilization interventions that the U.S. Government has ever undertaken. It is also the only one to date subjected to peer review; in addition, three peer review papers for publication in leading journals and a presentation for the 2015 annual conference of the American Evaluation Association are in preparation.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/MISTI_Survey_Data.sav",
                     "format": "SPSS",
                     "mediaType": "application/SPSS",
-                    "title": "Measuring Impact of Stabilization Initiatives Survey Data (MISTI), Survey-response data in SPSS format",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/MISTI_Survey_Codebook.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "Measuring Impact of Stabilization Initiatives Survey Data (MISTI), Survey-response data in SPSS format"
                 }
             ],
+            "identifier": "2cafcb62-00da-4f83-ac7b-471bccf8528f",
+            "keyword": [
+                "Impact Evaluation",
+                "Survey",
+                "Stability Index",
+                "Stability",
+                "Afghanistan"
+            ],
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-11-30",
+            "programCode": [
+                "184:003"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://pdf.usaid.gov/pdf_docs/pnaed047.pdf",
                 "http://pdf.usaid.gov/pdf_docs/pa00jgfg.pdf",
@@ -9897,14 +9901,11 @@
                 "http://pdf.usaid.gov/pdf_docs/pa00ks3x.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/MISTI%20Factsheet.docx"
             ],
-            "describedByType": "application/pdf",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "AID-OAA-I-10-00002",
-            "USAIDsubmittingOrganization": "Management Systems International"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Measuring Impact of Stabilization Initiatives Survey Data (MISTI)"
         },
         {
+            "USAIDawardNumber": "AID-OAA-P-13-00004",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -9913,98 +9914,97 @@
                 "fn": "Tom Zearley",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-04-11",
+            "describedByType": "application/pdf",
             "description": "In March 2016, USAID sponsored the U.S. Institute for Peace (USIP) and researchers from Princeton\udc92s Empirical Studies on Conflict project (ESOC) in their analysis of numerous studies, articles, and data sets on stabilization programming in Afghanistan.  USIP and ESOC subsequently synthesized and analyzed quantitative and qualitative data on stabilization projects, and it prepared a final summary report that analyzed the impact of stabilization programs in Afghanistan and other countries where USAID operates.   After finalization of this ESOC report in June 2017, the team also drafted a Special Report, Aid and Stabilization in Afghanistan: What Do the Data Say?, summarizing the main report\udc92s findings.  The summary of findings and the data reports are attached.  In the process of preparing the What Do the Data Say? report, the Princeton Team prepared the attached EXCEL data sets and Code Book supporting their analyses.",
-            "title": "U.S. Stabilization Efforts: What Do the Data Say?",
-            "keyword": [
-                "USIP",
-                "Afghanistan",
-                "stabilization",
-                "codebook"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "programCode": [
-                "184:003"
-            ],
-            "identifier": "4cb878b4-3c42-4eff-8d6b-c4767c39c3e7",
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
+                    "describedByType": "application/pdf",
                     "description": "Afghan Info was used to identify programmatic information on stabilization projects in Afghanistan between 2010-2015.  It has a number of known limitations articulated in the file entitled CodeBook_for_ESOC_Report_Data_Set.pdf",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Afghanistan_Information.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Programmatic Information on Stabilization Projects in Afghanistan Between 2010-2015",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "Programmatic Information on Stabilization Projects in Afghanistan Between 2010-2015"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
+                    "describedByType": "application/pdf",
                     "description": "The broad panel dataset consists of outcome measures such as popular support for the Afghan government, support from anti- government elements, community cohesion , health access and economic well- being of the Afghan people.",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Support_Disbursements.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Broad Panel Dataset with Relevant Outcome Measures",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "Broad Panel Dataset with Relevant Outcome Measures"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
+                    "describedByType": "application/pdf",
                     "description": "CERP funds have been used to implement projects in all 34 provinces with a significant portion of these funds used in the South and South West regional command areas. Projects included, but were not limited to, transportation, education, agriculture/irrigation, health care, water and sanitation, and economic, financial and management system improvements.  Most CERP projects were relatively low cost and limited in time-duration.",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Commanders_Response_Program.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Commanders Response Program Dataset",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "Commanders Response Program Dataset"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
+                    "describedByType": "application/pdf",
                     "description": "This file aggregates road construction at district level.  It contains the length of roads constructed in the district and their density, defined as total road length divided by the district area.",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Road_Lengths_and_Density.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Road Construction Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "Road Construction Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
+                    "describedByType": "application/pdf",
                     "description": "This file contains the population weighted Pashtun speaking percentage in a district.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Ethnicity.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Ethnicity Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "Ethnicity Data"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
+                    "describedByType": "application/pdf",
                     "description": "This file contains indices of stability by region based on the data from the Measuring Impact of Stabilization Initiatives Project (MISTI).  The key indices studied were government capacity, local governance, quality of life and community cohesion.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Stability_Indices.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Stability by Region",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "Stability by Region"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
+                    "describedByType": "application/pdf",
                     "description": "This file contans the specification of region command grouping of districts.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/Regional_Command.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
-                    "title": "Region Command Grouping of Districts",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/CodeBook_for_ESOC_Report_Data_Set.pdf",
-                    "describedByType": "application/pdf"
+                    "title": "Region Command Grouping of Districts"
                 }
             ],
-            "references": [
-                "https://www.usaid.gov/opengov/developer/datasets/Aid_and_Stabilization_in_Afghanistan--What_Do_the_Data_Say_Kapstein.pdf",
-                "https://www.usaid.gov/opengov/developer/datasets/Lessons_Learned_From_Stabilization_Initiatives_in_Afghanistan--A_Systematic_Review_of_Existing_Research.pdf"
+            "identifier": "4cb878b4-3c42-4eff-8d6b-c4767c39c3e7",
+            "keyword": [
+                "USIP",
+                "Afghanistan",
+                "stabilization",
+                "codebook"
             ],
-            "describedByType": "application/pdf",
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "AID-OAA-P-13-00004"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2017-04-11",
+            "programCode": [
+                "184:003"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "https://www.usaid.gov/opengov/developer/datasets/Aid_and_Stabilization_in_Afghanistan--What_Do_the_Data_Say_Kapstein.pdf",
+                "https://www.usaid.gov/opengov/developer/datasets/Lessons_Learned_From_Stabilization_Initiatives_in_Afghanistan--A_Systematic_Review_of_Existing_Research.pdf"
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "U.S. Stabilization Efforts: What Do the Data Say?"
         },
         {
             "accessLevel": "public",
@@ -10015,23 +10015,7 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-05-16",
             "description": "Microenterprise Results Reporting (MRR) is an annual report to the U.S. Congress providing funding and program data on USAID's microenterprise activities. The MRR online reporting system, which supports the annual report, tracks USAID's progress towards congressionally mandated funding targets and monitors the results of USAID assistance to the microenterprise sector.",
-            "title": "Microenterprise Results Reporting",
-            "keyword": [
-                "microenterprise",
-                "economic growth"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "aeb361ff-1f9e-4084-9533-87c325ca2826",
-            "programCode": [
-                "184:029",
-                "184:031"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "https://mrr.usaid.gov/",
             "distribution": [
                 {
                     "description": "Microenterprise Results Reporting (MRR) is an annual report to the U.S. Congress providing funding and program data on USAID's microenterprise activities. The MRR online reporting system, which supports the annual report, tracks USAID's progress towards congressionally mandated funding targets and monitors the results of USAID assistance to the microenterprise sector.",
@@ -10041,11 +10025,28 @@
                     "title": "Microenterprise Results Reporting"
                 }
             ],
+            "identifier": "aeb361ff-1f9e-4084-9533-87c325ca2826",
+            "keyword": [
+                "microenterprise",
+                "economic growth"
+            ],
+            "landingPage": "https://mrr.usaid.gov/",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2016-05-16",
+            "programCode": [
+                "184:029",
+                "184:031"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "title": "Microenterprise Results Reporting"
         },
         {
+            "USAIDawardNumber": "AID-OAA-F-13-00034",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -10054,36 +10055,35 @@
                 "fn": "Minhchau Dinh",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-10-01",
             "description": "mWater is a tool that can be used to upload and visualize geospatial data describing water and sanitation systems.  The user can create space to store data from a particular site and to enter data drawn from a survey administered at that site.  Mapping the data and updating the data is as easy as using a smartphone app.  The platform is free and there is no need to install any special software.",
-            "title": "mWater Open API",
-            "keyword": [
-                "water",
-                "sanitation",
-                "water quality"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "282b92d4-3ff4-44ca-b9f1-9cb61ed5cf92",
-            "programCode": [
-                "184:018"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
-                    "description": "For a desktop comupter, this link provides access to the tool that can be used to upload and visualize geospatial data describing water and sanitation systems. If using the smartphone app, the link http://app.mWater.co - smartphone provides access to the tool that can be used to upload and visualize geospatial data describing water and sanitation systems.",
                     "accessURL": "http://portal.mwater.co/#entities",
+                    "description": "For a desktop comupter, this link provides access to the tool that can be used to upload and visualize geospatial data describing water and sanitation systems. If using the smartphone app, the link http://app.mWater.co - smartphone provides access to the tool that can be used to upload and visualize geospatial data describing water and sanitation systems.",
                     "format": "API",
                     "title": "mWater Open API - desktop"
                 }
             ],
+            "identifier": "282b92d4-3ff4-44ca-b9f1-9cb61ed5cf92",
+            "keyword": [
+                "water",
+                "sanitation",
+                "water quality"
+            ],
             "landingPage": "https://www.usaid.gov/global-waters/march-2015/mobiles-for-monitoring",
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "AID-OAA-F-13-00034"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-10-01",
+            "programCode": [
+                "184:018"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "mWater Open API"
         },
         {
             "accessLevel": "public",
@@ -10094,9 +10094,8 @@
                 "fn": "Tim Essam",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-11-21",
             "description": "The Open Cities Project aims to catalyze the creation, management and use of open data to produce innovative solutions for urban planning and resilience challenges across South Asia. Open Cities dataset includes geocoded information about 100,000 buildings, 2256 educational and 350 health facilities within Kathmandu Valley.",
-            "title": "OpenCities Project",
+            "identifier": "5e11db6f-f193-4750-b5a3-ab0c29bd4e6c",
             "keyword": [
                 "geospatial",
                 "Nepal",
@@ -10105,71 +10104,75 @@
                 "community",
                 "openstreetmap"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "5e11db6f-f193-4750-b5a3-ab0c29bd4e6c",
+            "landingPage": "http://opencitiesproject.com",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-11-21",
             "programCode": [
                 "184:024",
                 "184:034"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://opencitiesproject.com",
             "spatial": "Nepal",
-            "language": [
-                "en-US"
-            ]
+            "title": "OpenCities Project"
         },
         {
+            "USAIDawardNumber": "SOL-114-13-000008",
+            "USAIDinitiative": "USAID Forward",
+            "USAIDsubmittingOrganization": "Mendez England & Associates",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
-            ],
-            "contactPoint": {
-                "fn": "Brandon Pustejovsky",
-                "hasEmail": "mailto:opendata@usaid.gov"
-            },
-            "modified": "2014-01-16",
-            "description": "During the course of an evaluation, the Evaluation Team conducted a mini-survey among the members of the 13 youth centers supported under a program to promote integration of diverse population groups into Georgian society.  The ANI program is implemented by a Georgian organization, the United Nations Association of Georgia (UNAG).  The survey is based on a random sample of 160 respondents selected proportional to their distribution among members based on their ethnicity and gender.",
-            "title": "Mini Survey Data for the Advancing National Integration in Georgia Activity Mid-term Performance Evaluation",
-            "keyword": [
-                "mid-term evaluation",
-                "integration",
-                "ethnic groups",
-                "Georgia"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "8c4821a1-f7ea-4412-b7b9-64d0d5847400",
-            "programCode": [
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            ],
+            "contactPoint": {
+                "fn": "Brandon Pustejovsky",
+                "hasEmail": "mailto:opendata@usaid.gov"
+            },
+            "description": "During the course of an evaluation, the Evaluation Team conducted a mini-survey among the members of the 13 youth centers supported under a program to promote integration of diverse population groups into Georgian society.  The ANI program is implemented by a Georgian organization, the United Nations Association of Georgia (UNAG).  The survey is based on a random sample of 160 respondents selected proportional to their distribution among members based on their ethnicity and gender.",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ani_codebook.xlsx",
+                    "describedByType": "application/vnd.ms-excel",
                     "description": "During the course of an evaluation, the Evaluation Team conducted a mini-survey among the members of the 13 youth centers supported under a program to promote integration of diverse population groups into Georgian society.  The ANI program is implemented by a Georgian organization, the United Nations Association of Georgia (UNAG).  The survey is based on a random sample of 160 respondents selected proportional to their distribution among members based on their ethnicity and gender.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ANI_Data_Final_with_ids.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/ani_codebook.xlsx",
-                    "describedByType": "application/vnd.ms-excel",
                     "title": "Mini Survey Data for the Advancing National Integration in Georgia Activity Mid-term Performance Evaluation"
                 }
             ],
-            "references": [
-                "http://pdf.usaid.gov/pdf_docs/pdacy246.pdf"
+            "identifier": "8c4821a1-f7ea-4412-b7b9-64d0d5847400",
+            "keyword": [
+                "mid-term evaluation",
+                "integration",
+                "ethnic groups",
+                "Georgia"
             ],
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "SOL-114-13-000008",
-            "USAIDsubmittingOrganization": "Mendez England & Associates",
-            "USAIDinitiative": "USAID Forward"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2014-01-16",
+            "programCode": [
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "references": [
+                "http://pdf.usaid.gov/pdf_docs/pdacy246.pdf"
+            ],
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Mini Survey Data for the Advancing National Integration in Georgia Activity Mid-term Performance Evaluation"
         },
         {
+            "USAIDawardNumber": "RAN-I-00-09-00019",
+            "USAIDsubmittingOrganization": "Social Impact",
+            "USAIDtaskOrder": "AID-668-TO-12-0007",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -10178,9 +10181,19 @@
                 "fn": "Chris Murphy",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-09-26",
             "description": "This data set is derived from a 2013 household baseline survey in the country's Greenbelt region as part of an impact evaluation of the Food, Agribusiness, and Rural Markets (FARM) Project,which is intended to improve agricultural sector productivity and marketing in the Greenbelt and to support increasing South Sudan's food supply to reach food self-sufficiency.",
-            "title": "Baseline Survey for an Impact Evaluation of the Greenbelt Transformation Initiative in South Sudan",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/sites/default/files/SouthSudanDataDictionary.json",
+                    "describedByType": "application/json",
+                    "description": "This data set is derived from a 2013 household baseline survey in the country's Greenbelt region as part of an impact evaluation of the Food, Agribusiness, and Rural Markets (FARM) Project,which is intended to improve agricultural sector productivity and marketing in the Greenbelt and to support increasing South Sudan's food supply to reach food self-sufficiency.",
+                    "downloadURL": "http://www.usaid.gov/sites/default/files/SouthSudanHouseholdData.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "Baseline Survey for an Impact Evaluation of the Greenbelt Transformation Initiative in South Sudan"
+                }
+            ],
+            "identifier": "968fb1a1-0f2b-4c00-a601-0bca5ef07a5f",
             "keyword": [
                 "South Sudan",
                 "agriculture",
@@ -10196,38 +10209,28 @@
                 "nutrition",
                 "hunger"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "968fb1a1-0f2b-4c00-a601-0bca5ef07a5f",
+            "landingPage": "https://www.usaid.gov/developer/SouthSudanBaseline",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-09-26",
             "programCode": [
                 "184:019",
                 "184:026",
                 "184:032"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "publisher": {
+                "name": "USAID"
+            },
             "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "https://www.usaid.gov/developer/SouthSudanBaseline",
             "spatial": "South Sudan",
-            "distribution": [
-                {
-                    "description": "This data set is derived from a 2013 household baseline survey in the country's Greenbelt region as part of an impact evaluation of the Food, Agribusiness, and Rural Markets (FARM) Project,which is intended to improve agricultural sector productivity and marketing in the Greenbelt and to support increasing South Sudan's food supply to reach food self-sufficiency.",
-                    "downloadURL": "http://www.usaid.gov/sites/default/files/SouthSudanHouseholdData.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "Baseline Survey for an Impact Evaluation of the Greenbelt Transformation Initiative in South Sudan",
-                    "describedBy": "http://www.usaid.gov/sites/default/files/SouthSudanDataDictionary.json",
-                    "describedByType": "application/json"
-                }
-            ],
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "RAN-I-00-09-00019",
-            "USAIDtaskOrder": "AID-668-TO-12-0007",
-            "USAIDsubmittingOrganization": "Social Impact"
+            "title": "Baseline Survey for an Impact Evaluation of the Greenbelt Transformation Initiative in South Sudan"
         },
         {
+            "USAIDawardNumber": "GPO-I-03-05-00032",
+            "USAIDsubmittingOrganization": "Partnership for Supply Chain Management",
+            "USAIDtaskOrder": "03",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -10236,49 +10239,48 @@
                 "fn": "Lindabeth Doby",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-08-24",
+            "describedByType": "application/vnd.oasis.opendocument.text",
+            "description": "This data set provides supply chain health commodity shipment and pricing data. Specifically, the data set identifies Antiretroviral (ARV) and HIV lab shipments to supported countries. In addition, the data set provides the commodity pricing and associated supply chain expenses necessary to move the commodities to countries for use.  The dataset has similar fields to the Global Fund's Price, Quality and Reporting (PQR) data.  PEPFAR and the Global Fund represent the two largest procurers of HIV health commodities.  This dataset, when analyzed in conjunction with the PQR data, provides a more complete picture of global spending on specific health commodities. The data are particularly valuable for understanding ranges and trends in pricing as well as volumes delivered by country.  The US Government believes this data will help stakeholders make better, data-driven decisions.  Care should be taken to consider contextual factors when using the database.  Conclusions related to costs associated with moving specific line items or products to specific countries and lead times by product/country will not be accurate.",
+            "distribution": [
+                {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/SCMS_Delivery_History_Dataset_Data_Dictionary_20150929.csv",
+                    "describedByType": "text/csv",
                     "description": "This data set provides supply chain health commodity shipment and pricing data. Specifically, the data set identifies Antiretroviral (ARV) and HIV lab shipments to supported countries. In addition, the data set provides the commodity pricing and associated supply chain expenses necessary to move the commodities to countries for use.  The dataset has similar fields to the Global Fund's Price, Quality and Reporting (PQR) data.  PEPFAR and the Global Fund represent the two largest procurers of HIV health commodities.  This dataset, when analyzed in conjunction with the PQR data, provides a more complete picture of global spending on specific health commodities. The data are particularly valuable for understanding ranges and trends in pricing as well as volumes delivered by country.  The US Government believes this data will help stakeholders make better, data-driven decisions.  Care should be taken to consider contextual factors when using the database.  Conclusions related to costs associated with moving specific line items or products to specific countries and lead times by product/country will not be accurate.",
-            "title": "Supply Chain Shipment Pricing Data",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/SCMS_Delivery_History_Dataset_20150929.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "Supply Chain Shipment Pricing Data"
+                }
+            ],
+            "identifier": "0162a542-4f2e-4fe2-ad5d-8f6ed2344056",
             "keyword": [
                 "PEPFAR",
                 "Supply Chain",
                 "antiretroviral drugs",
                 "ARV"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "0162a542-4f2e-4fe2-ad5d-8f6ed2344056",
-            "programCode": [
-                "184:011"
+            "landingPage": "http://www.pepfar.gov/",
+            "language": [
+                "en-US"
             ],
             "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "landingPage": "http://www.pepfar.gov/",
-            "distribution": [
-                {
-                    "description": "This data set provides supply chain health commodity shipment and pricing data. Specifically, the data set identifies Antiretroviral (ARV) and HIV lab shipments to supported countries. In addition, the data set provides the commodity pricing and associated supply chain expenses necessary to move the commodities to countries for use.  The dataset has similar fields to the Global Fund's Price, Quality and Reporting (PQR) data.  PEPFAR and the Global Fund represent the two largest procurers of HIV health commodities.  This dataset, when analyzed in conjunction with the PQR data, provides a more complete picture of global spending on specific health commodities. The data are particularly valuable for understanding ranges and trends in pricing as well as volumes delivered by country.  The US Government believes this data will help stakeholders make better, data-driven decisions.  Care should be taken to consider contextual factors when using the database.  Conclusions related to costs associated with moving specific line items or products to specific countries and lead times by product/country will not be accurate.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/SCMS_Delivery_History_Dataset_20150929.csv",
-                    "format": "CSV",
-                    "mediaType": "text/csv",
-                    "title": "Supply Chain Shipment Pricing Data",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/SCMS_Delivery_History_Dataset_Data_Dictionary_20150929.csv",
-                    "describedByType": "text/csv"
-                }
+            "modified": "2015-08-24",
+            "programCode": [
+                "184:011"
             ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/SCMS_Historical_Delivery_Dataset_Purpose_and_Data_Notes_20150930.odt",
                 "http://www.usaid.gov/opengov/developer/datasets/LPA_Approved_Press_Release_20150928.odt"
             ],
-            "describedByType": "application/vnd.oasis.opendocument.text",
-            "language": [
-                "en-US"
-            ],
-            "USAIDawardNumber": "GPO-I-03-05-00032",
-            "USAIDtaskOrder": "03",
-            "USAIDsubmittingOrganization": "Partnership for Supply Chain Management"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "Supply Chain Shipment Pricing Data"
         },
         {
+            "USAIDawardNumber": "AID-114-c-14-00007",
+            "USAIDsubmittingOrganization": "Deloitte Consulting LLP",
             "accessLevel": "public",
             "bureauCode": [
                 "184:15"
@@ -10287,55 +10289,34 @@
                 "fn": "Lela Kerashvili",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-03-31",
             "description": "The objective of survey was to collect statistical energy and water end-use data for commercial and industrial sectors. The survey identified volumes of energy and water consumed, sources of energy and water and specifications of the technologies used in energy and water consumption.  The results of the survey will be used for updating the data for Commercial and Industrial sectors in Market Allocation Model (MARKAL Georgia) and will contribute to better quality of model results as well as to a better understanding of the water consumption patterns and to design effective water related policies.",
-            "title": "Energy and Water Consumption End-Use Survey in Commercial and Industrial Sectors in Georgia",
-            "keyword": [
-                "Energy",
-                "Water",
-                "Consumption",
-                "Commercial",
-                "Industrial",
-                "Consumer",
-                "Georgia"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "6b78be5b-0ff1-443c-9d23-f5a5e605ffe0",
-            "programCode": [
-                "184:032"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "spatial": "Georgia",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Water_and_Energy_Survey-CODEBOOK-Agricultural_Commercial-Georgia.csv",
+                    "describedByType": "text/csv",
                     "description": "Survey of energy and water end-use to update the Markal Allocation Model (MARKAL Georgia), Agriculture Sector",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Water_and_Energy_Survey_Agricultural_Enterprises-Georgia.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Georgia Water and Energy Survey, Agriculture Sector",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Water_and_Energy_Survey-CODEBOOK-Agricultural_Commercial-Georgia.csv",
-                    "describedByType": "text/csv"
+                    "title": "Georgia Water and Energy Survey, Agriculture Sector"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Water_and_Energy_Survey-CODEBOOK-Agricultural_Commercial-Georgia.csv",
+                    "describedByType": "text/csv",
                     "description": "Survey of energy and water end-use to update the Markal Allocation Model (MARKAL Georgia), Commercial Sector",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Water_and_Energy_Survey_Commercial_Enterprises-Georgia.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Georgia Water and Energy Survey, Commercial Sector",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/Water_and_Energy_Survey-CODEBOOK-Agricultural_Commercial-Georgia.csv",
-                    "describedByType": "text/csv"
+                    "title": "Georgia Water and Energy Survey, Commercial Sector"
                 },
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/Water_and_Energy_Survey-CODEBOOK-Industrial-Georgia.csv",
+                    "describedByType": "text/csv",
                     "description": "Survey of energy and water end-use to update the Markal Allocation Model (MARKAL Georgia), Industrial Sector",
                     "downloadURL": "https://www.usaid.gov/opengov/developer/datasets/Water_and_Energy_Survey_Industrial_Enterprises-Georgia.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "Georgia Water and Energy Survey, Industrial Sector",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/Water_and_Energy_Survey-CODEBOOK-Industrial-Georgia.csv",
-                    "describedByType": "text/csv"
+                    "title": "Georgia Water and Energy Survey, Industrial Sector"
                 },
                 {
                     "description": "Survey of energy and water end-use to update the Markal Allocation Model (MARKAL Georgia), Industrial Sector-Exchange Rates",
@@ -10345,11 +10326,30 @@
                     "title": "Georgia Water and Energy Survey, Industrial Sector-Exchange Rates"
                 }
             ],
+            "identifier": "6b78be5b-0ff1-443c-9d23-f5a5e605ffe0",
+            "keyword": [
+                "Energy",
+                "Water",
+                "Consumption",
+                "Commercial",
+                "Industrial",
+                "Consumer",
+                "Georgia"
+            ],
             "language": [
                 "en-US"
             ],
-            "USAIDawardNumber": "AID-114-c-14-00007",
-            "USAIDsubmittingOrganization": "Deloitte Consulting LLP"
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2016-03-31",
+            "programCode": [
+                "184:032"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Georgia",
+            "title": "Energy and Water Consumption End-Use Survey in Commercial and Industrial Sectors in Georgia"
         },
         {
             "accessLevel": "public",
@@ -10360,26 +10360,7 @@
                 "fn": "Kathleen Wu",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2018-03-30",
             "description": "Since 2001, the U.S. Agency for International Development (USAID) has conducted an annual survey on behalf of the Office of the U.S. Trade Representative (USTR) to identify and quantify the U.S. Government's trade capacity building (TCB) activities in developing countries and transitional economies. This dataset contains the results of that survey for the period, including funding levels, for the period FY1999-FY2016.",
-            "title": "Trade Capacity Building Database Data Set",
-            "keyword": [
-                "trade",
-                "annual",
-                "survey",
-                "international aid"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "9ae76cfd-9fc2-4fe2-ad58-9b0ee2a218eb",
-            "programCode": [
-                "184:025",
-                "184:026",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "https://tcb.usaid.gov",
             "distribution": [
                 {
                     "description": "Since 2001, the U.S. Agency for International Development (USAID) has conducted an annual survey on behalf of the Office of the U.S. Trade Representative (USTR) to identify and quantify the U.S. Government's trade capacity building (TCB) activities in developing countries and transitional economies. This dataset contains the results of that survey for the period, including funding levels, for the period FY1999-FY2016.",
@@ -10396,13 +10377,32 @@
                     "title": "Trade Capacity Building Database Data Set -- EXCEL Format"
                 }
             ],
+            "identifier": "9ae76cfd-9fc2-4fe2-ad58-9b0ee2a218eb",
+            "keyword": [
+                "trade",
+                "annual",
+                "survey",
+                "international aid"
+            ],
+            "landingPage": "https://tcb.usaid.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2018-03-30",
+            "programCode": [
+                "184:025",
+                "184:026",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "https://tcb.usaid.gov/about-database.html",
                 "http://www.usaid.gov/opengov/developer/datasets/Trade_Capacity_Building_Database_FY1999-FY2016_Definitions.csv"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Trade Capacity Building Database Data Set"
         },
         {
             "accessLevel": "public",
@@ -10413,18 +10413,32 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2012-06-01",
+            "dataQuality": false,
+            "describedByType": "application/rtf",
             "description": "The USAID Activities dataset is a snapshot of activities supported by USAID including their geographical locations within countries at the time of the snapshot. The data were used to create the map.usaid.gov web site on the Where We Work page. The data were used to create a map for the USAID web site on the Where We Work page.  Only a subset of USAID?s field offices provided data and many provided data on only a part of their portfolios.  Efforts are underway to harmonize the way data are collected by USAID missions which, when completed, will facilitate the display of a comprehensive portfolio of USAID activities.  The geographic names and boundaries in this dataset may not reflect the views of the United States Government on the sovereignty over geographic features.",
-            "title": "USAID Activity Locations",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/WhereWeWork_Codebook.rtf",
+                    "describedByType": "application/rtf",
+                    "description": "For each activity identified by the USAID missions, information provided includes activity name, description, start and end date, funds obligated, implementing partner, geographical areas covered and others.",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/WhereWeWork.zip",
+                    "format": "zipped csv",
+                    "mediaType": "application/zip",
+                    "title": "USAID Activity Locations: Project Details and Geographical Locations"
+                }
+            ],
+            "identifier": "00840fa9-4289-4e9f-bbad-2bea668ab364",
             "keyword": [
                 "activity locations",
                 "map data",
                 "USAID activities"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "00840fa9-4289-4e9f-bbad-2bea668ab364",
+            "landingPage": "http://map.usaid.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2012-06-01",
             "programCode": [
                 "184:001",
                 "184:002",
@@ -10464,27 +10478,13 @@
                 "184:036",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "http://map.usaid.gov/",
-            "distribution": [
-                {
-                    "description": "For each activity identified by the USAID missions, information provided includes activity name, description, start and end date, funds obligated, implementing partner, geographical areas covered and others.",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/WhereWeWork.zip",
-                    "format": "zipped csv",
-                    "mediaType": "application/zip",
-                    "title": "USAID Activity Locations: Project Details and Geographical Locations",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/WhereWeWork_Codebook.rtf",
-                    "describedByType": "application/rtf"
-                }
-            ],
-            "dataQuality": false,
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/opengov/developer/datasets/WhereWeWork_ReadMe.rtf"
             ],
-            "describedByType": "application/rtf"
+            "title": "USAID Activity Locations"
         },
         {
             "accessLevel": "public",
@@ -10495,9 +10495,19 @@
                 "fn": "Jill Moss",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2015-02-03",
             "description": "The Anticorruption Projects Database (Database) includes information about USAID projects with anticorruption interventions implemented worldwide between 2007 and 2013. The Database includes about 300 long-term country projects and regional or short-term projects. Projects were identified and information collected by the six Implementing Partners (IP) of the ENGAGE Indefinite Quantity Contract.  Criteria for selecting projects included: distinctive project interventions targeted at reducing corruption or promoting government integrity, accountability and transparency that ultimately results in reducing opportunities to corruption.  Availability of sufficient information about the projects was another criterion for selecting them to the Database.  This included but was not limited to project description and results, implementation timeframe, project value, and implementer.  After reviewing approximately 2000 projects, more than 300 were identified for the Database.  (The codebook can be found at http://www.usaid.gov/opengov/developer/datasets/Codebook_for_the_Anticorruption_Database.rtf)",
-            "title": "USAID Anticorruption Projects Database",
+            "distribution": [
+                {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Codebook_for_the_Anticorruption_Database.rtf",
+                    "describedByType": "application/rtf",
+                    "description": "The Anticorruption Projects Database (Database) includes information about USAID projects with anticorruption interventions implemented worldwide between 2007 and 2013. The Database includes about 300 long-term country projects and regional or short-term projects. Projects were identified and information collected by the six Implementing Partners (IP) of the ENGAGE Indefinite Quantity Contract.  Criteria for selecting projects included: distinctive project interventions targeted at reducing corruption or promoting government integrity, accountability and transparency that ultimately results in reducing opportunities to corruption.  Availability of sufficient information about the projects was another criterion for selecting them to the Database.  This included but was not limited to project description and results, implementation timeframe, project value, and implementer.  After reviewing approximately 2000 projects, more than 300 were identified for the Database.  (The codebook can be found at http://www.usaid.gov/opengov/developer/datasets/Codebook_for_the_Anticorruption_Database.rtf)",
+                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ACDatabase_2014-9-29.csv",
+                    "format": "csv",
+                    "mediaType": "text/csv",
+                    "title": "USAID Anticorruption Projects Database"
+                }
+            ],
+            "identifier": "b2cd92f6-e8bb-447b-9720-510222a80d0b",
             "keyword": [
                 "corruption",
                 "anticorruption",
@@ -10507,35 +10517,25 @@
                 "integrity",
                 "transparency"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "b2cd92f6-e8bb-447b-9720-510222a80d0b",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2015-02-03",
             "programCode": [
                 "184:007",
                 "184:008"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
-            "spatial": "Worldwide",
-            "distribution": [
-                {
-                    "description": "The Anticorruption Projects Database (Database) includes information about USAID projects with anticorruption interventions implemented worldwide between 2007 and 2013. The Database includes about 300 long-term country projects and regional or short-term projects. Projects were identified and information collected by the six Implementing Partners (IP) of the ENGAGE Indefinite Quantity Contract.  Criteria for selecting projects included: distinctive project interventions targeted at reducing corruption or promoting government integrity, accountability and transparency that ultimately results in reducing opportunities to corruption.  Availability of sufficient information about the projects was another criterion for selecting them to the Database.  This included but was not limited to project description and results, implementation timeframe, project value, and implementer.  After reviewing approximately 2000 projects, more than 300 were identified for the Database.  (The codebook can be found at http://www.usaid.gov/opengov/developer/datasets/Codebook_for_the_Anticorruption_Database.rtf)",
-                    "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ACDatabase_2014-9-29.csv",
-                    "format": "csv",
-                    "mediaType": "text/csv",
-                    "title": "USAID Anticorruption Projects Database",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/Codebook_for_the_Anticorruption_Database.rtf",
-                    "describedByType": "application/rtf"
-                }
-            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://www.usaid.gov/sites/default/files/documents/1866/AnalysisUSAIDAnticorruptionProgrammingWorldwideFinalReport2007-2013.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/Practitioner's_Guide_for_Anticorruption_Programming_2015.pdf"
             ],
-            "language": [
-                "en-US"
-            ]
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "spatial": "Worldwide",
+            "title": "USAID Anticorruption Projects Database"
         },
         {
             "accessLevel": "public",
@@ -10546,23 +10546,7 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2016-08-03",
             "description": "The USAID business forecast contains in-advance information about opportunities to partner with USAID. USAID regularly collaborates with host countries, beneficiaries, U.S. government agencies, international donors, and implementing partners to ensure that we effectively address development needs in the countries where we work",
-            "title": "USAID Business Forecast",
-            "keyword": [
-                "business forecast",
-                "Washington DC opportunities",
-                "Overseas Opportunities"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "c176d582-9805-44df-8113-148b74860b97",
-            "programCode": [
-                "184:000"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "https://www.usaid.gov/business-forecast",
             "distribution": [
                 {
                     "description": "Forecast of USAID Washington and Mission business opportunities",
@@ -10572,9 +10556,25 @@
                     "title": "USAID Washington and Mission Procurement Forecast Opportunities"
                 }
             ],
+            "identifier": "c176d582-9805-44df-8113-148b74860b97",
+            "keyword": [
+                "business forecast",
+                "Washington DC opportunities",
+                "Overseas Opportunities"
+            ],
+            "landingPage": "https://www.usaid.gov/business-forecast",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2016-08-03",
+            "programCode": [
+                "184:000"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "title": "USAID Business Forecast"
         },
         {
             "accessLevel": "public",
@@ -10585,59 +10585,59 @@
                 "fn": "Chris Murphy",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2013-06-30",
+            "describedByType": "application/pdf",
             "description": "The USAID construction assessment is a survey of the character, scope, value and management of construction activities supported by USAID during the period from June 1, 2011 to June 20, 2013.",
-            "title": "USAID Construction Assessment",
-            "keyword": [
-                "USAID",
-                "construction"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "6ee23912-b343-4ba6-bca7-77a310292f10",
-            "programCode": [
-                "184:028"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
-            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
             "distribution": [
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/awards_cleanedandlabeled_codebook.csv",
+                    "describedByType": "text/csv",
                     "description": "This dataset contains data on the primary awards identified in the survey of USAID construction carried out between June 1, 2011 to June 20 to learn aboutthe character, scope, value and management of USAID supported construction activities.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/awards_cleanedandlabeled.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "USAID Construction Assessment, Primary Awards",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/awards_cleanedandlabeled_codebook.csv",
-                    "describedByType": "text/csv"
+                    "title": "USAID Construction Assessment, Primary Awards"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/subawards_cleanedandlabeled_codebook.csv",
+                    "describedByType": "text/csv",
                     "description": "This dataset contains data on subwards identified in the survey of USAID construction carried out between June 1, 2011 to June 20 to learn about the character, scope, value and management of USAID supported construction activities.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/subawards_cleanedandlabeled.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "USAID Construction Assessment, Subawards",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/subawards_cleanedandlabeled_codebook.csv",
-                    "describedByType": "text/csv"
+                    "title": "USAID Construction Assessment, Subawards"
                 },
                 {
+                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/analysisdata_codebook.csv",
+                    "describedByType": "text/csv",
                     "description": "This dataset merges data from the primary and subawards datasets for analysis purposes for the survey of USAID construction carried out between June 1, 2011 to June 20 to learn about the character, scope, value and management of USAID supported construction activities.",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/analysisdata.csv",
                     "format": "csv",
                     "mediaType": "text/csv",
-                    "title": "USAID Construction Assessment, Analysis",
-                    "describedBy": "http://www.usaid.gov/opengov/developer/datasets/analysisdata_codebook.csv",
-                    "describedByType": "text/csv"
+                    "title": "USAID Construction Assessment, Analysis"
                 }
             ],
+            "identifier": "6ee23912-b343-4ba6-bca7-77a310292f10",
+            "keyword": [
+                "USAID",
+                "construction"
+            ],
             "language": [
                 "en-US"
             ],
+            "license": "http://www.usaid.gov/data/license-data-created-usaid-partners",
+            "modified": "2013-06-30",
+            "programCode": [
+                "184:028"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
             "references": [
                 "http://pdf.usaid.gov/pdf_docs/PBAAB700.pdf",
                 "http://www.usaid.gov/opengov/developer/datasets/USAID_Construction_Assessment_Questionnaire.pdf"
             ],
-            "describedByType": "application/pdf"
+            "rights": "Under the terms of an agreement with USAID, a partner owns data it collects.  Under the authority of the license that partners grant to USAID, USAID posts the data with a CC-BY license providing attribution to the partner.",
+            "title": "USAID Construction Assessment"
         },
         {
             "accessLevel": "public",
@@ -10648,18 +10648,28 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2014-10-09",
             "description": "Displays obligations and disbursements by operating unit (OU) and sector, beginning with Fiscal Years 2009. The data was pulled from USAID's financial accounting system of record, Phoenix.",
-            "title": "USAID Dollars Obligated and Dollars Spent",
+            "distribution": [
+                {
+                    "description": "Displays obligations and disbursements by operating unit (OU) and sector, beginning with Fiscal Years 2009. The data was pulled from USAID's financial accounting system of record, Phoenix.",
+                    "downloadURL": "http://www.foreignassistance.gov/web/dataview.aspx",
+                    "format": "zipped excel",
+                    "mediaType": "application/zip",
+                    "title": "USAID Dollars Obligated and Dollars Spent"
+                }
+            ],
+            "identifier": "d91c8da4-e06f-48a9-b12a-f9beb685281c",
             "keyword": [
                 "financial",
                 "obligations",
                 "disbursements"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "d91c8da4-e06f-48a9-b12a-f9beb685281c",
+            "landingPage": "http://foreignassistance.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2014-10-09",
             "programCode": [
                 "184:001",
                 "184:002",
@@ -10699,20 +10709,10 @@
                 "184:036",
                 "184:037"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "landingPage": "http://foreignassistance.gov",
-            "distribution": [
-                {
-                    "description": "Displays obligations and disbursements by operating unit (OU) and sector, beginning with Fiscal Years 2009. The data was pulled from USAID's financial accounting system of record, Phoenix.",
-                    "downloadURL": "http://www.foreignassistance.gov/web/dataview.aspx",
-                    "format": "zipped excel",
-                    "mediaType": "application/zip",
+            "publisher": {
+                "name": "USAID"
+            },
             "title": "USAID Dollars Obligated and Dollars Spent"
-                }
-            ],
-            "language": [
-                "en-US"
-            ]
         },
         {
             "accessLevel": "public",
@@ -10723,36 +10723,36 @@
                 "fn": "Thomas Mon",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-12-21",
             "description": "The Environmental Compliance Database is a record of environmental compliance submissions with their outcomes.  Documents in the database can be found by visiting the landing page http://gemini.info.usaid.gov/egat/envcomp/.  The entire dataset can be downloaded here. ",
-            "title": "The USAID Environmental Compliance Database",
-            "keyword": [
-                "environment",
-                "compliance"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "bb23de34-fc2b-4be9-a40d-a0f56450ac06",
-            "programCode": [
-                "184:032"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
             "distribution": [
                 {
+                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/ECD_Developer_and_Database_Guide_v2-B.docx",
+                    "describedByType": "application/msword",
                     "description": "This dataset is the complete Environmental Compliance database .",
                     "downloadURL": "http://www.usaid.gov/opengov/developer/datasets/ecd.xml",
                     "format": "XML",
                     "mediaType": "application/xml",
-                    "title": "The complete USAID Environmental Compliance Database",
-                    "describedBy": "https://www.usaid.gov/opengov/developer/datasets/ECD_Developer_and_Database_Guide_v2-B.docx",
-                    "describedByType": "application/msword"
+                    "title": "The complete USAID Environmental Compliance Database"
                 }
             ],
+            "identifier": "bb23de34-fc2b-4be9-a40d-a0f56450ac06",
+            "keyword": [
+                "environment",
+                "compliance"
+            ],
             "landingPage": "http://gemini.info.usaid.gov/egat/envcomp/",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2017-12-21",
+            "programCode": [
+                "184:032"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "title": "The USAID Environmental Compliance Database"
         },
         {
             "accessLevel": "public",
@@ -10763,38 +10763,7 @@
                 "fn": "Brandon Pustejovsky",
                 "hasEmail": "mailto:opendata@usaid.gov"
             },
-            "modified": "2017-10-01",
             "description": "The USAID Forward reform initiative ran from 2010-2016.  USAID Forward improved the way that the Agency delivers foreign assistance by embracing new partnerships, investing in the catalytic role of innovation, and demanding a renewed focus on results.  In 2017, the Agency determined that the work advanced under USAID Forward had largely been institutionalized.  On this site, you will find the FY 2012-2016 data related to USAID Forward's three main areas of focus: 1) Deliver results on a meaningful scale through a strengthened USAID, 2) Promote sustainable development through high-impact partnerships and local solutions, and 3) Identify and scale up innovative, breakthrough solutions to intractable development challenges.  As of October 2017, we are no longer updating information, including collecting indicators, on this legacy effort.",
-            "title": "USAID Forward",
-            "keyword": [
-                "usaid forward",
-                "open data",
-                "transparency",
-                "strategy",
-                "capacity",
-                "private sector development",
-                "mobile money",
-                "public-private partnerships",
-                "evaluation",
-                "leverage commercial private capital",
-                "DCA",
-                "mentoring",
-                "local solutions",
-                "procurement reform",
-                "engagement"
-            ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "d45f05be-50de-4840-83a1-8ebb8e93f25f",
-            "programCode": [
-                "184:036",
-                "184:037"
-            ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
-            "language": [
-                "en-US"
-            ],
             "distribution": [
                 {
                     "description": "USAID Forward: Number of USAID missions supporting mobile money initiatives_2010-2016",
@@ -10908,45 +10877,49 @@
                     "mediaType": "application/vnd.ms-excel",
                     "title": "USAID Forward, Strengthen staff capacity_2010-2016_EXCEL"
                 }
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "184:15"
             ],
-            "contactPoint": {
-                "fn": "Winnette Richards",
-                "hasEmail": "mailto:opendata@usaid.gov"
-            },
-            "modified": "2016-08-05",
-            "description": "This dataset brings together information collected since 2001 on PPPs that have been supported by USAID. For the purposes of this dataset a Public-Private Partnership is defined as a USAID-supported development project or initiative which engages the private sector (including corporations, foundations, and other non-governmental actors) as a core resource partner. Due to changes in Agency data collection systems, standards, and internal organization, the data has been collected according to different mechanisms, definitions, and timeframes from 2001-2015, and therefore cannot be considered to be comprehensive of all PPPs during this period.",
-            "title": "USAID Public-Private Partnerships Database",
+            "identifier": "d45f05be-50de-4840-83a1-8ebb8e93f25f",
             "keyword": [
-                "PPP",
-                "GDA",
-                "Public-Private Partnerships",
-                "Global Development Alliance"
+                "usaid forward",
+                "open data",
+                "transparency",
+                "strategy",
+                "capacity",
+                "private sector development",
+                "mobile money",
+                "public-private partnerships",
+                "evaluation",
+                "leverage commercial private capital",
+                "DCA",
+                "mentoring",
+                "local solutions",
+                "procurement reform",
+                "engagement"
             ],
-            "publisher": {
-                "name": "USAID"
-            },
-            "identifier": "83ace88b-c6a3-4520-990f-439ffc74e08f",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "modified": "2017-10-01",
             "programCode": [
-                "184:008",
-                "184:011",
-                "184:012",
-                "184:013",
-                "184:016",
-                "184:017",
-                "184:018",
-                "184:019",
-                "184:020",
-                "184:029",
-                "184:031",
-                "184:032"
+                "184:036",
+                "184:037"
+            ],
+            "publisher": {
+                "name": "USAID"
+            },
+            "title": "USAID Forward"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "184:15"
             ],
-            "license": "http://www.usaid.gov/data/license-data-created-agency",
+            "contactPoint": {
+                "fn": "Winnette Richards",
+                "hasEmail": "mailto:opendata@usaid.gov"
+            },
+            "description": "This dataset brings together information collected since 2001 on PPPs that have been supported by USAID. For the purposes of this dataset a Public-Private Partnership is defined as a USAID-supported development project or initiative which engages the private sector (including corporations, foundations, and other non-governmental actors) as a core resource partner. Due to changes in Agency data collection systems, standards, and internal organization, the data has been collected according to different mechanisms, definitions, and timeframes from 2001-2015, and therefore cannot be considered to be comprehensive of all PPPs during this period.",
             "distribution": [
                 {
```

