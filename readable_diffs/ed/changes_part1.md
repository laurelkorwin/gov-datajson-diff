# Change History for ed.json

### Changes from 31606f9 to dd2190f (Part 1/13)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/ed.json b/ed.json
index d4ef0ab..1454f0f 100644
--- a/ed.json
+++ b/ed.json
@@ -1,75 +1,65 @@
 {
-    "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "@context": "https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld",
-    "@type": "dcat:Catalog",
     "@id": "https://data.ed.gov/data.json",
+    "@type": "dcat:Catalog",
+    "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
     "dataset": [
         {
             "@type": "dcat:Dataset",
-            "title": "Common Core of Data (CCD) - School Nonfiscal Data Files and Documentation, 2018-19",
-            "description": "The primary purpose of the CCD is to provide basic information on public elementary and secondary schools, local education agencies (LEAs), and state education agencies (SEAs) for each state, the District of Columbia, and the outlying territories with a U.S. relationship.",
-            "modified": "2024-10-30T21:11:16.697377",
             "accessLevel": "public",
-            "identifier": "9b2910b7-5dbd-4b89-89d8-a4755d9eed3f",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
-            "temporal": "2018-10-01/2019-06-30",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "U.S. Government"
-                }
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chen-Su Chen",
                 "hasEmail": "mailto:chen-su.chen@ed.gov"
             },
+            "description": "The primary purpose of the CCD is to provide basic information on public elementary and secondary schools, local education agencies (LEAs), and state education agencies (SEAs) for each state, the District of Columbia, and the outlying territories with a U.S. relationship.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD School Directory",
                     "description": "Names, addresses and status variables for public K-12 schools",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sch_029_1819_w_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sch_029_1819_w_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD School Directory"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD School Membership File",
                     "description": "Student counts and demographic information at the school level",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sch_052_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sch_052_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD School Membership File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD School Staff File",
                     "description": "Teacher and staff counts at the school level",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sch_059_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sch_059_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD School Staff File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD School Characteristics File",
                     "description": "Program participation and other characteristics of k-12 public schools",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sch_129_1819_w_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sch_129_1819_w_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD School Characteristics File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD School Lunch Program File",
                     "description": "Counts of students at the school level eligible for free or reduced price lunch within USDA's National School Lunch Program",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sch_033_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sch_033_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD School Lunch Program File"
                 }
             ],
+            "identifier": "9b2910b7-5dbd-4b89-89d8-a4755d9eed3f",
             "keyword": [
                 "2018-19",
                 "72752616-32cd-4680-a309-499c7848841a",
@@ -80,125 +70,101 @@
                 "school",
                 "students"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-30T21:11:16.697377",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Approved Debt Relief by State",
-            "description": "Total Number of Borrowers with state-by-state borrower count, and disbursement amount (in millions)",
-            "modified": "2024-10-30T21:11:03.329910",
-            "accessLevel": "public",
-            "identifier": "bdcca3fd-4841-41df-8b0d-cbd455748a2d",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
-            "temporal": "2024-05-01/2024-05-31",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Communications and Outreach (OCO)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Secretary (OS)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "U.S. Department of Education",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "U.S. Government"
                 }
-                    }
-                }
             },
+            "temporal": "2018-10-01/2019-06-30",
+            "title": "Common Core of Data (CCD) - School Nonfiscal Data Files and Documentation, 2018-19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shahzeb Malik",
                 "hasEmail": "mailto:press@ed.gov"
             },
+            "description": "Total Number of Borrowers with state-by-state borrower count, and disbursement amount (in millions)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/4d42a56e-849b-4ea8-afaf-e26556544f16/download/1024pslf-discharges-and-approvals-pslf-tepslf-and-limited-waiver-by-location-data_pslf-only.csv",
                     "format": "CSV",
-                    "title": "1024PSLF Discharges and Approvals (PSLF, TEPSLF, and limited waiver) by Location Data_PSLF Only.csv",
-                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/4d42a56e-849b-4ea8-afaf-e26556544f16/download/1024pslf-discharges-and-approvals-pslf-tepslf-and-limited-waiver-by-location-data_pslf-only.csv"
+                    "mediaType": "text/csv",
+                    "title": "1024PSLF Discharges and Approvals (PSLF, TEPSLF, and limited waiver) by Location Data_PSLF Only.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/29bd5c49-8a25-4cf1-a3f9-d65abd4e5fa3/download/1024by-forgiveness-program_by-forgiveness-program.csv",
                     "format": "CSV",
-                    "title": "1024By Forgiveness program_By forgiveness program.csv",
-                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/29bd5c49-8a25-4cf1-a3f9-d65abd4e5fa3/download/1024by-forgiveness-program_by-forgiveness-program.csv"
+                    "mediaType": "text/csv",
+                    "title": "1024By Forgiveness program_By forgiveness program.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/667fc964-9dc6-4f71-8124-24926e18fc10/download/1024-total-number-of-borrowers-with-approved-debt-cancellation-by-state_total-approvals-by-state.csv",
                     "format": "CSV",
-                    "title": "1024 Total Number of Borrowers with Approved Debt Cancellation by State_Total Approvals by State.csv",
-                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/667fc964-9dc6-4f71-8124-24926e18fc10/download/1024-total-number-of-borrowers-with-approved-debt-cancellation-by-state_total-approvals-by-state.csv"
+                    "mediaType": "text/csv",
+                    "title": "1024 Total Number of Borrowers with Approved Debt Cancellation by State_Total Approvals by State.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/9a08be95-1fd5-4ba5-9454-6a3488b9aa73/download/pslf-discharges-and-approvals-pslf-tepslf-and-limited-waiver-by-location-data-as-of-early-octob.xlsx",
                     "format": "XLSX",
-                    "title": "1024PSLF Discharges and Approvals (PSLF, TEPSLF, and limited waiver) by Location Data.xlsx",
-                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/9a08be95-1fd5-4ba5-9454-6a3488b9aa73/download/pslf-discharges-and-approvals-pslf-tepslf-and-limited-waiver-by-location-data-as-of-early-octob.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "1024PSLF Discharges and Approvals (PSLF, TEPSLF, and limited waiver) by Location Data.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/a4d21727-d172-4364-9b71-d90ae9690015/download/by-forgiveness-program.xlsx",
                     "format": "XLSX",
-                    "title": "1024By Forgiveness program.xlsx",
-                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/a4d21727-d172-4364-9b71-d90ae9690015/download/by-forgiveness-program.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "1024By Forgiveness program.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/9abca06c-45a7-4249-9140-6959802d13ee/download/total-number-of-borrowers-with-approved-debt-cancellation-by-state.xlsx",
                     "format": "XLSX",
-                    "title": "1024 Total Number of Borrowers with Approved Debt Cancellation by State.xlsx",
-                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/9abca06c-45a7-4249-9140-6959802d13ee/download/total-number-of-borrowers-with-approved-debt-cancellation-by-state.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "1024 Total Number of Borrowers with Approved Debt Cancellation by State.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "BorrowerReliefApprovals0524",
                     "description": "Numbers of Borrowers with Approved Debt Cancellation by state for May 2024.",
-                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/d19424eb-a32e-4788-a9fb-2932bd48e956/download/bd-approvals-by-state-may2024-2-1.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/bdcca3fd-4841-41df-8b0d-cbd455748a2d/resource/d19424eb-a32e-4788-a9fb-2932bd48e956/download/bd-approvals-by-state-may2024-2-1.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "BorrowerReliefApprovals0524"
                 }
             ],
+            "identifier": "bdcca3fd-4841-41df-8b0d-cbd455748a2d",
             "keyword": [
                 "SDR",
                 "oco",
                 "student debt relief",
                 "student loans"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-30T21:11:03.329910",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Perkins Loan Cohort Default Rates",
-            "description": "The Federal Perkins Loan Cohort Default Rates is a data collection that is part of the Federal Perkins Loan program; the most recent Federal Perkins Loan Cohort Default Rates are available <https://ifap.ed.gov/ifap/byAwardYear.jsp?type=perkinscdrguide&display=single>. Historical program data is available electronically since 2006 at <https://ifap.ed.gov/ifap/byAwardYear.jsp?type=perkinscdrguide&set=archive&display=single>. The data collection is conducted using a web-based entry system wherein postsecondary institutions must submit information electronically if they participate in the Federal Perkins Loan program. Key statistics produced from this data collection are the Federal Perkins Loan cohort default rates (previously known as the Orange Book).",
-            "modified": "2024-10-30T21:10:48.928915",
-            "accessLevel": "public",
-            "identifier": "d884f887-33ca-4720-b06f-d2f0df4a8f50",
-            "dataQuality": true,
-            "issued": "2013-06-12",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/P1Y",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Federal Student Aid (FSA)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                "name": "Office of Communications and Outreach (OCO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -211,14 +177,26 @@
                         }
                     }
                 }
-                }
             },
+            "temporal": "2024-05-01/2024-05-31",
+            "title": "Approved Debt Relief by State"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Marini",
                 "hasEmail": "mailto:tara.marini@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Federal Perkins Loan Cohort Default Rates is a data collection that is part of the Federal Perkins Loan program; the most recent Federal Perkins Loan Cohort Default Rates are available <https://ifap.ed.gov/ifap/byAwardYear.jsp?type=perkinscdrguide&display=single>. Historical program data is available electronically since 2006 at <https://ifap.ed.gov/ifap/byAwardYear.jsp?type=perkinscdrguide&set=archive&display=single>. The data collection is conducted using a web-based entry system wherein postsecondary institutions must submit information electronically if they participate in the Federal Perkins Loan program. Key statistics produced from this data collection are the Federal Perkins Loan cohort default rates (previously known as the Orange Book).",
+            "identifier": "d884f887-33ca-4720-b06f-d2f0df4a8f50",
+            "issued": "2013-06-12",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "federal-perkins-cdr",
@@ -228,33 +206,20 @@
                 "orange-book",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-10-30T21:10:48.928915",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Data and Documentation - PSS 2017-18",
-            "description": "The Private School Universe Survey (PSS) is conducted by the National Center for Education Statistics (NCES) on behalf of the U.S. Department of Education in order to collect basic information on American private elementary and secondary schools. PSS grew out of a proposal in 1988 to develop a private school data collection that would improve on the sporadic collection of private school data dating back to 1890 and improve on commercially available private school sampling frames. PSS was first collected in the 1989\u201390 school year, with data collections every 2 years since.",
-            "modified": "2024-10-30T18:48:45.624738",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "d1cfb941-6390-4fe8-8ff9-56dbc9893988",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
-            "temporal": "2017-10-01/2018-06-15",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
+                "name": "Office of Federal Student Aid (FSA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -269,46 +234,58 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2012/P1Y",
+            "title": "Federal Perkins Loan Cohort Default Rates"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.Broughman@ed.gov"
             },
+            "description": "The Private School Universe Survey (PSS) is conducted by the National Center for Education Statistics (NCES) on behalf of the U.S. Department of Education in order to collect basic information on American private elementary and secondary schools. PSS grew out of a proposal in 1988 to develop a private school data collection that would improve on the sporadic collection of private school data dating back to 1890 and improve on commercially available private school sampling frames. PSS was first collected in the 1989\u201390 school year, with data collections every 2 years since.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "PSS 2017-18 SAS Data File",
                     "description": "Zip file archive containing the public use dataset for the 2017-18 Private School Universe Survey:  SAS format.",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1718_pu_sas7bdat.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1718_pu_sas7bdat.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "PSS 2017-18 SAS Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "PSS 2017-18 SPSS Data File",
                     "description": "Zip file archive containing the public use dataset for the 2017-18 Private School Universe Survey:  SPSS format",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1718_pu_sav.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1718_pu_sav.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "PSS 2017-18 SPSS Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "PSS 2017-18 Text Data File",
                     "description": "Zip file archive containing the public use dataset for the 2017-18 Private School Universe Survey:  Text format",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1718_pu_csv.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1718_pu_csv.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "PSS 2017-18 Text Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "PSS 2017-18 Restricted Use Data Files",
                     "description": "Research organizations can apply for access to more detailed restricted use files (available in SAS, SPSS and text format) through the IES Restricted Use Data License.   More information and the license application process can be found at https://nces.ed.gov/statprog/instruct.asp",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "PSS 2017-18 Restricted Use Data Files"
                 }
             ],
+            "identifier": "d1cfb941-6390-4fe8-8ff9-56dbc9893988",
             "keyword": [
                 "2017-18",
                 "72752616-32cd-4680-a309-499c7848841a",
@@ -316,22 +293,11 @@
                 "private-school",
                 "school"
             ],
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-30T18:48:45.624738",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data (CCD) - State Nonfiscal Data Files and Documentation, 2018-19",
-            "description": "The primary purpose of the CCD is to provide basic information on public elementary and secondary schools, local education agencies (LEAs), and state education agencies (SEAs) for each state, the District of Columbia, and the outlying territories with a U.S. relationship.",
-            "modified": "2024-10-30T18:47:31.764101",
-            "accessLevel": "public",
-            "identifier": "90525b1e-49d5-4ff8-8bb0-9c5734fc0238",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
-            "temporal": "2018-10-01/2019-06-30",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -352,38 +318,50 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "temporal": "2017-10-01/2018-06-15",
+            "title": "Data and Documentation - PSS 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chen-Su Chen",
                 "hasEmail": "mailto:chen-su.chen@ed.gov"
             },
+            "description": "The primary purpose of the CCD is to provide basic information on public elementary and secondary schools, local education agencies (LEAs), and state education agencies (SEAs) for each state, the District of Columbia, and the outlying territories with a U.S. relationship.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD State Directory",
                     "description": "Name and contact information at the state/SEA level",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_029_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_029_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD State Directory"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD State Membership File",
                     "description": "Student counts and demographic information at the state/SEA level",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_052_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_052_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD State Membership File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD State Staff File",
                     "description": "Teacher and staff counts at the state/SEA level",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_059_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_059_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD State Staff File"
                 }
             ],
+            "identifier": "90525b1e-49d5-4ff8-8bb0-9c5734fc0238",
             "keyword": [
                 "2018-19",
                 "72752616-32cd-4680-a309-499c7848841a",
@@ -394,22 +372,11 @@
                 "state",
                 "teachers"
             ],
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-30T18:47:31.764101",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "IPEDS Access Database 2018-19",
-            "description": "The Integrated Postsecondary Education Data System (IPEDS) is a system of interrelated surveys conducted annually by the U.S. Department of Education's National Center for Education Statistics (NCES). IPEDS annually gathers information from about 6,400 colleges, universities, and technical and vocational institutions that participate in the federal student aid programs.\r\n\r\nAccess Database: To eliminate the step of downloading IPEDS separately by survey component or select variables, IPEDS has made available the entire survey data for one collection year in the Microsoft Access format beginning with the 2004-05 IPEDS data collection year. Each database contains the relational data tables as well as the metadata tables that describe each data table, the variable titles, descriptions and variables types. Value codes and value labels are also available for all categorical variables. When downloading an IPEDS Access Database, the file is compressed using WinZip.",
-            "modified": "2024-10-30T18:46:11.507847",
-            "accessLevel": "public",
-            "identifier": "82e5b18d-d14e-47c4-be3d-03360fe3d82f",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
-            "temporal": "2018-08-01/2019-06-30",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -430,22 +397,33 @@
                     }
                 }
             },
+            "temporal": "2018-10-01/2019-06-30",
+            "title": "Common Core of Data (CCD) - State Nonfiscal Data Files and Documentation, 2018-19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Moussa Ezzeddine",
                 "hasEmail": "mailto:moussa.ezzeddine@ed.gov"
             },
+            "description": "The Integrated Postsecondary Education Data System (IPEDS) is a system of interrelated surveys conducted annually by the U.S. Department of Education's National Center for Education Statistics (NCES). IPEDS annually gathers information from about 6,400 colleges, universities, and technical and vocational institutions that participate in the federal student aid programs.\r\n\r\nAccess Database: To eliminate the step of downloading IPEDS separately by survey component or select variables, IPEDS has made available the entire survey data for one collection year in the Microsoft Access format beginning with the 2004-05 IPEDS data collection year. Each database contains the relational data tables as well as the metadata tables that describe each data table, the variable titles, descriptions and variables types. Value codes and value labels are also available for all categorical variables. When downloading an IPEDS Access Database, the file is compressed using WinZip.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "IPEDS 2018-19 Access Database",
                     "description": "Access databases for all years since 2004-05 and further information about IPEDS can be found at https://nces.ed.gov/ipeds/use-the-data/download-access-database",
-                    "downloadURL": "https://nces.ed.gov/ipeds/tablefiles/zipfiles/IPEDS_2018-19_Provisional.zip"
+                    "downloadURL": "https://nces.ed.gov/ipeds/tablefiles/zipfiles/IPEDS_2018-19_Provisional.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "IPEDS 2018-19 Access Database"
                 }
             ],
+            "identifier": "82e5b18d-d14e-47c4-be3d-03360fe3d82f",
             "keyword": [
                 "2018-19",
                 "72752616-32cd-4680-a309-499c7848841a",
@@ -456,22 +434,11 @@
                 "school",
                 "university"
             ],
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-30T18:46:11.507847",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "IPEDS Access Database 2017-18",
-            "description": "The Integrated Postsecondary Education Data System (IPEDS) is a system of interrelated surveys conducted annually by the U.S. Department of Education's National Center for Education Statistics (NCES). IPEDS annually gathers information from about 6,400 colleges, universities, and technical and vocational institutions that participate in the federal student aid programs.\r\n\r\nAccess Database: To eliminate the step of downloading IPEDS separately by survey component or select variables, IPEDS has made available the entire survey data for one collection year in the Microsoft Access format beginning with the 2004-05 IPEDS data collection year. Each database contains the relational data tables as well as the metadata tables that describe each data table, the variable titles, descriptions and variables types. Value codes and value labels are also available for all categorical variables. When downloading an IPEDS Access Database, the file is compressed using WinZip.",
-            "modified": "2024-10-30T18:45:21.448106",
-            "accessLevel": "public",
-            "identifier": "866e4ae6-2721-459b-b459-95346797e779",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
-            "temporal": "2017-08-01/2018-06-30",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -492,22 +459,33 @@
                     }
                 }
             },
+            "temporal": "2018-08-01/2019-06-30",
+            "title": "IPEDS Access Database 2018-19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Moussa Ezzeddine",
                 "hasEmail": "mailto:moussa.ezzeddine@ed.gov"
             },
+            "description": "The Integrated Postsecondary Education Data System (IPEDS) is a system of interrelated surveys conducted annually by the U.S. Department of Education's National Center for Education Statistics (NCES). IPEDS annually gathers information from about 6,400 colleges, universities, and technical and vocational institutions that participate in the federal student aid programs.\r\n\r\nAccess Database: To eliminate the step of downloading IPEDS separately by survey component or select variables, IPEDS has made available the entire survey data for one collection year in the Microsoft Access format beginning with the 2004-05 IPEDS data collection year. Each database contains the relational data tables as well as the metadata tables that describe each data table, the variable titles, descriptions and variables types. Value codes and value labels are also available for all categorical variables. When downloading an IPEDS Access Database, the file is compressed using WinZip.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "IPEDS 2017-18 Access Database",
                     "description": "Access databases for all years since 2004-05 and further information about IPEDS can be found at https://nces.ed.gov/ipeds/use-the-data/download-access-database",
-                    "downloadURL": "https://nces.ed.gov/ipeds/tablefiles/zipfiles/IPEDS_2017-18_Final.zip"
+                    "downloadURL": "https://nces.ed.gov/ipeds/tablefiles/zipfiles/IPEDS_2017-18_Final.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "IPEDS 2017-18 Access Database"
                 }
             ],
+            "identifier": "866e4ae6-2721-459b-b459-95346797e779",
             "keyword": [
                 "2017-18",
                 "72752616-32cd-4680-a309-499c7848841a",
@@ -518,22 +496,11 @@
                 "school",
                 "university"
             ],
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-30T18:45:21.448106",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data (CCD) - District Nonfiscal Data Files and Documentation, 2018-19",
-            "description": "The primary purpose of the CCD is to provide basic information on public elementary and secondary schools, local education agencies (LEAs), and state education agencies (SEAs) for each state, the District of Columbia, and the outlying territories with a U.S. relationship.",
-            "modified": "2024-10-30T18:43:12.873918",
-            "accessLevel": "public",
-            "identifier": "78b48c8b-120e-4172-85e6-359f377b4c6a",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
-            "temporal": "2018-10-01/2019-06-30",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -554,54 +521,65 @@
                     }
                 }
             },
+            "temporal": "2017-08-01/2018-06-30",
+            "title": "IPEDS Access Database 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chen-Su Chen",
                 "hasEmail": "mailto:chen-su.chen@ed.gov"
             },
+            "description": "The primary purpose of the CCD is to provide basic information on public elementary and secondary schools, local education agencies (LEAs), and state education agencies (SEAs) for each state, the District of Columbia, and the outlying territories with a U.S. relationship.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD District/LEA Directory",
                     "description": "File contains the names, location and status information for local education agencies.",
-                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/ccd_lea_029_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/ccd_lea_029_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD District/LEA Directory"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD District/LEA Membership File",
                     "description": "File contains student membership and demographic information at the district/LEA level.",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_lea_052_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_lea_052_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD District/LEA Membership File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD District/LEA Staff File",
                     "description": "File contains teacher and staff counts at the district/LEA level",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_lea_059_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_lea_059_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD District/LEA Staff File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD District/LEA Children with Disabilities File",
                     "description": "File contains counts of students with disabilities served under the Individuals with Disabilities Education Act (IDEA) Part B at the district/LEA level",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_lea_2_89_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_lea_2_89_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD District/LEA Children with Disabilities File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2018-19 CCD District/LEA English Learners File",
                     "description": "File contains counts of students identified as English learners at the district/LEA level",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_lea_141_1819_l_1a_091019.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_lea_141_1819_l_1a_091019.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2018-19 CCD District/LEA English Learners File"
                 }
             ],
+            "identifier": "78b48c8b-120e-4172-85e6-359f377b4c6a",
             "keyword": [
                 "2018-19",
                 "72752616-32cd-4680-a309-499c7848841a",
@@ -616,25 +594,17 @@
                 "students-with-disabilities",
                 "teachers"
             ],
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-30T18:43:12.873918",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2014 Awards: President's Education Awards Program",
-            "description": "This page details 2014 awards under the President's Education Awards Program.",
-            "modified": "2024-10-29T15:55:06.760024",
-            "accessLevel": "public",
-            "identifier": "d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
-            "temporal": "2014-01-01/2014-01-31",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Communications and Outreach (OCO)",
+                "name": "National Center for Education Statistics (NCES)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -647,479 +617,491 @@
                             }
                         }
                     }
+                }
+            },
+            "temporal": "2018-10-01/2019-06-30",
+            "title": "Common Core of Data (CCD) - District Nonfiscal Data Files and Documentation, 2018-19"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Frances Hopkins",
                 "hasEmail": "mailto:Frances.Hopkins@ed.gov"
             },
+            "description": "This page details 2014 awards under the President's Education Awards Program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "All Participating Schools (2014)",
                     "description": "All Participating Schools (2014) - All Participating Schools (2014)",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/9c8985a6-7e67-4129-a691-6b2f00bb17a5/download/all-states.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/9c8985a6-7e67-4129-a691-6b2f00bb17a5/download/all-states.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "All Participating Schools (2014)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AE/AP Schools",
                     "description": "AE/AP Schools - AE/AP Schools",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/8bac9806-0078-47bb-a1ac-a76df718d2e5/download/militarystate.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/8bac9806-0078-47bb-a1ac-a76df718d2e5/download/militarystate.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AE/AP Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "American Samoa",
                     "description": "American Samoa - American Samoa",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/c2e34fa3-20e5-4ef9-b350-9fa45a0a5668/download/as.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/c2e34fa3-20e5-4ef9-b350-9fa45a0a5668/download/as.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "American Samoa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Guam",
                     "description": "American Samoa - Guam",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/f122260e-655f-4962-9eef-d07e064bfbc1/download/gu.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/f122260e-655f-4962-9eef-d07e064bfbc1/download/gu.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Guam"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "American Samoa - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/aa254555-6ffd-458b-8d79-84191bd14cbd/download/pr.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/aa254555-6ffd-458b-8d79-84191bd14cbd/download/pr.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virgin Islands",
                     "description": "American Samoa - Virgin Islands",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/2be6c4b7-083f-4653-ad5b-6cef7dafdd16/download/vi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/2be6c4b7-083f-4653-ad5b-6cef7dafdd16/download/vi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virgin Islands"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/00a586aa-2558-4e46-8649-88dedf1dc70c/download/al.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/00a586aa-2558-4e46-8649-88dedf1dc70c/download/al.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alabama - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/bd8dad1e-82c8-4bdf-9c82-efc87ceb3d07/download/ak.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/bd8dad1e-82c8-4bdf-9c82-efc87ceb3d07/download/ak.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Alabama - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/10466df7-7434-46e2-a816-beab4e948374/download/az.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/10466df7-7434-46e2-a816-beab4e948374/download/az.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Alabama - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/38cc9764-c25a-4469-a8d6-6eb49f0dbb3a/download/ar.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/38cc9764-c25a-4469-a8d6-6eb49f0dbb3a/download/ar.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "Alabama - California",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/de536d64-69af-441a-bf9c-0d2a76ed8378/download/ca.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/de536d64-69af-441a-bf9c-0d2a76ed8378/download/ca.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Alabama - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/3d61b09f-6e87-40e8-8e6f-27f4d0af17fb/download/co.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/3d61b09f-6e87-40e8-8e6f-27f4d0af17fb/download/co.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Alabama - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/e5d529c5-2390-414b-b1b3-405c6077627a/download/ct.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/e5d529c5-2390-414b-b1b3-405c6077627a/download/ct.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Alabama - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/875e98e4-63b1-4737-9309-8a9a8e179f2c/download/de.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/875e98e4-63b1-4737-9309-8a9a8e179f2c/download/de.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "Alabama - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/f8295ba7-4347-4a84-8648-4b93bb663dae/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/f8295ba7-4347-4a84-8648-4b93bb663dae/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Alabama - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/75e39a63-e47b-4b9c-8702-3c92c23b53c9/download/fl.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/75e39a63-e47b-4b9c-8702-3c92c23b53c9/download/fl.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Alabama - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/ff15a178-b530-4fef-b164-81e622118091/download/ga.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/ff15a178-b530-4fef-b164-81e622118091/download/ga.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Alabama - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/ead7128b-b4a2-479c-88d6-80358b196134/download/hi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/ead7128b-b4a2-479c-88d6-80358b196134/download/hi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Alabama - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/7d073256-0ef8-4222-9f98-b1164c9bb409/download/id.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/7d073256-0ef8-4222-9f98-b1164c9bb409/download/id.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Alabama - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/e891d96e-748d-4559-8213-4af2bb331029/download/il.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/e891d96e-748d-4559-8213-4af2bb331029/download/il.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Alabama - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/3590b9f0-6bfc-4c9b-baf6-0060ad075fe7/download/in.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/3590b9f0-6bfc-4c9b-baf6-0060ad075fe7/download/in.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Alabama - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/7535bd49-f62a-498d-9e1f-4bb6c9064d84/download/ia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/7535bd49-f62a-498d-9e1f-4bb6c9064d84/download/ia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Alabama - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/3c56e88f-b384-4787-8a34-205a099faa88/download/ks.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/3c56e88f-b384-4787-8a34-205a099faa88/download/ks.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Alabama - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/8ca09e2f-9dae-4aca-82a8-61cd8d4d1544/download/ky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/8ca09e2f-9dae-4aca-82a8-61cd8d4d1544/download/ky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Alabama - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/2f5328c4-74f4-4c73-85ec-73d2785f66fe/download/la.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/2f5328c4-74f4-4c73-85ec-73d2785f66fe/download/la.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Alabama - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/84290191-a158-4127-8871-acef6db66b01/download/me.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/84290191-a158-4127-8871-acef6db66b01/download/me.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Alabama - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/96f05e66-27d3-4016-aec0-fada24523f57/download/md.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/96f05e66-27d3-4016-aec0-fada24523f57/download/md.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Alabama - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/5eac2639-ff1c-4b9c-b263-a4f618f51d62/download/ma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/5eac2639-ff1c-4b9c-b263-a4f618f51d62/download/ma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Alabama - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/1f4c9c89-46b8-4d59-99c5-78111705d2bf/download/mi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/1f4c9c89-46b8-4d59-99c5-78111705d2bf/download/mi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Alabama - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/2a698cab-3617-4401-bf4f-a75f0d4dd9e5/download/mn.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/2a698cab-3617-4401-bf4f-a75f0d4dd9e5/download/mn.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Alabama - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/f9b4c41e-c9f1-4ac9-8d7c-d5674fb9a80c/download/ms.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/f9b4c41e-c9f1-4ac9-8d7c-d5674fb9a80c/download/ms.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Alabama - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/e0522d53-a264-4e73-aefe-3dee087170f8/download/mo.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/e0522d53-a264-4e73-aefe-3dee087170f8/download/mo.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Alabama - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/553cb412-b43c-44fe-a0cb-d8c711eb4e71/download/mt.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/553cb412-b43c-44fe-a0cb-d8c711eb4e71/download/mt.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Alabama - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/935e2a6a-c0f6-4d8d-9509-59460cf54f9c/download/ne.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/935e2a6a-c0f6-4d8d-9509-59460cf54f9c/download/ne.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Alabama - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/e0631398-8a5b-4c20-8b09-b783a1dcb6e7/download/nv.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/e0631398-8a5b-4c20-8b09-b783a1dcb6e7/download/nv.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "Alabama - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/b4514807-3d1e-4bed-aac2-35eca7750f45/download/nh.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/b4514807-3d1e-4bed-aac2-35eca7750f45/download/nh.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "Alabama - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/76ea5290-45d0-4981-b96a-15e2aeba9e52/download/nj.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/76ea5290-45d0-4981-b96a-15e2aeba9e52/download/nj.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "Alabama - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/0f00567c-87f6-4459-9268-e6a6d6c59c6c/download/nm.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/0f00567c-87f6-4459-9268-e6a6d6c59c6c/download/nm.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "Alabama - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/daa3ed76-ce35-4e72-beaa-50840b2576b5/download/ny.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/daa3ed76-ce35-4e72-beaa-50840b2576b5/download/ny.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "Alabama - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/d0286d4f-6fe2-4d15-b64b-877bf00e9d12/download/nc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/d0286d4f-6fe2-4d15-b64b-877bf00e9d12/download/nc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "Alabama - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/82bc4928-2343-460c-a7e7-4fa748ef930c/download/nd.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/82bc4928-2343-460c-a7e7-4fa748ef930c/download/nd.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Alabama - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/7734b8ef-4a45-4ceb-bc57-9ec930865aa7/download/oh.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/7734b8ef-4a45-4ceb-bc57-9ec930865aa7/download/oh.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Alabama - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/8c0f5e14-ffa7-4656-9b25-84a324388f66/download/ok.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/8c0f5e14-ffa7-4656-9b25-84a324388f66/download/ok.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Alabama - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/bdd55e03-ccbd-40f5-9dc4-681e4f2f747d/download/or.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/bdd55e03-ccbd-40f5-9dc4-681e4f2f747d/download/or.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Alabama - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/024ae4d1-8e81-494c-9b33-57bde11e7e57/download/pa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/024ae4d1-8e81-494c-9b33-57bde11e7e57/download/pa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Alabama - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/e4d36f4f-1409-406d-8019-c52c1b99dd32/download/ri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/e4d36f4f-1409-406d-8019-c52c1b99dd32/download/ri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "Alabama - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/8d9557dd-ffac-49b2-a20b-b4f7a6bec4c8/download/sc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/8d9557dd-ffac-49b2-a20b-b4f7a6bec4c8/download/sc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "Alabama - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/2f5b2003-d777-4458-a46d-eb62ec0d66ed/download/sd.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/2f5b2003-d777-4458-a46d-eb62ec0d66ed/download/sd.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Alabama - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/0c527f4e-d1d5-4982-a747-28aeaba0a455/download/tn.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/0c527f4e-d1d5-4982-a747-28aeaba0a455/download/tn.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Alabama - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/5addea2d-5c11-4d8f-98d1-c66891de9d1f/download/tx.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/5addea2d-5c11-4d8f-98d1-c66891de9d1f/download/tx.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Alabama - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/9a24d677-8411-43af-a2c5-0ff3cf1c0bd4/download/ut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/9a24d677-8411-43af-a2c5-0ff3cf1c0bd4/download/ut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Alabama - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/4af57798-8d7a-46f1-81b1-d8f7c0a64324/download/vt.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/4af57798-8d7a-46f1-81b1-d8f7c0a64324/download/vt.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Alabama - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/0c5e5ca4-9fb5-4a53-bc42-c17cc99c6add/download/va.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/0c5e5ca4-9fb5-4a53-bc42-c17cc99c6add/download/va.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Alabama - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/03ac81f5-5d0d-4abe-abe5-511e24bfd369/download/wa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/03ac81f5-5d0d-4abe-abe5-511e24bfd369/download/wa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "Alabama - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/ac370e68-6863-441a-8c1e-ef6f5604a526/download/wv.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/ac370e68-6863-441a-8c1e-ef6f5604a526/download/wv.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Alabama - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/4962c682-0617-4f68-befa-34fafb6dde1d/download/wi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/4962c682-0617-4f68-befa-34fafb6dde1d/download/wi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Alabama - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/7abde9e0-c494-4fcb-8b23-da03752a3e06/download/wy.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/7abde9e0-c494-4fcb-8b23-da03752a3e06/download/wy.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "List of Participating Schools (2013)",
                     "description": "List of Participating Schools (2013) - List of Participating Schools (2013)",
-                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/2edf35cf-19ef-417a-a573-af473d0deee0/download/2013-participating-schools.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1/resource/2edf35cf-19ef-417a-a573-af473d0deee0/download/2013-participating-schools.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "List of Participating Schools (2013)"
                 }
             ],
+            "identifier": "d2d4b35c-fbf4-4014-85a0-39c4dda7f5c1",
             "keyword": [
                 "academic-achievement",
                 "academic-improvement",
@@ -1128,28 +1110,14 @@
                 "presidents-education-awards-program",
                 "recognition-achievement"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-29T15:55:06.760024",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "IDEA Section 618 LEA Part B Exiting",
-            "description": "#Part B Exiting\r\n##LEA\r\n\r\nPart B of _IDEA_ provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services. This file provides the count of children with disabilities exiting special education by exiting reason at the LEA level.",
-            "modified": "2024-10-25T15:39:21.917282",
-            "accessLevel": "public",
-            "identifier": "183e21a7-0a9b-43e5-bf22-1bb6f6e98db2",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Special Education Programs (OSEP)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                "name": "Office of Communications and Outreach (OCO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -1162,23 +1130,34 @@
                         }
                     }
                 }
-                }
             },
+            "spatial": "United States",
+            "temporal": "2014-01-01/2014-01-31",
+            "title": "2014 Awards: President's Education Awards Program"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Special Education Programs - Research to Practice Division",
                 "hasEmail": "mailto:OSEPideadata@ed.gov"
             },
+            "description": "#Part B Exiting\r\n##LEA\r\n\r\nPart B of _IDEA_ provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services. This file provides the count of children with disabilities exiting special education by exiting reason at the LEA level.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2022-23",
                     "description": "IDEA Part B Exiting LEA\r\n\r\n*[Data Notes](/dataset/e9ba7c29-453a-42a0-9c35-3b04b689f707/resource/6b4c1f6d-e14b-482d-8bbc-36ff394596a8/download/b-exitinglea-data-notes-2022-23.docx)*\r\n\r\n*[Documentation](/dataset/e9ba7c29-453a-42a0-9c35-3b04b689f707/resource/bf79c805-4913-4f92-a037-80eee4ed0b56/download/idea-partb-exitinglea-2022-23.xlsx)*",
-                    "downloadURL": "https://data.ed.gov/dataset/183e21a7-0a9b-43e5-bf22-1bb6f6e98db2/resource/1c1baac9-49b7-439a-a94d-eef523dabf5b/download/bexitinglea2022-23.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/183e21a7-0a9b-43e5-bf22-1bb6f6e98db2/resource/1c1baac9-49b7-439a-a94d-eef523dabf5b/download/bexitinglea2022-23.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2022-23"
                 }
             ],
+            "identifier": "183e21a7-0a9b-43e5-bf22-1bb6f6e98db2",
             "isPartOf": "be4d7917-53ad-423c-be7d-fd91184faeba",
             "keyword": [
                 "OSEP",
@@ -1187,26 +1166,11 @@
                 "osep",
                 "state"
             ],
-            "bureauCode": [
-                "018:20"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-25T15:39:21.917282",
             "programCode": [
                 "018:000"
             ],
-            "references": [
-                "https://data.ed.gov/dataset/e9ba7c29-453a-42a0-9c35-3b04b689f707/resource/bf79c805-4913-4f92-a037-80eee4ed0b56/download/idea-partb-exitinglea-2022-23.xlsx",
-                "https://data.ed.gov/dataset/e9ba7c29-453a-42a0-9c35-3b04b689f707/resource/6b4c1f6d-e14b-482d-8bbc-36ff394596a8/download/b-exitinglea-data-notes-2022-23.docx"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "IDEA Section 618 State Part C Exiting",
-            "description": "Part C of *IDEA* provides funds to states to assist them in developing and implementing statewide, comprehensive, coordinated, multidisciplinary interagency systems to make early intervention services available to all children from birth through age two with disabilities and their families.\r\n#Exiting\r\n\r\n[*Documentation*](/dataset/docs/idea-section-618-state-part-c-exiting)",
-            "modified": "2024-10-25T14:55:56.637994",
-            "accessLevel": "public",
-            "identifier": "628c4cca-7c49-4bd0-9066-9130ff3d960b",
-            "landingPage": "https://www2.ed.gov/programs/osepidea/618-data/state-level-data-files/index.html",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Special Education Programs (OSEP)",
@@ -1227,157 +1191,171 @@
                     }
                 }
             },
+            "references": [
+                "https://data.ed.gov/dataset/e9ba7c29-453a-42a0-9c35-3b04b689f707/resource/bf79c805-4913-4f92-a037-80eee4ed0b56/download/idea-partb-exitinglea-2022-23.xlsx",
+                "https://data.ed.gov/dataset/e9ba7c29-453a-42a0-9c35-3b04b689f707/resource/6b4c1f6d-e14b-482d-8bbc-36ff394596a8/download/b-exitinglea-data-notes-2022-23.docx"
+            ],
+            "title": "IDEA Section 618 LEA Part B Exiting"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Special Education Programs - Research to Practice Division",
                 "hasEmail": "mailto:OSEPideadata@ed.gov"
             },
+            "description": "Part C of *IDEA* provides funds to states to assist them in developing and implementing statewide, comprehensive, coordinated, multidisciplinary interagency systems to make early intervention services available to all children from birth through age two with disabilities and their families.\r\n#Exiting\r\n\r\n[*Documentation*](/dataset/docs/idea-section-618-state-part-c-exiting)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2022-2023",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2022-2023\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/deed738c-41df-4929-ac97-56681c7a08d6/download/c-exiting-datanotes-2022-23.docx)*\r\n\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/5f993a35-6211-4141-91c0-07c080dac5da/download/idea-partc-exiting-2022-23.docx)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/58d07bce-7d5a-4ed0-a426-90eb2ba6ecdf/download/cexiting2022-23.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/58d07bce-7d5a-4ed0-a426-90eb2ba6ecdf/download/cexiting2022-23.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2022-2023"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2021-2022",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2021-2022\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/6310d246-c085-4cc5-8eb0-30f4e8344bdc/download/c-exiting-datanotes-2021-22.docx)*\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/3088665d-8509-41a8-9fd0-946d8b8df138/download/idea-partc-exiting-2021-22.docx)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/aa8db60d-46c8-4596-92aa-cdedb187c266/download/cexiting2021-22.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/aa8db60d-46c8-4596-92aa-cdedb187c266/download/cexiting2021-22.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2021-2022"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2020-2021",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2020-2021\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/2202adb4-b347-44a9-b71e-3ad34a36b5c7/download/c-exiting-datanotes-2020-21-1.docx)*\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/5ba45152-8cc1-4e7b-9418-4bf4dbc6284a/download/idea-partc-exiting-2020-21-2.docx)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/36ad21f1-d235-4bf7-9bf6-265ec84e6a98/download/cexiting2020-21.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/36ad21f1-d235-4bf7-9bf6-265ec84e6a98/download/cexiting2020-21.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2020-2021"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2019-2020",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2019-2020\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/5585456e-5187-46a8-9a66-cb1400ad840f/download/c-exiting-datanotes-2019-20.docx)*\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/6fcf0138-2304-4b01-8f2a-8bf3dd4631aa/download/idea-partc-exiting-2019-20.docx)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/986979d5-d2c6-4e38-93e7-d1ca0c11aa3a/download/cexiting2019-20.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/986979d5-d2c6-4e38-93e7-d1ca0c11aa3a/download/cexiting2019-20.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2019-2020"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2018-2019",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2018-2019\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/13c43781-167e-4756-b6fa-a52e75c2e088/download/c-exiting-datanotes-2018-19.pdf)*\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/225d0990-4b1f-4ac4-9079-9d92db2b7ab5/download/idea-partc-exiting-2018-19.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/f948d73e-1cd5-46af-bd61-831705637e0e/download/cexiting2018-19.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/f948d73e-1cd5-46af-bd61-831705637e0e/download/cexiting2018-19.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2018-2019"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2017-2018",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2017-2018\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/62ef05b3-03d1-4792-8f42-9d99b63ffb4c/download/c-exiting-datanotes-2017-18.pdf)*\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/74891c2d-f30a-4ae1-bc6c-eb555d7ee4cb/download/idea-partc-exiting-2017-18.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/88bc3047-a642-4862-a32b-1f213ab66032/download/cexiting2017-18.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/88bc3047-a642-4862-a32b-1f213ab66032/download/cexiting2017-18.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2017-2018"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2016-2017",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2016-2017\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/cd24aeed-7d74-4731-8ea6-c9e47d071e68/download/c-exiting-datanotes-2016-17.pdf)*\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/60c8017e-8d07-4b4a-b6a7-ef1812e2804b/download/idea-partc-exiting-2016-17.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/78f220cb-e181-4469-af4c-d14cdf216823/download/cexiting2016-17.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/78f220cb-e181-4469-af4c-d14cdf216823/download/cexiting2016-17.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2016-2017"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2015-2016",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2015-2016\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/87e2b9ba-5e54-40e9-a0f1-87dc76214e56/download/c-exitingdatanotes-2015-16.pdf)*\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/28a1510c-d1d3-4ff9-ae16-78e133e1703b/download/idea-partc-exiting-2015-16.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/7bd8c43e-5367-43b4-871f-cad3dbfd7fe8/download/cexiting2015-16.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/7bd8c43e-5367-43b4-871f-cad3dbfd7fe8/download/cexiting2015-16.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2015-2016"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2014-2015",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2014-2015\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/f51c9467-e995-416b-ac52-37e41655c0af/download/c-exitingdatanotes-2014-15.pdf)*\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/9f077de9-107a-4bc9-8fc0-68c790fb53fa/download/idea-partc-exiting-2014.docx)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/2ef2f8d0-19e5-48f8-a86a-f6945471d1a9/download/cexiting2014-15.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/2ef2f8d0-19e5-48f8-a86a-f6945471d1a9/download/cexiting2014-15.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2014-2015"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2013-2014",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2013-2014\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/4fde7483-2879-416b-86a1-d413b3dee5ea/download/c-exitingdatanotes-2013-14.pdf)*\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/a5b6b3c6-f34c-44aa-9fec-c23fe45eb8aa/download/idea-partc-exiting-2013.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/c15a48f6-8488-43dc-be44-aa212e0c0df8/download/cexiting2013-14.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/c15a48f6-8488-43dc-be44-aa212e0c0df8/download/cexiting2013-14.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2013-2014"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2012-2013",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Exiting\r\n2012-2013\r\n\r\n*[Data Notes](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/d059eed8-225d-43a3-94e0-9812193bc320/download/c-exitingdatanotes-2012-13.pdf)*\r\n*[Data Documentation](/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/abae76c0-4200-401e-97ae-ad2432d47c04/download/idea-partc-exiting-2012.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/6d7b4795-ef61-4c58-bd15-0ef11728586a/download/cexiting2012-13.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/6d7b4795-ef61-4c58-bd15-0ef11728586a/download/cexiting2012-13.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2012-2013"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2011-2012",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Exiting\n2011-2012\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/9bac9f1f-9567-4e2b-b192-2beb641a9793/download/cexiting2011-12.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/9bac9f1f-9567-4e2b-b192-2beb641a9793/download/cexiting2011-12.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2011-2012"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2010-2011",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Exiting\n2010-2011\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/f6ff72cb-51b1-41f2-a992-a427b056856c/download/cexiting2010-11.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/f6ff72cb-51b1-41f2-a992-a427b056856c/download/cexiting2010-11.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2010-2011"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2009-2010",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Exiting\n2009-2010\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/aecde8bc-172d-4679-a564-03d840c55023/download/cexiting2009-10.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/aecde8bc-172d-4679-a564-03d840c55023/download/cexiting2009-10.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2009-2010"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2008-2009",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Exiting\n2008-2009\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/7d43583e-0bb4-42e9-a676-3ba00715ffcd/download/cexiting2008-09.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/7d43583e-0bb4-42e9-a676-3ba00715ffcd/download/cexiting2008-09.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2008-2009"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2007-2008",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Exiting\n2007-2008\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/b9f76c45-ecc3-4be5-9082-2dcbfba5abc2/download/cexiting2007-08.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/b9f76c45-ecc3-4be5-9082-2dcbfba5abc2/download/cexiting2007-08.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2007-2008"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2006-2007",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Exiting\n2006-2007\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/f824d80a-9f4c-444a-b88b-bcd11e9eaff5/download/cexiting2006-07.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/f824d80a-9f4c-444a-b88b-bcd11e9eaff5/download/cexiting2006-07.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2006-2007"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2005-2006",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Exiting\n2005-2006\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/3f3929c8-4cd8-4934-bf63-da66fdd56fb5/download/cexiting2005-06.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/628c4cca-7c49-4bd0-9066-9130ff3d960b/resource/3f3929c8-4cd8-4934-bf63-da66fdd56fb5/download/cexiting2005-06.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2005-2006"
                 }
             ],
+            "identifier": "628c4cca-7c49-4bd0-9066-9130ff3d960b",
             "isPartOf": "0a53acaf-5ec2-47ba-8867-a7de9d9c5e25",
             "keyword": [
                 "b155e7a9-48f7-4edd-863d-896d48d84367",
@@ -1389,13 +1367,32 @@
                 "special-education",
                 "state-level-data-files"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:20"
-            ],
+            "landingPage": "https://www2.ed.gov/programs/osepidea/618-data/state-level-data-files/index.html",
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-25T14:55:56.637994",
             "programCode": [
                 "018:000"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Special Education Programs (OSEP)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Secretary (OS)",
+                        "subOrganizationOf": {
+                            "@type": "org:Organization",
+                            "name": "U.S. Department of Education",
+                            "subOrganizationOf": {
+                                "@type": "org:Organization",
+                                "name": "U.S. Government"
+                            }
+                        }
+                    }
+                }
+            },
             "references": [
                 "https://data.ed.gov/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/deed738c-41df-4929-ac97-56681c7a08d6/download/c-exiting-datanotes-2022-23.docx",
                 "https://data.ed.gov/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/5f993a35-6211-4141-91c0-07c080dac5da/download/idea-partc-exiting-2022-23.docx",
@@ -1419,180 +1416,161 @@
                 "https://data.ed.gov/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/a5b6b3c6-f34c-44aa-9fec-c23fe45eb8aa/download/idea-partc-exiting-2013.pdf",
                 "https://data.ed.gov/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/d059eed8-225d-43a3-94e0-9812193bc320/download/c-exitingdatanotes-2012-13.pdf",
                 "https://data.ed.gov/dataset/4a53895a-e535-45f6-b4dd-f57379b125ba/resource/abae76c0-4200-401e-97ae-ad2432d47c04/download/idea-partc-exiting-2012.pdf"
-            ]
+            ],
+            "spatial": "United States",
+            "title": "IDEA Section 618 State Part C Exiting"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "IDEA Section 618 State Part C Dispute Resolution",
-            "description": "Part C of *IDEA* provides funds to states to assist them in developing and implementing statewide, comprehensive, coordinated, multidisciplinary interagency systems to make early intervention services available to all children from birth through age two with disabilities and their families.\r\n#Dispute Resolution\r\n\r\n[*Documentation*](/docs/idea-section-618-state-part-c-dispute-resolution)",
-            "modified": "2024-10-25T14:51:39.500201",
             "accessLevel": "public",
-            "identifier": "edf9f4f1-bc66-4dde-a270-5917168d42c5",
-            "landingPage": "https://www2.ed.gov/programs/osepidea/618-data/state-level-data-files/index.html",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Special Education Programs (OSEP)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Special Education and Rehabilitative Services (OSERS)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "Office of the Secretary (OS)",
-                        "subOrganizationOf": {
-                            "@type": "org:Organization",
-                            "name": "U.S. Department of Education",
-                            "subOrganizationOf": {
-                                "@type": "org:Organization",
-                                "name": "U.S. Government"
-                            }
-                        }
-                    }
-                }
-            },
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Special Education Programs - Research to Practice Division",
                 "hasEmail": "mailto:OSEPideadata@ed.gov"
             },
+            "description": "Part C of *IDEA* provides funds to states to assist them in developing and implementing statewide, comprehensive, coordinated, multidisciplinary interagency systems to make early intervention services available to all children from birth through age two with disabilities and their families.\r\n#Dispute Resolution\r\n\r\n[*Documentation*](/docs/idea-section-618-state-part-c-dispute-resolution)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2022-2023",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2022-2023\r\n\r\n[*Data Notes*][1]\r\n\r\n[*Documentation*][2]\r\n\r\n[1]: https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/60849e69-adc4-49c7-a62f-505e6049d1c8/download/c-disputeresolution-datanotes-2022-23.docx\r\n[2]: https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/4396c1f1-a1cc-4f0e-abf0-b22101f67579/download/idea-partc-dispute-resolution-2022-23.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/3f7c488d-4445-4f17-9625-d147cf885f28/download/cdispres2022-23.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/3f7c488d-4445-4f17-9625-d147cf885f28/download/cdispres2022-23.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2022-2023"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2021-2022",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2021-2022\r\n\r\n[*Data Notes*][1]\r\n\r\n[*Documentation*][2]\r\n\r\n[1]: https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/6553bc8e-d9af-43a0-86a0-06c5d2fd72ac/download/c-disputeresolution-datanotes-2021-22.docx\r\n[2]: https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/66d4eb1d-bfba-4ac7-932c-1f473f3bd1e2/download/idea-partc-dispute-resolution-2021-22.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/57e66563-33b9-4e27-8c33-31e005cb54e4/download/cdispres2021-22.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/57e66563-33b9-4e27-8c33-31e005cb54e4/download/cdispres2021-22.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2021-2022"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2020-2021",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2020-2021\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/55b3eeb2-bafd-4c43-bd1c-f00e0daea740/download/c-disputeresolution-datanotes-2020-21.docx)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/dd7ca2ea-a5ac-4f3f-9b8f-978708753326/download/idea-partc-dispute-resolution-2020-21.docx)",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/3c4f807a-ccd3-4cfb-b324-b4df328e1015/download/cdispres2020-21.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/3c4f807a-ccd3-4cfb-b324-b4df328e1015/download/cdispres2020-21.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2020-2021"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2019-2020",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2019-2020\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/42966ae4-6084-4bb9-9f0e-fccd265b5cd2/download/c-disputeresolution-datanotes-2019-20.docx)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/7cb38cf9-2b5c-4d44-98e9-e3b7b06af57f/download/idea-partc-dispute-resolution-2019-20.docx)",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/a1bf302d-4d1a-46ef-a39b-24cc04ede145/download/cdispres2019-20.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/a1bf302d-4d1a-46ef-a39b-24cc04ede145/download/cdispres2019-20.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2019-2020"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2018-2019",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2018-2019\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/93757ee6-d433-4c5f-aed9-da2d038ce734/download/c-disputeresolution-datanotes-2018-19.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/4a718b11-9aa0-40d9-89e5-df7cb81e88b5/download/idea-partc-dispute-resolution-2018-19.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/0904f9f5-332d-4b5e-9c71-07197eb2822b/download/cdispres2018-19.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/0904f9f5-332d-4b5e-9c71-07197eb2822b/download/cdispres2018-19.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2018-2019"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2017-2018",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2017-2018\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/8319d01e-fade-43a1-870d-68183d2efe98/download/c-disputeresolution-datanotes-2017-18.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/42f38bfb-f6d5-4d24-bf89-630b4b815a97/download/idea-partc-dispute-resolution-2017-18.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/15f960c7-2b35-45eb-b286-aa9b2a1325f5/download/cdispres2017-18.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/15f960c7-2b35-45eb-b286-aa9b2a1325f5/download/cdispres2017-18.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2017-2018"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2016-2017",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2016-2017\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/e16ea08f-e7f1-4ac1-b414-8d7d3da919ee/download/c-disputeresolution-datanotes-2016-17.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/2620d338-807a-4560-8c84-94953a242a62/download/idea-partc-dispute-resolution-2016-17.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/7d87c0f3-15c3-49fc-9b4d-d3700681a9c8/download/cdispres2016-17.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/7d87c0f3-15c3-49fc-9b4d-d3700681a9c8/download/cdispres2016-17.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2016-2017"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2015-2016",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2015-2016\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/44115622-2e47-4656-81f0-455215184539/download/c-disputeresolution-datanotes-2015-16.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/84fd202a-c36f-40f1-8758-f924dd68f110/download/idea-partc-dispute-resolution-2015-16.docx)",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/19d7eb2d-e855-4401-922b-31717f4b110f/download/cdispres2015-16.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/19d7eb2d-e855-4401-922b-31717f4b110f/download/cdispres2015-16.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2015-2016"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2014-2015",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2014-2015\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/4720b8b2-fd02-4b76-b793-db5318d2b56f/download/c-disputeresolution-datanotes-2014-15.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/22a9b436-70f0-4364-8a3b-09221b82648b/download/idea-partc-dispute-resolution-2014.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/2de4c2ff-164b-434e-a481-86e1bc889b14/download/cdispres2014-15.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/2de4c2ff-164b-434e-a481-86e1bc889b14/download/cdispres2014-15.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2014-2015"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2013-2014",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2013-2014\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/10268b10-4796-49a0-86b3-7ef5e503d50b/download/c-disputeresolution-datanotes-2013-14.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/e36c0476-a639-4d2f-a10c-8ce684167489/download/idea-partc-dispute-resolution-2013.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/2b4ae655-08fe-4338-83e7-89383d408595/download/cdispres2013-14.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/2b4ae655-08fe-4338-83e7-89383d408595/download/cdispres2013-14.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2013-2014"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2012-2013",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part C Dispute Resolution\r\n2012-2013\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/2897f9d2-d941-4c61-b9b2-a6187a9f1bda/download/c-disputeresolution-datanotes-2012-13.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/84f4e96f-2764-4ed8-9a39-e5a15d514f59/download/idea-partc-dispute-resolution-2012.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/077c61d1-3b04-4608-b56e-861d241e482c/download/cdispres2012-13.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/077c61d1-3b04-4608-b56e-861d241e482c/download/cdispres2012-13.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2012-2013"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2011-2012",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Dispute Resolution\n2011-2012\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/3244119d-1464-4b98-b3f6-352bf1df487c/download/cdispres2011-12.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/3244119d-1464-4b98-b3f6-352bf1df487c/download/cdispres2011-12.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2011-2012"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2010-2011",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Dispute Resolution\n2010-2011\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/b8be741b-b8a2-4b9c-a49c-3125f791e072/download/cdispres2010-11.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/b8be741b-b8a2-4b9c-a49c-3125f791e072/download/cdispres2010-11.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2010-2011"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2009-2010",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Dispute Resolution\n2009-2010\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/db0ea744-4baa-4301-8d3e-e8e31cf61d64/download/cdispres2009-10.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/db0ea744-4baa-4301-8d3e-e8e31cf61d64/download/cdispres2009-10.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2009-2010"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2008-2009",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Dispute Resolution\n2008-2009\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/d581305b-e98a-4b9f-8fd5-cc5f69a4ff82/download/cdispres2008-09.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/d581305b-e98a-4b9f-8fd5-cc5f69a4ff82/download/cdispres2008-09.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2008-2009"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2007-2008",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Dispute Resolution\n2007-2008\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/931d56e9-fc60-4966-bb9c-96dba264d7f2/download/cdispres2007-08.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/931d56e9-fc60-4966-bb9c-96dba264d7f2/download/cdispres2007-08.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2007-2008"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2006-2007",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part C Dispute Resolution\n2006-2007\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/b0bdf928-ff00-48e4-875a-39478962d9e8/download/cdispres2006-07.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/edf9f4f1-bc66-4dde-a270-5917168d42c5/resource/b0bdf928-ff00-48e4-875a-39478962d9e8/download/cdispres2006-07.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2006-2007"
                 }
             ],
+            "identifier": "edf9f4f1-bc66-4dde-a270-5917168d42c5",
             "isPartOf": "0a53acaf-5ec2-47ba-8867-a7de9d9c5e25",
             "keyword": [
                 "b155e7a9-48f7-4edd-863d-896d48d84367",
@@ -1606,13 +1584,32 @@
                 "special-education",
                 "state-level-data-files"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:20"
-            ],
+            "landingPage": "https://www2.ed.gov/programs/osepidea/618-data/state-level-data-files/index.html",
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-25T14:51:39.500201",
             "programCode": [
                 "018:000"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Special Education Programs (OSEP)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Secretary (OS)",
+                        "subOrganizationOf": {
+                            "@type": "org:Organization",
+                            "name": "U.S. Department of Education",
+                            "subOrganizationOf": {
+                                "@type": "org:Organization",
+                                "name": "U.S. Government"
+                            }
+                        }
+                    }
+                }
+            },
             "references": [
                 "https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/60849e69-adc4-49c7-a62f-505e6049d1c8/download/c-disputeresolution-datanotes-2022-23.docx",
                 "https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/4396c1f1-a1cc-4f0e-abf0-b22101f67579/download/idea-partc-dispute-resolution-2022-23.docx",
@@ -1636,180 +1633,161 @@
                 "https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/e36c0476-a639-4d2f-a10c-8ce684167489/download/idea-partc-dispute-resolution-2013.pdf",
                 "https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/2897f9d2-d941-4c61-b9b2-a6187a9f1bda/download/c-disputeresolution-datanotes-2012-13.pdf",
                 "https://data.ed.gov/dataset/acfc0e54-b4bf-4f1c-bb81-27dd9ff8489b/resource/84f4e96f-2764-4ed8-9a39-e5a15d514f59/download/idea-partc-dispute-resolution-2012.pdf"
-            ]
+            ],
+            "spatial": "United States",
+            "title": "IDEA Section 618 State Part C Dispute Resolution"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "IDEA Section 618 State Part B Dispute Resolution",
-            "description": "Part B of *IDEA* provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services.\r\n#Dispute Resolution\r\n\r\n*[Documentation](/dataset/docs/idea-section-618-state-part-b-dispute-resolution)*",
-            "modified": "2024-10-25T14:49:13.025260",
             "accessLevel": "public",
-            "identifier": "19666ae7-6e53-4cb7-8b86-31795955de11",
-            "landingPage": "https://www2.ed.gov/programs/osepidea/618-data/state-level-data-files/index.html",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Special Education Programs (OSEP)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Special Education and Rehabilitative Services (OSERS)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "Office of the Secretary (OS)",
-                        "subOrganizationOf": {
-                            "@type": "org:Organization",
-                            "name": "U.S. Department of Education",
-                            "subOrganizationOf": {
-                                "@type": "org:Organization",
-                                "name": "U.S. Government"
-                            }
-                        }
-                    }
-                }
-            },
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Special Education Programs - Research to Practice Division",
                 "hasEmail": "mailto:OSEPideadata@ed.gov"
             },
+            "description": "Part B of *IDEA* provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services.\r\n#Dispute Resolution\r\n\r\n*[Documentation](/dataset/docs/idea-section-618-state-part-b-dispute-resolution)*",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2022-2023",
                     "description": "Part B of *IDEA* provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services.\r\n#Dispute Resolution\r\n[*Data Notes*][1]\r\n\r\n[*Data Documentation*][2]\r\n[1]: https://data.ed.gov/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/6f559b54-e58f-457b-9076-3e81ac75dc66/download/b-disputeresolution-datanotes-2022-23.docx\r\n[2]: https://data.ed.gov/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/0a402ca4-e092-43d5-afbf-621268126000/download/idea-partb-dispute-resolution-2022-23.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/ff09e22d-fc88-404b-9527-8e5e6766d12f/download/bdispres2022-23.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/ff09e22d-fc88-404b-9527-8e5e6766d12f/download/bdispres2022-23.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2022-2023"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2021-2022",
                     "description": "Part B of *IDEA* provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services.\r\n#Dispute Resolution\r\n[*Data Notes*][1]\r\n\r\n[*Data Documentation*][2]\r\n[1]: https://data.ed.gov/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/ff4649db-3726-4ed3-a750-3746e88aba32/download/b-disputeresolution-datanotes-2021-22.docx\r\n[2]: https://data.ed.gov/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/773b0e04-8eb1-40da-a8ae-e3a543299845/download/idea-partb-dispute-resolution-2021-22.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/57827762-f1d5-4d74-a356-2091b4c1aa67/download/bdispres2021-22.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/57827762-f1d5-4d74-a356-2091b4c1aa67/download/bdispres2021-22.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2021-2022"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2020-2021",
                     "description": "Part B of *IDEA* provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services.\r\n#Dispute Resolution\r\n\r\n[*Data Notes*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/d6e00baf-b86e-495e-9d92-5ab534f10121/download/b-disputeresolution-datanotes-2020-21.docx)\r\n\r\n[*Data Documentation*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/e3727b6f-57b6-40ed-bb47-dcf1113a2e93/download/idea-partb-dispute-resolution-2020-21.docx)",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/7a32cfe0-bd6c-4e6c-9829-9a8f868516bc/download/bdispres2020-21.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/7a32cfe0-bd6c-4e6c-9829-9a8f868516bc/download/bdispres2020-21.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2020-2021"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2019-2020",
                     "description": "Part B of *IDEA* provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services.\r\n#Dispute Resolution\r\n\r\n[*Data Notes*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/6fa69502-0597-43bc-8ea8-96e908a1545e/download/b-disputeresolution-datanotes-2019-20.docx)\r\n\r\n[*Data Documentation*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/5e7ed923-b87e-4e9f-b461-dfd71ae6d8e6/download/idea-partb-dispute-resolution-2019-20.docx)",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/d8caff9a-1fd4-4c91-a522-9b22dd7bd860/download/bdispres2019-20.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/d8caff9a-1fd4-4c91-a522-9b22dd7bd860/download/bdispres2019-20.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2019-2020"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2018-2019",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Dispute Resolution\r\n2018-2019\r\n\r\n[*Data Notes*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/ed868976-6adc-44b5-b45b-b9c00960e2d4/download/b-disputeresolution-datanotes-2018-19.pdf)\r\n\r\n[*Data Documentation*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/bbd5cd12-12a8-4558-871c-086b77087681/download/idea-partb-dispute-resolution-2018-19.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/04a9f334-bc47-4095-a28a-ae190ccded3d/download/bdispres2018-19.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/04a9f334-bc47-4095-a28a-ae190ccded3d/download/bdispres2018-19.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2018-2019"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2017-2018",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Dispute Resolution\r\n2017-2018\r\n\r\n[*Data Notes*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/162dfe19-14a7-4d3f-a441-c72db6935907/download/b-disputeresolution-datanotes-2017-18.pdf)\r\n\r\n[*Data Documentation*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/61f2e35f-264b-458b-bd8d-de61f85a2206/download/idea-partb-dispute-resolution-2017-18.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/2e662be0-14c4-4b1b-939e-58cc925687b9/download/bdispres2017-18.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/2e662be0-14c4-4b1b-939e-58cc925687b9/download/bdispres2017-18.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2017-2018"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2016-2017",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Dispute Resolution\r\n2016-2017\r\n\r\n[*Data Notes*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/54631357-8d2f-47bf-a1bf-bfa7dda07ef4/download/b-disputeresolution-datanotes-2016-17.pdf)\r\n\r\n[*Data Documentation*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/cef4f9be-1c51-4932-9027-de124f14abaa/download/idea-partb-dispute-resolution-2016-17.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/174104a2-a3d1-4793-9456-dbdda6682147/download/bdispres2016-17.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/174104a2-a3d1-4793-9456-dbdda6682147/download/bdispres2016-17.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2016-2017"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2015-2016",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Dispute Resolution\r\n2015-2016\r\n\r\n[*Data Notes*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/2e38372e-9738-4c72-b8b4-f9c4f2979682/download/b-disputeresolution-datanotes-2015-16.pdf)\r\n\r\n[*Data Documentation*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/dfa82ede-eee0-44b8-99af-f7f90bc1f5ab/download/idea-partb-dispute-resolution-2015-16.docx)",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/ad839b62-eee9-477c-a453-a00789adb304/download/bdispres2015-16.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/ad839b62-eee9-477c-a453-a00789adb304/download/bdispres2015-16.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2015-2016"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2014-2015",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Dispute Resolution\r\n2014-2015\r\n\r\n[*Data Notes*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/afaf061e-39c4-4b93-907a-265daaf6325a/download/b-disputeresolution-datanotes-2014-15.pdf)\r\n\r\n[*Data Documentation*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/22e36d02-0022-4102-bc22-5254e9038144/download/idea-partb-dispute-resolution-2014.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/11b04d4d-18db-47fc-b316-5c2633df63f9/download/bdispres2014-15.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/11b04d4d-18db-47fc-b316-5c2633df63f9/download/bdispres2014-15.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2014-2015"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2013-2014",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Dispute Resolution\r\n2013-2014\r\n\r\n[*Data Notes*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/d3472a28-01dd-44ae-9392-0f335d4099ca/download/b-disputeresolution-datanotes-2013-14.pdf)\r\n\r\n[*Data Documentation*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/69970f3e-8d47-432e-8105-beb046f9796c/download/idea-partb-dispute-resolution-2013.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/c657be89-e3a0-41ed-a5a4-c94ec30503de/download/bdispres2013-14.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/c657be89-e3a0-41ed-a5a4-c94ec30503de/download/bdispres2013-14.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2013-2014"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2012-2013",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Dispute Resolution\r\n2012-2013\r\n\r\n[*Data Notes*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/6100e13a-e38e-491f-9c4e-37204fe5bc5f/download/b-disputeresolution-datanotes-2012-13.pdf)\r\n\r\n[*Data Documentation*](/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/204f3a58-8b86-4879-be71-0e23f0386069/download/idea-partb-dispute-resolution-2012.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/5dcc8500-4108-4dc4-8ec6-dc15404e325e/download/bdispres2012-13.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/5dcc8500-4108-4dc4-8ec6-dc15404e325e/download/bdispres2012-13.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2012-2013"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2011-2012",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Dispute Resolution\n2011-2012\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/e8edc3e1-2479-4d25-b0b7-42ab110407cd/download/bdispres2011-12.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/e8edc3e1-2479-4d25-b0b7-42ab110407cd/download/bdispres2011-12.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2011-2012"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2010-2011",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Dispute Resolution\n2010-2011\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/24ff4337-ac7a-475d-a3b7-94a016d2c461/download/bdispres2010-11.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/24ff4337-ac7a-475d-a3b7-94a016d2c461/download/bdispres2010-11.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2010-2011"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2009-2010",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Dispute Resolution\n2009-2010\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/ec39b570-e45d-4b9e-a2a9-e5e647ae8ae4/download/bdispres2009-10.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/ec39b570-e45d-4b9e-a2a9-e5e647ae8ae4/download/bdispres2009-10.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2009-2010"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2008-2009",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Dispute Resolution\n2008-2009\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/0bad2f67-188a-4e2e-898a-ca4cfb9a5140/download/bdispres2008-09.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/0bad2f67-188a-4e2e-898a-ca4cfb9a5140/download/bdispres2008-09.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2008-2009"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2007-2008",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Dispute Resolution\n2007-2008\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/c6180cfa-1eba-45c7-afa1-866520867bbc/download/bdispres2007-08.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/c6180cfa-1eba-45c7-afa1-866520867bbc/download/bdispres2007-08.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2007-2008"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2006-2007",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Dispute Resolution\n2006-2007\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/7df1bf4e-1e94-4342-802e-8ce48acd7335/download/bdispres2006-07.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/19666ae7-6e53-4cb7-8b86-31795955de11/resource/7df1bf4e-1e94-4342-802e-8ce48acd7335/download/bdispres2006-07.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2006-2007"
                 }
             ],
+            "identifier": "19666ae7-6e53-4cb7-8b86-31795955de11",
             "isPartOf": "0a53acaf-5ec2-47ba-8867-a7de9d9c5e25",
             "keyword": [
                 "b155e7a9-48f7-4edd-863d-896d48d84367",
@@ -1823,13 +1801,32 @@
                 "special-education",
                 "state-level-data-files"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:20"
-            ],
+            "landingPage": "https://www2.ed.gov/programs/osepidea/618-data/state-level-data-files/index.html",
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-25T14:49:13.025260",
             "programCode": [
                 "018:000"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Special Education Programs (OSEP)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Secretary (OS)",
+                        "subOrganizationOf": {
+                            "@type": "org:Organization",
+                            "name": "U.S. Department of Education",
+                            "subOrganizationOf": {
+                                "@type": "org:Organization",
+                                "name": "U.S. Government"
+                            }
+                        }
+                    }
+                }
+            },
             "references": [
                 "https://data.ed.gov/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/6f559b54-e58f-457b-9076-3e81ac75dc66/download/b-disputeresolution-datanotes-2022-23.docx",
                 "https://data.ed.gov/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/0a402ca4-e092-43d5-afbf-621268126000/download/idea-partb-dispute-resolution-2022-23.docx",
@@ -1853,172 +1850,153 @@
                 "https://data.ed.gov/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/69970f3e-8d47-432e-8105-beb046f9796c/download/idea-partb-dispute-resolution-2013.pdf",
                 "https://data.ed.gov/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/6100e13a-e38e-491f-9c4e-37204fe5bc5f/download/b-disputeresolution-datanotes-2012-13.pdf",
                 "https://data.ed.gov/dataset/1c51faad-bd94-40e9-8019-3de431ab22af/resource/204f3a58-8b86-4879-be71-0e23f0386069/download/idea-partb-dispute-resolution-2012.pdf"
-            ]
+            ],
+            "spatial": "United States",
+            "title": "IDEA Section 618 State Part B Dispute Resolution"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "IDEA Section 618 State Level Data Files Part B Assessment",
-            "description": "Part B of *IDEA* provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services.\r\n#Assessment\r\n\r\n[*Documentation*](/docs/idea-section-618-state-level-data-files-part-b-assessment)",
-            "modified": "2024-10-25T14:47:03.008199",
             "accessLevel": "public",
-            "identifier": "1deabc43-21f9-46a8-b93d-8fbbb6d89d48",
-            "landingPage": "https://www2.ed.gov/programs/osepidea/618-data/state-level-data-files/index.html",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Special Education Programs (OSEP)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Special Education and Rehabilitative Services (OSERS)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "Office of the Secretary (OS)",
-                        "subOrganizationOf": {
-                            "@type": "org:Organization",
-                            "name": "U.S. Department of Education",
-                            "subOrganizationOf": {
-                                "@type": "org:Organization",
-                                "name": "U.S. Government"
-                            }
-                        }
-                    }
-                }
-            },
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Special Education Programs - Research to Practice Division",
                 "hasEmail": "mailto:OSEPideadata@ed.gov"
             },
+            "description": "Part B of *IDEA* provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services.\r\n#Assessment\r\n\r\n[*Documentation*](/docs/idea-section-618-state-level-data-files-part-b-assessment)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2022-23",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Assessment\r\n2022-2023\r\n\r\n[*Data Notes*][1]\r\n\r\n[*Data Documentation*][2]\r\n\r\n[1]: https://data.ed.gov/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/792cca05-fe10-4eb0-a788-eee6e1b13fd4/download/b-assessment-datanotes-2022-23.docx\r\n[2]: https://data.ed.gov/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/17943047-a145-4b16-bd36-122ef8d35fca/download/idea-partb-assessment-2022-23.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/31b34fcc-f41d-4ec2-bf87-e237810ac7b4/download/bassessment2022-23.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/31b34fcc-f41d-4ec2-bf87-e237810ac7b4/download/bassessment2022-23.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2022-23"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2021-22",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Assessment\r\n2021-2022\r\n\r\n[*Data Notes*][1]\r\n\r\n[*Data Documentation*][2]\r\n\r\n[1]: https://data.ed.gov/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/4b8769ec-178c-4586-9454-807a245ff292/download/b-assessment-datanotes-2021-22.docx\r\n[2]: https://data.ed.gov/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/8e179e59-a060-4b22-9fb9-6c57c0adf9e4/download/idea-partb-assessment-2021-22.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/6ef97f41-26ab-4dc6-b638-c4fae2882f51/download/bassessment2021-22.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/6ef97f41-26ab-4dc6-b638-c4fae2882f51/download/bassessment2021-22.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2021-22"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2020-21",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Assessment\r\n2020-2021\r\n\r\n*[Data Notes](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/75bfec90-2cb9-434c-a475-1968e8e80b97/download/b-assessment-datanotes-2020-21.docx)\r\n*[Data Documentation](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/54a28c14-0778-4ef5-b6af-6feeaddda57a/download/idea-partb-assessment-2020-21.docx)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/8a02388a-bf0f-48aa-9943-37517c3170c1/download/bassessment2020-21.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/8a02388a-bf0f-48aa-9943-37517c3170c1/download/bassessment2020-21.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2020-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-                    "format": "DOCX",
-                    "title": "2019-20 No Data Available",
                     "description": "Due to the extraordinary circumstances created by the novel Coronavirus disease 2019 (COVID-19) pandemic and resulting school closures, on March 20, 2020, the U.S. Department of Education (Department) offered flexibility to all States/ entities regarding the assessment and accountability requirements under the Elementary and Secondary Education Act of 1965, as amended (ESEA). Specifically, the Department invited States/ entities to request a waiver for the 2019-2020 school year, of the assessment requirements in section 1111(b)(2) of the ESEA, the accountability and school identification requirements in sections 1111(c)(4) and 1111(d)(2)(C)-(D), and certain reporting requirements related to assessments and accountability in section 1111(h). Under these waivers, which all States/ entities requested and received, States/ entities did not have data necessary to submit certain files, including the assessment data files, for SY 2019-2020. OSEP did not collect any SY 2019-20 IDEA Part B Assessment data.",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/2d900d11-93a9-4917-9a4f-c31bc737bc97/download/idea-part-b-assessment-school-year-2019-20-covid19-waivers.docx"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/2d900d11-93a9-4917-9a4f-c31bc737bc97/download/idea-part-b-assessment-school-year-2019-20-covid19-waivers.docx",
+                    "format": "DOCX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "2019-20 No Data Available"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2018-19",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Assessment\r\n2018-2019\r\n\r\n*[Data Notes](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/d5fe77bb-cd6f-4a1d-adbd-262706bec92c/download/b-assessment-datanotes-2018-19.pdf)*\r\n*[Documentation](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/fa03f059-d303-4414-8c8d-9b744fa0a802/download/idea-partb-assessment-2018-19.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/a04939b6-5fea-47c4-b6bd-aaa94ee79067/download/bassessment2018-19.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/a04939b6-5fea-47c4-b6bd-aaa94ee79067/download/bassessment2018-19.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2018-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2017-18",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Assessment\r\n2017-2018\r\n\r\n*[Data Notes](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/4276f5ff-985f-4212-95f8-5fa13e39ea33/download/b-assessment-datanotes-2017-18.pdf)*\r\n*[Data Documentation](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/17f33aa8-e72d-439b-a8c3-1fee884354ce/download/idea-partb-assessment-2017-18.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/89b57bb6-2017-410b-8c92-379fb1686e02/download/bassessment2017-18.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/89b57bb6-2017-410b-8c92-379fb1686e02/download/bassessment2017-18.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2017-18"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2016-17",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Assessment\r\n2016-2017\r\n\r\n*[Data Notes](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/930effcf-bd83-4809-9f5f-a7826a1e3a49/download/b-assessment-datanotes-2016-17.pdf)*\r\n*[Data Documentation](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/d942819f-0ed5-416a-94e2-5e65fd52493d/download/idea-partb-assessment-2016-17.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/b40cff5f-f5a1-40c9-8441-51cee3aca1ff/download/bassessment2016-17.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/b40cff5f-f5a1-40c9-8441-51cee3aca1ff/download/bassessment2016-17.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2016-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2015-2016",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Assessment\r\n2015-2016\r\n\r\n*[Data Notes](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/d963f6e3-faf2-4890-87bd-36b5647235c0/download/b-assessment-datanotes-2015-16.pdf)*\r\n*[Data Documentation](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/4a5a6ab3-0689-432d-ba17-97bc152cba15/download/idea-partb-assessment-2015-16.docx)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/099a90a2-306e-436f-9ca8-c9bf4d6047e8/download/bassessment2015-16.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/099a90a2-306e-436f-9ca8-c9bf4d6047e8/download/bassessment2015-16.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2015-2016"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2014-2015",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Assessment\r\n2014-2015\r\n\r\n*[Data Notes](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/bc65b98f-b71b-4deb-90c0-e390d6cedbdc/download/b-assessment-datanotes-2014-15.pdf)*\r\n*[Data Documentation](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/be4bf6e1-df06-4df8-92c9-3b91931fd06a/download/idea-partb-assessment-2014.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/0106be3f-ee5b-440b-be2f-0e741d47b03a/download/bassessment2014-15.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/0106be3f-ee5b-440b-be2f-0e741d47b03a/download/bassessment2014-15.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2014-2015"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2013-2014",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Assessment\r\n2013-2014\r\n\r\n*[Data Notes](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/489c9ac4-3ecd-4b0c-b5c0-fcb278ed5234/download/b-assessment-datanotes-2013-14.pdf)*\r\n*[Data Documentation](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/bb2c9809-5546-4da3-8c23-365e8e881c20/download/idea-partb-assessment-2013.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/29043602-3a7b-4905-81db-d66848823d63/download/bassessment2013-14.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/29043602-3a7b-4905-81db-d66848823d63/download/bassessment2013-14.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2013-2014"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2012-2013",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Assessment\r\n2012-2013\r\n\r\n*[Data Notes](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/7a1a3fce-4796-4cf8-b431-1aa3308ad531/download/b-assessment-datanotes-2012-13.pdf)*\r\n*[Data Documentation](/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/e44186ce-3d46-4a43-af9a-7414161ef2e6/download/idea-partb-assessment-2012.pdf)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/9796d0cb-4ff2-42ee-9040-b1342875fafc/download/bassessment2012-13.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/9796d0cb-4ff2-42ee-9040-b1342875fafc/download/bassessment2012-13.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2012-2013"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2011-2012",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Assessment\n2011-2012\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/45ba9bed-468d-4791-a61e-ab385debe0e6/download/bassessment2011-12.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/45ba9bed-468d-4791-a61e-ab385debe0e6/download/bassessment2011-12.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2011-2012"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2010-2011",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Assessment\n2010-2011\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/425ca377-dfa5-421c-979d-3e2d9985eae5/download/bassessment2010-11.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/425ca377-dfa5-421c-979d-3e2d9985eae5/download/bassessment2010-11.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2010-2011"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2009-2010",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Assessment\n2009-2010\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/c45db2fb-f75e-4837-8ab2-9732b107ef9e/download/bassessment2009-10.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/c45db2fb-f75e-4837-8ab2-9732b107ef9e/download/bassessment2009-10.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2009-2010"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2008-2009",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Assessment\n2008-2009\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/e8021bfd-f9e5-4e93-a648-9312dd57f086/download/bassessment2008-09.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/e8021bfd-f9e5-4e93-a648-9312dd57f086/download/bassessment2008-09.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2008-2009"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2007-2008",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Assessment\n2007-2008\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/5a60f756-414a-4abe-beaa-3f536f84a102/download/bassessment2007-08.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/1deabc43-21f9-46a8-b93d-8fbbb6d89d48/resource/5a60f756-414a-4abe-beaa-3f536f84a102/download/bassessment2007-08.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2007-2008"
                 }
             ],
+            "identifier": "1deabc43-21f9-46a8-b93d-8fbbb6d89d48",
             "isPartOf": "0a53acaf-5ec2-47ba-8867-a7de9d9c5e25",
             "keyword": [
                 "assessment",
@@ -2030,13 +2008,32 @@
                 "special-education",
                 "state-level-data-files"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:20"
-            ],
+            "landingPage": "https://www2.ed.gov/programs/osepidea/618-data/state-level-data-files/index.html",
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-25T14:47:03.008199",
             "programCode": [
                 "018:000"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Special Education Programs (OSEP)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Secretary (OS)",
+                        "subOrganizationOf": {
+                            "@type": "org:Organization",
+                            "name": "U.S. Department of Education",
+                            "subOrganizationOf": {
+                                "@type": "org:Organization",
+                                "name": "U.S. Government"
+                            }
+                        }
+                    }
+                }
+            },
             "references": [
                 "https://data.ed.gov/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/792cca05-fe10-4eb0-a788-eee6e1b13fd4/download/b-assessment-datanotes-2022-23.docx",
                 "https://data.ed.gov/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/17943047-a145-4b16-bd36-122ef8d35fca/download/idea-partb-assessment-2022-23.docx",
@@ -2058,188 +2055,169 @@
                 "https://data.ed.gov/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/bb2c9809-5546-4da3-8c23-365e8e881c20/download/idea-partb-assessment-2013.pdf",
                 "https://data.ed.gov/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/7a1a3fce-4796-4cf8-b431-1aa3308ad531/download/b-assessment-datanotes-2012-13.pdf",
                 "https://data.ed.gov/dataset/a453fbf9-c8fd-4818-bd06-96752c35d02d/resource/e44186ce-3d46-4a43-af9a-7414161ef2e6/download/idea-partb-assessment-2012.pdf"
-            ]
+            ],
+            "spatial": "United States",
+            "title": "IDEA Section 618 State Level Data Files Part B Assessment"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "IDEA Section 618 State Part B Exiting",
-            "description": "Part B of *IDEA* provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services.\r\n#Exiting\r\n\r\n*[Documentation](/dataset/docs/idea-section-618-state-part-b-exiting)*",
-            "modified": "2024-10-25T14:44:32.565934",
             "accessLevel": "public",
-            "identifier": "0ca544c4-acc3-4afe-a439-827ffe343747",
-            "landingPage": "https://www2.ed.gov/programs/osepidea/618-data/state-level-data-files/index.html",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Special Education Programs (OSEP)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Special Education and Rehabilitative Services (OSERS)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "Office of the Secretary (OS)",
-                        "subOrganizationOf": {
-                            "@type": "org:Organization",
-                            "name": "U.S. Department of Education",
-                            "subOrganizationOf": {
-                                "@type": "org:Organization",
-                                "name": "U.S. Government"
-                            }
-                        }
-                    }
-                }
-            },
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Special Education Programs - Research to Practice Division",
                 "hasEmail": "mailto:OSEPideadata@ed.gov"
             },
+            "description": "Part B of *IDEA* provides funds to states to assist them in providing free appropriate public education (FAPE) to children ages three through 21 with disabilities who are in need of special education and related services.\r\n#Exiting\r\n\r\n*[Documentation](/dataset/docs/idea-section-618-state-part-b-exiting)*",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2022-2023",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n\r\n[*Data Notes*][1]\r\n\r\n[*Data Documentation*][2]\r\n\r\n[1]: https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/040e6cc0-5a9a-40df-8893-89d4b17e168b/download/b-exiting-datanotes-2022-23.docx\r\n[2]: https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/d4d77bbf-fdfb-43de-b653-d23748d12865/download/idea-partb-exiting-2022-23.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/6b0342de-14f4-44ea-9e0e-e10bcfad84f3/download/bexiting2022-23.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/6b0342de-14f4-44ea-9e0e-e10bcfad84f3/download/bexiting2022-23.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2022-2023"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2021-2022",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n\r\n[*Data Notes*][1]\r\n\r\n[*Data Documentation*][2]\r\n\r\n[1]: https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/be2963d1-34df-4836-bfd7-bb75398bde84/download/b-exiting-datanotes-2021-22.docx\r\n[2]: https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/cc5a2ed7-8a99-41a4-a6d3-2d98ffd06755/download/idea-partb-exiting-2021-22.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/37be9243-53f6-4308-94a9-f44374ed88c3/download/bexiting2021-22-2.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/37be9243-53f6-4308-94a9-f44374ed88c3/download/bexiting2021-22-2.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2021-2022"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2020-2021",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/f1d177ee-de67-490c-8856-3b3061b881b9/download/b-exiting-datanotes-2020-21.docx)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/208a1d8c-ebb9-42e8-8c59-c6b2a36e2c67/download/idea-partb-exiting-2020-21.docx)",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/bff63bd7-574e-45cc-b733-4cf81f1764db/download/bexiting2020-21-13.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/bff63bd7-574e-45cc-b733-4cf81f1764db/download/bexiting2020-21-13.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2020-2021"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2019-2020",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/308439a7-f2d4-4dfb-9d99-21515c88a33e/download/b-exiting-datanotes-2019-20.docx)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/5358e526-9875-4743-b928-8324ab288c71/download/idea-partb-exiting-2019-20.docx)",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/c85f9ff8-170e-4bc6-80b5-c880013f89d2/download/bexiting2019-20-10.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/c85f9ff8-170e-4bc6-80b5-c880013f89d2/download/bexiting2019-20-10.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2019-2020"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2018-2019",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n2018-2019\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/7040ce1e-a3fd-4221-91f4-e9dca843d902/download/b-exiting-datanotes-2018-19.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/58b4d778-e1a4-42a1-9d8f-7eaa45577b8d/download/idea-partb-exiting-2018-19.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/bfa0fe39-f5b1-42ff-9424-e823566158b3/download/bexiting2018-19-4.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/bfa0fe39-f5b1-42ff-9424-e823566158b3/download/bexiting2018-19-4.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2018-2019"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2017-2018",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n2017-2018\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/a25dbfab-1869-4fcb-babe-f18555e6236d/download/b-exiting-datanotes-2017-18.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/8ef2d0f7-d0c7-4de0-b3b0-94602131f37b/download/idea-partb-exiting-2017-18.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/d67ece99-dc2e-4184-8128-22c7830e0198/download/bexiting2017-18.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/d67ece99-dc2e-4184-8128-22c7830e0198/download/bexiting2017-18.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2017-2018"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2016-2017",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n2016-2017\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/8927495f-1b86-4b3f-90ab-92d158accc67/download/b-exiting-datanotes-2016-17.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/2099bd91-685e-4ec4-b786-5be574f22478/download/idea-partb-exiting-2016-17.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/c7fe41d2-d455-4f0a-9c5b-da27571b81ef/download/bexiting2016-17.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/c7fe41d2-d455-4f0a-9c5b-da27571b81ef/download/bexiting2016-17.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2016-2017"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2015-2016",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n2015-2016\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/9d8391ea-4ae4-4bba-8e93-27ebed528309/download/b-exiting-datanotes-2015-16.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/97718b00-8d5d-4c24-ac4b-09eca6750b42/download/idea-partb-exiting-2015-16.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/b708c838-4e59-4b0a-a35e-684f50c5bbe5/download/bexiting2015-16.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/b708c838-4e59-4b0a-a35e-684f50c5bbe5/download/bexiting2015-16.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2015-2016"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2014-2015",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n2014-2015\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/01c98419-5fdb-4c1e-9ed8-bb166221c2cb/download/b-exiting-datanotes-2014-15.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/004afb66-c185-4c73-ac2c-40e00a886900/download/idea-partb-exiting-2014.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/9e07ae8c-80f6-4201-ab72-b493184f52d0/download/bexiting2014-15.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/9e07ae8c-80f6-4201-ab72-b493184f52d0/download/bexiting2014-15.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2014-2015"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2013-2014",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n2013-2014\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/5ca9e333-51bc-4d97-ac9b-b6bf551c28a4/download/b-exiting-datanotes-2013-14.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/62b73f1a-9cab-432a-8a79-7b375e5902d7/download/idea-partb-exiting-2013.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/18b4aebd-d792-43d0-9383-a41e27e11514/download/bexiting2013-14.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/18b4aebd-d792-43d0-9383-a41e27e11514/download/bexiting2013-14.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2013-2014"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2012-2013",
                     "description": "#IDEA Section 618 Data Products\r\n##State Level Data Files Part B Exiting\r\n2012-2013\r\n\r\n[*Data Notes*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/ddcc5483-a577-47cc-8d36-e5946358a242/download/b-exiting-datanotes-2012-13.pdf)\r\n\r\n[*Data Documentation*](https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/7fdad30b-28c0-4539-a7ca-2c4525b49a87/download/idea-partb-exiting-2012.pdf)",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/81d3326e-dea1-4111-86f7-d5e617f66143/download/bexiting2012-13.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/81d3326e-dea1-4111-86f7-d5e617f66143/download/bexiting2012-13.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2012-2013"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2011-2012",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Exiting\n2011-2012\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/688a7995-dafc-45be-bef7-e4896072172d/download/bexiting2011-12.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/688a7995-dafc-45be-bef7-e4896072172d/download/bexiting2011-12.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2011-2012"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2010-2011",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Exiting\n2010-2011\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/9ec503c3-2a51-47f1-8e88-a6d5b55f6e8f/download/bexiting2010-11.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/9ec503c3-2a51-47f1-8e88-a6d5b55f6e8f/download/bexiting2010-11.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2010-2011"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2009-2010",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Exiting\n2009-2010\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/219e6827-76c1-4bf2-bbf0-227219314315/download/bexiting2009-10.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/219e6827-76c1-4bf2-bbf0-227219314315/download/bexiting2009-10.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2009-2010"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2008-2009",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Exiting\n2008-2009\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/55bbd0cb-39c7-443e-846f-d4d06d9a4b8b/download/bexiting2008-09.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/55bbd0cb-39c7-443e-846f-d4d06d9a4b8b/download/bexiting2008-09.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2008-2009"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2007-2008",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Exiting\n2007-2008\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/9695ae04-1bb0-4f9b-bcd4-9bd47070ae38/download/bexiting2007-08.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/9695ae04-1bb0-4f9b-bcd4-9bd47070ae38/download/bexiting2007-08.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2007-2008"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2006-2007",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Exiting\n2006-2007\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/f9af691b-02ee-4607-9d83-e25d2375c257/download/bexiting2006-07.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/f9af691b-02ee-4607-9d83-e25d2375c257/download/bexiting2006-07.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2006-2007"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "2005-2006",
                     "description": "#IDEA Section 618 Data Products\n##State Level Data Files Part B Exiting\n2005-2006\n\n*[Documentation](/documentation/idea-section-618-state-level-documentation)*",
-                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/719ee39c-6125-4392-8f34-6a877c1977f8/download/bexiting2005-06.csv"
+                    "downloadURL": "https://data.ed.gov/dataset/0ca544c4-acc3-4afe-a439-827ffe343747/resource/719ee39c-6125-4392-8f34-6a877c1977f8/download/bexiting2005-06.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "2005-2006"
                 }
             ],
+            "identifier": "0ca544c4-acc3-4afe-a439-827ffe343747",
             "isPartOf": "0a53acaf-5ec2-47ba-8867-a7de9d9c5e25",
             "keyword": [
                 "b155e7a9-48f7-4edd-863d-896d48d84367",
@@ -2251,13 +2229,32 @@
                 "special-education",
                 "state-level-data-files"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:20"
-            ],
+            "landingPage": "https://www2.ed.gov/programs/osepidea/618-data/state-level-data-files/index.html",
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-25T14:44:32.565934",
             "programCode": [
                 "018:000"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Special Education Programs (OSEP)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Secretary (OS)",
+                        "subOrganizationOf": {
+                            "@type": "org:Organization",
+                            "name": "U.S. Department of Education",
+                            "subOrganizationOf": {
+                                "@type": "org:Organization",
+                                "name": "U.S. Government"
+                            }
+                        }
+                    }
+                }
+            },
             "references": [
                 "https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/040e6cc0-5a9a-40df-8893-89d4b17e168b/download/b-exiting-datanotes-2022-23.docx",
                 "https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/d4d77bbf-fdfb-43de-b653-d23748d12865/download/idea-partb-exiting-2022-23.docx",
@@ -2281,48 +2278,33 @@
                 "https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/62b73f1a-9cab-432a-8a79-7b375e5902d7/download/idea-partb-exiting-2013.pdf",
                 "https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/ddcc5483-a577-47cc-8d36-e5946358a242/download/b-exiting-datanotes-2012-13.pdf",
                 "https://data.ed.gov/dataset/d59e7546-1a69-43ea-821b-24569a091233/resource/7fdad30b-28c0-4539-a7ca-2c4525b49a87/download/idea-partb-exiting-2012.pdf"
-            ]
+            ],
+            "spatial": "United States",
+            "title": "IDEA Section 618 State Part B Exiting"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "2013-14 Gifted and Talented Enrollment Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on students enrolled in gifted and talented programs for all states. The file contains three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:54:21.608776",
             "accessLevel": "public",
-            "identifier": "b486d8ff-3986-4c28-b1f0-4d4cf3da105f",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office for Civil Rights (OCR)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Secretary (OS)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "U.S. Department of Education",
-                        "subOrganizationOf": {
-                            "@type": "org:Organization",
-                            "name": "U.S. Government"
-                        }
-                    }
-                }
-            },
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on students enrolled in gifted and talented programs for all states. The file contains three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Gifted and Talented Enrollment",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on students enrolled in gifted and talented programs for all states. The file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Gifted-Talented-Programs.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Gifted-Talented-Programs.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Gifted and Talented Enrollment"
                 }
             ],
+            "identifier": "b486d8ff-3986-4c28-b1f0-4d4cf3da105f",
             "keyword": [
                 "Elementary-and-secondary",
                 "Language",
@@ -2335,22 +2317,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:54:21.608776",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 Discipline Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-            "modified": "2024-10-23T14:49:04.445533",
-            "accessLevel": "public",
-            "identifier": "997e01a7-1c4d-427e-a6b6-de4bc44ce590",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -2367,165 +2339,175 @@
                     }
                 }
             },
+            "title": "2013-14 Gifted and Talented Enrollment Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Incidents of Preschool Corporal Punishment and Suspension",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-Discipline.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-Discipline.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Incidents of Preschool Corporal Punishment and Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool Expulsions",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-Expulsions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-Expulsions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool Expulsions"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool One or More Out-of-School Suspension",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-One-or-More-out-of-school-suspensions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-One-or-More-out-of-school-suspensions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool One or More Out-of-School Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool More Than One Out-of-School Suspension",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-More-than-one-out-of-school-suspension.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-More-than-one-out-of-school-suspension.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool More Than One Out-of-School Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool One Out-of-School Suspension",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-One-out-of-school-suspension.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-One-out-of-school-suspension.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool One Out-of-School Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool Corporal Punishment",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-Corporal-Punishment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-Corporal-Punishment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool Corporal Punishment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Days Missed Due to Out-of-School Suspensions",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Days-missed-due-to-out-of-school-suspensions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Days-missed-due-to-out-of-school-suspensions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Days Missed Due to Out-of-School Suspensions"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Transfers to Alternative Schools",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Transferred-to-alternative-school.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Transferred-to-alternative-school.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Transfers to Alternative Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Referrals to Law Enforcement",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Referral-to-law-enforcement.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Referral-to-law-enforcement.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Referrals to Law Enforcement"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions with and without Educational Services",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Expulsions-with-and-without-educational-services.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Expulsions-with-and-without-educational-services.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions with and without Educational Services"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions with Educational Services",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Expulsions-with-educational-services.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Expulsions-with-educational-services.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions with Educational Services"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "More Than One Out-of-School Suspension",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/More-than-one-out-of-school-suspension.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/More-than-one-out-of-school-suspension.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "More Than One Out-of-School Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "In-school Suspension",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/In-school-suspensions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/In-school-suspensions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "In-school Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "School-related Arrests",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/School-related-arrests.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/School-related-arrests.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "School-related Arrests"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions Under Zero Tolerance Policies",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Expulsions-due-to-zero-tolerance-policies.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Expulsions-due-to-zero-tolerance-policies.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions Under Zero Tolerance Policies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions without Educational Services",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Expulsions-without-educational-services.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Expulsions-without-educational-services.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions without Educational Services"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "One or More Out-of-School Suspensions",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/One-or-more-out-of-school-suspensions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/One-or-more-out-of-school-suspensions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "One or More Out-of-School Suspensions"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "One Out-of-School Suspension",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/One-out-of-school-suspension.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/One-out-of-school-suspension.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "One Out-of-School Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Corporal Punishment",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Corporal-Punishment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Corporal-Punishment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Corporal Punishment"
                 }
             ],
+            "identifier": "997e01a7-1c4d-427e-a6b6-de4bc44ce590",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -2539,22 +2521,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 Mathematics and Science Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for schools offering courses and classes in mathematics and science taught by certified teachers for all states. As well as student enrollment data for all states, presented by mathematics and science course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students. For each science course, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:49:03.525436",
-            "accessLevel": "public",
-            "identifier": "5bd5e3c2-75be-40dc-9a3a-9c36ee7a3e19",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:49:04.445533",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -2571,157 +2543,167 @@
                     }
                 }
             },
+            "title": "2015-16 Discipline Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for schools offering courses and classes in mathematics and science taught by certified teachers for all states. As well as student enrollment data for all states, presented by mathematics and science course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students. For each science course, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Physics",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by science course. For each science course, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Physics.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Physics.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Physics"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Chemistry",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by science course. For each science course, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Chemistry.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Chemistry.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Chemistry"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Biology",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by science course. For each science course, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Biology.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Biology.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Biology"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Calculus",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Calculus.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Calculus.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Calculus"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Advanced Mathematics",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Advanced-Mathematics.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Advanced-Mathematics.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Advanced Mathematics"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra II",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Algebra-II.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Algebra-II.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra II"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Geometry in High School",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Geometry-in-High-School.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Geometry-in-High-School.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Geometry in High School"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Geometry Grade 8",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Geometry-in-Grade-8.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Geometry-in-Grade-8.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Geometry Grade 8"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grades 11-12",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Algebra-I-Grades-11-12.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Algebra-I-Grades-11-12.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grades 11-12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grades 9-10",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Algebra-I-Grades-9-10.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Algebra-I-Grades-9-10.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grades 9-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grade 8",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Algebra-I-Grade-8.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Algebra-I-Grade-8.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grade 8"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grade 7",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Algebra-I-Grade-7.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-in-Algebra-I-Grade-7.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grade 7"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "High School Science classes taught by Certified Teachers",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for school classes in mathematics and science taught by certified teachers for all states. Each file contains one spreadsheet with classes data by type of course.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/High-School-Science-Classes-Certified-Teachers.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/High-School-Science-Classes-Certified-Teachers.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "High School Science classes taught by Certified Teachers"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "High School Mathematics classes taught by Certified Teachers",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for school classes in mathematics and science taught by certified teachers for all states. Each file contains one spreadsheet with classes data by type of course.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/High-School-Math-Classes-Certified-Teachers.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/High-School-Math-Classes-Certified-Teachers.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "High School Mathematics classes taught by Certified Teachers"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Middle School Mathematics classes taught by Certified Teachers",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for school classes in mathematics and science taught by certified teachers for all states. Each file contains one spreadsheet with classes data by type of course.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Middle-School-Math-Classes-Certified-Teachers.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Middle-School-Math-Classes-Certified-Teachers.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Middle School Mathematics classes taught by Certified Teachers"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "High Schools offering Science courses",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for schools offering courses in mathematics and science for all states. Each file contains one spreadsheet for total schools.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/High-Schools-Offering-Science-Classes.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/High-Schools-Offering-Science-Classes.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "High Schools offering Science courses"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "High Schools offering Mathematics courses",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for schools offering courses in mathematics and science for all states. Each file contains one spreadsheet for total schools.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/High-Schools-Offering-Mathematics-Classes.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/High-Schools-Offering-Mathematics-Classes.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "High Schools offering Mathematics courses"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Middle Schools offering Mathematic courses",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for schools offering courses in mathematics and science for all states. Each file contains one spreadsheet for total schools.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Middle-Schools-Offering-Mathematics-Classes-Grade-7-and-8.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Middle-Schools-Offering-Mathematics-Classes-Grade-7-and-8.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Middle Schools offering Mathematic courses"
                 }
             ],
+            "identifier": "5bd5e3c2-75be-40dc-9a3a-9c36ee7a3e19",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -2736,22 +2718,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:49:03.525436",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Discipline Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-            "modified": "2024-10-23T14:49:01.281946",
-            "accessLevel": "public",
-            "identifier": "1f3135d8-14b9-45ca-85e3-3c6d18647a22",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -2768,133 +2740,143 @@
                     }
                 }
             },
+            "title": "2015-16 Mathematics and Science Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool Expulsions",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Preschool-Expulsions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Preschool-Expulsions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool Expulsions"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool One or More Out-of-School Suspension",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Preschool-One-or-More-Out-of-School-Suspensions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Preschool-One-or-More-Out-of-School-Suspensions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool One or More Out-of-School Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool More Than One Out-of-School Suspension",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Preschool-More-than-One-Out-of-School-Suspension.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Preschool-More-than-One-Out-of-School-Suspension.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool More Than One Out-of-School Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool One Out-of-School Suspension",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Preschool-One-Out-of-School-Suspension.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Preschool-One-Out-of-School-Suspension.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool One Out-of-School Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "School Arrests",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/School-related-arrests.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/School-related-arrests.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "School Arrests"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Referrals to Law Enforcement",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Referral-to-law-enforcement.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Referral-to-law-enforcement.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Referrals to Law Enforcement"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions Under Zero Tolerance Policies",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Expulsions-under-zero-tolerance-policies.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Expulsions-under-zero-tolerance-policies.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions Under Zero Tolerance Policies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions with and without Educational Services",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Expulsions-with-and-without-educational-services.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Expulsions-with-and-without-educational-services.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions with and without Educational Services"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions without Educational Services",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Expulsions-without-educational-services.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Expulsions-without-educational-services.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions without Educational Services"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions with Educational Services",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Expulsions-with-educational-services.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Expulsions-with-educational-services.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions with Educational Services"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "One or More Out-of-School Suspensions",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/One-or-more-out-of-school-suspensions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/One-or-more-out-of-school-suspensions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "One or More Out-of-School Suspensions"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "More Than One Out-of-School Suspension",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/More-than-one-out-of-school-suspension.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/More-than-one-out-of-school-suspension.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "More Than One Out-of-School Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "One Out-of-School Suspension",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/One-out-of-school-suspension.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/One-out-of-school-suspension.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "One Out-of-School Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "In-school Suspension",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/In-School-Suspensions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/In-School-Suspensions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "In-school Suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Corporal Punishment",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: male students with disabilities, female students with disabilities, total students with disabilities, male students without disabilities, female students without disabilities, total students without disabilities, male students with and without disabilities, female students with and without disabilities, and total students with and without disabilities. This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool children, male preschool children, and female preschool children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Corporal-Punishment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Corporal-Punishment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Corporal Punishment"
                 }
             ],
+            "identifier": "1f3135d8-14b9-45ca-85e3-3c6d18647a22",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -2908,22 +2890,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:49:01.281946",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 Mathematics and Science Civil Rights Data Collection",
-            "description": "The 2017-18 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for schools offering courses and student enrollment data in mathematics and science courses for all states.",
-            "modified": "2024-10-23T14:48:58.552288",
-            "accessLevel": "public",
-            "identifier": "d9f79af3-1c18-4210-ab75-66241ab75fc2",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -2940,125 +2912,135 @@
                     }
                 }
             },
+            "title": "2013-14 Discipline Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2017-18 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for schools offering courses and student enrollment data in mathematics and science courses for all states.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Physics",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by science course. For each science course, there are three spreadsheets: total students, male students, and female students",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Physics.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Physics.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Physics"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Chemistry",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by science course. For each science course, there are three spreadsheets: total students, male students, and female students",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Chemistry.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Chemistry.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Chemistry"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Biology",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by science course. For each science course, there are three spreadsheets: total students, male students, and female students",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Biology.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Biology.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Biology"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Advanced mathematics",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Advanced-Mathematics.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Advanced-Mathematics.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Advanced mathematics"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra II",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Algebra-II.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Algebra-II.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra II"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Geometry in high school",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Geometry-in-High-School.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Geometry-in-High-School.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Geometry in high school"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Geometry Grade 8",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Geometry-in-Grade-8.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Geometry-in-Grade-8.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Geometry Grade 8"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grades 11-12",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Algebra-I_Grades-11-12.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Algebra-I_Grades-11-12.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grades 11-12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grades 9-10",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Algebra-I_Grades-9-10.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Algebra-I_Grades-9-10.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grades 9-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grade 8",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Algebra-I_Grade-8.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Algebra-I_Grade-8.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grade 8"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grade 7",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by mathematics course. For each mathematics course, except Algebra I Grade 7 and Geometry Grade 8, there are three spreadsheets: total students, male students, and female students. For each Algebra I Grade 7 and Geometry Grade 8 course, there is one spreadsheet for total students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Algebra-I_Grade-7.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Enrollment-in-Algebra-I_Grade-7.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grade 7"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "High schools offering science courses",
                     "description": "This set of Excel files contains data for schools offering courses in mathematics and science for all states. Each file contains one spreadsheet for total schools.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/High-Schools-Offering-Science-Classes.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/High-Schools-Offering-Science-Classes.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "High schools offering science courses"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "High schools offering mathematics courses",
                     "description": "This set of Excel files contains data for schools offering courses in mathematics and science for all states. Each file contains one spreadsheet for total schools.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/High-Schools-Offering-Mathematics-Classes.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/High-Schools-Offering-Mathematics-Classes.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "High schools offering mathematics courses"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Middle schools offering mathematics courses",
                     "description": "This set of Excel files contains data for schools offering courses in mathematics and science for all states. Each file contains one spreadsheet for total schools.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Middle-Schools-Offering-Mathematics-Classes.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Mathematics-and-Science/Middle-Schools-Offering-Mathematics-Classes.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Middle schools offering mathematics courses"
                 }
             ],
+            "identifier": "d9f79af3-1c18-4210-ab75-66241ab75fc2",
             "isPartOf": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "keyword": [
                 "Elementary-and-secondary",
@@ -3074,22 +3056,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:48:58.552288",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Retention by Grade Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:48:57.749237",
-            "accessLevel": "public",
-            "identifier": "835be722-b8d0-494c-ab16-c2a11e6a76a3",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -3106,117 +3078,127 @@
                     }
                 }
             },
+            "title": "2017-18 Mathematics and Science Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 12",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-12.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-12.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 11",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-11.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-11.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 10",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-10.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-10.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 9",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-9.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-9.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 9"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 8",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-8.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-8.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 8"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 7",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-7.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-7.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 7"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 6",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-6.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-6.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 6"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 5",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-5.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-5.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 5"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 4",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-4.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-4.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 4"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 3",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-3.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-3.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 3"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 2",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-2.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-2.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 2"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 1",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-1.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Grade-1.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 1"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Kindergarten",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Kindergarten.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Retention-in-Kindergarten.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Kindergarten"
                 }
             ],
+            "identifier": "835be722-b8d0-494c-ab16-c2a11e6a76a3",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -3231,22 +3213,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:48:57.749237",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 Student Retention Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:48:56.579165",
-            "accessLevel": "public",
-            "identifier": "d409a2c0-d3d4-474e-b867-ef7c111bb797",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -3263,117 +3235,127 @@
                     }
                 }
             },
+            "title": "2013-14 Retention by Grade Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 12",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-12.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-12.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 11",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-11.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-11.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 10",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-10.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-10.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 9",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-9.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-9.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 9"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 8",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-8.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-8.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 8"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 7",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-7.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-7.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 7"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 6",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-6.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-6.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 6"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 5",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-5.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-5.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 5"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 4",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-4.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-4.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 4"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 3",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-3.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-3.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 3"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 2",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-2.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-2.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 2"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 1",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-1.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Grade-1.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 1"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Kindergarten",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Kindergarten.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Retention-in-Kindergarten.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Kindergarten"
                 }
             ],
+            "identifier": "d409a2c0-d3d4-474e-b867-ef7c111bb797",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -3387,22 +3369,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:48:56.579165",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 Student Retention Civil Rights Data Collection",
-            "description": "The 2017-18 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:48:56.195254",
-            "accessLevel": "public",
-            "identifier": "39fe5aba-e4f6-4569-91e3-6187fb25403c",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -3419,117 +3391,127 @@
                     }
                 }
             },
+            "title": "2015-16 Student Retention Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2017-18 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 12",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-12.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-12.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 11",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-11.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-11.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 10",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-10.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-10.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 9",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-9.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-9.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 9"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 8",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-8.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-8.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 8"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 7",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-7.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-7.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 7"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 6",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-6.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-6.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 6"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 5",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-5.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-5.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 5"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 4",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-4.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-4.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 4"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 3",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-3.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-3.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 3"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 2",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-2.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-2.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 2"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Grade 1",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-1.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Grade-1.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Grade 1"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Kindergarten",
                     "description": "This set of Excel files contains student retention data for all states, presented by grade. For each grade, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Kindergarten.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Retention/Retention-(by-grade)/Retention-in-Kindergarten.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Kindergarten"
                 }
             ],
+            "identifier": "39fe5aba-e4f6-4569-91e3-6187fb25403c",
             "isPartOf": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "keyword": [
                 "Elementary-and-secondary",
@@ -3544,22 +3526,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:48:56.195254",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Mathematics and Science Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:48:52.027638",
-            "accessLevel": "public",
-            "identifier": "a0ba036f-c364-415b-8516-32491541a488",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -3576,101 +3548,111 @@
                     }
                 }
             },
+            "title": "2017-18 Student Retention Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Physics",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Physics.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Physics.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Physics"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Chemistry",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Chemistry.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Chemistry.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Chemistry"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Biology",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Biology.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Biology.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Biology"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Advanced Mathematics",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Advanced-Mathematics.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Advanced-Mathematics.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Advanced Mathematics"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Calculus",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Calculus.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Calculus.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Calculus"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra II",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Algebra-II.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Algebra-II.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra II"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Geometry",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Geometry.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Geometry.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Geometry"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grade 11-12",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Algebra-I-11-12.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Algebra-I-11-12.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grade 11-12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grade 9-10",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Algebra-I-9-10.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Algebra-I-9-10.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grade 9-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Algebra I Grade 7-8",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Algebra-I-7-8.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Enrollment-in-Algebra-I-7-8.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Algebra I Grade 7-8"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Schools Offering Mathematics and Science Classes",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for schools offering classes in mathematics and science, and student enrollment for all states. The file contains one spreadsheet for total schools.  For all mathematics and science courses, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Classes-in-Mathematics-and-Science.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Classes-in-Mathematics-and-Science.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Schools Offering Mathematics and Science Classes"
                 }
             ],
+            "identifier": "a0ba036f-c364-415b-8516-32491541a488",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -3684,22 +3666,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:48:52.027638",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 Restraint and Seclusion Civil Rights Data Collection",
-            "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-            "modified": "2024-10-23T14:48:44.674921",
-            "accessLevel": "public",
-            "identifier": "b0f2b4e8-86bd-4b84-ab03-235d5c94d5e8",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -3716,85 +3688,95 @@
                     }
                 }
             },
+            "title": "2013-14 Mathematics and Science Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Physical restraint Non IDEA",
                     "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-not-served-under-IDEA_phys.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-not-served-under-IDEA_phys.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Physical restraint Non IDEA"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Seclusion Non IDEA",
                     "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-not-served-under-IDEA_seclusion.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-not-served-under-IDEA_seclusion.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Seclusion Non IDEA"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Seclusion IDEA",
                     "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-served-under-IDEA_seclusion.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-served-under-IDEA_seclusion.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Seclusion IDEA"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Seclusion IDEA/Non IDEA",
                     "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-under-IDEA-or-not_secl.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-under-IDEA-or-not_secl.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Seclusion IDEA/Non IDEA"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Physical restraint IDEA",
                     "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-served-under-IDEA_phys.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-served-under-IDEA_phys.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Physical restraint IDEA"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Physical restraint IDEA/Non IDEA",
                     "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-under-IDEA-or-not_phys.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-under-IDEA-or-not_phys.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Physical restraint IDEA/Non IDEA"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Mechanical restraint Non IDEA",
                     "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-not-served-under-IDEA_mech.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-not-served-under-IDEA_mech.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mechanical restraint Non IDEA"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Mechanical restraint IDEA",
                     "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-served-under-IDEA_mech.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-served-under-IDEA_mech.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mechanical restraint IDEA"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Mechanical restraint IDEA/Non IDEA",
                     "description": "This set of Excel files contains mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-under-IDEA-or-not_mech.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Restraint-and-Seclusion/Restraint-and-Seclusion/Restraint-or-Seclusion.Students-under-IDEA-or-not_mech.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mechanical restraint IDEA/Non IDEA"
                 }
             ],
+            "identifier": "b0f2b4e8-86bd-4b84-ab03-235d5c94d5e8",
             "isPartOf": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "keyword": [
                 "Elementary-and-secondary",
@@ -3811,22 +3793,12 @@
                 "seculsion",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 Discipline Civil Rights Data Collection",
-            "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. It also contains data on school days missed by students due to out-of-school-suspensions, for all states.",
-            "modified": "2024-10-23T14:48:43.830572",
-            "accessLevel": "public",
-            "identifier": "5f7b954d-5a60-45d7-959a-b1a0a0e66058",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:48:44.674921",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -3843,85 +3815,95 @@
                     }
                 }
             },
+            "title": "2017-18 Restraint and Seclusion Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities. It also contains data on school days missed by students due to out-of-school-suspensions, for all states.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Days missed due to out-of-school suspensions",
                     "description": "This Excel file contains data on school days missed by students due to out-of-school-suspensions, for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Days-missed-due-to-OoS-Suspensions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Days-missed-due-to-OoS-Suspensions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Days missed due to out-of-school suspensions"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions with and without educational services",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Expulsions-w-and-wo-ed-service/Expulsions-w-and-wo-ed-service_by-disability-and-no.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Expulsions-w-and-wo-ed-service/Expulsions-w-and-wo-ed-service_by-disability-and-no.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions with and without educational services"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions with educational services",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Expulsions-with-ed-service/Expulsions-with-ed-service_by-disability-and-no.xlsx"
-                },
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Expulsions-with-ed-service/Expulsions-with-ed-service_by-disability-and-no.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions with educational services"
+                },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "More than one out-of-school suspension",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/More-Than-One-Oos-Suspensions/More-Than-One-OoS-Suspensions_by-disability-and-no.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/More-Than-One-Oos-Suspensions/More-Than-One-OoS-Suspensions_by-disability-and-no.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "More than one out-of-school suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "In-school suspension",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/One-or-More-In-School-Suspensions/One-or-More-In-School-Suspensions_by-disability-and-no.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/One-or-More-In-School-Suspensions/One-or-More-In-School-Suspensions_by-disability-and-no.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "In-school suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Expulsions without educational services",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Expulsions-without-ed-service/Expulsions-without-ed-service_by-disability-and-no.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Expulsions-without-ed-service/Expulsions-without-ed-service_by-disability-and-no.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Expulsions without educational services"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "One or more out-of-school suspensions",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/One-or-More-Oos-Suspensions/One-or-More-OoS-Suspensions_by-disability-and-no.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/One-or-More-Oos-Suspensions/One-or-More-OoS-Suspensions_by-disability-and-no.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "One or more out-of-school suspensions"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "One out-of-school suspension",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/One-Out-of-School%20Suspensions/One-Out-of-School-Suspensions_by-disability-and-no.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/One-Out-of-School%20Suspensions/One-Out-of-School-Suspensions_by-disability-and-no.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "One out-of-school suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Corporal punishment",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are nine spreadsheets: total students with and without disabilities; male students with and without disabilities; female students with and without disabilities; total students with disabilities; male students with disabilities; female students with disabilities; total students without disabilities; male students without disabilities; and female students without disabilities.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Corporal-Punishment/Corporal-Punishment_by-Disability-and-no.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Corporal-Punishment/Corporal-Punishment_by-Disability-and-no.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Corporal punishment"
                 }
             ],
+            "identifier": "5f7b954d-5a60-45d7-959a-b1a0a0e66058",
             "isPartOf": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "keyword": [
                 "Elementary-and-secondary",
@@ -3936,22 +3918,12 @@
                 "student-discipline",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:48:43.830572",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 Classroom Teachers Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. These Excel files contain data on classroom teachers, including full-time equivalency counts, certification, years of experience, and retention for all states. As well as full-time equivalent support staff, and schools with support staff, by type of staff and for all states. Each file contains one spreadsheet for elementary, middle, or high schools, contains one spreadsheet for total teachers.",
-            "modified": "2024-10-23T14:45:30.612602",
-            "accessLevel": "public",
-            "identifier": "d85d57b7-7c5c-479d-bd0e-3b4c18158e48",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -3968,77 +3940,87 @@
                     }
                 }
             },
+            "title": "2017-18 Discipline Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. These Excel files contain data on classroom teachers, including full-time equivalency counts, certification, years of experience, and retention for all states. As well as full-time equivalent support staff, and schools with support staff, by type of staff and for all states. Each file contains one spreadsheet for elementary, middle, or high schools, contains one spreadsheet for total teachers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Support Staff in High Schools",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on full-time equivalent support staff, and schools with support staff, by type of staff and for all states. Each file contains one spreadsheet for elementary, middle, or high schools.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/FTE-Support-Staff-High-School.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/FTE-Support-Staff-High-School.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Support Staff in High Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Support Staff in Middle Schools",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on full-time equivalent support staff, and schools with support staff, by type of staff and for all states. Each file contains one spreadsheet for elementary, middle, or high schools.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/FTE-Support-Staff-Middle-School.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/FTE-Support-Staff-Middle-School.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Support Staff in Middle Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Support Staff in Elementary Schools",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on full-time equivalent support staff, and schools with support staff, by type of staff and for all states. Each file contains one spreadsheet for elementary, middle, or high schools.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/FTE-Support-Staff-Elementary-School.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/FTE-Support-Staff-Elementary-School.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Support Staff in Elementary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Teacher Retention",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. These Excel files contain data on classroom teachers, including full-time equivalency counts, certification, years of experience, and retention for all states. Each file contains one spreadsheet for total teachers.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Teacher-Retention.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Teacher-Retention.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Teacher Retention"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Classroom Teachers",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. These Excel files contain data on classroom teachers, including full-time equivalency counts, certification, years of experience, and retention for all states. Each file contains one spreadsheet for total teachers.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Teacher-Certification-and-Years-of-Experience.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Teacher-Certification-and-Years-of-Experience.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Classroom Teachers"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Classroom Teachers",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. These Excel files contain data on classroom teachers, including full-time equivalency counts, certification, years of experience, and retention for all states. As well as full-time equivalent support staff, and schools with support staff, by type of staff and for all states. Each file contains one spreadsheet for elementary, middle, or high schools, contains one spreadsheet for total teachers.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Teacher-Certification-and-Years-of-Experience.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Teacher-Certification-and-Years-of-Experience.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Classroom Teachers"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Teacher Retention",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. These Excel files contain data on classroom teachers, including full-time equivalency counts, certification, years of experience, and retention for all states. Each file contains one spreadsheet for total teachers.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Teacher-Retention.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Teacher-Retention.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Teacher Retention"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Classroom Teachers",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. These Excel files contain data on classroom teachers, including full-time equivalency counts, certification, years of experience, and retention for all states. Each file contains one spreadsheet for total teachers.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Teacher-Certification-and-Years-of-Experience.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Teacher-Certification-and-Years-of-Experience.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Classroom Teachers"
                 }
             ],
+            "identifier": "d85d57b7-7c5c-479d-bd0e-3b4c18158e48",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -4053,21 +4035,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:30.612602",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 Arrests Civil Rights Data Collection",
-            "description": "This set of Excel file contains data on student referrals to law enforcement by disability and student-related arrests by disability for all states. It also contains data on incidents of offenses by type of offense for all states.",
-            "modified": "2024-10-23T14:45:28.401715",
-            "accessLevel": "public",
-            "identifier": "65519d17-b971-47da-ac4d-d7047087d82e",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -4084,69 +4057,79 @@
                     }
                 }
             },
+            "title": "2015-16 Classroom Teachers Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "This set of Excel file contains data on student referrals to law enforcement by disability and student-related arrests by disability for all states. It also contains data on incidents of offenses by type of offense for all states.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Offenses",
                     "description": "This Excel file contains data on incidents of offenses by type of offense for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Offenses/Offenses.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Offenses/Offenses.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Offenses"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "School-Related Arrests without disability",
                     "description": "This Excel file contains data on student-related arrests by disability for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/School-Related-Arrest/School-Related-Arrest_by-no-disability.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/School-Related-Arrest/School-Related-Arrest_by-no-disability.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "School-Related Arrests without disability"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "School-Related Arrests with and without disability",
                     "description": "This Excel file contains data on student-related arrests by disability for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/School-Related-Arrest/School-Related-Arrest_by-disability-and-no.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/School-Related-Arrest/School-Related-Arrest_by-disability-and-no.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "School-Related Arrests with and without disability"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "School-Related Arrests by disability",
                     "description": "This Excel file contains data on student-related arrests by disability for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/School-Related-Arrest/School-Related-Arrest_by-disability.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/School-Related-Arrest/School-Related-Arrest_by-disability.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "School-Related Arrests by disability"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Referred to Law Enforcement without disability",
                     "description": "This Excel file contains data on student referrals to law enforcement by disability for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/Referred-to-Law-Enforcement/Referred-to-Law-Enforcement_by-no-disability.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/Referred-to-Law-Enforcement/Referred-to-Law-Enforcement_by-no-disability.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Referred to Law Enforcement without disability"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Referred to Law Enforcement with and without disability",
                     "description": "This Excel file contains data on student referrals to law enforcement by disability for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/Referred-to-Law-Enforcement/Referred-to-Law-Enforcement_by-disability-and-no.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/Referred-to-Law-Enforcement/Referred-to-Law-Enforcement_by-disability-and-no.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Referred to Law Enforcement with and without disability"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Referred to Law Enforcement by disability",
                     "description": "This Excel file contains data on student referrals to law enforcement by disability for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/Referred-to-Law-Enforcement/Referred-to-Law-Enforcement_by-disability.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Arrests/Referred-to-Law-Enforcement/Referred-to-Law-Enforcement_by-disability.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Referred to Law Enforcement by disability"
                 }
             ],
+            "identifier": "65519d17-b971-47da-ac4d-d7047087d82e",
             "keyword": [
                 "Elementary-and-secondary",
                 "Language",
@@ -4163,22 +4146,11 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:28.401715",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Harassment or Bullying by Basis Category",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by harassment or bullying basis category and by whether students were reported as harassed or bullied or disciplined for harassment and bullying. For each set, there are three spreadsheets: total students, male students, and female students. This Excel file contains data for all states on the number of students that were alleged to be harassed or bullied. The spreadsheet contains data on the total number of allegations of harassment or bullying, and on allegations of harassment or bullying on the basis of sex, race, and disability.",
-            "modified": "2024-10-23T14:45:27.288225",
-            "accessLevel": "public",
-            "identifier": "b72baf8e-b88c-4af2-bf0b-56051476cf55",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -4195,69 +4167,79 @@
                     }
                 }
             },
+            "title": "2017-18 Arrests Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by harassment or bullying basis category and by whether students were reported as harassed or bullied or disciplined for harassment and bullying. For each set, there are three spreadsheets: total students, male students, and female students. This Excel file contains data for all states on the number of students that were alleged to be harassed or bullied. The spreadsheet contains data on the total number of allegations of harassment or bullying, and on allegations of harassment or bullying on the basis of sex, race, and disability.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Allegations of Harassment or Bullying",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by harassment or bullying basis category and by whether students were reported as harassed or bullied or disciplined for harassment and bullying. For each set, there are three spreadsheets: total students, male students, and female students. This Excel file contains data for all states on the number of students that were alleged to be harassed or bullied. The spreadsheet contains data on the total number of allegations of harassment or bullying, and on allegations of harassment or bullying on the basis of sex, race, and disability.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Allegations-of-Harassment-or-Bullying.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Allegations-of-Harassment-or-Bullying.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Allegations of Harassment or Bullying"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Disability - Disciplined",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by harassment or bullying basis category and by whether students were reported as harassed or bullied or disciplined for harassment and bullying. For each set, there are three spreadsheets: total students, male students, and female students. This Excel file contains data for all states on the number of students that were alleged to be harassed or bullied. The spreadsheet contains data on the total number of allegations of harassment or bullying, and on allegations of harassment or bullying on the basis of sex, race, and disability.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-disability-disciplined.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-disability-disciplined.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Disability - Disciplined"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Disability - Reported",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by harassment or bullying basis category and by whether students were reported as harassed or bullied or disciplined for harassment and bullying. For each set, there are three spreadsheets: total students, male students, and female students. This Excel file contains data for all states on the number of students that were alleged to be harassed or bullied. The spreadsheet contains data on the total number of allegations of harassment or bullying, and on allegations of harassment or bullying on the basis of sex, race, and disability.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-disability-reported.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-disability-reported.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Disability - Reported"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Race - Disciplined",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by harassment or bullying basis category and by whether students were reported as harassed or bullied or disciplined for harassment and bullying. For each set, there are three spreadsheets: total students, male students, and female students. This Excel file contains data for all states on the number of students that were alleged to be harassed or bullied. The spreadsheet contains data on the total number of allegations of harassment or bullying, and on allegations of harassment or bullying on the basis of sex, race, and disability.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-race-disciplined.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-race-disciplined.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Race - Disciplined"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Race - Reported",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by harassment or bullying basis category and by whether students were reported as harassed or bullied or disciplined for harassment and bullying. For each set, there are three spreadsheets: total students, male students, and female students. This Excel file contains data for all states on the number of students that were alleged to be harassed or bullied. The spreadsheet contains data on the total number of allegations of harassment or bullying, and on allegations of harassment or bullying on the basis of sex, race, and disability.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-race-reported.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-race-reported.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Race - Reported"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Sex - Disciplined",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by harassment or bullying basis category and by whether students were reported as harassed or bullied or disciplined for harassment and bullying. For each set, there are three spreadsheets: total students, male students, and female students. This Excel file contains data for all states on the number of students that were alleged to be harassed or bullied. The spreadsheet contains data on the total number of allegations of harassment or bullying, and on allegations of harassment or bullying on the basis of sex, race, and disability.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-sex-disciplined.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-sex-disciplined.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Sex - Disciplined"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Sex - Reported",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by harassment or bullying basis category and by whether students were reported as harassed or bullied or disciplined for harassment and bullying. For each set, there are three spreadsheets: total students, male students, and female students. This Excel file contains data for all states on the number of students that were alleged to be harassed or bullied. The spreadsheet contains data on the total number of allegations of harassment or bullying, and on allegations of harassment or bullying on the basis of sex, race, and disability.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-sex-reported.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Harassment-Bullying-on-basis-of-sex-reported.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Sex - Reported"
                 }
             ],
+            "identifier": "b72baf8e-b88c-4af2-bf0b-56051476cf55",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -4275,22 +4257,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:27.288225",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 Harassment or Bullying by Basis Category Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students. The Excel file contains data on allegations of harassment or bullying by type of allegations for all states.",
-            "modified": "2024-10-23T14:45:25.469196",
-            "accessLevel": "public",
-            "identifier": "a6312d29-ef5b-4df4-97ea-5da38ce36a7f",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -4307,69 +4279,79 @@
                     }
                 }
             },
+            "title": "2013-14 Harassment or Bullying by Basis Category"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students. The Excel file contains data on allegations of harassment or bullying by type of allegations for all states.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Allegations of Harassment or Bullying",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students. The Excel file contains data on allegations of harassment or bullying by type of allegations for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Allegations-of-Harassment-or-Bullying.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Allegations-of-Harassment-or-Bullying.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Allegations of Harassment or Bullying"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Disability - Disciplined",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students. The Excel file contains data on allegations of harassment or bullying by type of allegations for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-disability-disciplined.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-disability-disciplined.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Disability - Disciplined"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Race - Disciplined",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students. The Excel file contains data on allegations of harassment or bullying by type of allegations for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-race-disciplined.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-race-disciplined.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Race - Disciplined"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Sex - Disciplined",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students. The Excel file contains data on allegations of harassment or bullying by type of allegations for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-sex-disciplined.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-sex-disciplined.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Sex - Disciplined"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Disability - Reported",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students. The Excel file contains data on allegations of harassment or bullying by type of allegations for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-disability-reported.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-disability-reported.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Disability - Reported"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Race - Reported",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students. The Excel file contains data on allegations of harassment or bullying by type of allegations for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-race-reported.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-race-reported.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Race - Reported"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On Basis of Sex - Reported",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students. The Excel file contains data on allegations of harassment or bullying by type of allegations for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-sex-reported.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Harassment-Bullying-on-basis-of-sex-reported.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On Basis of Sex - Reported"
                 }
             ],
+            "identifier": "a6312d29-ef5b-4df4-97ea-5da38ce36a7f",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -4383,21 +4365,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:25.469196",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 Harassment or Bullying Civil Rights Data Collection",
-            "description": "This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:45:22.979766",
-            "accessLevel": "public",
-            "identifier": "c1816abc-d633-4fbd-aa48-b8998f9e9f66",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -4414,61 +4387,71 @@
                     }
                 }
             },
+            "title": "2015-16 Harassment or Bullying by Basis Category Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On basis of disability - disciplined",
                     "description": "This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-disability_discplined.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-disability_discplined.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On basis of disability - disciplined"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On basis of disability - reported",
                     "description": "This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-disability_reported.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-disability_reported.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On basis of disability - reported"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On basis of race - disciplined",
                     "description": "This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-race_disciplined.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-race_disciplined.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On basis of race - disciplined"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On basis of race - reported",
                     "description": "This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-race_reported.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-race_reported.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On basis of race - reported"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On basis of sex - disciplined",
                     "description": "This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-sex_disciplined.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-sex_disciplined.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On basis of sex - disciplined"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "On basis of sex - reported",
                     "description": "This set of Excel files contains data on students reported as harassed or bullied or disciplined for harassment or bullying on the basis of sex, race, or disability category for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-sex_reported.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Climate/Harassment-or-Bullying/Harassment-Bullying-on-basis-of-sex_reported.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "On basis of sex - reported"
                 }
             ],
+            "identifier": "c1816abc-d633-4fbd-aa48-b8998f9e9f66",
             "keyword": [
                 "Elementary-and-secondary",
                 "Language",
@@ -4481,22 +4464,11 @@
                 "race",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:22.979766",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 Preschool Discipline Civil Rights Data Collection",
-            "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-            "modified": "2024-10-23T14:45:21.486790",
-            "accessLevel": "public",
-            "identifier": "3295e11c-7591-433c-94b5-b9e6c214e4d7",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -4513,61 +4485,71 @@
                     }
                 }
             },
+            "title": "2017-18 Harassment or Bullying Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Incidents of Preschool corporal punishment and suspension",
                     "description": "This Excel file contains data on incidents of preschool corporal punishment and preschool out-of-school suspension for all states.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-Discipline.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-Discipline.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Incidents of Preschool corporal punishment and suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool one or more out-of-school suspensions",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-One-or-More-Out-of-School-Suspensions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-One-or-More-Out-of-School-Suspensions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool one or more out-of-school suspensions"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool one out-of-school suspension",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-One-Out-of-School-Suspension.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-One-Out-of-School-Suspension.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool one out-of-school suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool expulsions",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-Expulsions.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-Expulsions.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool expulsions"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool more than one out-of-school suspension",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-More-than-One-Out-of-School-Suspension.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-More-than-One-Out-of-School-Suspension.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool more than one out-of-school suspension"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool corporal punishment",
                     "description": "This set of Excel files contains data for all states, presented by discipline type. For each discipline type, there are three spreadsheets: total preschool students, male preschool students, and female preschool students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-Corporal-Punishment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Discipline/Discipline/Preschool-Corporal-Punishment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool corporal punishment"
                 }
             ],
+            "identifier": "3295e11c-7591-433c-94b5-b9e6c214e4d7",
             "isPartOf": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "keyword": [
                 "Elementary-and-secondary",
@@ -4584,22 +4566,12 @@
                 "race",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 Student Enrollment Civil Rights Data Collection",
-            "description": "This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English language learners. For each category, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:45:10.475550",
-            "accessLevel": "public",
-            "identifier": "5564f622-17a2-4423-a9bf-8e3fbd2a285a",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:21.486790",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -4616,53 +4588,63 @@
                     }
                 }
             },
+            "title": "2017-18 Preschool Discipline Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English language learners. For each category, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool Enrollment",
                     "description": "This Excel file contains preschool enrollment data for all states. The file contains three spreadsheets: total children, male children, and female children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Enrollment/Preschool-Enrollment/Preschool-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Enrollment/Preschool-Enrollment/Preschool-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool Enrollment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Enrollment-Limited-English-Proficient.xlsx",
                     "description": "Enrollment of students who are English language learners",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Enrollment/All-Enrollment/Enrollment-Limited-English-Proficient.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Enrollment/All-Enrollment/Enrollment-Limited-English-Proficient.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Enrollment-Limited-English-Proficient.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Enrollment-Section-504-only.xlsx",
                     "description": "Enrollment of students served under Section 504",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Enrollment/All-Enrollment/Enrollment-Section-504-only.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Enrollment/All-Enrollment/Enrollment-Section-504-only.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Enrollment-Section-504-only.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Enrollment-IDEA.xlsx",
                     "description": "Enrollment of students served under IDEA",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Enrollment/All-Enrollment/Enrollment-IDEA.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Enrollment/All-Enrollment/Enrollment-IDEA.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Enrollment-IDEA.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Enrollment-Overall.xlsx",
                     "description": "Overall Enrollment",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Enrollment/All-Enrollment/Enrollment-Overall.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Student-Enrollment/All-Enrollment/Enrollment-Overall.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Enrollment-Overall.xlsx"
                 }
             ],
+            "identifier": "5564f622-17a2-4423-a9bf-8e3fbd2a285a",
             "isPartOf": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "keyword": [
                 "Elementary-and-secondary",
@@ -4676,22 +4658,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:10.475550",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Restraint and Seclusion Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by restraint or seclusion category. For each category, there are nine spreadsheets: students with and without disabilities, male students with and without disabilities, female students with and without disabilities, students served under IDEA, male students served under IDEA, female students served under IDEA, students not served under IDEA, male students not served under IDEA, and female students not served under IDEA. This set of Excel files contains data for all states, on the number of instances of restraint or seclusion. There are three spreadsheets: for students served under IDEA, for non-IDEA students, and for total.",
-            "modified": "2024-10-23T14:45:09.349115",
-            "accessLevel": "public",
-            "identifier": "b3aed61d-0abb-4b34-8244-70234f07c0e7",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -4708,45 +4680,55 @@
                     }
                 }
             },
+            "title": "2017-18 Student Enrollment Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by restraint or seclusion category. For each category, there are nine spreadsheets: students with and without disabilities, male students with and without disabilities, female students with and without disabilities, students served under IDEA, male students served under IDEA, female students served under IDEA, students not served under IDEA, male students not served under IDEA, and female students not served under IDEA. This set of Excel files contains data for all states, on the number of instances of restraint or seclusion. There are three spreadsheets: for students served under IDEA, for non-IDEA students, and for total.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Instances of Restraint or Seclusion",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by restraint or seclusion category. For each category, there are nine spreadsheets: students with and without disabilities, male students with and without disabilities, female students with and without disabilities, students served under IDEA, male students served under IDEA, female students served under IDEA, students not served under IDEA, male students not served under IDEA, and female students not served under IDEA. This set of Excel files contains data for all states, on the number of instances of restraint or seclusion. There are three spreadsheets: for students served under IDEA, for non-IDEA students, and for total.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Instances-of-Restraint-or-Seclusion-by-IDEA-Status.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Instances-of-Restraint-or-Seclusion-by-IDEA-Status.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Instances of Restraint or Seclusion"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Seclusion",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by restraint or seclusion category. For each category, there are nine spreadsheets: students with and without disabilities, male students with and without disabilities, female students with and without disabilities, students served under IDEA, male students served under IDEA, female students served under IDEA, students not served under IDEA, male students not served under IDEA, and female students not served under IDEA. This set of Excel files contains data for all states, on the number of instances of restraint or seclusion. There are three spreadsheets: for students served under IDEA, for non-IDEA students, and for total.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Seclusion.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Seclusion.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Seclusion"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Physical Restraint",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by restraint or seclusion category. For each category, there are nine spreadsheets: students with and without disabilities, male students with and without disabilities, female students with and without disabilities, students served under IDEA, male students served under IDEA, female students served under IDEA, students not served under IDEA, male students not served under IDEA, and female students not served under IDEA. This set of Excel files contains data for all states, on the number of instances of restraint or seclusion. There are three spreadsheets: for students served under IDEA, for non-IDEA students, and for total.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Physical-Restraint.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Physical-Restraint.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Physical Restraint"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Mechanical Restraint",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states, presented by restraint or seclusion category. For each category, there are nine spreadsheets: students with and without disabilities, male students with and without disabilities, female students with and without disabilities, students served under IDEA, male students served under IDEA, female students served under IDEA, students not served under IDEA, male students not served under IDEA, and female students not served under IDEA. This set of Excel files contains data for all states, on the number of instances of restraint or seclusion. There are three spreadsheets: for students served under IDEA, for non-IDEA students, and for total.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Mechanical-Restraint.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Mechanical-Restraint.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mechanical Restraint"
                 }
             ],
+            "identifier": "b3aed61d-0abb-4b34-8244-70234f07c0e7",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -4760,22 +4742,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Advanced Placement Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains student enrollment in Advanced Placement subjects for all states, and for each AP subject, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:45:07.960177",
-            "accessLevel": "public",
-            "identifier": "7ed37a79-ccf4-4779-8c8d-67c256393d5f",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:09.349115",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -4792,45 +4764,55 @@
                     }
                 }
             },
+            "title": "2013-14 Restraint and Seclusion Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains student enrollment in Advanced Placement subjects for all states, and for each AP subject, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "AP Other Subjects",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains student enrollment in Advanced Placement subjects for all states, and for each AP subject, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Other-Subjects-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Other-Subjects-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AP Other Subjects"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "AP Science",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains student enrollment in Advanced Placement subjects for all states, and for each AP subject, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Science-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Science-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AP Science"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "AP Mathematics",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains student enrollment in Advanced Placement subjects for all states, and for each AP subject, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Mathematics-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Mathematics-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AP Mathematics"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Advanced Placement Total Enrollment",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains student enrollment in Advanced Placement subjects for all states, and for each AP subject, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Advanced Placement Total Enrollment"
                 }
             ],
+            "identifier": "7ed37a79-ccf4-4779-8c8d-67c256393d5f",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -4844,22 +4826,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Enrollment Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English learners (EL). For each category, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:45:07.513492",
-            "accessLevel": "public",
-            "identifier": "5ae0f10c-6480-4835-a124-f439b0ee6183",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:07.960177",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -4876,45 +4848,55 @@
                     }
                 }
             },
+            "title": "2013-14 Advanced Placement Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English learners (EL). For each category, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "EL Enrollment",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English learners (EL). For each category, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/SCH-0009-Limited-English-Proficient-Students-by-state.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/SCH-0009-Limited-English-Proficient-Students-by-state.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EL Enrollment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Section 504 Enrollment",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English learners (EL). For each category, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/SCH-0102-Enrollment-of-Students-with-Disabilities-Served-under-Section-504-only.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/SCH-0102-Enrollment-of-Students-with-Disabilities-Served-under-Section-504-only.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Section 504 Enrollment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "IDEA Enrollment",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English learners (EL). For each category, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/SCH-0101-Enrollment-of-Students-with-Disabilities-Served-under-IDEA.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/SCH-0101-Enrollment-of-Students-with-Disabilities-Served-under-IDEA.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "IDEA Enrollment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Enrollment",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English learners (EL). For each category, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/SCH-0005-Overall-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/SCH-0005-Overall-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Enrollment"
                 }
             ],
+            "identifier": "5ae0f10c-6480-4835-a124-f439b0ee6183",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -4928,22 +4910,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:07.513492",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 Restraint and Seclusion Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on incidents of offenses by type of offense, to include uses of:  mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-            "modified": "2024-10-23T14:45:06.850978",
-            "accessLevel": "public",
-            "identifier": "a49fe791-881d-4756-90b1-0e8ea118222a",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -4960,45 +4932,55 @@
                     }
                 }
             },
+            "title": "2013-14 Enrollment Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on incidents of offenses by type of offense, to include uses of:  mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Offenses",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on incidents of offenses by type of offense, to include uses of:  mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Offenses.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Offenses.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Offenses"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Seclusion",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on incidents of offenses by type of offense, to include uses of:  mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Seclusion.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Seclusion.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Seclusion"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Physical Restraint",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on incidents of offenses by type of offense, to include uses of:  mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Physical-Restraint.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Physical-Restraint.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Physical Restraint"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Mechanical Restraint",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on incidents of offenses by type of offense, to include uses of:  mechanical restraint, physical restraint, and seclusion data on students for all states. Each file contains nine spreadsheets: total students served under IDEA and not served under IDEA; male students served under IDEA and not served under IDEA; female students served under IDEA and not served under IDEA; total students served under IDEA; male students served under IDEA; female students served under IDEA; total students not served under IDEA; male students not served under IDEA; and female students not served under IDEA.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Mechanical-Restraint.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Mechanical-Restraint.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Mechanical Restraint"
                 }
             ],
+            "identifier": "a49fe791-881d-4756-90b1-0e8ea118222a",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5012,22 +4994,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 Advanced Placement Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This Excel file contains student enrollment in Advanced Placement for all states. There are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:45:04.037487",
-            "accessLevel": "public",
-            "identifier": "328ebced-5728-44b7-916f-d4fa876a1bc6",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:06.850978",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5044,45 +5016,55 @@
                     }
                 }
             },
+            "title": "2015-16 Restraint and Seclusion Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This Excel file contains student enrollment in Advanced Placement for all states. There are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "AP other subjects",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by Advanced Placement (AP) subject. For each AP subject, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Other-Subjects-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Other-Subjects-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AP other subjects"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "AP Science",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by Advanced Placement (AP) subject. For each AP subject, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Science-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Science-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AP Science"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "AP Mathematics",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains student enrollment data for all states, presented by Advanced Placement (AP) subject. For each AP subject, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Mathematics-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Mathematics-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AP Mathematics"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Advanced Placement Total Enrollment",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This Excel file contains student enrollment in Advanced Placement for all states. There are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Advanced Placement Total Enrollment"
                 }
             ],
+            "identifier": "328ebced-5728-44b7-916f-d4fa876a1bc6",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5097,22 +5079,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 Pathways to College and Career Readiness Civil Rights Data Collection",
-            "description": "This Excel file contains preschool enrollment data, gifted and talented program enrollment data, and English language learners enrolled in English language instruction educational programs for all states. It also contains data on chronic student absenteeism - students absent 15 or more days during the school year - for all states. The files contains three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:45:02.661890",
-            "accessLevel": "public",
-            "identifier": "a918a93f-4da6-44a7-9bd0-4c4f96c371d4",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:04.037487",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5129,45 +5101,55 @@
                     }
                 }
             },
+            "title": "2015-16 Advanced Placement Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "This Excel file contains preschool enrollment data, gifted and talented program enrollment data, and English language learners enrolled in English language instruction educational programs for all states. It also contains data on chronic student absenteeism - students absent 15 or more days during the school year - for all states. The files contains three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Student Absenteeism",
                     "description": "This Excel file contains data on chronic student absenteeism - students absent 15 or more days during the school year - for all states. The file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Chronic-Absenteeism.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Chronic-Absenteeism.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Student Absenteeism"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Gifted and Talented",
                     "description": "This Excel file contains data on students enrolled in gifted and talented programs for all states. The file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Gifted-Talented-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Gifted-Talented-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Gifted and Talented"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "English Language Instruction Educational Programs",
                     "description": "This Excel file contains data for English language learners enrolled in English language instruction educational programs for all states. The file contains three spreadsheets: total children, male children, and female children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/English-Language-Instruction-Programs.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/English-Language-Instruction-Programs.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "English Language Instruction Educational Programs"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Preschool Enrollment",
                     "description": "This Excel file contains preschool enrollment data for all states. The file contains three spreadsheets: total children, male children, and female children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Preschool-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Preschool Enrollment"
                 }
             ],
+            "identifier": "a918a93f-4da6-44a7-9bd0-4c4f96c371d4",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5184,22 +5166,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 Student Enrollment Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English language learners. For each category, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:45:00.851696",
-            "accessLevel": "public",
-            "identifier": "01537748-76b4-4e40-a780-e91abadc080e",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:02.661890",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5216,45 +5188,55 @@
                     }
                 }
             },
+            "title": "2015-16 Pathways to College and Career Readiness Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English language learners. For each category, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "ELL Enrollment",
                     "description": "This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English language learners. For each category, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-ELL.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-ELL.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ELL Enrollment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Section 504 Enrollment",
                     "description": "This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English language learners. For each category, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-Section-504-only.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-Section-504-only.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Section 504 Enrollment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "IDEA Enrollment",
                     "description": "This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English language learners. For each category, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-IDEA.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-IDEA.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "IDEA Enrollment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Enrollment",
                     "description": "This set of Excel files contains data for all states on overall enrollment, enrollment of students served under IDEA, enrollment of students served under Section 504, and enrollment of students who are English language learners. For each category, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-Overall.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Enrollment-Overall.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Enrollment"
                 }
             ],
+            "identifier": "01537748-76b4-4e40-a780-e91abadc080e",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5268,22 +5250,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:00.851696",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 Advanced Placement Courses Civil Rights Data Collection",
-            "description": "The 2017-18 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states on students enrolled in student enrollment in Advanced Placement Courses. For each category, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:45:00.109297",
-            "accessLevel": "public",
-            "identifier": "28a39c03-7fe6-4621-8ca5-6b5c0eb58bd5",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5300,45 +5272,55 @@
                     }
                 }
             },
+            "title": "2015-16 Student Enrollment Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2017-18 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states on students enrolled in student enrollment in Advanced Placement Courses. For each category, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "AP other subjects",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by Advanced Placement (AP) subject. For each AP subject, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Advanced-Placement-(courses)/Advanced-Placement-Other-Subjects-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Advanced-Placement-(courses)/Advanced-Placement-Other-Subjects-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AP other subjects"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "AP science",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by Advanced Placement (AP) subject. For each AP subject, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Advanced-Placement-(courses)/Advanced-Placement-Science-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Advanced-Placement-(courses)/Advanced-Placement-Science-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AP science"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "AP mathematics",
                     "description": "This set of Excel files contains student enrollment data for all states, presented by Advanced Placement (AP) subject. For each AP subject, there are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Advanced-Placement-(courses)/Advanced-Placement-Mathematics-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Advanced-Placement-(courses)/Advanced-Placement-Mathematics-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AP mathematics"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Advanced Placement Total Enrollment",
                     "description": "This Excel file contains student enrollment in Advanced Placement for all states. There are three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Advanced-Placement-(courses)/Advanced-Placement-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/Course-Enrollment/Advanced-Placement-(courses)/Advanced-Placement-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Advanced Placement Total Enrollment"
                 }
             ],
+            "identifier": "28a39c03-7fe6-4621-8ca5-6b5c0eb58bd5",
             "isPartOf": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5354,22 +5336,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 College Preparatory Exams Civil Rights Data Collection",
-            "description": "The 2017-18 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for Advanced Placement exam taking and SAT/ACT student participation data for all states.",
-            "modified": "2024-10-23T14:39:57.565369",
-            "accessLevel": "public",
-            "identifier": "42a4336e-d359-40a8-a9b9-39920cfa7025",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:45:00.109297",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5386,37 +5358,47 @@
                     }
                 }
             },
+            "title": "2017-18 Advanced Placement Courses Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2017-18 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for Advanced Placement exam taking and SAT/ACT student participation data for all states.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "SAT/ACT Participation",
                     "description": "This Excel file contains SAT/ACT student participation data for all states. The file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/College-Prepatory-Exams/SAT-ACT/SAT-or-ACT-Participation-by-state.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/College-Prepatory-Exams/SAT-ACT/SAT-or-ACT-Participation-by-state.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SAT/ACT Participation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Took AP Exam",
                     "description": "This set of Excel files contains data on Advanced Placement exam taking for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/College-Prepatory-Exams/Advanced-Placement-Exams/Advanced-Placement-Participation-by-state_Took-Exam.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/College-Prepatory-Exams/Advanced-Placement-Exams/Advanced-Placement-Participation-by-state_Took-Exam.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Took AP Exam"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Did not take AP Exam",
                     "description": "This set of Excel files contains data on Advanced Placement exam taking for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/College-Prepatory-Exams/Advanced-Placement-Exams/Advanced-Placement-Participation-by-state_Did-Not-Take-Exam.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/College-Prepatory-Exams/Advanced-Placement-Exams/Advanced-Placement-Participation-by-state_Did-Not-Take-Exam.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Did not take AP Exam"
                 }
             ],
+            "identifier": "42a4336e-d359-40a8-a9b9-39920cfa7025",
             "isPartOf": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5433,22 +5415,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 School Programs Civil Rights Data Collection",
-            "description": "The 2017-18 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states on students enrolled in English language instruction educational programs, gifted and talented programs, and International Baccalaureate (IB) programs.  For each category, there are three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:39:56.258483",
-            "accessLevel": "public",
-            "identifier": "846dfb7a-90a6-4887-8ad5-5088f3bd5727",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:39:57.565369",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5465,37 +5437,47 @@
                     }
                 }
             },
+            "title": "2017-18 College Preparatory Exams Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2017-18 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data for all states on students enrolled in English language instruction educational programs, gifted and talented programs, and International Baccalaureate (IB) programs.  For each category, there are three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "International Baccalaureate Enrollment",
                     "description": "This Excel file contains data on student enrollment in International Baccalaureate (IB) programs for all states. The file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Programs/International-Baccalaureate-(IB)/IB-Enrollment-by-state.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Programs/International-Baccalaureate-(IB)/IB-Enrollment-by-state.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "International Baccalaureate Enrollment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Gifted and Talented Enrollment",
                     "description": "This Excel file contains data on students enrolled in gifted and talented programs for all states. The file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Programs/Gifted-and-Talented/Gifted-Talented-Enrollment.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Programs/Gifted-and-Talented/Gifted-Talented-Enrollment.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Gifted and Talented Enrollment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "English Language Instruction Program Enrollment",
                     "description": "This Excel file contains data for English language learners enrolled in English language instruction educational programs for all states. The file contains three spreadsheets: total children, male children, and female children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Programs/English-Language-Instruction-Education-Programs/English-Language-Instruction-Programs.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Programs/English-Language-Instruction-Education-Programs/English-Language-Instruction-Programs.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "English Language Instruction Program Enrollment"
                 }
             ],
+            "identifier": "846dfb7a-90a6-4887-8ad5-5088f3bd5727",
             "isPartOf": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5512,22 +5494,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:39:56.258483",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Advanced Placement Test Taking Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data on Advanced Placement test taking for all states. For each set, there are three three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:36:55.599307",
-            "accessLevel": "public",
-            "identifier": "27745ee1-c1ed-458f-bfda-d9fa3aaaae40",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5544,29 +5516,39 @@
                     }
                 }
             },
+            "title": "2017-18 School Programs Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data on Advanced Placement test taking for all states. For each set, there are three three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Took AP Exam",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data on Advanced Placement test taking for all states. For each set, there are three three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Participation-by-state-Took-Exam.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Participation-by-state-Took-Exam.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Took AP Exam"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Did Not Take AP Exam",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This set of Excel files contains data on Advanced Placement test taking for all states. For each set, there are three three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Participation-by-state-Did-Not-Take-Exam.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Advanced-Placement-Participation-by-state-Did-Not-Take-Exam.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Did Not Take AP Exam"
                 }
             ],
+            "identifier": "27745ee1-c1ed-458f-bfda-d9fa3aaaae40",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5581,22 +5563,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Early Childhood and Prekindergarten Enrollment",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains early childhood and prekindergarten student enrollment data for all states. The file contains three spreadsheets: total children, male children, and female children.",
-            "modified": "2024-10-23T14:36:52.397921",
-            "accessLevel": "public",
-            "identifier": "68614a24-5d15-4c74-adbc-f67cc3f44faa",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:36:55.599307",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5613,29 +5585,39 @@
                     }
                 }
             },
+            "title": "2013-14 Advanced Placement Test Taking Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains early childhood and prekindergarten student enrollment data for all states. The file contains three spreadsheets: total children, male children, and female children.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Early Childhood and Prekindergarten Enrollment",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains early childhood and prekindergarten student enrollment data for all states. The file contains three spreadsheets: total children, male children, and female children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Total-Enrollment-in-Early-Childhood-and-Prekindergarten.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Total-Enrollment-in-Early-Childhood-and-Prekindergarten.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Early Childhood and Prekindergarten Enrollment"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Early Childhood and Prekindergarten Enrollment",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains early childhood and prekindergarten student enrollment data for all states. The file contains three spreadsheets: total children, male children, and female children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Total-Enrollment-in-Early-Childhood-and-Prekindergarten.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Total-Enrollment-in-Early-Childhood-and-Prekindergarten.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Early Childhood and Prekindergarten Enrollment"
                 }
             ],
+            "identifier": "68614a24-5d15-4c74-adbc-f67cc3f44faa",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5649,22 +5631,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:36:52.397921",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 Advanced Placement Exam Taking Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on Advanced Placement exam taking for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:36:50.316483",
-            "accessLevel": "public",
-            "identifier": "6f559334-e7ab-4cad-9e03-0dea4197b757",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5681,29 +5653,39 @@
                     }
                 }
             },
+            "title": "2013-14 Early Childhood and Prekindergarten Enrollment"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on Advanced Placement exam taking for all states. Each file contains three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Took AP Exam",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on Advanced Placement exam taking for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Participation-by-State-Took-Exam.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Participation-by-State-Took-Exam.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Took AP Exam"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Did Not Take AP Exam",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This set of Excel files contains data on Advanced Placement exam taking for all states. Each file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Participation-by-State-Did-Not-Take-Exam.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/Advanced-Placement-Participation-by-State-Did-Not-Take-Exam.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Did Not Take AP Exam"
                 }
             ],
+            "identifier": "6f559334-e7ab-4cad-9e03-0dea4197b757",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5718,22 +5700,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:36:50.316483",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2017-18 School Staff Civil Rights Data Collection",
-            "description": "These Excel files contain data on classroom teachers, including full-time equivalency counts, certification, and years of experience for all states.  Each file contains one spreadsheet for total teachers. It also contains data on full-time equivalent support staff, and schools with support staff, by type of staff and for all states. Each file contains one spreadsheet for elementary, middle, or high schools.",
-            "modified": "2024-10-23T14:36:48.959179",
-            "accessLevel": "public",
-            "identifier": "487b44c9-7303-4fab-aa61-e2f6d18901d8",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5750,29 +5722,39 @@
                     }
                 }
             },
+            "title": "2015-16 Advanced Placement Exam Taking Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "These Excel files contain data on classroom teachers, including full-time equivalency counts, certification, and years of experience for all states.  Each file contains one spreadsheet for total teachers. It also contains data on full-time equivalent support staff, and schools with support staff, by type of staff and for all states. Each file contains one spreadsheet for elementary, middle, or high schools.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Counselors High School",
                     "description": "This set of Excel files contains data on full-time equivalent support staff, and schools with support staff, by type of staff and for all states. Each file contains one spreadsheet for elementary, middle, or high schools.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Staff/School-Support-Staff/Counselors_High-School.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Staff/School-Support-Staff/Counselors_High-School.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Counselors High School"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Teacher Certification and Years of Experience",
                     "description": "These Excel files contain data on classroom teachers, including full-time equivalency counts, certification, and years of experience for all states. Each file contains one spreadsheet for total teachers.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Staff/Classroom-Teachers/Teacher-Certification-and-Years-of-Experience.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2017-2018/School-Staff/Classroom-Teachers/Teacher-Certification-and-Years-of-Experience.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Teacher Certification and Years of Experience"
                 }
             ],
+            "identifier": "487b44c9-7303-4fab-aa61-e2f6d18901d8",
             "isPartOf": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5789,22 +5771,12 @@
                 "support-staff",
                 "teachers"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2017-2018",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:36:48.959179",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Classroom Teachers Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on classroom teachers, including full-time equivalency counts, certification, and years of experience for all states. The file contains one spreadsheet for total classroom teachers.",
-            "modified": "2024-10-23T14:32:57.526207",
-            "accessLevel": "public",
-            "identifier": "9c3e8cd6-e7cb-4213-be71-d130e59b7813",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5821,21 +5793,31 @@
                     }
                 }
             },
+            "title": "2017-18 School Staff Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on classroom teachers, including full-time equivalency counts, certification, and years of experience for all states. The file contains one spreadsheet for total classroom teachers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Classroom Teachers",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on classroom teachers, including full-time equivalency counts, certification, and years of experience for all states. The file contains one spreadsheet for total classroom teachers.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Teacher-Certification-and-Years-of-Experience.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Teacher-Certification-and-Years-of-Experience.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Classroom Teachers"
                 }
             ],
+            "identifier": "9c3e8cd6-e7cb-4213-be71-d130e59b7813",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5850,22 +5832,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 School Counselors Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on high school counselors for all states. The file contains one spreadsheet for total high school counselors.",
-            "modified": "2024-10-23T14:32:56.803312",
-            "accessLevel": "public",
-            "identifier": "0ce577bd-9430-4cb1-9875-7fa5cb8a34f3",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:32:57.526207",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5882,21 +5854,31 @@
                     }
                 }
             },
+            "title": "2013-14 Classroom Teachers Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on high school counselors for all states. The file contains one spreadsheet for total high school counselors.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "School Counselors",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on high school counselors for all states. The file contains one spreadsheet for total high school counselors.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/School-Counselors.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/School-Counselors.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "School Counselors"
                 }
             ],
+            "identifier": "0ce577bd-9430-4cb1-9875-7fa5cb8a34f3",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5910,22 +5892,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 SAT/ACT Participation Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains SAT/ACT student participation data for all states. The file contains three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:32:55.398618",
-            "accessLevel": "public",
-            "identifier": "347ebe5f-c4bc-4198-abbe-5283cad7e45e",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:32:56.803312",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -5942,21 +5914,31 @@
                     }
                 }
             },
+            "title": "2013-14 School Counselors Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains SAT/ACT student participation data for all states. The file contains three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "SAT/ACT Participation",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains SAT/ACT student participation data for all states. The file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/SAT-or-ACT-Participation-by-state.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/SAT-or-ACT-Participation-by-state.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SAT/ACT Participation"
                 }
             ],
+            "identifier": "347ebe5f-c4bc-4198-abbe-5283cad7e45e",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -5970,22 +5952,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 Student Absenteeism Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on chronic student absenteeism - students absent 15 or more days during the school year - for all states. The file contains three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:32:55.103112",
-            "accessLevel": "public",
-            "identifier": "40721303-4cbf-4311-b165-0564645de3a9",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:32:55.398618",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -6002,21 +5974,31 @@
                     }
                 }
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CRDC Team",
-                "hasEmail": "mailto:ocrdata@ed.gov"
+            "title": "2013-14 SAT/ACT Participation Civil Rights Data Collection"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CRDC Team",
+                "hasEmail": "mailto:ocrdata@ed.gov"
+            },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on chronic student absenteeism - students absent 15 or more days during the school year - for all states. The file contains three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Student Absenteeism",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data on chronic student absenteeism - students absent 15 or more days during the school year - for all states. The file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Chronic-Absenteeism.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/Chronic-Absenteeism.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Student Absenteeism"
                 }
             ],
+            "identifier": "40721303-4cbf-4311-b165-0564645de3a9",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -6030,22 +6012,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2013-14 English Language Instruction Educational Program Enrollment Civil Rights Data Collection",
-            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for English language learners enrolled in English language instruction educational programs for all states. The file contains three spreadsheets: total children, male children, and female children.",
-            "modified": "2024-10-23T14:31:33.569179",
-            "accessLevel": "public",
-            "identifier": "dd8f43a4-d227-4273-9fbf-f79a2d80acb8",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:32:55.103112",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -6062,21 +6034,31 @@
                     }
                 }
             },
+            "title": "2013-14 Student Absenteeism Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for English language learners enrolled in English language instruction educational programs for all states. The file contains three spreadsheets: total children, male children, and female children.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "English Language Instruction Educational Programs",
                     "description": "The 2013-14 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 16,500 school districts and 96,500 schools. This Excel file contains data for English language learners enrolled in English language instruction educational programs for all states. The file contains three spreadsheets: total children, male children, and female children.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/English-Language-Instruction-Programs-all-states.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2013-2014/English-Language-Instruction-Programs-all-states.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "English Language Instruction Educational Programs"
                 }
             ],
+            "identifier": "dd8f43a4-d227-4273-9fbf-f79a2d80acb8",
             "isPartOf": "15db19ce-5157-422d-9750-d2555a1cd804",
             "keyword": [
                 "Elementary-and-secondary",
@@ -6090,22 +6072,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2013-2014",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:31:33.569179",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 SAT/ACT Participation Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This Excel file contains SAT/ACT student participation data for all states. The file contains three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:31:10.056782",
-            "accessLevel": "public",
-            "identifier": "32a95beb-3246-43fd-a10e-b1fe09bd0273",
-            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -6122,21 +6094,31 @@
                     }
                 }
             },
+            "title": "2013-14 English Language Instruction Educational Program Enrollment Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This Excel file contains SAT/ACT student participation data for all states. The file contains three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "SAT/ACT Participation",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This Excel file contains SAT/ACT student participation data for all states. The file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/SAT-or-ACT-Participation-by-State.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/SAT-or-ACT-Participation-by-State.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SAT/ACT Participation"
                 }
             ],
+            "identifier": "32a95beb-3246-43fd-a10e-b1fe09bd0273",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -6150,22 +6132,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "2015-16 International Baccalaureate Enrollment Civil Rights Data Collection",
-            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This Excel file contains data on student enrollment in International Baccalaureate (IB) programs for all states. The file contains three spreadsheets: total students, male students, and female students.",
-            "modified": "2024-10-23T14:31:08.925823",
-            "accessLevel": "public",
-            "identifier": "deebda4e-8c48-49ef-9c70-2ded43e006e6",
             "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
             "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:31:10.056782",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -6182,21 +6154,31 @@
                     }
                 }
             },
+            "title": "2015-16 SAT/ACT Participation Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This Excel file contains data on student enrollment in International Baccalaureate (IB) programs for all states. The file contains three spreadsheets: total students, male students, and female students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "IB Enrolment",
                     "description": "The 2015-16 tables are based on data collected from all of the nation\u2019s school districts and schools\u2014approximately 17,300 school districts and 96,300 schools. This Excel file contains data on student enrollment in International Baccalaureate (IB) programs for all states. The file contains three spreadsheets: total students, male students, and female students.",
-                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/IB-Enrollment-by-State.xlsx"
+                    "downloadURL": "https://civilrightsdata.ed.gov/assets/downloads/2015-2016/IB-Enrollment-by-State.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "IB Enrolment"
                 }
             ],
+            "identifier": "deebda4e-8c48-49ef-9c70-2ded43e006e6",
             "isPartOf": "286204af-4841-4d1b-bd38-06ef167becfc",
             "keyword": [
                 "Elementary-and-secondary",
@@ -6212,24 +6194,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/estimations/2015-2016",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:31:08.925823",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Civil Rights Data Collection (CRDC) for the 2015-16  school year",
-            "description": "The Civil Rights Data Collection, 2015-16 (CRDC 2015-16) is part of the Civil Rights Data Collection (CRDC) program; program data are available beginning with the 2000 collection at https://civilrightsdata.ed.gov/data. CRDC 2015-16 is a cross-sectional survey that collects data on key education and civil rights issues in the nation's public schools, which include student enrollment and educational programs and services, disaggregated by race/ethnicity, sex, limited English proficiency, and disability. LEAs submit administrative records about schools in the district. CRDC 2015-16 is a universe survey. Key statistics produced from CRDC 2015-16 can provide information about critical civil rights issues as well as contextual information on the state of civil rights in the nation, including enrollment demographics, advanced placement, school discipline, and special education services.",
-            "modified": "2024-10-23T14:31:05.161484",
-            "accessLevel": "public",
-            "identifier": "286204af-4841-4d1b-bd38-06ef167becfc",
-            "describedBy": "https://civilrightsdata.ed.gov/assets/downloads/CRDC-Definitions-2015-16.pdf",
-            "describedByType": "application/pdf",
-            "landingPage": "https://civilrightsdata.ed.gov/data",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -6246,24 +6216,36 @@
                     }
                 }
             },
+            "title": "2015-16 International Baccalaureate Enrollment Civil Rights Data Collection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "describedBy": "https://civilrightsdata.ed.gov/assets/downloads/CRDC-Definitions-2015-16.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Civil Rights Data Collection, 2015-16 (CRDC 2015-16) is part of the Civil Rights Data Collection (CRDC) program; program data are available beginning with the 2000 collection at https://civilrightsdata.ed.gov/data. CRDC 2015-16 is a cross-sectional survey that collects data on key education and civil rights issues in the nation's public schools, which include student enrollment and educational programs and services, disaggregated by race/ethnicity, sex, limited English proficiency, and disability. LEAs submit administrative records about schools in the district. CRDC 2015-16 is a universe survey. Key statistics produced from CRDC 2015-16 can provide information about critical civil rights issues as well as contextual information on the state of civil rights in the nation, including enrollment demographics, advanced placement, school discipline, and special education services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2015-16-crdc-data.zip",
+                    "describedBy": "https://civilrightsdata.ed.gov/assets/downloads/CRDC-Definitions-2015-16.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A public-use data file containing the entire CRDC year-of-choice data set in CSV format can be downloaded in a zip file.",
                     "downloadURL": "https://civilrightsdata.ed.gov/assets/ocr/docs/2015-16-crdc-data.zip",
-                    "describedBy": "https://civilrightsdata.ed.gov/assets/downloads/CRDC-Definitions-2015-16.pdf",
-                    "describedByType": "application/pdf"
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2015-16-crdc-data.zip"
                 }
             ],
+            "identifier": "286204af-4841-4d1b-bd38-06ef167becfc",
             "isPartOf": "4ac6fe16-957d-4e2b-bbcb-1680c9f6939c",
             "keyword": [
                 "Elementary-and-secondary",
@@ -6277,29 +6259,12 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/data",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:31:05.161484",
             "programCode": [
                 "018:000"
             ],
-            "references": [
-                "https://civilrightsdata.ed.gov/assets/for-researchers/user-manual/Public-Use-Data-File-Manual-2015-16.pdf",
-                "https://civilrightsdata.ed.gov/assets/for-researchers/appendix/2015-16-data-notes-addendum.pdf",
-                "https://civilrightsdata.ed.gov/assets/for-researchers/data-notes/Data-Notes-CRDC-2015-16.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Civil Rights Data Collection (CRDC) for the 2017-18 school year",
-            "description": "The Civil Rights Data Collection, 2017-18 (CRDC 2017-18) is part of the Civil Rights Data Collection (CRDC) program; program data are available beginning with the 2000 collection at https://civilrightsdata.ed.gov/data. CRDC 2017-18 is a cross-sectional survey that collects data on key education and civil rights issues in the nation's public schools, which include student enrollment and educational programs and services, disaggregated by race/ethnicity, sex, limited English proficiency, and disability. LEAs submit administrative records about schools in the district. CRDC 2017-18 is a universe survey. Key statistics produced from CRDC 2017-18 can provide information about critical civil rights issues as well as contextual information on the state of civil rights in the nation, including enrollment demographics, advanced placement, school discipline, and special education services.",
-            "modified": "2024-10-23T14:31:02.368789",
-            "accessLevel": "public",
-            "identifier": "dd80845b-924e-40d3-964c-dd4875113f0a",
-            "describedBy": "https://civilrightsdata.ed.gov/assets/downloads/2017-18_Master_List_of_CRDC_Definitions.pdf",
-            "describedByType": "application/pdf",
-            "landingPage": "https://civilrightsdata.ed.gov/data",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office for Civil Rights (OCR)",
@@ -6316,23 +6281,40 @@
                     }
                 }
             },
+            "references": [
+                "https://civilrightsdata.ed.gov/assets/for-researchers/user-manual/Public-Use-Data-File-Manual-2015-16.pdf",
+                "https://civilrightsdata.ed.gov/assets/for-researchers/appendix/2015-16-data-notes-addendum.pdf",
+                "https://civilrightsdata.ed.gov/assets/for-researchers/data-notes/Data-Notes-CRDC-2015-16.pdf"
+            ],
+            "title": "Civil Rights Data Collection (CRDC) for the 2015-16  school year"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CRDC Team",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "describedBy": "https://civilrightsdata.ed.gov/assets/downloads/2017-18_Master_List_of_CRDC_Definitions.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Civil Rights Data Collection, 2017-18 (CRDC 2017-18) is part of the Civil Rights Data Collection (CRDC) program; program data are available beginning with the 2000 collection at https://civilrightsdata.ed.gov/data. CRDC 2017-18 is a cross-sectional survey that collects data on key education and civil rights issues in the nation's public schools, which include student enrollment and educational programs and services, disaggregated by race/ethnicity, sex, limited English proficiency, and disability. LEAs submit administrative records about schools in the district. CRDC 2017-18 is a universe survey. Key statistics produced from CRDC 2017-18 can provide information about critical civil rights issues as well as contextual information on the state of civil rights in the nation, including enrollment demographics, advanced placement, school discipline, and special education services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "2017-18-crdc-data.zip",
+                    "describedBy": "https://civilrightsdata.ed.gov/assets/downloads/2017-18_Master_List_of_CRDC_Definitions.pdf",
+                    "describedByType": "application/pdf",
                     "description": "A public-use data file containing the entire CRDC year-of-choice data set in CSV format can be downloaded in a zip file.",
                     "downloadURL": "https://civilrightsdata.ed.gov/assets/ocr/docs/2017-18-crdc-data.zip",
-                    "describedBy": "https://civilrightsdata.ed.gov/assets/downloads/2017-18_Master_List_of_CRDC_Definitions.pdf",
-                    "describedByType": "application/pdf"
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "2017-18-crdc-data.zip"
                 }
             ],
+            "identifier": "dd80845b-924e-40d3-964c-dd4875113f0a",
             "isPartOf": "4ac6fe16-957d-4e2b-bbcb-1680c9f6939c",
             "keyword": [
                 "Elementary-and-secondary",
@@ -6346,29 +6328,15 @@
                 "student-retention",
                 "students"
             ],
-            "bureauCode": [
-                "018:00"
-            ],
+            "landingPage": "https://civilrightsdata.ed.gov/data",
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-23T14:31:02.368789",
             "programCode": [
                 "018:000"
             ],
-            "references": [
-                "https://civilrightsdata.ed.gov/assets/for-researchers/appendix/Appendix-C-LEAs-Identified-with-Post-Submission-Data-Quality-Checks.xlsx",
-                "https://civilrightsdata.ed.gov/assets/for-researchers/data-notes/Data-Notes-CRDC-2017-18.pdf",
-                "https://civilrightsdata.ed.gov/assets/for-researchers/user-manual/2017-18%20CRDC%20Public-Use%20Data%20File%20Manual.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Title I Part A Performance, Participation, and Funding Data",
-            "description": "Performance, participation, and funding data related to Title 1, Part A. Data  from SY 2010-11 onward.",
-            "modified": "2024-10-22T14:47:32.768160",
-            "accessLevel": "public",
-            "identifier": "2c71d5c2-bae6-4fe3-92ca-57f5fdf12524",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Elementary and Secondary Education (OESE)",
+                "name": "Office for Civil Rights (OCR)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -6382,38 +6350,53 @@
                     }
                 }
             },
+            "references": [
+                "https://civilrightsdata.ed.gov/assets/for-researchers/appendix/Appendix-C-LEAs-Identified-with-Post-Submission-Data-Quality-Checks.xlsx",
+                "https://civilrightsdata.ed.gov/assets/for-researchers/data-notes/Data-Notes-CRDC-2017-18.pdf",
+                "https://civilrightsdata.ed.gov/assets/for-researchers/user-manual/2017-18%20CRDC%20Public-Use%20Data%20File%20Manual.pdf"
+            ],
+            "title": "Civil Rights Data Collection (CRDC) for the 2017-18 school year"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Elementary and Secondary Education",
                 "hasEmail": "mailto:eddataexpress@ed.gov"
             },
+            "description": "Performance, participation, and funding data related to Title 1, Part A. Data  from SY 2010-11 onward.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title 1 Part A Dashboard",
                     "description": "Dashboard presentation of performance, participation, and funding data on students in schools that receive Title I, Part A funding.  Data  from SY 2010-11 onward.",
                     "downloadURL": "https://eddataexpress.ed.gov/dashboard/title-i-part-a",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title 1 Part A Dashboard"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title I Part A Participation Data",
                     "description": "Participation data on students in schools that receive Title I, Part A funding.  Data  from SY 2010-11 onward available for download.",
                     "downloadURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3ATitle%20I%2C%20Part%20A&f%5B1%5D=type_of_data%3AParticipation",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title I Part A Participation Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title I Part A Performance Data",
                     "description": "Performance data on students in schools that receive Title I, Part A funding.  Data  from SY 2010-11 onward available for download.",
                     "downloadURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3ATitle%20I%2C%20Part%20A&f%5B1%5D=type_of_data%3APerformance",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title I Part A Performance Data"
                 }
             ],
+            "identifier": "2c71d5c2-bae6-4fe3-92ca-57f5fdf12524",
             "keyword": [
                 "district",
                 "e630b5cb-5a69-415b-a2cf-21aa81831130",
@@ -6425,21 +6408,11 @@
                 "secondary",
                 "state"
             ],
-            "bureauCode": [
-                "018:10"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-22T14:47:32.768160",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Title III (English Learners) Performance, Participation, and Funding Data",
-            "description": "Performance, participation, and funding data related to Title III. Data from SY 2010-11 onward.",
-            "modified": "2024-10-22T00:20:42.292871",
-            "accessLevel": "public",
-            "identifier": "29a551d1-1a26-4cf0-9321-d821196eceaa",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Elementary and Secondary Education (OESE)",
@@ -6456,38 +6429,48 @@
                     }
                 }
             },
+            "title": "Title I Part A Performance, Participation, and Funding Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Elementary and Secondary Education",
                 "hasEmail": "mailto:eddataexpress@ed.gov"
             },
+            "description": "Performance, participation, and funding data related to Title III. Data from SY 2010-11 onward.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title III Data Dashboard",
                     "description": "Dashboard presentation of performance, participation and funding data on English learners in Title III districts.  Data  from SY 2010-11 onward.",
                     "downloadURL": "https://eddataexpress.ed.gov/dashboard/title-iii",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title III Data Dashboard"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title III Performance Data",
                     "description": "Performance data on English learners in Title III districts.  Data  from SY 2010-11 onward available for download.",
                     "downloadURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3ATitle%20III&f%5B1%5D=type_of_data%3APerformance",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title III Performance Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title III Participation Data",
                     "description": "Participation data on English learners in Title III districts.  Data  from SY 2010-11 onward available for download.",
                     "downloadURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3ATitle%20III&f%5B1%5D=type_of_data%3AParticipation",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title III Participation Data"
                 }
             ],
+            "identifier": "29a551d1-1a26-4cf0-9321-d821196eceaa",
             "keyword": [
                 "district",
                 "e630b5cb-5a69-415b-a2cf-21aa81831130",
@@ -6501,21 +6484,11 @@
                 "state",
                 "title-iii"
             ],
-            "bureauCode": [
-                "018:10"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2024-10-22T00:20:42.292871",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Title I Part C Performance, Participation, and Funding Data",
-            "description": "Performance, participation, and funding data related to Title I, Part C (Migratory students). Data  from SY 2010-11 onward.",
-            "modified": "2024-10-21T23:57:43.392712",
-            "accessLevel": "public",
-            "identifier": "44f3c586-5b2e-445e-8c3c-953d7d5d2892",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Elementary and Secondary Education (OESE)",
@@ -6532,30 +6505,40 @@
                     }
                 }
             },
+            "title": "Title III (English Learners) Performance, Participation, and Funding Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Elementary and Secondary Education",
                 "hasEmail": "mailto:eddataexpress@ed.gov"
             },
+            "description": "Performance, participation, and funding data related to Title I, Part C (Migratory students). Data  from SY 2010-11 onward.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title I Part C Data Dashboards",
                     "description": "Dashboard presentation of data representing gap in performance between migratory students and all students, participation, and funding.  Data  from SY 2010-11 onward.",
                     "downloadURL": "https://eddataexpress.ed.gov/dashboard/mep?sy=147",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title I Part C Data Dashboards"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title I Part C Participation Data",
                     "description": "Participation data of migratory students in states that receive Title I, Part C funding. Data  from SY 2010-11 onward available for download.",
                     "downloadURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3ATitle%20I%2C%20Part%20C",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title I Part C Participation Data"
                 }
             ],
+            "identifier": "44f3c586-5b2e-445e-8c3c-953d7d5d2892",
             "keyword": [
                 "e630b5cb-5a69-415b-a2cf-21aa81831130",
                 "edfacts",
@@ -6566,21 +6549,11 @@
                 "secondary",
                 "state"
             ],
-            "bureauCode": [
-                "018:10"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-21T23:57:43.392712",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Title I Part D Performance, Participation, and Funding Data",
-            "description": "Data related to Title I, Part D performance, participation, and funding.  Data from SY 2010-11 onward.",
-            "modified": "2024-10-21T23:55:20.758842",
-            "accessLevel": "public",
-            "identifier": "2343113f-70f3-4dd4-81a8-47fc518a5d93",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Elementary and Secondary Education (OESE)",
@@ -6597,46 +6570,56 @@
                     }
                 }
             },
+            "title": "Title I Part C Performance, Participation, and Funding Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Elementary and Secondary Education",
                 "hasEmail": "mailto:eddataexpress@ed.gov"
             },
+            "description": "Data related to Title I, Part D performance, participation, and funding.  Data from SY 2010-11 onward.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title I Part D, Subpart 1 Data Dashboard",
                     "description": "Dashboard presentation of participation, performance, and funding for Title I, Part D, Subpart I.  Data from SY 2010-11 onward.",
                     "downloadURL": "https://eddataexpress.ed.gov/dashboard/title-i-part-d-subpart-1?sy=2304",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title I Part D, Subpart 1 Data Dashboard"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title 1, Part D, Subpart 2 Data Dashboard",
                     "description": "Dashboard presentation of participation, performance, and funding data for Title I, Part D, Subpart 2.  Data from SY 2010-11 onward.",
                     "downloadURL": "https://eddataexpress.ed.gov/dashboard/title-i-part-d-subpart-2",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title 1, Part D, Subpart 2 Data Dashboard"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title 1, Part D Participation Data",
                     "description": "Participation data for Title I, Part D. Data from SY 2010-11 onward available for download.",
                     "downloadURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3ATitle%20I%2C%20Part%20D&f%5B1%5D=type_of_data%3AParticipation",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title 1, Part D Participation Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title 1, Part D Performance Data",
                     "description": "Performance data for Title I, Part D. Data from SY 2010-11 onward available for download.",
                     "downloadURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3ATitle%20I%2C%20Part%20D&f%5B1%5D=type_of_data%3APerformance",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title 1, Part D Performance Data"
                 }
             ],
+            "identifier": "2343113f-70f3-4dd4-81a8-47fc518a5d93",
             "keyword": [
                 "district",
                 "e630b5cb-5a69-415b-a2cf-21aa81831130",
@@ -6648,23 +6631,11 @@
                 "secondary",
                 "state"
             ],
-            "bureauCode": [
-                "018:10"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2024-10-21T23:55:20.758842",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts School Improvement Grant, 2011-12",
-            "description": "EDFacts School Improvement Grant, 2011-12 (EDFacts SIG:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts SIG:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data about students, teachers, principals, and schools from states to monitor and report performance on the School Improvement Grant (SIG) program at the school levels. EDFacts SIG:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts SIG:2011-12 are from 14 data groups with information on Advanced Coursework, Dual Enrollment, Advanced Coursework/Dual Enrollment, Average Scale Scores, Increased Learning Time, Intervention Used, School Year Minutes, Student Attendance Rate, Teacher Attendance Rate, Persistently Lowest-Achieving Schools, Principal Evaluations, Principal Performance Level Names, Teacher Evaluations, and Teacher Performance Level Names. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2024-10-21T23:52:31.142430",
-            "accessLevel": "public",
-            "identifier": "60aa0309-d71f-4f81-acff-6c361767106b",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Elementary and Secondary Education (OESE)",
@@ -6681,21 +6652,32 @@
                     }
                 }
             },
+            "title": "Title I Part D Performance, Participation, and Funding Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts School Improvement Grant, 2011-12 (EDFacts SIG:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts SIG:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data about students, teachers, principals, and schools from states to monitor and report performance on the School Improvement Grant (SIG) program at the school levels. EDFacts SIG:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts SIG:2011-12 are from 14 data groups with information on Advanced Coursework, Dual Enrollment, Advanced Coursework/Dual Enrollment, Average Scale Scores, Increased Learning Time, Intervention Used, School Year Minutes, Student Attendance Rate, Teacher Attendance Rate, Persistently Lowest-Achieving Schools, Principal Evaluations, Principal Performance Level Names, Teacher Evaluations, and Teacher Performance Level Names. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www2.ed.gov/programs/sif/edfactssiglidatasy1112.xls",
                     "format": "XLS",
-                    "title": "edfactssiglidatasy1112.xls",
-                    "downloadURL": "https://www2.ed.gov/programs/sif/edfactssiglidatasy1112.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "edfactssiglidatasy1112.xls"
                 }
             ],
+            "identifier": "60aa0309-d71f-4f81-acff-6c361767106b",
             "keyword": [
                 "advanced-coursework",
                 "attendance",
@@ -6720,32 +6702,17 @@
                 "student",
                 "teacher"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-10-21T23:52:31.142430",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Neighborhood Poverty Estimates, 2020-21",
-            "description": "The 2020-2021 School Neighborhood Poverty Estimates are based on school locations from the 2020-2021 Common Core of Data (CCD) school file and income data from families with children ages 5 to 17 in the U.S. Census Bureau\u2019s 2017-2021 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools.<p style='margin-top:0px; margin-bottom:0px; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></p><p style='margin-top:0px; margin-bottom:0px; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px; font-weight:bold;'><span style='font-family:inherit;'></span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span></p>",
-            "modified": "2024-10-19T12:48:33.179537",
-            "accessLevel": "public",
-            "identifier": "544f2c79-fbdd-456d-94be-f828d45ac65f",
-            "issued": "2023-08-23T15:45:23.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                "name": "Office of Elementary and Secondary Education (OESE)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -6758,80 +6725,92 @@
                         }
                     }
                 }
-                }
             },
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "EDFacts School Improvement Grant, 2011-12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "The 2020-2021 School Neighborhood Poverty Estimates are based on school locations from the 2020-2021 Common Core of Data (CCD) school file and income data from families with children ages 5 to 17 in the U.S. Census Bureau\u2019s 2017-2021 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools.<p style='margin-top:0px; margin-bottom:0px; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></p><p style='margin-top:0px; margin-bottom:0px; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px; font-weight:bold;'><span style='font-family:inherit;'></span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span></p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/10bd90462ec14a53bab1827bc8f533c9/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/10bd90462ec14a53bab1827bc8f533c9/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-2020-21",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-2020-21"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_SIDE_1721_PUBLICSCH_2021/MapServer/1",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_SIDE_1721_PUBLICSCH_2021/MapServer/1"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School Neighborhood Poverty Estimates",
                     "description": "Technical Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SIDE_PUBSCH_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "School Neighborhood Poverty Estimates",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_SIDE1721_PUBSCHS2021.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10bd90462ec14a53bab1827bc8f533c9/csv?layers=1",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10bd90462ec14a53bab1827bc8f533c9/csv?layers=1"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10bd90462ec14a53bab1827bc8f533c9/geojson?layers=1",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10bd90462ec14a53bab1827bc8f533c9/geojson?layers=1"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10bd90462ec14a53bab1827bc8f533c9/shapefile?layers=1",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10bd90462ec14a53bab1827bc8f533c9/shapefile?layers=1"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10bd90462ec14a53bab1827bc8f533c9/kml?layers=1",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10bd90462ec14a53bab1827bc8f533c9/kml?layers=1"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "544f2c79-fbdd-456d-94be-f828d45ac65f",
+            "issued": "2023-08-23T15:45:23.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -6841,25 +6820,11 @@
                 "side",
                 "spatially-interpolated-demographic-estimates"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:33.179537",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Neighborhood Poverty Estimates, 2018-19",
-            "description": "<div style='text-align:Left;'><div><div><p style='margin:0px;'>The 2018-2019 School Neighborhood Poverty Estimates are based on school locations from the 2018-2019 Common Core of Data (CCD) school file and income data from families with children ages 5 to 17 in the U.S. Census Bureau\u2019s 2015-2019 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools.</p><p style='margin:0px;'><br /></p><p style='font-weight:bold; margin:0 0 0 0;'><span></span></p><p style='margin:0 0 11 0;'><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span></p></div></div></div>",
-            "modified": "2024-10-19T12:48:32.200095",
-            "accessLevel": "public",
-            "identifier": "91107a82-94f2-4f56-82e7-f54761dcaf3f",
-            "issued": "2021-06-09T18:05:31.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -6880,78 +6845,92 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School Neighborhood Poverty Estimates, 2020-21"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p style='margin:0px;'>The 2018-2019 School Neighborhood Poverty Estimates are based on school locations from the 2018-2019 Common Core of Data (CCD) school file and income data from families with children ages 5 to 17 in the U.S. Census Bureau\u2019s 2015-2019 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools.</p><p style='margin:0px;'><br /></p><p style='font-weight:bold; margin:0 0 0 0;'><span></span></p><p style='margin:0 0 11 0;'><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/8c7c4af648174dc1ad08bcb09303591e/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/8c7c4af648174dc1ad08bcb09303591e/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-2018-19",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-2018-19"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_SIDE_1519_PUBLICSCH_1819/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_SIDE_1519_PUBLICSCH_1819/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School Neighborhood Poverty Estimates",
                     "description": "Technical Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SIDE_PUBSCH_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "School Neighborhood Poverty Estimates",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_SIDE1519_PUBSCHS1819.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8c7c4af648174dc1ad08bcb09303591e/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8c7c4af648174dc1ad08bcb09303591e/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8c7c4af648174dc1ad08bcb09303591e/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8c7c4af648174dc1ad08bcb09303591e/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8c7c4af648174dc1ad08bcb09303591e/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8c7c4af648174dc1ad08bcb09303591e/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8c7c4af648174dc1ad08bcb09303591e/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8c7c4af648174dc1ad08bcb09303591e/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "91107a82-94f2-4f56-82e7-f54761dcaf3f",
+            "issued": "2021-06-09T18:05:31.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -6961,25 +6940,11 @@
                 "side",
                 "spatially-interpolated-demographic-estimates"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:32.200095",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Neighborhood Poverty Estimates, 2017-18",
-            "description": "<div style='text-align:Left;'><p><span>The 2017-2018 School Neighborhood Poverty Estimates are based on school locations from the 2017-2018 Common Core of Data (CCD) school file and income data from families with children ages 5 to 17 in the U.S. Census Bureau\u2019s 2014-2018 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools.</span></p><p><span style='font-family:Arial, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><span><br /></span></p></div>",
-            "modified": "2024-10-19T12:48:31.016101",
-            "accessLevel": "public",
-            "identifier": "e8903fa7-987a-439b-b2d5-468ff5efe691",
-            "issued": "2020-04-27T13:58:15.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -7000,77 +6965,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School Neighborhood Poverty Estimates, 2018-19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p><span>The 2017-2018 School Neighborhood Poverty Estimates are based on school locations from the 2017-2018 Common Core of Data (CCD) school file and income data from families with children ages 5 to 17 in the U.S. Census Bureau\u2019s 2014-2018 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools.</span></p><p><span style='font-family:Arial, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><span><br /></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/82561a1eb6914fa1ac7581520b97bd42/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/82561a1eb6914fa1ac7581520b97bd42/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-2017-18",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-2017-18"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_SIDE_1418_PUBLICSCH_1718/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_SIDE_1418_PUBLICSCH_1718/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School Neighborhood Poverty Estimates",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SIDE_PUBSCH_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "School Neighborhood Poverty Estimates",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_SIDE1418_PUBSCHS1718.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/82561a1eb6914fa1ac7581520b97bd42/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/82561a1eb6914fa1ac7581520b97bd42/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/82561a1eb6914fa1ac7581520b97bd42/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/82561a1eb6914fa1ac7581520b97bd42/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/82561a1eb6914fa1ac7581520b97bd42/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/82561a1eb6914fa1ac7581520b97bd42/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/82561a1eb6914fa1ac7581520b97bd42/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/82561a1eb6914fa1ac7581520b97bd42/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "e8903fa7-987a-439b-b2d5-468ff5efe691",
+            "issued": "2020-04-27T13:58:15.000Z",
             "keyword": [
                 "edge",
                 "education",
@@ -7086,25 +7065,11 @@
                 "side",
                 "snp"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:31.016101",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Attendance Boundary Survey 2013-2014",
-            "description": "<div style='text-align:Left;'><div><div><p style='margin:0 0 0 0;'><span><span>The School Attendance Boundaries Survey (SABS) was an experimental survey conducted by the U.S. Department of Education\u2019s (ED) National Center for Education Statistics (NCES) with assistance from the U.S. Census Bureau to collect school attendance boundaries for regular schools in the 50 states and the District of Columbia. Attendance boundaries, sometimes known as school catchment areas, define the geographic extent served by a local school for the purpose of student assignments. School district administrators create attendance areas to help organize and plan district-wide services, and districts may adjust individual school boundaries to help balance the physical capacity of local schools with changes in the local school-age population. The SABS collection includes boundaries for more than 70,000 schools in over 12,000 school districts throughout the U.S.</span></span></p><p style='margin:0 0 0 0;'><span><span><br /></span></span></p><p style='margin:0 0 0 0;'><span><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></span></p><p></p></div></div></div>",
-            "modified": "2024-10-19T12:48:30.153133",
-            "accessLevel": "public",
-            "identifier": "6bf0f3a0-6f69-4988-ba67-9c6082c92e8b",
-            "issued": "2020-03-21T13:36:10.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -7125,63 +7090,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School Neighborhood Poverty Estimates, 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p style='margin:0 0 0 0;'><span><span>The School Attendance Boundaries Survey (SABS) was an experimental survey conducted by the U.S. Department of Education\u2019s (ED) National Center for Education Statistics (NCES) with assistance from the U.S. Census Bureau to collect school attendance boundaries for regular schools in the 50 states and the District of Columbia. Attendance boundaries, sometimes known as school catchment areas, define the geographic extent served by a local school for the purpose of student assignments. School district administrators create attendance areas to help organize and plan district-wide services, and districts may adjust individual school boundaries to help balance the physical capacity of local schools with changes in the local school-age population. The SABS collection includes boundaries for more than 70,000 schools in over 12,000 school districts throughout the U.S.</span></span></p><p style='margin:0 0 0 0;'><span><span><br /></span></span></p><p style='margin:0 0 0 0;'><span><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></span></p><p></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/98802515e4a349eb871443d7bf17ffee/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/98802515e4a349eb871443d7bf17ffee/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-attendance-boundary-survey-2013-2014",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-attendance-boundary-survey-2013-2014"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/SABS_1314/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/SABS_1314/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/98802515e4a349eb871443d7bf17ffee/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/98802515e4a349eb871443d7bf17ffee/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/98802515e4a349eb871443d7bf17ffee/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/98802515e4a349eb871443d7bf17ffee/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/98802515e4a349eb871443d7bf17ffee/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/98802515e4a349eb871443d7bf17ffee/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/98802515e4a349eb871443d7bf17ffee/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/98802515e4a349eb871443d7bf17ffee/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "6bf0f3a0-6f69-4988-ba67-9c6082c92e8b",
+            "issued": "2020-03-21T13:36:10.000Z",
             "keyword": [
                 "attendance-zones",
                 "ccd",
@@ -7202,25 +7181,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:30.153133",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Locales 2018",
-            "description": "<div style='text-align:Left;'><p style='margin:0 0 0 0;'><span><span>This data layer produced by the National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located. The criteria for these classifications are defined by NCES, but they rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The 2018 NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line 2018. The NCES Education Demographic and Geographic Estimate (EDGE) program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to annually update the locale boundaries. For more information about the NCES locale framework,\u00a0</span></span>and to download the data,\u00a0see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>. The classifications include:</p><p style='margin:0 0 0 0;'></p><ul><li><span><span>City - Large (11): Territory inside an Urbanized Area and inside a Principal City with population of 250,000 or more. </span></span></li><li><span><span>City - Midsize (12): Territory inside an Urbanized Area and inside a Principal City with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>City - Small (13): Territory inside an Urbanized Area and inside a Principal City with population less than 100,000. </span></span></li><li><span><span>Suburb \u2013 Large (21): Territory outside a Principal City and inside an Urbanized Area with population of 250,000 or more. </span></span></li><li><span><span>Suburb - Midsize (22): Territory outside a Principal City and inside an Urbanized Area with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>Suburb - Small (23): Territory outside a Principal City and inside an Urbanized Area with population less than 100,000. </span></span></li><li><span><span>Town - Fringe (31): Territory inside an Urban Cluster that is less than or equal to 10 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Distant (32): Territory inside an Urban Cluster that is more than 10 miles and less than or equal to 35 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Remote (33): Territory inside an Urban Cluster that is more than 35 miles of an Urbanized Area. </span></span></li><li><span><span>Rural - Fringe (41): Census-defined rural territory that is less than or equal to 5 miles from an Urbanized Area, as well as rural territory that is less than or equal to 2.5 miles from an Urban Cluster. </span></span></li><li><span><span>Rural - Distant (42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urbanized Area, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Cluster. </span></span></li></ul><ul><li><span><span>Rural - Remote (43): Census-defined rural territory that is more than 25 miles from an Urbanized Area and is also more than 10 miles from an Urban Cluster.</span></span></li></ul><div>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.</div><p></p><p><span></span></p></div>",
-            "modified": "2024-10-19T12:48:29.388183",
-            "accessLevel": "public",
-            "identifier": "ea9bfa5d-a15c-4d2a-80f9-5a00d52ab141",
-            "issued": "2019-03-05T22:39:22.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -7241,63 +7206,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School Attendance Boundary Survey 2013-2014"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p style='margin:0 0 0 0;'><span><span>This data layer produced by the National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located. The criteria for these classifications are defined by NCES, but they rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The 2018 NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line 2018. The NCES Education Demographic and Geographic Estimate (EDGE) program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to annually update the locale boundaries. For more information about the NCES locale framework,\u00a0</span></span>and to download the data,\u00a0see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>. The classifications include:</p><p style='margin:0 0 0 0;'></p><ul><li><span><span>City - Large (11): Territory inside an Urbanized Area and inside a Principal City with population of 250,000 or more. </span></span></li><li><span><span>City - Midsize (12): Territory inside an Urbanized Area and inside a Principal City with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>City - Small (13): Territory inside an Urbanized Area and inside a Principal City with population less than 100,000. </span></span></li><li><span><span>Suburb \u2013 Large (21): Territory outside a Principal City and inside an Urbanized Area with population of 250,000 or more. </span></span></li><li><span><span>Suburb - Midsize (22): Territory outside a Principal City and inside an Urbanized Area with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>Suburb - Small (23): Territory outside a Principal City and inside an Urbanized Area with population less than 100,000. </span></span></li><li><span><span>Town - Fringe (31): Territory inside an Urban Cluster that is less than or equal to 10 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Distant (32): Territory inside an Urban Cluster that is more than 10 miles and less than or equal to 35 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Remote (33): Territory inside an Urban Cluster that is more than 35 miles of an Urbanized Area. </span></span></li><li><span><span>Rural - Fringe (41): Census-defined rural territory that is less than or equal to 5 miles from an Urbanized Area, as well as rural territory that is less than or equal to 2.5 miles from an Urban Cluster. </span></span></li><li><span><span>Rural - Distant (42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urbanized Area, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Cluster. </span></span></li></ul><ul><li><span><span>Rural - Remote (43): Census-defined rural territory that is more than 25 miles from an Urbanized Area and is also more than 10 miles from an Urban Cluster.</span></span></li></ul><div>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.</div><p></p><p><span></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/1910072305434517bbb53507525db777/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/1910072305434517bbb53507525db777/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2018",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2018"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE18_US/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE18_US/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1910072305434517bbb53507525db777/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1910072305434517bbb53507525db777/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1910072305434517bbb53507525db777/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1910072305434517bbb53507525db777/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1910072305434517bbb53507525db777/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1910072305434517bbb53507525db777/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1910072305434517bbb53507525db777/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1910072305434517bbb53507525db777/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "ea9bfa5d-a15c-4d2a-80f9-5a00d52ab141",
+            "issued": "2019-03-05T22:39:22.000Z",
             "keyword": [
                 "city",
                 "distant",
@@ -7313,25 +7292,11 @@
                 "suburb",
                 "town"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:29.388183",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Locales 2014",
-            "description": "<div style='text-align:Left;'><p style='margin-bottom:0in; margin-bottom:.0001pt;'><span style='background:white;'>This data layer produced by the </span>National\nCenter for Education Statistics\u2019 (<span style='background:white;'>NCES) Education\nDemographic and Geographic Estimates (EDGE) program provides a geographic locale\nframework that classifies all U.S. territory into twelve categories ranging\nfrom Large Cities to Remote Rural areas. NCES uses this framework to describe\nthe type of geographic area where schools and school districts are located. </span>The\ncriteria for these classifications are defined by NCES, but they rely on\nstandard geographic areas developed and maintained by the U.S. Census Bureau.\nThe 2014 NCES Locale boundaries are based on geographic areas represented in\nCensus TIGER/Line 2014. The NCES EDGE program collaborates with the U.S. Census\nBureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE)\nBranch to annually update the locale boundaries. For more information about the\nNCES locale framework, and to download the data, see:\u00a0 <a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>. The\nclassifications include:</p><p style='margin-bottom:0in; margin-bottom:.0001pt;'></p><ul><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Large City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(11): Territory inside an Urbanized Area and inside a Principal City with\npopulation of 250,000 or more.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Midsize City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(12): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Small City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(13): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb \u2013 Large</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(21): Territory outside a Principal City and inside an Urbanized Area with\npopulation of 250,000 or more.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Midsi</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>ze\n(22): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Small</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(23): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Fringe</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(31): Territory inside an Urban Cluster that is less than or equal to 10 miles\nfrom an Urbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Distant</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(32): Territory inside an Urban Cluster that is more than 10 miles and less\nthan or equal to 35 miles from an Urbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Remote</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(33): Territory inside an Urban Cluster that is more than 35 miles of an\nUrbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Fringe</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(41): Census-defined rural territory that is less than or equal to 5 miles from\nan Urbanized Area, as well as rural territory that is less than or equal to 2.5\nmiles from an Urban Cluster.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Distant</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(42): Census-defined rural territory that is more than 5 miles but less than or\nequal to 25 miles from an Urbanized Area, as well as rural territory that is\nmore than 2.5 miles but less than or equal to 10 miles from an Urban Cluster.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Remote</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(43): Census-defined rural territory that is more than 25 miles from an\nUrbanized Area and is also more than 10 miles from an Urban Cluster.</span></li></ul><div>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.</div><p></p><p style='margin-top:0px; margin-bottom:0px;'>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n</p><p><span></span></p></div>",
-            "modified": "2024-10-19T12:48:28.408887",
-            "accessLevel": "public",
-            "identifier": "a439d11a-23bb-4df4-a230-707109a11dcf",
-            "issued": "2017-11-26T22:25:26.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -7352,77 +7317,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Locales 2018"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p style='margin-bottom:0in; margin-bottom:.0001pt;'><span style='background:white;'>This data layer produced by the </span>National\nCenter for Education Statistics\u2019 (<span style='background:white;'>NCES) Education\nDemographic and Geographic Estimates (EDGE) program provides a geographic locale\nframework that classifies all U.S. territory into twelve categories ranging\nfrom Large Cities to Remote Rural areas. NCES uses this framework to describe\nthe type of geographic area where schools and school districts are located. </span>The\ncriteria for these classifications are defined by NCES, but they rely on\nstandard geographic areas developed and maintained by the U.S. Census Bureau.\nThe 2014 NCES Locale boundaries are based on geographic areas represented in\nCensus TIGER/Line 2014. The NCES EDGE program collaborates with the U.S. Census\nBureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE)\nBranch to annually update the locale boundaries. For more information about the\nNCES locale framework, and to download the data, see:\u00a0 <a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>. The\nclassifications include:</p><p style='margin-bottom:0in; margin-bottom:.0001pt;'></p><ul><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Large City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(11): Territory inside an Urbanized Area and inside a Principal City with\npopulation of 250,000 or more.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Midsize City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(12): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Small City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(13): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb \u2013 Large</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(21): Territory outside a Principal City and inside an Urbanized Area with\npopulation of 250,000 or more.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Midsi</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>ze\n(22): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Small</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(23): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Fringe</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(31): Territory inside an Urban Cluster that is less than or equal to 10 miles\nfrom an Urbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Distant</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(32): Territory inside an Urban Cluster that is more than 10 miles and less\nthan or equal to 35 miles from an Urbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Remote</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(33): Territory inside an Urban Cluster that is more than 35 miles of an\nUrbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Fringe</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(41): Census-defined rural territory that is less than or equal to 5 miles from\nan Urbanized Area, as well as rural territory that is less than or equal to 2.5\nmiles from an Urban Cluster.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Distant</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(42): Census-defined rural territory that is more than 5 miles but less than or\nequal to 25 miles from an Urbanized Area, as well as rural territory that is\nmore than 2.5 miles but less than or equal to 10 miles from an Urban Cluster.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Remote</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(43): Census-defined rural territory that is more than 25 miles from an\nUrbanized Area and is also more than 10 miles from an Urban Cluster.</span></li></ul><div>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.</div><p></p><p style='margin-top:0px; margin-bottom:0px;'>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n</p><p><span></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/8d81129d2d3b4b029bd9e38a25c8e574/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/8d81129d2d3b4b029bd9e38a25c8e574/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2014",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2014"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE14_US/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE14_US/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Locale Boundaries File Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_NCES_LOCALE.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Locale Boundaries File Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Entire US",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_LOCALE14_NCES_ALL_US.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Entire US"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8d81129d2d3b4b029bd9e38a25c8e574/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8d81129d2d3b4b029bd9e38a25c8e574/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8d81129d2d3b4b029bd9e38a25c8e574/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8d81129d2d3b4b029bd9e38a25c8e574/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8d81129d2d3b4b029bd9e38a25c8e574/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8d81129d2d3b4b029bd9e38a25c8e574/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8d81129d2d3b4b029bd9e38a25c8e574/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/8d81129d2d3b4b029bd9e38a25c8e574/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "a439d11a-23bb-4df4-a230-707109a11dcf",
+            "issued": "2017-11-26T22:25:26.000Z",
             "keyword": [
                 "city",
                 "distant",
@@ -7439,25 +7418,11 @@
                 "suburb",
                 "town"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:28.408887",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Locales 2019",
-            "description": "<div style='text-align:Left;'><p style='margin:0 0 0 0;'><span>This data layer produced by the National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located. The criteria for these classifications are defined by NCES, but they rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The 2019 NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line 2019. The NCES Education Demographic and Geographic Estimate (EDGE) program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to annually update the locale boundaries. For more information about the NCES locale framework,\u00a0</span>and to download the data,\u00a0see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>. The classifications include:</p><p style='margin:0 0 0 0;'><span><span></span></span></p><p style='margin:0 0 0 0;'></p><ul><li><span><span>City - Large (11): Territory inside an Urbanized Area and inside a Principal City with population of 250,000 or more. </span></span></li><li><span><span>City - Midsize (12): Territory inside an Urbanized Area and inside a Principal City with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>City - Small (13): Territory inside an Urbanized Area and inside a Principal City with population less than 100,000. </span></span></li><li><span><span>Suburb \u2013 Large (21): Territory outside a Principal City and inside an Urbanized Area with population of 250,000 or more. </span></span></li><li><span><span>Suburb - Midsize (22): Territory outside a Principal City and inside an Urbanized Area with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>Suburb - Small (23): Territory outside a Principal City and inside an Urbanized Area with population less than 100,000. </span></span></li><li><span><span>Town - Fringe (31): Territory inside an Urban Cluster that is less than or equal to 10 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Distant (32): Territory inside an Urban Cluster that is more than 10 miles and less than or equal to 35 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Remote (33): Territory inside an Urban Cluster that is more than 35 miles of an Urbanized Area. </span></span></li><li><span><span>Rural - Fringe (41): Census-defined rural territory that is less than or equal to 5 miles from an Urbanized Area, as well as rural territory that is less than or equal to 2.5 miles from an Urban Cluster. </span></span></li><li><span><span>Rural - Distant (42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urbanized Area, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Cluster. </span></span></li><li><span><span>Rural - Remote (43): Census-defined rural territory that is more than 25 miles from an Urbanized Area and is also more than 10 miles from an Urban Cluster.</span></span></li></ul><div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /><br /></div><p></p></div>",
-            "modified": "2024-10-19T12:48:27.501145",
-            "accessLevel": "public",
-            "identifier": "49f2e546-84a6-4f87-8de8-0b13a9203991",
-            "issued": "2019-12-04T20:49:59.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -7478,63 +7443,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Locales 2014"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p style='margin:0 0 0 0;'><span>This data layer produced by the National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located. The criteria for these classifications are defined by NCES, but they rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The 2019 NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line 2019. The NCES Education Demographic and Geographic Estimate (EDGE) program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to annually update the locale boundaries. For more information about the NCES locale framework,\u00a0</span>and to download the data,\u00a0see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>. The classifications include:</p><p style='margin:0 0 0 0;'><span><span></span></span></p><p style='margin:0 0 0 0;'></p><ul><li><span><span>City - Large (11): Territory inside an Urbanized Area and inside a Principal City with population of 250,000 or more. </span></span></li><li><span><span>City - Midsize (12): Territory inside an Urbanized Area and inside a Principal City with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>City - Small (13): Territory inside an Urbanized Area and inside a Principal City with population less than 100,000. </span></span></li><li><span><span>Suburb \u2013 Large (21): Territory outside a Principal City and inside an Urbanized Area with population of 250,000 or more. </span></span></li><li><span><span>Suburb - Midsize (22): Territory outside a Principal City and inside an Urbanized Area with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>Suburb - Small (23): Territory outside a Principal City and inside an Urbanized Area with population less than 100,000. </span></span></li><li><span><span>Town - Fringe (31): Territory inside an Urban Cluster that is less than or equal to 10 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Distant (32): Territory inside an Urban Cluster that is more than 10 miles and less than or equal to 35 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Remote (33): Territory inside an Urban Cluster that is more than 35 miles of an Urbanized Area. </span></span></li><li><span><span>Rural - Fringe (41): Census-defined rural territory that is less than or equal to 5 miles from an Urbanized Area, as well as rural territory that is less than or equal to 2.5 miles from an Urban Cluster. </span></span></li><li><span><span>Rural - Distant (42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urbanized Area, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Cluster. </span></span></li><li><span><span>Rural - Remote (43): Census-defined rural territory that is more than 25 miles from an Urbanized Area and is also more than 10 miles from an Urban Cluster.</span></span></li></ul><div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /><br /></div><p></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/b437474b90484b0ebcc0d1904a51ae3d/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/b437474b90484b0ebcc0d1904a51ae3d/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2019",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2019"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE19_US/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE19_US/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b437474b90484b0ebcc0d1904a51ae3d/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b437474b90484b0ebcc0d1904a51ae3d/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b437474b90484b0ebcc0d1904a51ae3d/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b437474b90484b0ebcc0d1904a51ae3d/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b437474b90484b0ebcc0d1904a51ae3d/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b437474b90484b0ebcc0d1904a51ae3d/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b437474b90484b0ebcc0d1904a51ae3d/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b437474b90484b0ebcc0d1904a51ae3d/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "49f2e546-84a6-4f87-8de8-0b13a9203991",
+            "issued": "2019-12-04T20:49:59.000Z",
             "keyword": [
                 "city",
                 "distant",
@@ -7550,25 +7529,11 @@
                 "suburb",
                 "town"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:27.501145",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Locales 2015",
-            "description": "<p style='margin-bottom:0in; margin-bottom:.0001pt;'><span style='background:white;'>This data layer produced by the </span><span>National\nCenter for Education Statistics\u2019 (</span><span style='background:white;'>NCES)\nEducation Demographic and Geographic Estimates (EDGE) program provides a\ngeographic locale framework that classifies all U.S. territory into twelve\ncategories ranging from Large Cities to Remote Rural areas. NCES uses this\nframework to describe the type of geographic area where schools and school\ndistricts are located. </span><span>The criteria for these classifications are\ndefined by NCES, but they rely on standard geographic areas developed and\nmaintained by the U.S. Census Bureau. The 2015 NCES Locale boundaries are based\non geographic areas represented in Census TIGER/Line 2015. The NCES Education\nDemographic and Geographic Estimate (EDGE) program collaborates with the U.S.\nCensus Bureau\u2019s Education Demographic, Geographic, and Economic Statistics\n(EDGE) Branch to annually update the locale boundaries. For more information\nabout the NCES locale framework,\u00a0</span>and to download the data,\u00a0see:\u00a0\u00a0<font color='#0000ee'><u>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</u></font>. The\nclassifications include:</p>\n\n<p style='margin:0in; margin-bottom:.0001pt; background:white;'></p><ul><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Large City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(11): Territory inside an Urbanized Area and inside a Principal City with\npopulation of 250,000 or more.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Midsize City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(12): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Small City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(13): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb \u2013 Large</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(21): Territory outside a Principal City and inside an Urbanized Area with\npopulation of 250,000 or more.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Midsi</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>ze\n(22): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Small</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(23): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Fringe</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(31): Territory inside an Urban Cluster that is less than or equal to 10 miles\nfrom an Urbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Distant</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(32): Territory inside an Urban Cluster that is more than 10 miles and less\nthan or equal to 35 miles from an Urbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Remote</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(33): Territory inside an Urban Cluster that is more than 35 miles of an\nUrbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Fringe</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(41): Census-defined rural territory that is less than or equal to 5 miles from\nan Urbanized Area, as well as rural territory that is less than or equal to 2.5\nmiles from an Urban Cluster.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Distant</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(42): Census-defined rural territory that is more than 5 miles but less than or\nequal to 25 miles from an Urbanized Area, as well as rural territory that is\nmore than 2.5 miles but less than or equal to 10 miles from an Urban Cluster.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Remote</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(43): Census-defined rural territory that is more than 25 miles from an\nUrbanized Area and is also more than 10 miles from an Urban Cluster.</span></li></ul><div>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.</div>",
-            "modified": "2024-10-19T12:48:26.443568",
-            "accessLevel": "public",
-            "identifier": "82ab3d83-0b73-4a4d-97e8-6d8bfb0079c9",
-            "issued": "2017-11-26T22:29:36.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -7589,77 +7554,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Locales 2019"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p style='margin-bottom:0in; margin-bottom:.0001pt;'><span style='background:white;'>This data layer produced by the </span><span>National\nCenter for Education Statistics\u2019 (</span><span style='background:white;'>NCES)\nEducation Demographic and Geographic Estimates (EDGE) program provides a\ngeographic locale framework that classifies all U.S. territory into twelve\ncategories ranging from Large Cities to Remote Rural areas. NCES uses this\nframework to describe the type of geographic area where schools and school\ndistricts are located. </span><span>The criteria for these classifications are\ndefined by NCES, but they rely on standard geographic areas developed and\nmaintained by the U.S. Census Bureau. The 2015 NCES Locale boundaries are based\non geographic areas represented in Census TIGER/Line 2015. The NCES Education\nDemographic and Geographic Estimate (EDGE) program collaborates with the U.S.\nCensus Bureau\u2019s Education Demographic, Geographic, and Economic Statistics\n(EDGE) Branch to annually update the locale boundaries. For more information\nabout the NCES locale framework,\u00a0</span>and to download the data,\u00a0see:\u00a0\u00a0<font color='#0000ee'><u>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</u></font>. The\nclassifications include:</p>\n\n<p style='margin:0in; margin-bottom:.0001pt; background:white;'></p><ul><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Large City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(11): Territory inside an Urbanized Area and inside a Principal City with\npopulation of 250,000 or more.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Midsize City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(12): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Small City</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(13): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb \u2013 Large</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(21): Territory outside a Principal City and inside an Urbanized Area with\npopulation of 250,000 or more.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Midsi</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>ze\n(22): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Small</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(23): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 100,000.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Fringe</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(31): Territory inside an Urban Cluster that is less than or equal to 10 miles\nfrom an Urbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Distant</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(32): Territory inside an Urban Cluster that is more than 10 miles and less\nthan or equal to 35 miles from an Urbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Remote</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(33): Territory inside an Urban Cluster that is more than 35 miles of an\nUrbanized Area.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Fringe</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(41): Census-defined rural territory that is less than or equal to 5 miles from\nan Urbanized Area, as well as rural territory that is less than or equal to 2.5\nmiles from an Urban Cluster.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Distant</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(42): Census-defined rural territory that is more than 5 miles but less than or\nequal to 25 miles from an Urbanized Area, as well as rural territory that is\nmore than 2.5 miles but less than or equal to 10 miles from an Urban Cluster.</span><br /></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Remote</span></i><span style='font-size:11pt; font-family:Calibri, sans-serif;'>\n(43): Census-defined rural territory that is more than 25 miles from an\nUrbanized Area and is also more than 10 miles from an Urban Cluster.</span></li></ul><div>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.</div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/45652a4263bd4773ac283ae39789f728/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/45652a4263bd4773ac283ae39789f728/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2015",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2015"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE15_US/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE15_US/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Locale Boundaries File Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_NCES_LOCALE.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Locale Boundaries File Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Entire US",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_LOCALE15_US.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Entire US"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45652a4263bd4773ac283ae39789f728/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45652a4263bd4773ac283ae39789f728/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45652a4263bd4773ac283ae39789f728/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45652a4263bd4773ac283ae39789f728/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45652a4263bd4773ac283ae39789f728/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45652a4263bd4773ac283ae39789f728/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45652a4263bd4773ac283ae39789f728/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45652a4263bd4773ac283ae39789f728/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "82ab3d83-0b73-4a4d-97e8-6d8bfb0079c9",
+            "issued": "2017-11-26T22:29:36.000Z",
             "keyword": [
                 "city",
                 "distant",
@@ -7676,25 +7655,11 @@
                 "suburb",
                 "town"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:26.443568",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Locales 2016",
-            "description": "<div style='text-align:Left;'><p style='margin-top:0px; margin-bottom:0.0001pt; background-color:rgb(255, 255, 255);'><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>This data layer produced by the\u00a0</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px;'>National Center for Education Statistics\u2019 (</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located.\u00a0</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px;'>The criteria for these classifications are defined by NCES, but they rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The 2016 NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line 2016. The NCES Education Demographic and Geographic Estimate (EDGE) program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to annually update the locale boundaries. For more information about the NCES locale framework,\u00a0</span><font face='Avenir Next W01, Avenir Next W00, Avenir Next, Avenir, Helvetica Neue, Helvetica, Arial, sans-serif'><span style='font-size:17px;'>and to download the data,</span></font><span style='font-family:&quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:15px;'>\u00a0</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px;'>see:\u00a0\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px; color:rgb(0, 121, 193); text-decoration-line:none;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px;'>. The classifications include:</span></p><p style='margin:0in 0in 0.0001pt; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:17px; background:white;'></p><ul><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Large City</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(11): Territory inside an Urbanized Area and inside a Principal City with population of 250,000 or more.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Midsize City</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(12): Territory inside an Urbanized Area and inside a Principal City with population less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Small City</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(13): Territory inside an Urbanized Area and inside a Principal City with population less than 100,000.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Suburb \u2013 Large</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(21): Territory outside a Principal City and inside an Urbanized Area with population of 250,000 or more.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Suburb - Midsi</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>ze (22): Territory outside a Principal City and inside an Urbanized Area with population less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Suburb - Small</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(23): Territory outside a Principal City and inside an Urbanized Area with population less than 100,000.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Town - Fringe</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(31): Territory inside an Urban Cluster that is less than or equal to 10 miles from an Urbanized Area.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Town - Distant</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(32): Territory inside an Urban Cluster that is more than 10 miles and less than or equal to 35 miles from an Urbanized Area.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Town - Remote</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(33): Territory inside an Urban Cluster that is more than 35 miles of an Urbanized Area.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Rural - Fringe</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(41): Census-defined rural territory that is less than or equal to 5 miles from an Urbanized Area, as well as rural territory that is less than or equal to 2.5 miles from an Urban Cluster.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Rural - Distant</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urbanized Area, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Cluster.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Rural - Remote</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(43): Census-defined rural territory that is more than 25 miles from an Urbanized Area and is also more than 10 miles from an Urban Cluster.</span></li></ul><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px;'>All\n information contained in this file is in the public domain. Data users \nare advised to review NCES program documentation and feature class \nmetadata to understand the limitations and appropriate use of these \ndata.</span></div></div>",
-            "modified": "2024-10-19T12:48:25.456803",
-            "accessLevel": "public",
-            "identifier": "38387280-9b17-496f-88ce-4698fd3144d6",
-            "issued": "2018-06-22T17:01:39.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -7715,77 +7680,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Locales 2015"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p style='margin-top:0px; margin-bottom:0.0001pt; background-color:rgb(255, 255, 255);'><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>This data layer produced by the\u00a0</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px;'>National Center for Education Statistics\u2019 (</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located.\u00a0</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px;'>The criteria for these classifications are defined by NCES, but they rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The 2016 NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line 2016. The NCES Education Demographic and Geographic Estimate (EDGE) program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to annually update the locale boundaries. For more information about the NCES locale framework,\u00a0</span><font face='Avenir Next W01, Avenir Next W00, Avenir Next, Avenir, Helvetica Neue, Helvetica, Arial, sans-serif'><span style='font-size:17px;'>and to download the data,</span></font><span style='font-family:&quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:15px;'>\u00a0</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px;'>see:\u00a0\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px; color:rgb(0, 121, 193); text-decoration-line:none;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px;'>. The classifications include:</span></p><p style='margin:0in 0in 0.0001pt; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:17px; background:white;'></p><ul><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Large City</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(11): Territory inside an Urbanized Area and inside a Principal City with population of 250,000 or more.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Midsize City</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(12): Territory inside an Urbanized Area and inside a Principal City with population less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Small City</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(13): Territory inside an Urbanized Area and inside a Principal City with population less than 100,000.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Suburb \u2013 Large</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(21): Territory outside a Principal City and inside an Urbanized Area with population of 250,000 or more.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Suburb - Midsi</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>ze (22): Territory outside a Principal City and inside an Urbanized Area with population less than 250,000 and greater than or equal to 100,000.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Suburb - Small</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(23): Territory outside a Principal City and inside an Urbanized Area with population less than 100,000.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Town - Fringe</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(31): Territory inside an Urban Cluster that is less than or equal to 10 miles from an Urbanized Area.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Town - Distant</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(32): Territory inside an Urban Cluster that is more than 10 miles and less than or equal to 35 miles from an Urbanized Area.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Town - Remote</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(33): Territory inside an Urban Cluster that is more than 35 miles of an Urbanized Area.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Rural - Fringe</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(41): Census-defined rural territory that is less than or equal to 5 miles from an Urbanized Area, as well as rural territory that is less than or equal to 2.5 miles from an Urban Cluster.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Rural - Distant</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urbanized Area, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Cluster.</span><br /></li><li><i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>Rural - Remote</span></i><span style='font-family:Calibri, sans-serif; font-size:11pt;'>\u00a0(43): Census-defined rural territory that is more than 25 miles from an Urbanized Area and is also more than 10 miles from an Urban Cluster.</span></li></ul><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif !important; font-size:17px;'>All\n information contained in this file is in the public domain. Data users \nare advised to review NCES program documentation and feature class \nmetadata to understand the limitations and appropriate use of these \ndata.</span></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/f9f0e21315ed4ba7a8762cb414827bf6/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/f9f0e21315ed4ba7a8762cb414827bf6/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2016",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2016"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE16_US/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE16_US/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Locale Boundaries File Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_NCES_LOCALE.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Locale Boundaries File Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Entire US",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_LOCALE16_US.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Entire US"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f9f0e21315ed4ba7a8762cb414827bf6/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f9f0e21315ed4ba7a8762cb414827bf6/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f9f0e21315ed4ba7a8762cb414827bf6/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f9f0e21315ed4ba7a8762cb414827bf6/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f9f0e21315ed4ba7a8762cb414827bf6/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f9f0e21315ed4ba7a8762cb414827bf6/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f9f0e21315ed4ba7a8762cb414827bf6/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f9f0e21315ed4ba7a8762cb414827bf6/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "38387280-9b17-496f-88ce-4698fd3144d6",
+            "issued": "2018-06-22T17:01:39.000Z",
             "keyword": [
                 "city",
                 "distant",
@@ -7801,25 +7780,11 @@
                 "suburb",
                 "town"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:25.456803",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Locales 2017",
-            "description": "<div style='text-align:Left;'><p style='margin-bottom:0in; margin-bottom:.0001pt;'><span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>This data layer produced by the </span>National\nCenter for Education Statistics\u2019 (<span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>NCES)\nEducation Demographic and Geographic Estimates (EDGE) program provides a\ngeographic locale framework that classifies all U.S. territory into twelve\ncategories ranging from Large Cities to Remote Rural areas. NCES uses this\nframework to describe the type of geographic area where schools and school\ndistricts are located. </span>The criteria for these classifications are\ndefined by NCES, but they rely on standard geographic areas developed and\nmaintained by the U.S. Census Bureau. The 2017 NCES Locale boundaries are based\non geographic areas represented in Census TIGER/Line 2017. The NCES Education\nDemographic and Geographic Estimate (EDGE) program collaborates with the U.S.\nCensus Bureau\u2019s Education Demographic, Geographic, and Economic Statistics\n(EDGE) Branch to annually update the locale boundaries. For more information\nabout the NCES locale framework, and to download the data,\u00a0see:\u00a0\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>.\nThe classifications include:</p><p style='margin-bottom:0in; margin-bottom:.0001pt;'></p><ul><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Large City</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(11): Territory inside an Urbanized Area and inside a Principal City with\npopulation of 250,000 or more.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Midsize City</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(12): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 250,000 and greater than or equal to 100,000.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Small City</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(13): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 100,000.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb \u2013 Large</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(21): Territory outside a Principal City and inside an Urbanized Area with\npopulation of 250,000 or more.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Midsi</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>ze\n(22): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 250,000 and greater than or equal to 100,000.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Small</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(23): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 100,000.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Fringe</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(31): Territory inside an Urban Cluster that is less than or equal to 10 miles\nfrom an Urbanized Area.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Distant</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(32): Territory inside an Urban Cluster that is more than 10 miles and less\nthan or equal to 35 miles from an Urbanized Area.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Remote</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(33): Territory inside an Urban Cluster that is more than 35 miles of an\nUrbanized Area.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Fringe</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(41): Census-defined rural territory that is less than or equal to 5 miles from\nan Urbanized Area, as well as rural territory that is less than or equal to 2.5\nmiles from an Urban Cluster.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Distant</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(42): Census-defined rural territory that is more than 5 miles but less than or\nequal to 25 miles from an Urbanized Area, as well as rural territory that is\nmore than 2.5 miles but less than or equal to 10 miles from an Urban Cluster.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Remote</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(43): Census-defined rural territory that is more than 25 miles from an\nUrbanized Area and is also more than 10 miles from an Urban Cluster.</span></li></ul><div>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.</div><p></p><p style='margin-top:0px; margin-bottom:0px;'>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n</p><p><span></span></p></div>",
-            "modified": "2024-10-19T12:48:24.268023",
-            "accessLevel": "public",
-            "identifier": "4ec43ec6-d70a-4cfa-bb05-586c22ab3d27",
-            "issued": "2018-06-22T17:20:15.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -7840,77 +7805,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Locales 2016"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p style='margin-bottom:0in; margin-bottom:.0001pt;'><span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>This data layer produced by the </span>National\nCenter for Education Statistics\u2019 (<span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>NCES)\nEducation Demographic and Geographic Estimates (EDGE) program provides a\ngeographic locale framework that classifies all U.S. territory into twelve\ncategories ranging from Large Cities to Remote Rural areas. NCES uses this\nframework to describe the type of geographic area where schools and school\ndistricts are located. </span>The criteria for these classifications are\ndefined by NCES, but they rely on standard geographic areas developed and\nmaintained by the U.S. Census Bureau. The 2017 NCES Locale boundaries are based\non geographic areas represented in Census TIGER/Line 2017. The NCES Education\nDemographic and Geographic Estimate (EDGE) program collaborates with the U.S.\nCensus Bureau\u2019s Education Demographic, Geographic, and Economic Statistics\n(EDGE) Branch to annually update the locale boundaries. For more information\nabout the NCES locale framework, and to download the data,\u00a0see:\u00a0\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>.\nThe classifications include:</p><p style='margin-bottom:0in; margin-bottom:.0001pt;'></p><ul><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Large City</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(11): Territory inside an Urbanized Area and inside a Principal City with\npopulation of 250,000 or more.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Midsize City</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(12): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 250,000 and greater than or equal to 100,000.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Small City</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(13): Territory inside an Urbanized Area and inside a Principal City with\npopulation less than 100,000.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb \u2013 Large</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(21): Territory outside a Principal City and inside an Urbanized Area with\npopulation of 250,000 or more.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Midsi</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>ze\n(22): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 250,000 and greater than or equal to 100,000.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Suburb - Small</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(23): Territory outside a Principal City and inside an Urbanized Area with\npopulation less than 100,000.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Fringe</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(31): Territory inside an Urban Cluster that is less than or equal to 10 miles\nfrom an Urbanized Area.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Distant</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(32): Territory inside an Urban Cluster that is more than 10 miles and less\nthan or equal to 35 miles from an Urbanized Area.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Town - Remote</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(33): Territory inside an Urban Cluster that is more than 35 miles of an\nUrbanized Area.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Fringe</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(41): Census-defined rural territory that is less than or equal to 5 miles from\nan Urbanized Area, as well as rural territory that is less than or equal to 2.5\nmiles from an Urban Cluster.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Distant</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(42): Census-defined rural territory that is more than 5 miles but less than or\nequal to 25 miles from an Urbanized Area, as well as rural territory that is\nmore than 2.5 miles but less than or equal to 10 miles from an Urban Cluster.</span></li><li><i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>Rural - Remote</span></i><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif;'>\n(43): Census-defined rural territory that is more than 25 miles from an\nUrbanized Area and is also more than 10 miles from an Urban Cluster.</span></li></ul><div>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.</div><p></p><p style='margin-top:0px; margin-bottom:0px;'>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n</p><p><span></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/7e50d1b09d4e44b09cc46aae7c0b17d3/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/7e50d1b09d4e44b09cc46aae7c0b17d3/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2017",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2017"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE17_US/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE17_US/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Education Demographic and Geographic Estimates Program (EDGE) Locale Boundaries User\u2019s Manual",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/NCES_LOCALE_USERSMANUAL_2016012.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Education Demographic and Geographic Estimates Program (EDGE) Locale Boundaries User\u2019s Manual"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Entire US",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_LOCALE17_US.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Entire US"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e50d1b09d4e44b09cc46aae7c0b17d3/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e50d1b09d4e44b09cc46aae7c0b17d3/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e50d1b09d4e44b09cc46aae7c0b17d3/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e50d1b09d4e44b09cc46aae7c0b17d3/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e50d1b09d4e44b09cc46aae7c0b17d3/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e50d1b09d4e44b09cc46aae7c0b17d3/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e50d1b09d4e44b09cc46aae7c0b17d3/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e50d1b09d4e44b09cc46aae7c0b17d3/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "4ec43ec6-d70a-4cfa-bb05-586c22ab3d27",
+            "issued": "2018-06-22T17:20:15.000Z",
             "keyword": [
                 "018-107",
                 "018107",
@@ -7928,25 +7907,11 @@
                 "suburb",
                 "town"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:24.268023",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Locales 2021",
-            "description": "<div style='text-align:Left;'><p>This data layer produced by the National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located. The criteria for these classifications are defined by NCES, and rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line. For more information about the NCES locale framework, and to download the data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>. The classifications include:<br /></p><p></p><div style='text-align:Left;'><ul><li><li>City - Large (11): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population of 250,000 or more.</li><li>City - Midsize (12): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population less than 250,000 and greater than or equal to 100,000.</li><li>City - Small (13): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population less than 100,000.</li><li>Suburb \u2013 Large (21): Territory outside a Principal City and inside an Urban Area with population of 250,000 or more.</li><li>Suburb - Midsize (22): Territory outside a Principal City and inside an Urban Area with population less than 250,000 and greater than or equal to 100,000.</li><li>Suburb - Small (23): Territory outside a Principal City and inside an Urban Area with population less than 100,000.\u00a0</li><li>Town - Fringe (31): Territory inside an Urban Area with a population less than 50,000 that is less than or equal to 10 miles from an Urban Area with a population of 50,000 or more.</li><li>Town - Distant (32): Territory inside an Urban Area with a population less than 50,000 that is more than 10 miles and less than or equal to 35 miles from an Urban Area with a population of 50,000 or more.</li><li>Town - Remote (33): Territory inside an Urban Area with a population less than 50,000 that is more than 35 miles of an Urban Area with a population of 50,000 or more.</li><li>Rural - Fringe (41): Census-defined rural territory that is less than or equal to 5 miles from an Urban Area of 50,000 or more, as well as rural territory that is less than or equal to 2.5 miles from an Urban Area with a population less than 50,000.</li><li>Rural - Distant (42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urban Area with a population of 50,000 or more, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Area with a population less than 50,000.</li><li>Rural - Remote (43): Census-defined rural territory that is more than 25 miles from an Urban Area with a population of 50,000 or more and is also more than 10 miles from an Urban Area with a population less than 50,000.</li></li></ul></div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /><p></p></div>",
-            "modified": "2024-10-19T12:48:22.993819",
-            "accessLevel": "public",
-            "identifier": "32eeebf2-b0fa-46d3-83bc-0176a061a1bc",
-            "issued": "2022-11-10T16:44:40.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -7967,77 +7932,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Locales 2017"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>This data layer produced by the National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located. The criteria for these classifications are defined by NCES, and rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line. For more information about the NCES locale framework, and to download the data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>. The classifications include:<br /></p><p></p><div style='text-align:Left;'><ul><li><li>City - Large (11): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population of 250,000 or more.</li><li>City - Midsize (12): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population less than 250,000 and greater than or equal to 100,000.</li><li>City - Small (13): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population less than 100,000.</li><li>Suburb \u2013 Large (21): Territory outside a Principal City and inside an Urban Area with population of 250,000 or more.</li><li>Suburb - Midsize (22): Territory outside a Principal City and inside an Urban Area with population less than 250,000 and greater than or equal to 100,000.</li><li>Suburb - Small (23): Territory outside a Principal City and inside an Urban Area with population less than 100,000.\u00a0</li><li>Town - Fringe (31): Territory inside an Urban Area with a population less than 50,000 that is less than or equal to 10 miles from an Urban Area with a population of 50,000 or more.</li><li>Town - Distant (32): Territory inside an Urban Area with a population less than 50,000 that is more than 10 miles and less than or equal to 35 miles from an Urban Area with a population of 50,000 or more.</li><li>Town - Remote (33): Territory inside an Urban Area with a population less than 50,000 that is more than 35 miles of an Urban Area with a population of 50,000 or more.</li><li>Rural - Fringe (41): Census-defined rural territory that is less than or equal to 5 miles from an Urban Area of 50,000 or more, as well as rural territory that is less than or equal to 2.5 miles from an Urban Area with a population less than 50,000.</li><li>Rural - Distant (42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urban Area with a population of 50,000 or more, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Area with a population less than 50,000.</li><li>Rural - Remote (43): Census-defined rural territory that is more than 25 miles from an Urban Area with a population of 50,000 or more and is also more than 10 miles from an Urban Area with a population less than 50,000.</li></li></ul></div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /><p></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/c9501bdb824e4ca68ffe5eec2f09a59b/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/c9501bdb824e4ca68ffe5eec2f09a59b/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2021",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2021"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE21_US/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE21_US/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Locale Boundaries File Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_NCES_LOCALE.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Locale Boundaries File Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Entire US",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_Locale21_US.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Entire US"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/c9501bdb824e4ca68ffe5eec2f09a59b/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/c9501bdb824e4ca68ffe5eec2f09a59b/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/c9501bdb824e4ca68ffe5eec2f09a59b/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/c9501bdb824e4ca68ffe5eec2f09a59b/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/c9501bdb824e4ca68ffe5eec2f09a59b/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/c9501bdb824e4ca68ffe5eec2f09a59b/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/c9501bdb824e4ca68ffe5eec2f09a59b/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/c9501bdb824e4ca68ffe5eec2f09a59b/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "32eeebf2-b0fa-46d3-83bc-0176a061a1bc",
+            "issued": "2022-11-10T16:44:40.000Z",
             "keyword": [
                 "city",
                 "distant",
@@ -8053,25 +8032,11 @@
                 "suburb",
                 "town"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:22.993819",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Locales 2020",
-            "description": "<div style='text-align:Left;'><p><span>This data layer produced by the National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located. The criteria for these classifications are defined by NCES, but they rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The 2020 NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line 2020. The NCES Education Demographic and Geographic Estimate (EDGE) program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to annually update the locale boundaries. For more information about the NCES locale framework, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a><span>. The classifications include: </span></p><p></p><ul><li><span><span>City - Large (11): Territory inside an Urbanized Area and inside a Principal City with population of 250,000 or more. </span></span></li><li><span><span>City - Midsize (12): Territory inside an Urbanized Area and inside a Principal City with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>City - Small (13): Territory inside an Urbanized Area and inside a Principal City with population less than 100,000. </span></span></li><li><span><span>Suburb \u2013 Large (21): Territory outside a Principal City and inside an Urbanized Area with population of 250,000 or more. </span></span></li><li><span><span>Suburb - Midsize (22): Territory outside a Principal City and inside an Urbanized Area with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>Suburb - Small (23): Territory outside a Principal City and inside an Urbanized Area with population less than 100,000. </span></span></li><li><span><span>Town - Fringe (31): Territory inside an Urban Cluster that is less than or equal to 10 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Distant (32): Territory inside an Urban Cluster that is more than 10 miles and less than or equal to 35 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Remote (33): Territory inside an Urban Cluster that is more than 35 miles of an Urbanized Area. </span></span></li><li><span><span>Rural - Fringe (41): Census-defined rural territory that is less than or equal to 5 miles from an Urbanized Area, as well as rural territory that is less than or equal to 2.5 miles from an Urban Cluster. </span></span></li><li><span><span>Rural - Distant (42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urbanized Area, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Cluster. </span></span></li><li><span><span>Rural - Remote (43): Census-defined rural territory that is more than 25 miles from an Urbanized Area and is also more than 10 miles from an Urban Cluster.</span></span></li></ul><div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><p></p></div>",
-            "modified": "2024-10-19T12:48:22.145669",
-            "accessLevel": "public",
-            "identifier": "5c488b7e-2779-4d29-b86b-efdc252ef8d2",
-            "issued": "2021-04-29T18:25:28.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -8092,77 +8057,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Locales 2021"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p><span>This data layer produced by the National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located. The criteria for these classifications are defined by NCES, but they rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The 2020 NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line 2020. The NCES Education Demographic and Geographic Estimate (EDGE) program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to annually update the locale boundaries. For more information about the NCES locale framework, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a><span>. The classifications include: </span></p><p></p><ul><li><span><span>City - Large (11): Territory inside an Urbanized Area and inside a Principal City with population of 250,000 or more. </span></span></li><li><span><span>City - Midsize (12): Territory inside an Urbanized Area and inside a Principal City with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>City - Small (13): Territory inside an Urbanized Area and inside a Principal City with population less than 100,000. </span></span></li><li><span><span>Suburb \u2013 Large (21): Territory outside a Principal City and inside an Urbanized Area with population of 250,000 or more. </span></span></li><li><span><span>Suburb - Midsize (22): Territory outside a Principal City and inside an Urbanized Area with population less than 250,000 and greater than or equal to 100,000. </span></span></li><li><span><span>Suburb - Small (23): Territory outside a Principal City and inside an Urbanized Area with population less than 100,000. </span></span></li><li><span><span>Town - Fringe (31): Territory inside an Urban Cluster that is less than or equal to 10 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Distant (32): Territory inside an Urban Cluster that is more than 10 miles and less than or equal to 35 miles from an Urbanized Area. </span></span></li><li><span><span>Town - Remote (33): Territory inside an Urban Cluster that is more than 35 miles of an Urbanized Area. </span></span></li><li><span><span>Rural - Fringe (41): Census-defined rural territory that is less than or equal to 5 miles from an Urbanized Area, as well as rural territory that is less than or equal to 2.5 miles from an Urban Cluster. </span></span></li><li><span><span>Rural - Distant (42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urbanized Area, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Cluster. </span></span></li><li><span><span>Rural - Remote (43): Census-defined rural territory that is more than 25 miles from an Urbanized Area and is also more than 10 miles from an Urban Cluster.</span></span></li></ul><div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><p></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/2b441a672742434f8bec73a730194827/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/2b441a672742434f8bec73a730194827/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2020",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locales-2020"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE20_US/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Locale_Boundaries/EDGE_LOCALE20_US/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Locale Boundaries File Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_NCES_LOCALE.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Locale Boundaries File Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Entire US",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/edge_locale20_nces_all_us.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Entire US"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2b441a672742434f8bec73a730194827/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2b441a672742434f8bec73a730194827/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2b441a672742434f8bec73a730194827/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2b441a672742434f8bec73a730194827/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2b441a672742434f8bec73a730194827/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2b441a672742434f8bec73a730194827/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2b441a672742434f8bec73a730194827/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2b441a672742434f8bec73a730194827/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "5c488b7e-2779-4d29-b86b-efdc252ef8d2",
+            "issued": "2021-04-29T18:25:28.000Z",
             "keyword": [
                 "city",
                 "distant",
@@ -8178,25 +8157,11 @@
                 "suburb",
                 "town"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:22.145669",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Neighborhood Poverty Estimates, 2016-17",
-            "description": "<div><font face='Avenir Next W01, Avenir Next W00, Avenir Next, Avenir, Helvetica Neue, sans-serif'><span style='font-size:16px;'>The 2016-2017 School Neighborhood Poverty Estimates\u00a0are based on school locations from the 2016-2017 Common Core of Data (CCD) school file and income data from families with children ages 5 to 17 in the U.S. Census Bureau\u2019s 2013-2017 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools.</span></font></div><div><font face='Avenir Next W01, Avenir Next W00, Avenir Next, Avenir, Helvetica Neue, sans-serif'><span style='font-size:16px;'><br /></span></font></div><div><font face='Avenir Next W01, Avenir Next W00, Avenir Next, Avenir, Helvetica Neue, sans-serif'><span style='font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></font></div>",
-            "modified": "2024-10-19T12:48:21.323715",
-            "accessLevel": "public",
-            "identifier": "9d86dc92-05f8-4e91-9cbb-1dcf85ef40a6",
-            "issued": "2020-03-21T13:25:39.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -8217,77 +8182,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Locales 2020"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div><font face='Avenir Next W01, Avenir Next W00, Avenir Next, Avenir, Helvetica Neue, sans-serif'><span style='font-size:16px;'>The 2016-2017 School Neighborhood Poverty Estimates\u00a0are based on school locations from the 2016-2017 Common Core of Data (CCD) school file and income data from families with children ages 5 to 17 in the U.S. Census Bureau\u2019s 2013-2017 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools.</span></font></div><div><font face='Avenir Next W01, Avenir Next W00, Avenir Next, Avenir, Helvetica Neue, sans-serif'><span style='font-size:16px;'><br /></span></font></div><div><font face='Avenir Next W01, Avenir Next W00, Avenir Next, Avenir, Helvetica Neue, sans-serif'><span style='font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></font></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/eafacbb8ed48433ebdcb2fd9cf93eb82/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/eafacbb8ed48433ebdcb2fd9cf93eb82/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-2016-17",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-2016-17"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/SIDE_1317_SY_1617/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/SIDE_1317_SY_1617/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School Neighborhood Poverty Estimates, 2016-2017",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SIDE1317_PUBSCH1617_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates, 2016-2017"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "School Neighborhood Poverty Estimates, 2016-2017",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_SIDE1317_PUBSCHS1617.zip",
-                    "mediaType": "text/plain"
-                },
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates, 2016-2017"
+                },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/eafacbb8ed48433ebdcb2fd9cf93eb82/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/eafacbb8ed48433ebdcb2fd9cf93eb82/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/eafacbb8ed48433ebdcb2fd9cf93eb82/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/eafacbb8ed48433ebdcb2fd9cf93eb82/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/eafacbb8ed48433ebdcb2fd9cf93eb82/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/eafacbb8ed48433ebdcb2fd9cf93eb82/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/eafacbb8ed48433ebdcb2fd9cf93eb82/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/eafacbb8ed48433ebdcb2fd9cf93eb82/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "9d86dc92-05f8-4e91-9cbb-1dcf85ef40a6",
+            "issued": "2020-03-21T13:25:39.000Z",
             "keyword": [
                 "edge",
                 "education",
@@ -8303,25 +8282,11 @@
                 "side",
                 "snp"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:21.323715",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Neighborhood Poverty Estimates, 2015-16",
-            "description": "<div style='text-align:Left;'><div><div><p><span>The 2015-2016 School Neighborhood Poverty Estimates\u00a0are based on school locations from the 2015-2016 Common Core of Data (CCD) school file and income data from families with children ages 5 to 17 in the U.S. Census Bureau\u2019s 2012-2016 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools. <br /></span></p><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div></div></div>",
-            "modified": "2024-10-19T12:48:20.365938",
-            "accessLevel": "public",
-            "identifier": "81dead46-3faa-4fc6-ab12-51817ed958de",
-            "issued": "2020-03-21T13:07:49.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -8342,100 +8307,100 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School Neighborhood Poverty Estimates, 2016-17"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p><span>The 2015-2016 School Neighborhood Poverty Estimates\u00a0are based on school locations from the 2015-2016 Common Core of Data (CCD) school file and income data from families with children ages 5 to 17 in the U.S. Census Bureau\u2019s 2012-2016 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools. <br /></span></p><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/9bed2f9afd86406c88dea2f40e73a658/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/9bed2f9afd86406c88dea2f40e73a658/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-2015-16",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-2015-16"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_SIDE_1216_PS_1516/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_SIDE_1216_PS_1516/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School Neighborhood Poverty Estimates, 2015-2016",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SIDE1216_PUBSCH1516_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates, 2015-2016"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "School Neighborhood Poverty Estimates, 2015-2016",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_SIDE1216_PUBSCHS1516.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates, 2015-2016"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9bed2f9afd86406c88dea2f40e73a658/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9bed2f9afd86406c88dea2f40e73a658/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9bed2f9afd86406c88dea2f40e73a658/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9bed2f9afd86406c88dea2f40e73a658/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9bed2f9afd86406c88dea2f40e73a658/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9bed2f9afd86406c88dea2f40e73a658/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9bed2f9afd86406c88dea2f40e73a658/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9bed2f9afd86406c88dea2f40e73a658/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "81dead46-3faa-4fc6-ab12-51817ed958de",
+            "issued": "2020-03-21T13:07:49.000Z",
             "keyword": [
                 "side-snp-edge-education-demographic-and-geographic-estimates-program-nces-national-center-for-e",
                 "side-snp-edge-education-demographic-and-geographic-estimates-program-nces-national-center-for-educat"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:20.365938",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Locations 2022-23",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions. School and agency point locations are derived from reported information about the physical location of schools and agency administrative offices. The point locations in this data layer were developed from the 2022-2023 CCD collection. For more information about NCES school point data, see:<a target='_blank' href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><div></div><div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</div></div>",
-            "modified": "2024-10-19T12:48:19.526160",
-            "accessLevel": "public",
-            "identifier": "b6b01bf4-17a6-455d-a4e7-0673dd5afec4",
-            "issued": "2024-02-09T16:43:13.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -8456,63 +8421,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School Neighborhood Poverty Estimates, 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions. School and agency point locations are derived from reported information about the physical location of schools and agency administrative offices. The point locations in this data layer were developed from the 2022-2023 CCD collection. For more information about NCES school point data, see:<a target='_blank' href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><div></div><div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/ffff9c03dee848f5b4fe6400972fcb55/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/ffff9c03dee848f5b4fe6400972fcb55/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2022-23-",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2022-23-"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_2223/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_2223/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ffff9c03dee848f5b4fe6400972fcb55/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ffff9c03dee848f5b4fe6400972fcb55/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ffff9c03dee848f5b4fe6400972fcb55/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ffff9c03dee848f5b4fe6400972fcb55/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ffff9c03dee848f5b4fe6400972fcb55/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ffff9c03dee848f5b4fe6400972fcb55/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ffff9c03dee848f5b4fe6400972fcb55/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ffff9c03dee848f5b4fe6400972fcb55/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "b6b01bf4-17a6-455d-a4e7-0673dd5afec4",
+            "issued": "2024-02-09T16:43:13.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -8528,25 +8507,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:19.526160",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Locations 2021-22",
-            "description": "The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions.  School and agency point locations are derived from reported information about the physical location of schools and agency administrative offices. The point locations in this data layer were developed from the 2021-2022 CCD collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.\u00a0<div><br /></div><div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</div>",
-            "modified": "2024-10-19T12:48:18.483090",
-            "accessLevel": "public",
-            "identifier": "5529cda4-ca1f-4d00-97b0-d18f2b079cfa",
-            "issued": "2023-03-09T01:02:02.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -8567,77 +8532,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Locations 2022-23"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions.  School and agency point locations are derived from reported information about the physical location of schools and agency administrative offices. The point locations in this data layer were developed from the 2021-2022 CCD collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.\u00a0<div><br /></div><div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/bb54cfd626b74fb695cf8534b5f97c12/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/bb54cfd626b74fb695cf8534b5f97c12/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2021-22",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2021-22"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_2122/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_2122/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_2122.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/bb54cfd626b74fb695cf8534b5f97c12/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/bb54cfd626b74fb695cf8534b5f97c12/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/bb54cfd626b74fb695cf8534b5f97c12/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/bb54cfd626b74fb695cf8534b5f97c12/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/bb54cfd626b74fb695cf8534b5f97c12/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/bb54cfd626b74fb695cf8534b5f97c12/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/bb54cfd626b74fb695cf8534b5f97c12/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/bb54cfd626b74fb695cf8534b5f97c12/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "5529cda4-ca1f-4d00-97b0-d18f2b079cfa",
+            "issued": "2023-03-09T01:02:02.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -8653,25 +8632,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:18.483090",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Locations 2019-20",
-            "description": "<div style='text-align:Left;'><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2019-2020 CCD collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p></div>",
-            "modified": "2024-10-19T12:48:17.200181",
-            "accessLevel": "public",
-            "identifier": "6c1a1c80-7395-45ae-aa9e-55513fb96d03",
-            "issued": "2021-03-25T16:36:26.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -8692,77 +8657,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Locations 2021-22"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2019-2020 CCD collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/7e9f773ef00d4bd9b27d3fc1dc4727b0/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/7e9f773ef00d4bd9b27d3fc1dc4727b0/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2019-20",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2019-20"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_1920/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_1920/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_1920.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e9f773ef00d4bd9b27d3fc1dc4727b0/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e9f773ef00d4bd9b27d3fc1dc4727b0/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e9f773ef00d4bd9b27d3fc1dc4727b0/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e9f773ef00d4bd9b27d3fc1dc4727b0/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e9f773ef00d4bd9b27d3fc1dc4727b0/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e9f773ef00d4bd9b27d3fc1dc4727b0/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e9f773ef00d4bd9b27d3fc1dc4727b0/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7e9f773ef00d4bd9b27d3fc1dc4727b0/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "6c1a1c80-7395-45ae-aa9e-55513fb96d03",
+            "issued": "2021-03-25T16:36:26.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -8777,25 +8756,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:17.200181",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Locations 2018-19",
-            "description": "<p>The National Center for Education Statistics\u2019 (NCES)\nEducation Demographic and Geographic Estimate (EDGE) program develops annually\nupdated point locations (latitude and longitude) for public elementary and\nsecondary schools included in the NCES Common Core of Data (CCD). The CCD is an\nannual collection of basic administrative characteristics that includes the\nphysical address for all public schools, school districts, and state education\nagencies in the United States. The NCES EDGE program collaborates with the U.S.\nCensus Bureau\u2019s Education Demographic, Geographic, and Economic Statistics\n(EDGE) Branch to develop point locations for schools and school district\nadministrative offices based on these addresses. The point locations in this\ndata layer were developed from the 2018-2019 CCD collection. For more\ninformation about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p>",
-            "modified": "2024-10-19T12:48:16.096899",
-            "accessLevel": "public",
-            "identifier": "255d5750-bbd2-4c20-8a3a-9139223401d7",
-            "issued": "2020-03-17T16:19:42.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -8816,77 +8781,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Locations 2019-20"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p>The National Center for Education Statistics\u2019 (NCES)\nEducation Demographic and Geographic Estimate (EDGE) program develops annually\nupdated point locations (latitude and longitude) for public elementary and\nsecondary schools included in the NCES Common Core of Data (CCD). The CCD is an\nannual collection of basic administrative characteristics that includes the\nphysical address for all public schools, school districts, and state education\nagencies in the United States. The NCES EDGE program collaborates with the U.S.\nCensus Bureau\u2019s Education Demographic, Geographic, and Economic Statistics\n(EDGE) Branch to develop point locations for schools and school district\nadministrative offices based on these addresses. The point locations in this\ndata layer were developed from the 2018-2019 CCD collection. For more\ninformation about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/005415edb02847ff9b31a788c1a0441b/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/005415edb02847ff9b31a788c1a0441b/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2018-19",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2018-19"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_1819/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_1819/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_1819.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/005415edb02847ff9b31a788c1a0441b/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/005415edb02847ff9b31a788c1a0441b/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/005415edb02847ff9b31a788c1a0441b/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/005415edb02847ff9b31a788c1a0441b/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/005415edb02847ff9b31a788c1a0441b/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/005415edb02847ff9b31a788c1a0441b/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/005415edb02847ff9b31a788c1a0441b/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/005415edb02847ff9b31a788c1a0441b/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "255d5750-bbd2-4c20-8a3a-9139223401d7",
+            "issued": "2020-03-17T16:19:42.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -8901,25 +8880,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:16.096899",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Locations 2017-18",
-            "description": "The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions. The CCD program also provides fiscal data about school district revenues and expenditures. CCD school and agency point locations are derived from reported information about the physical location of schools and agency administrative offices. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual CCD directory file. The point locations in this data layer were developed from the 2017-2018 CCD collection. For more information about NCES school point data, see: https://nces.ed.gov/programs/edge/Geographic/SchoolLocations.",
-            "modified": "2024-10-19T12:48:15.035219",
-            "accessLevel": "public",
-            "identifier": "0b9aaf03-3f15-4936-b285-7482cbe2e03b",
-            "issued": "2020-03-21T12:58:57.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -8940,77 +8905,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Locations 2018-19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions. The CCD program also provides fiscal data about school district revenues and expenditures. CCD school and agency point locations are derived from reported information about the physical location of schools and agency administrative offices. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual CCD directory file. The point locations in this data layer were developed from the 2017-2018 CCD collection. For more information about NCES school point data, see: https://nces.ed.gov/programs/edge/Geographic/SchoolLocations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/fb92b1df7c5a445c96840005cd6de264/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/fb92b1df7c5a445c96840005cd6de264/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2017-18",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2017-18"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_1718/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_1718/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_1718.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fb92b1df7c5a445c96840005cd6de264/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fb92b1df7c5a445c96840005cd6de264/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fb92b1df7c5a445c96840005cd6de264/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fb92b1df7c5a445c96840005cd6de264/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fb92b1df7c5a445c96840005cd6de264/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fb92b1df7c5a445c96840005cd6de264/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fb92b1df7c5a445c96840005cd6de264/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fb92b1df7c5a445c96840005cd6de264/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "0b9aaf03-3f15-4936-b285-7482cbe2e03b",
+            "issued": "2020-03-21T12:58:57.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -9025,25 +9004,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:15.035219",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Locations 2016-17",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2016-2017 CCD collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p></div>",
-            "modified": "2024-10-19T12:48:13.722272",
-            "accessLevel": "public",
-            "identifier": "4b3ccc07-d85c-417e-b214-b833dd17d5e8",
-            "issued": "2020-03-21T12:53:31.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -9064,77 +9029,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Locations 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2016-2017 CCD collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/fa109be704b74281b70cde3680f0d480/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/fa109be704b74281b70cde3680f0d480/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2016-17",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2016-17"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_1617/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_1617/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_1617.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fa109be704b74281b70cde3680f0d480/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fa109be704b74281b70cde3680f0d480/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fa109be704b74281b70cde3680f0d480/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fa109be704b74281b70cde3680f0d480/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fa109be704b74281b70cde3680f0d480/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fa109be704b74281b70cde3680f0d480/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fa109be704b74281b70cde3680f0d480/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fa109be704b74281b70cde3680f0d480/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "4b3ccc07-d85c-417e-b214-b833dd17d5e8",
+            "issued": "2020-03-21T12:53:31.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -9149,25 +9128,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:13.722272",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Locations 2015-16",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2015-2016 CCD collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p><p><span></span></p></div>",
-            "modified": "2024-10-19T12:48:12.308553",
-            "accessLevel": "public",
-            "identifier": "352c4611-8b56-46a5-9314-7de47a19418c",
-            "issued": "2020-03-21T12:47:02.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -9188,77 +9153,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Locations 2016-17"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2015-2016 CCD collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p><p><span></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/741214a4a1824b018506fd140599e57f/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/741214a4a1824b018506fd140599e57f/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2015-16",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-locations-2015-16"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_1516/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_1516/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_1516.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/741214a4a1824b018506fd140599e57f/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/741214a4a1824b018506fd140599e57f/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/741214a4a1824b018506fd140599e57f/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/741214a4a1824b018506fd140599e57f/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/741214a4a1824b018506fd140599e57f/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/741214a4a1824b018506fd140599e57f/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/741214a4a1824b018506fd140599e57f/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/741214a4a1824b018506fd140599e57f/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "352c4611-8b56-46a5-9314-7de47a19418c",
+            "issued": "2020-03-21T12:47:02.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -9275,25 +9254,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:12.308553",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Locations - Current",
-            "description": "<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'>The\nNational Center for Education Statistics\u2019 (NCES) Education Demographic and\nGeographic Estimates (EDGE) program develops bi-annually updated point\nlocations (latitude and longitude) for private schools included in the NCES\nPrivate School Survey (PSS). The PSS is conducted to provide a biennial count\nof the total number of private schools, teachers, and students. The PSS school\nlocation and associated geographic area assignments are derived from reported\ninformation about the physical location of private schools. The school geocode\nfile includes supplemental geographic information for the universe of schools\nreported in the most current PSS school collection, and they can be integrated\nwith the survey files through use of institutional identifiers included in both\nsources. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#0079C1;'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</span></a>\u00a0</span><span style='font-size:11.5pt; color:#4C4C4C;'>and\u00a0</span><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#0079C1;'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</span></a></span></p>\n\n<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'>Previous\ncollections are available for the following year:</span></p>\n\n<ul>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif;'><a href='https://nces.maps.arcgis.com/home/item.html?id=5ebacc8bd42e4d85a66d0661fd5fb29e' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-size:12.0pt; color:blue;'>2021-22</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif;'><a href='https://nces.maps.arcgis.com/home/item.html?id=18cd70b6f5424bbaa05dd4086a29d63b' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-size:12.0pt; color:blue;'>2019-20</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif;'><a href='https://nces.maps.arcgis.com/home/item.html?id=b3c70b83d725438292cce259a0fc1d08' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-size:12.0pt; color:blue;'>2017-18</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif;'><a href='https://nces.maps.arcgis.com/home/item.html?id=528953aa81b24f6f8ec071302c550401' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-size:12.0pt; color:blue;'>2015-16</span></a></span></li>\n</ul>\n\n<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'>All\ninformation contained in this file is in the public domain. Data users are\nadvised to review NCES program documentation and feature class metadata to\nunderstand the limitations and appropriate use of these data.</span></p>",
-            "modified": "2024-10-19T12:48:11.180862",
-            "accessLevel": "public",
-            "identifier": "d80ca738-e107-4584-87e2-ce7ff8f27e9a",
-            "issued": "2020-03-25T21:20:39.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -9314,63 +9279,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Locations 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'>The\nNational Center for Education Statistics\u2019 (NCES) Education Demographic and\nGeographic Estimates (EDGE) program develops bi-annually updated point\nlocations (latitude and longitude) for private schools included in the NCES\nPrivate School Survey (PSS). The PSS is conducted to provide a biennial count\nof the total number of private schools, teachers, and students. The PSS school\nlocation and associated geographic area assignments are derived from reported\ninformation about the physical location of private schools. The school geocode\nfile includes supplemental geographic information for the universe of schools\nreported in the most current PSS school collection, and they can be integrated\nwith the survey files through use of institutional identifiers included in both\nsources. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#0079C1;'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</span></a>\u00a0</span><span style='font-size:11.5pt; color:#4C4C4C;'>and\u00a0</span><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#0079C1;'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</span></a></span></p>\n\n<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'>Previous\ncollections are available for the following year:</span></p>\n\n<ul>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif;'><a href='https://nces.maps.arcgis.com/home/item.html?id=5ebacc8bd42e4d85a66d0661fd5fb29e' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-size:12.0pt; color:blue;'>2021-22</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif;'><a href='https://nces.maps.arcgis.com/home/item.html?id=18cd70b6f5424bbaa05dd4086a29d63b' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-size:12.0pt; color:blue;'>2019-20</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif;'><a href='https://nces.maps.arcgis.com/home/item.html?id=b3c70b83d725438292cce259a0fc1d08' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-size:12.0pt; color:blue;'>2017-18</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif;'><a href='https://nces.maps.arcgis.com/home/item.html?id=528953aa81b24f6f8ec071302c550401' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-size:12.0pt; color:blue;'>2015-16</span></a></span></li>\n</ul>\n\n<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'>All\ninformation contained in this file is in the public domain. Data users are\nadvised to review NCES program documentation and feature class metadata to\nunderstand the limitations and appropriate use of these data.</span></p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/1c004a108b18460bba1ddb29ec1f7982/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/1c004a108b18460bba1ddb29ec1f7982/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::private-school-locations-current",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::private-school-locations-current"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/Private_School_Locations_Current/FeatureServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/Private_School_Locations_Current/FeatureServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1c004a108b18460bba1ddb29ec1f7982/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1c004a108b18460bba1ddb29ec1f7982/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1c004a108b18460bba1ddb29ec1f7982/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1c004a108b18460bba1ddb29ec1f7982/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1c004a108b18460bba1ddb29ec1f7982/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1c004a108b18460bba1ddb29ec1f7982/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
```

