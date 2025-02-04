# Change History for ed.json (Part 5)

### Changes from 31606f9 to dd2190f (Part 5/13)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "The Free Application for Federal Student Aid, 2010-11 (FAFSA 2010-11), is part of the Free Application for Federal Student Aid (FAFSA) program; program data is available since 2006-07 at <https://studentaid.ed.gov/sa/about/data-center/student/application-volume/>. FAFSA 2010-11 (https://studentaid.ed.gov/) is a universe data collection of eligible incoming postsecondary education students, along with a subset of eligible continuing postsecondary education students, that collects financial information to determine the need and eligibility for financial assistance during postsecondary education. FAFSA 2010-11 applications are accepted via web and paper submission. Citizen and specified noncitizen students demonstrating financial need and planning to attend eligible degree or certificate programs in the 50 United States, the District of Columbia, Puerto Rico, and the outlying areas as regular students are eligible to apply for FAFSA 2010-11. FAFSA 2010-11 resulted in an expected family contribution (EFC) for each applying student. Statistics produced from FAFSA 2010-11 include application volumes by postsecondary school, state of legal residence, and completion by high school; and recipient and volume data by program for each school participating in Title IV programs.",
-            "modified": "2023-08-02T20:56:14.465864",
-            "accessLevel": "public",
-            "identifier": "580df5c6-cf9a-42ef-85d0-c536112b2165",
-            "dataQuality": true,
-            "issued": "2011-06-30",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2011-08-03/pdf/2011-19607.pdf",
-            "temporal": "2010/2011",
+            "modified": "2023-08-02T20:56:15.869215",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Federal Student Aid (FSA)",
@@ -34628,117 +34587,135 @@
                     }
                 }
             },
+            "references": [
+                "https://studentaid.ed.gov/sites/default/files/fsawg/datacenter/library/FAFSAReportDefinitions.doc"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2011-08-03/pdf/2011-19607.pdf",
+            "temporal": "2013/2014",
+            "title": "Free Application for Federal Student Aid, 2013-14"
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
+            "description": "The Free Application for Federal Student Aid, 2010-11 (FAFSA 2010-11), is part of the Free Application for Federal Student Aid (FAFSA) program; program data is available since 2006-07 at <https://studentaid.ed.gov/sa/about/data-center/student/application-volume/>. FAFSA 2010-11 (https://studentaid.ed.gov/) is a universe data collection of eligible incoming postsecondary education students, along with a subset of eligible continuing postsecondary education students, that collects financial information to determine the need and eligibility for financial assistance during postsecondary education. FAFSA 2010-11 applications are accepted via web and paper submission. Citizen and specified noncitizen students demonstrating financial need and planning to attend eligible degree or certificate programs in the 50 United States, the District of Columbia, Puerto Rico, and the outlying areas as regular students are eligible to apply for FAFSA 2010-11. FAFSA 2010-11 resulted in an expected family contribution (EFC) for each applying student. Statistics produced from FAFSA 2010-11 include application volumes by postsecondary school, state of legal residence, and completion by high school; and recipient and volume data by program for each school participating in Title IV programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20102011Qtr1.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 1 data (01/01/10-03/31/10) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20102011Qtr1.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20102011Qtr1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20102011Qtr1.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20102011Qtr2.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 2 data (04/01/10-06/30/10) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20102011Qtr2.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20102011Qtr2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20102011Qtr2.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20102011Qtr3.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 3 data (07/01/10-09/30/10) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20102011Qtr3.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20102011Qtr3.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20102011Qtr3.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20102011Q4.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 4 data (10/01/10-12/31/10) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDataBySchool20102011Q4.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDataBySchool20102011Q4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20102011Q4.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20102011Q5.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 5 data (01/01/11-03/31/11) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20102011Q5.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20102011Q5.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20102011Q5.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20102011Q6.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 6 data (04/01/11-06/30/11) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20102011Q6.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20102011Q6.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20102011Q6.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20102011Qtr1.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 1 data (01/01/10-03/31/10) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20102011Qtr1.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20102011Qtr2.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 2 data (04/01/10-06/30/10) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20102011Qtr2.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20102012Qtr3.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 3 data (07/01/10-09/30/10) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20102012Qtr3.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20102011Q4.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 4 data (10/01/10-12/31/10) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20102011Q4.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20102011Q5.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 5 data (01/01/11-03/31/11) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20102011Q5.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20102011Q6.xls",
                     "description": "Free Application for Federal Student Aid, 2010-11 quarter 6 data (04/01/11-06/30/11) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20102011Q6.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/FSADataCenter_Demographics_2010-11Cycle.xls",
                     "format": "XLS",
-                    "title": "FSADataCenter_Demographics_2010-11Cycle",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/FSADataCenter_Demographics_2010-11Cycle.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FSADataCenter_Demographics_2010-11Cycle"
                 }
             ],
+            "identifier": "580df5c6-cf9a-42ef-85d0-c536112b2165",
+            "issued": "2011-06-30",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "fafsa",
@@ -34747,32 +34724,14 @@
                 "free-application-for-federal-student-aid",
                 "postsecondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://studentaid.ed.gov/sites/default/files/fsawg/datacenter/library/FAFSAReportDefinitions.doc"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Free Application for Federal Student Aid, 2015-16",
-            "description": "The Free Application for Federal Student Aid, 2015-16 (FAFSA 2015-16), is part of the Free Application for Federal Student Aid (FAFSA) program; program data is available since 2006-07 at <https://studentaid.ed.gov/sa/about/data-center/student/application-volume/>. FAFSA 2015-16 (https://studentaid.ed.gov/) is a universe data collection of eligible incoming postsecondary education students, along with a subset of eligible continuing postsecondary education students, that collects financial information to determine the need and eligibility for financial assistance during postsecondary education. FAFSA 2015-16 applications are accepted via web and paper submission. Citizen and specified noncitizen students demonstrating financial need and planning to attend eligible degree or certificate programs in the 50 United States, the District of Columbia, Puerto Rico, and the outlying areas as regular students are eligible to apply for FAFSA 2015-16. FAFSA 2015-16 resulted in an expected family contribution (EFC) for each applying student. Statistics produced from FAFSA 2015-16 include application volumes by postsecondary school, state of legal residence, and completion by high school; and recipient and volume data by program for each school participating in Title IV programs.",
-            "modified": "2023-08-02T20:56:13.824288",
-            "accessLevel": "public",
-            "identifier": "d324c9ff-83ef-4ab1-ac1b-3eb4b6075f26",
-            "dataQuality": true,
-            "issued": "2016-06-30",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2011-08-03/pdf/2011-19607.pdf",
-            "temporal": "2015/2016",
+            "modified": "2023-08-02T20:56:14.465864",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Federal Student Aid (FSA)",
@@ -34793,124 +34752,142 @@
                     }
                 }
             },
+            "references": [
+                "https://studentaid.ed.gov/sites/default/files/fsawg/datacenter/library/FAFSAReportDefinitions.doc"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2011-08-03/pdf/2011-19607.pdf",
+            "temporal": "2010/2011",
+            "title": "Free Application for Federal Student Aid, 2010-11"
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
+            "description": "The Free Application for Federal Student Aid, 2015-16 (FAFSA 2015-16), is part of the Free Application for Federal Student Aid (FAFSA) program; program data is available since 2006-07 at <https://studentaid.ed.gov/sa/about/data-center/student/application-volume/>. FAFSA 2015-16 (https://studentaid.ed.gov/) is a universe data collection of eligible incoming postsecondary education students, along with a subset of eligible continuing postsecondary education students, that collects financial information to determine the need and eligibility for financial assistance during postsecondary education. FAFSA 2015-16 applications are accepted via web and paper submission. Citizen and specified noncitizen students demonstrating financial need and planning to attend eligible degree or certificate programs in the 50 United States, the District of Columbia, Puerto Rico, and the outlying areas as regular students are eligible to apply for FAFSA 2015-16. FAFSA 2015-16 resulted in an expected family contribution (EFC) for each applying student. Statistics produced from FAFSA 2015-16 include application volumes by postsecondary school, state of legal residence, and completion by high school; and recipient and volume data by program for each school participating in Title IV programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20152016Qtr1.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 1 data (01/01/15-03/31/15) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_School_Q1.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_School_Q1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20152016Qtr1.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2015_16App_Data_by_School_Q2.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 2 data (04/01/15-06/30/15) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_School_Q2.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_School_Q2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2015_16App_Data_by_School_Q2.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2015_16App_Data_by_School_Q3.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 3 data (07/01/15-09/30/15) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_School_Q3.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_School_Q3.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2015_16App_Data_by_School_Q3.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2015_16App_Data_by_School_Q4.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 4 data (10/01/15-12/31/15) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_School_Q4.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_School_Q4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2015_16App_Data_by_School_Q4.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2015_16App_Data_by_School_Q5.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 5 data (01/01/16-03/31/16) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_School_Q5.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_School_Q5.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2015_16App_Data_by_School_Q5.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "App_Data_by_School_2015_2016_Q6.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 6 data (04/01/16-06/30/16) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_By_School_Q6.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_By_School_Q6.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "App_Data_by_School_2015_2016_Q6.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabyState20152016Q1.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 1 data (01/01/15-03/31/15) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_State_Q1.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_State_Q1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabyState20152016Q1.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2015_16App_Data_by_State_Q2.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 2 data (04/01/15-06/30/15) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_State_Q2.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_State_Q2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2015_16App_Data_by_State_Q2.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2015_16App_Data_by_State_Q3.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 3 data (07/01/15-09/30/15) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_State_Q3.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_State_Q3.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2015_16App_Data_by_State_Q3.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2015_16App_Data_by_State_Q4.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 4 data (10/01/15-12/31/15) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_State_Q4.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_State_Q4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2015_16App_Data_by_State_Q4.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2015_16App_Data_by_State_Q5.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 5 data (01/01/16-03/31/16) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_State_Q5.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_by_State_Q5.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2015_16App_Data_by_State_Q5.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "App_Data_by_State_2015_2016_Q6.xls",
                     "description": "Free Application for Federal Student Aid, 2015-16 quarter 6 data (04/01/16-06/30/16) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_By_State_Q6.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2015_2016App_Data_By_State_Q6.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "App_Data_by_State_2015_2016_Q6.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/FSADataCenter_Demographics_2015-16Cycle.xls",
                     "format": "XLS",
-                    "title": "FSADataCenter_Demographics_2015-16Cycle",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/FSADataCenter_Demographics_2015-16Cycle.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FSADataCenter_Demographics_2015-16Cycle"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "FAFSA Completion by High School",
                     "downloadURL": "http://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-completion-high-school",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "FAFSA Completion by High School"
                 }
             ],
+            "identifier": "d324c9ff-83ef-4ab1-ac1b-3eb4b6075f26",
+            "issued": "2016-06-30",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "fafsa",
@@ -34919,38 +34896,20 @@
                 "free-application-for-federal-student-aid",
                 "postsecondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://studentaid.ed.gov/sites/default/files/fsawg/datacenter/library/FAFSAReportDefinitions.doc"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Culturally Based Education for American Indian/Alaska Native Students: School Feasibility Survey, 2003-04",
-            "description": "The Culturally Based Education for American Indian/Alaska Native Students: School Feasibility Survey, 2003-04 (CBE 2003-04) is a survey that is part of the Regional Educational Laboratory Program (REL) program. CBE 2003-04 (https://ies.ed.gov/ncee/edLabs/regions/) was a cross-sectional survey that assessed the feasibility of conducting experimental research in culturally based education (CBE) programs. The study was conducted using paper questionnaires and telephone follow-ups of educators. Educators of CBE programs were sampled. Key statistics produced from CBE 2003-04 can be used to inform a request for proposal for a feasible experimental study of culturally based education. The results can also be used to design new programs or funding initiatives that combine program development with embedded experimental research to test the effectiveness of new approaches.",
-            "modified": "2023-08-02T20:55:41.968567",
-            "accessLevel": "public",
-            "identifier": "22af694b-8c16-44e2-8bdb-6ac90387d04a",
-            "dataQuality": true,
-            "issued": "2004-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2003/2004",
+            "modified": "2023-08-02T20:56:13.824288",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Evaluation and Regional Assistance (NCEERA)",
+                "name": "Office of Federal Student Aid (FSA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -34965,19 +34924,37 @@
                     }
                 }
             },
+            "references": [
+                "https://studentaid.ed.gov/sites/default/files/fsawg/datacenter/library/FAFSAReportDefinitions.doc"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2011-08-03/pdf/2011-19607.pdf",
+            "temporal": "2015/2016",
+            "title": "Free Application for Federal Student Aid, 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Nelson",
                 "hasEmail": "mailto:steve.nelson@educationnorthwest.org"
             },
+            "dataQuality": true,
+            "description": "The Culturally Based Education for American Indian/Alaska Native Students: School Feasibility Survey, 2003-04 (CBE 2003-04) is a survey that is part of the Regional Educational Laboratory Program (REL) program. CBE 2003-04 (https://ies.ed.gov/ncee/edLabs/regions/) was a cross-sectional survey that assessed the feasibility of conducting experimental research in culturally based education (CBE) programs. The study was conducted using paper questionnaires and telephone follow-ups of educators. Educators of CBE programs were sampled. Key statistics produced from CBE 2003-04 can be used to inform a request for proposal for a feasible experimental study of culturally based education. The results can also be used to design new programs or funding initiatives that combine program development with embedded experimental research to test the effectiveness of new approaches.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "REL Program",
                     "downloadURL": "https://ies.ed.gov/ncee/edLabs/regions",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "REL Program"
                 }
             ],
+            "identifier": "22af694b-8c16-44e2-8bdb-6ac90387d04a",
+            "issued": "2004-06-01",
             "keyword": [
                 "34621008-400b-4c5c-b37f-2af6fec112e8",
                 "american-indians-and-alaska-natives",
@@ -34990,32 +34967,20 @@
                 "native-americans",
                 "questionnaire"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-08-02T20:55:41.968567",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Origination and Disbursement System",
-            "description": "The Common Origination and Disbursement System (COD System) is a technical solution designed to accommodate the COD Process for Perkins, Pell Grant, Academic Competitiveness Grant (ACG), National Science and Mathematics Access to Retain Talent Grant (National SMART Grant), and the Teacher Education Assistance for College and Higher Education (TEACH) Grant and Direct Loan funding.",
-            "modified": "2023-08-02T20:55:41.375034",
-            "accessLevel": "public",
-            "identifier": "793b36e4-719e-46cf-89ae-58f897bbe224",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Federal Student Aid (FSA)",
+                "name": "National Center for Education Evaluation and Regional Assistance (NCEERA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -35030,102 +34995,116 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2003/2004",
+            "title": "Culturally Based Education for American Indian/Alaska Native Students: School Feasibility Survey, 2003-04"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Marini",
                 "hasEmail": "mailto:tara.marini@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Origination and Disbursement System (COD System) is a technical solution designed to accommodate the COD Process for Perkins, Pell Grant, Academic Competitiveness Grant (ACG), National Science and Mathematics Access to Retain Talent Grant (National SMART Grant), and the Teacher Education Assistance for College and Higher Education (TEACH) Grant and Direct Loan funding.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "SummarybySchoolType.xls",
                     "description": "Award Year Grant and Loan Volume Summary by School Type",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/SummarybySchoolType.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/SummarybySchoolType.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "SummarybySchoolType.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AidRecipientsSummary.xls",
                     "description": "Award Year Recipient Summary",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/AidRecipientsSummary.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/AidRecipientsSummary.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AidRecipientsSummary.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "DL_Dashboard_AY2014_2015_Q1.xls",
                     "description": "2014-2015 Award Year Direct Loan Q1 Quarterly Activity",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/DL_Dashboard_AY2014_2015_Q1.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/DL_Dashboard_AY2014_2015_Q1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "DL_Dashboard_AY2014_2015_Q1.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "DL_Dashboard_AY2014_2015_Q2.xls",
                     "description": "2014-2015 Award Year Direct Loan Q2 Quarterly Activity",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/DL_Dashboard_AY2014_2015_Q2.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/DL_Dashboard_AY2014_2015_Q2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "DL_Dashboard_AY2014_2015_Q2.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "DL_Dashboard_AY2014_2015_Q3.xls",
                     "description": "2014-2015 Award Year Direct Loan Q3 Quarterly Activity",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/DL_Dashboard_AY2014_2015_Q3.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/DL_Dashboard_AY2014_2015_Q3.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "DL_Dashboard_AY2014_2015_Q3.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "DL_Dashboard_AY2014_2015_Q4.xls",
                     "description": "2014-2015 Award Year Direct Loan Q4 Quarterly Activity",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/DL_Dashboard_AY2014_2015_Q4.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/DL_Dashboard_AY2014_2015_Q4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "DL_Dashboard_AY2014_2015_Q4.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Q11415AY.xls",
                     "description": "2014-2015 Award Year Grant Q1 Quarterly Activity",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/Q11415AY.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/Q11415AY.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Q11415AY.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Q21415AY.xls",
                     "description": "2014-2015 Award Year Grant Q2 Quarterly Activity",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/Q21415AY.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/Q21415AY.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Q21415AY.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Q31415AY.xls",
                     "description": "2014-2015 Award Year Grant Q3 Quarterly Activity",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/Q31415AY.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/Q31415AY.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Q31415AY.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Q41415AY.xls",
                     "description": "2014-2015 Award Year Grant Q4 Quarterly Activity",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/Q41415AY.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/Q41415AY.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Q41415AY.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2014-15CampusBased.xls",
                     "description": "2014-2015 Award Year Campus-Based Program Data by School",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2014-15CampusBased.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2014-15CampusBased.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2014-15CampusBased.xls"
                 }
             ],
+            "identifier": "793b36e4-719e-46cf-89ae-58f897bbe224",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "cod-system",
@@ -35153,74 +35132,85 @@
                 "title-iv-programs",
                 "william-d-ford-federal-direct-loan-program"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-08-02T20:55:41.375034",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Data and Documentation - PSS 2015-16",
-            "description": "The Private School Universe Survey (PSS) is conducted by the National Center for Education Statistics (NCES) on behalf of the U.S. Department of Education in order to collect basic information on American\r\nprivate elementary and secondary schools. PSS grew out of a proposal in 1988 to develop a private school data collection that would improve on the sporadic collection of private school data dating back to 1890 and improve on commercially available private school sampling frames. PSS was first collected in the 1989\u201390 school year, with data collections every 2 years since.",
-            "modified": "2023-08-02T16:29:23.965799",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "cf8d7fb1-bf25-454d-8248-878b0059db7a",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
+                "name": "Office of Federal Student Aid (FSA)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Under Secretary (OUS)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Secretary (OS)",
+                        "subOrganizationOf": {
+                            "@type": "org:Organization",
+                            "name": "U.S. Department of Education",
                             "subOrganizationOf": {
                                 "@type": "org:Organization",
                                 "name": "U.S. Government"
                             }
+                        }
+                    }
+                }
+            },
+            "spatial": "United States",
+            "title": "Common Origination and Disbursement System"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "description": "The Private School Universe Survey (PSS) is conducted by the National Center for Education Statistics (NCES) on behalf of the U.S. Department of Education in order to collect basic information on American\r\nprivate elementary and secondary schools. PSS grew out of a proposal in 1988 to develop a private school data collection that would improve on the sporadic collection of private school data dating back to 1890 and improve on commercially available private school sampling frames. PSS was first collected in the 1989\u201390 school year, with data collections every 2 years since.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "PSS 2015-16 SAS Data File",
                     "description": "Zip file archive containing the public use dataset for the 2017-18 Private School Universe Survey:  SAS Format",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_sas7bdat.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_sas7bdat.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "PSS 2015-16 SAS Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "PSS 2015-16 SPSS Data File",
                     "description": "Zip file archive containing the public use dataset for the 2017-18 Private School Universe Survey: SPSS format",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_sav.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_sav.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "PSS 2015-16 SPSS Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "PSS 2015-16 Text Data File",
                     "description": "Zip file archive containing the public use dataset for the 2017-18 Private School Universe Survey: Text format",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_csv.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_csv.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "PSS 2015-16 Text Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "PSS 2015-16 Restricted Use Data Files",
                     "description": "Research organizations can apply for access to more detailed restricted use files (available in SAS, SPSS and text format) through the IES Restricted Use Data License.   More information and the license application process can be found at https://nces.ed.gov/statprog/instruct.asp",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "PSS 2015-16 Restricted Use Data Files"
                 }
             ],
+            "identifier": "cf8d7fb1-bf25-454d-8248-878b0059db7a",
             "keyword": [
                 "2015-16",
                 "72752616-32cd-4680-a309-499c7848841a",
@@ -35228,90 +35218,77 @@
                 "private-school",
                 "school"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-08-02T16:29:23.965799",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 2015-16",
-            "description": "The Private School Universe Survey, 2015-16 (PSS 2015-16), is a study that is part of the Private School Universe program. PSS 2015-16 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study will be conducted using mail questionnaires, an internet response option and telephone and personal follow-up of all private schools in the United States. The PSS universe consists of a diverse population of schools. It includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 2015-16 are on the number of private schools, students, and teachers, the number of high school graduates, the length of the school year and school day.",
-            "modified": "2023-08-02T12:50:26.579259",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "33fb52ff-dcdd-47ea-89f1-16c29ca696e5",
-            "dataQuality": true,
-            "issued": "2017-04-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2015/2016",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "Office of the Secretary (OS)",
-                        "subOrganizationOf": {
-                            "@type": "org:Organization",
-                            "name": "U.S. Department of Education",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "U.S. Government"
                 }
-                        }
-                    }
-                }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "title": "Data and Documentation - PSS 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Private School Universe Survey, 2015-16 (PSS 2015-16), is a study that is part of the Private School Universe program. PSS 2015-16 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study will be conducted using mail questionnaires, an internet response option and telephone and personal follow-up of all private schools in the United States. The PSS universe consists of a diverse population of schools. It includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 2015-16 are on the number of private schools, students, and teachers, the number of high school graduates, the length of the school year and school day.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Private School Universe Survey (PSS): Restricted-Use Data for School Year 2015-16",
                     "description": "Restricted-use data for the 2015-16 Private School Universe Survey in three formats: SAS, SPSS, and text. Includes file documentation and a copy of the questionnaire.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2017159",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Private School Universe Survey (PSS): Restricted-Use Data for School Year 2015-16"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "pss1516_pu_csv.zip",
-                    "description": "2015-16 Private School Universe Survey data as a zipped CSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/codebook2015_16.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_csv.zip"
+                    "description": "2015-16 Private School Universe Survey data as a zipped CSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "pss1516_pu_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "pss1516_pu_sas7bdat.zip",
-                    "description": "2015-16 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/codebook2015_16.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_sas7bdat.zip"
+                    "description": "2015-16 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_sas7bdat.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "pss1516_pu_sas7bdat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "pss1516_pu_sav.zip",
-                    "description": "2015-16 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/codebook2015_16.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_sav.zip"
+                    "description": "2015-16 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1516_pu_sav.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "pss1516_pu_sav.zip"
                 }
             ],
+            "identifier": "33fb52ff-dcdd-47ea-89f1-16c29ca696e5",
+            "issued": "2017-04-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -35320,29 +35297,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-08-02T12:50:26.579259",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Distance Education Courses for Public Elementary and Secondary School Students, 2004-05",
-            "description": "The Distance Education Courses for Public Elementary and Secondary School Students, 2004-05 (FRSS 89), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 89 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates for technology-based distance education courses in public elementary and secondary schools. The study was mailed to public school district superintendents, who were sampled for the survey. The study's response rate was 96 percent. Key statistics produced from the study were the percent of districts and the percent of schools (by instructional level) with students enrolled in technology-based distance education courses. The number of enrollments in distance education courses (by instructional level) was also collected. The survey contained questions on the completion status of the enrollments in distance education. Districts were asked to report the technologies used to deliver distance education courses and where students accessed online distance education courses (e.g., at school or at home). The survey included questions on whether technology-based distance education was used to offer Advanced Placement (AP) and college-level courses to students. Districts with students enrolled in technology-based distance education courses were asked whether they planned to expand their distance education courses.",
-            "modified": "2023-07-28T20:41:16.872796",
-            "accessLevel": "public",
-            "identifier": "56b3fb57-ac3b-4cf2-b109-850a392adb50",
-            "dataQuality": true,
-            "issued": "2010-06-29",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2004/2005",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -35363,30 +35325,45 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2015/2016",
+            "title": "Private School Universe Survey, 2015-16"
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
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Distance Education Courses for Public Elementary and Secondary School Students, 2004-05 (FRSS 89), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 89 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates for technology-based distance education courses in public elementary and secondary schools. The study was mailed to public school district superintendents, who were sampled for the survey. The study's response rate was 96 percent. Key statistics produced from the study were the percent of districts and the percent of schools (by instructional level) with students enrolled in technology-based distance education courses. The number of enrollments in distance education courses (by instructional level) was also collected. The survey contained questions on the completion status of the enrollments in distance education. Districts were asked to report the technologies used to deliver distance education courses and where students accessed online distance education courses (e.g., at school or at home). The survey included questions on whether technology-based distance education was used to offer Advanced Placement (AP) and college-level courses to students. Districts with students enrolled in technology-based distance education courses were asked whether they planned to expand their distance education courses.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f89data.zip",
                     "description": "Distance Education Courses for Public Elementary and Secondary School Students, 2004-05 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f89data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f89data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f89data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f89sas.zip",
                     "description": "Distance Education Courses for Public Elementary and Secondary School Students, 2004-05 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f89sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f89sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f89sas.zip"
                 }
             ],
+            "identifier": "56b3fb57-ac3b-4cf2-b109-850a392adb50",
+            "issued": "2010-06-29",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "distance-education",
@@ -35398,31 +35375,14 @@
                 "school-overcrowding",
                 "secondary-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-28T20:41:16.872796",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f89doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Principal Follow-Up Survey, 2016-17",
-            "description": "The Principal Follow-Up Survey, 2016-17 (PFS 16/17) is a data collection that is part of the National Teacher and Principal Survey program; program data are available since 2017 at https://nces.ed.gov/pubsearch/licenses.asp. PFS 16/17 (https://nces.ed.gov/surveys/ntps/overview.asp?OverviewType=6) is a longitudinal follow-up to the National Teacher and Principal Survey, 2015-16 (NTPS 2015-16) data collection. PFS 16/17 determined mobility patterns of principals in the base (NTPS 2015-16) school year. The PFS 16/17 sample includes all schools whose principals completed questionnaires in NTPS 2015-16. Schools and principals were mailed the PFS questionnaire. Nonrespondents were followed-up via telephone. Key statistics produced from PFS 16/17 include the number of principals that still worked as a principal in the same school in the following school year, how many moved to become a principal in another school, how many left the principalship altogether, and from those who left the principalship, what percentage retired or sought work in another occupational field.",
-            "modified": "2023-07-28T20:41:11.699539",
-            "accessLevel": "public",
-            "identifier": "15d4cd08-f3c8-468c-8e1b-4ce9a2e69fd9",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2016/2017",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -35443,54 +35403,58 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f89doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2004/2005",
+            "title": "Distance Education Courses for Public Elementary and Secondary School Students, 2004-05"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amy Ho",
                 "hasEmail": "mailto:amy.ho@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Principal Follow-Up Survey, 2016-17 (PFS 16/17) is a data collection that is part of the National Teacher and Principal Survey program; program data are available since 2017 at https://nces.ed.gov/pubsearch/licenses.asp. PFS 16/17 (https://nces.ed.gov/surveys/ntps/overview.asp?OverviewType=6) is a longitudinal follow-up to the National Teacher and Principal Survey, 2015-16 (NTPS 2015-16) data collection. PFS 16/17 determined mobility patterns of principals in the base (NTPS 2015-16) school year. The PFS 16/17 sample includes all schools whose principals completed questionnaires in NTPS 2015-16. Schools and principals were mailed the PFS questionnaire. Nonrespondents were followed-up via telephone. Key statistics produced from PFS 16/17 include the number of principals that still worked as a principal in the same school in the following school year, how many moved to become a principal in another school, how many left the principalship altogether, and from those who left the principalship, what percentage retired or sought work in another occupational field.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Principal Attrition and Mobility: Results From the 2016-17 Principal Follow-up Survey",
                     "description": "This report presents selected findings from the Public School Principal Status Data File of the 2016-17 Principal Follow-up Survey (PFS)",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2018066",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Principal Attrition and Mobility: Results From the 2016-17 Principal Follow-up Survey"
                 }
             ],
+            "identifier": "15d4cd08-f3c8-468c-8e1b-4ce9a2e69fd9",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "principal-attrition-rates",
                 "principal-retention",
                 "principal-turnover"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-28T20:41:11.699539",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Charter Schools, 2017-18",
-            "description": "EDFacts Charter Schools 2017-18 (EDFacts CHRTR:2017-18) is one of 17 \u201ctopics\"identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts CHRTR:2017-18 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about the status of charter school as an LEA for purposes of federal programs at school, LEA, and state levels. EDFacts CHRTR:2017-18 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts CHRTR:2017-18 are from 2 data groups with information on Charter-School status and Charter-School LEA status. For the purposes of this system, data groups are referred to as variables, as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-26T19:18:09.260230",
-            "accessLevel": "public",
-            "identifier": "47c11cc0-1ec4-46d7-a969-6924d12cefe4",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/2014",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Innovation and Improvement (OII)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Elementary and Secondary Education (OESE)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -35505,12 +35469,26 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2016/2017",
+            "title": "Principal Follow-Up Survey, 2016-17"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Charter Schools 2017-18 (EDFacts CHRTR:2017-18) is one of 17 \u201ctopics\"identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts CHRTR:2017-18 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about the status of charter school as an LEA for purposes of federal programs at school, LEA, and state levels. EDFacts CHRTR:2017-18 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts CHRTR:2017-18 are from 2 data groups with information on Charter-School status and Charter-School LEA status. For the purposes of this system, data groups are referred to as variables, as a result of the structure and format of EDFacts' data.",
+            "identifier": "47c11cc0-1ec4-46d7-a969-6924d12cefe4",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "charter-schools",
@@ -35522,29 +35500,18 @@
                 "state-education-agencies-seas",
                 "states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-26T19:18:09.260230",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Assessment, 2011-12",
-            "description": "EDFacts Assessment, 2011-12 (EDFacts ASSMT:2011-12) is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study). EDFacts ASSMT:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about students participation in and performance on academic assessments in Reading/Language Arts, Science, and Mathematics in elementary and secondary education at the school, LEA, and SEA levels. EDFacts ASSMT:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal, and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts ASSMT:2011-12 are from eight (8) data groups with information on Academic Achievement, Academic Achievement-Flexibility, Assessment Participation, and Assessment Participation-Flexibility in Mathematics and Reading/Language Arts. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts data.",
-            "modified": "2023-07-26T18:17:40.285458",
-            "accessLevel": "public",
-            "identifier": "b1f7eaaf-acda-40b6-ab38-e48df1f0fcf8",
-            "dataQuality": true,
-            "issued": "2013-06-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Innovation and Improvement (OII)",
+                "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of Elementary and Secondary Education (OESE)",
                     "subOrganizationOf": {
@@ -35559,55 +35526,70 @@
                             }
                         }
                     }
+                }
+            },
+            "spatial": "United States",
+            "temporal": "2013/2014",
+            "title": "EDFacts Charter Schools, 2017-18"
         },
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
+            "description": "EDFacts Assessment, 2011-12 (EDFacts ASSMT:2011-12) is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study). EDFacts ASSMT:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about students participation in and performance on academic assessments in Reading/Language Arts, Science, and Mathematics in elementary and secondary education at the school, LEA, and SEA levels. EDFacts ASSMT:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal, and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts ASSMT:2011-12 are from eight (8) data groups with information on Academic Achievement, Academic Achievement-Flexibility, Assessment Participation, and Assessment Participation-Flexibility in Mathematics and Reading/Language Arts. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Assessment 2011-12 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "userssharedsdfachvmntrsltsstateassmtsmathssy201112.csv",
                     "description": "EDFacts Assessment 2011-12 mathematics data by school in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/cee9d558-313f-41f7-8955-1d6e4df3a2dc/resource/0f696b5b-129c-4a83-93af-662f5f8162f4/download/userssharedsdfachvmntrsltsstateassmtsmathssy201112.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/cee9d558-313f-41f7-8955-1d6e4df3a2dc/resource/0f696b5b-129c-4a83-93af-662f5f8162f4/download/userssharedsdfachvmntrsltsstateassmtsmathssy201112.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfachvmntrsltsstateassmtsmathssy201112.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "userssharedsdfachvmntrsltsstateassmtsrlasy201112.csv",
                     "description": "EDFacts Assessment 2011-12 reading data by school in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/e1f06719-f437-431c-8a52-d7706b7791aa/resource/5a238416-a57d-4c73-8c3c-e3bd1d0d7cb7/download/userssharedsdfachvmntrsltsstateassmtsrlasy201112.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/e1f06719-f437-431c-8a52-d7706b7791aa/resource/5a238416-a57d-4c73-8c3c-e3bd1d0d7cb7/download/userssharedsdfachvmntrsltsstateassmtsrlasy201112.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfachvmntrsltsstateassmtsrlasy201112.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "userssharedsdflealvlachvmntrsltsforstateassmntsinmathssy201112.csv",
                     "description": "EDFacts Assessment 2011-12 mathematics data by district in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/53266ad7-8fc0-4929-b4be-fb93772bd441/resource/b4e7f148-3afc-4782-84a3-dfaca3156e8b/download/userssharedsdflealvlachvmntrsltsforstateassmntsinmathssy201112.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/53266ad7-8fc0-4929-b4be-fb93772bd441/resource/b4e7f148-3afc-4782-84a3-dfaca3156e8b/download/userssharedsdflealvlachvmntrsltsforstateassmntsinmathssy201112.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdflealvlachvmntrsltsforstateassmntsinmathssy201112.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "userssharedsdfleaachvrsltsassessrlasy201112.csv",
                     "description": "EDFacts Assessment 2011-12 reading data by district in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/e4b3ce38-c0e2-45c1-97b4-73f6a467e801/resource/7c9a1737-5501-492a-8d23-99e1501e9e0b/download/userssharedsdfleaachvrsltsassessrlasy201112.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/e4b3ce38-c0e2-45c1-97b4-73f6a467e801/resource/7c9a1737-5501-492a-8d23-99e1501e9e0b/download/userssharedsdfleaachvrsltsassessrlasy201112.csv",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfleaachvrsltsassessrlasy201112.csv"
                 }
             ],
+            "identifier": "b1f7eaaf-acda-40b6-ab38-e48df1f0fcf8",
+            "issued": "2013-06-01",
             "keyword": [
                 "achievement",
                 "assessment",
@@ -35637,36 +35619,14 @@
                 "students",
                 "students-with-disabilities"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm",
-                "https://inventory.data.gov/dataset/e4b3ce38-c0e2-45c1-97b4-73f6a467e801/resource/a475ad70-5914-49fe-a969-6c9aa3d12018/download/ca67g5i2edfactssy1112stateassessmentspublicfiledocumentation.doc",
-                "https://inventory.data.gov/dataset/cee9d558-313f-41f7-8955-1d6e4df3a2dc/resource/7ac10234-8f57-4777-9776-bb6b082bd798/download/3yp32q8tedfactssy1112stateassessmentspublicfiledocumentation.doc",
-                "https://inventory.data.gov/dataset/e1f06719-f437-431c-8a52-d7706b7791aa/resource/5b9828f5-b5da-4f51-bce5-d3757e6788d0/download/6dpmi24pedfactssy1112stateassessmentspublicfiledocumentation.doc",
-                "https://inventory.data.gov/dataset/53266ad7-8fc0-4929-b4be-fb93772bd441/resource/7ae017d2-1c88-4791-8397-ff4dc2d3b49a/download/kebbrsteedfactssy1112stateassessmentspublicfiledocumentation.doc"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Accountability, 2011-12",
-            "description": "EDFacts Accountability, 2011-12 (EDFacts ACCNT:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts ACCNT:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about school or district status according to the accountability provisions of ESEA at the school, LEA, and state levels. EDFacts ACCNT:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts ACCNT:2011-12 are from 20 data groups with information on Alternate Approach Status, AYP Status, Corrective Actions, Elementary/Middle Additional Indicator Status, High School Graduation Rate Indicator Status, Mathematics Participation Status, Reading/Language Arts Participation Status, AMO Mathematics Status, AMO Reading/Language Arts Status, Improvement Status, Restructuring Actions, Reconstituted Status, School Improvement Funds Allocation, School Improvement Funds Status, Intervention, Mathematics Participation Status- Flexibility, Reading/language Arts Participation Status- Flexibility, AMO mathematics status - Flexibility, AMO reading/language arts status- Flexibility, and High school graduation rate indicator status- Flexibility. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-26T18:14:26.339992",
-            "accessLevel": "public",
-            "identifier": "4632ca75-f6e8-4d08-8d4a-5b10be23dd79",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
+            "modified": "2023-07-26T18:17:40.285458",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Elementary and Secondary Education (OESE)",
@@ -35683,22 +35643,44 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm",
+                "https://inventory.data.gov/dataset/e4b3ce38-c0e2-45c1-97b4-73f6a467e801/resource/a475ad70-5914-49fe-a969-6c9aa3d12018/download/ca67g5i2edfactssy1112stateassessmentspublicfiledocumentation.doc",
+                "https://inventory.data.gov/dataset/cee9d558-313f-41f7-8955-1d6e4df3a2dc/resource/7ac10234-8f57-4777-9776-bb6b082bd798/download/3yp32q8tedfactssy1112stateassessmentspublicfiledocumentation.doc",
+                "https://inventory.data.gov/dataset/e1f06719-f437-431c-8a52-d7706b7791aa/resource/5b9828f5-b5da-4f51-bce5-d3757e6788d0/download/6dpmi24pedfactssy1112stateassessmentspublicfiledocumentation.doc",
+                "https://inventory.data.gov/dataset/53266ad7-8fc0-4929-b4be-fb93772bd441/resource/7ae017d2-1c88-4791-8397-ff4dc2d3b49a/download/kebbrsteedfactssy1112stateassessmentspublicfiledocumentation.doc"
+            ],
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "EDFacts Assessment, 2011-12"
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
+            "description": "EDFacts Accountability, 2011-12 (EDFacts ACCNT:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts ACCNT:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about school or district status according to the accountability provisions of ESEA at the school, LEA, and state levels. EDFacts ACCNT:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts ACCNT:2011-12 are from 20 data groups with information on Alternate Approach Status, AYP Status, Corrective Actions, Elementary/Middle Additional Indicator Status, High School Graduation Rate Indicator Status, Mathematics Participation Status, Reading/Language Arts Participation Status, AMO Mathematics Status, AMO Reading/Language Arts Status, Improvement Status, Restructuring Actions, Reconstituted Status, School Improvement Funds Allocation, School Improvement Funds Status, Intervention, Mathematics Participation Status- Flexibility, Reading/language Arts Participation Status- Flexibility, AMO mathematics status - Flexibility, AMO reading/language arts status- Flexibility, and High school graduation rate indicator status- Flexibility. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Accountability 2011-12 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "4632ca75-f6e8-4d08-8d4a-5b10be23dd79",
+            "issued": "2013-06-01",
             "keyword": [
                 "accountability",
                 "adequate-yearly-progress",
@@ -35729,31 +35711,14 @@
                 "sig",
                 "status"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Accountability, 2010-11",
-            "description": "EDFacts Accountability, 2010-11 (EDFacts ACCNT:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts ACCNT:2010-11 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about school or district status according to the accountability provisions of ESEA at the school, LEA, and state levels. EDFacts ACCNT:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts ACCNT:2010-11 are from 20 data groups with information on Alternate Approach Status, AYP Status, Corrective Actions, Elementary/Middle Additional Indicator Status, High School Graduation Rate Indicator Status, Mathematics Participation Status, Reading/Language Arts Participation Status, AMO Mathematics Status, AMO Reading/Language Arts Status, Improvement Status, Restructuring Actions, Reconstituted Status, School Improvement Funds Allocation, School Improvement Funds Status, Intervention, Mathematics Participation Status- Flexibility, Reading/language Arts Participation Status- Flexibility, AMO mathematics status - Flexibility, AMO reading/language arts status- Flexibility, and High school graduation rate indicator status- Flexibility. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-26T18:13:53.615887",
-            "accessLevel": "public",
-            "identifier": "f162a76b-37b1-4feb-9084-d4e74ea65b25",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
+            "modified": "2023-07-26T18:14:26.339992",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Elementary and Secondary Education (OESE)",
@@ -35770,22 +35735,39 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "EDFacts Accountability, 2011-12"
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
+            "description": "EDFacts Accountability, 2010-11 (EDFacts ACCNT:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts ACCNT:2010-11 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about school or district status according to the accountability provisions of ESEA at the school, LEA, and state levels. EDFacts ACCNT:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts ACCNT:2010-11 are from 20 data groups with information on Alternate Approach Status, AYP Status, Corrective Actions, Elementary/Middle Additional Indicator Status, High School Graduation Rate Indicator Status, Mathematics Participation Status, Reading/Language Arts Participation Status, AMO Mathematics Status, AMO Reading/Language Arts Status, Improvement Status, Restructuring Actions, Reconstituted Status, School Improvement Funds Allocation, School Improvement Funds Status, Intervention, Mathematics Participation Status- Flexibility, Reading/language Arts Participation Status- Flexibility, AMO mathematics status - Flexibility, AMO reading/language arts status- Flexibility, and High school graduation rate indicator status- Flexibility. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Accountability 2010-11 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "f162a76b-37b1-4feb-9084-d4e74ea65b25",
             "keyword": [
                 "accountability",
                 "adequate-yearly-progress",
@@ -35816,56 +35798,64 @@
                 "sig",
                 "status"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Graduates and Dropouts, 2011-12",
-            "description": "EDFacts Graduates and Dropouts, 2011-12 (EDFacts GD:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts GD:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2011-12 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:13:16.725095",
-            "accessLevel": "public",
-            "identifier": "b555b8a5-58be-4066-9695-168ace184d52",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
+            "modified": "2023-07-26T18:13:53.615887",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Elementary and Secondary Education (OESE)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Secretary (OS)",
+                    "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "U.S. Department of Education",
                         "subOrganizationOf": {
                             "@type": "org:Organization",
                             "name": "U.S. Government"
                         }
+                    }
+                }
+            },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "EDFacts Accountability, 2010-11"
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
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Graduates and Dropouts, 2011-12 (EDFacts GD:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts GD:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2011-12 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Graduates and Dropouts 2011-12 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "b555b8a5-58be-4066-9695-168ace184d52",
+            "issued": "2013-06-01",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "ccd",
@@ -35886,31 +35876,14 @@
                 "sea",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Graduates and Dropouts, 2010-11",
-            "description": "EDFacts Graduates and Dropouts, 2010-11 (EDFacts GD:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts GD:2010-11 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2010-11 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:12:44.168096",
-            "accessLevel": "public",
-            "identifier": "f93b1f9d-c3e0-4e76-8fc6-6053b5dc68e1",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
+            "modified": "2023-07-20T22:13:16.725095",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
@@ -35919,36 +35892,53 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "EDFacts Graduates and Dropouts, 2011-12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Graduates and Dropouts, 2010-11 (EDFacts GD:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts GD:2010-11 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2010-11 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Graduates and Dropouts 2010-11 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Adjusted_Cohort_Grdtn_Rates_LEA_SY_2010-11",
                     "description": "This dataset contains district level information on the four-year adjusted cohort graduation rates calculated by state education agencies in accordance with U.S. Department of Education...",
                     "downloadURL": "https://inventory.data.gov/dataset/adjusted-cohort-graduation-rates-at-the-lea-level-school-year-2010-11/resource/9543c4f7-7a60-464a-be95-57675b03fad8",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Adjusted_Cohort_Grdtn_Rates_LEA_SY_2010-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Adjusted_Cohort_Grdtn_Rates_SL_SY_2010-11",
                     "description": "Note: This dataset was updated on September 18, 2013 to reflect data that states resubmitted to address data quality issues. This dataset contains school level information on the...",
                     "downloadURL": "https://inventory.data.gov/dataset/adjusted-cohort-graduation-rates-at-the-school-level-school-year-2010-11/resource/566c5a0c-0a44-4ada-af54-7b3cd826d306",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Adjusted_Cohort_Grdtn_Rates_SL_SY_2010-11"
                 }
             ],
+            "identifier": "f93b1f9d-c3e0-4e76-8fc6-6053b5dc68e1",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "ccd",
@@ -35969,32 +35959,14 @@
                 "sea",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Graduates and Dropouts, 2012-13",
-            "description": "EDFacts Graduates and Dropouts, 2012-13 (EDFacts GD:2012-13) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2012-13 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2012-\u015313 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2012-13 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:12:08.725780",
-            "accessLevel": "public",
-            "identifier": "45e3698c-9952-41ba-bbcb-eae8fd339013",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/2014",
+            "modified": "2023-07-20T22:12:44.168096",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
@@ -36003,22 +35975,40 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "EDFacts Graduates and Dropouts, 2010-11"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Graduates and Dropouts, 2012-13 (EDFacts GD:2012-13) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2012-13 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2012-\u015313 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2012-13 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Graduates and Dropouts 2012-13 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "45e3698c-9952-41ba-bbcb-eae8fd339013",
+            "issued": "2013-06-01",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "ccd",
@@ -36039,32 +36029,14 @@
                 "sea",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Graduates and Dropouts, 2013-14",
-            "description": "EDFacts Graduates and Dropouts, 2013-14 (EDFacts GD:2013-14) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2013-14 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2013-14 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2013-14 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:10:47.346771",
-            "accessLevel": "public",
-            "identifier": "10c97e6f-655f-4c2c-8ec3-27ee52088e27",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2014/2015",
+            "modified": "2023-07-20T22:12:08.725780",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
@@ -36073,22 +36045,40 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2013/2014",
+            "title": "EDFacts Graduates and Dropouts, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Graduates and Dropouts, 2013-14 (EDFacts GD:2013-14) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2013-14 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2013-14 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2013-14 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Graduates and Dropouts 2013-14 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "10c97e6f-655f-4c2c-8ec3-27ee52088e27",
+            "issued": "2013-06-01",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "ccd",
@@ -36109,32 +36099,14 @@
                 "sea",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Graduates and Dropouts, 2014-15",
-            "description": "EDFacts Graduates and Dropouts, 2014-15 (EDFacts GD:2014-15) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2014-15 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2014-15 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2014-15 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:09:26.648837",
-            "accessLevel": "public",
-            "identifier": "79a0a87e-de11-4e42-b346-45d2dcf66d7e",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2015/2016",
+            "modified": "2023-07-20T22:10:47.346771",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
@@ -36143,22 +36115,40 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2014/2015",
+            "title": "EDFacts Graduates and Dropouts, 2013-14"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Graduates and Dropouts, 2014-15 (EDFacts GD:2014-15) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2014-15 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2014-15 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2014-15 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Graduates and Dropouts 2014-15 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "79a0a87e-de11-4e42-b346-45d2dcf66d7e",
+            "issued": "2013-06-01",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "ccd",
@@ -36179,32 +36169,14 @@
                 "sea",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Graduates and Dropouts, 2015-16",
-            "description": "EDFacts Graduates and Dropouts, 2015-16 (EDFacts GD:2015-16) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2015-16 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2015-16 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2015-16 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:08:13.961435",
-            "accessLevel": "public",
-            "identifier": "72399dad-fc4d-458d-9821-f0bc7cc04ecc",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2015/2016",
+            "modified": "2023-07-20T22:09:26.648837",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
@@ -36213,22 +36185,40 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2015/2016",
+            "title": "EDFacts Graduates and Dropouts, 2014-15"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Graduates and Dropouts, 2015-16 (EDFacts GD:2015-16) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2015-16 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2015-16 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2015-16 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Graduates and Dropouts 2015-16 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "72399dad-fc4d-458d-9821-f0bc7cc04ecc",
+            "issued": "2013-06-01",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "ccd",
@@ -36249,32 +36239,14 @@
                 "sea",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-20T22:08:13.961435",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Graduates and Dropouts, 2016-17",
-            "description": "EDFacts Graduates and Dropouts, 2016-17 (EDFacts GD:2016-17) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2016-17 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2016-17 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2016-17 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:07:04.021480",
-            "accessLevel": "public",
-            "identifier": "a0a54ec7-4a22-41df-a469-7140f34de663",
-            "dataQuality": true,
-            "issued": "2013-06-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2015/2016",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
@@ -36283,22 +36255,40 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2015/2016",
+            "title": "EDFacts Graduates and Dropouts, 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Graduates and Dropouts, 2016-17 (EDFacts GD:2016-17) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2016-17 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2016-17 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2016-17 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Graduates and Dropouts 2016-17 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "a0a54ec7-4a22-41df-a469-7140f34de663",
+            "issued": "2013-06-01",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "ccd",
@@ -36319,32 +36309,14 @@
                 "sea",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Graduates and Dropouts, 2017-18",
-            "description": "EDFacts Graduates and Dropouts, 2017-18 (EDFacts GD:2017-18) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2017-18 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2017-18 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2017-18 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as variables, as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:05:44.584242",
-            "accessLevel": "public",
-            "identifier": "6b45fc33-cf88-4f5e-a610-f0937e26c8d6",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2015/2016",
+            "modified": "2023-07-20T22:07:04.021480",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
@@ -36353,22 +36325,40 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2015/2016",
+            "title": "EDFacts Graduates and Dropouts, 2016-17"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Graduates and Dropouts, 2017-18 (EDFacts GD:2017-18) is one of 17 \u201ctopics\" identified in the EDFacts documentation (in this database, each \u201ctopic\" is entered as a separate study). EDFacts GD:2017-18 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student who graduate or receive a certificate of completion from secondary education or students who dropped out of secondary education at the school, LEA, and state levels. EDFacts GD:2017-18 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts GD:2017-18 are from 6 data groups with information on Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Graduation Rate; Regulatory Cohort Graduation Rate (Four, Five, and Six Year)-Student Counts; Graduation Rate; Graduates/Completers; Regulatory Cohort Graduation Rate-Flex; and Regulatory Cohort Graduation Rate Student Counts-Flex. For the purposes of this system, data groups are referred to as variables, as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Graduates and Dropouts 2017-18 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "6b45fc33-cf88-4f5e-a610-f0937e26c8d6",
+            "issued": "2013-06-01",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "ccd",
@@ -36389,63 +36379,55 @@
                 "sea",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Homeless, Neglected, or Delinquent, 2010-11",
-            "description": "EDFacts Homeless, Neglected, or Delinquent, 2010-11 (EDFacts HND:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts HND:2010-11 (ed.gov/about/inits/ed/edfacts/eden/non-xml/c175-8-0.doc) annually collects cross-sectional data from states about homeless students and students who are participating in programs for neglected or delinquent students (\"N or D\") under Title I, Part D of the Elementary and Secondary Education Act (ESEA), as amended. EDFacts HND:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submissions by states in mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the states. Key statistics produced from EDFacts HND:2010-11 are from 5 data groups with information on Homeless Served (McKinney-Vento), Homeless Students Enrolled, N or D-Academic Achievement, N or D-Long Term Students Served, and N or D-Program Participation. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:03:16.016073",
-            "accessLevel": "public",
-            "identifier": "1e2fca11-630f-4b06-a66c-5e0d78dc57a9",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
+            "modified": "2023-07-20T22:05:44.584242",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Elementary and Secondary Education (OESE)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Secretary (OS)",
-                    "subOrganizationOf": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "U.S. Government"
                 }
-                    }
-                }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2015/2016",
+            "title": "EDFacts Graduates and Dropouts, 2017-18"
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
+            "description": "EDFacts Homeless, Neglected, or Delinquent, 2010-11 (EDFacts HND:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts HND:2010-11 (ed.gov/about/inits/ed/edfacts/eden/non-xml/c175-8-0.doc) annually collects cross-sectional data from states about homeless students and students who are participating in programs for neglected or delinquent students (\"N or D\") under Title I, Part D of the Elementary and Secondary Education Act (ESEA), as amended. EDFacts HND:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submissions by states in mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the states. Key statistics produced from EDFacts HND:2010-11 are from 5 data groups with information on Homeless Served (McKinney-Vento), Homeless Students Enrolled, N or D-Academic Achievement, N or D-Long Term Students Served, and N or D-Program Participation. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Homeless, Neglected, or Delinquent 2010-11 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "1e2fca11-630f-4b06-a66c-5e0d78dc57a9",
             "keyword": [
                 "academic-subject",
                 "age",
@@ -36470,32 +36452,14 @@
                 "sex",
                 "student"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Homeless, Neglected, or Delinquent, 2016-17",
-            "description": "EDFacts Homeless, Neglected, or Delinquent, 2016-17 (EDFacts HND:2016-17) is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study). EDFacts HND:2016-17 (https://www2.ed.gov/about/inits/ed/edfacts/index.html) annually collects cross- sectional data from states about homeless students and students who are participating in programs for neglected or delinquent students (N or D) under Title I, Part D of the Elementary and Secondary Education Act (ESEA), as amended. EDFacts HND:2016-17 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submissions by states in mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the states. Key statistics produced from EDFacts HND:2016-17 are from 5 data groups with information on Homeless Served (McKinney-Vento), Homeless Students Enrolled, N or D-Academic Achievement, N or D-Long Term Students Served, and N or D-Program Participation. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts data.",
-            "modified": "2023-07-20T22:02:30.107563",
-            "accessLevel": "public",
-            "identifier": "55ac2d1e-c88b-4f83-b0fc-5a7592ac743f",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2017/2018",
+            "modified": "2023-07-20T22:03:16.016073",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Elementary and Secondary Education (OESE)",
@@ -36512,22 +36476,40 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "EDFacts Homeless, Neglected, or Delinquent, 2010-11"
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
+            "description": "EDFacts Homeless, Neglected, or Delinquent, 2016-17 (EDFacts HND:2016-17) is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study). EDFacts HND:2016-17 (https://www2.ed.gov/about/inits/ed/edfacts/index.html) annually collects cross- sectional data from states about homeless students and students who are participating in programs for neglected or delinquent students (N or D) under Title I, Part D of the Elementary and Secondary Education Act (ESEA), as amended. EDFacts HND:2016-17 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submissions by states in mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the states. Key statistics produced from EDFacts HND:2016-17 are from 5 data groups with information on Homeless Served (McKinney-Vento), Homeless Students Enrolled, N or D-Academic Achievement, N or D-Long Term Students Served, and N or D-Program Participation. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Homeless, Neglected, or Delinquent 2016-17 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "55ac2d1e-c88b-4f83-b0fc-5a7592ac743f",
+            "issued": "2013-06-01",
             "keyword": [
                 "academic-subjects",
                 "age",
@@ -36552,32 +36534,14 @@
                 "students",
                 "subgroups"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Homeless, Neglected, or Delinquent, 2011-12",
-            "description": "EDFacts Homeless, Neglected, or Delinquent, 2011-12 (EDFacts HND:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts HND:2011-12 (ed.gov/about/inits/ed/edfacts/eden/non-xml/c175-8-0.doc) annually collects cross-sectional data from states about homeless students and students who are participating in programs for neglected or delinquent students (\"N or D\") under Title I, Part D of the Elementary and Secondary Education Act (ESEA), as amended. EDFacts HND:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submissions by states in mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the states. Key statistics produced from EDFacts HND:2011-12 are from 5 data groups with information on Homeless Served (McKinney-Vento), Homeless Students Enrolled, N or D-Academic Achievement, N or D-Long Term Students Served, and N or D-Program Participation. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:00:59.280523",
-            "accessLevel": "public",
-            "identifier": "572310f8-c376-4024-8b91-808dc24d530b",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
+            "modified": "2023-07-20T22:02:30.107563",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Elementary and Secondary Education (OESE)",
@@ -36594,22 +36558,40 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2017/2018",
+            "title": "EDFacts Homeless, Neglected, or Delinquent, 2016-17"
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
+            "description": "EDFacts Homeless, Neglected, or Delinquent, 2011-12 (EDFacts HND:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts HND:2011-12 (ed.gov/about/inits/ed/edfacts/eden/non-xml/c175-8-0.doc) annually collects cross-sectional data from states about homeless students and students who are participating in programs for neglected or delinquent students (\"N or D\") under Title I, Part D of the Elementary and Secondary Education Act (ESEA), as amended. EDFacts HND:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submissions by states in mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the states. Key statistics produced from EDFacts HND:2011-12 are from 5 data groups with information on Homeless Served (McKinney-Vento), Homeless Students Enrolled, N or D-Academic Achievement, N or D-Long Term Students Served, and N or D-Program Participation. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Homeless, Neglected, or Delinquent 2011-12 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "572310f8-c376-4024-8b91-808dc24d530b",
+            "issued": "2013-06-01",
             "keyword": [
                 "academic-subject",
                 "age",
@@ -36634,36 +36616,15 @@
                 "sex",
                 "student"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Migrant Education Program, 2011-12",
-            "description": "EDFacts Migrant Education Program, 2011-12 (EDFacts MEP:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts MEP:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, LEA, and state levels. EDFacts MEP:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2011-12 are from 10 data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served -Summer/Intersession, MEP Students Served - 12 - Month, MEP Students Served - Regular School Year, MEP Students Served - Summer/Intersession, Migrant Students Eligible - 12 - Month, and Migrant Students Eligible - Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T22:00:22.224106",
-            "accessLevel": "public",
-            "identifier": "a5d612bd-92cc-4cdc-b0ff-503b2477dab5",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
+            "modified": "2023-07-20T22:00:59.280523",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Migrant Education (MEP)",
-                "subOrganizationOf": {
                 "@type": "org:Organization",
                 "name": "Office of Elementary and Secondary Education (OESE)",
                 "subOrganizationOf": {
@@ -36678,24 +36639,41 @@
                         }
                     }
                 }
-                }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "EDFacts Homeless, Neglected, or Delinquent, 2011-12"
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
+            "description": "EDFacts Migrant Education Program, 2011-12 (EDFacts MEP:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts MEP:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, LEA, and state levels. EDFacts MEP:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2011-12 are from 10 data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served -Summer/Intersession, MEP Students Served - 12 - Month, MEP Students Served - Regular School Year, MEP Students Served - Summer/Intersession, Migrant Students Eligible - 12 - Month, and Migrant Students Eligible - Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Migrant Education Program 2011-12 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "a5d612bd-92cc-4cdc-b0ff-503b2477dab5",
+            "issued": "2013-06-01",
             "keyword": [
                 "252a4986-4fc5-46d1-ae78-5c89bfb43b9a",
                 "adult-education",
@@ -36715,32 +36693,14 @@
                 "students",
                 "title-i"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Migrant Education Program, 2017-18",
-            "description": "EDFacts Migrant Education Program, 2017-18 (EDFacts MEP:2017-18) is one of 17\u201ctopics identified in the EDFacts documentation (in this database, each \u201ctopic' is entered as a separate study). EDFacts MEP:2017-18 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, LEA, and state levels. EDFacts MEP:2017-18 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2017-18 are from 10 data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served (Summer/Intersession, MEP Students Served Month, MEP Students Served  Regular School Year, MEP Students Served  Summer/Intersession, Migrant Students Eligible 12  Month, and Migrant Students Eligible \r\n Regular School Year. For the purposes of this system, data groups are referred to as variables, as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-07-20T00:06:06.380613",
-            "accessLevel": "public",
-            "identifier": "b07d4838-b47a-4765-815f-3ccb0a763c5a",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2018/2019",
+            "modified": "2023-07-20T22:00:22.224106",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Migrant Education (MEP)",
@@ -36761,22 +36721,40 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "EDFacts Migrant Education Program, 2011-12"
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
+            "description": "EDFacts Migrant Education Program, 2017-18 (EDFacts MEP:2017-18) is one of 17\u201ctopics identified in the EDFacts documentation (in this database, each \u201ctopic' is entered as a separate study). EDFacts MEP:2017-18 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, LEA, and state levels. EDFacts MEP:2017-18 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2017-18 are from 10 data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served (Summer/Intersession, MEP Students Served Month, MEP Students Served  Regular School Year, MEP Students Served  Summer/Intersession, Migrant Students Eligible 12  Month, and Migrant Students Eligible \r\n Regular School Year. For the purposes of this system, data groups are referred to as variables, as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Migrant Education Program 2017-18 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "b07d4838-b47a-4765-815f-3ccb0a763c5a",
+            "issued": "2013-06-01",
             "keyword": [
                 "252a4986-4fc5-46d1-ae78-5c89bfb43b9a",
                 "adult-education",
@@ -36796,36 +36774,20 @@
                 "students",
                 "title-i"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Postsecondary Education Participants System",
-            "description": "The Postsecondary Education Participants System (PEPS) is the Office of Federal Student Aid (FSA) management information system of all organizations that have a role in administering student financial aid and other Higher Education Act programs. PEPS maintains eligibility, certification, demographic, financial, review, audit, and default rate data about schools, lenders, and guarantors participating in the Title IV programs.",
-            "modified": "2023-07-19T23:55:59.596437",
-            "accessLevel": "public",
-            "identifier": "d5be6ee5-3a1f-43ef-8250-b9880cfd82d6",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-20T00:06:06.380613",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Federal Student Aid (FSA)",
+                "name": "Office of Migrant Education (MEP)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Office of Elementary and Secondary Education (OESE)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -36840,22 +36802,39 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2018/2019",
+            "title": "EDFacts Migrant Education Program, 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michele Brown",
                 "hasEmail": "mailto:michele.brown@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Postsecondary Education Participants System (PEPS) is the Office of Federal Student Aid (FSA) management information system of all organizations that have a role in administering student financial aid and other Higher Education Act programs. PEPS maintains eligibility, certification, demographic, financial, review, audit, and default rate data about schools, lenders, and guarantors participating in the Title IV programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "closedschoolsearch.xlsx",
                     "description": "Closed School Search File",
-                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/PEPS/docs/closedschoolsearch.xlsx"
+                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/PEPS/docs/closedschoolsearch.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "closedschoolsearch.xlsx"
                 }
             ],
+            "identifier": "d5be6ee5-3a1f-43ef-8250-b9880cfd82d6",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "data-system",
@@ -36879,29 +36858,14 @@
                 "teacher-education-assistance-for-college-and-higher-education-grant-program",
                 "william-d-ford-direct-student-loan-program"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T23:55:59.596437",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Free Application for Federal Student Aid, 2011-12",
-            "description": "The Free Application for Federal Student Aid, 2011-12 (FAFSA 2011-12), is part of the Free Application for Federal Student Aid (FAFSA) program; program data is available since 2006-07 at <https://studentaid.ed.gov/sa/about/data-center/student/application-volume/>. FAFSA 2011-12 (https://studentaid.ed.gov/) is a universe data collection of eligible incoming postsecondary education students, along with a subset of eligible continuing postsecondary education students, that collects financial information to determine the need and eligibility for financial assistance during postsecondary education. FAFSA 2011-12 applications are accepted via web and paper submission. Citizen and specified noncitizen students demonstrating financial need and planning to attend eligible degree or certificate programs in the 50 United States, the District of Columbia, Puerto Rico, and the outlying areas as regular students are eligible to apply for FAFSA 2011-12. FAFSA 2011-12 resulted in an expected family contribution (EFC) for each applying student. Statistics produced from FAFSA 2011-12 include application volumes by postsecondary school, state of legal residence, and completion by high school; and recipient and volume data by program for each school participating in Title IV programs.",
-            "modified": "2023-07-19T23:16:57.927309",
-            "accessLevel": "public",
-            "identifier": "57838400-c7b3-42d2-ba4f-d91e9f2ae6c6",
-            "dataQuality": true,
-            "issued": "2012-06-30",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2011-08-03/pdf/2011-19607.pdf",
-            "temporal": "2011/2012",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Federal Student Aid (FSA)",
@@ -36922,117 +36886,130 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Postsecondary Education Participants System"
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
+            "description": "The Free Application for Federal Student Aid, 2011-12 (FAFSA 2011-12), is part of the Free Application for Federal Student Aid (FAFSA) program; program data is available since 2006-07 at <https://studentaid.ed.gov/sa/about/data-center/student/application-volume/>. FAFSA 2011-12 (https://studentaid.ed.gov/) is a universe data collection of eligible incoming postsecondary education students, along with a subset of eligible continuing postsecondary education students, that collects financial information to determine the need and eligibility for financial assistance during postsecondary education. FAFSA 2011-12 applications are accepted via web and paper submission. Citizen and specified noncitizen students demonstrating financial need and planning to attend eligible degree or certificate programs in the 50 United States, the District of Columbia, Puerto Rico, and the outlying areas as regular students are eligible to apply for FAFSA 2011-12. FAFSA 2011-12 resulted in an expected family contribution (EFC) for each applying student. Statistics produced from FAFSA 2011-12 include application volumes by postsecondary school, state of legal residence, and completion by high school; and recipient and volume data by program for each school participating in Title IV programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20112012Q1.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 1 data (01/01/11-03/31/11) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20112012Q1.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20112012Q1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20112012Q1.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20112012Q2.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 2 data (04/01/11-06/30/11) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20112012Q2.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20112012Q2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20112012Q2.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20112012Qtr3.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 3 data (07/01/11-09/30/11) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20112012Qtr3.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20112012Qtr3.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20112012Qtr3.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20112012Qtr4.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 4 data (10/01/11-12/31/11) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20112012Qtr4.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20112012Qtr4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20112012Qtr4.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20112012Qtr5.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 5 data (01/01/12-03/31/12) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20112012Qtr5.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20112012Qtr5.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20112012Qtr5.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2011_12App_Data_by_School_Q6.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 6 data (04/01/12-06/30/12) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2011_12App_Data_by_School_Q6.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2011_12App_Data_by_School_Q6.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2011_12App_Data_by_School_Q6.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabyState20112012Q1.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 1 data (01/01/11-03/31/11) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabyState20112012Q1.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabyState20112012Q1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabyState20112012Q1.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabyState20112012Q2.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 2 data (04/01/11-06/30/11) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabyState20112012Q2.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabyState20112012Q2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabyState20112012Q2.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabyState20112012Q3.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 3 data (07/01/11-09/30/11) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabyState20112012Q3.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabyState20112012Q3.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabyState20112012Q3.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabyState20112012Q4.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 4 data (10/01/11-12/31/11) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabyState20112012Q4.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabyState20112012Q4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabyState20112012Q4.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabyState20112012Q5.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 5 data (01/01/12-03/31/12) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabyState20112012Q5.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabyState20112012Q5.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabyState20112012Q5.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2011_12App_Data_by_State_Q6.xls",
                     "description": "Free Application for Federal Student Aid, 2011-12 quarter 6 data (04/01/12-06/30/12) by state available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/2011_12App_Data_by_State_Q6.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/2011_12App_Data_by_State_Q6.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2011_12App_Data_by_State_Q6.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/FSADataCenter_Demographics_2011-12Cycle.xls",
                     "format": "XLS",
-                    "title": "FSADataCenter_Demographics_2011-12Cycle",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/fsawg/datacenter/library/FSADataCenter_Demographics_2011-12Cycle.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FSADataCenter_Demographics_2011-12Cycle"
                 }
             ],
+            "identifier": "57838400-c7b3-42d2-ba4f-d91e9f2ae6c6",
+            "issued": "2012-06-30",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "fafsa",
@@ -37041,32 +37018,14 @@
                 "free-application-for-federal-student-aid",
                 "postsecondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://studentaid.ed.gov/sites/default/files/fsawg/datacenter/library/FAFSAReportDefinitions.doc"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Free Application for Federal Student Aid, 2009-10",
-            "description": "The Free Application for Federal Student Aid, 2009-10 (FAFSA 2009-10), is part of the Free Application for Federal Student Aid (FAFSA) program; program data is available since 2006-07 at <https://studentaid.ed.gov/sa/about/data-center/student/application-volume/>. FAFSA 2009-10 (https://studentaid.ed.gov/) is a universe data collection of eligible incoming postsecondary education students, along with a subset of eligible continuing postsecondary education students, that collects financial information to determine the need and eligibility for financial assistance during postsecondary education. FAFSA 2009-10 applications are accepted via web and paper submission. Citizen and specified noncitizen students demonstrating financial need and planning to attend eligible degree or certificate programs in the 50 United States, the District of Columbia, Puerto Rico, and the outlying areas as regular students are eligible to apply for FAFSA 2009-10. FAFSA 2009-10 resulted in an expected family contribution (EFC) for each applying student. Statistics produced from FAFSA 2009-10 include application volumes by postsecondary school, state of legal residence, and completion by high school; and recipient and volume data by program for each school participating in Title IV programs.",
-            "modified": "2023-07-19T23:16:54.557571",
-            "accessLevel": "public",
-            "identifier": "f6ea5f2d-70f3-464f-855f-39093299bfbc",
-            "dataQuality": true,
-            "issued": "2010-06-30",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2011-08-03/pdf/2011-19607.pdf",
-            "temporal": "2009/2010",
+            "modified": "2023-07-19T23:16:57.927309",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Federal Student Aid (FSA)",
@@ -37087,117 +37046,135 @@
                     }
                 }
             },
+            "references": [
+                "https://studentaid.ed.gov/sites/default/files/fsawg/datacenter/library/FAFSAReportDefinitions.doc"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2011-08-03/pdf/2011-19607.pdf",
+            "temporal": "2011/2012",
+            "title": "Free Application for Federal Student Aid, 2011-12"
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
+            "description": "The Free Application for Federal Student Aid, 2009-10 (FAFSA 2009-10), is part of the Free Application for Federal Student Aid (FAFSA) program; program data is available since 2006-07 at <https://studentaid.ed.gov/sa/about/data-center/student/application-volume/>. FAFSA 2009-10 (https://studentaid.ed.gov/) is a universe data collection of eligible incoming postsecondary education students, along with a subset of eligible continuing postsecondary education students, that collects financial information to determine the need and eligibility for financial assistance during postsecondary education. FAFSA 2009-10 applications are accepted via web and paper submission. Citizen and specified noncitizen students demonstrating financial need and planning to attend eligible degree or certificate programs in the 50 United States, the District of Columbia, Puerto Rico, and the outlying areas as regular students are eligible to apply for FAFSA 2009-10. FAFSA 2009-10 resulted in an expected family contribution (EFC) for each applying student. Statistics produced from FAFSA 2009-10 include application volumes by postsecondary school, state of legal residence, and completion by high school; and recipient and volume data by program for each school participating in Title IV programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://studentaid.gov/sites/default/files/FSADataCenter_Demographics_2009-10Cycle.xls",
                     "format": "XLS",
-                    "title": "FSADataCenter_Demographics_2009-10Cycle",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/FSADataCenter_Demographics_2009-10Cycle.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FSADataCenter_Demographics_2009-10Cycle"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20092010Qtr1.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 1 data (01/01/09-03/31/09) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr1.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20092010Qtr1.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20092010Qtr2.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 2 data (04/01/09-06/30/09) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr2.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20092010Qtr2.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20092010Qtr3.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 3 data (07/01/09-09/30/09) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr3.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr3.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20092010Qtr3.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20092010Qtr4.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 4 data (10/01/09-12/31/09) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr4.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20092010Qtr4.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20092010Qtr5.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 5 data (01/01/10-03/31/10) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr5.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr5.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20092010Qtr5.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "AppDatabySchool20092010Qtr6.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 6 data (04/01/10-06/30/10) by school available in a Microsoft Excel file",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr6.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/AppDatabySchool20092010Qtr6.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "AppDatabySchool20092010Qtr6.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20092010Qtr1.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 1 data (01/01/09-03/31/09) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20092010Qtr1.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20092010Qtr2.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 2 data (04/01/09-06/30/09) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20092010Qtr2.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20092010Qtr3.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 3 data (07/01/09-09/30/09) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20092010Qtr3.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20092010Qtr4.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 4 data (10/01/09-12/31/09) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20092010Qtr4.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20092010Qtr5.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 5 data (01/01/10-03/31/10) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20092010Qtr5.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "XLS",
-                    "title": "AppDatabyState20092010Qtr6.xls",
                     "description": "Free Application for Federal Student Aid, 2009-10 quarter 6 data (04/01/10-06/30/10) by state available in a Microsoft Excel file",
                     "downloadURL": "https://studentaid.ed.gov/about/data-center/student/application-volume/fafsa-school-state",
-                    "mediaType": "text/plain"
+                    "format": "XLS",
+                    "mediaType": "text/plain",
+                    "title": "AppDatabyState20092010Qtr6.xls"
                 }
             ],
+            "identifier": "f6ea5f2d-70f3-464f-855f-39093299bfbc",
+            "issued": "2010-06-30",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "fafsa",
@@ -37206,30 +37183,14 @@
                 "free-application-for-federal-student-aid",
                 "postsecondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://studentaid.ed.gov/sites/default/files/fsawg/datacenter/library/FAFSAReportDefinitions.doc"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Foreign Gifts and Contracts Report",
-            "description": "The Foreign Gift and Contracts Report contains all gifts received within the previous six years from any foreign source, contracts with a foreign entity, and/or any ownership interests in or control over the institution by a foreign entity reported by Title IV-eligible domestic institutions that offer a bachelor's degree or higher, or that offer a transfer program of not less than two years that is acceptable for credit toward a bachelor's degree, when the total value of all gifts given in a calendar year is $250,000 or greater or if the institution is owned or controlled by a foreign source.",
-            "modified": "2023-07-19T23:16:48.062537",
-            "accessLevel": "public",
-            "identifier": "60b12a02-abe4-438d-b3b6-76ae00faaebd",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/2011",
+            "modified": "2023-07-19T23:16:54.557571",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Federal Student Aid (FSA)",
@@ -37250,22 +37211,39 @@
                     }
                 }
             },
+            "references": [
+                "https://studentaid.ed.gov/sites/default/files/fsawg/datacenter/library/FAFSAReportDefinitions.doc"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2011-08-03/pdf/2011-19607.pdf",
+            "temporal": "2009/2010",
+            "title": "Free Application for Federal Student Aid, 2009-10"
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
+            "description": "The Foreign Gift and Contracts Report contains all gifts received within the previous six years from any foreign source, contracts with a foreign entity, and/or any ownership interests in or control over the institution by a foreign entity reported by Title IV-eligible domestic institutions that offer a bachelor's degree or higher, or that offer a transfer program of not less than two years that is acceptable for credit toward a bachelor's degree, when the total value of all gifts given in a calendar year is $250,000 or greater or if the institution is owned or controlled by a foreign source.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "ForeignGifts.xls",
                     "description": "Foreign Gift and Contract Report",
-                    "downloadURL": "https://studentaid.gov/sites/default/files/ForeignGifts.xls"
+                    "downloadURL": "https://studentaid.gov/sites/default/files/ForeignGifts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ForeignGifts.xls"
                 }
             ],
+            "identifier": "60b12a02-abe4-438d-b3b6-76ae00faaebd",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "contracts",
@@ -37275,34 +37253,20 @@
                 "relationships",
                 "title-iv-student-assistance-programs"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T23:16:48.062537",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Compensation Survey, 2009-10",
-            "description": "The Teacher Compensation Survey, 2009-10 (TCS 2009-10), is part of the Common Core of Data (CCD) program. TCS 2009-10 (https://nces.ed.gov/ccd/tcssurvinfo.asp) is a cross-sectional universe survey that collected information on each public school teacher and on how public school teachers are compensated. TCS data are collected electronically from the administrative records of state education agencies. Participating state education agencies (SEAs) voluntarily submit TCS data. The study's response rate has not been calculated as of March 2013. Key statistics produced from TCS 2009-10 includes information on teachers' salaries, benefits, and compensations.",
-            "modified": "2023-07-19T23:16:47.087139",
-            "accessLevel": "public",
-            "identifier": "b3e523b6-ae8d-47aa-b90c-dffed0c4b668",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2009/2010",
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
@@ -37317,20 +37281,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2010/2011",
+            "title": "Foreign Gifts and Contracts Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Teacher Compensation Survey, 2009-10 (TCS 2009-10), is part of the Common Core of Data (CCD) program. TCS 2009-10 (https://nces.ed.gov/ccd/tcssurvinfo.asp) is a cross-sectional universe survey that collected information on each public school teacher and on how public school teachers are compensated. TCS data are collected electronically from the administrative records of state education agencies. Participating state education agencies (SEAs) voluntarily submit TCS data. The study's response rate has not been calculated as of March 2013. Key statistics produced from TCS 2009-10 includes information on teachers' salaries, benefits, and compensations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "tcssurvinfo.asp",
                     "downloadURL": "https://nces.ed.gov/ccd/tcssurvinfo.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "tcssurvinfo.asp"
                 }
             ],
+            "identifier": "b3e523b6-ae8d-47aa-b90c-dffed0c4b668",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data",
@@ -37342,28 +37319,14 @@
                 "teacher-salaries",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T23:16:47.087139",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Compensation Survey, 2010-11",
-            "description": "The Teacher Compensation Survey, 2010-11 (TCS 2010-11), is part of the Common Core of Data (CCD) program. TCS 2010-11 (https://nces.ed.gov/ccd/tcssurvinfo.asp) is a cross-sectional universe survey that collected information on each public school teacher and on how public school teachers are compensated. TCS data are collected electronically from the administrative records of state education agencies. Participating state education agencies (SEAs) voluntarily submit TCS data. Key statistics produced from TCS 2010-11 includes information on teachers' salaries, benefits, and compensations.",
-            "modified": "2023-07-19T23:16:46.679756",
-            "accessLevel": "public",
-            "identifier": "3ff07578-bb23-4896-81d7-d0e8c0b10c89",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2010/2011",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -37384,20 +37347,34 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2009/2010",
+            "title": "Teacher Compensation Survey, 2009-10"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Teacher Compensation Survey, 2010-11 (TCS 2010-11), is part of the Common Core of Data (CCD) program. TCS 2010-11 (https://nces.ed.gov/ccd/tcssurvinfo.asp) is a cross-sectional universe survey that collected information on each public school teacher and on how public school teachers are compensated. TCS data are collected electronically from the administrative records of state education agencies. Participating state education agencies (SEAs) voluntarily submit TCS data. Key statistics produced from TCS 2010-11 includes information on teachers' salaries, benefits, and compensations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "tcssurvinfo.asp",
                     "downloadURL": "https://nces.ed.gov/ccd/tcssurvinfo.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "tcssurvinfo.asp"
                 }
             ],
+            "identifier": "3ff07578-bb23-4896-81d7-d0e8c0b10c89",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data",
@@ -37409,34 +37386,20 @@
                 "teacher-salaries",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T23:16:46.679756",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Cohort Default Rates",
-            "description": "A cohort default rate is the percentage of a school's borrowers who enter repayment on certain Federal Family Education Loan (FFEL) Program or William D. Ford Federal Direct Loan (Direct Loan) Program loans during a particular federal fiscal year (FY), October 1 to September 30, and default or meet other specified conditions prior to the end of the second following fiscal year, as calculated by Federal Student Aid using data derived from the National Student Loan Data System (NSLDS).",
-            "modified": "2023-07-19T19:53:42.359004",
-            "accessLevel": "public",
-            "identifier": "38da9f3e-4775-468d-9a57-c544322af811",
-            "dataQuality": true,
-            "issued": "2014-09-22",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/2011",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Federal Student Aid (FSA)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -37451,71 +37414,86 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2010/2011",
+            "title": "Teacher Compensation Survey, 2010-11"
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
                 "fn": "Katrina Turner",
                 "hasEmail": "mailto:katrina.turner@ed.gov"
             },
+            "dataQuality": true,
+            "description": "A cohort default rate is the percentage of a school's borrowers who enter repayment on certain Federal Family Education Loan (FFEL) Program or William D. Ford Federal Direct Loan (Direct Loan) Program loans during a particular federal fiscal year (FY), October 1 to September 30, and default or meet other specified conditions prior to the end of the second following fiscal year, as calculated by Federal Student Aid using data derived from the National Student Loan Data System (NSLDS).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped ACCDB",
-                    "title": "peps300.zip",
                     "description": "Official 3-year cohort default rates published for schools participating in the Title IV student financial assistance programs.",
-                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/peps300.zip"
+                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/peps300.zip",
+                    "format": "Zipped ACCDB",
+                    "mediaType": "application/zip",
+                    "title": "peps300.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped ACCDB",
-                    "title": "peps304.zip",
                     "description": "Schools subject to loss of Direct Loan Program and/or Federal Pell Grant Program eligibility due to its three most recent years of cohort default rates being 30.0% or greater.",
-                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/peps304.zip"
+                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/peps304.zip",
+                    "format": "Zipped ACCDB",
+                    "mediaType": "application/zip",
+                    "title": "peps304.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped ACCDB",
-                    "title": "peps305.zip",
                     "description": "Schools subject to loss of Direct Loan Program eligibility due to its most recent official 3-year cohort default rates being greater than 40.0%.",
-                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/peps305.zip"
+                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/peps305.zip",
+                    "format": "Zipped ACCDB",
+                    "mediaType": "application/zip",
+                    "title": "peps305.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped ACCDB",
-                    "title": "peps751.zip",
                     "description": "Schools with its most recent official 3-year cohort default rate less than 5.0% and are eligible to make single and non-delayed disbursements on loans used for attendance in a study abroad program as defined in Section 428G(e) of the Higher Education Act.",
-                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/peps751.zip"
+                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/peps751.zip",
+                    "format": "Zipped ACCDB",
+                    "mediaType": "application/zip",
+                    "title": "peps751.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped ACCDB",
-                    "title": "peps753.zip",
                     "description": "Schools with its most recent three years of 3-year cohort default rates less than 15.0%, including eligible foreign institutions, and that disburse in a single installment loans that are made for one semester, one trimester, one quarter, or a four-month period. These institutions are no longer required to delay the delivery or disbursement of loans for 30 days for first-time, first-year undergraduate borrowers.",
-                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/peps753.zip"
+                    "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/peps753.zip",
+                    "format": "Zipped ACCDB",
+                    "mediaType": "application/zip",
+                    "title": "peps753.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
                     "description": "Official 3-Year Cohort Default Rate Search for Postsecondary Schools",
                     "downloadURL": "https://www2.ed.gov/offices/OSFAP/defaultmanagement/cdr.html",
+                    "format": "HTML",
                     "mediaType": "text/plain"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "PDF",
-                    "title": "060614DefaultRatesforCohortYears20072011",
-                    "description": "Federal student loan default rates for cohort years 2007-2011 in PDF format",
                     "describedBy": "https://ifap.ed.gov/eannouncements/attachments/060614ExplanationDefaultRates.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://ifap.ed.gov/eannouncements/attachments/060614DefaultRatesforCohortYears20072011.pdf"
+                    "description": "Federal student loan default rates for cohort years 2007-2011 in PDF format",
+                    "downloadURL": "https://ifap.ed.gov/eannouncements/attachments/060614DefaultRatesforCohortYears20072011.pdf",
+                    "format": "PDF",
+                    "mediaType": "application/pdf",
+                    "title": "060614DefaultRatesforCohortYears20072011"
                 }
             ],
+            "identifier": "38da9f3e-4775-468d-9a57-c544322af811",
+            "issued": "2014-09-22",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "cohort-default-rates",
@@ -37524,33 +37502,20 @@
                 "operations-performance-division",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T19:53:42.359004",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Public Education Financial Survey, 2012-13",
-            "description": "The National Public Education Financial Survey, 2012-13 (NPEFS 2012-13), is a study that is part of the Common Core of Data's National Public Education Financial Survey program; program data is available since 1987 at <https://nces.ed.gov/ccd/stfis.asp>. CCD-NPEFS 2012-13 [https://nces.ed.gov/ccd/stfis.asp] is a cross-sectional survey that gathers data on the financing of education. NPEFS data are used in calculating states' Title I grants. The study was conducted using responding agencies' existing administrative records. The universe of state education agencies was sampled. The study's response rate is TBD. Key statistics produced from CCD-NPEFS 2012-13 will collect data on attendance, revenue, and expenditure data from which NCES determines a State's 'average per-pupil expenditure' (SPPE) for elementary and secondary education.",
-            "modified": "2023-07-19T18:39:04.761603",
-            "accessLevel": "public",
-            "identifier": "3e99842a-bccb-46be-8bc1-54c1d923754c",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
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
@@ -37565,46 +37530,59 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2010/2011",
+            "title": "Cohort Default Rates"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Public Education Financial Survey, 2012-13 (NPEFS 2012-13), is a study that is part of the Common Core of Data's National Public Education Financial Survey program; program data is available since 1987 at <https://nces.ed.gov/ccd/stfis.asp>. CCD-NPEFS 2012-13 [https://nces.ed.gov/ccd/stfis.asp] is a cross-sectional survey that gathers data on the financing of education. NPEFS data are used in calculating states' Title I grants. The study was conducted using responding agencies' existing administrative records. The universe of state education agencies was sampled. The study's response rate is TBD. Key statistics produced from CCD-NPEFS 2012-13 will collect data on attendance, revenue, and expenditure data from which NCES determines a State's 'average per-pupil expenditure' (SPPE) for elementary and secondary education.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "stfis13_1a.zip",
                     "description": "National Public Education Financial Survey 2012-13 data in a zipped text file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stfis13_1a.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stfis13_1a.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "stfis13_1a.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "stfis13_1a_xls.zip",
                     "description": "National Public Education Financial Survey 2012-13 data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/Stfis13_1a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/Stfis13_1a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "stfis13_1a_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "stfis13_1a_sas.zip",
                     "description": "National Public Education Financial Survey 2012-13 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stfis13_1a_sas.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stfis13_1a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "stfis13_1a_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SPSS",
-                    "title": "stfs_1a_spss.zip",
                     "description": "National Public Education Financial Survey 2012-13 data in a zipped SPSS file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stfs_1a_spss.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stfs_1a_spss.zip",
+                    "format": "Zipped SPSS",
+                    "mediaType": "application/zip",
+                    "title": "stfs_1a_spss.zip"
                 }
             ],
+            "identifier": "3e99842a-bccb-46be-8bc1-54c1d923754c",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "expenditures",
@@ -37612,27 +37590,14 @@
                 "public-schools",
                 "revenues"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T18:39:04.761603",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Public Education Financial Survey, 2011-12",
-            "description": "The National Public Education Financial Survey, 2011-12 (NPEFS 2011-12), is a study that is part of the Common Core of Data's National Public Education Financial Survey program; program data is available since 1987 at <https://nces.ed.gov/ccd/stfis.asp>. CCD-NPEFS 2011-12 [https://nces.ed.gov/ccd/stfis.asp] is a cross-sectional survey that gathers data on the financing of education. NPEFS data are used in calculating states' Title I grants. The study was conducted using responding agencies' existing administrative records. The universe of state education agencies was sampled. The study's response rate has not been calculated as of May 2013. Key statistics produced from CCD-NPEFS 2011-12 will collect data on attendance, revenue, and expenditure data from which NCES determines a State's 'average per-pupil expenditure' (SPPE) for elementary and secondary education.",
-            "modified": "2023-07-19T18:39:04.303396",
-            "accessLevel": "public",
-            "identifier": "05b90d83-242b-496f-bcc7-b00bf6eba0ac",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -37653,46 +37618,59 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "National Public Education Financial Survey, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Public Education Financial Survey, 2011-12 (NPEFS 2011-12), is a study that is part of the Common Core of Data's National Public Education Financial Survey program; program data is available since 1987 at <https://nces.ed.gov/ccd/stfis.asp>. CCD-NPEFS 2011-12 [https://nces.ed.gov/ccd/stfis.asp] is a cross-sectional survey that gathers data on the financing of education. NPEFS data are used in calculating states' Title I grants. The study was conducted using responding agencies' existing administrative records. The universe of state education agencies was sampled. The study's response rate has not been calculated as of May 2013. Key statistics produced from CCD-NPEFS 2011-12 will collect data on attendance, revenue, and expenditure data from which NCES determines a State's 'average per-pupil expenditure' (SPPE) for elementary and secondary education.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "stfis_1a_txt.zip",
                     "description": "National Public Education Financial Survey 2011-12 data in a zipped text file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/Stfis_1a_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/Stfis_1a_txt.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "stfis_1a_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "stfis_1a_xls.zip",
                     "description": "National Public Education Financial Survey 2011-12 data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/Stfis_1a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/Stfis_1a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "stfis_1a_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "stfis_1a_sas.zip",
                     "description": "National Public Education Financial Survey 2011-12 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/npefs/Stfis_1a_sas.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/npefs/Stfis_1a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "stfis_1a_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SPSS",
-                    "title": "stfis_1a_spss.zip",
                     "description": "National Public Education Financial Survey 2011-12 data in a zipped SPSS file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/npefs/stfis_1a_spss.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/npefs/stfis_1a_spss.zip",
+                    "format": "Zipped SPSS",
+                    "mediaType": "application/zip",
+                    "title": "stfis_1a_spss.zip"
                 }
             ],
+            "identifier": "05b90d83-242b-496f-bcc7-b00bf6eba0ac",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "expenditures",
@@ -37700,34 +37678,20 @@
                 "public-schools",
                 "revenues"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T18:39:04.303396",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Submission of Financial Statements and Compliance Audits, 2012-13",
-            "description": "The Annual Submission of Financial Statements and Compliance Audits, 2012-13 (ASFS 2012-13), is a study that is part of the Annual Submission of Financial Statements and Compliance Audits program. ASFS 2012-13 is a cross-sectional survey that collects data from postsecondary institutions in the form of annual audited financial statements. The study was conducted using a web-based data collection system where postsecondary institutions submitted information. The universe of postsecondary schools was sampled. The study's response rate was 100 percent. Key statistics produced from ASFS 2012-13 are on the disbursement of Title IV funding, compliance to federal regulations regarding Title IV funding, and overall financial health of institutions.",
-            "modified": "2023-07-19T18:39:02.715693",
-            "accessLevel": "public",
-            "identifier": "1ee4e5b0-c200-490a-b533-61d8c241bd32",
-            "dataQuality": true,
-            "issued": "2014-07-22",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/P1Y",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Federal Student Aid (FSA)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -37742,27 +37706,41 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "National Public Education Financial Survey, 2011-12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ti Baker",
                 "hasEmail": "mailto:ti.baker@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Annual Submission of Financial Statements and Compliance Audits, 2012-13 (ASFS 2012-13), is a study that is part of the Annual Submission of Financial Statements and Compliance Audits program. ASFS 2012-13 is a cross-sectional survey that collects data from postsecondary institutions in the form of annual audited financial statements. The study was conducted using a web-based data collection system where postsecondary institutions submitted information. The universe of postsecondary schools was sampled. The study's response rate was 100 percent. Key statistics produced from ASFS 2012-13 are on the disbursement of Title IV funding, compliance to federal regulations regarding Title IV funding, and overall financial health of institutions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Financial Responsibility Composite Scores",
                     "description": "Section 498(c) of the Higher Education Act of 1965, as amended, requires for-profit and non-profit institutions to annually submit audited financial statements to the Department to demonstrate they are maintaining the standards of financial responsibility necessary to participate in the Title IV programs. One of many standards, which the Department utilizes to gauge the financial responsibility of an institution, is a composite of three ratios derived from an institution's audited financial statements. The three ratios are a primary reserve ratio, an equity ratio, and a net income ratio. These ratios gauge the fundamental elements of the financial health of an institution, not the educational quality of an institution.",
                     "downloadURL": "https://studentaid.gov/data-center/school/composite-scores",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Financial Responsibility Composite Scores"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Proprietary School 90/10 Revenue Percentages",
                     "description": "Section 487(d)(4) of the Higher Education Act of 1965 (HEA), as amended, requires the Secretary to annually submit a report to Congress containing information regarding the amount and percentage of each proprietary institution's revenues from Title IV sources and non-Title IV sources as provided by the institution in its audited financial statements. The reports are sent to the Chairmen and Ranking Members of the corresponding House and Senate authorizing committees. Below, you can access the 90/10 transmittal letters, summary charts and reports for institutions with fiscal years ending in the corresponding award year.",
                     "downloadURL": "https://studentaid.gov/data-center/school/proprietary",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Proprietary School 90/10 Revenue Percentages"
                 }
             ],
+            "identifier": "1ee4e5b0-c200-490a-b533-61d8c241bd32",
+            "issued": "2014-07-22",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "compliance-audits",
@@ -37787,34 +37765,20 @@
                 "school-participation-division",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T18:39:02.715693",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Preparation Experiences and Early Teacher Effectiveness Study",
-            "description": "Teacher Preparation Experiences and Early Teacher Effectiveness Study (TPEETE) is a data collection that is part of a study authorized under the Improving Teacher State Formula Grants (TSFG) program. TSFG <https://ies.ed.gov/ncee/projects/evaluation/tq_teacherprep_early.asp> includes a cross-sectional survey that measures the frequency of particular variations in teachers' preparation experiences. The study examines whether the instructional skills that teachers learn about and have opportunities to practice in their preparation programs are associated with novice teachers' effectiveness in the classroom, as measured by teacher value-added scores. The data collection was conducted using electronic data collection from school districts and online surveys of school districts and elementary and middle school teachers. Teachers in their first, second, or third year of teaching responsible for teaching to at least one general education classroom of fourth- through sixth-grade students were sampled. TSFG will compute value-added scores for teachers, based on students' state math and English language arts tests, and examine the relationships between teacher preparation experiences and teacher value-added scores.",
-            "modified": "2023-07-19T18:39:00.361925",
-            "accessLevel": "public",
-            "identifier": "9bc940b2-68b9-4639-b0b9-f4f388607448",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-06-28/pdf/2012-15886.pdf",
-            "temporal": "2015/2017",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Evaluation and Regional Assistance (NCEERA)",
+                "name": "Office of Federal Student Aid (FSA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -37829,19 +37793,32 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2013/P1Y",
+            "title": "Annual Submission of Financial Statements and Compliance Audits, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Melanie Ali",
                 "hasEmail": "mailto:Melanie.Ali@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Teacher Preparation Experiences and Early Teacher Effectiveness Study (TPEETE) is a data collection that is part of a study authorized under the Improving Teacher State Formula Grants (TSFG) program. TSFG <https://ies.ed.gov/ncee/projects/evaluation/tq_teacherprep_early.asp> includes a cross-sectional survey that measures the frequency of particular variations in teachers' preparation experiences. The study examines whether the instructional skills that teachers learn about and have opportunities to practice in their preparation programs are associated with novice teachers' effectiveness in the classroom, as measured by teacher value-added scores. The data collection was conducted using electronic data collection from school districts and online surveys of school districts and elementary and middle school teachers. Teachers in their first, second, or third year of teaching responsible for teaching to at least one general education classroom of fourth- through sixth-grade students were sampled. TSFG will compute value-added scores for teachers, based on students' state math and English language arts tests, and examine the relationships between teacher preparation experiences and teacher value-added scores.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "tq_teacherprep_early.asp",
                     "downloadURL": "https://ies.ed.gov/ncee/projects/evaluation/tq_teacherprep_early.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "tq_teacherprep_early.asp"
                 }
             ],
+            "identifier": "9bc940b2-68b9-4639-b0b9-f4f388607448",
             "keyword": [
                 "34621008-400b-4c5c-b37f-2af6fec112e8",
                 "elementary-and-secondary-education",
@@ -37851,33 +37828,20 @@
                 "teacher-preparation",
                 "teacher-quality"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T18:39:00.361925",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "College Affordability and Transparency List Explanation Form, 2013-14",
-            "description": "College Affordability and Transparency List Explanation Form 2013-14 (CATEF 2013-14) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100% response rate. Key statistics produced from CATEF 2013-14 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of State government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
-            "modified": "2023-07-19T18:38:59.978261",
-            "accessLevel": "public",
-            "identifier": "b5cafdf4-e4f5-4d93-a66b-0dfbf2fbdb3b",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
+                "name": "National Center for Education Evaluation and Regional Assistance (NCEERA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -37892,22 +37856,36 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-06-28/pdf/2012-15886.pdf",
+            "temporal": "2015/2017",
+            "title": "Teacher Preparation Experiences and Early Teacher Effectiveness Study"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "dataQuality": true,
+            "description": "College Affordability and Transparency List Explanation Form 2013-14 (CATEF 2013-14) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100% response rate. Key statistics produced from CATEF 2013-14 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of State government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel Document",
-                    "title": "CATClists2011.xls",
                     "description": "College Affordability and Transparency list data for the 2011-2012 academic year",
-                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2011.xls"
+                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2011.xls",
+                    "format": "Microsoft Excel Document",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "CATClists2011.xls"
                 }
             ],
+            "identifier": "b5cafdf4-e4f5-4d93-a66b-0dfbf2fbdb3b",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "college-affordability",
@@ -37917,30 +37895,14 @@
                 "transparency-of-information",
                 "tuition-and-fees"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://collegecost.ed.gov/catc/resources/CATEF%20Summary%20Guide%20to%20College%20Costs%202014.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "College Affordability and Transparency List Explanation Form, 2016-17",
-            "description": "College Affordability and Transparency List Explanation Form 2016-17 (CATEF 2016-17) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100 percent response rate. Key statistics produced from CATEF 2016\u00c3-17 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of state government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
-            "modified": "2023-07-19T18:38:58.710035",
-            "accessLevel": "public",
-            "identifier": "47865b40-037e-4822-8669-06c098ff966a",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2014/2015",
+            "modified": "2023-07-19T18:38:59.978261",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -37961,30 +37923,46 @@
                     }
                 }
             },
+            "references": [
+                "https://collegecost.ed.gov/catc/resources/CATEF%20Summary%20Guide%20to%20College%20Costs%202014.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "College Affordability and Transparency List Explanation Form, 2013-14"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "dataQuality": true,
+            "description": "College Affordability and Transparency List Explanation Form 2016-17 (CATEF 2016-17) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100 percent response rate. Key statistics produced from CATEF 2016\u00c3-17 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of state government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "Microsoft Excel Document",
-                    "title": "CATClists2014.xls",
                     "description": "College Affordability and Transparency list data for the 2014-2015 academic year",
-                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2014.xlsx"
+                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2014.xlsx",
+                    "format": "Microsoft Excel Document",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CATClists2014.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "Microsoft Excel Document",
-                    "title": "2016_CATEF_Responses.xlsx",
                     "description": "College Affordability and Transparency Explanation Form responses for the 2014-2015 academic year",
-                    "downloadURL": "https://collegecost.ed.gov/catc/resources/2016_CATEF_Responses.xlsx"
+                    "downloadURL": "https://collegecost.ed.gov/catc/resources/2016_CATEF_Responses.xlsx",
+                    "format": "Microsoft Excel Document",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2016_CATEF_Responses.xlsx"
                 }
             ],
+            "identifier": "47865b40-037e-4822-8669-06c098ff966a",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "college-affordability",
@@ -37994,27 +37972,14 @@
                 "transparency-of-information",
                 "tuition-and-fees"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T18:38:58.710035",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "College Affordability and Transparency List Explanation Form, 2015-16",
-            "description": "College Affordability and Transparency List Explanation Form 2015-16 (CATEF 2015-16) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100 percent response rate. Key statistics produced from CATEF 2015-16 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of state government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
-            "modified": "2023-07-19T18:38:58.321250",
-            "accessLevel": "public",
-            "identifier": "0143a683-f4f0-4625-a4a8-f9b87e0c20f0",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/2014",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -38035,22 +38000,35 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2014/2015",
+            "title": "College Affordability and Transparency List Explanation Form, 2016-17"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "dataQuality": true,
+            "description": "College Affordability and Transparency List Explanation Form 2015-16 (CATEF 2015-16) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100 percent response rate. Key statistics produced from CATEF 2015-16 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of state government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "Microsoft Excel Document",
-                    "title": "CATClists2013.xls",
                     "description": "College Affordability and Transparency list data for the 2013-2014 academic year",
-                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2013.xlsx"
+                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2013.xlsx",
+                    "format": "Microsoft Excel Document",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "CATClists2013.xls"
                 }
             ],
+            "identifier": "0143a683-f4f0-4625-a4a8-f9b87e0c20f0",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "college-affordability",
@@ -38060,30 +38038,14 @@
                 "transparency-of-information",
                 "tuition-and-fees"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T18:38:58.321250",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://collegecost.ed.gov/catc/resources/2016_College_Affordability_and_Transparency_Explanation_Form_Summary.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "College Affordability and Transparency List Explanation Form, 2014-15",
-            "description": "College Affordability and Transparency List Explanation Form 2014-15 (CATEF 2014-15) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100 percent response rate. Key statistics produced from CATEF 2014-15 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of state government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
-            "modified": "2023-07-19T18:38:57.947227",
-            "accessLevel": "public",
-            "identifier": "bffb5f1a-2775-4f80-a769-5ad9c2ce820b",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -38104,22 +38066,38 @@
                     }
                 }
             },
+            "references": [
+                "https://collegecost.ed.gov/catc/resources/2016_College_Affordability_and_Transparency_Explanation_Form_Summary.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2013/2014",
+            "title": "College Affordability and Transparency List Explanation Form, 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "dataQuality": true,
+            "description": "College Affordability and Transparency List Explanation Form 2014-15 (CATEF 2014-15) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100 percent response rate. Key statistics produced from CATEF 2014-15 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of state government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel Document",
-                    "title": "CATClists2012.xls",
                     "description": "College Affordability and Transparency list data for the 2012-2013 academic year",
-                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2012.xls"
+                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2012.xls",
+                    "format": "Microsoft Excel Document",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "CATClists2012.xls"
                 }
             ],
+            "identifier": "bffb5f1a-2775-4f80-a769-5ad9c2ce820b",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "college-affordability",
@@ -38129,38 +38107,20 @@
                 "transparency-of-information",
                 "tuition-and-fees"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://collegecost.ed.gov/catc/resources/2015%20CATEF%20Summary%20Guide%20to%20College%20Costs.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2015-16",
-            "description": "The Common Core of Data Nonfiscal Survey, 2015-16 (CCD 2015-16) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2015-16 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2015-16 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:20:10.764217",
-            "accessLevel": "public",
-            "identifier": "3fb0b312-68c4-455d-b699-3dae8f9c3114",
-            "dataQuality": true,
-            "issued": "2017-12-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2015/2016",
+            "modified": "2023-07-19T18:38:57.947227",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
+                "name": "Office of Postsecondary Education (OPE)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -38175,62 +38135,79 @@
                     }
                 }
             },
+            "references": [
+                "https://collegecost.ed.gov/catc/resources/2015%20CATEF%20Summary%20Guide%20to%20College%20Costs.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "College Affordability and Transparency List Explanation Form, 2014-15"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2015-16 (CCD 2015-16) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2015-16 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2015-16 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "ccd_sea_029_1516_w_1a_011717_csv.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2015-16 v.1a Directory data in a zipped CSV file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_029_1516_w_1a_011717_csv.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_029_1516_w_1a_011717_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_029_1516_w_1a_011717_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLSX",
-                    "title": "ccd_sea_029_1516_w_1a_011717_xlsx.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2015-16 v.1a Directory data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_029_1516_w_1a_011717_xlsx.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_029_1516_w_1a_011717_xlsx.zip",
+                    "format": "Zipped XLSX",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_029_1516_w_1a_011717_xlsx.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "ccd_sea_052_1516_w_1a_011717_csv.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2015-16 v.1a Membership data in a zipped CSV file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_052_1516_w_1a_011717_csv.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_052_1516_w_1a_011717_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_052_1516_w_1a_011717_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "ccd_sea_052_1516_w_1a_011717_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2015-16 v.1a Membership data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_052_1516_w_1a_011717_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_052_1516_w_1a_011717_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_052_1516_w_1a_011717_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "ccd_sea_059_1516_w_1a_011717_csv.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2014-15 v.1a Staff data in a zipped CSV file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_059_1516_w_1a_011717_csv.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_059_1516_w_1a_011717_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_059_1516_w_1a_011717_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLSX",
-                    "title": "ccd_sea_059_1516_w_1a_011717_xlsx.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2014-15 v.1a Staff data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_059_1516_w_1a_011717_xlsx.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_059_1516_w_1a_011717_xlsx.zip",
+                    "format": "Zipped XLSX",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_059_1516_w_1a_011717_xlsx.zip"
                 }
             ],
+            "identifier": "3fb0b312-68c4-455d-b699-3dae8f9c3114",
+            "issued": "2017-12-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -38240,33 +38217,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/CCD_201516_File_Documentation_2017074.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/2017074_Documentation_CCD_201516.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2014-15",
-            "description": "The Common Core of Data Nonfiscal Survey, 2014-15 (CCD 2014-15) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2014-15 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2014-15 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:18:58.467554",
-            "accessLevel": "public",
-            "identifier": "53314e14-0cd2-4eb3-a4bc-bf44f4baf35b",
-            "dataQuality": true,
-            "issued": "2016-07-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2014/2015",
+            "modified": "2023-07-19T18:20:10.764217",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -38287,62 +38245,81 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/CCD_201516_File_Documentation_2017074.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/2017074_Documentation_CCD_201516.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2015/2016",
+            "title": "Common Core of Data Nonfiscal Survey, 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2014-15 (CCD 2014-15) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2014-15 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2014-15 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "ccd_sea_029_1415_w_0216161a_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2014-15 v.1a Directory data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_029_1415_w_0216161a_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_029_1415_w_0216161a_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_029_1415_w_0216161a_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "ccd_sea_029_1415_w_0216161a_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2014-15 v.1a Directory data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_029_1415_w_0216161a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_029_1415_w_0216161a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_029_1415_w_0216161a_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "ccd_sea_052_1415_w_0216161a_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2014-15 v.1a Membership data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_052_1415_w_0216161a_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_052_1415_w_0216161a_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_052_1415_w_0216161a_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "ccd_sea_052_1415_w_0216161a_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2014-15 v.1a Membership data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_052_1415_w_0216161a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_052_1415_w_0216161a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_052_1415_w_0216161a_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "ccd_sea_059_1415_w_0216161a_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2014-15 v.1a Staff data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_059_1415_w_0216161a_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_059_1415_w_0216161a_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_059_1415_w_0216161a_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "ccd_sea_059_1415_w_0216161a_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2014-15 v.1a Staff data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_059_1415_w_0216161a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/ccd_sea_059_1415_w_0216161a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "ccd_sea_059_1415_w_0216161a_xls.zip"
                 }
             ],
+            "identifier": "53314e14-0cd2-4eb3-a4bc-bf44f4baf35b",
+            "issued": "2016-07-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -38352,33 +38329,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/2016077_Documentation_062916.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/2016077_CCD_201415_Data_File_Documentation.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2013-14",
-            "description": "The Common Core of Data Nonfiscal Survey, 2013-14 (CCD 2013-14) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2013-14 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2013-14 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:16:16.160951",
-            "accessLevel": "public",
-            "identifier": "f155d6ca-1f1f-4213-9405-51124f643b37",
-            "dataQuality": true,
-            "issued": "2014-07-15",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2013/2014",
+            "modified": "2023-07-19T18:18:58.467554",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -38399,30 +38357,49 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/2016077_Documentation_062916.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/2016077_CCD_201415_Data_File_Documentation.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2014/2015",
+            "title": "Common Core of Data Nonfiscal Survey, 2014-15"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2013-14 (CCD 2013-14) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2013-14 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2013-14 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st131a_imp_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2013-14 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/st131a_imp_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/st131a_imp_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st131a_imp_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st131a_imp_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2013-14 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/st131a_imp_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/st131a_imp_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st131a_imp_xls.zip"
                 }
             ],
+            "identifier": "f155d6ca-1f1f-4213-9405-51124f643b37",
+            "issued": "2014-07-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -38432,33 +38409,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/2015146_2013-14_State_documentation_v1a.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/st131a_documentation.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2012-13",
-            "description": "The Common Core of Data Nonfiscal Survey, 2012-13 (CCD 2012-13) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2012-13 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2012-13 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:15:07.535882",
-            "accessLevel": "public",
-            "identifier": "db22c058-614a-40be-ab27-c401e6a143ae",
-            "dataQuality": true,
-            "issued": "2014-12-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2012/2013",
+            "modified": "2023-07-19T18:16:16.160951",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -38479,30 +38437,49 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/2015146_2013-14_State_documentation_v1a.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/st131a_documentation.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2013/2014",
+            "title": "Common Core of Data Nonfiscal Survey, 2013-14"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2012-13 (CCD 2012-13) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2012-13 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2012-13 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st121a_imp_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2012-13 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/st121a_imp_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/st121a_imp_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st121a_imp_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st121a_imp_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2012-13 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/st121a_imp_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/st121a_imp_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st121a_imp_xls.zip"
                 }
             ],
+            "identifier": "db22c058-614a-40be-ab27-c401e6a143ae",
+            "issued": "2014-12-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -38512,33 +38489,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/2015007.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/st121a_documentation.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2011-12",
-            "description": "The Common Core of Data Nonfiscal Survey, 2011-12 (CCD 2011-12) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2011-12 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2011-12 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:13:21.193930",
-            "accessLevel": "public",
-            "identifier": "1ca0c175-70f1-4927-9134-835c53240678",
-            "dataQuality": true,
-            "issued": "2014-03-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2011/2012",
+            "modified": "2023-07-19T18:15:07.535882",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -38559,30 +38517,49 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/2015007.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/st121a_documentation.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2012/2013",
+            "title": "Common Core of Data Nonfiscal Survey, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2011-12 (CCD 2011-12) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2011-12 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2011-12 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st111a_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2011-12 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st111a_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st111a_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st111a_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st111a_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2011-12 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st111a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st111a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st111a_xls.zip"
                 }
             ],
+            "identifier": "1ca0c175-70f1-4927-9134-835c53240678",
+            "issued": "2014-03-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -38592,33 +38569,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stfis111a_documentation.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/STnonfis111agen.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2010-11",
-            "description": "The Common Core of Data Nonfiscal Survey, 2010-11 (CCD 2010-11) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2010-11 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2010-11 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:12:09.636269",
-            "accessLevel": "public",
-            "identifier": "5570a3cc-54aa-4915-8a2e-429c8b8017c2",
-            "dataQuality": true,
-            "issued": "2012-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2010/2011",
+            "modified": "2023-07-19T18:13:21.193930",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -38639,30 +38597,49 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stfis111a_documentation.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/STnonfis111agen.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2011/2012",
+            "title": "Common Core of Data Nonfiscal Survey, 2011-12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2010-11 (CCD 2010-11) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2010-11 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2010-11 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st101a_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2010-11 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st101a_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st101a_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st101a_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st101a_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2010-11 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st101a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st101a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st101a_xls.zip"
                 }
             ],
+            "identifier": "5570a3cc-54aa-4915-8a2e-429c8b8017c2",
+            "issued": "2012-06-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -38672,33 +38649,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/STnonfis101agen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/STnonfis101agen.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2008-09",
-            "description": "The Common Core of Data Nonfiscal Survey, 2008-09 (CCD 2008-09) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2008-09 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2008-09 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:11:05.719043",
-            "accessLevel": "public",
-            "identifier": "221d050f-1c28-450c-9a03-447fd52ade89",
-            "dataQuality": true,
-            "issued": "2010-07-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2008/2009",
+            "modified": "2023-07-19T18:12:09.636269",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -38719,62 +38677,81 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/STnonfis101agen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/STnonfis101agen.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2010/2011",
+            "title": "Common Core of Data Nonfiscal Survey, 2010-11"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2008-09 (CCD 2008-09) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2008-09 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2008-09 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st081a_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2008-09 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081a_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081a_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st081a_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st081a_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2008-09 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st081a_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st081b_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2008-09 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081b_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081b_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st081b_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st081b_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2008-09 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081b_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081b_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st081b_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st081c_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2008-09 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081c_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081c_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st081c_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st081c_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2008-09 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081c_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st081c_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st081c_xls.zip"
                 }
             ],
+            "identifier": "221d050f-1c28-450c-9a03-447fd52ade89",
+            "issued": "2010-07-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -38784,37 +38761,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis081agen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis081agen.zip",
-                "https://nces.ed.gov/ccd/pdf/StNonfis081bgen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/StNonfis081bgen.zip",
-                "https://nces.ed.gov/ccd/pdf/StNonfis081cgen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnonfis081cgen.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2009-10",
-            "description": "The Common Core of Data Nonfiscal Survey, 2009-10 (CCD 2009-10) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2009-10 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2009-10 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:10:03.882906",
-            "accessLevel": "public",
-            "identifier": "7260921d-9b52-4072-af10-20b6f748313e",
-            "dataQuality": true,
-            "issued": "2011-03-10",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2009/2010",
+            "modified": "2023-07-19T18:11:05.719043",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -38835,46 +38789,69 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis081agen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis081agen.zip",
+                "https://nces.ed.gov/ccd/pdf/StNonfis081bgen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/StNonfis081bgen.zip",
+                "https://nces.ed.gov/ccd/pdf/StNonfis081cgen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnonfis081cgen.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2008/2009",
+            "title": "Common Core of Data Nonfiscal Survey, 2008-09"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2009-10 (CCD 2009-10) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2009-10 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2009-10 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st091a_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2009-10 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st091a_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st091a_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st091a_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st091a_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2009-10 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st091a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st091a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st091a_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st091b_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2009-10 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st091b_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st091b_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st091b_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st091b_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2009-10 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st091b_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st091b_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st091b_xls.zip"
                 }
             ],
+            "identifier": "7260921d-9b52-4072-af10-20b6f748313e",
+            "issued": "2011-03-10",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -38884,35 +38861,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T18:10:03.882906",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/STNONFIS091agen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnonfis091agen.zip",
-                "https://nces.ed.gov/ccd/pdf/STnonfis091bgen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/STnonfis091bgen.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2007-08",
-            "description": "The Common Core of Data Nonfiscal Survey, 2007-08 (CCD 2007-08) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2007-08 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2007-08 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:09:04.909303",
-            "accessLevel": "public",
-            "identifier": "df23e796-2272-4436-a489-7b2cd8fe9561",
-            "dataQuality": true,
-            "issued": "2009-11-10",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2007/2008",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -38933,46 +38889,67 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/STNONFIS091agen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnonfis091agen.zip",
+                "https://nces.ed.gov/ccd/pdf/STnonfis091bgen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/STnonfis091bgen.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2009/2010",
+            "title": "Common Core of Data Nonfiscal Survey, 2009-10"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2007-08 (CCD 2007-08) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2007-08 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2007-08 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st071a_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2007-08 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st071a_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st071a_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st071a_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st071a_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2007-08 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st071a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st071a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st071a_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st071b_txt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2007-08 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st071b_txt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st071b_txt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st071b_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st071b_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2007-08 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st071b_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st071b_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st071b_xls.zip"
                 }
             ],
+            "identifier": "df23e796-2272-4436-a489-7b2cd8fe9561",
+            "issued": "2009-11-10",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -38982,35 +38959,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/StNfis071agen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis071agen.zip",
-                "https://nces.ed.gov/ccd/pdf/StNfis071bgen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis071bgen.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2006-07",
-            "description": "The Common Core of Data Nonfiscal Survey, 2006-07 (CCD 2006-07) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2006-07 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2006-07 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:04:48.962751",
-            "accessLevel": "public",
-            "identifier": "0cee527c-0f53-4ccc-aa34-19effd1a73a7",
-            "dataQuality": true,
-            "issued": "2008-01-15",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2007/2008",
+            "modified": "2023-07-19T18:09:04.909303",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -39031,46 +38987,67 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/StNfis071agen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis071agen.zip",
+                "https://nces.ed.gov/ccd/pdf/StNfis071bgen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis071bgen.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2007/2008",
+            "title": "Common Core of Data Nonfiscal Survey, 2007-08"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2006-07 (CCD 2006-07) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2006-07 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2006-07 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st061a_dat.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2006-07 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st061a_dat.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st061a_dat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st061a_dat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st061a_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2006-07 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st061a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st061a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st061a_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st061b_dat.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2006-07 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st061b_dat.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st061b_dat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st061b_dat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st061a_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2006-07 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st061b_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st061b_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st061a_xls.zip"
                 }
             ],
+            "identifier": "0cee527c-0f53-4ccc-aa34-19effd1a73a7",
+            "issued": "2008-01-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -39080,35 +39057,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stNfis061bgen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis061bgen.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis061agen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis061agen.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2005-06",
-            "description": "The Common Core of Data Nonfiscal Survey, 2005-06 (CCD 2005-06) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2005-06 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2005-06 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:03:41.658072",
-            "accessLevel": "public",
-            "identifier": "e4f06ad2-6e27-4e08-a16e-6c6b982f8963",
-            "dataQuality": true,
-            "issued": "2008-07-15",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2005/2006",
+            "modified": "2023-07-19T18:04:48.962751",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -39129,30 +39085,51 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stNfis061bgen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis061bgen.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis061agen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis061agen.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2007/2008",
+            "title": "Common Core of Data Nonfiscal Survey, 2006-07"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2005-06 (CCD 2005-06) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2005-06 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2005-06 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st051a_dat.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2005-06 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st051a_dat.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st051a_dat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st051a_dat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st051a_xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2005-06 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st051a_xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st051a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st051a_xls.zip"
                 }
             ],
+            "identifier": "e4f06ad2-6e27-4e08-a16e-6c6b982f8963",
+            "issued": "2008-07-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "public-school-districts",
@@ -39160,33 +39137,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/Data/zip/stnfis051agen.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis051agen.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2003-04",
-            "description": "The Common Core of Data Nonfiscal Survey, 2003-04 (CCD 2003-04) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2003-04 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2003-04 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:02:04.378551",
-            "accessLevel": "public",
-            "identifier": "6f3e1d79-8387-4f92-9603-f9da76507fc9",
-            "dataQuality": true,
-            "issued": "2006-11-16",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2003/2004",
+            "modified": "2023-07-19T18:03:41.658072",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -39207,30 +39165,49 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/Data/zip/stnfis051agen.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis051agen.pdf"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2005/2006",
+            "title": "Common Core of Data Nonfiscal Survey, 2005-06"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2003-04 (CCD 2003-04) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2003-04 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2003-04 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st031adat.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2003-04 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st031adat.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st031adat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st031adat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st031axls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2003-04 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st031axls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st031axls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st031axls.zip"
                 }
             ],
+            "identifier": "6f3e1d79-8387-4f92-9603-f9da76507fc9",
+            "issued": "2006-11-16",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "elementary-education",
@@ -39238,33 +39215,14 @@
                 "public-schools",
                 "secondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stNfis031agen.pdf",
-                "https://nces.ed.gov/ccd/data/zip/stnfis031agen.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2004-05",
-            "description": "The Common Core of Data Nonfiscal Survey, 2004-05) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2004-05 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2004-05 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T18:00:16.299033",
-            "accessLevel": "public",
-            "identifier": "db1fdc19-04c3-4759-ab3b-161fe97e845d",
-            "dataQuality": true,
-            "issued": "2006-06-16",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2004/2005",
+            "modified": "2023-07-19T18:02:04.378551",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -39285,78 +39243,97 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stNfis031agen.pdf",
+                "https://nces.ed.gov/ccd/data/zip/stnfis031agen.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2003/2004",
+            "title": "Common Core of Data Nonfiscal Survey, 2003-04"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2004-05) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2004-05 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2004-05 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st041adat.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2004-05 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041adat.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041adat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st041adat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st041axls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2004-05 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041axls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041axls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st041axls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st041cdat.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2004-05 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041cdat.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041cdat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st041cdat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st041cxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2004-05 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041cxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041cxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st041cxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st041ddat.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2004-05 v.1d data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041ddat.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041ddat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st041ddat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st041dxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2004-05 v.1d data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041dxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041dxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st041dxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st041edat.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2004-05 v.1e data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041edat.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041edat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st041edat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st041exls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2004-05 v.1e data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041exls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st041exls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st041exls.zip"
                 }
             ],
+            "identifier": "db1fdc19-04c3-4759-ab3b-161fe97e845d",
+            "issued": "2006-06-16",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "elementary-education",
@@ -39364,39 +39341,14 @@
                 "public-schools",
                 "secondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stNfis04genr.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis041cgenr.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis041dgen.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis041egen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/st041agenr.zip",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis041cgen.zip",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis041dgen.zip",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis041egen.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2002-03",
-            "description": "The Common Core of Data Nonfiscal Survey, 2002-03 (CCD 2002-03) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2002-03 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2002-03 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:58:37.547760",
-            "accessLevel": "public",
-            "identifier": "8e29575c-260b-4984-8b58-118abc7f23f7",
-            "dataQuality": true,
-            "issued": "2005-01-15",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2002/2003",
+            "modified": "2023-07-19T18:00:16.299033",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -39417,62 +39369,87 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stNfis04genr.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis041cgenr.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis041dgen.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis041egen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/st041agenr.zip",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis041cgen.zip",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis041dgen.zip",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis041egen.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2004/2005",
+            "title": "Common Core of Data Nonfiscal Survey, 2004-05"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2002-03 (CCD 2002-03) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2002-03 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2002-03 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st020fdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2002-03 v.0f data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st020fdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st020fdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st020fdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st020fxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2002-03 v.0f data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st020fxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st020fxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st020fxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st021adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2002-03 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st021adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st021adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st021adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st021axls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2002-03 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st021axls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st021axls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st021axls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st030cdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2002-03 v.0c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st030cdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st030cdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st030cdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st030cxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2002-03 v.0c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st030cxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st030cxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st030cxls.zip"
                 }
             ],
+            "identifier": "8e29575c-260b-4984-8b58-118abc7f23f7",
+            "issued": "2005-01-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "elementary-education",
@@ -39481,37 +39458,14 @@
                 "public-schools",
                 "secondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stNfis02gen.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis021agen.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis030cgen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis020fgen.zip",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis021agen.zip",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis030cgen.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2001-02",
-            "description": "The Common Core of Data Nonfiscal Survey, 2001-02 (CCD 2001-02) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2001-02 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2001-02 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:57:29.448800",
-            "accessLevel": "public",
-            "identifier": "2b37b25f-9a78-46ee-b7fd-8b3044c7adce",
-            "dataQuality": true,
-            "issued": "2003-04-24",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2001/2002",
+            "modified": "2023-07-19T17:58:37.547760",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -39532,46 +39486,69 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stNfis02gen.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis021agen.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis030cgen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis020fgen.zip",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis021agen.zip",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis030cgen.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2002/2003",
+            "title": "Common Core of Data Nonfiscal Survey, 2002-03"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2001-02 (CCD 2001-02) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2001-02 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2001-02 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st011adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2001-02 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st011adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st011adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st011adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st011axls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2001-02 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st011axls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st011axls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st011axls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st011bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2001-02 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st011bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st011bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st011bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st011bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2001-02 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st011bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st011bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st011bxls.zip"
                 }
             ],
+            "identifier": "2b37b25f-9a78-46ee-b7fd-8b3044c7adce",
+            "issued": "2003-04-24",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "elementary-education",
@@ -39579,35 +39556,14 @@
                 "public-schools",
                 "secondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis01gen.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis01genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis01gen.zip",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis01genr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 2000-01",
-            "description": "The Common Core of Data Nonfiscal Survey, 2000-01 (CCD 2000-01) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2000-01 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2000-01 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:56:06.013547",
-            "accessLevel": "public",
-            "identifier": "687a6154-724f-4a62-88b3-f3386774bed5",
-            "dataQuality": true,
-            "issued": "2002-04-26",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2000/2001",
+            "modified": "2023-07-19T17:57:29.448800",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -39628,63 +39584,84 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis01gen.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis01genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis01gen.zip",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis01genr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2001/2002",
+            "title": "Common Core of Data Nonfiscal Survey, 2001-02"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 2000-01 (CCD 2000-01) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 2000-01 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 2000-01 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st001adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2000-01 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st001adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st001axls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2000-01 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001axls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001axls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st001axls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st001bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2000-01 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st001bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st001bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2000-01 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st001bxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st001cdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2000-01 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001cdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001cdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st001cdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st001cxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 2000-01 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001cxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st001cxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st001cxls.zip"
                 }
             ],
-            "keyword": [
+            "identifier": "687a6154-724f-4a62-88b3-f3386774bed5",
+            "issued": "2002-04-26",
+            "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
                 "public-school-districts",
@@ -39692,37 +39669,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis00gen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis00gen.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis00genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis00genr.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis001cgenr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis001cgenr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1998-99",
-            "description": "The Common Core of Data Nonfiscal Survey, 1998-99 (CCD 1998-99) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1998-99 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1998-99 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:54:46.475894",
-            "accessLevel": "public",
-            "identifier": "648ff35f-df42-462e-ad2a-ca8dd1601e63",
-            "dataQuality": true,
-            "issued": "2000-09-27",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1998/1999",
+            "modified": "2023-07-19T17:56:06.013547",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -39743,46 +39697,69 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis00gen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis00gen.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis00genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis00genr.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis001cgenr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis001cgenr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2000/2001",
+            "title": "Common Core of Data Nonfiscal Survey, 2000-01"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1998-99 (CCD 1998-99) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1998-99 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1998-99 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "stnfis98data.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1998-99 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis98data.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis98data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "stnfis98data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "stnfis98xls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1998-99 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis98xls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis98xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "stnfis98xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st981bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1998-99 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st981bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st981bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st981bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st981bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1998-99 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st981bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st981bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st981bxls.zip"
                 }
             ],
+            "identifier": "648ff35f-df42-462e-ad2a-ca8dd1601e63",
+            "issued": "2000-09-27",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -39791,35 +39768,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis98gen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis98gen.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis98genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis98genr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1999-2000",
-            "description": "The Common Core of Data Nonfiscal Survey, 1999-2000 (CCD 1999-2000) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1999-2000 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1999-2000 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:51:17.515564",
-            "accessLevel": "public",
-            "identifier": "0092c8d5-8288-4bee-bc3d-095837618d15",
-            "dataQuality": true,
-            "issued": "2001-04-26",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1999/2000",
+            "modified": "2023-07-19T17:54:46.475894",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -39840,46 +39796,67 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis98gen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis98gen.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis98genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis98genr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1998/1999",
+            "title": "Common Core of Data Nonfiscal Survey, 1998-99"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1999-2000 (CCD 1999-2000) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1999-2000 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, Bureau of Indian Affairs, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1999-2000 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st991adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1999-2000 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st991adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st991adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st991adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st991axls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1999-2000 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st991axls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st991axls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st991axls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st991bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1999-2000 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st991bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st991bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st991bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st991bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1999-2000 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st991bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st991bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st991bxls.zip"
                 }
             ],
+            "identifier": "0092c8d5-8288-4bee-bc3d-095837618d15",
+            "issued": "2001-04-26",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -39888,35 +39865,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis99gen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis99gen.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis99genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis99genr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1997-98",
-            "description": "The Common Core of Data Nonfiscal Survey, 1997-98 (CCD 1997-98) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1997-98 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1997-98 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:49:25.133507",
-            "accessLevel": "public",
-            "identifier": "3cb03611-dda2-4130-9819-686ae6c73267",
-            "dataQuality": true,
-            "issued": "1999-07-22",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1997/1998",
+            "modified": "2023-07-19T17:51:17.515564",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -39937,62 +39893,83 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis99gen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis99gen.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis99genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis99genr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1999/2000",
+            "title": "Common Core of Data Nonfiscal Survey, 1999-2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1997-98 (CCD 1997-98) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1997-98 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1997-98 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "stnfis971adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1997-98 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis971adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis971adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "stnfis971adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "stnfis971axls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1997-98 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis971axls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis971axls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "stnfis971axls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st971bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1997-98 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st971bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st971bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st971bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st971bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1997-98 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st971bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st971bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st971bxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st971cdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1997-98 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st971cdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st971cdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st971cdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st971cxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1997-98 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st971cxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st971cxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st971cxls.zip"
                 }
             ],
+            "identifier": "3cb03611-dda2-4130-9819-686ae6c73267",
+            "issued": "1999-07-22",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -40001,37 +39978,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis97gen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis97gen.zip",
-                "https://nces.ed.gov/ccd/pdf/stnfis971bgenr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis971bgenr.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis971cgenr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis971cgenr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1996-97",
-            "description": "The Common Core of Data Nonfiscal Survey, 1996-97 (CCD 1996-97) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1996-97 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1996-97 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:46:18.765294",
-            "accessLevel": "public",
-            "identifier": "6f54fed9-0126-4f74-9bd6-2d28b9eef99e",
-            "dataQuality": true,
-            "issued": "1999-01-11",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1996/1997",
+            "modified": "2023-07-19T17:49:25.133507",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -40052,54 +40006,77 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis97gen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis97gen.zip",
+                "https://nces.ed.gov/ccd/pdf/stnfis971bgenr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis971bgenr.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis971cgenr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis971cgenr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1997/1998",
+            "title": "Common Core of Data Nonfiscal Survey, 1997-98"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1996-97 (CCD 1996-97) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1996-97 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, Department of Defense schools, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1996-97 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "stnfis961adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1996-97 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis961adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis961adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "stnfis961adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st961bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1996-97 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st961bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st961bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st961bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st961bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1996-97 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st961bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st961bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st961bxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st961cdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1996-97 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st961cdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st961cdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st961cdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st961cxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1996-97 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st961cxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st961cxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st961cxls.zip"
                 }
             ],
+            "identifier": "6f54fed9-0126-4f74-9bd6-2d28b9eef99e",
+            "issued": "1999-01-11",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -40108,37 +40085,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis96gen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis96gen.zip",
-                "https://nces.ed.gov/ccd/pdf/stnfis961bgenr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis961bgenr.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis961cgenr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis961cgenr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1994-95",
-            "description": "The Common Core of Data Nonfiscal Survey, 1994-95 (CCD 1994-95) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1994-95 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1994-95 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:44:38.901070",
-            "accessLevel": "public",
-            "identifier": "c4ebba46-bfcb-4a64-b4b3-74daaa1e91a2",
-            "dataQuality": true,
-            "issued": "2000-11-09",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1994/1995",
+            "modified": "2023-07-19T17:46:18.765294",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -40159,46 +40113,69 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis96gen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis96gen.zip",
+                "https://nces.ed.gov/ccd/pdf/stnfis961bgenr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis961bgenr.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis961cgenr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis961cgenr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1996/1997",
+            "title": "Common Core of Data Nonfiscal Survey, 1996-97"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1994-95 (CCD 1994-95) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1994-95 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1994-95 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "stnfis94data.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1994-95 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis94data.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis94data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "stnfis94data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st941axls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1994-95 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st941axls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st941axls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st941axls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "stNfis94data.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1994-95 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stNfis94data.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stNfis94data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "stNfis94data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st941bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1994-95 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st941bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st941bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st941bxls.zip"
                 }
             ],
+            "identifier": "c4ebba46-bfcb-4a64-b4b3-74daaa1e91a2",
+            "issued": "2000-11-09",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -40207,35 +40184,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis94gen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis94gen.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis94genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis94genr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1995-96",
-            "description": "The Common Core of Data Nonfiscal Survey, 1995-96 (CCD 1995-96) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1995-96 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1995-96 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:43:24.128273",
-            "accessLevel": "public",
-            "identifier": "8f37539a-02e4-4a66-a5ef-8acf81422c98",
-            "dataQuality": true,
-            "issued": "1999-12-16",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1995/1996",
+            "modified": "2023-07-19T17:44:38.901070",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -40256,38 +40212,59 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis94gen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis94gen.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis94genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis94genr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1994/1995",
+            "title": "Common Core of Data Nonfiscal Survey, 1994-95"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1995-96 (CCD 1995-96) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1995-96 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1995-96 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "stnfis95data.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1995-96 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis95data.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis95data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "stnfis95data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st951bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1995-96 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st951bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st951bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st951bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st951bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1995-96 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st951bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st951bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st951bxls.zip"
                 }
             ],
+            "identifier": "8f37539a-02e4-4a66-a5ef-8acf81422c98",
+            "issued": "1999-12-16",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -40296,35 +40273,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis95gen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis95gen.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis95genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis95genr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1993-94",
-            "description": "The Common Core of Data Nonfiscal Survey, 1993-94 (CCD 1993-94) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1993-94 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1993-94 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:41:46.580576",
-            "accessLevel": "public",
-            "identifier": "364f27e5-839a-4c83-95ad-eae1e28dd9f4",
-            "dataQuality": true,
-            "issued": "2000-10-27",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1993/1994",
+            "modified": "2023-07-19T17:43:24.128273",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -40345,46 +40301,67 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis95gen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis95gen.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis95genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis95genr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1995/1996",
+            "title": "Common Core of Data Nonfiscal Survey, 1995-96"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1993-94 (CCD 1993-94) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1993-94 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1993-94 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "stnfis93data.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1993-94 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis93data.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stnfis93data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "stnfis93data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st931axls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1993-94 v.1a data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st931axls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st931axls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st931axls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "stNfis93data.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1993-94 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stNfis93data.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/stNfis93data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "stNfis93data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st931bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1993-94 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st931bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st931bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st931bxls.zip"
                 }
             ],
+            "identifier": "364f27e5-839a-4c83-95ad-eae1e28dd9f4",
+            "issued": "2000-10-27",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -40393,35 +40370,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis93gen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis93gen.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis93genr.pdf",
-                "https://nces.ed.gov/ccd/data/zip/st931bxls.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1991-92",
-            "description": "The Common Core of Data Nonfiscal Survey, 1991-92 (CCD 1991-92) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1991-92 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1991-92 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:40:27.835569",
-            "accessLevel": "public",
-            "identifier": "11a69c7e-0210-4657-8bdf-7de5a7ebf5ad",
-            "dataQuality": true,
-            "issued": "2000-05-09",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1991/1992",
+            "modified": "2023-07-19T17:41:46.580576",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -40442,54 +40398,75 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis93gen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis93gen.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis93genr.pdf",
+                "https://nces.ed.gov/ccd/data/zip/st931bxls.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1993/1994",
+            "title": "Common Core of Data Nonfiscal Survey, 1993-94"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1991-92 (CCD 1991-92) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1991-92 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1991-92 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st911adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1991-92 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st911adata.zip"
-                },
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st911adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st911adata.zip"
+                },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st911bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1991-92 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st911bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st911bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st911bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st991bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1991-92 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st911bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st911bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st991bxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st911cdat.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1991-92 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st911cdat.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st911cdat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st911cdat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st911cxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1991-92 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st911cxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st911cxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st911cxls.zip"
                 }
             ],
+            "identifier": "11a69c7e-0210-4657-8bdf-7de5a7ebf5ad",
+            "issued": "2000-05-09",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -40498,36 +40475,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis91gen.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis911bgenr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis911bgenr.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis91genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis91genr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1989-90",
-            "description": "The Common Core of Data Nonfiscal Survey, 1989-90 (CCD 1989-90) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1989-90 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1989-90 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:34:39.846772",
-            "accessLevel": "public",
-            "identifier": "bcefe52f-c5cf-4918-bb45-6968a80e1bb5",
-            "dataQuality": true,
-            "issued": "2000-05-09",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1989/1990",
+            "modified": "2023-07-19T17:40:27.835569",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -40548,54 +40503,76 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis91gen.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis911bgenr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis911bgenr.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis91genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis91genr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1991/1992",
+            "title": "Common Core of Data Nonfiscal Survey, 1991-92"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1989-90 (CCD 1989-90) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1989-90 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1989-90 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st891adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1989-90 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st891adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st891adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st891adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st891bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1989-90 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st891bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st891bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st891bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st891bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1989-90 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st891bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st891bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st891bxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st881cdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1989-90 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st881cdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st881cdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st881cdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st891cxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1989-90 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st891cxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st891cxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st891cxls.zip"
                 }
             ],
+            "identifier": "bcefe52f-c5cf-4918-bb45-6968a80e1bb5",
+            "issued": "2000-05-09",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -40604,35 +40581,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis89gen.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis89genr1b.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis89genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis89genr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1990-91",
-            "description": "The Common Core of Data Nonfiscal Survey, 1990-91 (CCD 1990-91) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1990-91 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1990-91 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:31:58.102358",
-            "accessLevel": "public",
-            "identifier": "8038b1bf-e3ed-4d5b-a0c5-834f68b5e1f1",
-            "dataQuality": true,
-            "issued": "2000-05-23",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1990/1991",
+            "modified": "2023-07-19T17:34:39.846772",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -40653,54 +40609,75 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis89gen.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis89genr1b.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis89genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis89genr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1989/1990",
+            "title": "Common Core of Data Nonfiscal Survey, 1989-90"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1990-91 (CCD 1990-91) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1990-91 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1990-91 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st901adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1990-91 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st901adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st901adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st901adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st901bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1990-91 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st901bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st901bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st901bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st901bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1990-91 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st901bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st901bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st901bxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st901ctxt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1990-91 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st901ctxt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st901ctxt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st901ctxt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st901cxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1990-91 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st901cxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st901cxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st901cxls.zip"
                 }
             ],
+            "identifier": "8038b1bf-e3ed-4d5b-a0c5-834f68b5e1f1",
+            "issued": "2000-05-23",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -40709,36 +40686,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis90gen.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis901bgenr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis901bgenr.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis90genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis90genr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1988-89",
-            "description": "The Common Core of Data Nonfiscal Survey, 1988-89 (CCD 1988-89) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1988-89 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1988-89 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:30:30.759455",
-            "accessLevel": "public",
-            "identifier": "051876f9-b789-4c5a-906e-6b40ab31385a",
-            "dataQuality": true,
-            "issued": "2000-02-10",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1988/1989",
+            "modified": "2023-07-19T17:31:58.102358",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -40759,54 +40714,76 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis90gen.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis901bgenr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis901bgenr.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis90genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis90genr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1990/1991",
+            "title": "Common Core of Data Nonfiscal Survey, 1990-91"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1988-89 (CCD 1988-89) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1988-89 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1988-89 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st881adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1988-89 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st881adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st881adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st881adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st881bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1988-89 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st881bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st881bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st881bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st881bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1988-89 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st881bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st881bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st881bxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st891cdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1988-89 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st891cdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st891cdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st891cdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "stNfis881cgenr.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1988-89 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/stNfis881cgenr.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/Data/zip/stNfis881cgenr.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "stNfis881cgenr.zip"
                 }
             ],
+            "identifier": "051876f9-b789-4c5a-906e-6b40ab31385a",
+            "issued": "2000-02-10",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -40815,36 +40792,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis88gen.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis88genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis88genr.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis881cgenr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis881cgenr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1986-87",
-            "description": "The Common Core of Data Nonfiscal Survey, 1986-87 (CCD 1986-87) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 198687 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1986-87 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T17:23:11.243743",
-            "accessLevel": "public",
-            "identifier": "11547c27-4d97-4c9e-91f3-faaaa9c6c28f",
-            "dataQuality": true,
-            "issued": "2000-05-24",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1986/1987",
+            "modified": "2023-07-19T17:30:30.759455",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -40865,54 +40820,76 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis88gen.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis88genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis88genr.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis881cgenr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis881cgenr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1988/1989",
+            "title": "Common Core of Data Nonfiscal Survey, 1988-89"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1986-87 (CCD 1986-87) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 198687 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1986-87 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st861adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1986-87 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st861adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st861adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st861adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st861bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1986-87 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st861bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st861bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st861bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st861bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1986-87 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st861bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st861bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st861bxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st861ctxt.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1986-87 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st861ctxt.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st861ctxt.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st861ctxt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st861cxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1986-87 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st861cxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st861cxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st861cxls.zip"
                 }
             ],
+            "identifier": "11547c27-4d97-4c9e-91f3-faaaa9c6c28f",
+            "issued": "2000-05-24",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -40921,36 +40898,14 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis86gen.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis861bgenr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis861bgenr.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis86genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis86genr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Common Core of Data Nonfiscal Survey, 1987-88",
-            "description": "The Common Core of Data Nonfiscal Survey, 1987-88 (CCD 1987-88) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1987-88 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1987-88 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
-            "modified": "2023-07-19T16:03:05.145016",
-            "accessLevel": "public",
-            "identifier": "4cfb5f32-8137-483b-9d54-b04db4702782",
-            "dataQuality": true,
-            "issued": "2000-02-10",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1987/1988",
+            "modified": "2023-07-19T17:23:11.243743",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -40971,54 +40926,76 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis86gen.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis861bgenr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis861bgenr.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis86genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis86genr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1986/1987",
+            "title": "Common Core of Data Nonfiscal Survey, 1986-87"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Cornman",
                 "hasEmail": "mailto:stephen.cornman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Common Core of Data Nonfiscal Survey, 1987-88 (CCD 1987-88) is a data collection that is part of the Common Core of Data (CCD) program; program data is available since 1986-1987 at <https://nces.ed.gov/ccd/ccddata.asp>. CCD-Nonfiscal 1987-88 (https://nces.ed.gov/ccd/index.asp) is a cross-sectional survey that collected non-fiscal data about all public schools, public school districts, and state education agencies in the 50 United States, the District of Columbia, and other outlying jurisdictions. The data were supplied by state education agency officials and included basic information and descriptive statistics on public elementary and secondary schools and schooling in general. Key information produced from CCD-Nonfiscal 1987-88 include information that described schools and school districts, including name, address, and phone number; student counts by race/ethnicity, grade and sex and full-time equivalent (FTE) staff counts by labor category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st871adata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1987-88 v.1a data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st871adata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st871adata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st871adata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st871bdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1987-88 v.1b data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st871bdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st871bdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st871bdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st871bxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1987-88 v.1b data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st871bxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st871bxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st871bxls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "st871cdata.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1987-88 v.1c data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st871cdata.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st871cdata.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "st871cdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "st871cxls.zip",
                     "description": "Common Core of Data Nonfiscal Survey, 1987-88 v.1c data in a zipped Microsoft Excel file",
-                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st871cxls.zip"
+                    "downloadURL": "https://nces.ed.gov/ccd/data/zip/st871cxls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "st871cxls.zip"
                 }
             ],
+            "identifier": "4cfb5f32-8137-483b-9d54-b04db4702782",
+            "issued": "2000-02-10",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "common-core-of-data-ccd",
@@ -41027,39 +41004,20 @@
                 "public-school-teachers",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis87gen.pdf",
-                "https://nces.ed.gov/ccd/pdf/stNfis87genr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stnfis87genr.zip",
-                "https://nces.ed.gov/ccd/pdf/stNfis871cgenr.pdf",
-                "https://nces.ed.gov/ccd/Data/zip/stNfis871cgenr.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Clery Act Reports",
-            "description": "The Jeanne Clery Disclosure of Campus Security Policy and Campus Crime Statistics Act is a federal statute requiring colleges and universities participating in federal financial aid programs to maintain and disclose campus crime statistics and security information. The U.S. Department of Education conducts reviews to evaluate an institution's compliance with the Clery Act requirements. A review may be initiated when a complaint is received, a media event raises certain concerns, the school's independent audit identifies serious noncompliance, or through a review selection process that may also coincide with state reviews performed by the FBI's Criminal Justice Information Service (CJIS) Audit Unit. Once a review is completed, the Department issues a Final Program Review Determination. Although regular program reviews may contain Clery Act findings, this page includes only those program reviews that were focused exclusively on the Clery Act.",
-            "modified": "2023-07-19T15:35:59.694565",
-            "accessLevel": "public",
-            "identifier": "c167bc4f-838c-4ca3-bb46-3e2d6fb104c9",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T16:03:05.145016",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Federal Student Aid (FSA)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -41074,19 +41032,40 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis87gen.pdf",
+                "https://nces.ed.gov/ccd/pdf/stNfis87genr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stnfis87genr.zip",
+                "https://nces.ed.gov/ccd/pdf/stNfis871cgenr.pdf",
+                "https://nces.ed.gov/ccd/Data/zip/stNfis871cgenr.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1987/1988",
+            "title": "Common Core of Data Nonfiscal Survey, 1987-88"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Marini",
                 "hasEmail": "mailto:tara.marini@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Jeanne Clery Disclosure of Campus Security Policy and Campus Crime Statistics Act is a federal statute requiring colleges and universities participating in federal financial aid programs to maintain and disclose campus crime statistics and security information. The U.S. Department of Education conducts reviews to evaluate an institution's compliance with the Clery Act requirements. A review may be initiated when a complaint is received, a media event raises certain concerns, the school's independent audit identifies serious noncompliance, or through a review selection process that may also coincide with state reviews performed by the FBI's Criminal Justice Information Service (CJIS) Audit Unit. Once a review is completed, the Department issues a Final Program Review Determination. Although regular program reviews may contain Clery Act findings, this page includes only those program reviews that were focused exclusively on the Clery Act.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Clery Act Reports",
                     "downloadURL": "https://studentaid.gov/data-center/school/clery-act-reports",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Clery Act Reports"
                 }
             ],
+            "identifier": "c167bc4f-838c-4ca3-bb46-3e2d6fb104c9",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "campus-crime-statistics",
@@ -41098,23 +41077,11 @@
                 "safety",
                 "university"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T15:35:59.694565",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Campus-Based Program Data for Federal Student Aid",
-            "description": "Provides annual recipient, disbursement and federal award information for the Campus-Based Programs (Perkins Loan Program, Federal Supplemental Education Opportunity Grant and Federal Work-Study Program) by postsecondary school.",
-            "modified": "2023-07-19T15:35:59.020975",
-            "accessLevel": "public",
-            "identifier": "81d095b5-0b61-4f85-b7a8-ec379632eb2a",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Federal Student Aid (FSA)",
@@ -41135,19 +41102,31 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Clery Act Reports"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Marini",
                 "hasEmail": "mailto:tara.marini@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Provides annual recipient, disbursement and federal award information for the Campus-Based Programs (Perkins Loan Program, Federal Supplemental Education Opportunity Grant and Federal Work-Study Program) by postsecondary school.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "title-iv",
                     "downloadURL": "https://studentaid.gov/data-center/student/title-iv",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "title-iv"
                 }
             ],
+            "identifier": "81d095b5-0b61-4f85-b7a8-ec379632eb2a",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "campus-based-programs",
@@ -41165,23 +41144,11 @@
                 "title-iv-programs",
                 "university"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T15:35:59.020975",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Grant Program Data for Federal Student Aid",
-            "description": "Provides recipient and disbursement information each quarter for the Federal Pell, TEACH, and Iraq and Afghanistan Service Grant Programs by postsecondary school.",
-            "modified": "2023-07-19T15:35:58.499507",
-            "accessLevel": "public",
-            "identifier": "fa3cb192-deee-4949-970f-1c4afec2abe4",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Federal Student Aid (FSA)",
@@ -41202,19 +41169,31 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Campus-Based Program Data for Federal Student Aid"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Marini",
                 "hasEmail": "mailto:tara.marini@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Provides recipient and disbursement information each quarter for the Federal Pell, TEACH, and Iraq and Afghanistan Service Grant Programs by postsecondary school.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "title-iv",
                     "downloadURL": "https://studentaid.gov/data-center/student/title-iv",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "title-iv"
                 }
             ],
+            "identifier": "fa3cb192-deee-4949-970f-1c4afec2abe4",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "academic-competitiveness-grant",
@@ -41227,23 +41206,11 @@
                 "title-iv-programs",
                 "university"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T15:35:58.499507",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FAFSA Application Volume",
-            "description": "These reports provide information on the number of Free Applications for Federal Student Aid (FAFSAs) processed.  One report provides the number of applications by the applicant's state of legal residence and the other report provides the number of applications by postsecondary institution, as listed on the applicant's FAFSA.  In both reports, numbers are reported in two categories: dependent students and independent students",
-            "modified": "2023-07-19T15:35:58.035430",
-            "accessLevel": "public",
-            "identifier": "64074c80-dffa-4d83-8d2c-246ab1fbbe1b",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Federal Student Aid (FSA)",
@@ -41264,19 +41231,31 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Grant Program Data for Federal Student Aid"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Marini",
                 "hasEmail": "mailto:tara.marini@ed.gov"
             },
+            "dataQuality": true,
+            "description": "These reports provide information on the number of Free Applications for Federal Student Aid (FAFSAs) processed.  One report provides the number of applications by the applicant's state of legal residence and the other report provides the number of applications by postsecondary institution, as listed on the applicant's FAFSA.  In both reports, numbers are reported in two categories: dependent students and independent students",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "FAFSA Application Volume",
                     "downloadURL": "https://studentaid.gov/data-center/student/application-volume",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "FAFSA Application Volume"
                 }
             ],
+            "identifier": "64074c80-dffa-4d83-8d2c-246ab1fbbe1b",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "fafsa",
@@ -41284,23 +41263,11 @@
                 "free-application-for-federal-student-aid",
                 "title-iv-programs"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T15:35:58.035430",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Student Loan Program Data",
-            "description": "Provides recipient and disbursement information each quarter for the Direct Loan and Federal Family Education Loan Programs by postsecondary school.",
-            "modified": "2023-07-19T15:35:57.538540",
-            "accessLevel": "public",
-            "identifier": "2ac2d6a4-202d-499c-9fc4-e0a05dcfb698",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Federal Student Aid (FSA)",
@@ -41321,19 +41288,31 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "FAFSA Application Volume"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Marini",
                 "hasEmail": "mailto:tara.marini@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Provides recipient and disbursement information each quarter for the Direct Loan and Federal Family Education Loan Programs by postsecondary school.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "title-iv",
                     "downloadURL": "https://studentaid.gov/data-center/student/title-iv",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "title-iv"
                 }
             ],
+            "identifier": "2ac2d6a4-202d-499c-9fc4-e0a05dcfb698",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "college",
@@ -41347,29 +41326,17 @@
                 "title-iv-programs",
                 "university"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T15:35:57.538540",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ED Grants: Ready-To-Learn Television",
-            "description": "Ready-to-Learn Television supports the development of educational television and digital media targeted at preschool and early elementary school children and their families.  This data-focused toolset site contains data visualizations and downloads. Ready-to-Learn TV's general goal is to promote early learning and school readiness, with a particular interest in reaching low-income children. In addition to creating television and other media products, the program supports activities intended to promote national distribution of the programming, effective educational uses of the programming, community-based outreach, and research on educational effectiveness. CFDA Number: 84.295",
-            "modified": "2023-07-19T15:35:56.934390",
-            "accessLevel": "public",
-            "identifier": "aa5c1729-c0f9-4873-bd44-60da5fbb7da5",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Innovation and Improvement (OII)",
+                "name": "Office of Federal Student Aid (FSA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Elementary and Secondary Education (OESE)",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -41384,19 +41351,31 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Federal Student Loan Program Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alula Asfaw",
                 "hasEmail": "mailto:alula.asfaw@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Ready-to-Learn Television supports the development of educational television and digital media targeted at preschool and early elementary school children and their families.  This data-focused toolset site contains data visualizations and downloads. Ready-to-Learn TV's general goal is to promote early learning and school readiness, with a particular interest in reaching low-income children. In addition to creating television and other media products, the program supports activities intended to promote national distribution of the programming, effective educational uses of the programming, community-based outreach, and research on educational effectiveness. CFDA Number: 84.295",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Ready to Learn Programming",
                     "downloadURL": "https://oese.ed.gov/offices/office-of-discretionary-grants-support-services/innovation-early-learning/ready-to-learn-television-rtl/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Ready to Learn Programming"
                 }
             ],
+            "identifier": "aa5c1729-c0f9-4873-bd44-60da5fbb7da5",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "cfda-84-295",
@@ -41412,24 +41391,11 @@
                 "television",
                 "tv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T15:35:56.934390",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ED Grants: Investing in Innovation (i3) Fund 2011",
-            "description": "The Investing in Innovation (i3) Fund website depicts and allows downloading of general information on the i3 applicants received, grantees awarded and project locations. The Investing in Innovation Fund, established under section 14007 of the American Recovery and Reinvestment Act of 2009 (ARRA), provides funding to support (1) local educational agencies (LEAs), and (2) nonprofit organizations in partnership with (a) one or more LEAs or (b) a consortium of schools. The purpose of the i3 program is to provide competitive grants to applicants with a record of improving student achievement and attainment in order to expand the implementation of, and investment in, innovative practices that are demonstrated to have an impact on improving student achievement or student growth, closing achievement gaps, decreasing dropout rates, increasing high school graduation rates, or increasing college enrollment and completion rates. These grants will (1) allow eligible entities to expand and develop innovative practices that can serve as models of best practices, (2) allow eligible entities to work in partnership with the private sector and the philanthropic community, and (3) identify and document best practices that can be shared and taken to scale based on demonstrated success.",
-            "modified": "2023-07-19T15:35:56.370455",
-            "accessLevel": "public",
-            "identifier": "4b18a941-a306-4c55-a91b-d6abdfab82db",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/P1Y",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Innovation and Improvement (OII)",
@@ -41450,19 +41416,31 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ED Grants: Ready-To-Learn Television"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alula Asfaw",
                 "hasEmail": "mailto:alula.asfaw@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Investing in Innovation (i3) Fund website depicts and allows downloading of general information on the i3 applicants received, grantees awarded and project locations. The Investing in Innovation Fund, established under section 14007 of the American Recovery and Reinvestment Act of 2009 (ARRA), provides funding to support (1) local educational agencies (LEAs), and (2) nonprofit organizations in partnership with (a) one or more LEAs or (b) a consortium of schools. The purpose of the i3 program is to provide competitive grants to applicants with a record of improving student achievement and attainment in order to expand the implementation of, and investment in, innovative practices that are demonstrated to have an impact on improving student achievement or student growth, closing achievement gaps, decreasing dropout rates, increasing high school graduation rates, or increasing college enrollment and completion rates. These grants will (1) allow eligible entities to expand and develop innovative practices that can serve as models of best practices, (2) allow eligible entities to work in partnership with the private sector and the philanthropic community, and (3) identify and document best practices that can be shared and taken to scale based on demonstrated success.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "awards",
                     "downloadURL": "https://oese.ed.gov/offices/office-of-discretionary-grants-support-services/innovation-early-learning/investing-in-innovation-i3/awards/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "awards"
                 }
             ],
+            "identifier": "4b18a941-a306-4c55-a91b-d6abdfab82db",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "arra",
@@ -41475,27 +41453,14 @@
                 "student-achievement",
                 "validation-grants"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T15:35:56.370455",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ED Grants: Investing in Innovation (i3) Fund 2010",
-            "description": "The Investing in Innovation (i3) Fund website depicts and allows downloading of general information on the i3 applicants received, grantees awarded and project locations. The Investing in Innovation Fund, established under section 14007 of the American Recovery and Reinvestment Act of 2009 (ARRA), provides funding to support (1) local educational agencies (LEAs), and (2) nonprofit organizations in partnership with (a) one or more LEAs or (b) a consortium of schools. The purpose of the i3 program is to provide competitive grants to applicants with a record of improving student achievement and attainment in order to expand the implementation of, and investment in, innovative practices that are demonstrated to have an impact on improving student achievement or student growth, closing achievement gaps, decreasing dropout rates, increasing high school graduation rates, or increasing college enrollment and completion rates. These grants will (1) allow eligible entities to expand and develop innovative practices that can serve as models of best practices, (2) allow eligible entities to work in partnership with the private sector and the philanthropic community, and (3) identify and document best practices that can be shared and taken to scale based on demonstrated success.",
-            "modified": "2023-07-19T15:35:55.894413",
-            "accessLevel": "public",
-            "identifier": "374ec2c4-9699-493a-918b-e303bc3185c7",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/P1Y",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Innovation and Improvement (OII)",
@@ -41516,19 +41481,32 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2011/P1Y",
+            "title": "ED Grants: Investing in Innovation (i3) Fund 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alula Asfaw",
                 "hasEmail": "mailto:alula.asfaw@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Investing in Innovation (i3) Fund website depicts and allows downloading of general information on the i3 applicants received, grantees awarded and project locations. The Investing in Innovation Fund, established under section 14007 of the American Recovery and Reinvestment Act of 2009 (ARRA), provides funding to support (1) local educational agencies (LEAs), and (2) nonprofit organizations in partnership with (a) one or more LEAs or (b) a consortium of schools. The purpose of the i3 program is to provide competitive grants to applicants with a record of improving student achievement and attainment in order to expand the implementation of, and investment in, innovative practices that are demonstrated to have an impact on improving student achievement or student growth, closing achievement gaps, decreasing dropout rates, increasing high school graduation rates, or increasing college enrollment and completion rates. These grants will (1) allow eligible entities to expand and develop innovative practices that can serve as models of best practices, (2) allow eligible entities to work in partnership with the private sector and the philanthropic community, and (3) identify and document best practices that can be shared and taken to scale based on demonstrated success.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "awards",
                     "downloadURL": "https://oese.ed.gov/offices/office-of-discretionary-grants-support-services/innovation-early-learning/investing-in-innovation-i3/awards/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "awards"
                 }
             ],
+            "identifier": "374ec2c4-9699-493a-918b-e303bc3185c7",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "arra",
@@ -41541,26 +41519,14 @@
                 "student-achievement",
                 "validation-grants"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T15:35:55.894413",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ED Grants: Promise Neighborhoods Fund",
-            "description": "The Promise Neighborhoods Fund website depicts open grantmaking information on the applicants received, grantees awarded and project locations. The purpose of Promise Neighborhoods is to improve significantly the educational and developmental outcomes of children in our most distressed communities, and to transform those communities by-- (1) Supporting efforts to improve child outcomes and ensure that data on those outcomes are communicated and analyzed on an ongoing basis by leaders and members of the community; (2) Identifying and increasing the capacity of eligible entities that are focused on achieving results and building a college-going culture in the neighborhood; (3) Building a complete continuum of cradle-through-college-to-career solutions (continuum of solutions), which has both academic programs and family and community supports, with a strong school or schools at the center. Academic programs must include (a) High-quality early learning programs designed to improve outcomes in multiple domains of early learning; (b) programs, policies, and personnel for children in kindergarten through the 12th grade that are linked to improved academic outcomes; and (c) programs that prepare students for college and career success. Family and community supports must include programs to improve student health, safety, community stability, family and community engagement, and student access to 21st century learning tools. The continuum of solutions also must be linked and integrated seamlessly so there are common outcomes, a focus on similar milestones, support during transitional time periods, and no time or resource gaps that create obstacles for students in making academic progress. The continuum also must be based on the best available evidence including, where available, strong or moderate evidence, and include programs, policies, practices, services, systems, and supports that result in improving educational and developmental outcomes for children from cradle through college to career; (4) Integrating programs and breaking down agency \"silos\" so that solutions are implemented effectively and efficiently across agencies; (5) Supporting the efforts of eligible entities, working with local governments, to build the infrastructure of policies, practices, systems, and resources needed to sustain and \"scale up\" proven, effective solutions across the broader region beyond the initial neighborhood; and (6) Learning about the overall impact of Promise Neighborhoods and about the relationship between particular strategies in Promise Neighborhoods and student outcomes, including a rigorous evaluation of the program.",
-            "modified": "2023-07-19T15:35:55.334610",
-            "accessLevel": "public",
-            "identifier": "53ee0ebe-8f04-4728-9634-55ebf8c14470",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Innovation and Improvement (OII)",
@@ -41581,20 +41547,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2010/P1Y",
+            "title": "ED Grants: Investing in Innovation (i3) Fund 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alula Asfaw",
                 "hasEmail": "mailto:alula.asfaw@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Promise Neighborhoods Fund website depicts open grantmaking information on the applicants received, grantees awarded and project locations. The purpose of Promise Neighborhoods is to improve significantly the educational and developmental outcomes of children in our most distressed communities, and to transform those communities by-- (1) Supporting efforts to improve child outcomes and ensure that data on those outcomes are communicated and analyzed on an ongoing basis by leaders and members of the community; (2) Identifying and increasing the capacity of eligible entities that are focused on achieving results and building a college-going culture in the neighborhood; (3) Building a complete continuum of cradle-through-college-to-career solutions (continuum of solutions), which has both academic programs and family and community supports, with a strong school or schools at the center. Academic programs must include (a) High-quality early learning programs designed to improve outcomes in multiple domains of early learning; (b) programs, policies, and personnel for children in kindergarten through the 12th grade that are linked to improved academic outcomes; and (c) programs that prepare students for college and career success. Family and community supports must include programs to improve student health, safety, community stability, family and community engagement, and student access to 21st century learning tools. The continuum of solutions also must be linked and integrated seamlessly so there are common outcomes, a focus on similar milestones, support during transitional time periods, and no time or resource gaps that create obstacles for students in making academic progress. The continuum also must be based on the best available evidence including, where available, strong or moderate evidence, and include programs, policies, practices, services, systems, and supports that result in improving educational and developmental outcomes for children from cradle through college to career; (4) Integrating programs and breaking down agency \"silos\" so that solutions are implemented effectively and efficiently across agencies; (5) Supporting the efforts of eligible entities, working with local governments, to build the infrastructure of policies, practices, systems, and resources needed to sustain and \"scale up\" proven, effective solutions across the broader region beyond the initial neighborhood; and (6) Learning about the overall impact of Promise Neighborhoods and about the relationship between particular strategies in Promise Neighborhoods and student outcomes, including a rigorous evaluation of the program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://www2.ed.gov/programs/promiseneighborhoods/index.html",
                     "format": "HTML",
-                    "title": "Promise Neighborhoods Fund",
-                    "downloadURL": "https://www2.ed.gov/programs/promiseneighborhoods/index.html"
+                    "mediaType": "text/html",
+                    "title": "Promise Neighborhoods Fund"
                 }
             ],
+            "identifier": "53ee0ebe-8f04-4728-9634-55ebf8c14470",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "academic-improvement",
@@ -41612,33 +41591,20 @@
                 "student-achievement",
                 "validation-grants"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T15:35:55.334610",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Campus Safety and Security Survey, 2009",
-            "description": "The Campus Safety and Security Survey, 2009 (CSSS 2009), is a data collection that is part of the Campus Safety and Security Survey (CSSS) program; program data is available since 2005 at <https://ope.ed.gov/security/GetDownloadFile.aspx>. CSSS 2009 (https://ope.ed.gov/security/) was a cross-sectional survey that collected information required for benefits about crime, criminal activity, and fire safety at postsecondary institutions in the United States. The collection was conducted through a web-based data entry system utilized by postsecondary institutions. All postsecondary institutions participating in Title IV funding were sampled. The collection's response rate was 100 percent. Key statistics produced from CSSS 2009 were on the number and types of crimes committed at responding postsecondary institutions and the number of fires on institution property.",
-            "modified": "2023-07-19T15:35:54.759075",
-            "accessLevel": "public",
-            "identifier": "7da1a8df-f100-414d-948d-5d00a55a9103",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2009/P1Y",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
+                "name": "Office of Innovation and Improvement (OII)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Office of Elementary and Secondary Education (OESE)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -41653,20 +41619,32 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ED Grants: Promise Neighborhoods Fund"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashley Higgins",
                 "hasEmail": "mailto:ashley.higgins@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Campus Safety and Security Survey, 2009 (CSSS 2009), is a data collection that is part of the Campus Safety and Security Survey (CSSS) program; program data is available since 2005 at <https://ope.ed.gov/security/GetDownloadFile.aspx>. CSSS 2009 (https://ope.ed.gov/security/) was a cross-sectional survey that collected information required for benefits about crime, criminal activity, and fire safety at postsecondary institutions in the United States. The collection was conducted through a web-based data entry system utilized by postsecondary institutions. All postsecondary institutions participating in Title IV funding were sampled. The collection's response rate was 100 percent. Key statistics produced from CSSS 2009 were on the number and types of crimes committed at responding postsecondary institutions and the number of fires on institution property.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Campus Safety and Security Survey Files",
                     "downloadURL": "https://ope.ed.gov/campussafety/#/datafile/list",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Campus Safety and Security Survey Files"
                 }
             ],
+            "identifier": "7da1a8df-f100-414d-948d-5d00a55a9103",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "campus-safety",
@@ -41682,30 +41660,14 @@
                 "postsecondary-institutions",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www2.ed.gov/admins/lead/safety/campus.html"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Campus Safety and Security Survey, 2010",
-            "description": "The Campus Safety and Security Survey, 2010 (CSSS 2010), is a data collection that is part of the Campus Safety and Security Survey (CSSS) program; program data is available since 2005 at <https://ope.ed.gov/security/GetDownloadFile.aspx>. CSSS 2010 (https://ope.ed.gov/security/) was a cross-sectional survey that collected information required for benefits about crime, criminal activity, and fire safety at postsecondary institutions in the United States. The collection was conducted through a web-based data entry system utilized by postsecondary institutions. All postsecondary institutions participating in Title IV funding were sampled. The collection's response rate was 100 percent. Key statistics produced from CSSS 2010 were on the number and types of crimes committed at responding postsecondary institutions and the number of fires on institution property.",
-            "modified": "2023-07-19T15:35:54.196374",
-            "accessLevel": "public",
-            "identifier": "d0aebbe2-0ee5-45a6-b7f0-0ee903489eeb",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/P1Y",
+            "modified": "2023-07-19T15:35:54.759075",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -41726,20 +41688,36 @@
                     }
                 }
             },
+            "references": [
+                "https://www2.ed.gov/admins/lead/safety/campus.html"
+            ],
+            "spatial": "United States",
+            "temporal": "2009/P1Y",
+            "title": "Campus Safety and Security Survey, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashley Higgins",
                 "hasEmail": "mailto:ashley.higgins@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Campus Safety and Security Survey, 2010 (CSSS 2010), is a data collection that is part of the Campus Safety and Security Survey (CSSS) program; program data is available since 2005 at <https://ope.ed.gov/security/GetDownloadFile.aspx>. CSSS 2010 (https://ope.ed.gov/security/) was a cross-sectional survey that collected information required for benefits about crime, criminal activity, and fire safety at postsecondary institutions in the United States. The collection was conducted through a web-based data entry system utilized by postsecondary institutions. All postsecondary institutions participating in Title IV funding were sampled. The collection's response rate was 100 percent. Key statistics produced from CSSS 2010 were on the number and types of crimes committed at responding postsecondary institutions and the number of fires on institution property.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Campus Safety and Security Survey Files",
                     "downloadURL": "https://ope.ed.gov/campussafety/#/datafile/list",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Campus Safety and Security Survey Files"
                 }
             ],
+            "identifier": "d0aebbe2-0ee5-45a6-b7f0-0ee903489eeb",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "campus-safety",
@@ -41755,30 +41733,14 @@
                 "postsecondary-institutions",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www2.ed.gov/admins/lead/safety/campus.html"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Campus Safety and Security Survey, 2012",
-            "description": "The Campus Safety and Security Survey, 2012 (CSSS 2012), is a data collection that is part of the Campus Safety and Security Survey (CSSS) program; program data is available since 2005 at <https://ope.ed.gov/security/GetDownloadFile.aspx>. CSSS 2012 (https://ope.ed.gov/security/) was a cross-sectional survey that collected information required for benefits about crime, criminal activity, and fire safety at postsecondary institutions in the United States. The collection was conducted through a web-based data entry system utilized by postsecondary institutions. All postsecondary institutions participating in Title IV funding were sampled. The collection's response rate was 100 percent. Key statistics produced from CSSS 2012 were on the number and types of crimes committed at responding postsecondary institutions and the number of fires on institution property.",
-            "modified": "2023-07-19T15:35:53.432688",
-            "accessLevel": "public",
-            "identifier": "456b0260-846f-48b1-b6f9-76d066336c72",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/P1Y",
+            "modified": "2023-07-19T15:35:54.196374",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -41799,20 +41761,36 @@
                     }
                 }
             },
+            "references": [
+                "https://www2.ed.gov/admins/lead/safety/campus.html"
+            ],
+            "spatial": "United States",
+            "temporal": "2010/P1Y",
+            "title": "Campus Safety and Security Survey, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashley Higgins",
                 "hasEmail": "mailto:ashley.higgins@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Campus Safety and Security Survey, 2012 (CSSS 2012), is a data collection that is part of the Campus Safety and Security Survey (CSSS) program; program data is available since 2005 at <https://ope.ed.gov/security/GetDownloadFile.aspx>. CSSS 2012 (https://ope.ed.gov/security/) was a cross-sectional survey that collected information required for benefits about crime, criminal activity, and fire safety at postsecondary institutions in the United States. The collection was conducted through a web-based data entry system utilized by postsecondary institutions. All postsecondary institutions participating in Title IV funding were sampled. The collection's response rate was 100 percent. Key statistics produced from CSSS 2012 were on the number and types of crimes committed at responding postsecondary institutions and the number of fires on institution property.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Campus Safety and Security Survey Files",
                     "downloadURL": "https://ope.ed.gov/campussafety/#/datafile/list",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Campus Safety and Security Survey Files"
                 }
             ],
+            "identifier": "456b0260-846f-48b1-b6f9-76d066336c72",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "campus-safety",
@@ -41828,30 +41806,14 @@
                 "postsecondary-institutions",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www2.ed.gov/admins/lead/safety/campus.html"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Campus Safety and Security Survey, 2011",
-            "description": "The Campus Safety and Security Survey, 2011 (CSSS 2011), is a data collection that is part of the Campus Safety and Security Survey (CSSS) program; program data is available since 2005 at <https://ope.ed.gov/security/GetDownloadFile.aspx>. CSSS 2011 (https://ope.ed.gov/security/) was a cross-sectional survey that collected information required for benefits about crime, criminal activity, and fire safety at postsecondary institutions in the United States. The collection was conducted through a web-based data entry system utilized by postsecondary institutions. All postsecondary institutions participating in Title IV funding were sampled. The collection's response rate was 100 percent. Key statistics produced from CSSS 2011 were on the number and types of crimes committed at responding postsecondary institutions and the number of fires on institution property.",
-            "modified": "2023-07-19T15:35:52.871469",
-            "accessLevel": "public",
-            "identifier": "55816c9e-872e-4faa-ae3e-f95e69cb9978",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/P1Y",
+            "modified": "2023-07-19T15:35:53.432688",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -41872,20 +41834,36 @@
                     }
                 }
             },
+            "references": [
+                "https://www2.ed.gov/admins/lead/safety/campus.html"
+            ],
+            "spatial": "United States",
+            "temporal": "2012/P1Y",
+            "title": "Campus Safety and Security Survey, 2012"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashley Higgins",
                 "hasEmail": "mailto:ashley.higgins@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Campus Safety and Security Survey, 2011 (CSSS 2011), is a data collection that is part of the Campus Safety and Security Survey (CSSS) program; program data is available since 2005 at <https://ope.ed.gov/security/GetDownloadFile.aspx>. CSSS 2011 (https://ope.ed.gov/security/) was a cross-sectional survey that collected information required for benefits about crime, criminal activity, and fire safety at postsecondary institutions in the United States. The collection was conducted through a web-based data entry system utilized by postsecondary institutions. All postsecondary institutions participating in Title IV funding were sampled. The collection's response rate was 100 percent. Key statistics produced from CSSS 2011 were on the number and types of crimes committed at responding postsecondary institutions and the number of fires on institution property.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Campus Safety and Security Survey Files",
                     "downloadURL": "https://ope.ed.gov/campussafety/#/datafile/list",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Campus Safety and Security Survey Files"
                 }
             ],
+            "identifier": "55816c9e-872e-4faa-ae3e-f95e69cb9978",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "campus-safety",
@@ -41901,39 +41879,20 @@
                 "postsecondary-institutions",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www2.ed.gov/admins/lead/safety/campus.html"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Schools and Staffing Survey, 1999-2000",
-            "description": "The 1999-2000 Schools and Staffing Survey is a study that is part of the Schools and Staffing Survey (SASS) program; program data is available since 1987-88 at <https://nces.ed.gov/surveys/sass/dataproducts.asp>. SASS 99-00 (https://nces.ed.gov/surveys/sass) is a survey that covers a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers' perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention practices, to basic characteristics of the student population. The survey was conducted using mail, email, paper questionnaires, and telephone interviews. Teachers, librarians, principals, and school coordinators were sampled. Key statistics produced from SASS 99-00 are how many teachers and principals remained at the same school, moved to another school, or left the profession in the year following the SASS administration.",
-            "modified": "2023-07-19T15:35:52.314158",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "5736cf51-2e4f-41c0-8114-5f11d960b23d",
-            "dataQuality": true,
-            "issued": "2005-01-31",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1999/2000",
+            "modified": "2023-07-19T15:35:52.871469",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
+                "name": "Office of Postsecondary Education (OPE)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -41948,27 +41907,44 @@
                     }
                 }
             },
+            "references": [
+                "https://www2.ed.gov/admins/lead/safety/campus.html"
+            ],
+            "spatial": "United States",
+            "temporal": "2011/P1Y",
+            "title": "Campus Safety and Security Survey, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amy Ho",
                 "hasEmail": "mailto:amy.ho@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 1999-2000 Schools and Staffing Survey is a study that is part of the Schools and Staffing Survey (SASS) program; program data is available since 1987-88 at <https://nces.ed.gov/surveys/sass/dataproducts.asp>. SASS 99-00 (https://nces.ed.gov/surveys/sass) is a survey that covers a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers' perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention practices, to basic characteristics of the student population. The survey was conducted using mail, email, paper questionnaires, and telephone interviews. Teachers, librarians, principals, and school coordinators were sampled. Key statistics produced from SASS 99-00 are how many teachers and principals remained at the same school, moved to another school, or left the profession in the year following the SASS administration.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "1999-2000 SASS Public-Use Data and Documentation",
                     "description": "1999-2000 Schools and Staffing Survey public-use data files",
                     "downloadURL": "https://nces.ed.gov/surveys/sass/dataprod9901.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "1999-2000 SASS Public-Use Data and Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "1999-2000 Schools and Staffing Survey (SASS) and 2000-01 Teacher Follow-up Survey (TFS) (CD ROM) Restricted-Use Data with Electronic Codebook",
                     "description": "Restricted-use data file for the 1999\u00c3\u0192\u00c6\u2019\u00c3\u201a\u00c2\u00a2\u00c3\u0192\u00c2\u00a2\u00c3\u00a2\u00e2\u201a\u00ac\u00c5\u00a1\u00c3\u201a\u00c2\u00ac\u00c3\u0192\u00c2\u00a2\u00c3\u00a2\u00e2\u20ac\u0161\u00c2\u00ac\u00c3\u2026\u00e2\u20ac\u01532000 School and Staffing Survey",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009317",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "1999-2000 Schools and Staffing Survey (SASS) and 2000-01 Teacher Follow-up Survey (TFS) (CD ROM) Restricted-Use Data with Electronic Codebook"
                 }
             ],
+            "identifier": "5736cf51-2e4f-41c0-8114-5f11d960b23d",
+            "issued": "2005-01-31",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "charter-school",
@@ -41983,36 +41959,20 @@
                 "teacher-salaries",
                 "violence"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2004303"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "College Affordability and Transparency List Explanation Form, 2012-13",
-            "description": "College Affordability and Transparency List Explanation Form 2012-13 (CATEF 2012-13) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100% response rate. Key statistics produced from CATEF 2012-13 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of State government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
-            "modified": "2023-07-19T15:35:51.854886",
-            "accessLevel": "public",
-            "identifier": "605decc8-daa8-4d4f-a834-d1fc73590fe1",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/2011",
+            "modified": "2023-07-19T15:35:52.314158",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -42027,22 +41987,40 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2004303"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1999/2000",
+            "title": "Schools and Staffing Survey, 1999-2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "dataQuality": true,
+            "description": "College Affordability and Transparency List Explanation Form 2012-13 (CATEF 2012-13) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100% response rate. Key statistics produced from CATEF 2012-13 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of State government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel Document",
-                    "title": "CATClists2010.xls",
                     "description": "College Affordability and Transparency list data for the 2010-2011 academic year",
-                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2010.xls"
+                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2010.xls",
+                    "format": "Microsoft Excel Document",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "CATClists2010.xls"
                 }
             ],
+            "identifier": "605decc8-daa8-4d4f-a834-d1fc73590fe1",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "college-affordability",
@@ -42052,30 +42030,14 @@
                 "transparency-of-information",
                 "tuition-and-fees"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://collegecost.ed.gov/catc/resources/2012-13%20CATEF%20Summary%20Guide%20to%20College%20Costs.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "College Affordability and Transparency List Explanation Form, 2011-12",
-            "description": "College Affordability and Transparency List Explanation Form 2011-12 (CATEF 2011-12) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100% response rate. Key statistics produced from CATEF 2011-12 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of State government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
-            "modified": "2023-07-19T15:35:51.272710",
-            "accessLevel": "public",
-            "identifier": "406524f9-dc60-4211-b7c6-af4eb6073f62",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2009/2010",
+            "modified": "2023-07-19T15:35:51.854886",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -42096,22 +42058,38 @@
                     }
                 }
             },
+            "references": [
+                "https://collegecost.ed.gov/catc/resources/2012-13%20CATEF%20Summary%20Guide%20to%20College%20Costs.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2010/2011",
+            "title": "College Affordability and Transparency List Explanation Form, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "dataQuality": true,
+            "description": "College Affordability and Transparency List Explanation Form 2011-12 (CATEF 2011-12) is a cross-sectional data collection that collects information on the major areas of institutions' budgets with the greatest cost increases, the explanations for these increases, and the steps institutions have been or will be taking towards reducing these costs. The data collection is conducted on the subset of institutions that appear on the tuition and fees and/or net price increase lists for being in the five percent of institutions in their institutional sector that have the highest increases, expressed as a percentage change, over the three-year time period. This data collection is mandatory and expects a 100% response rate. Key statistics produced from CATEF 2011-12 are a description of the major areas in the institution's budget with the greatest cost increases; an explanation of the cost increases; a description of the steps the institution will take toward the goal of reducing costs in the areas described; an explanation of the extent to which the institution participates in determining such cost increase; the identification of the agency or instrumentality of State government responsible for determining such cost increase; and any other information the institution considers relevant to the report.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel Document",
-                    "title": "CATClists2011.xls",
                     "description": "College Affordability and Transparency list data for the 2011-2012 academic year",
-                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2011.xls"
+                    "downloadURL": "https://collegecost.ed.gov/wwwroot/documents/CATClists2011.xls",
+                    "format": "Microsoft Excel Document",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "CATClists2011.xls"
                 }
             ],
+            "identifier": "406524f9-dc60-4211-b7c6-af4eb6073f62",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "college-affordability",
@@ -42121,34 +42099,20 @@
                 "transparency-of-information",
                 "tuition-and-fees"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://collegecost.ed.gov/catc/resources/2011%20Affordability%20Summary%20Report.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Civil Rights Data Collection, 2013-14",
-            "description": "The Civil Rights Data Collection, 2013-14 (CRDC 2013-14) is part of the Civil Rights Data Collection (CRDC) program; program data are available beginning with the 2000 collection at <http://ocrdata.ed.gov/>. CRDC 2013-14 is a cross-sectional survey that collects data on key education and civil rights issues in the nation's public schools, which include student enrollment and educational programs and services, disaggregated by race/ethnicity, sex, limited English proficiency, and disability. LEAs submit administrative records about schools in the district. CRDC 2013-14 is a universe survey. Key statistics produced from CRDC 2013-14 can provide information about critical civil rights issues as well as contextual information on the state of civil rights in the nation, including enrollment demographics, advanced placement, school discipline, and special education services.",
-            "modified": "2023-07-19T00:57:49.420352",
-            "accessLevel": "public",
-            "identifier": "57a7b253-9e69-4f17-8797-09568363c1ac",
-            "dataQuality": true,
-            "issued": "2016-06-06",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/2014",
+            "modified": "2023-07-19T15:35:51.272710",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office for Civil Rights (OCR)",
+                "name": "Office of Postsecondary Education (OPE)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -42161,44 +42125,62 @@
                             }
                         }
                     }
+                }
+            },
+            "references": [
+                "https://collegecost.ed.gov/catc/resources/2011%20Affordability%20Summary%20Report.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2009/2010",
+            "title": "College Affordability and Transparency List Explanation Form, 2011-12"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Janis Brown",
                 "hasEmail": "mailto:ocrdata@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Civil Rights Data Collection, 2013-14 (CRDC 2013-14) is part of the Civil Rights Data Collection (CRDC) program; program data are available beginning with the 2000 collection at <http://ocrdata.ed.gov/>. CRDC 2013-14 is a cross-sectional survey that collects data on key education and civil rights issues in the nation's public schools, which include student enrollment and educational programs and services, disaggregated by race/ethnicity, sex, limited English proficiency, and disability. LEAs submit administrative records about schools in the district. CRDC 2013-14 is a universe survey. Key statistics produced from CRDC 2013-14 can provide information about critical civil rights issues as well as contextual information on the state of civil rights in the nation, including enrollment demographics, advanced placement, school discipline, and special education services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "School Search",
                     "description": "View and compare data across multiple schools and districts",
                     "downloadURL": "https://ocrdata.ed.gov/flex/Reports.aspx?type=school",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "School Search"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "District Search",
                     "description": "View and compare data across multiple schools and districts",
                     "downloadURL": "https://ocrdata.ed.gov/flex/Reports.aspx?type=district",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "District Search"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "School/District Search",
                     "description": "Find school- or district-level summaries; access all data for a single school or district",
                     "downloadURL": "https://ocrdata.ed.gov/DistrictSchoolSearch",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "School/District Search"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "crdc201314csv.zip",
                     "description": "Download the entire 2013-14 Civil Rights Data Collection data file via one .zip file",
-                    "downloadURL": "https://inventory.data.gov/dataset/2acc601e-9806-4dff-b144-f8a5e7c095b8/resource/3dc84a95-526a-4b90-aacd-72f60d4fecbc/download/crdc201314csv.zip"
+                    "downloadURL": "https://inventory.data.gov/dataset/2acc601e-9806-4dff-b144-f8a5e7c095b8/resource/3dc84a95-526a-4b90-aacd-72f60d4fecbc/download/crdc201314csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "crdc201314csv.zip"
                 }
             ],
+            "identifier": "57a7b253-9e69-4f17-8797-09568363c1ac",
+            "issued": "2016-06-06",
             "keyword": [
                 "519e6cdf-3011-4b75-9e12-34a45cb17fd8",
                 "advanced-placement",
@@ -42230,40 +42212,17 @@
                 "teacher-certification",
                 "teacher-experience"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-19T00:57:49.420352",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://ocrdata.ed.gov/Overview",
-                "https://ocrdata.ed.gov/downloads/UserGuide.pdf",
-                "https://ocrdata.ed.gov/downloads/FAQ.pdf",
-                "https://ocrdata.ed.gov/DataInfor1314"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Schools and Staffing Survey, 1990-91",
-            "description": "The Schools and Staffing Survey, 1990-91 (SASS 90-91), is a study that is part of the Schools and Staffing Survey (SASS) program; program data is available since 1987-88 at <https://nces.ed.gov/surveys/sass/dataproducts.asp>. SASS 90-91 (https://nces.ed.gov/surveys/sass) is a cross-sectional survey that covers a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers' perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention practices, to basic characteristics of the student population. The survey was conducted using mail, paper questionnaires, and telephone interviews. Teachers, librarians, principals, and school coordinators were sampled. Key statistics produced from SASS 90-91 are average teacher salaries and the percentage of teachers by teaching field.",
-            "modified": "2023-07-18T16:12:40.772621",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "f3a83825-84d5-42a4-8947-8e4852bea74d",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1990/1991",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                "name": "Office for Civil Rights (OCR)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -42276,28 +42235,46 @@
                         }
                     }
                 }
-                }
             },
+            "references": [
+                "https://ocrdata.ed.gov/Overview",
+                "https://ocrdata.ed.gov/downloads/UserGuide.pdf",
+                "https://ocrdata.ed.gov/downloads/FAQ.pdf",
+                "https://ocrdata.ed.gov/DataInfor1314"
+            ],
+            "spatial": "United States",
+            "temporal": "2013/2014",
+            "title": "Civil Rights Data Collection, 2013-14"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amy Ho",
                 "hasEmail": "mailto:amy.ho@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Schools and Staffing Survey, 1990-91 (SASS 90-91), is a study that is part of the Schools and Staffing Survey (SASS) program; program data is available since 1987-88 at <https://nces.ed.gov/surveys/sass/dataproducts.asp>. SASS 90-91 (https://nces.ed.gov/surveys/sass) is a cross-sectional survey that covers a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers' perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention practices, to basic characteristics of the student population. The survey was conducted using mail, paper questionnaires, and telephone interviews. Teachers, librarians, principals, and school coordinators were sampled. Key statistics produced from SASS 90-91 are average teacher salaries and the percentage of teachers by teaching field.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "SASS Restricted Use",
                     "downloadURL": "https://nces.ed.gov/surveys/sass/dataproducts.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "SASS Restricted Use"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "SASS downloads",
                     "downloadURL": "https://nces.ed.gov/surveys/sass",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "SASS downloads"
                 }
             ],
+            "identifier": "f3a83825-84d5-42a4-8947-8e4852bea74d",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "elementary",
@@ -42312,32 +42289,20 @@
                 "teacher-qualifications",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-18T16:12:40.772621",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal School Code List for Free Application for Federal Student Aid (FAFSA)",
-            "description": "The Federal School Code List contains the unique codes assigned by the Department of Education for schools participating in the Title IV federal student aid programs. Students can enter these codes on the Free Application for Federal Student Aid (FAFSA) to indicate which postsecondary schools they want to receive their financial application results. The Federal School Code List is a searchable document in Excel format. The list will be updated on the first of February, May, August, and November of each calendar year.",
-            "modified": "2023-07-18T16:12:40.356714",
-            "accessLevel": "public",
-            "identifier": "82004750-0c73-4af9-9e44-a83e6608a730",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Federal Student Aid (FSA)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -42352,20 +42317,34 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "1990/1991",
+            "title": "Schools and Staffing Survey, 1990-91"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Marini",
                 "hasEmail": "mailto:tara.marini@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Federal School Code List contains the unique codes assigned by the Department of Education for schools participating in the Title IV federal student aid programs. Students can enter these codes on the Free Application for Federal Student Aid (FAFSA) to indicate which postsecondary schools they want to receive their financial application results. The Federal School Code List is a searchable document in Excel format. The list will be updated on the first of February, May, August, and November of each calendar year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Federal School Code Lists",
                     "downloadURL": "https://fsapartners.ed.gov/knowledge-center/library/resource-type/Federal%20School%20Code%20Lists",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Federal School Code Lists"
                 }
             ],
+            "identifier": "82004750-0c73-4af9-9e44-a83e6608a730",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "college",
@@ -42373,29 +42352,20 @@
                 "student-loans",
                 "university"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-18T16:12:40.356714",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Guidance Documents Related to Sexual Harassment, Sexual Assault, and Retaliation in Schools",
-            "description": "These guidance documents were issued by the U.S. Department of Education Office for Civil Rights. This 2001 Sexual Harassment Guidance reaffirms the compliance standards that OCR applies in investigations and administrative enforcement of Title IX of the Education Amendments of 1972 regarding sexual harassment. The guidance provides the principles that a school should use to recognize and effectively respond to sexual harassment of students in its program as a condition of receiving Federal financial assistance. This 2011 Dear Colleague Letter on Sexual Violence explains that the requirements of Title IX of the Education Amendments of 1972 cover sexual violence and reminds schools of their responsibilities to take immediate and effective steps to respond to sexual violence in accordance with the requirements of Title IX. This 2013 Dear Colleague Letter on Retaliation reminds school districts, postsecondary institutions, and other recipients that retaliation is also a violation of Federal law. The letter seeks to clarify the basic principles of retaliation law and to describe OCR's methods of enforcement.",
-            "modified": "2023-07-18T16:12:39.883338",
-            "accessLevel": "public",
-            "identifier": "2be76e43-f2a6-4a62-a9ab-58bca4e41e71",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office for Civil Rights (OCR)",
+                "name": "Office of Federal Student Aid (FSA)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -42408,21 +42378,34 @@
                             }
                         }
                     }
+                }
+            },
+            "spatial": "United States",
+            "title": "Federal School Code List for Free Application for Federal Student Aid (FAFSA)"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Helen Boyer",
                 "hasEmail": "mailto:Helen.Boyer@ed.gov"
             },
+            "dataQuality": true,
+            "description": "These guidance documents were issued by the U.S. Department of Education Office for Civil Rights. This 2001 Sexual Harassment Guidance reaffirms the compliance standards that OCR applies in investigations and administrative enforcement of Title IX of the Education Amendments of 1972 regarding sexual harassment. The guidance provides the principles that a school should use to recognize and effectively respond to sexual harassment of students in its program as a condition of receiving Federal financial assistance. This 2011 Dear Colleague Letter on Sexual Violence explains that the requirements of Title IX of the Education Amendments of 1972 cover sexual violence and reminds schools of their responsibilities to take immediate and effective steps to respond to sexual violence in accordance with the requirements of Title IX. This 2013 Dear Colleague Letter on Retaliation reminds school districts, postsecondary institutions, and other recipients that retaliation is also a violation of Federal law. The letter seeks to clarify the basic principles of retaliation law and to describe OCR's methods of enforcement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://www2.ed.gov/about/offices/list/ocr/docs/shguide.html",
                     "format": "HTML",
-                    "title": "shguide.html",
-                    "downloadURL": "https://www2.ed.gov/about/offices/list/ocr/docs/shguide.html"
+                    "mediaType": "text/html",
+                    "title": "shguide.html"
                 }
             ],
+            "identifier": "2be76e43-f2a6-4a62-a9ab-58bca4e41e71",
             "keyword": [
                 "519e6cdf-3011-4b75-9e12-34a45cb17fd8",
                 "civil-rights",
@@ -42434,74 +42417,81 @@
                 "sexual-harassment",
                 "sexual-violence"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-18T16:12:39.883338",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Library Agencies Survey, Fiscal Year 2007",
-            "description": "The State Library Agencies Survey, Fiscal Year 2007 (StLA FY2007), is a study that is part of the State Library Agencies Survey. StLA FY2007 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2007 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 285 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
-            "modified": "2023-07-18T16:12:39.379371",
-            "accessLevel": "public",
-            "identifier": "e409521a-2f03-4c2a-985c-7aa40581f6b5",
-            "dataQuality": true,
-            "issued": "2008-09-30",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2007/2008",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Institute of Museum and Library Services",
+                "name": "Office for Civil Rights (OCR)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Secretary (OS)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "U.S. Department of Education",
                         "subOrganizationOf": {
                             "@type": "org:Organization",
                             "name": "U.S. Government"
                         }
+                    }
+                }
+            },
+            "spatial": "United States",
+            "title": "Guidance Documents Related to Sexual Harassment, Sexual Assault, and Retaliation in Schools"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The State Library Agencies Survey, Fiscal Year 2007 (StLA FY2007), is a study that is part of the State Library Agencies Survey. StLA FY2007 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2007 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 285 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "state_library_agency_survey download",
                     "downloadURL": "https://www.imls.gov/research/state_library_agency_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "state_library_agency_survey download"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "istla07a_acsii.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2007 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla07a_ascii.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla07a_ascii.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "istla07a_acsii.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "istla07a_sas.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2007 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla07a_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla07a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "istla07a_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped MDB",
-                    "title": "istla07a_access.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2007 data available in a zipped Microsoft Access Database file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla07a_access.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla07a_access.zip",
+                    "format": "Zipped MDB",
+                    "mediaType": "application/zip",
+                    "title": "istla07a_access.zip"
                 }
             ],
+            "identifier": "e409521a-2f03-4c2a-985c-7aa40581f6b5",
+            "issued": "2008-09-30",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "cosla",
@@ -42511,31 +42501,14 @@
                 "state-library-agency",
                 "stla"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2007.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Library Agencies Survey, Fiscal Year 2004",
-            "description": "The State Library Agencies Survey, Fiscal Year 2004 (StLA FY2004), is a study that is part of the State Library Agencies Survey.  StLA FY2004 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2004 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 339 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
-            "modified": "2023-07-18T16:12:38.906276",
-            "accessLevel": "public",
-            "identifier": "7bb809a6-45cf-4dc0-8efd-b0985d548a57",
-            "dataQuality": true,
-            "issued": "2005-07-12",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2004/2005",
+            "modified": "2023-07-18T16:12:39.379371",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -42544,44 +42517,61 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2007.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2007/2008",
+            "title": "State Library Agencies Survey, Fiscal Year 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The State Library Agencies Survey, Fiscal Year 2004 (StLA FY2004), is a study that is part of the State Library Agencies Survey.  StLA FY2004 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2004 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 339 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "state_library_agency_survey download",
                     "downloadURL": "https://www.imls.gov/research/state_library_agency_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "state_library_agency_survey download"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "istla04a_acsii.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2004 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla04a_ascii.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla04a_ascii.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "istla04a_acsii.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "istla04a_sas.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2004 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla04a_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla04a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "istla04a_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped MDB",
-                    "title": "istla04a_access.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2004 data available in a zipped Microsoft Access Database file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla04a_access.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla04a_access.zip",
+                    "format": "Zipped MDB",
+                    "mediaType": "application/zip",
+                    "title": "istla04a_access.zip"
                 }
             ],
+            "identifier": "7bb809a6-45cf-4dc0-8efd-b0985d548a57",
+            "issued": "2005-07-12",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "cosla",
@@ -42591,31 +42581,14 @@
                 "state-library-agency",
                 "stla"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2004.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Library Agencies Survey, Fiscal Year 2005",
-            "description": "The State Library Agencies Survey, Fiscal Year 2005 (StLA FY2005), is a study that is part of the State Library Agencies Survey. StLA FY2005 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2005 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 285 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
-            "modified": "2023-07-18T16:12:38.449087",
-            "accessLevel": "public",
-            "identifier": "3fbc7847-5659-40fd-91d4-1bdaf9fc5726",
-            "dataQuality": true,
-            "issued": "2006-12-31",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2005/2006",
+            "modified": "2023-07-18T16:12:38.906276",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -42624,44 +42597,61 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2004.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2004/2005",
+            "title": "State Library Agencies Survey, Fiscal Year 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The State Library Agencies Survey, Fiscal Year 2005 (StLA FY2005), is a study that is part of the State Library Agencies Survey. StLA FY2005 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2005 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 285 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "state_library_agency_survey download",
                     "downloadURL": "https://www.imls.gov/research/state_library_agency_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "state_library_agency_survey download"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "istla05a_acsii.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2005 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla05a_ascii.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla05a_ascii.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "istla05a_acsii.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "istla05a_sas.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2005 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla05a_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla05a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "istla05a_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped MDB",
-                    "title": "istla05a_access.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2005 data available in a zipped Microsoft Access Database file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla05a_access.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla05a_access.zip",
+                    "format": "Zipped MDB",
+                    "mediaType": "application/zip",
+                    "title": "istla05a_access.zip"
                 }
             ],
+            "identifier": "3fbc7847-5659-40fd-91d4-1bdaf9fc5726",
+            "issued": "2006-12-31",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "cosla",
@@ -42671,65 +42661,52 @@
                 "state-library-agency",
                 "stla"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2005.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Schools and Staffing Survey, 1987-88",
-            "description": "The Schools and Staffing Survey, 1987-88 (SASS 87-88), is the first year of the Schools and Staffing Survey (SASS) program. Program data are available since 1987-88 at <https://nces.ed.gov/surveys/sass/dataproducts.asp>. SASS 87-88 is a system of surveys that cover a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers'perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention policies, to basic characteristics of the student population. The surveys were conducted using mail, paper questionnaires, and telephone interviews. Teachers, principals, school district coordinators and school coordinators were sampled. Key statistics produced from SASS 87-88 are average teacher salaries and the percentage of teachers by teaching field. Key statistics from the follow-up to SASS 87-88 (TFS 88-89) are the percentage of teachers staying at the same school, moving to a new school, or leaving the teaching profession. Prior to the founding of SASS in 1987-88, there were three sets of Elementary and Secondary School Division surveys administered by the National Center for Education Statistics in different years: the \u201cTeacher Demand and Shortage Surveys, & the \u201cPublic and Private School Surveys,and the \u201cTeacher Surveys. The public and private sector versions of each of these three survey types were conducted in alternate years.",
-            "modified": "2023-07-18T16:12:38.020647",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "a99339b5-b46c-49fa-bf2c-ed12fed32749",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1987/1988",
+            "modified": "2023-07-18T16:12:38.449087",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "Office of the Secretary (OS)",
-                        "subOrganizationOf": {
-                            "@type": "org:Organization",
-                            "name": "U.S. Department of Education",
+                "name": "Institute of Museum and Library Services",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "U.S. Government"
                 }
-                        }
-                    }
-                }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2005.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2005/2006",
+            "title": "State Library Agencies Survey, Fiscal Year 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amy Ho",
                 "hasEmail": "mailto:amy.ho@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Schools and Staffing Survey, 1987-88 (SASS 87-88), is the first year of the Schools and Staffing Survey (SASS) program. Program data are available since 1987-88 at <https://nces.ed.gov/surveys/sass/dataproducts.asp>. SASS 87-88 is a system of surveys that cover a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers'perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention policies, to basic characteristics of the student population. The surveys were conducted using mail, paper questionnaires, and telephone interviews. Teachers, principals, school district coordinators and school coordinators were sampled. Key statistics produced from SASS 87-88 are average teacher salaries and the percentage of teachers by teaching field. Key statistics from the follow-up to SASS 87-88 (TFS 88-89) are the percentage of teachers staying at the same school, moving to a new school, or leaving the teaching profession. Prior to the founding of SASS in 1987-88, there were three sets of Elementary and Secondary School Division surveys administered by the National Center for Education Statistics in different years: the \u201cTeacher Demand and Shortage Surveys, & the \u201cPublic and Private School Surveys,and the \u201cTeacher Surveys. The public and private sector versions of each of these three survey types were conducted in alternate years.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "SASS Restricted Use",
                     "downloadURL": "https://nces.ed.gov/surveys/sass/dataproducts.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "SASS Restricted Use"
                 }
             ],
+            "identifier": "a99339b5-b46c-49fa-bf2c-ed12fed32749",
             "keyword": [
                 "2112b71e-c6b5-4c18-aa9a-76eca458c84c",
                 "elementary",
@@ -42744,74 +42721,87 @@
                 "teacher-qualifications",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-18T16:12:38.020647",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Library Agencies Survey, Fiscal Year 2003",
-            "description": "The State Library Agencies Survey, Fiscal Year 2003 (StLA FY2003), is a study that is part of the State Library Agencies Survey.  StLA FY2003 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2003 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 436 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
-            "modified": "2023-07-18T16:12:37.513600",
-            "accessLevel": "public",
-            "identifier": "96c21b52-82bd-4444-acfa-ead34c287c85",
-            "dataQuality": true,
-            "issued": "2005-02-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2003/2004",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Institute of Museum and Library Services",
+                "name": "National Center for Education Statistics (NCES)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Institute of Education Sciences (IES)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Secretary (OS)",
+                        "subOrganizationOf": {
+                            "@type": "org:Organization",
+                            "name": "U.S. Department of Education",
                             "subOrganizationOf": {
                                 "@type": "org:Organization",
                                 "name": "U.S. Government"
                             }
+                        }
+                    }
+                }
+            },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "1987/1988",
+            "title": "Schools and Staffing Survey, 1987-88"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The State Library Agencies Survey, Fiscal Year 2003 (StLA FY2003), is a study that is part of the State Library Agencies Survey.  StLA FY2003 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2003 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 436 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "state_library_agency_survey download",
                     "downloadURL": "https://www.imls.gov/research/state_library_agency_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "state_library_agency_survey download"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "istla03b_acsii.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2003 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla03b_ascii.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla03b_ascii.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "istla03b_acsii.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "istla03b_sas.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2003 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla03b_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla03b_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "istla03b_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped MDB",
-                    "title": "istla03b_access.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2003 data available in a zipped Microsoft Access Database file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla03b_access.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla03b_access.zip",
+                    "format": "Zipped MDB",
+                    "mediaType": "application/zip",
+                    "title": "istla03b_access.zip"
                 }
             ],
+            "identifier": "96c21b52-82bd-4444-acfa-ead34c287c85",
+            "issued": "2005-02-01",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "cosla",
@@ -42821,31 +42811,14 @@
                 "state-library-agency",
                 "stla"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2003.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Library Agencies Survey, Fiscal Year 2002",
-            "description": "The State Library Agencies Survey, Fiscal Year 2002 (StLA FY2002), is a study that is part of the State Library Agencies Survey.  StLA FY2002 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2002 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 436 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
-            "modified": "2023-07-18T16:12:37.035829",
-            "accessLevel": "public",
-            "identifier": "70423a6c-2715-410c-84ea-bce0a3aecd7b",
-            "dataQuality": true,
-            "issued": "2004-03-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2002/2003",
+            "modified": "2023-07-18T16:12:37.513600",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -42854,44 +42827,61 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2003.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2003/2004",
+            "title": "State Library Agencies Survey, Fiscal Year 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The State Library Agencies Survey, Fiscal Year 2002 (StLA FY2002), is a study that is part of the State Library Agencies Survey.  StLA FY2002 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2002 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 436 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "state_library_agency_survey download",
                     "downloadURL": "https://www.imls.gov/research/state_library_agency_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "state_library_agency_survey download"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "istla02a_acsii.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2002 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla02a_ascii.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla02a_ascii.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "istla02a_acsii.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "istla02a_sas.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2002 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla02a_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla02a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "istla02a_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped MDB",
-                    "title": "istla02a_access.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2002 data available in a zipped Microsoft Access Database file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla02a_access.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla02a_access.zip",
+                    "format": "Zipped MDB",
+                    "mediaType": "application/zip",
+                    "title": "istla02a_access.zip"
                 }
             ],
+            "identifier": "70423a6c-2715-410c-84ea-bce0a3aecd7b",
+            "issued": "2004-03-01",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "cosla",
@@ -42901,31 +42891,14 @@
                 "state-library-agency",
                 "stla"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2002.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public Libraries Survey, Fiscal Year 2003",
-            "description": "The Public Libraries Survey, Fiscal Year 2003 (PLS FY2003), is a study that is part of the Library Statistics program. PLS FY2003 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional study that includes information on population of legal service area, service outlets, public service hours, library materials, total circulation, circulation of children's materials, reference transactions, library visits, children's program attendance, interlibrary loans, electronic services and information, full-time-equivalent staff, operating revenue and expenditures, and capital expenditures. The study was conducted using paper surveys, web-based surveys, and email. The key respondents in this study were state library agencies. The study's response rate was 97.2 percent. The key statistics produced from PLS FY2003 were about service measures such as access to the Internet, number of users of electronic resources, number of internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating revenue and expenditures, type of geographic service area, type of legal basis, type of administrative structure, number and type of public library service outlets, and square footage of outlets.",
-            "modified": "2023-07-18T16:12:36.550378",
-            "accessLevel": "public",
-            "identifier": "4ec71f30-7a28-4400-940f-7cbfc1a2ab7a",
-            "dataQuality": true,
-            "issued": "2005-06-10",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2003/2004",
+            "modified": "2023-07-18T16:12:37.035829",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -42934,52 +42907,69 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2002.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2002/2003",
+            "title": "State Library Agencies Survey, Fiscal Year 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Public Libraries Survey, Fiscal Year 2003 (PLS FY2003), is a study that is part of the Library Statistics program. PLS FY2003 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional study that includes information on population of legal service area, service outlets, public service hours, library materials, total circulation, circulation of children's materials, reference transactions, library visits, children's program attendance, interlibrary loans, electronic services and information, full-time-equivalent staff, operating revenue and expenditures, and capital expenditures. The study was conducted using paper surveys, web-based surveys, and email. The key respondents in this study were state library agencies. The study's response rate was 97.2 percent. The key statistics produced from PLS FY2003 were about service measures such as access to the Internet, number of users of electronic resources, number of internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating revenue and expenditures, type of geographic service area, type of legal basis, type of administrative structure, number and type of public library service outlets, and square footage of outlets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "public_libraries_in_the_united_states_survey downloads",
                     "downloadURL": "https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "public_libraries_in_the_united_states_survey downloads"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "pupld03a_csv.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2003 data available in a zipped CSV file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld03a_csv.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld03a_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "pupld03a_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "pupld03a_xls.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2003 data available in a zipped Microsoft Excel file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld03a_xls.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld03a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "pupld03a_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "pupld03a_ASCII.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2003 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld03a_ASCII.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld03a_ASCII.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "pupld03a_ASCII.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "pupld03a_sas.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2003 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld03a_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld03a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "pupld03a_sas.zip"
                 }
             ],
+            "identifier": "4ec71f30-7a28-4400-940f-7cbfc1a2ab7a",
+            "issued": "2005-06-10",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "librarians",
@@ -42989,31 +42979,14 @@
                 "library-system",
                 "public-library"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-18T16:12:36.550378",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/fy2003_pls_database_documentation.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Library Agencies Survey, Fiscal Year 2000",
-            "description": "The State Library Agencies Survey, Fiscal Year 2000 (StLA FY2000), is a study that is part of the State Library Agencies Survey program. StLA FY2000 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2000 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 423 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information). The study's response rate was 100 percent",
-            "modified": "2023-07-18T16:12:35.996250",
-            "accessLevel": "public",
-            "identifier": "c4f5c605-b85e-4925-bce6-d02c89a5552b",
-            "dataQuality": true,
-            "issued": "2001-11-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2000/2001",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -43022,44 +42995,61 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/fy2003_pls_database_documentation.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2003/2004",
+            "title": "Public Libraries Survey, Fiscal Year 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The State Library Agencies Survey, Fiscal Year 2000 (StLA FY2000), is a study that is part of the State Library Agencies Survey program. StLA FY2000 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2000 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 423 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information). The study's response rate was 100 percent",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "state-library-administrative-agency-survey Download",
                     "downloadURL": "https://www.imls.gov/research-evaluation/data-collection/state-library-administrative-agency-survey",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "state-library-administrative-agency-survey Download"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "stla00b_ASCII.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2000 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/stla00b_ASCII.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/stla00b_ASCII.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "stla00b_ASCII.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "istla00a_sas.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2000 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla00a_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla00a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "istla00a_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped MDB",
-                    "title": "stla00b_Access.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2000 data available in a zipped Microsoft Access Database file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/stla00b_Access.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/stla00b_Access.zip",
+                    "format": "Zipped MDB",
+                    "mediaType": "application/zip",
+                    "title": "stla00b_Access.zip"
                 }
             ],
+            "identifier": "c4f5c605-b85e-4925-bce6-d02c89a5552b",
+            "issued": "2001-11-01",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "cosla",
@@ -43069,31 +43059,14 @@
                 "state-library-agency",
                 "stla"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2000.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Library Agencies Survey, Fiscal Year 2001",
-            "description": "The State Library Agencies Survey, Fiscal Year 2001 (StLA FY2001), is a study that is part of the State Library Agencies Survey.  StLA FY2001 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2001 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 423 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
-            "modified": "2023-07-18T16:12:35.550620",
-            "accessLevel": "public",
-            "identifier": "9d39c2ed-ea28-4047-8861-83c703a13ff6",
-            "dataQuality": true,
-            "issued": "2002-10-25",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2001/2002",
+            "modified": "2023-07-18T16:12:35.996250",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -43102,44 +43075,61 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2000.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2000/2001",
+            "title": "State Library Agencies Survey, Fiscal Year 2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The State Library Agencies Survey, Fiscal Year 2001 (StLA FY2001), is a study that is part of the State Library Agencies Survey.  StLA FY2001 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2001 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 423 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "state_library_agency_survey download",
                     "downloadURL": "https://www.imls.gov/research/state_library_agency_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "state_library_agency_survey download"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "stla01b_ASCII.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2001 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/stla01b_ASCII.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/stla01b_ASCII.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "stla01b_ASCII.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "istla01a_sas.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2001 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla01a_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla01a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "istla01a_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped MDB",
-                    "title": "stla01b_Access.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2001 data available in a zipped Microsoft Access Database file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/stla01b_Access.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/stla01b_Access.zip",
+                    "format": "Zipped MDB",
+                    "mediaType": "application/zip",
+                    "title": "stla01b_Access.zip"
                 }
             ],
+            "identifier": "9d39c2ed-ea28-4047-8861-83c703a13ff6",
+            "issued": "2002-10-25",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "cosla",
@@ -43149,31 +43139,14 @@
                 "state-library-agency",
                 "stla"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2001.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public Libraries Survey, Fiscal Year 2007",
-            "description": "The Public Libraries Survey, Fiscal Year 2007 (PLS FY2007), is a study that is part of the Library Statistics program. PLS FY2007 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional study that includes information on population of legal service area, service outlets, public service hours, library materials, total circulation, circulation of children's materials, reference transactions, library visits, children's program attendance, interlibrary loans, electronic services and information, full-time-equivalent staff, operating revenue and expenditures, and capital expenditures. The study was conducted using paper surveys, web-based surveys, and email. The key respondents in this study were state library agencies. The study's response rate was 97.7 percent. The key statistics produced from PLS FY2007 were about service measures such as access to the Internet, number of users of electronic resources, number of internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating revenue and expenditures, type of geographic service area, type of legal basis, type of administrative structure, number and type of public library service outlets, and square footage of outlets.",
-            "modified": "2023-07-18T16:12:34.596510",
-            "accessLevel": "public",
-            "identifier": "9388c1fb-4d9e-4578-81ec-381c203677bd",
-            "dataQuality": true,
-            "issued": "2009-06-30",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2006/2007",
+            "modified": "2023-07-18T16:12:35.550620",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -43182,36 +43155,53 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2001.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2001/2002",
+            "title": "State Library Agencies Survey, Fiscal Year 2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Public Libraries Survey, Fiscal Year 2007 (PLS FY2007), is a study that is part of the Library Statistics program. PLS FY2007 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional study that includes information on population of legal service area, service outlets, public service hours, library materials, total circulation, circulation of children's materials, reference transactions, library visits, children's program attendance, interlibrary loans, electronic services and information, full-time-equivalent staff, operating revenue and expenditures, and capital expenditures. The study was conducted using paper surveys, web-based surveys, and email. The key respondents in this study were state library agencies. The study's response rate was 97.7 percent. The key statistics produced from PLS FY2007 were about service measures such as access to the Internet, number of users of electronic resources, number of internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating revenue and expenditures, type of geographic service area, type of legal basis, type of administrative structure, number and type of public library service outlets, and square footage of outlets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "public_libraries_in_the_united_states_survey downloads",
                     "downloadURL": "https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "public_libraries_in_the_united_states_survey downloads"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "pupld07a_csv.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2007 in a zipped CSV file",
-                    "downloadURL": "https://www.imls.gov/assests/1/AssetManager/pupld07a_csv.zip"
+                    "downloadURL": "https://www.imls.gov/assests/1/AssetManager/pupld07a_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "pupld07a_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "pupld07a_xls.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2007 in a zipped Microsoft excel file",
-                    "downloadURL": "https://www.imls.gov/assests/1/AssetManager/pupld07a_xls.zip"
+                    "downloadURL": "https://www.imls.gov/assests/1/AssetManager/pupld07a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "pupld07a_xls.zip"
                 }
             ],
+            "identifier": "9388c1fb-4d9e-4578-81ec-381c203677bd",
+            "issued": "2009-06-30",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "librarians",
@@ -43221,31 +43211,14 @@
                 "library-system",
                 "public-library"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/PLS2007.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Library Agencies Survey, Fiscal Year 2006",
-            "description": "The State Library Agencies Survey, Fiscal Year 2006 (StLA FY2006), is a study that is part of the State Library Agencies Survey. StLA FY2006 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2006 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 285 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
-            "modified": "2023-07-18T16:12:34.154530",
-            "accessLevel": "public",
-            "identifier": "b3c00f36-8a84-4783-8ac2-5c8148b47309",
-            "dataQuality": true,
-            "issued": "2007-11-30",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2006/2007",
+            "modified": "2023-07-18T16:12:34.596510",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -43254,44 +43227,61 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/PLS2007.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2006/2007",
+            "title": "Public Libraries Survey, Fiscal Year 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The State Library Agencies Survey, Fiscal Year 2006 (StLA FY2006), is a study that is part of the State Library Agencies Survey. StLA FY2006 (https://www.imls.gov/research/state_library_agency_survey.aspx) is a cross-sectional survey that that provides state and federal policymakers and other interested user with information about state library agencies. StLA FY2006 collects data on state library agency services to public, academic, and school libraries, and library systems, overall this data will help to complete the national picture of library service.   The study was conducted using Web survey application via Internet Web- based reporting system of 285 items (state library agency identification, governance, public service hours. Service outlets, collections, library service transactions, library development transactions, services to other libraries in the state, allied operations, staff, income, expenditures, and electronic services and information), from all 50 states and the District of Columbia.  The response rate for this study was 100 percent.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "state_library_agency_survey download",
                     "downloadURL": "https://www.imls.gov/research/state_library_agency_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "state_library_agency_survey download"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "istla06a_acsii.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2006 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla06a_ascii.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla06a_ascii.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "istla06a_acsii.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "istla06a_sas.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2006 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla06a_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla06a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "istla06a_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped MDB",
-                    "title": "istla06a_access.zip",
                     "description": "State Library Agencies Survey, Fiscal Year 2006 data available in a zipped Microsoft Access Database file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla06a_access.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/istla06a_access.zip",
+                    "format": "Zipped MDB",
+                    "mediaType": "application/zip",
+                    "title": "istla06a_access.zip"
                 }
             ],
+            "identifier": "b3c00f36-8a84-4783-8ac2-5c8148b47309",
+            "issued": "2007-11-30",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "cosla",
@@ -43301,31 +43291,14 @@
                 "state-library-agency",
                 "stla"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2006.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public Libraries Survey, Fiscal Year 2006",
-            "description": "The Public Libraries Survey, Fiscal Year 2006 (PLS FY2006), is a study that is part of the Library Statistics program. PLS FY2006 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional study that includes information on population of legal service area, service outlets, public service hours, library materials, total circulation, circulation of children's materials, reference transactions, library visits, children's program attendance, interlibrary loans, electronic services and information, full-time-equivalent staff, operating revenue and expenditures, and capital expenditures. The study was conducted using paper surveys, web-based surveys, and email. The key respondents in this study were state library agencies. The study's response rate was 97.7 percent. The key statistics produced from PLS FY2006 were about service measures such as access to the Internet, number of users of electronic resources, number of internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating revenue and expenditures, type of geographic service area, type of legal basis, type of administrative structure, number and type of public library service outlets, and square footage of outlets.",
-            "modified": "2023-07-18T16:12:33.721322",
-            "accessLevel": "public",
-            "identifier": "f85d7dca-bb19-4ffe-afbf-f6a81f14b031",
-            "dataQuality": true,
-            "issued": "2008-12-31",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2005/2006",
+            "modified": "2023-07-18T16:12:34.154530",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -43334,36 +43307,53 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/StLADataDoc2006.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2006/2007",
+            "title": "State Library Agencies Survey, Fiscal Year 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Public Libraries Survey, Fiscal Year 2006 (PLS FY2006), is a study that is part of the Library Statistics program. PLS FY2006 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional study that includes information on population of legal service area, service outlets, public service hours, library materials, total circulation, circulation of children's materials, reference transactions, library visits, children's program attendance, interlibrary loans, electronic services and information, full-time-equivalent staff, operating revenue and expenditures, and capital expenditures. The study was conducted using paper surveys, web-based surveys, and email. The key respondents in this study were state library agencies. The study's response rate was 97.7 percent. The key statistics produced from PLS FY2006 were about service measures such as access to the Internet, number of users of electronic resources, number of internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating revenue and expenditures, type of geographic service area, type of legal basis, type of administrative structure, number and type of public library service outlets, and square footage of outlets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "public_libraries_in_the_united_states_survey downloads",
                     "downloadURL": "https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "public_libraries_in_the_united_states_survey downloads"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "pupld06a_csv.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2006 in a zipped CSV file",
-                    "downloadURL": "https://www.imls.gov/assests/1/AssetManager/pupld06a_csv.zip"
+                    "downloadURL": "https://www.imls.gov/assests/1/AssetManager/pupld06a_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "pupld06a_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "pupld06a_xls.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2006 in a zipped Microsoft excel file",
-                    "downloadURL": "https://www.imls.gov/assests/1/AssetManager/pupld06a_xls.zip"
+                    "downloadURL": "https://www.imls.gov/assests/1/AssetManager/pupld06a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "pupld06a_xls.zip"
                 }
             ],
+            "identifier": "f85d7dca-bb19-4ffe-afbf-f6a81f14b031",
+            "issued": "2008-12-31",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "librarians",
@@ -43373,31 +43363,14 @@
                 "library-system",
                 "public-library"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/ccd/pdf/stnfis01gen.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public Libraries Survey, Fiscal Year 2005",
-            "description": "The Public Libraries Survey, Fiscal Year 2005 (PLS FY2005), is a study that is part of the Library Statistics program. PLS FY2005 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional study that includes information on population of legal service area, service outlets, public service hours, library materials, total circulation, circulation of children's materials, reference transactions, library visits, children's program attendance, interlibrary loans, electronic services and information, full-time-equivalent staff, operating revenue and expenditures, and capital expenditures. The study was conducted using paper surveys, web-based surveys, and email. The key respondents in this study were state library agencies. The study's response rate was 97.7 percent. The key statistics produced from PLS FY2005 were about service measures such as access to the Internet, number of users of electronic resources, number of internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating revenue and expenditures, type of geographic service area, type of legal basis, type of administrative structure, number and type of public library service outlets, and square footage of outlets.",
-            "modified": "2023-07-18T16:12:33.229028",
-            "accessLevel": "public",
-            "identifier": "b1aecf01-98fc-4964-9507-baccedb24b1f",
-            "dataQuality": true,
-            "issued": "2007-11-07",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2005/2006",
+            "modified": "2023-07-18T16:12:33.721322",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -43406,52 +43379,69 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://nces.ed.gov/ccd/pdf/stnfis01gen.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2005/2006",
+            "title": "Public Libraries Survey, Fiscal Year 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Public Libraries Survey, Fiscal Year 2005 (PLS FY2005), is a study that is part of the Library Statistics program. PLS FY2005 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional study that includes information on population of legal service area, service outlets, public service hours, library materials, total circulation, circulation of children's materials, reference transactions, library visits, children's program attendance, interlibrary loans, electronic services and information, full-time-equivalent staff, operating revenue and expenditures, and capital expenditures. The study was conducted using paper surveys, web-based surveys, and email. The key respondents in this study were state library agencies. The study's response rate was 97.7 percent. The key statistics produced from PLS FY2005 were about service measures such as access to the Internet, number of users of electronic resources, number of internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating revenue and expenditures, type of geographic service area, type of legal basis, type of administrative structure, number and type of public library service outlets, and square footage of outlets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "public_libraries_in_the_united_states_survey downloads",
                     "downloadURL": "https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "public_libraries_in_the_united_states_survey downloads"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "pupld05a_csv.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2005 data available in a zipped CSV file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld05a_csv.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld05a_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "pupld05a_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "pupld05a_xls.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2005 data available in a zipped Microsoft Excel file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld05a_xls.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld05a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "pupld05a_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "pupld05a_ASCII.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2005 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld05a_ASCII.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld05a_ASCII.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "pupld05a_ASCII.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "pupld05a_sas.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2005 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld05a_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld05a_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "pupld05a_sas.zip"
                 }
             ],
+            "identifier": "b1aecf01-98fc-4964-9507-baccedb24b1f",
+            "issued": "2007-11-07",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "librarians",
@@ -43461,31 +43451,14 @@
                 "library-system",
                 "public-library"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/fy2005_pls_database_documentation.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public Libraries Survey, Fiscal Year 2004",
-            "description": "The Public Libraries Survey, Fiscal Year 2004 (PLS FY2004), is a study that is part of the Library Statistics program. PLS FY2004 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional study that includes information on population of legal service area, service outlets, public service hours, library materials, total circulation, circulation of children's materials, reference transactions, library visits, children's program attendance, interlibrary loans, electronic services and information, full-time-equivalent staff, operating revenue and expenditures, and capital expenditures. The study was conducted using paper surveys, web-based surveys, and email. The key respondents in this study were state library agencies. The study's response rate was 97.7 percent. The key statistics produced from PLS FY2004 were about service measures such as access to the Internet, number of users of electronic resources, number of internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating revenue and expenditures, type of geographic service area, type of legal basis, type of administrative structure, number and type of public library service outlets, and square footage of outlets.",
-            "modified": "2023-07-18T16:12:32.741252",
-            "accessLevel": "public",
-            "identifier": "d522d7eb-8cb7-4c19-bd4b-8257f5c5aadc",
-            "dataQuality": true,
-            "issued": "2006-08-10",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2004/2005",
+            "modified": "2023-07-18T16:12:33.229028",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -43494,52 +43467,69 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/fy2005_pls_database_documentation.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2005/2006",
+            "title": "Public Libraries Survey, Fiscal Year 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Public Libraries Survey, Fiscal Year 2004 (PLS FY2004), is a study that is part of the Library Statistics program. PLS FY2004 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional study that includes information on population of legal service area, service outlets, public service hours, library materials, total circulation, circulation of children's materials, reference transactions, library visits, children's program attendance, interlibrary loans, electronic services and information, full-time-equivalent staff, operating revenue and expenditures, and capital expenditures. The study was conducted using paper surveys, web-based surveys, and email. The key respondents in this study were state library agencies. The study's response rate was 97.7 percent. The key statistics produced from PLS FY2004 were about service measures such as access to the Internet, number of users of electronic resources, number of internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating revenue and expenditures, type of geographic service area, type of legal basis, type of administrative structure, number and type of public library service outlets, and square footage of outlets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "public_libraries_in_the_united_states_survey downloads",
                     "downloadURL": "https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "public_libraries_in_the_united_states_survey downloads"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "pupld04a_csv.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2004 data available in a zipped CSV file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld04a_csv.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld04a_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "pupld04a_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "pupld04a_xls.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2004 data available in a zipped Microsoft Excel file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld04a_xls.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld04a_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "pupld04a_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "pupld04a_ASCII.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2004 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld04a_ASCII.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld04a_ASCII.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "pupld04a_ASCII.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "pupld04b_sas.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2004 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld04b_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld04b_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "pupld04b_sas.zip"
                 }
             ],
+            "identifier": "d522d7eb-8cb7-4c19-bd4b-8257f5c5aadc",
+            "issued": "2006-08-10",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "librarians",
@@ -43549,31 +43539,14 @@
                 "library-system",
                 "public-library"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/fy2004_pls_database_documentation.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public Libraries Survey, Fiscal Year 2002",
-            "description": "The Public Libraries Survey, Fiscal Year 2002 (PLS FY2002), is a study that is part of the Library Statistics program. PLS FY2002 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional survey that collects annual descriptive data on the universe of public libraries in the U.S. and the Outlying Areas.  Information such as public service hours per year, circulation of library books, etc., number of librarians, population of legal service area, expenditures for library collection, staff salary data, and access to technology are collected. The study was conducted using paper surveys. The key respondents in this study were state library agencies. The study's response rate was 98.1 percent. The key statistics produced from PLS FY2002 were about service measures such as access to the Internet, number of users of electronic resources, other electronic services, number of Internet terminals used by staff only, number of Internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating income and expenditures, type of geographic service area, type of legal basis, type of administrative structure, and number and type of public library service outlets.",
-            "modified": "2023-07-18T16:12:32.258337",
-            "accessLevel": "public",
-            "identifier": "04f3c6a9-d1bf-40b6-9dde-ac4e2b7d50f3",
-            "dataQuality": true,
-            "issued": "2002-11-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2002/2003",
+            "modified": "2023-07-18T16:12:32.741252",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Institute of Museum and Library Services",
@@ -43582,52 +43555,69 @@
                     "name": "U.S. Government"
                 }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/fy2004_pls_database_documentation.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2004/2005",
+            "title": "Public Libraries Survey, Fiscal Year 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Public Libraries Survey, Fiscal Year 2002 (PLS FY2002), is a study that is part of the Library Statistics program. PLS FY2002 (https://www.imls.gov/research/public_libraries_in_the_united_states_survey.aspx) is a cross-sectional survey that collects annual descriptive data on the universe of public libraries in the U.S. and the Outlying Areas.  Information such as public service hours per year, circulation of library books, etc., number of librarians, population of legal service area, expenditures for library collection, staff salary data, and access to technology are collected. The study was conducted using paper surveys. The key respondents in this study were state library agencies. The study's response rate was 98.1 percent. The key statistics produced from PLS FY2002 were about service measures such as access to the Internet, number of users of electronic resources, other electronic services, number of Internet terminals used by staff only, number of Internet terminals used by the general public, reference transactions, public service hours, interlibrary loans, circulation, library visits, children's program attendance, and circulation of children's materials. It also includes information about size of collection, staffing, operating income and expenditures, type of geographic service area, type of legal basis, type of administrative structure, and number and type of public library service outlets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "public-libraries-survey- downloads",
                     "downloadURL": "https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "public-libraries-survey- downloads"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "pupld02b_csv.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2002 data available in a zipped CSV file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld02b_csv.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld02b_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "pupld02b_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped XLS",
-                    "title": "pupld02b_xls.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2002 data available in a zipped Microsoft Excel file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld02b_xls.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld02b_xls.zip",
+                    "format": "Zipped XLS",
+                    "mediaType": "application/zip",
+                    "title": "pupld02b_xls.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped text",
-                    "title": "PUPLD02b_ASCII.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2002 data available in a zipped text file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/PUPLD02b_ASCII.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/PUPLD02b_ASCII.zip",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip",
+                    "title": "PUPLD02b_ASCII.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "pupld02b_sas.zip",
                     "description": "Public Libraries Survey, Fiscal Year 2002 data available in a zipped SAS file",
-                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld02b_sas.zip"
+                    "downloadURL": "https://www.imls.gov/assets/1/AssetManager/pupld02b_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "pupld02b_sas.zip"
                 }
             ],
+            "identifier": "04f3c6a9-d1bf-40b6-9dde-ac4e2b7d50f3",
+            "issued": "2002-11-01",
             "keyword": [
                 "0c7a3027-6d0b-4199-a454-1fbf3b9480f5",
                 "librarians",
@@ -43637,63 +43627,51 @@
                 "library-system",
                 "public-library"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-18T16:12:32.258337",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.imls.gov/assets/1/AssetManager/fy2002_pls_database_documentation.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Trends in International Mathematics and Science Study, 2015",
-            "description": "The Trends in International Mathematics and Science Study, 2015 (TIMSS 2015) is a data collection that is part of the Trends in International Mathematics and Science Study (TIMSS) program; program data are available since 1999 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=073>. TIMSS 2015 (https://nces.ed.gov/timss/) is a cross-sectional study that provides international comparative information of the mathematics and science literacy of fourth-, eighth-, and twelfth-grade students and examines factors that may be associated with the acquisition of math and science literacy in students. The study was conducted using direct assessments of students and questionnaires for students, teachers, and school administrators. Fourth-, eighth-, and twelfth-graders in the 2014-15 school year were sampled. Key statistics produced from TIMSS 2015 provide reliable and timely data on the mathematics and science achievement of U.S. students compared to that of students in other countries. Data are expected to be released in 2018.",
-            "modified": "2023-07-10T15:50:33.035400",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "2c75d51d-0c09-4b37-abde-ba96cdac2465",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "Office of the Secretary (OS)",
-                        "subOrganizationOf": {
-                            "@type": "org:Organization",
-                            "name": "U.S. Department of Education",
+                "name": "Institute of Museum and Library Services",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "U.S. Government"
                 }
-                        }
-                    }
-                }
             },
+            "references": [
+                "https://www.imls.gov/assets/1/AssetManager/fy2002_pls_database_documentation.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2002/2003",
+            "title": "Public Libraries Survey, Fiscal Year 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lydia Malley",
                 "hasEmail": "mailto:lydia.malley@ed.gov"
             },
+            "description": "The Trends in International Mathematics and Science Study, 2015 (TIMSS 2015) is a data collection that is part of the Trends in International Mathematics and Science Study (TIMSS) program; program data are available since 1999 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=073>. TIMSS 2015 (https://nces.ed.gov/timss/) is a cross-sectional study that provides international comparative information of the mathematics and science literacy of fourth-, eighth-, and twelfth-grade students and examines factors that may be associated with the acquisition of math and science literacy in students. The study was conducted using direct assessments of students and questionnaires for students, teachers, and school administrators. Fourth-, eighth-, and twelfth-graders in the 2014-15 school year were sampled. Key statistics produced from TIMSS 2015 provide reliable and timely data on the mathematics and science achievement of U.S. students compared to that of students in other countries. Data are expected to be released in 2018.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Trends in International Mathematics and Science Study (TIMSS) 2015 U.S. restricted-use datafile",
                     "description": "Trends in International Mathematics and Science Study, 2015 restricted-use data",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2018022",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Trends in International Mathematics and Science Study (TIMSS) 2015 U.S. restricted-use datafile"
                 }
             ],
+            "identifier": "2c75d51d-0c09-4b37-abde-ba96cdac2465",
             "keyword": [
                 "793bd80d-d5ff-44c1-84b7-0b054c9c910d",
                 "assessments",
@@ -43720,32 +43698,16 @@
                 "teachers",
                 "textbooks"
             ],
-            "bureauCode": [
-                "018:50"
-            ],
+            "modified": "2023-07-10T15:50:33.035400",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Bureau IT Leadership Directory",
-            "description": "A listing of individuals who, besides the Chief Information Officer, have bureau-specific duties or responsibilities as a chief information officer.",
-            "modified": "2023-07-10T15:48:58.660398",
-            "accessLevel": "public",
-            "identifier": "5755dbb3-00e8-4322-9c79-cfd3b60f6489",
-            "dataQuality": true,
-            "issued": "2015-08-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Advisory Committee on Student Financial Assistance (ACSFA)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Federal Student Aid (FSA)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                        "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -43759,31 +43721,44 @@
                         }
                     }
                 }
-                }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "title": "Trends in International Mathematics and Science Study, 2015"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jim Mould",
                 "hasEmail": "mailto:Jim.Mould@ed.gov"
             },
+            "dataQuality": true,
+            "description": "A listing of individuals who, besides the Chief Information Officer, have bureau-specific duties or responsibilities as a chief information officer.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "HTML",
-                    "title": "bureaudirectory",
                     "description": "A listing of individuals who, besides the Chief Information Officer, have bureau-specific duties or responsibilities as a chief information officer.",
-                    "downloadURL": "https://www.ed.gov/digitalstrategy/bureaudirectory.html"
+                    "downloadURL": "https://www.ed.gov/digitalstrategy/bureaudirectory.html",
+                    "format": "HTML",
+                    "mediaType": "text/html",
+                    "title": "bureaudirectory"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "JSON",
-                    "title": "bureaudirectory",
                     "description": "A listing of individuals who, besides the Chief Information Officer, have bureau-specific duties or responsibilities as a chief information officer.",
-                    "downloadURL": "https://www.ed.gov/digitalstrategy/bureaudirectory.json"
+                    "downloadURL": "https://www.ed.gov/digitalstrategy/bureaudirectory.json",
+                    "format": "JSON",
+                    "mediaType": "application/json",
+                    "title": "bureaudirectory"
                 }
             ],
+            "identifier": "5755dbb3-00e8-4322-9c79-cfd3b60f6489",
+            "issued": "2015-08-15",
             "keyword": [
                 "7697c1a0-c706-4cc7-9c2c-dbf6d0f02c89",
                 "bureau-specific",
@@ -43794,26 +43769,14 @@
                 "it",
                 "it-leadership"
             ],
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
-            "programCode": [
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T15:48:58.660398",
+            "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "CIO Governance Board Membership List",
-            "description": "A listing of the governing boards within the U.S. Department of Education in which the Department's Chief Information Officer is actively involved.",
-            "modified": "2023-07-10T15:47:27.658867",
-            "accessLevel": "public",
-            "identifier": "51f15eb0-58d5-4b17-b1a1-b936edb3eab3",
-            "dataQuality": true,
-            "issued": "2015-08-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Advisory Committee on Student Financial Assistance (ACSFA)",
@@ -43838,29 +43801,41 @@
                     }
                 }
             },
+            "title": "Bureau IT Leadership Directory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jim Mould",
                 "hasEmail": "mailto:Jim.Mould@ed.gov"
             },
+            "dataQuality": true,
+            "description": "A listing of the governing boards within the U.S. Department of Education in which the Department's Chief Information Officer is actively involved.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "HTML",
-                    "title": "governanceboards.html",
                     "description": "A listing of the governing boards within the U.S. Department of Education in which the Department's Chief Information Officer is actively involved.",
-                    "downloadURL": "https://www2.ed.gov/digitalstrategy/governanceboards.html"
+                    "downloadURL": "https://www2.ed.gov/digitalstrategy/governanceboards.html",
+                    "format": "HTML",
+                    "mediaType": "text/html",
+                    "title": "governanceboards.html"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "JSON",
-                    "title": "governanceboards.json",
                     "description": "A listing of the governing boards within the U.S. Department of Education in which the Department's Chief Information Officer is actively involved.",
-                    "downloadURL": "https://www.ed.gov/digitalstrategy/governanceboards.json"
+                    "downloadURL": "https://www.ed.gov/digitalstrategy/governanceboards.json",
+                    "format": "JSON",
+                    "mediaType": "application/json",
+                    "title": "governanceboards.json"
                 }
             ],
+            "identifier": "51f15eb0-58d5-4b17-b1a1-b936edb3eab3",
+            "issued": "2015-08-15",
             "keyword": [
                 "7697c1a0-c706-4cc7-9c2c-dbf6d0f02c89",
                 "active-involvement",
@@ -43870,26 +43845,14 @@
                 "governing-boards",
                 "membership"
             ],
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T15:47:27.658867",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Agency IT Policy Archive",
-            "description": "Archive of U.S. Department of Education (ED) information technology (IT) policy documents--including \"Information Technology Investment Management (ITIM) Directive\" (OCIO 3-108), \"Lifecycle Management (LCM) Directive\" (OCIO 1-106), \"Investment Review Board (IRB) Charter (Departmental)\", \"Investment Review Board (IRB) Charter (Federal Student Aid [FSA])\", and \"Agency IT Policy Archive\".",
-            "modified": "2023-07-10T15:46:18.450744",
-            "accessLevel": "public",
-            "identifier": "4c3f1513-2ee7-4f6d-95aa-7e5cd4c145f3",
-            "dataQuality": true,
-            "issued": "2015-08-31",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Advisory Committee on Student Financial Assistance (ACSFA)",
@@ -43914,21 +43877,33 @@
                     }
                 }
             },
+            "title": "CIO Governance Board Membership List"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jim Mould",
                 "hasEmail": "mailto:Jim.Mould@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Archive of U.S. Department of Education (ED) information technology (IT) policy documents--including \"Information Technology Investment Management (ITIM) Directive\" (OCIO 3-108), \"Lifecycle Management (LCM) Directive\" (OCIO 1-106), \"Investment Review Board (IRB) Charter (Departmental)\", \"Investment Review Board (IRB) Charter (Federal Student Aid [FSA])\", and \"Agency IT Policy Archive\".",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/x-zip-compressed",
-                    "format": "ZIP",
-                    "title": "policyarchive.zip",
                     "description": "Archive of U.S. Department of Education (ED) information technology (IT) policy documents--including \"Information Technology Investment Management (ITIM) Directive\" (OCIO 3-108), \"Lifecycle Management (LCM) Directive\" (OCIO 1-106), \"Investment Review Board (IRB) Charter (Departmental)\", \"Investment Review Board (IRB) Charter (Federal Student Aid [FSA])\", and \"Agency IT Policy Archive\".",
-                    "downloadURL": "https://www.ed.gov/digitalstrategy/policyarchive/policyarchive.zip"
+                    "downloadURL": "https://www.ed.gov/digitalstrategy/policyarchive/policyarchive.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "policyarchive.zip"
                 }
             ],
+            "identifier": "4c3f1513-2ee7-4f6d-95aa-7e5cd4c145f3",
+            "issued": "2015-08-31",
             "keyword": [
                 "7697c1a0-c706-4cc7-9c2c-dbf6d0f02c89",
                 "archive",
@@ -43940,88 +43915,104 @@
                 "lifecycle-management",
                 "policy"
             ],
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T15:46:18.450744",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "IDEA Performance Reporting and Determinations",
-            "description": "This page provides information regarding formula grantee's performance and determinations under the Individuals with Disabilities Education Act (IDEA).  IDEA requires each state to develop a state performance plan/annual performance report (SPP/APR) that evaluates the state\u2019s efforts to implement the requirements and purposes of the IDEA and describes how the state will improve its implementation. The Office of Special Education Programs (OSEP) uses information from the SPP/APR, information obtained through monitoring visits, and any other public information to determine if the state meet the requirements and purposes of IDEA.  This page provides a summary of these determination from 2007 to 2020.",
-            "modified": "2023-07-10T15:40:46.360107",
-            "accessLevel": "public",
-            "identifier": "c59b82ad-03e1-4f1c-b4b2-95bc68a3868b",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                "name": "Advisory Committee on Student Financial Assistance (ACSFA)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Federal Student Aid (FSA)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Under Secretary (OUS)",
+                        "subOrganizationOf": {
+                            "@type": "org:Organization",
+                            "name": "Office of the Secretary (OS)",
+                            "subOrganizationOf": {
+                                "@type": "org:Organization",
+                                "name": "U.S. Department of Education",
                                 "subOrganizationOf": {
                                     "@type": "org:Organization",
                                     "name": "U.S. Government"
                                 }
+                            }
+                        }
+                    }
+                }
+            },
+            "title": "Agency IT Policy Archive"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Special Education Programs - Monitoring and State Improvement Planning Division",
                 "hasEmail": "mailto:osers@ed.gov"
             },
+            "description": "This page provides information regarding formula grantee's performance and determinations under the Individuals with Disabilities Education Act (IDEA).  IDEA requires each state to develop a state performance plan/annual performance report (SPP/APR) that evaluates the state\u2019s efforts to implement the requirements and purposes of the IDEA and describes how the state will improve its implementation. The Office of Special Education Programs (OSEP) uses information from the SPP/APR, information obtained through monitoring visits, and any other public information to determine if the state meet the requirements and purposes of IDEA.  This page provides a summary of these determination from 2007 to 2020.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "IDEA\u00a0Part B State Determinations Under Results Driven Accountability, 2015:",
                     "description": "IDEA Performance Reporting and Determinations - Results Driven Accountability Graphics and Data Files",
-                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/3c52fc88-cbdc-454d-ba1f-c50b6f8a8821/download/2015partbrdadeterminationsrevised.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/3c52fc88-cbdc-454d-ba1f-c50b6f8a8821/download/2015partbrdadeterminationsrevised.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "IDEA\u00a0Part B State Determinations Under Results Driven Accountability, 2015:"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "IDEA\u00a0Part B State Compliance Only, 2015:",
                     "description": "IDEA Performance Reporting and Determinations - Results Driven Accountability Graphics and Data Files",
-                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/24b2e2b4-0148-4437-bea6-0f0e9668686f/download/2015partbcomplianceonly.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/24b2e2b4-0148-4437-bea6-0f0e9668686f/download/2015partbcomplianceonly.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "IDEA\u00a0Part B State Compliance Only, 2015:"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "IDEA\u00a0Part B State Determinations, 2007\u201315:",
                     "description": "IDEA Performance Reporting and Determinations - Results Driven Accountability Graphics and Data Files",
-                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/ec1a5b40-66dd-40f8-8b12-77b5543c170a/download/20072015partbdeterminations.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/ec1a5b40-66dd-40f8-8b12-77b5543c170a/download/20072015partbdeterminations.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "IDEA\u00a0Part B State Determinations, 2007\u201315:"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "IDEA\u00a0Part C State Determinations Under Results Driven Accountability, 2015:",
                     "description": "IDEA Performance Reporting and Determinations - Results Driven Accountability Graphics and Data Files",
-                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/2e4775a3-4a50-4008-8f34-c7f9e48a997c/download/2015partcrdadeterminations.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/2e4775a3-4a50-4008-8f34-c7f9e48a997c/download/2015partcrdadeterminations.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "IDEA\u00a0Part C State Determinations Under Results Driven Accountability, 2015:"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "IDEA\u00a0Part C State Compliance Only, 2015:",
                     "description": "IDEA Performance Reporting and Determinations - Results Driven Accountability Graphics and Data Files",
-                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/80660397-3b27-44a1-9a9c-f1d27182205f/download/2015partccomplianceonly.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/80660397-3b27-44a1-9a9c-f1d27182205f/download/2015partccomplianceonly.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "IDEA\u00a0Part C State Compliance Only, 2015:"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "IDEA\u00a0Part C State Determinations, 2007\u201315:",
                     "description": "IDEA Performance Reporting and Determinations - Results Driven Accountability Graphics and Data Files",
-                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/7831a8cf-67f6-463a-8ea0-15c3d2b15df4/download/20072015partcdeterminations.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/31a964f6-25c1-49f0-bfeb-ddc9b4227fc6/resource/7831a8cf-67f6-463a-8ea0-15c3d2b15df4/download/20072015partcdeterminations.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "IDEA\u00a0Part C State Determinations, 2007\u201315:"
                 }
             ],
+            "identifier": "c59b82ad-03e1-4f1c-b4b2-95bc68a3868b",
             "keyword": [
                 "9343cd39-02f5-4811-83c0-b0fb8503e767",
                 "apr",
@@ -44033,89 +44024,76 @@
                 "spp",
                 "state"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-10T15:40:46.360107",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 2001-02",
-            "description": "The 2001-02 Private School Universe Survey (PSS 2001-02) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 2001-02 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires, with an internet response option, and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 2001-02 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
-            "modified": "2023-07-10T15:36:11.590009",
-            "accessLevel": "public",
-            "identifier": "4396b7f4-2510-45ca-be38-319b4b1f3917",
-            "dataQuality": true,
-            "issued": "2006-06-28",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2001/2002",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "Office of the Secretary (OS)",
-                        "subOrganizationOf": {
-                            "@type": "org:Organization",
-                            "name": "U.S. Department of Education",
+                "name": "Office of Special Education and Rehabilitative Services (OSERS)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "U.S. Government"
                 }
-                        }
-                    }
-                }
             },
+            "title": "IDEA Performance Reporting and Determinations"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2001-02 Private School Universe Survey (PSS 2001-02) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 2001-02 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires, with an internet response option, and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 2001-02 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Elementary/Secondary Information System",
                     "description": "The Elementary/Secondary Information System (ELSi) is an NCES web application that allows users to quickly view public and private school data and create custom tables and charts using data from the Common Core of Data (CCD) and Private School Survey (PSS)",
                     "downloadURL": "https://nces.ed.gov/ccd/elsi/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Elementary/Secondary Information System"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS0102.zip",
-                    "description": "2001-02 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0102.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS0102.zip"
+                    "description": "2001-02 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS0102.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS0102.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS0102_SAS7BDAT.zip",
-                    "description": "2001-02 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0102.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS0102_SAS7BDAT.zip"
+                    "description": "2001-02 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS0102_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS0102_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS0102.zip",
-                    "description": "2001-02 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0102.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS0102.zip"
+                    "description": "2001-02 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS0102.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS0102.zip"
                 }
             ],
+            "identifier": "4396b7f4-2510-45ca-be38-319b4b1f3917",
+            "issued": "2006-06-28",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -44124,33 +44102,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2005/2005305.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_0102.zip",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_0102.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 2003-04",
-            "description": "The Private School Universe Survey, 2003-04 (PSS 2003-04), is a study that is part of the Private School Universe program. PSS 2003-04 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS universe consists of a diverse population of schools. It includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. The study's unweighted and weighted response rates were both 94 percent. Key statistics produced from PSS 2003-04 are on the growth of religiously affiliated schools, the number of private high school graduates, the length of the school year for various private schools, and the number of private school students and teachers.",
-            "modified": "2023-07-10T15:35:18.492950",
-            "accessLevel": "public",
-            "identifier": "f7575a26-a0ec-490d-805e-a485d5a0161a",
-            "dataQuality": true,
-            "issued": "2006-03-16",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2003/2004",
+            "modified": "2023-07-10T15:36:11.590009",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -44171,51 +44130,70 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2005/2005305.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_0102.zip",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_0102.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2001/2002",
+            "title": "Private School Universe Survey, 2001-02"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Private School Universe Survey, 2003-04 (PSS 2003-04), is a study that is part of the Private School Universe program. PSS 2003-04 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS universe consists of a diverse population of schools. It includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. The study's unweighted and weighted response rates were both 94 percent. Key statistics produced from PSS 2003-04 are on the growth of religiously affiliated schools, the number of private high school graduates, the length of the school year for various private schools, and the number of private school students and teachers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Elementary/Secondary Information System",
                     "description": "The Elementary/Secondary Information System (ELSi) is an NCES web application that allows users to quickly view public and private school data and create custom tables and charts using data from the Common Core of Data (CCD) and Private School Survey (PSS)",
                     "downloadURL": "https://nces.ed.gov/ccd/elsi/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Elementary/Secondary Information System"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS0304.zip",
-                    "description": "2003-04 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0304.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS0304.zip"
+                    "description": "2003-04 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS0304.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS0304.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS0304_SAS7BDAT.zip",
-                    "description": "2003-04 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0304.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS0304_SAS7BDAT.zip"
+                    "description": "2003-04 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS0304_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS0304_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS0304.zip",
-                    "description": "2003-04 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0304.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS0304.zip"
+                    "description": "2003-04 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS0304.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS0304.zip"
                 }
             ],
+            "identifier": "f7575a26-a0ec-490d-805e-a485d5a0161a",
+            "issued": "2006-03-16",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -44224,33 +44202,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2008/2008314.pdf",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_0304.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_0304.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 2005-06",
-            "description": "The Private School Universe Survey, 2005-06 (PSS 2005-06), is a study that is part of the Private School Universe program. PSS 2005-06 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS universe consists of a diverse population of schools. It includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. The study's unweighted and weighted response rates were both 94 percent. Key statistics produced from PSS 2005-06 are on the growth of religiously affiliated schools, the number of private high school graduates, the length of the school year for various private schools, and the number of private school students and teachers.",
-            "modified": "2023-07-10T15:34:45.382680",
-            "accessLevel": "public",
-            "identifier": "7188018a-7d78-4d5c-bf15-1875f98ab923",
-            "dataQuality": true,
-            "issued": "2008-04-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2005/2006",
+            "modified": "2023-07-10T15:35:18.492950",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -44271,51 +44230,70 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2008/2008314.pdf",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_0304.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_0304.zip"
+            ],
+            "spatial": "United States",
+            "temporal": "2003/2004",
+            "title": "Private School Universe Survey, 2003-04"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Private School Universe Survey, 2005-06 (PSS 2005-06), is a study that is part of the Private School Universe program. PSS 2005-06 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS universe consists of a diverse population of schools. It includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. The study's unweighted and weighted response rates were both 94 percent. Key statistics produced from PSS 2005-06 are on the growth of religiously affiliated schools, the number of private high school graduates, the length of the school year for various private schools, and the number of private school students and teachers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Elementary/Secondary Information System",
                     "description": "The Elementary/Secondary Information System (ELSi) is an NCES web application that allows users to quickly view public and private school data and create custom tables and charts using data from the Common Core of Data (CCD) and Private School Survey (PSS)",
                     "downloadURL": "https://nces.ed.gov/ccd/elsi/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Elementary/Secondary Information System"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS0506.zip",
-                    "description": "2005-06 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0506.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS0506.zip"
+                    "description": "2005-06 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS0506.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS0506.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS0506_SAS7BDAT.zip",
-                    "description": "2005-06 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0506.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS0506_SAS7BDAT.zip"
+                    "description": "2005-06 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS0506_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS0506_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS0506.zip",
-                    "description": "2005-06 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0506.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS0506.zip"
+                    "description": "2005-06 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS0506.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS0506.zip"
                 }
             ],
+            "identifier": "7188018a-7d78-4d5c-bf15-1875f98ab923",
+            "issued": "2008-04-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -44324,33 +44302,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2009/2009310.pdf",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_0506.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_0506.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 2007-08",
-            "description": "The Private School Universe Survey, 2007-08 (PSS 2007-08), is a study that is part of the Private School Universe Survey program. PSS 2007-08 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that builds an accurate and complete universe of private schools to serve as a sampling frame for NCES surveys of private schools and generates biennial data on the total number of private schools, teachers, and students. The study was conducted using surveys of administrative personnel. The study's response rate was 91.8 percent. Key statistics produced from PSS 2007-08 are religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program.",
-            "modified": "2023-07-10T15:34:08.513062",
-            "accessLevel": "public",
-            "identifier": "22c648bb-2f0f-4c08-bce3-d908b5fae108",
-            "dataQuality": true,
-            "issued": "2009-03-19",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2007/2008",
+            "modified": "2023-07-10T15:34:45.382680",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -44371,51 +44330,70 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2009/2009310.pdf",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_0506.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_0506.zip"
+            ],
+            "spatial": "United States",
+            "temporal": "2005/2006",
+            "title": "Private School Universe Survey, 2005-06"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Private School Universe Survey, 2007-08 (PSS 2007-08), is a study that is part of the Private School Universe Survey program. PSS 2007-08 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that builds an accurate and complete universe of private schools to serve as a sampling frame for NCES surveys of private schools and generates biennial data on the total number of private schools, teachers, and students. The study was conducted using surveys of administrative personnel. The study's response rate was 91.8 percent. Key statistics produced from PSS 2007-08 are religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Elementary/Secondary Information System",
                     "description": "The Elementary/Secondary Information System (ELSi) is an NCES web application that allows users to quickly view public and private school data and create custom tables and charts using data from the Common Core of Data (CCD) and Private School Survey (PSS)",
                     "downloadURL": "https://nces.ed.gov/ccd/elsi/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Elementary/Secondary Information System"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS0708.zip",
-                    "description": "2007-08 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0708.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS0708.zip"
+                    "description": "2007-08 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS0708.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS0708.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS0708_SAS7BDAT.zip",
-                    "description": "2007-08 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0708.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS0708_SAS7BDAT.zip"
+                    "description": "2007-08 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS0708_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS0708_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS0708.zip",
-                    "description": "2007-08 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0708.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS0708.zip"
+                    "description": "2007-08 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS0708.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS0708.zip"
                 }
             ],
+            "identifier": "22c648bb-2f0f-4c08-bce3-d908b5fae108",
+            "issued": "2009-03-19",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -44424,33 +44402,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2009/2009319.pdf",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_0708.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_0708.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 2009-10",
-            "description": "The Private School Universe Survey, 2009-10 (PSS 2009-10), is a study that is part of the Private School Universe Survey program. PSS 2009-10 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that builds an accurate and complete universe of private schools to serve as a sampling frame for NCES surveys of private schools and generates biennial data on the total number of private schools, teachers, and students. The study was conducted using surveys of administrative personnel. A universe of private schools extant in October 2009 was built. The study's response rate was 93.6 percent. Key statistics produced from PSS 2009-10 are religious orientation, level of school, length of school year, length of year and school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program.",
-            "modified": "2023-07-10T15:33:27.600017",
-            "accessLevel": "public",
-            "identifier": "1a620de3-6b04-47b5-8548-75bbbfe6feea",
-            "dataQuality": true,
-            "issued": "2011-05-06",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2009/2010",
+            "modified": "2023-07-10T15:34:08.513062",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -44471,51 +44430,70 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2009/2009319.pdf",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_0708.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_0708.zip"
+            ],
+            "spatial": "United States",
+            "temporal": "2007/2008",
+            "title": "Private School Universe Survey, 2007-08"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Private School Universe Survey, 2009-10 (PSS 2009-10), is a study that is part of the Private School Universe Survey program. PSS 2009-10 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that builds an accurate and complete universe of private schools to serve as a sampling frame for NCES surveys of private schools and generates biennial data on the total number of private schools, teachers, and students. The study was conducted using surveys of administrative personnel. A universe of private schools extant in October 2009 was built. The study's response rate was 93.6 percent. Key statistics produced from PSS 2009-10 are religious orientation, level of school, length of school year, length of year and school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Elementary/Secondary Information System",
                     "description": "The Elementary/Secondary Information System (ELSi) is an NCES web application that allows users to quickly view public and private school data and create custom tables and charts using data from the Common Core of Data (CCD) and Private School Survey (PSS)",
                     "downloadURL": "https://nces.ed.gov/ccd/elsi/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Elementary/Secondary Information System"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS0910.zip",
-                    "description": "2009-10 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0910.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS0910.zip"
+                    "description": "2009-10 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS0910.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS0910.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS0910_SAS7BDAT.zip",
-                    "description": "2009-10 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0910.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS0910_SAS7BDAT.zip"
+                    "description": "2009-10 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS0910_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS0910_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS0910.zip",
-                    "description": "2009-10 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_0910.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS0910.zip"
+                    "description": "2009-10 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS0910.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS0910.zip"
                 }
             ],
+            "identifier": "1a620de3-6b04-47b5-8548-75bbbfe6feea",
+            "issued": "2011-05-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -44524,33 +44502,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2011/2011322.pdf",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_0910.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_0910.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 2011-12",
-            "description": "The Private School Universe Survey, 2011-12 (PSS 2011-12), is a study that is part of the Private School Universe program. PSS 2011-12 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires, an internet response option and telephone and personal follow-up of all private schools in the United States. The PSS universe consists of a diverse population of schools. It includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. The study's response rate is 91.8 percent. Key statistics produced from PSS 2011-12 are on the number of private schools, students, and teachers, the number of high school graduates, the length of the school year and school day.",
-            "modified": "2023-07-10T15:32:35.252975",
-            "accessLevel": "public",
-            "identifier": "f6b6136e-5f04-41ac-bc1f-027944fb320a",
-            "dataQuality": true,
-            "issued": "2013-04-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
+            "modified": "2023-07-10T15:33:27.600017",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -44571,51 +44530,70 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2011/2011322.pdf",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_0910.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_0910.zip"
+            ],
+            "spatial": "United States",
+            "temporal": "2009/2010",
+            "title": "Private School Universe Survey, 2009-10"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Private School Universe Survey, 2011-12 (PSS 2011-12), is a study that is part of the Private School Universe program. PSS 2011-12 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires, an internet response option and telephone and personal follow-up of all private schools in the United States. The PSS universe consists of a diverse population of schools. It includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. The study's response rate is 91.8 percent. Key statistics produced from PSS 2011-12 are on the number of private schools, students, and teachers, the number of high school graduates, the length of the school year and school day.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Elementary/Secondary Information System",
                     "description": "The Elementary/Secondary Information System (ELSi) is an NCES web application that allows users to quickly view public and private school data and create custom tables and charts using data from the Common Core of Data (CCD) and Private School Survey (PSS)",
                     "downloadURL": "https://nces.ed.gov/ccd/elsi/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Elementary/Secondary Information System"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "pss1112_pu_txt.zip",
-                    "description": "2011-12 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/codebook20112012.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1112_pu_txt.zip"
+                    "description": "2011-12 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1112_pu_txt.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "pss1112_pu_txt.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "pss1112_pu_sas7bdat.zip",
-                    "description": "2011-12 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/codebook20112012.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1112_pu_sas7bdat.zip"
+                    "description": "2011-12 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1112_pu_sas7bdat.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "pss1112_pu_sas7bdat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "pss1112_pu_sav.zip",
-                    "description": "2011-12 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/codebook20112012.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1112_pu_sav.zip"
+                    "description": "2011-12 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1112_pu_sav.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "pss1112_pu_sav.zip"
                 }
             ],
+            "identifier": "f6b6136e-5f04-41ac-bc1f-027944fb320a",
+            "issued": "2013-04-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -44624,34 +44602,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2014/2014351.pdf",
-                "https://nces.ed.gov/surveys/pss/pdf/Questoinnaire_20112012.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_PSS1112_PU.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 2013-14",
-            "description": "The Private School Universe Survey, 2013-14 (PSS 2013-14), is a study that is part of the Private School Universe program. PSS 2013-14 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study is conducted using mail questionnaires, an internet response option and telephone and personal follow-up of all private schools in the United States. The PSS universe consists of a diverse population of schools. It includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Keys statistics produced from PSS 2013-14 are on the number of private schools, students, and teachers, the number of high school graduates, the length of the school year and school day.",
-            "modified": "2023-07-10T15:31:21.916876",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "358fff77-78ff-4cbc-9cb5-6f6c5fa401ef",
-            "dataQuality": true,
-            "issued": "2015-04-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/2014",
+            "modified": "2023-07-10T15:32:35.252975",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -44672,51 +44630,70 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2014/2014351.pdf",
+                "https://nces.ed.gov/surveys/pss/pdf/Questoinnaire_20112012.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_PSS1112_PU.zip"
+            ],
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "Private School Universe Survey, 2011-12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Private School Universe Survey, 2013-14 (PSS 2013-14), is a study that is part of the Private School Universe program. PSS 2013-14 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study is conducted using mail questionnaires, an internet response option and telephone and personal follow-up of all private schools in the United States. The PSS universe consists of a diverse population of schools. It includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Keys statistics produced from PSS 2013-14 are on the number of private schools, students, and teachers, the number of high school graduates, the length of the school year and school day.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Private School Universe Survey (PSS): Restricted-Use Data for School Year 2013-14",
                     "description": "Restricted-use data for the 2013-14 Private School Universe Survey in three formats: SAS, SPSS, and text. Includes file documentation and a copy of the questionnaire.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2017068",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Private School Universe Survey (PSS): Restricted-Use Data for School Year 2013-14"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "pss1314_pu_csv.zip",
-                    "description": "2013-14 Private School Universe Survey data as a zipped CSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/codebook2013_14.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1314_pu_csv.zip"
+                    "description": "2013-14 Private School Universe Survey data as a zipped CSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1314_pu_csv.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "pss1314_pu_csv.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "pss1314_pu_sas7bdat.zip",
-                    "description": "2013-14 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/codebook2013_14.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1314_pu_sas7bdat.zip"
+                    "description": "2013-14 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1314_pu_sas7bdat.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "pss1314_pu_sas7bdat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "pss1314_pu_sav.zip",
-                    "description": "2013-14 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/codebook2013_14.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1314_pu_sav.zip"
+                    "description": "2013-14 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/pss1314_pu_sav.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "pss1314_pu_sav.zip"
                 }
             ],
+            "identifier": "358fff77-78ff-4cbc-9cb5-6f6c5fa401ef",
+            "issued": "2015-04-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -44725,34 +44702,17 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2017065"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Elementary School Math Professional Development Impact Evaluation",
-            "description": "The Elementary School Math Professional Development Impact Evaluation (Elementary School Math PD Evaluation) is a data collection that is part of the Professional Development Impact Program (PD Impact). Elementary School Math PD Evaluation <https://ies.ed.gov/ncee/projects/evaluation/tq_mathpd.asp> examines the implementation and impact of the Math Professional Development (PD) program, by means of collecting fourth-grade teachers' content knowledge, classroom practices, and their student's achievement for one academic year. Two-hundred such volunteer teachers from six local education agencies (LEAs) were recruited to be randomly assigned to either an experimental or control group. Teachers in the experimental group were given the PD intervention, whereas teachers in the control group engaged in their LEAs' and schools' standard PD regimen over the 2013-14 academic year. At the end of the experimental period, a survey was then administered to obtain teacher background information for covariate use in the impact analyses. Key statistics produced from Elementary School Math PD Evaluation include, inter alia, the implementation of the PD program and its impact on the participating teachers' students' achievement in the classroom.",
-            "modified": "2023-07-10T14:48:27.068102",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "d08efd55-a032-46e5-8827-2a68d8972e09",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/2014",
+            "modified": "2023-07-10T15:31:21.916876",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Evaluation and Regional Assistance (NCEERA)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Institute of Education Sciences (IES)",
@@ -44770,20 +44730,37 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2017065"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2013/2014",
+            "title": "Private School Universe Survey, 2013-14"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Wei",
                 "hasEmail": "mailto:thomas.wei@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Elementary School Math Professional Development Impact Evaluation (Elementary School Math PD Evaluation) is a data collection that is part of the Professional Development Impact Program (PD Impact). Elementary School Math PD Evaluation <https://ies.ed.gov/ncee/projects/evaluation/tq_mathpd.asp> examines the implementation and impact of the Math Professional Development (PD) program, by means of collecting fourth-grade teachers' content knowledge, classroom practices, and their student's achievement for one academic year. Two-hundred such volunteer teachers from six local education agencies (LEAs) were recruited to be randomly assigned to either an experimental or control group. Teachers in the experimental group were given the PD intervention, whereas teachers in the control group engaged in their LEAs' and schools' standard PD regimen over the 2013-14 academic year. At the end of the experimental period, a survey was then administered to obtain teacher background information for covariate use in the impact analyses. Key statistics produced from Elementary School Math PD Evaluation include, inter alia, the implementation of the PD program and its impact on the participating teachers' students' achievement in the classroom.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Elementary School Math Professional Development Impact Evaluation Restricted-Use Data Files",
                     "description": "Restricted-use data file for Elementary School Math Professional Development Impact Evaluation",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Elementary School Math Professional Development Impact Evaluation Restricted-Use Data Files"
                 }
             ],
+            "identifier": "d08efd55-a032-46e5-8827-2a68d8972e09",
             "keyword": [
                 "34621008-400b-4c5c-b37f-2af6fec112e8",
                 "air",
@@ -44807,32 +44784,17 @@
                 "teacher-content-knowledge-and-background-characteristics",
                 "teacher-involvement"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T14:48:27.068102",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Program for International Student Assessment, 2003",
-            "description": "The 2003 Program for International Student Assessment (PISA:03) is a study that is part of the Program for International Student Assessment (PISA) program; program data is available since 2000 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=098>. PISA:03 (https://nces.ed.gov/surveys/pisa/) is a cross-sectional study that measures the yield of education systems, or what skills and competencies students have acquired and can apply in reading, mathematics, and science to real-world contexts by age 15. For PISA:03, mathematics literacy was the subject area assessed in-depth. The study was conducted using questionnaires and direct assessments of 15-year-old students. 15-year-old students in April to May of 2003 were sampled. The study's response rate was 83 percent. Key statistics produced from PISA:03 are 15-year-olds' capabilities in reading, mathematics, and science literacy.",
-            "modified": "2023-07-10T14:47:42.902932",
-            "accessLevel": "public",
-            "identifier": "4f65f2e1-0ebd-4199-8e07-9f7bfc61ac7a",
-            "dataQuality": true,
-            "issued": "2008-04-23",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf ",
-            "temporal": "2002/2003",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
+                "name": "National Center for Education Evaluation and Regional Assistance (NCEERA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Institute of Education Sciences (IES)",
@@ -44850,21 +44812,36 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2013/2014",
+            "title": "Elementary School Math Professional Development Impact Evaluation"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Patrick Gonzales",
                 "hasEmail": "mailto:patrick.gonzales@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2003 Program for International Student Assessment (PISA:03) is a study that is part of the Program for International Student Assessment (PISA) program; program data is available since 2000 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=098>. PISA:03 (https://nces.ed.gov/surveys/pisa/) is a cross-sectional study that measures the yield of education systems, or what skills and competencies students have acquired and can apply in reading, mathematics, and science to real-world contexts by age 15. For PISA:03, mathematics literacy was the subject area assessed in-depth. The study was conducted using questionnaires and direct assessments of 15-year-old students. 15-year-old students in April to May of 2003 were sampled. The study's response rate was 83 percent. Key statistics produced from PISA:03 are 15-year-olds' capabilities in reading, mathematics, and science literacy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2003: U.S. Public-Use Data Files, Electronic Codebook, and User's Guide",
                     "description": "2003 Program for International Student Assessment public-use data files, electronic codebook, and user\u00c3\u0192\u00c6\u2019\u00c3\u201a\u00c2\u00af\u00c3\u0192\u00e2\u20ac\u0161\u00c3\u201a\u00c2\u00bf\u00c3\u0192\u00e2\u20ac\u0161\u00c3\u201a\u00c2\u00bds guide",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2007048",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2003: U.S. Public-Use Data Files, Electronic Codebook, and User's Guide"
                 }
             ],
+            "identifier": "4f65f2e1-0ebd-4199-8e07-9f7bfc61ac7a",
+            "issued": "2008-04-23",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessment",
@@ -44875,30 +44852,14 @@
                 "reading-literacy",
                 "science-literacy"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T14:47:42.902932",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Program for International Student Assessment, 2006",
-            "description": "The 2006 Program for International Student Assessment (PISA:06) is a study that is part of the Program for International Student Assessment (PISA) program; program data is available since 2000 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=098>. PISA:06 (https://nces.ed.gov/surveys/pisa/) is a cross-sectional study that measures the yield of education systems, or what skills and competencies students have acquired and can apply in reading, mathematics, and science to real-world contexts by age 15. For PISA:06, science literacy was the subject area assessed in-depth. The study was conducted using questionnaires and direct assessments of 15-year-old students. 15-year-old students in April to May of 2006 were sampled. The study's response rate was 91 percent. Key statistics produced from PISA:06 are 15-year-olds' capabilities in reading, mathematics, and science literacy.",
-            "modified": "2023-07-10T14:46:48.143705",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "72eb571b-f81f-4f8e-b631-5dbc849e12ab",
-            "dataQuality": true,
-            "issued": "2009-04-24",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf ",
-            "temporal": "2005/2006",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -44919,28 +44880,43 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf ",
+            "temporal": "2002/2003",
+            "title": "Program for International Student Assessment, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Patrick Gonzales",
                 "hasEmail": "mailto:patrick.gonzales@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2006 Program for International Student Assessment (PISA:06) is a study that is part of the Program for International Student Assessment (PISA) program; program data is available since 2000 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=098>. PISA:06 (https://nces.ed.gov/surveys/pisa/) is a cross-sectional study that measures the yield of education systems, or what skills and competencies students have acquired and can apply in reading, mathematics, and science to real-world contexts by age 15. For PISA:06, science literacy was the subject area assessed in-depth. The study was conducted using questionnaires and direct assessments of 15-year-old students. 15-year-old students in April to May of 2006 were sampled. The study's response rate was 91 percent. Key statistics produced from PISA:06 are 15-year-olds' capabilities in reading, mathematics, and science literacy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2006: U. S. Restricted-Use Data File & Electronic Codebook",
                     "description": "2006 Program for International Student Assessment restricted-use data and electronic codebook",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009011",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2006: U. S. Restricted-Use Data File & Electronic Codebook"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2006: U.S. Public-Use Data Files and Electronic Codebook",
                     "description": "2006 Program for International Student Assessment  public-use data and electronic codebook",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009057",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2006: U.S. Public-Use Data Files and Electronic Codebook"
                 }
             ],
+            "identifier": "72eb571b-f81f-4f8e-b631-5dbc849e12ab",
+            "issued": "2009-04-24",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessment",
@@ -44949,30 +44925,14 @@
                 "reading-literacy",
                 "science-literacy"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T14:46:48.143705",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Program for International Student Assessment, 2009",
-            "description": "The 2009 Program for International Student Assessment (PISA:09) is a study that is part of the Program for International Student Assessment (PISA) program; program data is available since 2000 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=098>. PISA:09 (https://nces.ed.gov/surveys/pisa/) is a cross-sectional study that measures the yield of education systems, or what skills and competencies students have acquired and can apply in reading, mathematics, and science to real-world contexts by age 15. For PISA:09, reading literacy was the subject area assessed in-depth. The study was conducted using questionnaires and direct assessments of 15-year-old students. 15-year-old students in April to May of 2009 were sampled. The study's response rate was 87 percent. Key statistics produced from PISA:09 are 15-year-olds' capabilities in reading, mathematics, and science literacy.",
-            "modified": "2023-07-10T14:45:38.696407",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "1c5b27fc-1bd0-40df-a975-e7e2e48dcde6",
-            "dataQuality": true,
-            "issued": "2011-09-08",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf ",
-            "temporal": "2008/2009",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -44993,28 +44953,44 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf ",
+            "temporal": "2005/2006",
+            "title": "Program for International Student Assessment, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Patrick Gonzales",
                 "hasEmail": "mailto:patrick.gonzales@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2009 Program for International Student Assessment (PISA:09) is a study that is part of the Program for International Student Assessment (PISA) program; program data is available since 2000 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=098>. PISA:09 (https://nces.ed.gov/surveys/pisa/) is a cross-sectional study that measures the yield of education systems, or what skills and competencies students have acquired and can apply in reading, mathematics, and science to real-world contexts by age 15. For PISA:09, reading literacy was the subject area assessed in-depth. The study was conducted using questionnaires and direct assessments of 15-year-old students. 15-year-old students in April to May of 2009 were sampled. The study's response rate was 87 percent. Key statistics produced from PISA:09 are 15-year-olds' capabilities in reading, mathematics, and science literacy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2009: U. S. Restricted-Use Data File & Electronic Codebook",
                     "description": "2009 Program for International Student Assessment restricted-use data and electronic codebook",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011081",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2009: U. S. Restricted-Use Data File & Electronic Codebook"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2009: U.S. Public-Use Data Files and Electronic Codebook",
                     "description": "2009 Program for International Student Assessment  public-use data and electronic codebook",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011038",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2009: U.S. Public-Use Data Files and Electronic Codebook"
                 }
             ],
+            "identifier": "1c5b27fc-1bd0-40df-a975-e7e2e48dcde6",
+            "issued": "2011-09-08",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessment",
@@ -45023,30 +44999,14 @@
                 "reading-literacy",
                 "science-literacy"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T14:45:38.696407",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Program for International Student Assessment, 2012",
-            "description": "The 2012 Program for International Student Assessment (PISA:12) is a study that is part of the Program for International Student Assessment (PISA) program; program data is available since 2000 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=098>. PISA:12 (https://nces.ed.gov/surveys/pisa/) is a cross-sectional study that measures the yield of education systems, or what skills and competencies students have acquired and can apply in reading, mathematics, and science to real-world contexts by age 15. For PISA:12, mathematics literacy was the subject area assessed in-depth. The study was conducted using questionnaires and direct assessments of 15-year-old students. 15-year-old students in April to May of 2012 were sampled. Key statistics produced from PISA:12 are 15-year-olds' capabilities in reading, mathematics, and science literacy, problem solving, and financial literacy.",
-            "modified": "2023-07-10T14:44:43.032608",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "edf44493-19bd-4e09-a716-20e05237a60c",
-            "dataQuality": true,
-            "issued": "2014-02-08",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2011/2012",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -45067,51 +45027,67 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf ",
+            "temporal": "2008/2009",
+            "title": "Program for International Student Assessment, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Patrick Gonzales",
                 "hasEmail": "mailto:patrick.gonzales@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2012 Program for International Student Assessment (PISA:12) is a study that is part of the Program for International Student Assessment (PISA) program; program data is available since 2000 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=098>. PISA:12 (https://nces.ed.gov/surveys/pisa/) is a cross-sectional study that measures the yield of education systems, or what skills and competencies students have acquired and can apply in reading, mathematics, and science to real-world contexts by age 15. For PISA:12, mathematics literacy was the subject area assessed in-depth. The study was conducted using questionnaires and direct assessments of 15-year-old students. 15-year-old students in April to May of 2012 were sampled. Key statistics produced from PISA:12 are 15-year-olds' capabilities in reading, mathematics, and science literacy, problem solving, and financial literacy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "Program for International Student Assessment (PISA) 2012 U.S. Public-use Data Files",
                     "description": "2012 Program for International Student Assessment public-use data available through the International Data Explorer",
-                    "downloadURL": "https://nces.ed.gov/pubs2014/data/2014028_RAW_DATA.zip"
+                    "downloadURL": "https://nces.ed.gov/pubs2014/data/2014028_RAW_DATA.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "Program for International Student Assessment (PISA) 2012 U.S. Public-use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TXT",
-                    "title": "Program for International Student Assessment (PISA) 2012 U.S. Restricted-use Data File",
                     "description": "2012 Program for International Student Assessment restricted use data available through the International Data Explorer",
-                    "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014027"
+                    "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014027",
+                    "format": "Zipped TXT",
+                    "mediaType": "application/zip",
+                    "title": "Program for International Student Assessment (PISA) 2012 U.S. Restricted-use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2012 Connecticut Restricted-use Data File",
                     "description": "Program for International Student Assessment (PISA) 2012 Connecticut Restricted-use Data File",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014056",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2012 Connecticut Restricted-use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2012 Florida Restricted-use Data File",
                     "description": "Program for International Student Assessment (PISA) 2012 Florida Restricted-use Data File",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014057",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2012 Florida Restricted-use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2012 Massachusetts  Restricted-use Data File",
                     "description": "Program for International Student Assessment (PISA) 2012 Massachusetts Restricted-use Data File",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014055",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2012 Massachusetts  Restricted-use Data File"
                 }
             ],
+            "identifier": "edf44493-19bd-4e09-a716-20e05237a60c",
+            "issued": "2014-02-08",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessment",
@@ -45123,30 +45099,14 @@
                 "reading-literacy",
                 "science-literacy"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T14:44:43.032608",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Program for International Student Assessment, 2015",
-            "description": "The 2015 Program for International Student Assessment (PISA:15) is a study that is part of the Program for International Student Assessment (PISA) program; program data is available since 2000 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=098>. PISA:15 (https://nces.ed.gov/surveys/pisa/) is a cross-sectional study that measures the yield of education systems, or what skills and competencies students have acquired and can apply in reading, mathematics, and science to real-world contexts by age 15. For PISA:15, science was the subject area assessed in-depth. The study was conducted using questionnaires and direct assessments of 15-year-old students. Key statistics produced from PISA:15 are 15-year-olds' capabilities in reading, mathematics, and science literacy.",
-            "modified": "2023-07-10T14:43:46.119105",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "5e936dc0-6e51-4289-a240-c65b35a9c125",
-            "dataQuality": true,
-            "issued": "2017-12-19",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2014/2015",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -45167,51 +45127,67 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2011/2012",
+            "title": "Program for International Student Assessment, 2012"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P3Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Patrick Gonzales",
                 "hasEmail": "mailto:patrick.gonzales@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2015 Program for International Student Assessment (PISA:15) is a study that is part of the Program for International Student Assessment (PISA) program; program data is available since 2000 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=098>. PISA:15 (https://nces.ed.gov/surveys/pisa/) is a cross-sectional study that measures the yield of education systems, or what skills and competencies students have acquired and can apply in reading, mathematics, and science to real-world contexts by age 15. For PISA:15, science was the subject area assessed in-depth. The study was conducted using questionnaires and direct assessments of 15-year-old students. Key statistics produced from PISA:15 are 15-year-olds' capabilities in reading, mathematics, and science literacy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "Program for International Student Assessment (PISA) 2015 U.S. Public-use Data Files",
                     "description": "2015 Program for International Student Assessment Public-use Data Files",
-                    "downloadURL": "https://nces.ed.gov/pubs2017/data/2017120_ASCII_Data.zip"
+                    "downloadURL": "https://nces.ed.gov/pubs2017/data/2017120_ASCII_Data.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "Program for International Student Assessment (PISA) 2015 U.S. Public-use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TXT",
-                    "title": "Program for International Student Assessment (PISA) 2015 U.S. Restricted-use Data File",
                     "description": "2015 Program for International Student Assessment Restricted-use Data File",
-                    "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2017121"
+                    "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2017121",
+                    "format": "Zipped TXT",
+                    "mediaType": "application/zip",
+                    "title": "Program for International Student Assessment (PISA) 2015 U.S. Restricted-use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2015 North Carolina Restricted-use Data File",
                     "description": "Program for International Student Assessment (PISA) 2015 North Carolina Restricted-use Data File",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2017118",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2015 North Carolina Restricted-use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2015 Puerto Rico Restricted-use Data File",
                     "description": "Program for International Student Assessment (PISA) 2015 Puerto Rico Restricted-use Data File",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2017119",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2015 Puerto Rico Restricted-use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for International Student Assessment (PISA) 2015 Massachusetts  Restricted-use Data File",
                     "description": "Program for International Student Assessment (PISA) 2015 Massachusetts Restricted-use Data File",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2017116",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for International Student Assessment (PISA) 2015 Massachusetts  Restricted-use Data File"
                 }
             ],
+            "identifier": "5e936dc0-6e51-4289-a240-c65b35a9c125",
+            "issued": "2017-12-19",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessment",
@@ -45223,30 +45199,14 @@
                 "reading-literacy",
                 "science-literacy"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T14:43:46.119105",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Program for the International Assessment of Adult Competencies, 2011-12",
-            "description": "The Program for the International Assessment of Adult Competencies, 2011-12 (PIAAC:12), is a study that is part of the Program for the International Assessment of Adult Competencies (PIAAC) program. PIAAC:12 (https://nces.ed.gov/surveys/piaac/) is a cross-sectional survey that is designed to assess and compare the basic skills and the broad range of competencies of adults around the world. The assessment focuses on cognitive and workplace skills needed for successful participation in 21st-century society and the global economy. The study was conducted using paper-and-pencil and computer-administered direct assessments of adults' literacy, numeracy, component skills, problem solving in technology-rich environments and in-person interviews of background questionnaire. PIAAC achieved a 70 percent response rate. Key statistics produced from PIAAC:12 are information on relationships between individuals' educational background, workplace experiences and skills, occupational attainment, use of information and communications technology, and cognitive skills in the areas of literacy, numeracy, and problem solving.",
-            "modified": "2023-07-10T14:41:57.985154",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "f65ea203-4c5b-4f44-b37f-381a1fdd62a2",
-            "dataQuality": true,
-            "issued": "2013-10-18",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2011/2012",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -45267,58 +45227,74 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2014/2015",
+            "title": "Program for International Student Assessment, 2015"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P10Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Holly Xie",
                 "hasEmail": "mailto:holly.xie@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Program for the International Assessment of Adult Competencies, 2011-12 (PIAAC:12), is a study that is part of the Program for the International Assessment of Adult Competencies (PIAAC) program. PIAAC:12 (https://nces.ed.gov/surveys/piaac/) is a cross-sectional survey that is designed to assess and compare the basic skills and the broad range of competencies of adults around the world. The assessment focuses on cognitive and workplace skills needed for successful participation in 21st-century society and the global economy. The study was conducted using paper-and-pencil and computer-administered direct assessments of adults' literacy, numeracy, component skills, problem solving in technology-rich environments and in-person interviews of background questionnaire. PIAAC achieved a 70 percent response rate. Key statistics produced from PIAAC:12 are information on relationships between individuals' educational background, workplace experiences and skills, occupational attainment, use of information and communications technology, and cognitive skills in the areas of literacy, numeracy, and problem solving.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "U.S. PIAAC International Data Explorer (IDE)",
                     "description": "U.S. PIAAC IDE provides results from the 2012 PIAAC for the United States, including U.S.-specific variables, and other countries; the 2003 Adult Literacy and Lifeskills Survey (ALL), and the 1994 International Adult Literacy Survey (IALS)",
                     "downloadURL": "https://nces.ed.gov/surveys/piaac/ideuspiaac/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "U.S. PIAAC International Data Explorer (IDE)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for the International Assessment of Adult Competencies (PIAAC) U.S. Restricted Use File (RUF)",
                     "description": "Restricted-use data file for the 2011-12 Program for the International Assessment of Adult Competencies",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014046",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for the International Assessment of Adult Competencies (PIAAC) U.S. Restricted Use File (RUF)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "2014045_data.zip",
-                    "description": "2011-12 Program for the International Assessment of Adult Competencies data as a zipped ASCII data file",
                     "describedBy": "https://nces.ed.gov/pubs2014/2014045_codebook.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/pubs2014/data/2014045_data.zip"
+                    "description": "2011-12 Program for the International Assessment of Adult Competencies data as a zipped ASCII data file",
+                    "downloadURL": "https://nces.ed.gov/pubs2014/data/2014045_data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "2014045_data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "2014045_sas.zip",
-                    "description": "2011-12 Program for the International Assessment of Adult Competencies data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/pubs2014/2014045_codebook.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/pubs2014/data/2014045_sas.zip"
+                    "description": "2011-12 Program for the International Assessment of Adult Competencies data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/pubs2014/data/2014045_sas.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "2014045_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "2014045_spss.zip",
-                    "description": "2011-12 Program for the International Assessment of Adult Competencies data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/pubs2014/2014045_codebook.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/pubs2014/data/2014045_spss.zip"
+                    "description": "2011-12 Program for the International Assessment of Adult Competencies data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/pubs2014/data/2014045_spss.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "2014045_spss.zip"
                 }
             ],
+            "identifier": "f65ea203-4c5b-4f44-b37f-381a1fdd62a2",
+            "issued": "2013-10-18",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "adult-literacy",
@@ -45330,37 +45306,14 @@
                 "program-for-the-international-assessment-of-adult-competencies",
                 "reading-assessment"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/piaac/questionnaire.asp",
-                "https://nces.ed.gov/surveys/piaac/cba.asp",
-                "https://nces.ed.gov/surveys/piaac/pba.asp",
-                "https://nces.ed.gov/pubs2014/data/2014045_readme.zip",
-                "https://nces.ed.gov/pubs2014/data/2014045_background.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Program for the International Assessment of Adult Competencies (PIAAC) Household Supplement, 2013-14",
-            "description": "The U.S. Program for the International Assessment of Adult Competencies, National Supplement 2014 (PIAAC Household:14) is a study that is part of the Program for the International Assessment of Adult Competencies (PIAAC) program; program data is available since 2012 at <http://nces.ed.gov/pubsearch/getpubcats.asp?sid=113>. PIAAC Household:14 (http://nces.ed.gov/surveys/piaac/national_supp.asp) is an administration of PIAAC to a sample of 3,600 U.S. adults in households that supplements the U.S. PIAAC Main Study data collection using the same procedures, instruments, and assessments. The National Supplement increases the sample size of key U.S. subgroups of interest by focusing on unemployed adults (ages 16-65), young adults (ages 16-34), and older adults (ages 66-74).",
-            "modified": "2023-07-10T14:40:59.079064",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "09020cb7-4df1-4958-8558-fd1e9cb181ef",
-            "dataQuality": true,
-            "issued": "2016-09-15",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2013/2014",
+            "modified": "2023-07-10T14:41:57.985154",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -45381,35 +45334,58 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/piaac/questionnaire.asp",
+                "https://nces.ed.gov/surveys/piaac/cba.asp",
+                "https://nces.ed.gov/surveys/piaac/pba.asp",
+                "https://nces.ed.gov/pubs2014/data/2014045_readme.zip",
+                "https://nces.ed.gov/pubs2014/data/2014045_background.zip"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2011/2012",
+            "title": "Program for the International Assessment of Adult Competencies, 2011-12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P10Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Holly Xie",
                 "hasEmail": "mailto:holly.xie@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The U.S. Program for the International Assessment of Adult Competencies, National Supplement 2014 (PIAAC Household:14) is a study that is part of the Program for the International Assessment of Adult Competencies (PIAAC) program; program data is available since 2012 at <http://nces.ed.gov/pubsearch/getpubcats.asp?sid=113>. PIAAC Household:14 (http://nces.ed.gov/surveys/piaac/national_supp.asp) is an administration of PIAAC to a sample of 3,600 U.S. adults in households that supplements the U.S. PIAAC Main Study data collection using the same procedures, instruments, and assessments. The National Supplement increases the sample size of key U.S. subgroups of interest by focusing on unemployed adults (ages 16-65), young adults (ages 16-34), and older adults (ages 66-74).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "U.S. PIAAC International Data Explorer (IDE)",
                     "description": "U.S. PIAAC IDE provides results from the 2012 PIAAC for the United States, including U.S.-specific variables, and other countries; the 2003 Adult Literacy and Lifeskills Survey (ALL), and the 1994 International Adult Literacy Survey (IALS)",
                     "downloadURL": "https://nces.ed.gov/surveys/piaac/ideuspiaac/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "U.S. PIAAC International Data Explorer (IDE)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for the International Assessment of Adult Competencies (PIAAC) 2012/2014: U.S. National Supplement Public Use Data Files-Household",
                     "description": "Public use data files for the Program for the International Assessment of Adult Competencies (PIAAC) 2012/2014: U.S. National Supplement-Household",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2016667",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for the International Assessment of Adult Competencies (PIAAC) 2012/2014: U.S. National Supplement Public Use Data Files-Household"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for the International Assessment of Adult Competencies (PIAAC) 2012/2014: U.S. National Supplement Restricted Use Data Files-Household",
                     "description": "Restricted use data files for the Program for the International Assessment of Adult Competencies (PIAAC) 2012/2014: U.S. National Supplement-Household",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2016668",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for the International Assessment of Adult Competencies (PIAAC) 2012/2014: U.S. National Supplement Restricted Use Data Files-Household"
                 }
             ],
+            "identifier": "09020cb7-4df1-4958-8558-fd1e9cb181ef",
+            "issued": "2016-09-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "adult-literacy",
@@ -45437,36 +45413,14 @@
                 "work-history",
                 "work-responsibilities"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/piaac/questionnaire.asp",
-                "https://nces.ed.gov/surveys/piaac/household.asp",
-                "https://nces.ed.gov/surveys/piaac/cba.asp",
-                "https://nces.ed.gov/surveys/piaac/pba.asp"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "U.S. Program for the International Assessment of Adult Competencies (PIAAC) National Supplement Prison Study, 2013-14",
-            "description": "The U.S. Program for the International Assessment of Adult Competencies, National Supplement Prison Study (PIAAC Prison:14) is a study that is part of the Program for the International Assessment of Adult Competencies (PIAAC) program; program data is available since 2012 at <http://nces.ed.gov/pubsearch/getpubcats.asp?sid=113>. PIAAC Prison:14 (http://nces.ed.gov/surveys/piaac/national_supp.asp) is part of the National Supplement and draws from a sample of 1,200 inmates aged 18 to 74 years-old currently detained in State, Federal, or private prisons in the United States. The direct assessments of literacy, numeracy, and problem-solving in technology-rich environments are the same for the adults in prison. The background questionnaire was tailored specifically to address the experiences and needs of this subgroup. For example, the background questionnaire asks about activities in prison, such as participation in academic programs and ESL classes, experiences with prison jobs, and involvement in non-academic programs such as employment readiness classes.",
-            "modified": "2023-07-10T14:40:03.025988",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "9d1d9372-1f82-46bb-ab75-0c6098e27c35",
-            "dataQuality": true,
-            "issued": "2016-09-15",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2013/2014",
+            "modified": "2023-07-10T14:40:59.079064",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -45487,35 +45441,57 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/piaac/questionnaire.asp",
+                "https://nces.ed.gov/surveys/piaac/household.asp",
+                "https://nces.ed.gov/surveys/piaac/cba.asp",
+                "https://nces.ed.gov/surveys/piaac/pba.asp"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2013/2014",
+            "title": "Program for the International Assessment of Adult Competencies (PIAAC) Household Supplement, 2013-14"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P10Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Holly Xie",
                 "hasEmail": "mailto:holly.xie@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The U.S. Program for the International Assessment of Adult Competencies, National Supplement Prison Study (PIAAC Prison:14) is a study that is part of the Program for the International Assessment of Adult Competencies (PIAAC) program; program data is available since 2012 at <http://nces.ed.gov/pubsearch/getpubcats.asp?sid=113>. PIAAC Prison:14 (http://nces.ed.gov/surveys/piaac/national_supp.asp) is part of the National Supplement and draws from a sample of 1,200 inmates aged 18 to 74 years-old currently detained in State, Federal, or private prisons in the United States. The direct assessments of literacy, numeracy, and problem-solving in technology-rich environments are the same for the adults in prison. The background questionnaire was tailored specifically to address the experiences and needs of this subgroup. For example, the background questionnaire asks about activities in prison, such as participation in academic programs and ESL classes, experiences with prison jobs, and involvement in non-academic programs such as employment readiness classes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "U.S. PIAAC International Data Explorer (IDE)",
                     "description": "U.S. PIAAC IDE provides results from the 2012 PIAAC for the United States, including U.S.-specific variables, and other countries; the 2003 Adult Literacy and Lifeskills Survey (ALL), and the 1994 International Adult Literacy Survey (IALS)",
                     "downloadURL": "https://nces.ed.gov/surveys/piaac/ideuspiaac/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "U.S. PIAAC International Data Explorer (IDE)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for the International Assessment of Adult Competencies (PIAAC) 2014: U.S. National Supplement Public Use Data Files-Prison",
                     "description": "Public use data files for the Program for the International Assessment of Adult Competencies (PIAAC) 2014: U.S. National Supplement-Prison",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2016337",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for the International Assessment of Adult Competencies (PIAAC) 2014: U.S. National Supplement Public Use Data Files-Prison"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Program for the International Assessment of Adult Competencies (PIAAC) 2014: U.S. National Supplement Restricted Use Data Files-Prison",
                     "description": "Restricted use data files for the Program for the International Assessment of Adult Competencies (PIAAC) 2014: U.S. National Supplement-Prison",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2016058",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Program for the International Assessment of Adult Competencies (PIAAC) 2014: U.S. National Supplement Restricted Use Data Files-Prison"
                 }
             ],
+            "identifier": "9d1d9372-1f82-46bb-ab75-0c6098e27c35",
+            "issued": "2016-09-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "adult-literacy",
@@ -45541,35 +45517,14 @@
                 "work-history",
                 "work-responsibilities"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T14:40:03.025988",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://nces.ed.gov/surveys/piaac/questionnaire.asp",
-                "https://nces.ed.gov/surveys/piaac/prison.asp",
-                "https://nces.ed.gov/surveys/piaac/cba.asp",
-                "https://nces.ed.gov/surveys/piaac/pba.asp"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Progress in International Reading Literacy Study, 2001",
-            "description": "The Progress in International Reading Literacy Study, 2001 (PIRLS 2001), is a study that in the Progress in International Reading Literacy Study (PIRLS) program. PIRLS 2001 (https://nces.ed.gov/surveys/pirls/) is a cross-sectional study that provides international comparative information of the reading literacy of fourth-grade students and examines factors that may be associated with the acquisition of reading literacy in young students. The study was conducted using questionnaires and direct assessments of fourth-grade students. In the United States a total of 174 schools were sampled and 3,763 fourth-grade students were tested. The final weighted student response rate was 96 percent and the final weighted school response rate was 86 percent. The overall weighted response rate was 83 percent. Key statistics produced from PIRLS 2001 are how well fourth-grade students read, how students in one country compare with students in another country, how much fourth-grade students value and enjoy reading, and internationally, how the reading habits and attitudes of students vary.",
-            "modified": "2023-07-10T14:38:45.851058",
-            "accessLevel": "public",
-            "identifier": "b7fc9d4b-3e43-46d0-9bd7-e91315c78328",
-            "dataQuality": true,
-            "issued": "2004-08-09",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2000/2001",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -45590,20 +45545,42 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/piaac/questionnaire.asp",
+                "https://nces.ed.gov/surveys/piaac/prison.asp",
+                "https://nces.ed.gov/surveys/piaac/cba.asp",
+                "https://nces.ed.gov/surveys/piaac/pba.asp"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2013/2014",
+            "title": "U.S. Program for the International Assessment of Adult Competencies (PIAAC) National Supplement Prison Study, 2013-14"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sheila Thompson",
                 "hasEmail": "mailto:sheila.thompson@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Progress in International Reading Literacy Study, 2001 (PIRLS 2001), is a study that in the Progress in International Reading Literacy Study (PIRLS) program. PIRLS 2001 (https://nces.ed.gov/surveys/pirls/) is a cross-sectional study that provides international comparative information of the reading literacy of fourth-grade students and examines factors that may be associated with the acquisition of reading literacy in young students. The study was conducted using questionnaires and direct assessments of fourth-grade students. In the United States a total of 174 schools were sampled and 3,763 fourth-grade students were tested. The final weighted student response rate was 96 percent and the final weighted school response rate was 86 percent. The overall weighted response rate was 83 percent. Key statistics produced from PIRLS 2001 are how well fourth-grade students read, how students in one country compare with students in another country, how much fourth-grade students value and enjoy reading, and internationally, how the reading habits and attitudes of students vary.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Progress in International Reading Literacy Study (PIRLS) 2001: U.S. Public-Use Data Files and Electronic Codebook",
                     "description": "Progress in International Reading Literacy Study, 2001  public-use data files and electronic codebook",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2004016",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Progress in International Reading Literacy Study (PIRLS) 2001: U.S. Public-Use Data Files and Electronic Codebook"
                 }
             ],
+            "identifier": "b7fc9d4b-3e43-46d0-9bd7-e91315c78328",
+            "issued": "2004-08-09",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "educational-achievement",
@@ -45612,30 +45589,14 @@
                 "international-comparison",
                 "reading-literacy"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T14:38:45.851058",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Progress in International Reading Literacy Study, 2006",
-            "description": "The Progress in International Reading Literacy Study, 2006 (PIRLS 2006), is a study that is part of the Progress in International Reading Literacy Study (PIRLS) program. PIRLS 2006 (https://nces.ed.gov/surveys/pirls/) is a cross-sectional study that provides international comparative information of the reading literacy of fourth-grade students and examines factors that may be associated with the acquisition of reading literacy in young students. The study was conducted using questionnaires and direct assessments of fourth-grade students. In the United States a total of 183 schools were sampled and 5,190 fourth-grade students were tested. The final weighted student response rate was 95 percent and the final weighted school response rate was 99 percent. The overall weighted response rate was 82 percent. Key statistics produced from PIRLS 2006 are how well fourth-grade students read, how students in one country compare with students in another country, how much fourth-grade students value and enjoy reading, and internationally, how the reading habits and attitudes of students vary.",
-            "modified": "2023-07-10T14:37:13.007640",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "d2727d0b-c506-440a-8d40-5dedba79127d",
-            "dataQuality": true,
-            "issued": "2009-03-30",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2005/2006",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -45656,27 +45617,42 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2000/2001",
+            "title": "Progress in International Reading Literacy Study, 2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sheila Thompson",
                 "hasEmail": "mailto:sheila.thompson@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Progress in International Reading Literacy Study, 2006 (PIRLS 2006), is a study that is part of the Progress in International Reading Literacy Study (PIRLS) program. PIRLS 2006 (https://nces.ed.gov/surveys/pirls/) is a cross-sectional study that provides international comparative information of the reading literacy of fourth-grade students and examines factors that may be associated with the acquisition of reading literacy in young students. The study was conducted using questionnaires and direct assessments of fourth-grade students. In the United States a total of 183 schools were sampled and 5,190 fourth-grade students were tested. The final weighted student response rate was 95 percent and the final weighted school response rate was 99 percent. The overall weighted response rate was 82 percent. Key statistics produced from PIRLS 2006 are how well fourth-grade students read, how students in one country compare with students in another country, how much fourth-grade students value and enjoy reading, and internationally, how the reading habits and attitudes of students vary.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Progress in International Reading Literacy Study (PIRLS) 2006: U.S. Public-Use Data Files and Electronic Codebook",
                     "description": "Progress in International Reading Literacy Study, 2006  public-use data files and electronic codebook",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009061",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Progress in International Reading Literacy Study (PIRLS) 2006: U.S. Public-Use Data Files and Electronic Codebook"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Progress in International Reading Literacy Study (PIRLS) 2006: U.S. Restricted-Use Data Files and Electronic Codebook",
                     "description": "Progress in International Reading Literacy Study, 2006 restricted-use data files and electronic codebook",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009051",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Progress in International Reading Literacy Study (PIRLS) 2006: U.S. Restricted-Use Data Files and Electronic Codebook"
                 }
             ],
+            "identifier": "d2727d0b-c506-440a-8d40-5dedba79127d",
+            "issued": "2009-03-30",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "educational-achievement",
@@ -45685,33 +45661,14 @@
                 "international-comparison",
                 "reading-literacy"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009050"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Progress in International Reading Literacy Study, 2011",
-            "description": "The Progress in International Reading Literacy Study, 2011 (PIRLS 2011), is part of the Progress in International Reading Literacy Study (PIRLS) program. PIRLS 2011 (https://nces.ed.gov/surveys/pirls/) is a cross-sectional study that provides international comparative information of the reading literacy of fourth-grade students and examines factors that may be associated with the acquisition of reading literacy in young students. The study was conducted using questionnaires and direct assessments of fourth-grade students. In the United States a total of 370 schools and 12,726 fourth-grade students participated in 2011. The final weighted student response rate was 96 percent and the final weighted school response rate was 85 percent. The overall weighted response rate was 81 percent. Key statistics produced from PIRLS 2011 are how well fourth-grade students read, how students in one country compare with students in another country, how much fourth-grade students value and enjoy reading, and internationally, how the reading habits and attitudes of students vary.",
-            "modified": "2023-07-10T14:36:23.918601",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "8c7420d2-1baa-4f52-85b4-66e850bc3b43",
-            "dataQuality": true,
-            "issued": "2012-12-31",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2010/2011",
+            "modified": "2023-07-10T14:37:13.007640",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -45732,30 +45689,49 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009050"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2005/2006",
+            "title": "Progress in International Reading Literacy Study, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sheila Thompson",
                 "hasEmail": "mailto:sheila.thompson@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Progress in International Reading Literacy Study, 2011 (PIRLS 2011), is part of the Progress in International Reading Literacy Study (PIRLS) program. PIRLS 2011 (https://nces.ed.gov/surveys/pirls/) is a cross-sectional study that provides international comparative information of the reading literacy of fourth-grade students and examines factors that may be associated with the acquisition of reading literacy in young students. The study was conducted using questionnaires and direct assessments of fourth-grade students. In the United States a total of 370 schools and 12,726 fourth-grade students participated in 2011. The final weighted student response rate was 96 percent and the final weighted school response rate was 85 percent. The overall weighted response rate was 81 percent. Key statistics produced from PIRLS 2011 are how well fourth-grade students read, how students in one country compare with students in another country, how much fourth-grade students value and enjoy reading, and internationally, how the reading habits and attitudes of students vary.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "Progress in International Reading Literacy Study (PIRLS) 2011: U.S. Public-Use Data Files",
-                    "description": "Progress in International Reading Literacy Study, 2011 public-use data",
                     "describedBy": "https://nces.ed.gov/surveys/pirls/zip/PIRLS_2011_Codebooks.zip",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pirls/zip/PIRLS_2011_US_RAW_data.zip"
+                    "description": "Progress in International Reading Literacy Study, 2011 public-use data",
+                    "downloadURL": "https://nces.ed.gov/surveys/pirls/zip/PIRLS_2011_US_RAW_data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "Progress in International Reading Literacy Study (PIRLS) 2011: U.S. Public-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Progress in International Reading Literacy Study (PIRLS) 2011: U.S. restricted-use data file",
                     "description": "Progress in International Reading Literacy Study, 2011 restricted-use data",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2013043",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Progress in International Reading Literacy Study (PIRLS) 2011: U.S. restricted-use data file"
                 }
             ],
+            "identifier": "8c7420d2-1baa-4f52-85b4-66e850bc3b43",
+            "issued": "2012-12-31",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "educational-achievement",
@@ -45764,29 +45740,14 @@
                 "international-comparison",
                 "reading-literacy"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T14:36:23.918601",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Survey on Crime and Safety, 2000",
-            "description": "The School Survey on Crime and Safety, 2000 (SSOCS:2000), is a study that is part of the School Survey on Crime and Safety's program; program data is available since 2000 at <https://nces.ed.gov/surveys/ssocs/data_products.asp>. SSOCS:2000 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. SSOCS is administered to public primary, middle, high, and combined school principals in the spring of even-numbered school years. The study was conducted using a questionnaire and telephone follow-ups of school principals. Public schools were sampled in the spring of 2000 to participate in the study. The study's response rate was 70 percent.  A number of key statistics on a variety of topics can be produced with SSOCS data.",
-            "modified": "2023-07-10T14:30:24.785742",
-            "accessLevel": "public",
-            "identifier": "0858e1cb-bd91-4ccb-8949-d04aa747c788",
-            "dataQuality": true,
-            "issued": "2003-11-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-13-01_060499.pdf",
-            "temporal": "2000/P1Y",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -45807,93 +45768,109 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2010/2011",
+            "title": "Progress in International Reading Literacy Study, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rachel Hansen",
                 "hasEmail": "mailto:rachel.hansen@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The School Survey on Crime and Safety, 2000 (SSOCS:2000), is a study that is part of the School Survey on Crime and Safety's program; program data is available since 2000 at <https://nces.ed.gov/surveys/ssocs/data_products.asp>. SSOCS:2000 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. SSOCS is administered to public primary, middle, high, and combined school principals in the spring of even-numbered school years. The study was conducted using a questionnaire and telephone follow-ups of school principals. Public schools were sampled in the spring of 2000 to participate in the study. The study's response rate was 70 percent.  A number of key statistics on a variety of topics can be produced with SSOCS data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "1999_00_ssocs_sas7bdat.zip",
-                    "description": "SAS data file (version 8)",
                     "describedBy": "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsgde.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs_sas7bdat.zip"
+                    "description": "SAS data file (version 8)",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs_sas7bdat.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "1999_00_ssocs_sas7bdat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SD2",
-                    "title": "1999_00_ssocs_sd2.zip",
-                    "description": "SAS data file (version 6.08-6.12)",
                     "describedBy": "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsgde.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs_sd2.zip"
+                    "description": "SAS data file (version 6.08-6.12)",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs_sd2.zip",
+                    "format": "Zipped SD2",
+                    "mediaType": "application/zip",
+                    "title": "1999_00_ssocs_sd2.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "1999_00_ssocs1_sav.zip",
-                    "description": "SPSS for Windows data file",
                     "describedBy": "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsgde.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs1_sav.zip"
+                    "description": "SPSS for Windows data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs1_sav.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "1999_00_ssocs1_sav.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SYS",
-                    "title": "1999_00_ssocs_sys.zip",
-                    "description": "SPSS for DOS data file",
                     "describedBy": "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsgde.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs_sys.zip"
+                    "description": "SPSS for DOS data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs_sys.zip",
+                    "format": "Zipped SYS",
+                    "mediaType": "application/zip",
+                    "title": "1999_00_ssocs_sys.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped POR",
-                    "title": "1999_00_ssocs2_por.zip",
-                    "description": "SPSS portable data file",
                     "describedBy": "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsgde.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs2_por.zip"
+                    "description": "SPSS portable data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs2_por.zip",
+                    "format": "Zipped POR",
+                    "mediaType": "application/zip",
+                    "title": "1999_00_ssocs2_por.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DTA",
-                    "title": "1999_00_ssocs_dta.zip",
-                    "description": "STATA data file",
                     "describedBy": "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsgde.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs_dta.zip"
+                    "description": "STATA data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/1999_00_ssocs_dta.zip",
+                    "format": "Zipped DTA",
+                    "mediaType": "application/zip",
+                    "title": "1999_00_ssocs_dta.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/plain",
-                    "format": "Fixed-format text",
-                    "title": "1999_00_ssocs-ff.txt",
-                    "description": "Fixed-format ASCII data file",
                     "describedBy": "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsgde.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/txt/1999_00_ssocs-ff.txt"
+                    "description": "Fixed-format ASCII data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/txt/1999_00_ssocs-ff.txt",
+                    "format": "Fixed-format text",
+                    "mediaType": "text/plain",
+                    "title": "1999_00_ssocs-ff.txt"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "CSV",
-                    "title": "1999_00_ssocs-cd.txt",
-                    "description": "Comma-delimited ASCII data file",
                     "describedBy": "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsgde.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/txt/1999_00_ssocs-cd.txt"
+                    "description": "Comma-delimited ASCII data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/txt/1999_00_ssocs-cd.txt",
+                    "format": "CSV",
+                    "mediaType": "text/csv",
+                    "title": "1999_00_ssocs-cd.txt"
                 }
             ],
+            "identifier": "0858e1cb-bd91-4ccb-8949-d04aa747c788",
+            "issued": "2003-11-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "crime",
@@ -45904,32 +45881,14 @@
                 "violence",
                 "violent-incidents-at-school"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsgde.pdf",
-                "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsddd.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Survey on Crime and Safety, 2004",
-            "description": "The School Survey on Crime and Safety, 2004 (SSOCS:2004), is a study that is part of the School Survey on Crime and Safety program. SSOCS:2004 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. SSOCS is administered to public primary, middle, high, and combined school principals in the spring of even-numbered school years.  The study was conducted using a questionnaire and telephone follow-ups of school principals.  Public schools were sampled in the spring of 2004 to participate in the study. The study's response rate was 74 percent.  A number of key statistics on a variety of topics can be produced with SSOCS data.",
-            "modified": "2023-07-10T14:29:24.558405",
-            "accessLevel": "public",
-            "identifier": "6f333283-16c9-4d90-a47e-570cace56296",
-            "dataQuality": true,
-            "issued": "2006-12-28",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2003/2004",
+            "modified": "2023-07-10T14:30:24.785742",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -45950,44 +45909,63 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsgde.pdf",
+                "https://nces.ed.gov/surveys/ssocs/pdf/1999_00_ssocsddd.pdf"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-13-01_060499.pdf",
+            "temporal": "2000/P1Y",
+            "title": "School Survey on Crime and Safety, 2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rachel Hansen",
                 "hasEmail": "mailto:rachel.hansen@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The School Survey on Crime and Safety, 2004 (SSOCS:2004), is a study that is part of the School Survey on Crime and Safety program. SSOCS:2004 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. SSOCS is administered to public primary, middle, high, and combined school principals in the spring of even-numbered school years.  The study was conducted using a questionnaire and telephone follow-ups of school principals.  Public schools were sampled in the spring of 2004 to participate in the study. The study's response rate was 74 percent.  A number of key statistics on a variety of topics can be produced with SSOCS data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/tab-separated-values",
-                    "format": "TSV",
-                    "title": "2003_04_ssocs_puf.txt",
-                    "description": "2004 School Survey on Crime and Safety data as a TSV file",
                     "describedBy": "https://nces.ed.gov/pubs2007/2007333.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/txt/2003_04_ssocs_puf.txt"
+                    "description": "2004 School Survey on Crime and Safety data as a TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/txt/2003_04_ssocs_puf.txt",
+                    "format": "TSV",
+                    "mediaType": "text/tab-separated-values",
+                    "title": "2003_04_ssocs_puf.txt"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "2003_04_ssocs_puf_sas7bdat.zip",
-                    "description": "2004 School Survey on Crime and Safety data as a SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/pubs2007/2007333.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/2003_04_ssocs_puf_sas7bdat.zip"
+                    "description": "2004 School Survey on Crime and Safety data as a SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/2003_04_ssocs_puf_sas7bdat.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "2003_04_ssocs_puf_sas7bdat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "2003_04_ssocs_puf_sav.zip",
-                    "description": "2004 School Survey on Crime and Safety data as a SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/pubs2007/2007333.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/2003_04_ssocs_puf_sav.zip"
+                    "description": "2004 School Survey on Crime and Safety data as a SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/2003_04_ssocs_puf_sav.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "2003_04_ssocs_puf_sav.zip"
                 }
             ],
+            "identifier": "6f333283-16c9-4d90-a47e-570cace56296",
+            "issued": "2006-12-28",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "crime",
@@ -45999,32 +45977,14 @@
                 "violence",
                 "violent-incidents-at-school"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2007/2007335.pdf",
-                "https://nces.ed.gov/surveys/ssocs/data/txt/2003_04_readme.txt"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Survey on Crime and Safety, 2006",
-            "description": "The School Survey on Crime and Safety, 2006 (SSOCS:2006), is a study that is part of the School Survey on Crime and Safety program. SSOCS:2006 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. SSOCS is administered to public primary, middle, high, and combined school principals in the spring of even-numbered school years.  The study was conducted using a questionnaire and telephone follow-ups of school principals.  Public schools were sampled in the spring of 2006 to participate in the study. The study's response rate was 77.5 percent. A number of key statistics on a variety of topics can be produced with SSOCS data.",
-            "modified": "2023-07-10T14:28:21.847582",
-            "accessLevel": "public",
-            "identifier": "a93ff3ed-2d52-407b-90cf-ae72784d6d76",
-            "dataQuality": true,
-            "issued": "2007-09-25",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2005/2006",
+            "modified": "2023-07-10T14:29:24.558405",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -46045,54 +46005,72 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2007/2007335.pdf",
+                "https://nces.ed.gov/surveys/ssocs/data/txt/2003_04_readme.txt"
+            ],
+            "spatial": "United States",
+            "temporal": "2003/2004",
+            "title": "School Survey on Crime and Safety, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rachel Hansen",
                 "hasEmail": "mailto:rachel.hansen@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The School Survey on Crime and Safety, 2006 (SSOCS:2006), is a study that is part of the School Survey on Crime and Safety program. SSOCS:2006 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. SSOCS is administered to public primary, middle, high, and combined school principals in the spring of even-numbered school years.  The study was conducted using a questionnaire and telephone follow-ups of school principals.  Public schools were sampled in the spring of 2006 to participate in the study. The study's response rate was 77.5 percent. A number of key statistics on a variety of topics can be produced with SSOCS data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/tab-separated-values",
-                    "format": "TSV",
-                    "title": "SSOCS06_ASCII.txt",
-                    "description": "2006 School Survey on Crime and Safety data as a TSV file",
                     "describedBy": "https://nces.ed.gov/pubs2009/2009312.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/txt/SSOCS06_ASCII.txt"
+                    "description": "2006 School Survey on Crime and Safety data as a TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/txt/SSOCS06_ASCII.txt",
+                    "format": "TSV",
+                    "mediaType": "text/tab-separated-values",
+                    "title": "SSOCS06_ASCII.txt"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "2005_06_ssocs06_sas7bdat.zip",
-                    "description": "2006 School Survey on Crime and Safety data as a SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/pubs2009/2009312.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/2005_06_ssocs06_sas7bdat.zip"
+                    "description": "2006 School Survey on Crime and Safety data as a SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/2005_06_ssocs06_sas7bdat.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "2005_06_ssocs06_sas7bdat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "ssocs06_spss.zip",
-                    "description": "2006 School Survey on Crime and Safety data as a SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/pubs2009/2009312.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/ssocs06_spss.zip"
+                    "description": "2006 School Survey on Crime and Safety data as a SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/ssocs06_spss.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "ssocs06_spss.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DTA",
-                    "title": "ssocs06_stata.zip",
-                    "description": "2006 School Survey on Crime and Safety data as a Stata-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/pubs2009/2009312.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/ssocs06_stata.zip"
+                    "description": "2006 School Survey on Crime and Safety data as a Stata-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/ssocs06_stata.zip",
+                    "format": "Zipped DTA",
+                    "mediaType": "application/zip",
+                    "title": "ssocs06_stata.zip"
                 }
             ],
+            "identifier": "a93ff3ed-2d52-407b-90cf-ae72784d6d76",
+            "issued": "2007-09-25",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "crime",
@@ -46104,32 +46082,14 @@
                 "violence",
                 "violent-incidents-at-school"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2007/2007335.pdf",
-                "https://nces.ed.gov/surveys/ssocs/pdf/ssocs06_methodology.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Survey on Crime and Safety, 2008",
-            "description": "The School Survey on Crime and Safety, 2008 (SSOCS:2008), is a study that is part of the School Survey on Crime and Safety program. SSOCS:2008 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. SSOCS is administered to public primary, middle, high, and combined school principals in the spring of even-numbered school years.  The study was conducted using a questionnaire and telephone follow-ups of school principals.  Public schools were sampled in the spring of 2008 to participate in the study.  The study's response rate was 74.5 percent.  A number of key statistics on a variety of topics can be produced with SSOCS data.",
-            "modified": "2023-07-10T14:27:33.253296",
-            "accessLevel": "public",
-            "identifier": "6967ce90-616f-4b1d-aabc-5e30ca7dc61c",
-            "dataQuality": true,
-            "issued": "2009-05-05",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2007/2008",
+            "modified": "2023-07-10T14:28:21.847582",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -46150,54 +46110,72 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2007/2007335.pdf",
+                "https://nces.ed.gov/surveys/ssocs/pdf/ssocs06_methodology.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2005/2006",
+            "title": "School Survey on Crime and Safety, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rachel Hansen",
                 "hasEmail": "mailto:rachel.hansen@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The School Survey on Crime and Safety, 2008 (SSOCS:2008), is a study that is part of the School Survey on Crime and Safety program. SSOCS:2008 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. SSOCS is administered to public primary, middle, high, and combined school principals in the spring of even-numbered school years.  The study was conducted using a questionnaire and telephone follow-ups of school principals.  Public schools were sampled in the spring of 2008 to participate in the study.  The study's response rate was 74.5 percent.  A number of key statistics on a variety of topics can be produced with SSOCS data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/tab-separated-values",
-                    "format": "TSV",
-                    "title": "pu_ssocs08_ASCII.txt",
-                    "description": "2008 School Survey on Crime and Safety data as a TSV file",
                     "describedBy": "https://nces.ed.gov/pubs2010/2010334.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/txt/pu_ssocs08_ASCII.txt"
+                    "description": "2008 School Survey on Crime and Safety data as a TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/txt/pu_ssocs08_ASCII.txt",
+                    "format": "TSV",
+                    "mediaType": "text/tab-separated-values",
+                    "title": "pu_ssocs08_ASCII.txt"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "pu_ssocs08_sas.zip",
-                    "description": "2008 School Survey on Crime and Safety data as a SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/pubs2010/2010334.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/pu_ssocs08_sas.zip"
+                    "description": "2008 School Survey on Crime and Safety data as a SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/pu_ssocs08_sas.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "pu_ssocs08_sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "pu_ssocs08_spss.zip",
-                    "description": "2008 School Survey on Crime and Safety data as a SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/pubs2010/2010334.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/pu_ssocs08_spss.zip"
+                    "description": "2008 School Survey on Crime and Safety data as a SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/pu_ssocs08_spss.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "pu_ssocs08_spss.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DTA",
-                    "title": "pu_ssocs08_stata.zip",
-                    "description": "2008 School Survey on Crime and Safety data as a Stata-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/pubs2010/2010334.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/pu_ssocs08_stata.zip"
+                    "description": "2008 School Survey on Crime and Safety data as a Stata-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/ssocs/data/zip/pu_ssocs08_stata.zip",
+                    "format": "Zipped DTA",
+                    "mediaType": "application/zip",
+                    "title": "pu_ssocs08_stata.zip"
                 }
             ],
+            "identifier": "6967ce90-616f-4b1d-aabc-5e30ca7dc61c",
+            "issued": "2009-05-05",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "crime",
@@ -46209,32 +46187,14 @@
                 "violence",
                 "violent-incidents-at-school"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2010/2010307.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Survey on Crime and Safety, 2010",
-            "description": "The School Survey on Crime and Safety, 2010 (SSOCS:2010), is a study that is part of the School Survey on Crime and Safety program. SSOCS:2010 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. SSOCS is administered to public primary, middle, high, and combined school principals in the spring of even numbered school years. The study was conducted using a questionnaire and telephone follow-ups of school principals. Public schools were sampled in the spring of 2010 to participate in the study. The study's response rate was 74.3 percent. A number of key statistics on a variety of topics can be produced with SSOCS data.",
-            "modified": "2023-07-10T14:26:29.455136",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "527238ab-6fe1-493f-bc05-8b65c288a31b",
-            "dataQuality": true,
-            "issued": "2011-05-31",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2009/2010",
+            "modified": "2023-07-10T14:27:33.253296",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -46255,29 +46215,46 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2010/2010307.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2007/2008",
+            "title": "School Survey on Crime and Safety, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rachel Hansen",
                 "hasEmail": "mailto:rachel.hansen@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The School Survey on Crime and Safety, 2010 (SSOCS:2010), is a study that is part of the School Survey on Crime and Safety program. SSOCS:2010 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. SSOCS is administered to public primary, middle, high, and combined school principals in the spring of even numbered school years. The study was conducted using a questionnaire and telephone follow-ups of school principals. Public schools were sampled in the spring of 2010 to participate in the study. The study's response rate was 74.3 percent. A number of key statistics on a variety of topics can be produced with SSOCS data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2009-10 School Survey on Crime and Safety (SSOCS) Restricted-Use Data Files and User's Manual",
                     "description": "Restricted-use data file for the 2010 School Survey on Crime and Safety",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011322",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2009-10 School Survey on Crime and Safety (SSOCS) Restricted-Use Data Files and User's Manual"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TXT",
-                    "title": "2015060_data.zip",
                     "description": "2009-10 School Survey on Crime and Safety: Public-Use Data Files and Codebook",
-                    "downloadURL": "https://nces.ed.gov/pubs2015/data/2015060_data.zip"
+                    "downloadURL": "https://nces.ed.gov/pubs2015/data/2015060_data.zip",
+                    "format": "Zipped TXT",
+                    "mediaType": "application/zip",
+                    "title": "2015060_data.zip"
                 }
             ],
+            "identifier": "527238ab-6fe1-493f-bc05-8b65c288a31b",
+            "issued": "2011-05-31",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "crime",
@@ -46289,32 +46266,14 @@
                 "violence",
                 "violent-incidents-at-school"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2010/2010307.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Survey on Crime and Safety, 2016",
-            "description": "The 2016 School Survey on Crime and Safety (SSOCS:2016) is a data collection that is part of the School Survey on Crime and Safety program; program data are available since 2000 at <https://nces.ed.gov/surveys/ssocs/data_products.asp>. SSOCS:2016 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. Regular public schools were sampled. The data collection was conducted using a mail questionnaire with telephone follow-up. The data collection's response rate was 62.9 percent. Key statistics produced from SSOCS:2016 include the frequency and types of disciplinary actions taken for select offenses; perceptions of other disciplinary problems, such as bullying, verbal abuse and disorder in the classroom; the presence and role of school security staff; parent and community involvement; staff training; mental health services available to students; and school policies and programs concerning crime and safety.",
-            "modified": "2023-07-10T14:25:39.795725",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "2fb93382-093f-4984-88f5-0f3a3f275da7",
-            "dataQuality": true,
-            "issued": "2017-12-08",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2015/2016",
+            "modified": "2023-07-10T14:26:29.455136",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -46335,29 +46294,47 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2010/2010307.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2009/2010",
+            "title": "School Survey on Crime and Safety, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rachel Hansen",
                 "hasEmail": "mailto:rachel.hansen@ed.gov"
             },
```

