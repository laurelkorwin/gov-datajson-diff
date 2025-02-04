# Change History for ed.json (Part 6)

### Changes from 31606f9 to dd2190f (Part 6/13)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "dataQuality": true,
+            "description": "The 2016 School Survey on Crime and Safety (SSOCS:2016) is a data collection that is part of the School Survey on Crime and Safety program; program data are available since 2000 at <https://nces.ed.gov/surveys/ssocs/data_products.asp>. SSOCS:2016 (https://nces.ed.gov/surveys/ssocs/) is a cross-sectional survey of the nation's public schools designed to provide estimates of school crime, discipline, disorder, programs and policies. Regular public schools were sampled. The data collection was conducted using a mail questionnaire with telephone follow-up. The data collection's response rate was 62.9 percent. Key statistics produced from SSOCS:2016 include the frequency and types of disciplinary actions taken for select offenses; perceptions of other disciplinary problems, such as bullying, verbal abuse and disorder in the classroom; the presence and role of school security staff; parent and community involvement; staff training; mental health services available to students; and school policies and programs concerning crime and safety.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2015-16 School Survey on Crime and Safety (SSOCS) Restricted-Use Data Files and User's Manual",
                     "description": "Restricted-use data file for the 2016 School Survey on Crime and Safety",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2017129",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2015-16 School Survey on Crime and Safety (SSOCS) Restricted-Use Data Files and User's Manual"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TXT",
-                    "title": "2018109.zip",
                     "description": "2015-16 School Survey on Crime and Safety: Public-Use Data Files and Codebook",
-                    "downloadURL": "https://nces.ed.gov/pubs2018/data/2018109.zip"
+                    "downloadURL": "https://nces.ed.gov/pubs2018/data/2018109.zip",
+                    "format": "Zipped TXT",
+                    "mediaType": "application/zip",
+                    "title": "2018109.zip"
                 }
             ],
+            "identifier": "2fb93382-093f-4984-88f5-0f3a3f275da7",
+            "issued": "2017-12-08",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "disciplinary-actions",
@@ -46378,33 +46355,14 @@
                 "violence",
                 "violent-incidents-at-school"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T14:25:39.795725",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2018107"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Schools and Staffing Survey, 1993-94",
-            "description": "The Schools and Staffing Survey, 1993-94 (SASS 93-94), is a study that is part of the Schools and Staffing Survey (SASS) program; program data is available since 1987-88 at <https://nces.ed.gov/surveys/sass/dataproducts.asp>. SASS 93-94 (https://nces.ed.gov/surveys/sass) is a collection of surveys that cover a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers' perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention practices, to basic characteristics of the student population and school library resources and staffing. The surveys were conducted using questionnaires, personal interviews, list data, and telephone interviews. Superintendents, teachers, librarians, principals, and school coordinators were sampled. Key statistics from SASS 93-94 are the percentage of newly-hired teachers, average teacher salary, average principal salary, percentage distribution of students receiving free or reduced-price lunches, percentage distribution of students by race and ethnicity, percentage distribution of teachers and principals by race and ethnicity, and age distributions of teachers and principals.",
-            "modified": "2023-07-10T13:57:00.547028",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "d718a6cc-ac12-47a2-9936-e196d4b85e33",
-            "dataQuality": true,
-            "issued": "1995-07-18",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1993/1994",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -46425,55 +46383,73 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2018107"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2015/2016",
+            "title": "School Survey on Crime and Safety, 2016"
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
+            "description": "The Schools and Staffing Survey, 1993-94 (SASS 93-94), is a study that is part of the Schools and Staffing Survey (SASS) program; program data is available since 1987-88 at <https://nces.ed.gov/surveys/sass/dataproducts.asp>. SASS 93-94 (https://nces.ed.gov/surveys/sass) is a collection of surveys that cover a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers' perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention practices, to basic characteristics of the student population and school library resources and staffing. The surveys were conducted using questionnaires, personal interviews, list data, and telephone interviews. Superintendents, teachers, librarians, principals, and school coordinators were sampled. Key statistics from SASS 93-94 are the percentage of newly-hired teachers, average teacher salary, average principal salary, percentage distribution of students receiving free or reduced-price lunches, percentage distribution of students by race and ethnicity, percentage distribution of teachers and principals by race and ethnicity, and age distributions of teachers and principals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "1993-94 SASS Public-Use Data and Documentation",
                     "description": "1993-94 Schools and Staffing Survey public-use data files",
                     "downloadURL": "https://nces.ed.gov/surveys/sass/dataprod9395.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "1993-94 SASS Public-Use Data and Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "1993-94 Schools and Staffing Survey: Data File User's Manual: Volume II: Restricted-Use Codebook",
                     "description": "This volume documents the data collection of the 1993-94 Schools and Staffing Survey (SASS) and contains the layout and descriptive information on all survey and sampling variables.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=97573",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "1993-94 Schools and Staffing Survey: Data File User's Manual: Volume II: Restricted-Use Codebook"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "1993-94 Schools and Staffing Survey: Data File User's Manual, Volume III: Public-Use Codebook",
                     "description": "The public-use codebook contains the unweighted count of responses for each data item and most components of SASS in 1993-94. This codebook supplements the electronic codebook on the SASS and TFS CD-ROM by using the exact text of the questionnaire item and adding skip instructions as found on the questionnaire. Copies of the questionnaires are published in Volume I (Survey Documentation) of the Data File User's Manual.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=199912",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "1993-94 Schools and Staffing Survey: Data File User's Manual, Volume III: Public-Use Codebook"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "1993-94 Schools and Staffing Survey: Data File User's Manual, Volume IV: Bureau of Indian Affairs (BIA) Restricted-Use Codebook",
                     "description": "This volume of the Data File User's Manual contains the unweighted counts of responses to all SASS questionnaires administered to Bureau of Indian Affairs or tribally-operated schools, their teachers, and their principals. The file for BIA schools, principals, and teachers is produced only for researchers, as the number of BIA schools is small. Additionally, this codebook includes responses to the Student Records data file, as a number of items pertain to American Indian students. The questionnaires were published in the Data File User's Manual, Volume I (Survey Documentation).",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=199913",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "1993-94 Schools and Staffing Survey: Data File User's Manual, Volume IV: Bureau of Indian Affairs (BIA) Restricted-Use Codebook"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "1994-95 Teacher Followup Survey: Data File User's Manual Restricted-Use Codebook",
                     "description": "This volume of the Data File User's Manual contains the survey documentation and codebook for the 1994-95 Teacher Followup Survey. The TFS is a one-year followup of a subset of teachers who responded to the 1993-94 SASS. The codebook contains the exact questionnaire wording and unweighted count of responses to each item. The teachers' responses to the 1993-94 SASS are also included. A copy of the questionnaires for current and for former teachers are published as part of this manual.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=199914",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "1994-95 Teacher Followup Survey: Data File User's Manual Restricted-Use Codebook"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "1994-95 Teacher Followup Survey Data File User's Manual, Public-Use Version",
                     "description": "The 1994-95 Teacher Followup Survey data in this report links responses from the 1994-95 school year to characteristics of those same teachers who participated in the 1993-94 school year SASS. Within this report, there are some data that are drawn directly from the 1993-94 SASS. These data are termed \"base year\" because the SASS sample is the \"base\" for the teachers who are selected for the Teacher Followup Survey.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=98232",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "1994-95 Teacher Followup Survey Data File User's Manual, Public-Use Version"
                 }
             ],
+            "identifier": "d718a6cc-ac12-47a2-9936-e196d4b85e33",
+            "issued": "1995-07-18",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "bia",
@@ -46491,32 +46467,14 @@
                 "secondary",
                 "teacher"
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
-                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=97573"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Schools and Staffing Survey, 2003-04",
-            "description": "The Schools and Staffing Survey, 2003-04 (SASS 03-04), is a study that is part of the Schools and Staffing Survey (SASS) program. SASS 03-04 (https://nces.ed.gov/surveys/sass) is a survey that covers a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers' perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention practices, to basic characteristics of the student population. The survey was conducted using mail, email, paper questionnaires, and telephone interviews. Teachers, librarians, principals, and school coordinators were sampled. Key statistics produced from SASS 03-04 are how many teachers and principals remained at the same school, moved to another school, or left the profession in the year following the SASS administration.",
-            "modified": "2023-07-10T13:54:50.791507",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "fa4f04f8-cae2-44be-aabb-91c70903a0e5",
-            "dataQuality": true,
-            "issued": "2006-03-23",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2003/2004",
+            "modified": "2023-07-10T13:57:00.547028",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -46537,35 +46495,54 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=97573"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1993/1994",
+            "title": "Schools and Staffing Survey, 1993-94"
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
+            "description": "The Schools and Staffing Survey, 2003-04 (SASS 03-04), is a study that is part of the Schools and Staffing Survey (SASS) program. SASS 03-04 (https://nces.ed.gov/surveys/sass) is a survey that covers a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers' perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention practices, to basic characteristics of the student population. The survey was conducted using mail, email, paper questionnaires, and telephone interviews. Teachers, librarians, principals, and school coordinators were sampled. Key statistics produced from SASS 03-04 are how many teachers and principals remained at the same school, moved to another school, or left the profession in the year following the SASS administration.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Datalab for Schools and Staffing Survey",
                     "description": "The SASS data available in PowerStats are comprised of data collected from five SASS questionnaires: the School Questionnaire, Teacher Questionnaire, School Principal Questionnaire, School District Questionnaire, and Library Media Center Questionnaire",
                     "downloadURL": "https://nces.ed.gov/datalab/sass/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Datalab for Schools and Staffing Survey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2003-04 Schools and Staffing Survey (SASS) and 2004-05 Teacher Follow-up Survey (TFS) (CD ROM) Restricted-Use Data with Electronic Codebook",
                     "description": "Restricted-use data file for the 2003-04 School and Staffing Survey",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008309",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2003-04 Schools and Staffing Survey (SASS) and 2004-05 Teacher Follow-up Survey (TFS) (CD ROM) Restricted-Use Data with Electronic Codebook"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2003-04 Schools and Staffing Survey (SASS) CD-ROM: Restricted-Use Data with Electronic Codebook",
                     "description": "Restricted-use data file for the 2003-04 School and Staffing Survey",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2007313",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2003-04 Schools and Staffing Survey (SASS) CD-ROM: Restricted-Use Data with Electronic Codebook"
                 }
             ],
+            "identifier": "fa4f04f8-cae2-44be-aabb-91c70903a0e5",
+            "issued": "2006-03-23",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "charter-schools",
@@ -46574,42 +46551,14 @@
                 "public-schools",
                 "teachers"
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
-                "https://nces.ed.gov/pubs2007/2007337.pdf",
-                "https://nces.ed.gov/surveys/sass/pdf/0304/sass16.pdf",
-                "https://nces.ed.gov/surveys/sass/pdf/0304/sass1a.pdf",
-                "https://nces.ed.gov/surveys/sass/pdf/0304/sass3a.pdf",
-                "https://nces.ed.gov/surveys/sass/pdf/0304/sass3b.pdf",
-                "https://nces.ed.gov/surveys/sass/pdf/0304/sass3y.pdf",
-                "https://nces.ed.gov/surveys/sass/pdf/0304/sass2a.pdf",
-                "https://nces.ed.gov/surveys/sass/pdf/0304/sass2b.pdf",
-                "https://nces.ed.gov/surveys/sass/pdf/0304/sass4a.pdf",
-                "https://nces.ed.gov/surveys/sass/pdf/0304/sass4b.pdf",
-                "https://nces.ed.gov/surveys/sass/pdf/0304/sass_ls1a.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Schools and Staffing Survey, 2007-08",
-            "description": "The Schools and Staffing Survey, 2007-08 (SASS 07-08), is a study that is part of the Schools and Staffing Survey (SASS) program. SASS 07-08 (https://nces.ed.gov/surveys/sass/) is a cross-sectional survey that collects data on public, private, and Bureau of Indian Education (BIE) elementary and secondary schools across the nation. The survey was primarily conducted through the use of mailed paper questionnaires. Nonresponse follow-up interviews were conducted using computer-assisted telephone interviews and face-to-face paper interviews. Teachers, librarians, principals, and districts were sampled. Key statistics produced from SASS 07-08 included how many teachers remained at the same school, moved to another school, or left the profession in the year following the SASS administration.",
-            "modified": "2023-07-10T13:54:20.273481",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "6f90093a-6012-4fac-81fc-11c697293747",
-            "dataQuality": true,
-            "issued": "2006-03-23",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2007/2008",
+            "modified": "2023-07-10T13:54:50.791507",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -46630,91 +46579,119 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2007/2007337.pdf",
+                "https://nces.ed.gov/surveys/sass/pdf/0304/sass16.pdf",
+                "https://nces.ed.gov/surveys/sass/pdf/0304/sass1a.pdf",
+                "https://nces.ed.gov/surveys/sass/pdf/0304/sass3a.pdf",
+                "https://nces.ed.gov/surveys/sass/pdf/0304/sass3b.pdf",
+                "https://nces.ed.gov/surveys/sass/pdf/0304/sass3y.pdf",
+                "https://nces.ed.gov/surveys/sass/pdf/0304/sass2a.pdf",
+                "https://nces.ed.gov/surveys/sass/pdf/0304/sass2b.pdf",
+                "https://nces.ed.gov/surveys/sass/pdf/0304/sass4a.pdf",
+                "https://nces.ed.gov/surveys/sass/pdf/0304/sass4b.pdf",
+                "https://nces.ed.gov/surveys/sass/pdf/0304/sass_ls1a.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2003/2004",
+            "title": "Schools and Staffing Survey, 2003-04"
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
+            "description": "The Schools and Staffing Survey, 2007-08 (SASS 07-08), is a study that is part of the Schools and Staffing Survey (SASS) program. SASS 07-08 (https://nces.ed.gov/surveys/sass/) is a cross-sectional survey that collects data on public, private, and Bureau of Indian Education (BIE) elementary and secondary schools across the nation. The survey was primarily conducted through the use of mailed paper questionnaires. Nonresponse follow-up interviews were conducted using computer-assisted telephone interviews and face-to-face paper interviews. Teachers, librarians, principals, and districts were sampled. Key statistics produced from SASS 07-08 included how many teachers remained at the same school, moved to another school, or left the profession in the year following the SASS administration.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Datalab for Schools and Staffing Survey",
                     "description": "The SASS data available in PowerStats are comprised of data collected from five SASS questionnaires: the School Questionnaire, Teacher Questionnaire, School Principal Questionnaire, School District Questionnaire, and Library Media Center Questionnaire",
                     "downloadURL": "https://nces.ed.gov/datalab/sass/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Datalab for Schools and Staffing Survey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2007-08 Schools and Staffing Survey (SASS) and 2008-09 Teacher Follow-up Survey (TFS) (CD ROM) Restricted-Use Data with Codebook",
                     "description": "Restricted-use data file for the 2007-08 School and Staffing Survey",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2010363",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2007-08 Schools and Staffing Survey (SASS) and 2008-09 Teacher Follow-up Survey (TFS) (CD ROM) Restricted-Use Data with Codebook"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2007-08 Schools and Staffing Survey Public Charter School Analysis Restricted-Use Data File",
                     "description": "Restricted-use data file for the 2007-08 School and Staffing Survey; the Public Charter School Analysis data file contains additional variables not processed with the rest of SASS",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012310",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2007-08 Schools and Staffing Survey Public Charter School Analysis Restricted-Use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2007-08 Schools and Staffing Survey restricted-use data files in SAS and ASCII formats (12 files)",
                     "description": "Restricted-use data file for the 2007-08 School and Staffing Survey",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009344",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2007-08 Schools and Staffing Survey restricted-use data files in SAS and ASCII formats (12 files)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2008-09 Teacher Status Files",
                     "description": "Restricted-use data files which report on the status of teachers from the Schools and Staffing Survey one year later, in fall 2008-09. The teachers' status is reported by the school principal. Also included is an analysis of a comparison between the previous Teacher Status File from 2004-05 and the teachers' own reports in the Teacher Follow-up Survey.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2010333",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2008-09 Teacher Status Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2007-08 Schools and Staffing Survey (SASS) and 2008-09 Teacher Follow-up Survey (TFS) (CD ROM) Restricted-Use Data with Codebook",
                     "description": "The restricted-use codebook contains the count of responses for each data item and all components of SASS in 2007-2008 and the 2008-2009 TFS. The TFS data and User's manual are the added features to this re-release of the 2007-2008 SASS restricted-use ECB.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2010363",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2007-08 Schools and Staffing Survey (SASS) and 2008-09 Teacher Follow-up Survey (TFS) (CD ROM) Restricted-Use Data with Codebook"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2007-08 Schools and Staffing Survey Public Charter School Analysis Restricted-Use Data File",
                     "description": "This file contains additional data collected from public charter schools that are under the jurisdiction of a regular school district. These \"district-type\" items were not processed at the same time as the other 2007-08 SASS data. The data are weighted with public school weights appropriate for public charter schools.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012310",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2007-08 Schools and Staffing Survey Public Charter School Analysis Restricted-Use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Restricted-Use Public Charter School Analysis Data File User's Manual: 2007-08 Schools and Staffing Survey",
                     "description": "Survey documentation for an additional data file issued after the release of the 2007-08 SASS data files. The Public Charter School Analysis data file contains additional variables not processed with the rest of SASS. This technical information is about all aspects of the public charter school analysis data file, from data collection through weighting.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012311",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Restricted-Use Public Charter School Analysis Data File User's Manual: 2007-08 Schools and Staffing Survey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Principal Follow-up Survey 2008-09 restricted-use data files",
                     "description": "Data from the 2008-09 Principal Follow-up Survey as well as from the 2007-08 Schools and Staffing Survey's Principal survey. Documentation about the survey is included.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2010360",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Principal Follow-up Survey 2008-09 restricted-use data files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Beginning Teacher Longitudinal Study (BTLS) Waves 1-3 Preliminary Restricted-Use Data File and Documentation",
                     "description": "This restricted-use CD includes the combined wave 1 through wave 3 data file, questionnaires, codebook, file layout, and User\u00c3\u0192\u00c6\u2019\u00c3\u201a\u00c2\u00af\u00c3\u0192\u00e2\u20ac\u0161\u00c3\u201a\u00c2\u00bf\u00c3\u0192\u00e2\u20ac\u0161\u00c3\u201a\u00c2\u00bds Manual. The data files are in SAS and ASCII formats, with syntax for creating files in SPSS and STATA. The codebook contains the count of responses for each data item. The User's Manual explains the survey methodology and provides other information about the structure and content of the data file.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011359",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Beginning Teacher Longitudinal Study (BTLS) Waves 1-3 Preliminary Restricted-Use Data File and Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Beginning Teacher Longitudinal Study (BTLS) Waves 1-5 Restricted-Use Data File and Documentation",
                     "description": "This restricted-use CD includes the combined wave 1 through wave 5 data file, questionnaires, codebook, file layout, and User\u00c3\u0192\u00c6\u2019\u00c3\u201a\u00c2\u00af\u00c3\u0192\u00e2\u20ac\u0161\u00c3\u201a\u00c2\u00bf\u00c3\u0192\u00e2\u20ac\u0161\u00c3\u201a\u00c2\u00bds Manual. The data files are in SAS and ASCII formats, with syntax for creating files in SPSS and STATA. The codebook contains the count of responses for each data item. The User's Manual explains the survey methodology and provides other information about the structure and content of the data file.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2015059",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Beginning Teacher Longitudinal Study (BTLS) Waves 1-5 Restricted-Use Data File and Documentation"
                 }
             ],
+            "identifier": "6f90093a-6012-4fac-81fc-11c697293747",
+            "issued": "2006-03-23",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "charter-schools",
@@ -46735,33 +46712,14 @@
                 "teacher-satisfaction",
                 "teachers"
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
-                "https://nces.ed.gov/pubs2010/2010332.pdf",
-                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012311"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Schools and Staffing Survey, 2011-12",
-            "description": "The Schools and Staffing Survey, 2011-12 (SASS 11-12), is a study that is part of the Schools and Staffing Survey (SASS) program. SASS 11-12 (https://nces.ed.gov/surveys/sass/) is a survey that covers a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers' perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention practices, to basic characteristics of the student population. The survey was conducted using mail, email, and telephone interviews. Schools, teachers, librarians, and principals were sampled. Key statistics produced from SASS 11-12 are how many teachers and principals remained at the same school, moved to another school, or left the profession in the year following the SASS administration.",
-            "modified": "2023-07-10T13:53:43.646662",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "be5261c2-208a-4e43-aa99-bb5cd023f1ed",
-            "dataQuality": true,
-            "issued": "2013-11-06",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
+            "modified": "2023-07-10T13:54:20.273481",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -46782,28 +46740,47 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2010/2010332.pdf",
+                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012311"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2007/2008",
+            "title": "Schools and Staffing Survey, 2007-08"
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
+            "description": "The Schools and Staffing Survey, 2011-12 (SASS 11-12), is a study that is part of the Schools and Staffing Survey (SASS) program. SASS 11-12 (https://nces.ed.gov/surveys/sass/) is a survey that covers a wide range of topics from teacher demand, teacher and principal characteristics, general conditions in schools, principals' and teachers' perceptions of school climate and problems in their schools, teacher compensation, district hiring and retention practices, to basic characteristics of the student population. The survey was conducted using mail, email, and telephone interviews. Schools, teachers, librarians, and principals were sampled. Key statistics produced from SASS 11-12 are how many teachers and principals remained at the same school, moved to another school, or left the profession in the year following the SASS administration.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Datalab for Schools and Staffing Survey",
                     "description": "The SASS data available in PowerStats are comprised of data collected from five SASS questionnaires: the School Questionnaire, Teacher Questionnaire, School Principal Questionnaire, School District Questionnaire, and Library Media Center Questionnaire",
                     "downloadURL": "https://nces.ed.gov/datalab/sass/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Datalab for Schools and Staffing Survey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2011-12 Schools and Staffing Survey (SASS) Restricted-Use Data Files",
                     "description": "Restricted-use data file for the 2011-12 School and Staffing Survey",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014356",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2011-12 Schools and Staffing Survey (SASS) Restricted-Use Data Files"
                 }
             ],
+            "identifier": "be5261c2-208a-4e43-aa99-bb5cd023f1ed",
+            "issued": "2013-11-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "elementary-and-secondary-education",
@@ -46825,32 +46802,17 @@
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
+            "modified": "2023-07-10T13:53:43.646662",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Evaluation of the Effectiveness of the Alabama Mathematics, Science, and Technology Initiative",
-            "description": "The Evaluation of the Effectiveness of the Alabama Mathematics, Science, and Technology Initiative (AMSTI Evaluation) is a study with data available since 2012 at <https://ies.ed.gov/pubsearch/>. AMSTI Evaluation is a cross-sectional survey that determined the effect of the AMSTI program, which is designed as a whole-school reform initiative providing professional development, access to materials and technology, and in-school support for teachers. Specifically, this study examined the effects of the program on student achievement. The study was conducted using surveys and interviews of teachers and principal with administrative data being collected from the Alabama State Department of Education. Elementary and middle schools were sampled. The study's response rate is to be determined. Key statistics produced from AMSTI Evaluation are the effect of the program on student achievement in mathematics, reading, and science.",
-            "modified": "2023-07-10T13:51:17.927330",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "c420b1a5-dff9-42f3-aacc-95b2e2a23fbf",
-            "issued": "2012-11-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "http://",
-            "temporal": "2006/2010",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Evaluation and Regional Assistance (NCEERA)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Institute of Education Sciences (IES)",
@@ -46868,24 +46830,38 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "Schools and Staffing Survey, 2011-12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Hughes",
                 "hasEmail": "mailto:jhughes@fcrr.org"
             },
+            "description": "The Evaluation of the Effectiveness of the Alabama Mathematics, Science, and Technology Initiative (AMSTI Evaluation) is a study with data available since 2012 at <https://ies.ed.gov/pubsearch/>. AMSTI Evaluation is a cross-sectional survey that determined the effect of the AMSTI program, which is designed as a whole-school reform initiative providing professional development, access to materials and technology, and in-school support for teachers. Specifically, this study examined the effects of the program on student achievement. The study was conducted using surveys and interviews of teachers and principal with administrative data being collected from the Alabama State Department of Education. Elementary and middle schools were sampled. The study's response rate is to be determined. Key statistics produced from AMSTI Evaluation are the effect of the program on student achievement in mathematics, reading, and science.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "Restricted Use CD-ROM",
-                    "title": "The Effectiveness of the Alabama Math, Science, and Technology Initiative (AMSTI)",
-                    "description": "The Effectiveness of the Alabama Math, Science, and Technology Initiative (AMSTI) Restricted Use File",
                     "describedBy": "https://datainventory.ed.gov/Search?txtMenuSearchTerm=&txtSearchTerm=&searchTerm=Southeast%20Regional%20Education%20Laboratory%20REL%20Southeast&advanced_search=&rdSearchType=Exact&seriesID=1327&studyID=25865&studyType=study&seriesVar=&seriesVarTerm=&seriesVarType=Exact&studyVar=&studyVarTerm=&studyVarType=Exact&currentSearch=",
                     "describedByType": "text/html",
-                    "downloadURL": "http://nces.ed.gov/statprog/instruct.asp"
+                    "description": "The Effectiveness of the Alabama Math, Science, and Technology Initiative (AMSTI) Restricted Use File",
+                    "downloadURL": "http://nces.ed.gov/statprog/instruct.asp",
+                    "format": "Restricted Use CD-ROM",
+                    "mediaType": "text/html",
+                    "title": "The Effectiveness of the Alabama Math, Science, and Technology Initiative (AMSTI)"
                 }
             ],
+            "identifier": "c420b1a5-dff9-42f3-aacc-95b2e2a23fbf",
+            "issued": "2012-11-26",
             "keyword": [
                 "34621008-400b-4c5c-b37f-2af6fec112e8",
                 "alabama",
@@ -46906,34 +46882,20 @@
                 "student-achievement",
                 "technology"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:51:17.927330",
             "programCode": [
                 "018:108"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Shortage Areas, 2015-16",
-            "description": "Teacher Shortage Areas, 2015-16 (TSA 2015-16), is part of the Teacher Shortage Areas (TSA) program; program data is available since 1990-91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2015-16 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2015-16 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of Schools of Education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state's and outlying jurisdiction's pre-kindergarten through grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
-            "modified": "2023-07-10T13:49:52.492387",
-            "accessLevel": "public",
-            "identifier": "8e18288a-5240-412f-8a7c-90ba23ac533d",
-            "dataQuality": true,
-            "issued": "2015-05-01",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2015/2016",
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
@@ -46948,30 +46910,46 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "http://",
+            "temporal": "2006/2010",
+            "title": "Evaluation of the Effectiveness of the Alabama Mathematics, Science, and Technology Initiative"
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
+            "description": "Teacher Shortage Areas, 2015-16 (TSA 2015-16), is part of the Teacher Shortage Areas (TSA) program; program data is available since 1990-91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2015-16 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2015-16 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of Schools of Education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state's and outlying jurisdiction's pre-kindergarten through grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "Microsoft Word Document",
-                    "title": "tsa.doc",
                     "description": "Teacher Shortage Areas data from 1990-91 through 2015-16 in a Microsoft Word Document",
-                    "downloadURL": "https://www2.ed.gov/about/offices/list/ope/pol/tsa.doc"
+                    "downloadURL": "https://www2.ed.gov/about/offices/list/ope/pol/tsa.doc",
+                    "format": "Microsoft Word Document",
+                    "mediaType": "application/msword",
+                    "title": "tsa.doc"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "PDF",
-                    "title": "tsa.pdf",
                     "description": "Teacher Shortage Areas data from 1990-91 through 2015-16 in a Portable Document Format (PDF)",
-                    "downloadURL": "https://www2.ed.gov/about/offices/list/ope/pol/tsa.pdf"
+                    "downloadURL": "https://www2.ed.gov/about/offices/list/ope/pol/tsa.pdf",
+                    "format": "PDF",
+                    "mediaType": "application/pdf",
+                    "title": "tsa.pdf"
                 }
             ],
+            "identifier": "8e18288a-5240-412f-8a7c-90ba23ac533d",
+            "issued": "2015-05-01",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "elementary-and-secondary-education",
@@ -46979,27 +46957,14 @@
                 "grants",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:49:52.492387",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Shortage Areas 2016-17",
-            "description": "Teacher Shortage Areas 2016-17 (TSA 2016-17) is part of the Teacher Shortage Areas (TSA) program; program data are available since 1990?91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2016-17 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2016-17 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of schools of education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state?s and outlying jurisdiction?s pre-kindergarten through Grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
-            "modified": "2023-07-10T13:49:09.414788",
-            "accessLevel": "public",
-            "identifier": "efbefcb1-99fc-4d0e-bed1-38ea87d63c9f",
-            "issued": "2017-12-31",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-10-01_060499.pdf",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -47020,24 +46985,37 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2015/2016",
+            "title": "Teacher Shortage Areas, 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "description": "Teacher Shortage Areas 2016-17 (TSA 2016-17) is part of the Teacher Shortage Areas (TSA) program; program data are available since 1990?91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2016-17 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2016-17 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of schools of education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state?s and outlying jurisdiction?s pre-kindergarten through Grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "Excel, PDF",
-                    "title": "Teacher Shortage Areas 2016-2017",
-                    "description": "Teacher Shortage Areas Data Collection System",
                     "describedBy": "https://datainventory.ed.gov/Search?txtMenuSearchTerm=&txtSearchTerm=&searchTerm=Teacher%20Shortage%20Areas%20TSA&advanced_search=&rdSearchType=Exact&seriesID=230&studyID=19832&studyType=study&seriesVar=&seriesVarTerm=&seriesVarType=Exact&studyVar=&studyVarTerm=&studyVarType=Exact&currentSearch=",
                     "describedByType": "text/html",
-                    "downloadURL": "https://tsa.ed.gov/#/reports"
+                    "description": "Teacher Shortage Areas Data Collection System",
+                    "downloadURL": "https://tsa.ed.gov/#/reports",
+                    "format": "Excel, PDF",
+                    "mediaType": "text/html",
+                    "title": "Teacher Shortage Areas 2016-2017"
                 }
             ],
+            "identifier": "efbefcb1-99fc-4d0e-bed1-38ea87d63c9f",
+            "issued": "2017-12-31",
             "keyword": [
                 "284c495f-ff53-476d-adbf-2e0b7d1d31f0",
                 "elementary-and-secondary-education",
@@ -47045,27 +47023,14 @@
                 "grants",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:49:09.414788",
             "programCode": [
                 "018:102"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Shortage Areas 2017-18",
-            "description": "Teacher Shortage Areas 2017-18 (TSA 2017-18) is part of the Teacher Shortage Areas (TSA) program; program data are available since 1990?91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2017-18 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2017-18 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of schools of education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state?s and outlying jurisdiction?s pre-kindergarten through Grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
-            "modified": "2023-07-10T13:48:25.985170",
-            "accessLevel": "public",
-            "identifier": "f8736bd6-206d-46ff-9f9b-49fa736be77a",
-            "issued": "2017-12-31",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-10-01_060499.pdf",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -47086,24 +47051,37 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-10-01_060499.pdf",
+            "title": "Teacher Shortage Areas 2016-17"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "description": "Teacher Shortage Areas 2017-18 (TSA 2017-18) is part of the Teacher Shortage Areas (TSA) program; program data are available since 1990?91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2017-18 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2017-18 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of schools of education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state?s and outlying jurisdiction?s pre-kindergarten through Grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "Excel, PDF",
-                    "title": "Teacher Shortage Areas 2017-18",
-                    "description": "Teacher Shortage Areas Data Collection System",
                     "describedBy": "https://datainventory.ed.gov/Search?txtMenuSearchTerm=&txtSearchTerm=&searchTerm=Teacher%20Shortage%20Areas%20TSA&advanced_search=&rdSearchType=Exact&seriesID=230&studyID=19833&studyType=study&seriesVar=&seriesVarTerm=&seriesVarType=Exact&studyVar=&studyVarTerm=&studyVarType=Exact&currentSearch=",
                     "describedByType": "text/html",
-                    "downloadURL": "https://tsa.ed.gov/#/reports"
+                    "description": "Teacher Shortage Areas Data Collection System",
+                    "downloadURL": "https://tsa.ed.gov/#/reports",
+                    "format": "Excel, PDF",
+                    "mediaType": "text/html",
+                    "title": "Teacher Shortage Areas 2017-18"
                 }
             ],
+            "identifier": "f8736bd6-206d-46ff-9f9b-49fa736be77a",
+            "issued": "2017-12-31",
             "keyword": [
                 "284c495f-ff53-476d-adbf-2e0b7d1d31f0",
                 "elementary-and-secondary-education",
@@ -47111,27 +47089,14 @@
                 "grants",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:48:25.985170",
             "programCode": [
                 "018:102"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Shortage Areas 2018-19",
-            "description": "Teacher Shortage Areas 2018-19 (TSA 2018-19) is part of the Teacher Shortage Areas (TSA) program; program data are available since 1990?91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2018-19 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2018-19 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of schools of education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state?s and outlying jurisdiction?s pre-kindergarten through Grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
-            "modified": "2023-07-10T13:47:42.713723",
-            "accessLevel": "public",
-            "identifier": "5ac18f1a-5c74-4518-b79f-e989d1a8aac5",
-            "issued": "2019-08-08",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-10-01_060499.pdf",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -47152,24 +47117,37 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-10-01_060499.pdf",
+            "title": "Teacher Shortage Areas 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "description": "Teacher Shortage Areas 2018-19 (TSA 2018-19) is part of the Teacher Shortage Areas (TSA) program; program data are available since 1990?91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2018-19 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2018-19 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of schools of education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state?s and outlying jurisdiction?s pre-kindergarten through Grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "Excel, PDF",
-                    "title": "Teacher Shortage Areas 2018-19",
-                    "description": "Teacher Shortage Areas Data Collection System",
                     "describedBy": "https://datainventory.ed.gov/Search?txtMenuSearchTerm=&txtSearchTerm=&searchTerm=Teacher%20Shortage%20Areas%20TSA&advanced_search=&rdSearchType=Exact&seriesID=230&studyID=19834&studyType=study&seriesVar=&seriesVarTerm=&seriesVarType=Exact&studyVar=&studyVarTerm=&studyVarType=Exact&currentSearch=",
                     "describedByType": "text/html",
-                    "downloadURL": "https://tsa.ed.gov/#/reports"
+                    "description": "Teacher Shortage Areas Data Collection System",
+                    "downloadURL": "https://tsa.ed.gov/#/reports",
+                    "format": "Excel, PDF",
+                    "mediaType": "text/html",
+                    "title": "Teacher Shortage Areas 2018-19"
                 }
             ],
+            "identifier": "5ac18f1a-5c74-4518-b79f-e989d1a8aac5",
+            "issued": "2019-08-08",
             "keyword": [
                 "284c495f-ff53-476d-adbf-2e0b7d1d31f0",
                 "elementary-and-secondary-education",
@@ -47177,27 +47155,14 @@
                 "grants",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:47:42.713723",
             "programCode": [
                 "018:102"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Shortage Areas 2019-20",
-            "description": "Teacher Shortage Areas 2019-20 (TSA 2019-20) is part of the Teacher Shortage Areas (TSA) program; program data are available since 1990?91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2019-20 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2019-20 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of schools of education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state?s and outlying jurisdiction?s pre-kindergarten through Grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
-            "modified": "2023-07-10T13:46:39.010782",
-            "accessLevel": "public",
-            "identifier": "a1e76210-0968-46e3-929c-d548fcaadce0",
-            "issued": "2019-10-12",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-10-01_060499.pdf",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -47218,24 +47183,37 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-10-01_060499.pdf",
+            "title": "Teacher Shortage Areas 2018-19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "description": "Teacher Shortage Areas 2019-20 (TSA 2019-20) is part of the Teacher Shortage Areas (TSA) program; program data are available since 1990?91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2019-20 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2019-20 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of schools of education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state?s and outlying jurisdiction?s pre-kindergarten through Grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "Excel, PDF",
-                    "title": "Teacher Shortage Areas 2019-20",
-                    "description": "Teacher Shortage Areas Data Collection System",
                     "describedBy": "https://datainventory.ed.gov/Search?txtMenuSearchTerm=&txtSearchTerm=&searchTerm=Teacher%20Shortage%20Areas%20TSA&advanced_search=&rdSearchType=Exact&seriesID=230&studyID=19835&studyType=study&seriesVar=&seriesVarTerm=&seriesVarType=Exact&studyVar=&studyVarTerm=&studyVarType=Exact&currentSearch=",
                     "describedByType": "text/html",
-                    "downloadURL": "https://tsa.ed.gov/#/reports"
+                    "description": "Teacher Shortage Areas Data Collection System",
+                    "downloadURL": "https://tsa.ed.gov/#/reports",
+                    "format": "Excel, PDF",
+                    "mediaType": "text/html",
+                    "title": "Teacher Shortage Areas 2019-20"
                 }
             ],
+            "identifier": "a1e76210-0968-46e3-929c-d548fcaadce0",
+            "issued": "2019-10-12",
             "keyword": [
                 "284c495f-ff53-476d-adbf-2e0b7d1d31f0",
                 "elementary-and-secondary-education",
@@ -47243,27 +47221,14 @@
                 "grants",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:46:39.010782",
             "programCode": [
                 "018:102"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Shortage Areas 2021-22",
-            "description": "Teacher Shortage Areas 2021-22 (TSA 2021-22) is part of the Teacher Shortage Areas (TSA) program; program data are available since 1990?91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2021-22 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2021-22 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of schools of education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state?s and outlying jurisdiction?s pre-kindergarten through Grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
-            "modified": "2023-07-10T13:45:01.280718",
-            "accessLevel": "public",
-            "identifier": "3ce9f72c-a96b-4f48-9327-fe02d0927e79",
-            "issued": "2021-08-10",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-10-01_060499.pdf",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -47284,24 +47249,37 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-10-01_060499.pdf",
+            "title": "Teacher Shortage Areas 2019-20"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Freddie Cross",
                 "hasEmail": "mailto:freddie.cross@ed.gov"
             },
+            "description": "Teacher Shortage Areas 2021-22 (TSA 2021-22) is part of the Teacher Shortage Areas (TSA) program; program data are available since 1990?91 at <https://www2.ed.gov/about/offices/list/ope/pol/tsa.html>. TSA 2021-22 (https://www2.ed.gov/about/offices/list/ope/pol/tsa.html) is a cross-sectional study that collects information about teaching needs in the 50 United States and the outlying jurisdictions. TSA 2021-22 provides a reference document to notify the nation where states and schools are looking to potentially hire academic administrators, licensed teachers, and other educators and school faculty in specific disciplines/subject areas, grade levels, and/or geographic regions; and where recent graduates of schools of education and trained, experienced teaching professionals aiming to serve school districts with shortages can find (prospective) positions and fill the current voids in each state?s and outlying jurisdiction?s pre-kindergarten through Grade 12 classrooms, in areas that match their certification credentials; as well as to inform Federal financial aid recipients on reducing, deferring, or cancelling/nullifying/discharging student loan payments and meeting other specified (e.g., teaching) obligations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "Excel, PDF",
-                    "title": "Teacher Shortage Areas 2021-22",
-                    "description": "Teacher Shortage Areas Data Collection System",
                     "describedBy": "https://datainventory.ed.gov/Search?txtMenuSearchTerm=&txtSearchTerm=&searchTerm=Teacher%20Shortage%20Areas%20TSA&advanced_search=&rdSearchType=Exact&seriesID=230&studyID=19837&studyType=study&seriesVar=&seriesVarTerm=&seriesVarType=Exact&studyVar=&studyVarTerm=&studyVarType=Exact&currentSearch=",
                     "describedByType": "text/html",
-                    "downloadURL": "https://tsa.ed.gov/#/reports"
+                    "description": "Teacher Shortage Areas Data Collection System",
+                    "downloadURL": "https://tsa.ed.gov/#/reports",
+                    "format": "Excel, PDF",
+                    "mediaType": "text/html",
+                    "title": "Teacher Shortage Areas 2021-22"
                 }
             ],
+            "identifier": "3ce9f72c-a96b-4f48-9327-fe02d0927e79",
+            "issued": "2021-08-10",
             "keyword": [
                 "284c495f-ff53-476d-adbf-2e0b7d1d31f0",
                 "elementary-and-secondary-education",
@@ -47309,34 +47287,20 @@
                 "grants",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:45:01.280718",
             "programCode": [
                 "018:102"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teaching and Learning International Survey, 2013",
-            "description": "The Teaching and Learning International Survey, 2013 (TALIS:13), is a study that is part of the Teaching and Learning International Survey (TALIS) program. TALIS:13 (https://nces.ed.gov/surveys/talis/) is a cross-sectional survey that is designed to collect information about the teaching workforce, teaching as a profession, and the learning environments of schools. The study will be conducted through questionnaires for teachers and school administrators. Teachers and school administrators in lower secondary schools (Grades 7, 8, and 9) were sampled. Key statistics produced from TALIS:13 include information on teacher and principal background and characteristics, teacher and principal professional development, school leadership and management, teacher appraisal and feedback, teachers' instructional beliefs and pedagogical practices, school climate and ethos, student characteristics as perceived by the teacher, and teacher efficacy and job satisfaction.",
-            "modified": "2023-07-10T13:43:37.574383",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "73aa14a0-2af1-4b97-b0d5-abddca17c477",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2012/2013",
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
@@ -47351,53 +47315,65 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-10-01_060499.pdf",
+            "title": "Teacher Shortage Areas 2021-22"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mary Coleman",
                 "hasEmail": "mailto:mary.coleman@ed.gov"
             },
+            "description": "The Teaching and Learning International Survey, 2013 (TALIS:13), is a study that is part of the Teaching and Learning International Survey (TALIS) program. TALIS:13 (https://nces.ed.gov/surveys/talis/) is a cross-sectional survey that is designed to collect information about the teaching workforce, teaching as a profession, and the learning environments of schools. The study will be conducted through questionnaires for teachers and school administrators. Teachers and school administrators in lower secondary schools (Grades 7, 8, and 9) were sampled. Key statistics produced from TALIS:13 include information on teacher and principal background and characteristics, teacher and principal professional development, school leadership and management, teacher appraisal and feedback, teachers' instructional beliefs and pedagogical practices, school climate and ethos, student characteristics as perceived by the teacher, and teacher efficacy and job satisfaction.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "2016063_CODEBOOKS.ZIP",
-                    "description": "Teaching and Learning International Survey (TALIS) 2013 U.S. public-use data files, raw data",
                     "describedBy": "https://nces.ed.gov/pubs2016/2016063_readme.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/pubs2016/data/2016063_CODEBOOKS.ZIP"
+                    "description": "Teaching and Learning International Survey (TALIS) 2013 U.S. public-use data files, raw data",
+                    "downloadURL": "https://nces.ed.gov/pubs2016/data/2016063_CODEBOOKS.ZIP",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "2016063_CODEBOOKS.ZIP"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "2016063_SPSS.ZIP",
-                    "description": "Teaching and Learning International Survey (TALIS) 2013 U.S. public-use data files, for SPSS",
                     "describedBy": "https://nces.ed.gov/pubs2016/2016063_readme.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/pubs2016/data/2016063_SPSS.ZIP"
+                    "description": "Teaching and Learning International Survey (TALIS) 2013 U.S. public-use data files, for SPSS",
+                    "downloadURL": "https://nces.ed.gov/pubs2016/data/2016063_SPSS.ZIP",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "2016063_SPSS.ZIP"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "2016063_SAS.ZIP",
-                    "description": "Teaching and Learning International Survey (TALIS) 2013 U.S. public-use data files, for SAS",
                     "describedBy": "https://nces.ed.gov/pubs2016/2016063_readme.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/pubs2016/data/2016063_SAS.ZIP"
+                    "description": "Teaching and Learning International Survey (TALIS) 2013 U.S. public-use data files, for SAS",
+                    "downloadURL": "https://nces.ed.gov/pubs2016/data/2016063_SAS.ZIP",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "2016063_SAS.ZIP"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Teaching and Learning International Survey (TALIS) 2013 U.S. restricted-use data files and documentation",
-                    "description": "Restricted-use data files for the 2013 Teaching and Learning International Survey (TALIS)",
                     "describedBy": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2015010",
                     "describedByType": "application/pdf",
+                    "description": "Restricted-use data files for the 2013 Teaching and Learning International Survey (TALIS)",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2016064",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Teaching and Learning International Survey (TALIS) 2013 U.S. restricted-use data files and documentation"
                 }
             ],
+            "identifier": "73aa14a0-2af1-4b97-b0d5-abddca17c477",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "instructional-beliefs",
@@ -47416,29 +47392,14 @@
                 "teaching",
                 "teaching-workforce"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:43:37.574383",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Trends in International Mathematics and Science Study, 2003",
-            "description": "The Trends in International Mathematics and Science Study, 2003 (TIMSS 2003), is part of the Trends in International Mathematics and Science Study (TIMSS) program. TIMSS 2003 (https://nces.ed.gov/timss/) is a cross-sectional study that provides international comparative information of the mathematics and science literacy of fourth- and eighth-grade students and examines factors that may be associated with the acquisition of math and science literacy in students. The study was conducted using direct assessments of students and questionnaires for students, teachers, and school administrators. Fourth- and eighth-graders in the 2002-03 school year were sampled. The weighted student response rate at grade four was 95 percent, and the weighted student response rate at grade eight was 94 percent. Key statistics produced from TIMSS 2003 are mathematics and science achievement scores of U.S. fourth- and eighth- grade students compared to that of students in other countries.",
-            "modified": "2023-07-10T13:42:25.375747",
-            "accessLevel": "public",
-            "identifier": "b1ac8970-fb41-4060-9ef9-96bfec124a8b",
-            "dataQuality": true,
-            "issued": "2006-10-02",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2002/2003",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -47459,28 +47420,44 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2012/2013",
+            "title": "Teaching and Learning International Survey, 2013"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lydia Malley",
                 "hasEmail": "mailto:lydia.malley@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Trends in International Mathematics and Science Study, 2003 (TIMSS 2003), is part of the Trends in International Mathematics and Science Study (TIMSS) program. TIMSS 2003 (https://nces.ed.gov/timss/) is a cross-sectional study that provides international comparative information of the mathematics and science literacy of fourth- and eighth-grade students and examines factors that may be associated with the acquisition of math and science literacy in students. The study was conducted using direct assessments of students and questionnaires for students, teachers, and school administrators. Fourth- and eighth-graders in the 2002-03 school year were sampled. The weighted student response rate at grade four was 95 percent, and the weighted student response rate at grade eight was 94 percent. Key statistics produced from TIMSS 2003 are mathematics and science achievement scores of U.S. fourth- and eighth- grade students compared to that of students in other countries.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Trends in International Mathematics and Science Study (TIMSS) 2003 U.S. datafile and User's Guide",
                     "description": "Trends in International Mathematics and Science Study, 2003 datafile and User's Guide",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2006058",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Trends in International Mathematics and Science Study (TIMSS) 2003 U.S. datafile and User's Guide"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "International Data Explorer",
                     "description": "Trends in International Mathematics and Science Study, 2003 data explorer",
                     "downloadURL": "https://nces.ed.gov/timss/idetimss/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "International Data Explorer"
                 }
             ],
+            "identifier": "b1ac8970-fb41-4060-9ef9-96bfec124a8b",
+            "issued": "2006-10-02",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "educational-achievement",
@@ -47489,30 +47466,14 @@
                 "mathematics",
                 "science"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:42:25.375747",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Trends in International Mathematics and Science Study, 2007",
-            "description": "The Trends in International Mathematics and Science Study, 2007 (TIMSS 2007), is a study that is part of the Trends in International Mathematics and Science Study (TIMSS) program. TIMSS 2007 (https://nces.ed.gov/timss/) is a cross-sectional study that provides international comparative information of the mathematics and science literacy of fourth- and eighth-grade students and examines factors that may be associated with the acquisition of math and science literacy in students. The study was conducted using direct assessments of students and questionnaires for students, teachers, and school administrators. Fourth- and eighth-graders in the 2006-07 school year were sampled. The final weighted student response rate at grade four was 95 percent, and the final weighted student response rate at grade eight was 93 percent. Key statistics produced from TIMSS 2003 are mathematics and science achievement scores of U.S. fourth- and eighth- grade students compared to that of students in other countries.",
-            "modified": "2023-07-10T13:40:23.477537",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "f6c6b012-aa7c-4e85-b374-52cf8650604b",
-            "dataQuality": true,
-            "issued": "2009-11-06",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2006/2007",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -47533,35 +47494,50 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2002/2003",
+            "title": "Trends in International Mathematics and Science Study, 2003"
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
                 "fn": "Lydia Malley",
                 "hasEmail": "mailto:lydia.malley@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Trends in International Mathematics and Science Study, 2007 (TIMSS 2007), is a study that is part of the Trends in International Mathematics and Science Study (TIMSS) program. TIMSS 2007 (https://nces.ed.gov/timss/) is a cross-sectional study that provides international comparative information of the mathematics and science literacy of fourth- and eighth-grade students and examines factors that may be associated with the acquisition of math and science literacy in students. The study was conducted using direct assessments of students and questionnaires for students, teachers, and school administrators. Fourth- and eighth-graders in the 2006-07 school year were sampled. The final weighted student response rate at grade four was 95 percent, and the final weighted student response rate at grade eight was 93 percent. Key statistics produced from TIMSS 2003 are mathematics and science achievement scores of U.S. fourth- and eighth- grade students compared to that of students in other countries.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Trends in International Mathematics and Science Study (TIMSS) 2007 U.S. public-use datafile",
                     "description": "Trends in International Mathematics and Science Study, 2007 public-use data",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2010024",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Trends in International Mathematics and Science Study (TIMSS) 2007 U.S. public-use datafile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Trends in International Mathematics and Science Study (TIMSS) 2007 U.S. restricted-use datafile",
                     "description": "Trends in International Mathematics and Science Study, 2007 restricted-use data",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2010025",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Trends in International Mathematics and Science Study (TIMSS) 2007 U.S. restricted-use datafile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "International Data Explorer",
                     "description": "Trends in International Mathematics and Science Study, 2007 data explorer",
                     "downloadURL": "https://nces.ed.gov/timss/idetimss/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "International Data Explorer"
                 }
             ],
+            "identifier": "f6c6b012-aa7c-4e85-b374-52cf8650604b",
+            "issued": "2009-11-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "educational-achievement",
@@ -47570,30 +47546,14 @@
                 "mathematics",
                 "science"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:40:23.477537",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Trends in International Mathematics and Science Study, 2011",
-            "description": "The Trends in International Mathematics and Science Study, 2011 (TIMSS 2011), is a study that is part of the Trends in International Mathematics and Science Study (TIMSS) program. TIMSS 2011 (https://nces.ed.gov/timss/) is a cross-sectional study that provides international comparative information of the mathematics and science literacy of fourth- and eighth-grade students and examines factors that may be associated with the acquisition of math and science literacy in students. The study was conducted using direct assessments of students and questionnaires for students, teachers, and school administrators. Fourth- and eighth-graders in the 2010-11 school year were sampled. The study's response rate was 94 percent. Key statistics produced from TIMSS 2003 are mathematics and science achievement scores of U.S. fourth- and eighth- grade students compared to that of students in other countries.",
-            "modified": "2023-07-10T13:39:38.898792",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "6f3d56a8-8fa5-452e-8d27-858f787b5303",
-            "dataQuality": true,
-            "issued": "2013-12-31",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2010/2011",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -47614,41 +47574,57 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2006/2007",
+            "title": "Trends in International Mathematics and Science Study, 2007"
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
                 "fn": "Lydia Malley",
                 "hasEmail": "mailto:lydia.malley@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Trends in International Mathematics and Science Study, 2011 (TIMSS 2011), is a study that is part of the Trends in International Mathematics and Science Study (TIMSS) program. TIMSS 2011 (https://nces.ed.gov/timss/) is a cross-sectional study that provides international comparative information of the mathematics and science literacy of fourth- and eighth-grade students and examines factors that may be associated with the acquisition of math and science literacy in students. The study was conducted using direct assessments of students and questionnaires for students, teachers, and school administrators. Fourth- and eighth-graders in the 2010-11 school year were sampled. The study's response rate was 94 percent. Key statistics produced from TIMSS 2003 are mathematics and science achievement scores of U.S. fourth- and eighth- grade students compared to that of students in other countries.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped multiple DAT",
-                    "title": "T2011grade4_RAWdata.zip",
-                    "description": "Trends in International Mathematics and Science Study, 2011 Grade 4 public-use data available through TIMMS data explorer",
                     "describedBy": "https://nces.ed.gov/timss/zip/T2011grade4_codebooksHTML.zip",
                     "describedByType": "application/zip",
-                    "downloadURL": "https://nces.ed.gov/timss/zip/T2011grade4_RAWdata.zip"
+                    "description": "Trends in International Mathematics and Science Study, 2011 Grade 4 public-use data available through TIMMS data explorer",
+                    "downloadURL": "https://nces.ed.gov/timss/zip/T2011grade4_RAWdata.zip",
+                    "format": "Zipped multiple DAT",
+                    "mediaType": "application/zip",
+                    "title": "T2011grade4_RAWdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped multiple DAT",
-                    "title": "T2011grade8_RAWdata.zip",
-                    "description": "Trends in International Mathematics and Science Study, 2011 Grade 8 public-use data available through TIMMS data explorer",
                     "describedBy": "https://nces.ed.gov/timss/zip/T2011grade8_codebooksHTML.zip",
                     "describedByType": "application/zip",
-                    "downloadURL": "https://nces.ed.gov/timss/zip/T2011grade8_RAWdata.zip"
+                    "description": "Trends in International Mathematics and Science Study, 2011 Grade 8 public-use data available through TIMMS data explorer",
+                    "downloadURL": "https://nces.ed.gov/timss/zip/T2011grade8_RAWdata.zip",
+                    "format": "Zipped multiple DAT",
+                    "mediaType": "application/zip",
+                    "title": "T2011grade8_RAWdata.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Trends in International Mathematics and Science Study (TIMSS) 2011 U.S. restricted-use datafile",
                     "description": "Trends in International Mathematics and Science Study, 2011 restricted-use data",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2013041",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Trends in International Mathematics and Science Study (TIMSS) 2011 U.S. restricted-use datafile"
                 }
             ],
+            "identifier": "6f3d56a8-8fa5-452e-8d27-858f787b5303",
+            "issued": "2013-12-31",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "educational-achievement",
@@ -47657,33 +47633,20 @@
                 "mathematics",
                 "science"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:39:38.898792",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Investing in Innovation 2011 Applications",
-            "description": "Thank you for your interest in the Investing in Innovation (i3) Program! You can use the tools below to look at general information about the applications, and you can also find specific applications that you would like to explore in more detail. The data is sourced from supplemental forms as reported by applicants. The data from these forms may not be a full or accurate representation of the information provided in the formal application.",
-            "modified": "2023-07-10T13:37:30.925447",
-            "accessLevel": "public",
-            "identifier": "e0172fac-d7b6-48b3-8761-cac9034118fb",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/P1Y",
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
@@ -47698,44 +47661,46 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2010/2011",
+            "title": "Trends in International Mathematics and Science Study, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Thank you for your interest in the Investing in Innovation (i3) Program! You can use the tools below to look at general information about the applications, and you can also find specific applications that you would like to explore in more detail. The data is sourced from supplemental forms as reported by applicants. The data from these forms may not be a full or accurate representation of the information provided in the formal application.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/3c33d2e9-7476-4d89-98e3-452047ea2fa9/resource/5b5a20af-dbf2-4935-947a-d484384b8282/download/userssharedsdfinvestingininnovation2011applications.csv",
                     "format": "CSV",
-                    "title": "userssharedsdfinvestingininnovation2011applications.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/3c33d2e9-7476-4d89-98e3-452047ea2fa9/resource/5b5a20af-dbf2-4935-947a-d484384b8282/download/userssharedsdfinvestingininnovation2011applications.csv"
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfinvestingininnovation2011applications.csv"
                 }
             ],
+            "identifier": "e0172fac-d7b6-48b3-8761-cac9034118fb",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "application",
                 "innovation",
                 "interactive"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-10T13:37:30.925447",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Investing in Innovation 2010 Applications",
-            "description": "Thank you for your interest in the Investing in Innovation (i3) Program! You can use the tools below to look at general information about the applications, and you can also find specific applications that you would like to explore in more detail. The data is sourced from supplemental forms as reported by applicants. The data from these forms may not be a full or accurate representation of the information provided in the formal application.",
-            "modified": "2023-07-07T19:21:02.669612",
-            "accessLevel": "public",
-            "identifier": "2e92be11-03fc-474f-a62d-14ef3724f620",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/P1Y",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Innovation and Improvement (OII)",
@@ -47756,20 +47721,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2011/P1Y",
+            "title": "Investing in Innovation 2011 Applications"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Thank you for your interest in the Investing in Innovation (i3) Program! You can use the tools below to look at general information about the applications, and you can also find specific applications that you would like to explore in more detail. The data is sourced from supplemental forms as reported by applicants. The data from these forms may not be a full or accurate representation of the information provided in the formal application.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/787a2347-1e8a-48a8-8c95-6f99e6b495f3/resource/ddb4e855-bf97-4561-94a7-d6dee6a02eaa/download/userssharedsdfinvestingininnovation2010applications.csv",
                     "format": "CSV",
-                    "title": "userssharedsdfinvestingininnovation2010applications.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/787a2347-1e8a-48a8-8c95-6f99e6b495f3/resource/ddb4e855-bf97-4561-94a7-d6dee6a02eaa/download/userssharedsdfinvestingininnovation2010applications.csv"
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfinvestingininnovation2010applications.csv"
                 }
             ],
+            "identifier": "2e92be11-03fc-474f-a62d-14ef3724f620",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "application",
@@ -47777,24 +47755,11 @@
                 "interactive",
                 "investing"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:21:02.669612",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teaching American History 2010 Grantees",
-            "description": "The program is designed to raise student achievement by improving teachers' knowledge and understanding of and appreciation for traditional U.S. history. Grant awards will assist LEAs, in partnership with entities that have content expertise, to develop, document, evaluate, and disseminate innovative and cohesive models of professional development. By helping teachers to develop a deeper understanding and appreciation of U.S. history as a separate subject matter within the core curriculum, these programs will improve instruction and raise student achievement.",
-            "modified": "2023-07-07T19:19:53.800143",
-            "accessLevel": "public",
-            "identifier": "c5830b28-ccfe-41a6-a694-ae005ce4f3f7",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/P1Y",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Innovation and Improvement (OII)",
@@ -47815,20 +47780,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2010/P1Y",
+            "title": "Investing in Innovation 2010 Applications"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The program is designed to raise student achievement by improving teachers' knowledge and understanding of and appreciation for traditional U.S. history. Grant awards will assist LEAs, in partnership with entities that have content expertise, to develop, document, evaluate, and disseminate innovative and cohesive models of professional development. By helping teachers to develop a deeper understanding and appreciation of U.S. history as a separate subject matter within the core curriculum, these programs will improve instruction and raise student achievement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/da765763-7b50-4dd2-9772-c92e0fed8e1a/resource/411d25bd-ac44-4d90-99a0-c65670628afd/download/userssharedsdfteachingamericanhistory2010grantees.csv",
                     "format": "CSV",
-                    "title": "userssharedsdfteachingamericanhistory2010grantees.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/da765763-7b50-4dd2-9772-c92e0fed8e1a/resource/411d25bd-ac44-4d90-99a0-c65670628afd/download/userssharedsdfteachingamericanhistory2010grantees.csv"
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfteachingamericanhistory2010grantees.csv"
                 }
             ],
+            "identifier": "c5830b28-ccfe-41a6-a694-ae005ce4f3f7",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "american",
@@ -47836,24 +47814,11 @@
                 "history",
                 "interactive"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:19:53.800143",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teaching American History 2010 Applicants",
-            "description": "The program is designed to raise student achievement by improving teachers' knowledge and understanding of and appreciation for traditional U.S. history. Grant awards will assist LEAs, in partnership with entities that have content expertise, to develop, document, evaluate, and disseminate innovative and cohesive models of professional development. By helping teachers to develop a deeper understanding and appreciation of U.S. history as a separate subject matter within the core curriculum, these programs will improve instruction and raise student achievement.",
-            "modified": "2023-07-07T19:19:17.783269",
-            "accessLevel": "public",
-            "identifier": "5df1ac10-3d99-44e6-8d54-47788f7871f3",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/P1Y",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Innovation and Improvement (OII)",
@@ -47874,20 +47839,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2010/P1Y",
+            "title": "Teaching American History 2010 Grantees"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "The program is designed to raise student achievement by improving teachers' knowledge and understanding of and appreciation for traditional U.S. history. Grant awards will assist LEAs, in partnership with entities that have content expertise, to develop, document, evaluate, and disseminate innovative and cohesive models of professional development. By helping teachers to develop a deeper understanding and appreciation of U.S. history as a separate subject matter within the core curriculum, these programs will improve instruction and raise student achievement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/9b8df339-a659-4f7a-b6f0-de8e17964f68/resource/583cf78f-2508-4d21-a55d-3e3cb1dfff16/download/userssharedsdfteachingamericanhistory2010applicants.csv",
                     "format": "CSV",
-                    "title": "userssharedsdfteachingamericanhistory2010applicants.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/9b8df339-a659-4f7a-b6f0-de8e17964f68/resource/583cf78f-2508-4d21-a55d-3e3cb1dfff16/download/userssharedsdfteachingamericanhistory2010applicants.csv"
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfteachingamericanhistory2010applicants.csv"
                 }
             ],
+            "identifier": "5df1ac10-3d99-44e6-8d54-47788f7871f3",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "american",
@@ -47896,24 +47874,11 @@
                 "interactive",
                 "teaching"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:19:17.783269",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Promise Neighborhoods 2011 Applications",
-            "description": "Thank you for your interest in the Promise Neighborhoods Program! You can use the tools below to look at general information about the applications, and you can also find specific applications that you would like to explore in more detail. The data is sourced from supplemental forms as reported by applicants. The data from these forms may not be a full or accurate representation of the information provided in the formal application.",
-            "modified": "2023-07-07T19:16:54.764481",
-            "accessLevel": "public",
-            "identifier": "187c6d1f-266a-4fd0-abd1-cf3912723a35",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/P1Y",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Innovation and Improvement (OII)",
@@ -47934,20 +47899,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2010/P1Y",
+            "title": "Teaching American History 2010 Applicants"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Thank you for your interest in the Promise Neighborhoods Program! You can use the tools below to look at general information about the applications, and you can also find specific applications that you would like to explore in more detail. The data is sourced from supplemental forms as reported by applicants. The data from these forms may not be a full or accurate representation of the information provided in the formal application.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/8bf56e54-1a05-4726-9c20-cfd22a20c48d/resource/474b78a0-37c2-4d79-877f-05025428ae57/download/userssharedsdfpromiseneighborhoods2011applications.csv",
                     "format": "CSV",
-                    "title": "userssharedsdfpromiseneighborhoods2011applications.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/8bf56e54-1a05-4726-9c20-cfd22a20c48d/resource/474b78a0-37c2-4d79-877f-05025428ae57/download/userssharedsdfpromiseneighborhoods2011applications.csv"
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfpromiseneighborhoods2011applications.csv"
                 }
             ],
+            "identifier": "187c6d1f-266a-4fd0-abd1-cf3912723a35",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "application",
@@ -47955,24 +47933,11 @@
                 "neighborhoods",
                 "promise"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:16:54.764481",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Promise Neighborhood 2011 Grantees",
-            "description": "Thank you for your interest in the Promise Neighborhoods Program! You can use the tools below to look at general information about the applications, and you can also find specific applications that you would like to explore in more detail. The data is sourced from supplemental forms as reported by applicants. The data from these forms may not be a full or accurate representation of the information provided in the formal application.",
-            "modified": "2023-07-07T19:15:51.970312",
-            "accessLevel": "public",
-            "identifier": "01859310-3184-4f35-a1a4-4af7a4f237ce",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/P1Y",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Innovation and Improvement (OII)",
@@ -47993,20 +47958,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2011/P1Y",
+            "title": "Promise Neighborhoods 2011 Applications"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Thank you for your interest in the Promise Neighborhoods Program! You can use the tools below to look at general information about the applications, and you can also find specific applications that you would like to explore in more detail. The data is sourced from supplemental forms as reported by applicants. The data from these forms may not be a full or accurate representation of the information provided in the formal application.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/63644379-d93f-449f-9b06-bb520ecf1fb6/resource/01dda076-56b9-4488-957b-7101061c27a9/download/userssharedsdfpromiseneighborhoods2011grantees.csv",
                     "format": "CSV",
-                    "title": "userssharedsdfpromiseneighborhoods2011grantees.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/63644379-d93f-449f-9b06-bb520ecf1fb6/resource/01dda076-56b9-4488-957b-7101061c27a9/download/userssharedsdfpromiseneighborhoods2011grantees.csv"
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfpromiseneighborhoods2011grantees.csv"
                 }
             ],
+            "identifier": "01859310-3184-4f35-a1a4-4af7a4f237ce",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "grantees",
@@ -48014,24 +47992,11 @@
                 "neighborhoods",
                 "promise"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:15:51.970312",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Promise Neighborhood 2010 Applications",
-            "description": "Thank you for your interest in the Promise Neighborhoods Program! You can use the tools below to look at general information about the applications. The data is sourced from applications submitted for the program. Inclusion of an application in the data that follows does not ensure that the application will be considered eligible for an award, or that the application will be funded by the Department of Education. The Absolute Priority assignments do not conclusively indicate that the applicants are eligible to apply under those absolute priorities according to the Department's criteria. Inclusion of an application in this summary information is not an endorsement of an organization, idea, program, or product, and the Department does not validate or guarantee the accuracy of this information. The data are provided in this summary solely for the convenience of the public.",
-            "modified": "2023-07-07T19:14:44.451785",
-            "accessLevel": "public",
-            "identifier": "5a302683-f962-4882-a7ba-8cf0d74df016",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/P1Y",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Innovation and Improvement (OII)",
@@ -48052,20 +48017,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2011/P1Y",
+            "title": "Promise Neighborhood 2011 Grantees"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:12"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Thank you for your interest in the Promise Neighborhoods Program! You can use the tools below to look at general information about the applications. The data is sourced from applications submitted for the program. Inclusion of an application in the data that follows does not ensure that the application will be considered eligible for an award, or that the application will be funded by the Department of Education. The Absolute Priority assignments do not conclusively indicate that the applicants are eligible to apply under those absolute priorities according to the Department's criteria. Inclusion of an application in this summary information is not an endorsement of an organization, idea, program, or product, and the Department does not validate or guarantee the accuracy of this information. The data are provided in this summary solely for the convenience of the public.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/98a7d3da-2320-4ca1-a50d-df9da9c5b30f/resource/c17a3203-f67f-4319-af15-4c050c774a31/download/userssharedsdfpromiseneighborhood2010applications.csv",
                     "format": "CSV",
-                    "title": "userssharedsdfpromiseneighborhood2010applications.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/98a7d3da-2320-4ca1-a50d-df9da9c5b30f/resource/c17a3203-f67f-4319-af15-4c050c774a31/download/userssharedsdfpromiseneighborhood2010applications.csv"
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfpromiseneighborhood2010applications.csv"
                 }
             ],
+            "identifier": "5a302683-f962-4882-a7ba-8cf0d74df016",
             "keyword": [
                 "85f4c211-0469-4302-a83f-e9c18a7579b7",
                 "application",
@@ -48073,26 +48051,17 @@
                 "neighborhood",
                 "promise"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:12"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:14:44.451785",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ED Enterprise Data Inventory (EDI)",
-            "description": "U.S. Department of Education online JSON catalog file.",
-            "modified": "2023-07-07T19:13:30.764263",
-            "accessLevel": "public",
-            "identifier": "aedc6417-501f-4fbb-bcc0-f9b34e91988a",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Chief Information Officer (OCIO)",
+                "name": "Office of Innovation and Improvement (OII)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Elementary and Secondary Education (OESE)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -48105,25 +48074,39 @@
                             }
                         }
                     }
+                }
+            },
+            "spatial": "United States",
+            "temporal": "2010/P1Y",
+            "title": "Promise Neighborhood 2010 Applications"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jill James",
                 "hasEmail": "mailto:jill.james@ed.gov"
             },
+            "dataQuality": true,
+            "description": "U.S. Department of Education online JSON catalog file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "JSON",
-                    "title": "data.json",
-                    "description": "U.S. Department of Education online JSON catalog file",
                     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
                     "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
                     "describedByType": "application/json",
-                    "downloadURL": "https://www2.ed.gov/data.json"
+                    "description": "U.S. Department of Education online JSON catalog file",
+                    "downloadURL": "https://www2.ed.gov/data.json",
+                    "format": "JSON",
+                    "mediaType": "application/json",
+                    "title": "data.json"
                 }
             ],
+            "identifier": "aedc6417-501f-4fbb-bcc0-f9b34e91988a",
             "keyword": [
                 "955289e9-892f-460a-84cb-c981c2566e8e",
                 "catalog",
@@ -48145,24 +48128,11 @@
                 "u-s-department-of-education",
                 "us-department-of-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:13:30.764263",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Digital Government Strategy Report",
-            "description": "On May 23, 2012, the President issued a Presidential Memorandum on \u201cBuilding a 21st Century Digital Government. It launched a comprehensive Digital Government Strategy (pdf/html5) aimed at delivering better digital services to the American people. The strategy builds on several initiatives, including Executive Order 13571, Streamlining Service Delivery and Improving Customer Service, and Executive Order 13576, Delivering an Efficient, Effective, and Accountable Government. The strategy lays out actions in a 12-month roadmap and has three main objectives: (1) Enable the American people and an increasingly mobile workforce to access high-quality digital government information and services anywhere, anytime, on any device. (2) Ensure that as the government adjusts to this new digital world, we seize the opportunity to procure and manage devices, applications, and data in smart, secure and affordable ways. (3) Unlock the power of government data to spur innovation across our Nation and improve the quality of services for the American people.",
-            "modified": "2023-07-07T19:12:49.150374",
-            "accessLevel": "public",
-            "identifier": "06761243-ec17-4ab4-894d-3154bfd36bd2",
-            "dataQuality": true,
-            "issued": "2016-04-29",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Chief Information Officer (OCIO)",
@@ -48179,38 +48149,51 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ED Enterprise Data Inventory (EDI)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steven Corey-Bey",
                 "hasEmail": "mailto:steven.corey-bey@ed.gov"
             },
+            "dataQuality": true,
+            "description": "On May 23, 2012, the President issued a Presidential Memorandum on \u201cBuilding a 21st Century Digital Government. It launched a comprehensive Digital Government Strategy (pdf/html5) aimed at delivering better digital services to the American people. The strategy builds on several initiatives, including Executive Order 13571, Streamlining Service Delivery and Improving Customer Service, and Executive Order 13576, Delivering an Efficient, Effective, and Accountable Government. The strategy lays out actions in a 12-month roadmap and has three main objectives: (1) Enable the American people and an increasingly mobile workforce to access high-quality digital government information and services anywhere, anytime, on any device. (2) Ensure that as the government adjusts to this new digital world, we seize the opportunity to procure and manage devices, applications, and data in smart, secure and affordable ways. (3) Unlock the power of government data to spur innovation across our Nation and improve the quality of services for the American people.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/json",
-                    "format": "JSON",
-                    "title": "digitalstrategy.json",
                     "description": "Digital Government Strategy Report in JSON format",
-                    "downloadURL": "https://www2.ed.gov/digitalstrategy.json"
+                    "downloadURL": "https://www2.ed.gov/digitalstrategy.json",
+                    "format": "JSON",
+                    "mediaType": "text/json",
+                    "title": "digitalstrategy.json"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/xml",
-                    "format": "XML",
-                    "title": "digitalstrategy.xml",
                     "description": "Digital Government Strategy Report in XML format",
-                    "downloadURL": "https://www2.ed.gov/digitalstrategy.xml"
+                    "downloadURL": "https://www2.ed.gov/digitalstrategy.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml",
+                    "title": "digitalstrategy.xml"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/json",
-                    "format": "JSON",
-                    "title": "costsavings.json",
                     "description": "Realized Cost Savings and Avoidance Decisions",
-                    "downloadURL": "https://www2.ed.gov/digitalstrategy/costsavings.json"
+                    "downloadURL": "https://www2.ed.gov/digitalstrategy/costsavings.json",
+                    "format": "JSON",
+                    "mediaType": "text/json",
+                    "title": "costsavings.json"
                 }
             ],
+            "identifier": "06761243-ec17-4ab4-894d-3154bfd36bd2",
+            "issued": "2016-04-29",
             "keyword": [
                 "955289e9-892f-460a-84cb-c981c2566e8e",
                 "digital-government",
@@ -48220,33 +48203,17 @@
                 "roadmap",
                 "streamlining-service-delivery"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:12:49.150374",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Teacher and Principal Survey, 2015-16",
-            "description": "The 2015-16 National Teacher and Principal Survey (NTPS) is a redesign of the Schools and Staffing Survey (SASS); SASS program data is available since 1987-88 at <https://nces.ed.gov/surveys/sass/dataproducts.asp>. NTPS <https://nces.ed.gov/surveys/ntps/> will replace SASS as one of the key sources of nationally representative data on a range of important education topics including out-of-field teaching, school decision making, professional development, teacher and principal evaluation, and career paths of educators and administrators. The repeated cross-sectional design of NTPS allows tracking of trends on these topics over time. The survey is conducted through a combination of online and paper questionnaires. The sample includes teachers, principals, and schools, and is nationally representative.",
-            "modified": "2023-07-07T19:11:20.313458",
-            "accessLevel": "public",
-            "identifier": "f27854bb-dd15-44e9-8b9f-f4ab27be81b5",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2015/2016",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                "name": "Office of the Chief Information Officer (OCIO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -48259,23 +48226,34 @@
                         }
                     }
                 }
-                }
             },
+            "spatial": "United States",
+            "title": "Digital Government Strategy Report"
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
+            "description": "The 2015-16 National Teacher and Principal Survey (NTPS) is a redesign of the Schools and Staffing Survey (SASS); SASS program data is available since 1987-88 at <https://nces.ed.gov/surveys/sass/dataproducts.asp>. NTPS <https://nces.ed.gov/surveys/ntps/> will replace SASS as one of the key sources of nationally representative data on a range of important education topics including out-of-field teaching, school decision making, professional development, teacher and principal evaluation, and career paths of educators and administrators. The repeated cross-sectional design of NTPS allows tracking of trends on these topics over time. The survey is conducted through a combination of online and paper questionnaires. The sample includes teachers, principals, and schools, and is nationally representative.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "National Teacher and Principal Survey, 2015\u00c3\u0192\u00c6\u2019\u00c3\u201a\u00c2\u00a2\u00c3\u0192\u00c2\u00a2\u00c3\u00a2\u00e2\u201a\u00ac\u00c5\u00a1\u00c3\u201a\u00c2\u00ac\u00c3\u0192\u00c2\u00a2\u00c3\u00a2\u00e2\u20ac\u0161\u00c2\u00ac\u00c3\u2026\u00e2\u20ac\u015316 Restricted-Use Data Files",
                     "description": "Restricted-use data files for the National Teacher and Principal Survey, 2015\u00c3\u0192\u00c6\u2019\u00c3\u201a\u00c2\u00a2\u00c3\u0192\u00c2\u00a2\u00c3\u00a2\u00e2\u201a\u00ac\u00c5\u00a1\u00c3\u201a\u00c2\u00ac\u00c3\u0192\u00c2\u00a2\u00c3\u00a2\u00e2\u20ac\u0161\u00c2\u00ac\u00c3\u2026\u00e2\u20ac\u015316",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "National Teacher and Principal Survey, 2015\u00c3\u0192\u00c6\u2019\u00c3\u201a\u00c2\u00a2\u00c3\u0192\u00c2\u00a2\u00c3\u00a2\u00e2\u201a\u00ac\u00c5\u00a1\u00c3\u201a\u00c2\u00ac\u00c3\u0192\u00c2\u00a2\u00c3\u00a2\u00e2\u20ac\u0161\u00c2\u00ac\u00c3\u2026\u00e2\u20ac\u015316 Restricted-Use Data Files"
                 }
             ],
+            "identifier": "f27854bb-dd15-44e9-8b9f-f4ab27be81b5",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "hiring",
@@ -48286,28 +48264,14 @@
                 "teacher-characteristics",
                 "teacher-training-opportunities"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:11:20.313458",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Follow-Up Survey, 1991-92",
-            "description": "The 1991-92 Teacher Follow-Up Survey (TFS 91-92) is a longitudinal follow-up to the 1990-91 Schools and Staffing Survey (SASS 90-91). TFS 91-92 (https://nces.ed.gov/surveys/sass/index.asp) is used to determine how many teachers remained at the same school, moved to another school, or left the profession in the year following the Schools and Staffing Survey (SASS) administration. TFS 91-92 was administered to a sample of teachers who completed the SASS in the previous year. Key statistics found from 1991-92 TFS are the percentage of teachers who remained at the same school, the percentage of teachers who moved to another school, or the percentage of teachers who left the profession in the year following the 1990-91 Schools and Staffing Survey (SASS) administration.",
-            "modified": "2023-07-07T19:10:22.649634",
-            "accessLevel": "public",
-            "identifier": "4c244dd7-7d2a-4eba-b911-128b95a42d44",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1991/1992",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -48328,39 +48292,52 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2015/2016",
+            "title": "National Teacher and Principal Survey, 2015-16"
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
                 "fn": "Amy Ho",
                 "hasEmail": "mailto:amy.ho@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 1991-92 Teacher Follow-Up Survey (TFS 91-92) is a longitudinal follow-up to the 1990-91 Schools and Staffing Survey (SASS 90-91). TFS 91-92 (https://nces.ed.gov/surveys/sass/index.asp) is used to determine how many teachers remained at the same school, moved to another school, or left the profession in the year following the Schools and Staffing Survey (SASS) administration. TFS 91-92 was administered to a sample of teachers who completed the SASS in the previous year. Key statistics found from 1991-92 TFS are the percentage of teachers who remained at the same school, the percentage of teachers who moved to another school, or the percentage of teachers who left the profession in the year following the 1990-91 Schools and Staffing Survey (SASS) administration.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Datalab for Schools and Staffing Survey",
                     "description": "The SASS data available in PowerStats are comprised of data collected from five SASS questionnaires: the School Questionnaire, Teacher Questionnaire, School Principal Questionnaire, School District Questionnaire, and Library Media Center Questionnaire",
                     "downloadURL": "https://nces.ed.gov/datalab/sass/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Datalab for Schools and Staffing Survey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "frmrtchr91_ascii.zip",
-                    "description": "1991-92 TFS Public-Use Data--Former Teacher",
                     "describedBy": "https://nces.ed.gov/surveys/sass/pdf/FormerTeacher/frmrtchr91_layout.pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/sass/data/zip/frmrtchr91_ascii.zip"
+                    "description": "1991-92 TFS Public-Use Data--Former Teacher",
+                    "downloadURL": "https://nces.ed.gov/surveys/sass/data/zip/frmrtchr91_ascii.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "frmrtchr91_ascii.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "crnttchr91_ascii.zip",
-                    "description": "1991-92 TFS Public-Use Data--Current Teacher",
                     "describedBy": "https://nces.ed.gov/surveys/sass/pdf/CurrentTeacher/crnttchr91_layout.pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/sass/data/zip/crnttchr91_ascii.zip"
+                    "description": "1991-92 TFS Public-Use Data--Current Teacher",
+                    "downloadURL": "https://nces.ed.gov/surveys/sass/data/zip/crnttchr91_ascii.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "crnttchr91_ascii.zip"
                 }
             ],
+            "identifier": "4c244dd7-7d2a-4eba-b911-128b95a42d44",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "leavers",
@@ -48369,32 +48346,14 @@
                 "teacher-attrition",
                 "teacher-retention"
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
-                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=94337"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teacher Follow-Up Survey, 2012-13",
-            "description": "The 2012-13 Teacher Follow-Up Survey (TFS 12/13) is a longitudinal follow-up to the 2011-12 Schools and Staffing Survey (SASS 11-12). TFS 12/13 (https://nces.ed.gov/surveys/sass/) determines how many teachers remained at the same school, moved to another school, or left the profession in the year following the Schools and Staffing Survey (SASS) administration. TFS 12/13 was administered to a sample of teachers who completed the SASS in the previous year. The majority of TFS 12/13 is a web-based survey, but it also has paper component. Key statistics produced from TFS 12/13 are how many teachers remained at the same school, moved to another school, or left the profession in the year following the Schools and Staffing Survey (SASS) administration.",
-            "modified": "2023-07-07T19:09:08.090486",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "66e99d96-d1d2-406b-b0aa-27894b934709",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2012/2013",
+            "modified": "2023-07-07T19:10:22.649634",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -48415,21 +48374,38 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=94337"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1991/1992",
+            "title": "Teacher Follow-Up Survey, 1991-92"
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
                 "fn": "Amy Ho",
                 "hasEmail": "mailto:amy.ho@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2012-13 Teacher Follow-Up Survey (TFS 12/13) is a longitudinal follow-up to the 2011-12 Schools and Staffing Survey (SASS 11-12). TFS 12/13 (https://nces.ed.gov/surveys/sass/) determines how many teachers remained at the same school, moved to another school, or left the profession in the year following the Schools and Staffing Survey (SASS) administration. TFS 12/13 was administered to a sample of teachers who completed the SASS in the previous year. The majority of TFS 12/13 is a web-based survey, but it also has paper component. Key statistics produced from TFS 12/13 are how many teachers remained at the same school, moved to another school, or left the profession in the year following the Schools and Staffing Survey (SASS) administration.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2011-12 Schools and Staffing Survey (SASS) Restricted-Use Data Files",
                     "description": "Restricted-use data file for the 2011-12 School and Staffing Survey",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014356",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2011-12 Schools and Staffing Survey (SASS) Restricted-Use Data Files"
                 }
             ],
+            "identifier": "66e99d96-d1d2-406b-b0aa-27894b934709",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "leavers",
@@ -48437,29 +48413,14 @@
                 "stayers",
                 "teacher-attrition"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:09:08.090486",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Principal Follow-Up Survey, 2012-13",
-            "description": "The 2012-13 Principal Follow-Up Survey (PFS 12/13) is a longitudinal follow-up to the 2011-12 Schools and Staffing Survey (SASS 11-12) study. PFS 12/13 (https://nces.ed.gov/surveys/sass/) determined how many principals remained at the same school, moved to another school, or left the profession in the year following the 2011-12 Schools and Staffing Survey (SASS 11-12) administration. PFS 12/13 was administered to a sample of principals who completed the SASS 11-12 principal questionnaire. Due to its brevity and lack of skip patterns, PFS 12/13 was primarily a mail-based data collection with telephone and email follow-up.",
-            "modified": "2023-07-07T19:07:50.825012",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "3817c203-680a-4216-a64b-1c6682055491",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2012/2013",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -48480,49 +48441,50 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2012/2013",
+            "title": "Teacher Follow-Up Survey, 2012-13"
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
                 "fn": "Amy Ho",
                 "hasEmail": "mailto:amy.ho@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2012-13 Principal Follow-Up Survey (PFS 12/13) is a longitudinal follow-up to the 2011-12 Schools and Staffing Survey (SASS 11-12) study. PFS 12/13 (https://nces.ed.gov/surveys/sass/) determined how many principals remained at the same school, moved to another school, or left the profession in the year following the 2011-12 Schools and Staffing Survey (SASS 11-12) administration. PFS 12/13 was administered to a sample of principals who completed the SASS 11-12 principal questionnaire. Due to its brevity and lack of skip patterns, PFS 12/13 was primarily a mail-based data collection with telephone and email follow-up.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2011-12 Schools and Staffing Survey (SASS) Restricted-Use Data Files",
                     "description": "Restricted-use data file for the 2011-12 School and Staffing Survey",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014356",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2011-12 Schools and Staffing Survey (SASS) Restricted-Use Data Files"
                 }
             ],
+            "identifier": "3817c203-680a-4216-a64b-1c6682055491",
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
+            "modified": "2023-07-07T19:07:50.825012",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "NCES-Barron's Admissions Competitiveness Index Data Files: 1972, 1982, 1992, 2004, 2008, 2014",
-            "description": "The NCES-Barron's Admissions Competitiveness Index Data Files: 1972, 1982, 1992, 2004, 2008, 2014 (NCES 2015-332) contain the Barron's college admissions competitiveness selectivity ratings for 1972, 1982, 1992, 2004, 2008, 2014 along with the NCES Higher Education Information System (HEGIS) FICE ID and Integrated Postsecondary Education Data System (IPEDS) UNITID codes and the Office of Postsecondary Education OPEID codes of each postsecondary institution included. Also included are the city and state of each institution included in the Barron's lists. The years selected correspond to the years that students in the longitudinal studies (NLS-72, HS&B, NELS:88, ELS-2000,HSLS:09, and BPS) initially attended the 4-year postsecondary institutions. Each of the six NCES-Barron's index files is available in a separate worksheet in an Excel workbook file that is in Excel 1997-2003 compatible format.",
-            "modified": "2023-07-07T19:06:08.899882",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "958afa71-b7b2-4e43-ae38-81f23c2abb1f",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1972/2014",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -48543,21 +48505,36 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2012/2013",
+            "title": "Principal Follow-Up Survey, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carl M. Schmitt",
                 "hasEmail": "mailto:carl.schmitt@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The NCES-Barron's Admissions Competitiveness Index Data Files: 1972, 1982, 1992, 2004, 2008, 2014 (NCES 2015-332) contain the Barron's college admissions competitiveness selectivity ratings for 1972, 1982, 1992, 2004, 2008, 2014 along with the NCES Higher Education Information System (HEGIS) FICE ID and Integrated Postsecondary Education Data System (IPEDS) UNITID codes and the Office of Postsecondary Education OPEID codes of each postsecondary institution included. Also included are the city and state of each institution included in the Barron's lists. The years selected correspond to the years that students in the longitudinal studies (NLS-72, HS&B, NELS:88, ELS-2000,HSLS:09, and BPS) initially attended the 4-year postsecondary institutions. Each of the six NCES-Barron's index files is available in a separate worksheet in an Excel workbook file that is in Excel 1997-2003 compatible format.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NCES-Barron's Admissions Competitiveness Index Data Files: 1972, 1982, 1992, 2004, 2008, 2014",
                     "description": "Restricted-use data file for the NCES-Barron's Admissions Competitiveness Index Data Files: 1972, 1982, 1992, 2004, 2008, 2014",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2016332",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NCES-Barron's Admissions Competitiveness Index Data Files: 1972, 1982, 1992, 2004, 2008, 2014"
                 }
             ],
+            "identifier": "958afa71-b7b2-4e43-ae38-81f23c2abb1f",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "access-and-choice-in-higher-education",
@@ -48569,29 +48546,14 @@
                 "postsecondary-education-transcript-studies",
                 "postsecondary-institutions"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:06:08.899882",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2016",
-            "description": "The National Assessment of Educational Progress, 2016 (NAEP 2016) is a data collection that is part of the National Assessment of Educational Progress (NAEP) program; program data are available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2016 (https://nces.ed.gov/nationsreportcard/) was a cross-sectional survey of student achievement assessing what America's 8th-grade students know and can do in the musical and visual arts. The data collection included paper-and- pencil assessments of students as well as online questionnaires of teachers and school administrators. NAEP 2016 included only national-level assessments. Key statistics produced from NAEP 2016 include overall results of student performance and achievement, student performance results for various subgroups of students, and information on various educational factors.",
-            "modified": "2023-07-07T19:03:34.676727",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "deacbda6-22c5-4e99-b4a1-1abfb7262426",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2015/2016",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -48612,29 +48574,43 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "1972/2014",
+            "title": "NCES-Barron's Admissions Competitiveness Index Data Files: 1972, 1982, 1992, 2004, 2008, 2014"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2016 (NAEP 2016) is a data collection that is part of the National Assessment of Educational Progress (NAEP) program; program data are available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2016 (https://nces.ed.gov/nationsreportcard/) was a cross-sectional survey of student achievement assessing what America's 8th-grade students know and can do in the musical and visual arts. The data collection included paper-and- pencil assessments of students as well as online questionnaires of teachers and school administrators. NAEP 2016 included only national-level assessments. Key statistics produced from NAEP 2016 include overall results of student performance and achievement, student performance results for various subgroups of students, and information on various educational factors.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2016 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2016 Restricted-Use Data File",
                     "description": "Restricted-use data file for the National Assessment of Educational Progress, 2016",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2016 Restricted-Use Data File"
                 }
             ],
+            "identifier": "deacbda6-22c5-4e99-b4a1-1abfb7262426",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessments",
@@ -48646,33 +48622,14 @@
                 "secondary-education",
                 "students-with-disabilities-sd"
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
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Indian Education Study, 2015",
-            "description": "The 2015 National Indian Education Study (NIES 2015) is a data collection that is part of the National Assessment of Educational Progress (NAEP) program; program data are available since 2005 at <https://nces.ed.gov/nationsreportcard/nies/>. NIES 2015 (https://nces.ed.gov/nationsreportcard/nies/) was a cross-sectional survey of the educational experiences of American Indian and Alaska Native (AI/AN) students in the United States. The data collection included paper-and-pencil questionnaires of students, as well as online questionnaires of teachers and school administrators. Key statistics produced from NIES 2015 include information on student knowledge of their Native cultures and languages; the extent to which AI/AN culture and language were a part of curricula; and the extent to which school resources were available for improving AI/AN student achievement.",
-            "modified": "2023-07-07T19:02:50.772443",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "ecc05822-42c2-4aac-9702-b70916297281",
-            "dataQuality": true,
-            "issued": "2018-09-27",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2014/2015",
+            "modified": "2023-07-07T19:03:34.676727",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -48693,29 +48650,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2015/2016",
+            "title": "National Assessment of Educational Progress, 2016"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2015 National Indian Education Study (NIES 2015) is a data collection that is part of the National Assessment of Educational Progress (NAEP) program; program data are available since 2005 at <https://nces.ed.gov/nationsreportcard/nies/>. NIES 2015 (https://nces.ed.gov/nationsreportcard/nies/) was a cross-sectional survey of the educational experiences of American Indian and Alaska Native (AI/AN) students in the United States. The data collection included paper-and-pencil questionnaires of students, as well as online questionnaires of teachers and school administrators. Key statistics produced from NIES 2015 include information on student knowledge of their Native cultures and languages; the extent to which AI/AN culture and language were a part of curricula; and the extent to which school resources were available for improving AI/AN student achievement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2015 National Indian Education Study data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/niesdata",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2015 National Indian Education Study (NIES) Restricted Use Data Files",
                     "description": "Restricted-use data file for the NAEP 2015 National Indian Education Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2018158",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2015 National Indian Education Study (NIES) Restricted Use Data Files"
                 }
             ],
+            "identifier": "ecc05822-42c2-4aac-9702-b70916297281",
+            "issued": "2018-09-27",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "focus-groups",
@@ -48725,32 +48701,20 @@
                 "nies",
                 "report"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-07T19:02:50.772443",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "RSA PY2017 and PY2018 Workforce Innovation and Opportunity Act (WIOA) Annual Reports",
-            "description": "Annual statewide performance reports, including information on levels of performance achieved with respect to the primary indicators of performance. For Program Year (PY) 2017, State VR agencies reported this information for the first time under WIOA. PY 2017 data only includes performance for the Measurable Skill Gains indicator for the VR program because this was the only indicator for which data were available for reporting in PY 2017. In PY 2018, State VR agencies reported performance for Measurable Skill Gains along with two additional indicators: Employment Rate in the Second Quarter after Exit and Median Earnings in the Second Quarter after Exit.",
-            "modified": "2023-07-07T18:58:39.949133",
-            "accessLevel": "public",
-            "identifier": "6dbfa584-6362-453e-8d69-bd37a584188e",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
-            "temporal": "2017-07-01/2019-06-30",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                "name": "National Center for Education Statistics (NCES)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -48763,31 +48727,49 @@
                             }
                         }
                     }
+                }
+            },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2014/2015",
+            "title": "National Indian Education Study, 2015"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andrew Kerns",
                 "hasEmail": "mailto:rsadata@ed.gov"
             },
+            "description": "Annual statewide performance reports, including information on levels of performance achieved with respect to the primary indicators of performance. For Program Year (PY) 2017, State VR agencies reported this information for the first time under WIOA. PY 2017 data only includes performance for the Measurable Skill Gains indicator for the VR program because this was the only indicator for which data were available for reporting in PY 2017. In PY 2018, State VR agencies reported performance for Measurable Skill Gains along with two additional indicators: Employment Rate in the Second Quarter after Exit and Median Earnings in the Second Quarter after Exit.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Program Year 2017",
                     "description": "Workforce Innovation and Opportunity Act - View or Download",
-                    "downloadURL": "https://data.ed.gov/dataset/180234be-36fe-4572-8f46-8f062d5b178b/resource/53455bab-6494-45f8-b51d-9c711b20cd55/download/py2017-data-all-states.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/180234be-36fe-4572-8f46-8f062d5b178b/resource/53455bab-6494-45f8-b51d-9c711b20cd55/download/py2017-data-all-states.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Program Year 2017"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Program Year 2017",
                     "description": "Workforce Innovation and Opportunity Act - View or Download",
-                    "downloadURL": "https://data.ed.gov/dataset/180234be-36fe-4572-8f46-8f062d5b178b/resource/69ba07ac-4ef7-451d-aa87-8a6aee5d52e1/download/py18-data-all-states.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/180234be-36fe-4572-8f46-8f062d5b178b/resource/69ba07ac-4ef7-451d-aa87-8a6aee5d52e1/download/py18-data-all-states.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Program Year 2017"
                 }
             ],
+            "identifier": "6dbfa584-6362-453e-8d69-bd37a584188e",
             "keyword": [
                 "current-events",
                 "d9ef757b-555e-4337-8247-a8cc5a42ef23",
@@ -48801,25 +48783,14 @@
                 "vocational-rehabilitation",
                 "wioa"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:20"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:58:39.949133",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "U.S. Department of Education Budget News",
-            "description": "Provides the latest news on funding of the U.S. Department of Education programs, including the President's budget request, congressional action on appropriations and detailed budget tables.",
-            "modified": "2023-07-07T18:56:47.861169",
-            "accessLevel": "public",
-            "identifier": "e7a25f47-90e0-4dde-8469-cbe148e4da1d",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Finance and Operations (OFO)",
+                "name": "Office of Special Education and Rehabilitative Services (OSERS)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -48833,110 +48804,122 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2017-07-01/2019-06-30",
+            "title": "RSA PY2017 and PY2018 Workforce Innovation and Opportunity Act (WIOA) Annual Reports"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ofo@ed.gov"
             },
+            "description": "Provides the latest news on funding of the U.S. Department of Education programs, including the President's budget request, congressional action on appropriations and detailed budget tables.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2020 Congressional Action",
                     "description": "FY 2020 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/ad30f065-cee0-4c3a-b165-546fd8a6d18c/download/20action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/ad30f065-cee0-4c3a-b165-546fd8a6d18c/download/20action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2020 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2019 Congressional Action",
                     "description": "FY 2019 Congressional Action\u2014\nOn September 28, 2018 the President signed the Department of Defense and Labor, Health and Human Services, and Education Appropriations Act, 2019 (Public Law 115-245), which provides funding for the Department of Education through September 30, 2019.PDF [167KB] - FY 2019 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/d2a12572-e773-4a51-b195-d41bcef2b432/download/19action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/d2a12572-e773-4a51-b195-d41bcef2b432/download/19action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2019 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2018 Congressional Action",
                     "description": "FY 2018 Congressional Action\u2014\nOn March 23, 2018 the President signed into law the Department of Education  Appropriations Act, 2018 (P.L. 115-141) which provides funding for the Department of Education through September 30, 2018.PDF [161KB] - FY 2018 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/1639bd4a-57ec-4ee8-b2d1-fe76d74e6306/download/18action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/1639bd4a-57ec-4ee8-b2d1-fe76d74e6306/download/18action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2018 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2017 Congressional Action",
                     "description": "FY 2017 Congressional Action\u2014\nOn April 28, 2017, the President signed into law the Consolidated Appropriations Act, 2017, (P.L. 115-31) making appropriations for most Federal Agencies through September 30, 2017.  On December 10, 2016, the President signed the Further Continuing and Security Assistance Appropriation Act, 2017 (P.L. 114-254), providing funding for the Department of Education and other Federal Departments through April 28, 2017.  Under the terms of (P.L. 114-254) a 0.1901 percent across-the-board reduction is applied to discretionary budget authority.  The resulting amounts are reflected in the 2017 Annualized CR level.PDF [264KB] - FY 2017 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/dfa68f61-ffc7-43e4-9b6b-36a039ace623/download/17action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/dfa68f61-ffc7-43e4-9b6b-36a039ace623/download/17action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2017 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2016 Congressional Action",
                     "description": "FY 2016 Congressional Action\u2014\nOn December 18, the President signed into law the Consolidated Appropriations Act, 2016 (P.L. 114-113), making appropriations for FY 2016 Labor, Health and Human Services, Education and Related Agencies through September 30, 2016.PDF [264KB] - FY 2016 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/9077c7ee-6276-4760-af06-d7560a2711fd/download/16action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/9077c7ee-6276-4760-af06-d7560a2711fd/download/16action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2016 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2015 Congressional Action",
                     "description": "FY 2015 Congressional Action - FY 2015 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/d361f47e-e77d-4abb-9aca-27485788bef4/download/15action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/d361f47e-e77d-4abb-9aca-27485788bef4/download/15action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2015 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2014 Congressional Action",
                     "description": "FY 2014 Congressional Action - FY 2014 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/92886c9e-abca-4f97-8c3e-72ff26908cd5/download/14action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/92886c9e-abca-4f97-8c3e-72ff26908cd5/download/14action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2014 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2013 Congressional Action",
                     "description": "FY 2013 Congressional Action - FY 2013 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/c8dd7530-0422-4c2b-826d-5a086d78bb3a/download/13action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/c8dd7530-0422-4c2b-826d-5a086d78bb3a/download/13action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2013 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Sequestration\u2014The President was required by the Budget Control Act of 2011, as amended, to issue a sequestration order on March 1, 2013, for automatic spending cuts to Federal Government programs for the remainder of the fiscal year",
                     "description": "Sequestration\u2014The President was required by the Budget Control Act of 2011, as amended, to issue a sequestration order on March 1, 2013, for automatic spending cuts to Federal Government programs for the remainder of the fiscal year - Sequestration\u2014The President was required by the Budget Control Act of 2011, as amended, to issue a sequestration order on March 1, 2013, for automatic spending cuts to Federal Government programs for the remainder of the fiscal year",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/766a327f-802e-41d5-9770-7b9332c2eb6f/download/sequesterfy13.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/766a327f-802e-41d5-9770-7b9332c2eb6f/download/sequesterfy13.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Sequestration\u2014The President was required by the Budget Control Act of 2011, as amended, to issue a sequestration order on March 1, 2013, for automatic spending cuts to Federal Government programs for the remainder of the fiscal year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2012 Consolidated Appropriations Act of 2012",
                     "description": "FY 2012 Consolidated Appropriations Act of 2012 - FY 2012 Consolidated Appropriations Act of 2012",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/498388d1-5b45-4860-9043-a97745ede84b/download/12action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/498388d1-5b45-4860-9043-a97745ede84b/download/12action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2012 Consolidated Appropriations Act of 2012"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2011 Full-Year Continuing Appropriations Act",
                     "description": "FY 2011 Full-Year Continuing Appropriations Act - FY 2011 Full-Year Continuing Appropriations Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/8f9c078e-7c2e-43c6-aa91-c007ce2ffbff/download/11action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/8f9c078e-7c2e-43c6-aa91-c007ce2ffbff/download/11action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2011 Full-Year Continuing Appropriations Act"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2011 Full-Year Continuing Appropriations Act",
                     "description": "FY 2011 Full-Year Continuing Appropriations Act - FY 2011 Full-Year Continuing Appropriations Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/12d6e711-f200-4aa4-9536-b5e99f94ea66/download/compare11action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c86d8a85-649d-4025-b72a-31b418356005/resource/12d6e711-f200-4aa4-9536-b5e99f94ea66/download/compare11action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2011 Full-Year Continuing Appropriations Act"
                 }
             ],
+            "identifier": "e7a25f47-90e0-4dde-8469-cbe148e4da1d",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "appropriations",
@@ -48950,22 +48933,11 @@
                 "ofo",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:56:47.861169",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "U.S. Department of Education Budget News",
-            "description": "Provides the latest news on funding of the U.S. Department of Education programs, including the President's budget request, congressional action on appropriations and detailed budget tables.",
-            "modified": "2023-07-07T18:55:15.241880",
-            "accessLevel": "public",
-            "identifier": "e1fd91c7-e585-411a-b96b-386ac97a6ba5",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -48982,109 +48954,120 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "U.S. Department of Education Budget News"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ofo@ed.gov"
             },
+            "description": "Provides the latest news on funding of the U.S. Department of Education programs, including the President's budget request, congressional action on appropriations and detailed budget tables.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2020 Congressional Action",
                     "description": "FY 2020 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/815769f0-a52b-4acf-94b6-2bd84be69d6a/download/20action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/815769f0-a52b-4acf-94b6-2bd84be69d6a/download/20action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2020 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2019 Congressional Action",
                     "description": "FY 2019 Congressional Action\u2014\nOn September 28, 2018 the President signed the Department of Defense and Labor, Health and Human Services, and Education Appropriations Act, 2019 (Public Law 115-245), which provides funding for the Department of Education through September 30, 2019.PDF [167KB] - FY 2019 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/53e757a5-8472-4bc4-a531-c9e2db2b3f6c/download/19action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/53e757a5-8472-4bc4-a531-c9e2db2b3f6c/download/19action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2019 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2018 Congressional Action",
                     "description": "FY 2018 Congressional Action\u2014\nOn March 23, 2018 the President signed into law the Department of Education  Appropriations Act, 2018 (P.L. 115-141) which provides funding for the Department of Education through September 30, 2018.PDF [161KB] - FY 2018 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/6f4bb14e-5c42-4c6e-9934-c532fc3ae1b3/download/18action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/6f4bb14e-5c42-4c6e-9934-c532fc3ae1b3/download/18action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2018 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2017 Congressional Action",
                     "description": "FY 2017 Congressional Action\u2014\nOn April 28, 2017, the President signed into law the Consolidated Appropriations Act, 2017, (P.L. 115-31) making appropriations for most Federal Agencies through September 30, 2017.  On December 10, 2016, the President signed the Further Continuing and Security Assistance Appropriation Act, 2017 (P.L. 114-254), providing funding for the Department of Education and other Federal Departments through April 28, 2017.  Under the terms of (P.L. 114-254) a 0.1901 percent across-the-board reduction is applied to discretionary budget authority.  The resulting amounts are reflected in the 2017 Annualized CR level.PDF [264KB] - FY 2017 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/439708b3-c9d9-45da-8e62-67716edc2844/download/17action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/439708b3-c9d9-45da-8e62-67716edc2844/download/17action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2017 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2016 Congressional Action",
                     "description": "FY 2016 Congressional Action\u2014\nOn December 18, the President signed into law the Consolidated Appropriations Act, 2016 (P.L. 114-113), making appropriations for FY 2016 Labor, Health and Human Services, Education and Related Agencies through September 30, 2016.PDF [264KB] - FY 2016 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/acf34bec-f48e-4519-998e-3821acf8780c/download/16action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/acf34bec-f48e-4519-998e-3821acf8780c/download/16action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2016 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2015 Congressional Action",
                     "description": "FY 2015 Congressional Action - FY 2015 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/bb7fe1c9-0afa-47f8-b7c8-048025724762/download/15action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/bb7fe1c9-0afa-47f8-b7c8-048025724762/download/15action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2015 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2014 Congressional Action",
                     "description": "FY 2014 Congressional Action - FY 2014 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/283cc1f1-c699-448a-bcf0-000047d8eb9f/download/14action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/283cc1f1-c699-448a-bcf0-000047d8eb9f/download/14action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2014 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2013 Congressional Action",
                     "description": "FY 2013 Congressional Action - FY 2013 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/4a192f99-ea7d-4549-a498-6b4f1adc722d/download/13action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/4a192f99-ea7d-4549-a498-6b4f1adc722d/download/13action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2013 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Sequestration\u2014The President was required by the Budget Control Act of 2011, as amended, to issue a sequestration order on March 1, 2013, for automatic spending cuts to Federal Government programs for the remainder of the fiscal year",
                     "description": "Sequestration\u2014The President was required by the Budget Control Act of 2011, as amended, to issue a sequestration order on March 1, 2013, for automatic spending cuts to Federal Government programs for the remainder of the fiscal year - Sequestration\u2014The President was required by the Budget Control Act of 2011, as amended, to issue a sequestration order on March 1, 2013, for automatic spending cuts to Federal Government programs for the remainder of the fiscal year",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/d03ebe30-93bb-4db4-81d4-844a1ce7d443/download/sequesterfy13.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/d03ebe30-93bb-4db4-81d4-844a1ce7d443/download/sequesterfy13.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Sequestration\u2014The President was required by the Budget Control Act of 2011, as amended, to issue a sequestration order on March 1, 2013, for automatic spending cuts to Federal Government programs for the remainder of the fiscal year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2012 Consolidated Appropriations Act of 2012",
                     "description": "FY 2012 Consolidated Appropriations Act of 2012 - FY 2012 Consolidated Appropriations Act of 2012",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/f2b75f3f-250e-4cdc-8f35-3879dcea8737/download/12action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/f2b75f3f-250e-4cdc-8f35-3879dcea8737/download/12action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2012 Consolidated Appropriations Act of 2012"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2011 Full-Year Continuing Appropriations Act",
                     "description": "FY 2011 Full-Year Continuing Appropriations Act - FY 2011 Full-Year Continuing Appropriations Act",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/fdeef1d1-0dcc-4041-95b4-25ae76fbb799/download/11action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/fdeef1d1-0dcc-4041-95b4-25ae76fbb799/download/11action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2011 Full-Year Continuing Appropriations Act"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2011 Full-Year Continuing Appropriations Act",
                     "description": "FY 2011 Full-Year Continuing Appropriations Act - FY 2011 Full-Year Continuing Appropriations Act",
-                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/991b8cca-1be3-41d2-a4ef-75418196457b/download/compare11action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/a4a9cd35-8b4d-4799-b39a-3a31b28c8632/resource/991b8cca-1be3-41d2-a4ef-75418196457b/download/compare11action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2011 Full-Year Continuing Appropriations Act"
                 }
             ],
+            "identifier": "e1fd91c7-e585-411a-b96b-386ac97a6ba5",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "appropriations",
@@ -49097,22 +49080,11 @@
                 "ofo",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:55:15.241880",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "U.S. Department of Education Budget History",
-            "description": "Detailed tables showing the budget history of the U.S. Department of Education from FY 1980 to the FY 2018 President's Budget, by major program, and showing State allocations by State and by program from FY 1980-2017.",
-            "modified": "2023-07-07T18:54:37.061554",
-            "accessLevel": "public",
-            "identifier": "474c338a-2c74-4589-9f02-ef4e1a0c951a",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -49129,310 +49101,321 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "U.S. Department of Education Budget News"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "Detailed tables showing the budget history of the U.S. Department of Education from FY 1980 to the FY 2018 President's Budget, by major program, and showing State allocations by State and by program from FY 1980-2017.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1980\u20142019 PB",
                     "description": "1980\u20142019 PB - 1980\u20142019 PB",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/37cf162a-3c54-421e-aee3-84ac5a286865/download/edhistory.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/37cf162a-3c54-421e-aee3-84ac5a286865/download/edhistory.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1980\u20142019 PB"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "2017",
                     "description": "2017 - 2017",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/25a74cf1-9841-47cd-ac2b-0bfe6f57dcc5/download/sthistbypr17.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/25a74cf1-9841-47cd-ac2b-0bfe6f57dcc5/download/sthistbypr17.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2017"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2016",
                     "description": "2016 - 2016",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/c5d7b861-93dd-443c-bad3-d6bb3ee0c278/download/sthisbypr16.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/c5d7b861-93dd-443c-bad3-d6bb3ee0c278/download/sthisbypr16.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2016"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2015",
                     "description": "2015 - 2015",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/80174103-1568-4fd4-bec6-9f644a7e19eb/download/sthisbypr15.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/80174103-1568-4fd4-bec6-9f644a7e19eb/download/sthisbypr15.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2015"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2014",
                     "description": "2014 - 2014",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/0dc71cda-016d-4646-8787-555949942fe5/download/sthistbypr14.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/0dc71cda-016d-4646-8787-555949942fe5/download/sthistbypr14.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2014"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2013",
                     "description": "2013 - 2013",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/d71e8ff9-ccc7-405a-9edf-b99a85845be1/download/sthistbypr13.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/d71e8ff9-ccc7-405a-9edf-b99a85845be1/download/sthistbypr13.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2013"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2012",
                     "description": "2012 - 2012",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/e3a0a817-0674-4c96-af33-97ff1e88f802/download/sthistbypr12.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/e3a0a817-0674-4c96-af33-97ff1e88f802/download/sthistbypr12.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2012"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2011",
                     "description": "2011 - 2011",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/4db002bd-a16c-4f5f-a8a5-8684b4c1aa0b/download/sthistbypr11.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/4db002bd-a16c-4f5f-a8a5-8684b4c1aa0b/download/sthistbypr11.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2011"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2010",
                     "description": "2010 - 2010",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/24f6032d-262b-4e34-a847-af4576f461fd/download/sthistbypr10.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/24f6032d-262b-4e34-a847-af4576f461fd/download/sthistbypr10.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2010"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2009",
                     "description": "2009 - 2009",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/1cbf4429-9879-4eef-a431-efd09f6e1074/download/sthistbypr09.xls"
-                },
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/1cbf4429-9879-4eef-a431-efd09f6e1074/download/sthistbypr09.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2009"
+                },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2001-2008",
                     "description": "2001-2008 - 2001-2008",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/07d64759-76ac-40ac-a1a3-13a4d5d52a97/download/sthistbypr01to08.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/07d64759-76ac-40ac-a1a3-13a4d5d52a97/download/sthistbypr01to08.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2001-2008"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2000",
                     "description": "2000 - 2000",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/9c6c319f-0284-44b1-8d8e-8141cfcc2182/download/sthistbypr2000.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/9c6c319f-0284-44b1-8d8e-8141cfcc2182/download/sthistbypr2000.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2000"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1997\u20141999",
                     "description": "1997\u20141999 - 1997\u20141999",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/66b7c420-b85d-4b33-be4c-757c67a470db/download/sthistbypr97to99.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/66b7c420-b85d-4b33-be4c-757c67a470db/download/sthistbypr97to99.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1997\u20141999"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1994\u20141996",
                     "description": "1994\u20141996 - 1994\u20141996",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/410c2621-186a-4e71-a6cb-731230f6a08a/download/sthistbypr94to96.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/410c2621-186a-4e71-a6cb-731230f6a08a/download/sthistbypr94to96.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1994\u20141996"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1991\u20141993",
                     "description": "1991\u20141993 - 1991\u20141993",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/eff841b6-47fe-4d98-89ba-2c7eaa06b511/download/sthistbypr91to93.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/eff841b6-47fe-4d98-89ba-2c7eaa06b511/download/sthistbypr91to93.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1991\u20141993"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1988\u20141990",
                     "description": "1988\u20141990 - 1988\u20141990",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/94bc1420-3a53-403c-bdd8-adfcb8d0ccff/download/sthistbypr88to90.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/94bc1420-3a53-403c-bdd8-adfcb8d0ccff/download/sthistbypr88to90.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1988\u20141990"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1985\u20141987",
                     "description": "1985\u20141987 - 1985\u20141987",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/d41f6f6e-9462-4616-95e0-d5c17735bfb7/download/sthistbypr85to87.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/d41f6f6e-9462-4616-95e0-d5c17735bfb7/download/sthistbypr85to87.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1985\u20141987"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1982\u20141984",
                     "description": "1982\u20141984 - 1982\u20141984",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/47650773-b1fe-422f-af24-48577fdece9e/download/sthistbypr82to84.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/47650773-b1fe-422f-af24-48577fdece9e/download/sthistbypr82to84.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1982\u20141984"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1980\u20141981",
                     "description": "1980\u20141981 - 1980\u20141981",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/9eab5fea-7a73-4283-a57d-83377cfd1f81/download/sthistbypr80to81.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/9eab5fea-7a73-4283-a57d-83377cfd1f81/download/sthistbypr80to81.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1980\u20141981"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "2017",
                     "description": "2017 - 2017",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/93885a92-3235-4feb-9ff8-4f9ac8987826/download/sthisbyst17.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/93885a92-3235-4feb-9ff8-4f9ac8987826/download/sthisbyst17.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2017"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2016",
                     "description": "2016 - 2016",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/e4543f99-ff2d-4d68-be4d-4073d536f996/download/sthisbyst16.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/e4543f99-ff2d-4d68-be4d-4073d536f996/download/sthisbyst16.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2016"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2015",
                     "description": "2015 - 2015",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/26a73911-3b39-4cc9-b80a-a1e16d40a5b3/download/sthisbyst15.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/26a73911-3b39-4cc9-b80a-a1e16d40a5b3/download/sthisbyst15.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2015"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2014",
                     "description": "2014 - 2014",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/854b20ee-b08c-4dd5-a0a0-53043cbc6ed1/download/sthistbyst14.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/854b20ee-b08c-4dd5-a0a0-53043cbc6ed1/download/sthistbyst14.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2014"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2013",
                     "description": "2013 - 2013",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/8c0e380a-157b-4fb6-af42-f55cfb8f6fc4/download/sthistbyst13.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/8c0e380a-157b-4fb6-af42-f55cfb8f6fc4/download/sthistbyst13.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2013"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2012",
                     "description": "2012 - 2012",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/4bb3218e-ee7c-4e26-aa5d-7197dd2d6f07/download/sthistbyst12.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/4bb3218e-ee7c-4e26-aa5d-7197dd2d6f07/download/sthistbyst12.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2012"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2011",
                     "description": "2011 - 2011",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/ca71563e-f678-4bf9-93e7-e49553e7b009/download/sthistbyst11.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/ca71563e-f678-4bf9-93e7-e49553e7b009/download/sthistbyst11.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2011"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2010",
                     "description": "2010 - 2010",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/65acc467-ab92-4e51-bd4a-784b906ee9a2/download/sthistbyst10.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/65acc467-ab92-4e51-bd4a-784b906ee9a2/download/sthistbyst10.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2010"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2009",
                     "description": "2009 - 2009",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/52856480-b691-4de3-b23b-280fccf2c3ec/download/sthistbyst09.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/52856480-b691-4de3-b23b-280fccf2c3ec/download/sthistbyst09.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2009"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2001-2008",
                     "description": "2001-2008 - 2001-2008",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/6381b141-8318-4434-bf69-97db038a226c/download/sthistbyst01to08.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/6381b141-8318-4434-bf69-97db038a226c/download/sthistbyst01to08.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2001-2008"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2000",
                     "description": "2000 - 2000",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/788b1d0b-7559-4bee-9691-9417e504b9f3/download/sthistbyst2000.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/788b1d0b-7559-4bee-9691-9417e504b9f3/download/sthistbyst2000.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2000"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1997\u20141999",
                     "description": "1997\u20141999 - 1997\u20141999",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/d92b371d-90f0-41ab-9c26-76b219047518/download/sthistbyst97to99.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/d92b371d-90f0-41ab-9c26-76b219047518/download/sthistbyst97to99.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1997\u20141999"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1994\u20141996",
                     "description": "1994\u20141996 - 1994\u20141996",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/faa7dc40-764b-4afa-a59f-cbbdbe904c95/download/sthistbyst94to96.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/faa7dc40-764b-4afa-a59f-cbbdbe904c95/download/sthistbyst94to96.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1994\u20141996"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1991\u20141993",
                     "description": "1991\u20141993 - 1991\u20141993",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/737e8c45-8f01-4df1-9cc1-45a7c80f092f/download/sthistbyst91to93.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/737e8c45-8f01-4df1-9cc1-45a7c80f092f/download/sthistbyst91to93.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1991\u20141993"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1988\u20141990",
                     "description": "1988\u20141990 - 1988\u20141990",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/d0303fb1-0cd6-41d3-850d-c3192c29eadd/download/sthistbyst88to90.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/d0303fb1-0cd6-41d3-850d-c3192c29eadd/download/sthistbyst88to90.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1988\u20141990"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1985\u20141987",
                     "description": "1985\u20141987 - 1985\u20141987",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/5046483c-f53d-4ff3-bd50-42cb6d32b943/download/sthistbyst85to87.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/5046483c-f53d-4ff3-bd50-42cb6d32b943/download/sthistbyst85to87.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1985\u20141987"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1982\u20141984",
                     "description": "1982\u20141984 - 1982\u20141984",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/2597a609-eb6d-420d-9032-a5c32f640994/download/sthistbyst82to84.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/2597a609-eb6d-420d-9032-a5c32f640994/download/sthistbyst82to84.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1982\u20141984"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "1980\u20141981",
                     "description": "1980\u20141981 - 1980\u20141981",
-                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/72725d7e-11cc-4d82-80be-7441091530af/download/sthistbyst80to81.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d302983a-cd55-477c-afcc-004e3774b95c/resource/72725d7e-11cc-4d82-80be-7441091530af/download/sthistbyst80to81.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1980\u20141981"
                 }
             ],
+            "identifier": "474c338a-2c74-4589-9f02-ef4e1a0c951a",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "appropriations",
@@ -49448,22 +49431,11 @@
                 "state-federal-aid",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:54:37.061554",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US Department of Education 1999 FAIR Act Inventory",
-            "description": "This archive page contains the US Department of Education's FY 1999 FAIR Act Inventory of commmercial activities.  Also, contains inherently governmental activities.",
-            "modified": "2023-07-07T18:53:31.120399",
-            "accessLevel": "public",
-            "identifier": "0d50ba80-fc8c-4e09-bc6e-27db3309db24",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -49480,22 +49452,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "U.S. Department of Education Budget History"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ocfo@ed.gov"
             },
+            "description": "This archive page contains the US Department of Education's FY 1999 FAIR Act Inventory of commmercial activities.  Also, contains inherently governmental activities.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "EDFAIR99.zip (88K)",
                     "description": "On October 19, 1998, President Clinton signed into law the \"Federal Activities Inventory Reform Act of 1998\" (FAIR Act). The FAIR Act directs Federal agencies to submit to OMB each year an inventory of all their activities that are performed by Federal employees but are not inherently Governmental (i.e., are commercial). - EDFAIR99.zip (88K)",
-                    "downloadURL": "https://data.ed.gov/dataset/2eba1e27-77ce-4774-b34b-00c6945d1b18/resource/2c8ca742-4a79-4084-af1f-e04aeab7f3a3/download/edfair99.zip"
+                    "downloadURL": "https://data.ed.gov/dataset/2eba1e27-77ce-4774-b34b-00c6945d1b18/resource/2c8ca742-4a79-4084-af1f-e04aeab7f3a3/download/edfair99.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "EDFAIR99.zip (88K)"
                 }
             ],
+            "identifier": "0d50ba80-fc8c-4e09-bc6e-27db3309db24",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "data",
@@ -49504,26 +49487,14 @@
                 "ofo",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:53:31.120399",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teachers Enrolled in Programs Providing Alternative Routes 2015",
-            "description": "summarizes state- and district-level data on the numbers of full-time equivalent (FTE) highly qualified teachers who were enrolled in alternative route programs for three groups of teachers\u2014(1) all teachers, (2) special education teachers, and (3) teachers in language instruction educational programs for English learners (ELs) under Title III of the Elementary and Secondary Education Act of 1965 (ESEA)\u2014as well as for teachers in high-poverty and rural school districts.",
-            "modified": "2023-07-07T18:49:32.112696",
-            "accessLevel": "public",
-            "identifier": "4c9aa817-aa0d-4785-92c6-6cad48c134e2",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
-            "temporal": "2015-09-01/2016-06-01",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Planning, Evaluation and Policy Development (OPEPD)",
+                "name": "Office of Finance and Operations (OFO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -49537,22 +49508,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "US Department of Education 1999 FAIR Act Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:OCDO@ed.gov"
             },
+            "description": "summarizes state- and district-level data on the numbers of full-time equivalent (FTE) highly qualified teachers who were enrolled in alternative route programs for three groups of teachers\u2014(1) all teachers, (2) special education teachers, and (3) teachers in language instruction educational programs for English learners (ELs) under Title III of the Elementary and Secondary Education Act of 1965 (ESEA)\u2014as well as for teachers in high-poverty and rural school districts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "02origdi.xls",
                     "description": "02origdi.xls",
-                    "downloadURL": "https://data.ed.gov/dataset/17a8b175-d445-489a-a3ba-6fa8b4b9d70b/resource/cb7a4577-299e-4241-b631-fbe8caa61c5a/download/02origdi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/17a8b175-d445-489a-a3ba-6fa8b4b9d70b/resource/cb7a4577-299e-4241-b631-fbe8caa61c5a/download/02origdi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "02origdi.xls"
                 }
             ],
+            "identifier": "4c9aa817-aa0d-4785-92c6-6cad48c134e2",
             "keyword": [
                 "district",
                 "fcbc6e9b-a57b-46d9-8246-211eb2309029",
@@ -49561,25 +49543,14 @@
                 "teacher-certification",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2023-07-07T18:49:32.112696",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Student Loan Volume Tables\u2014FY 2009 President's Budget",
-            "description": "These tables show Federal Family Education Loan and William D. Ford Direct Student Loan program volume actuals and estimates prepared for the FY 2009 President's Budget.",
-            "modified": "2023-07-07T18:48:46.809932",
-            "accessLevel": "public",
-            "identifier": "c51cda55-7d0d-4ea4-acb2-85929a1c1839",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Finance and Operations (OFO)",
+                "name": "Office of Planning, Evaluation and Policy Development (OPEPD)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -49593,110 +49564,122 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2015-09-01/2016-06-01",
+            "title": "Teachers Enrolled in Programs Providing Alternative Routes 2015"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "These tables show Federal Family Education Loan and William D. Ford Direct Student Loan program volume actuals and estimates prepared for the FY 2009 President's Budget.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Gross Loan Volume by Award Year",
                     "description": "Gross Loan Volume by Award Year - Gross Loan Volume by Award Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/1c2fcf17-b952-4299-a4b8-4e5a1c3943f3/download/09dlgross-ay.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/1c2fcf17-b952-4299-a4b8-4e5a1c3943f3/download/09dlgross-ay.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Gross Loan Volume by Award Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Gross Loan Volume by Fiscal Year",
                     "description": "Gross Loan Volume by Fiscal Year - Gross Loan Volume by Fiscal Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/9ca9de55-74d5-4806-9fd1-3b7f7f646caa/download/09dlgross-fy.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/9ca9de55-74d5-4806-9fd1-3b7f7f646caa/download/09dlgross-fy.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Gross Loan Volume by Fiscal Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Net Loan Volume by Award Year",
                     "description": "Net Loan Volume by Award Year - Net Loan Volume by Award Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/497bfca0-e797-4601-aba0-4b0deddac049/download/09dlnet-ay.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/497bfca0-e797-4601-aba0-4b0deddac049/download/09dlnet-ay.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Net Loan Volume by Award Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Net Loan Volume by Fiscal Year",
                     "description": "Net Loan Volume by Fiscal Year - Net Loan Volume by Fiscal Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/420e4f76-549f-42d0-9a4d-cd239b075983/download/09dlnet-fy.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/420e4f76-549f-42d0-9a4d-cd239b075983/download/09dlnet-fy.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Net Loan Volume by Fiscal Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Gross Loan Volume by Award Year",
                     "description": "Gross Loan Volume by Award Year - Gross Loan Volume by Award Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/842cc69b-3333-48b3-9860-d18ade2be423/download/09ffelgross-ay.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/842cc69b-3333-48b3-9860-d18ade2be423/download/09ffelgross-ay.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Gross Loan Volume by Award Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Gross Loan Volume by Fiscal Year",
                     "description": "Gross Loan Volume by Fiscal Year - Gross Loan Volume by Fiscal Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/6fa1d486-8e86-445b-b723-d313761ba4f2/download/09ffelgross-fy.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/6fa1d486-8e86-445b-b723-d313761ba4f2/download/09ffelgross-fy.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Gross Loan Volume by Fiscal Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Net Loan Volume by Award Year",
                     "description": "Net Loan Volume by Award Year - Net Loan Volume by Award Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/c2caa849-030d-498b-9bce-2c3f4fa4d34e/download/09ffelnet-ay.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/c2caa849-030d-498b-9bce-2c3f4fa4d34e/download/09ffelnet-ay.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Net Loan Volume by Award Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Net Loan Volume by Fiscal Year",
                     "description": "Net Loan Volume by Fiscal Year - Net Loan Volume by Fiscal Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/d399a0b1-ebd4-4361-b724-82098d9652d3/download/09ffelnet-fy.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/d399a0b1-ebd4-4361-b724-82098d9652d3/download/09ffelnet-fy.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Net Loan Volume by Fiscal Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Gross Loan Volume by Award Year",
                     "description": "Gross Loan Volume by Award Year - Gross Loan Volume by Award Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/36eb7e6d-15bc-4653-82e7-f69cb69be301/download/09ffeldlgross-ay.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/36eb7e6d-15bc-4653-82e7-f69cb69be301/download/09ffeldlgross-ay.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Gross Loan Volume by Award Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Gross Loan Volume by Fiscal Year",
                     "description": "Gross Loan Volume by Fiscal Year - Gross Loan Volume by Fiscal Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/d937f9e0-d63e-4b2c-8db8-322c3aa2033d/download/09ffeldlgross-fy.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/d937f9e0-d63e-4b2c-8db8-322c3aa2033d/download/09ffeldlgross-fy.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Gross Loan Volume by Fiscal Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Net Loan Volume by Award Year",
                     "description": "Net Loan Volume by Award Year - Net Loan Volume by Award Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/8ed89b82-2796-443e-8e50-6ba2e452ac75/download/09ffeldlnet-ay.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/8ed89b82-2796-443e-8e50-6ba2e452ac75/download/09ffeldlnet-ay.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Net Loan Volume by Award Year"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Net Loan Volume by Fiscal Year",
                     "description": "Net Loan Volume by Fiscal Year - Net Loan Volume by Fiscal Year",
-                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/dece9241-6420-4264-8ab1-87983e4e79bb/download/09ffeldlnet-fy.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/243b4252-4a74-448c-846f-33cbab886b40/resource/dece9241-6420-4264-8ab1-87983e4e79bb/download/09ffeldlnet-fy.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Net Loan Volume by Fiscal Year"
                 }
             ],
+            "identifier": "c51cda55-7d0d-4ea4-acb2-85929a1c1839",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "direct-loans",
@@ -49707,22 +49690,11 @@
                 "student-loan-programs",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:48:46.809932",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Student Aid Policies Included in the FY 2006 President's Budget",
-            "description": "<p>This table (in pdf and xls) shows the budget impact, on outlays, of student aid-related Higher Education Act reauthorization proposals included in the FY 2006 President's Budget.",
-            "modified": "2023-07-07T18:47:42.132493",
-            "accessLevel": "public",
-            "identifier": "abc23346-13d8-4f81-839f-2628d8d9d520",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -49739,22 +49711,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Student Loan Volume Tables\u2014FY 2009 President's Budget"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "<p>This table (in pdf and xls) shows the budget impact, on outlays, of student aid-related Higher Education Act reauthorization proposals included in the FY 2006 President's Budget.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "This table (last updated 02/07/05), available in",
                     "description": "PDF - This table (last updated 02/07/05), available in",
-                    "downloadURL": "https://data.ed.gov/dataset/3f7da33b-50d2-4c0d-b4b7-38a71fff60d9/resource/2f5ff5cf-c18b-4417-bb0e-b920e8e7d954/download/outlayimpact.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3f7da33b-50d2-4c0d-b4b7-38a71fff60d9/resource/2f5ff5cf-c18b-4417-bb0e-b920e8e7d954/download/outlayimpact.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "This table (last updated 02/07/05), available in"
                 }
             ],
+            "identifier": "abc23346-13d8-4f81-839f-2628d8d9d520",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "direct-loans",
@@ -49765,25 +49748,14 @@
                 "student-loan-programs",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:47:42.132493",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Section 117 of the Higher Education Act of 1965",
-            "description": "This page provides information about ED's oversight of Section 117 of the Higher Education Act of 1965, which requires that universities report certain contracts with and gifts from foreign sources.",
-            "modified": "2023-07-07T18:45:51.792855",
-            "accessLevel": "public",
-            "identifier": "147b2b27-8677-4fcb-aec8-33edee8ca126",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the General Counsel (OGC)",
+                "name": "Office of Finance and Operations (OFO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -49797,22 +49769,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Student Aid Policies Included in the FY 2006 President's Budget"
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
                 "fn": "NA",
                 "hasEmail": "mailto:ForeignSourceReporting@ed.gov"
             },
+            "description": "This page provides information about ED's oversight of Section 117 of the Higher Education Act of 1965, which requires that universities report certain contracts with and gifts from foreign sources.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Foreign Gifts and Contracts Report",
                     "description": "Over 30 years ago, Congress enacted Section 117 of the Higher Education Act of 1965 (HEA) in light of concerns about the growing financial relationship between U.S. universities and foreign sources. Congress balanced academic freedom and national security by mandating financial transparency through required reporting of contracts with and gifts from a foreign source that, alone or combined, are valued at $250,000 or more in a calendar year.",
-                    "downloadURL": "https://data.ed.gov/dataset/4062761e-b13f-443c-8915-d279ffbbbab3/resource/d3e999d7-7bdc-46e0-ad3b-d7acda1f84f0/download/cuserssara.stefanikonedrive-u.s.-department-of-educationdesktopforeigngifts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/4062761e-b13f-443c-8915-d279ffbbbab3/resource/d3e999d7-7bdc-46e0-ad3b-d7acda1f84f0/download/cuserssara.stefanikonedrive-u.s.-department-of-educationdesktopforeigngifts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Foreign Gifts and Contracts Report"
                 }
             ],
+            "identifier": "147b2b27-8677-4fcb-aec8-33edee8ca126",
             "keyword": [
                 "8dea2fcc-a8c2-4e0c-b278-1182100318ab",
                 "colleges",
@@ -49824,26 +49807,14 @@
                 "united-states",
                 "universities"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:45:51.792855",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "RSA: Previously Posted News from RSA",
-            "description": "Previously posted news items from the Rehabilitation Services Administration (RSA) from calendar years 2013 through 2019.",
-            "modified": "2023-07-07T18:44:21.292667",
-            "accessLevel": "public",
-            "identifier": "1890311a-a9f1-45e0-9218-17e061b3e232",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
-            "temporal": "2013-01-01/2019-12-31",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                "name": "Office of the General Counsel (OGC)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -49857,30 +49828,41 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Section 117 of the Higher Education Act of 1965"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andrew Kerns",
                 "hasEmail": "mailto:rsadata@ed.gov"
             },
+            "description": "Previously posted news items from the Rehabilitation Services Administration (RSA) from calendar years 2013 through 2019.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2014 Vocational Rehabilitation Fiscal Monitoring Tables (3.1, 3.2, 3.3, 3.4)",
                     "description": "RSA: Previously Posted News from RSA - 2014 News Items",
-                    "downloadURL": "https://data.ed.gov/dataset/eaf2b56f-af0c-44d7-a346-e3c3c6732a11/resource/3a553315-ef26-49ad-9989-6f5abb5e5832/download/fiscal-tables.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/eaf2b56f-af0c-44d7-a346-e3c3c6732a11/resource/3a553315-ef26-49ad-9989-6f5abb5e5832/download/fiscal-tables.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2014 Vocational Rehabilitation Fiscal Monitoring Tables (3.1, 3.2, 3.3, 3.4)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2014 Vocational Rehabilitation Data Monitoring Tables (3.5 and above)",
                     "description": "RSA: Previously Posted News from RSA - 2014 News Items",
-                    "downloadURL": "https://data.ed.gov/dataset/eaf2b56f-af0c-44d7-a346-e3c3c6732a11/resource/b6c81e7b-9fb2-4109-b963-b48747239fd6/download/data-tables.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/eaf2b56f-af0c-44d7-a346-e3c3c6732a11/resource/b6c81e7b-9fb2-4109-b963-b48747239fd6/download/data-tables.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2014 Vocational Rehabilitation Data Monitoring Tables (3.5 and above)"
                 }
             ],
+            "identifier": "1890311a-a9f1-45e0-9218-17e061b3e232",
             "keyword": [
                 "current-events",
                 "d9ef757b-555e-4337-8247-a8cc5a42ef23",
@@ -49893,28 +49875,14 @@
                 "united-states",
                 "vocational-rehabilitation"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:20"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:44:21.292667",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Awards -- Promoting Postbaccalaureate Opportunities for Hispanic Americans Program",
-            "description": "The Promoting Postbaccalaureate Opportunities for Hispanic Americans (PPOHA) Program provides grants to: (1) expand postbaccalaureate educational opportunities for, and improve the academic attainment of, Hispanic students; and (2) expand the postbaccalaureate academic offerings as well as enhance the program quality in the institutions of higher education that are educating the majority of Hispanic college students and helping large numbers of Hispanic and low-income students complete postsecondary degrees.",
-            "modified": "2023-07-07T18:43:04.575905",
-            "accessLevel": "public",
-            "identifier": "6ee08fff-7825-44bc-86f6-8ca21a11695c",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                "name": "Office of Special Education and Rehabilitative Services (OSERS)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -49927,64 +49895,75 @@
                         }
                     }
                 }
-                }
             },
+            "spatial": "United States",
+            "temporal": "2013-01-01/2019-12-31",
+            "title": "RSA: Previously Posted News from RSA"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "The Promoting Postbaccalaureate Opportunities for Hispanic Americans (PPOHA) Program provides grants to: (1) expand postbaccalaureate educational opportunities for, and improve the academic attainment of, Hispanic students; and (2) expand the postbaccalaureate academic offerings as well as enhance the program quality in the institutions of higher education that are educating the majority of Hispanic college students and helping large numbers of Hispanic and low-income students complete postsecondary degrees.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "PDF",
-                    "title": "ppoha-grantees09.pdf",
                     "description": "ppoha-grantees09.pdf",
-                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/ebd81cdd-1478-4b48-9614-0d66bb45e7fc/download/ppoha-grantees09.pdf"
+                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/ebd81cdd-1478-4b48-9614-0d66bb45e7fc/download/ppoha-grantees09.pdf",
+                    "format": "PDF",
+                    "mediaType": "application/pdf",
+                    "title": "ppoha-grantees09.pdf"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "DOC",
-                    "title": "ppoha-abstracts2014.doc",
                     "description": "ppoha-abstracts2014.doc",
-                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/df63b4b7-e793-4a07-852a-365af41cc306/download/ppoha-abstracts2014.doc"
+                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/df63b4b7-e793-4a07-852a-365af41cc306/download/ppoha-abstracts2014.doc",
+                    "format": "DOC",
+                    "mediaType": "application/msword",
+                    "title": "ppoha-abstracts2014.doc"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "DOC",
-                    "title": "ppoha-abstracts10.doc",
                     "description": "ppoha-abstracts10.doc",
-                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/8ad4317e-046e-44e3-935e-a6995f80317d/download/ppoha-abstracts10.doc"
+                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/8ad4317e-046e-44e3-935e-a6995f80317d/download/ppoha-abstracts10.doc",
+                    "format": "DOC",
+                    "mediaType": "application/msword",
+                    "title": "ppoha-abstracts10.doc"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "PDF",
-                    "title": "ppoha-abstracts09.pdf",
                     "description": "ppoha-abstracts09.pdf",
-                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/953cfdd4-fa4a-4e4c-8243-83e226455857/download/ppoha-abstracts09.pdf"
+                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/953cfdd4-fa4a-4e4c-8243-83e226455857/download/ppoha-abstracts09.pdf",
+                    "format": "PDF",
+                    "mediaType": "application/pdf",
+                    "title": "ppoha-abstracts09.pdf"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-                    "format": "DOCX",
-                    "title": "ppoha2020abstracts.docx",
                     "description": "ppoha2020abstracts.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/8c29eb85-7b64-4d38-8631-f9e2bb7dcce3/download/ppoha2020abstracts.docx"
+                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/8c29eb85-7b64-4d38-8631-f9e2bb7dcce3/download/ppoha2020abstracts.docx",
+                    "format": "DOCX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "ppoha2020abstracts.docx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-                    "format": "DOCX",
-                    "title": "ppoha2019abstracts.docx",
                     "description": "ppoha2019abstracts.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/aa5c0535-928a-48f0-8f1f-4711b40cdf3b/download/ppoha2019abstracts.docx"
+                    "downloadURL": "https://data.ed.gov/dataset/e273508d-b1cb-43f9-bb08-f4814f694e9d/resource/aa5c0535-928a-48f0-8f1f-4711b40cdf3b/download/ppoha2019abstracts.docx",
+                    "format": "DOCX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "ppoha2019abstracts.docx"
                 }
             ],
+            "identifier": "6ee08fff-7825-44bc-86f6-8ca21a11695c",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "dhsi",
@@ -49999,25 +49978,17 @@
                 "title-v",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2023-07-07T18:43:04.575905",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Programs for English Language Learners (OCR)",
-            "description": "The Office for Civil Rights (OCR), U.S. Department of Education developed these materials in response to requests from school districts for a reference tool to assist them through the process of developing a comprehensive English language proficiency or English language learners (ELL)  program.",
-            "modified": "2023-07-07T18:40:33.521529",
-            "accessLevel": "public",
-            "identifier": "b1900abf-ceaa-4cad-aaea-8a1c288051f5",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
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
@@ -50030,23 +50001,35 @@
                             }
                         }
                     }
+                }
+            },
+            "spatial": "United States",
+            "title": "Awards -- Promoting Postbaccalaureate Opportunities for Hispanic Americans Program"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ocr@ed.gov"
             },
+            "description": "The Office for Civil Rights (OCR), U.S. Department of Education developed these materials in response to requests from school districts for a reference tool to assist them through the process of developing a comprehensive English language proficiency or English language learners (ELL)  program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "This document is an HTML version of OCR's November 30, 1999, Resource Materials.  The original document in MS Word format (ELLmsw.zip) can be downloaded",
                     "description": "Resource Materials for Planning and Self-Assessments - This document is an HTML version of OCR's November 30, 1999, Resource Materials.  The original document in MS Word format (ELLmsw.zip) can be downloaded",
-                    "downloadURL": "https://data.ed.gov/dataset/dfd234fb-af4d-46d9-b99e-5a2012fd72da/resource/2115c562-15a6-48e4-b3bd-c5fdf7810f6d/download/ellmsw.zip"
+                    "downloadURL": "https://data.ed.gov/dataset/dfd234fb-af4d-46d9-b99e-5a2012fd72da/resource/2115c562-15a6-48e4-b3bd-c5fdf7810f6d/download/ellmsw.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "This document is an HTML version of OCR's November 30, 1999, Resource Materials.  The original document in MS Word format (ELLmsw.zip) can be downloaded"
                 }
             ],
+            "identifier": "b1900abf-ceaa-4cad-aaea-8a1c288051f5",
             "keyword": [
                 "519e6cdf-3011-4b75-9e12-34a45cb17fd8",
                 "bilingual-education",
@@ -50060,25 +50043,14 @@
                 "school",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:40:33.521529",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Phase Three Resources - Race to the Top Fund",
-            "description": "This page contains links to publications, research, reports, related sites, technical assistance, events notices, or presentations for the Race to the Top Fund program.",
-            "modified": "2023-07-07T18:39:03.245319",
-            "accessLevel": "public",
-            "identifier": "c3c0602d-7d3a-4498-adef-cb22d1fc993c",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Finance and Operations (OFO)",
+                "name": "Office for Civil Rights (OCR)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -50092,22 +50064,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Programs for English Language Learners (OCR)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "This page contains links to publications, research, reports, related sites, technical assistance, events notices, or presentations for the Race to the Top Fund program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Application",
                     "description": "MS Word (508K) - Application",
-                    "downloadURL": "https://data.ed.gov/dataset/ebd65139-6818-4c7d-b74a-adcaeef52b89/resource/c69d30c4-3967-4d3f-9b3b-f45d6266320d/download/phase3-budget-template.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/ebd65139-6818-4c7d-b74a-adcaeef52b89/resource/c69d30c4-3967-4d3f-9b3b-f45d6266320d/download/phase3-budget-template.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Application"
                 }
             ],
+            "identifier": "c3c0602d-7d3a-4498-adef-cb22d1fc993c",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "academic-achievement",
@@ -50123,28 +50106,14 @@
                 "school-reform",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:39:03.245319",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Performance -- Teacher Quality Enhancement Grants",
-            "description": "This archived page lists annual performance reports, Government Performance and Results Act (GPRA) indicators, success stories, promising practices, data analysis, and performance reports for the Teacher Quality Enhancement Grants Program.",
-            "modified": "2023-07-07T18:37:32.089330",
-            "accessLevel": "public",
-            "identifier": "23c42d65-9026-4cd7-a3e9-f55477b3fbaa",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                "name": "Office of Finance and Operations (OFO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -50157,32 +50126,42 @@
                         }
                     }
                 }
-                }
             },
+            "spatial": "United States",
+            "title": "Phase Three Resources - Race to the Top Fund"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "This archived page lists annual performance reports, Government Performance and Results Act (GPRA) indicators, success stories, promising practices, data analysis, and performance reports for the Teacher Quality Enhancement Grants Program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Grantee Analysis and Summary, 2005-06:",
                     "description": "Grantee Analysis and Summary, 2005-06: -",
-                    "downloadURL": "https://data.ed.gov/dataset/8c3b132d-89c0-4106-aac7-81f979bdfa88/resource/f92f66c8-453e-4233-83df-a8b0d731368c/download/tqeanalysis0506.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8c3b132d-89c0-4106-aac7-81f979bdfa88/resource/f92f66c8-453e-4233-83df-a8b0d731368c/download/tqeanalysis0506.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Grantee Analysis and Summary, 2005-06:"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Grantee Analysis and Summary, 2006-07:",
                     "description": "Grantee Analysis and Summary, 2006-07: -",
-                    "downloadURL": "https://data.ed.gov/dataset/8c3b132d-89c0-4106-aac7-81f979bdfa88/resource/552828b3-d13a-480a-a31d-d0962ac6da39/download/tqeanalysis0607.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8c3b132d-89c0-4106-aac7-81f979bdfa88/resource/552828b3-d13a-480a-a31d-d0962ac6da39/download/tqeanalysis0607.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Grantee Analysis and Summary, 2006-07:"
                 }
             ],
+            "identifier": "23c42d65-9026-4cd7-a3e9-f55477b3fbaa",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "grantee",
@@ -50196,22 +50175,11 @@
                 "teacher-quality",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:37:32.089330",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Performance Measures Analysis: 2004-05",
-            "description": "This page provides information on grantee performance effectiveness for the Title III Part A - Strengthening Institutions Program.",
-            "modified": "2023-07-07T18:36:20.769157",
-            "accessLevel": "public",
-            "identifier": "558aedf0-182f-45e8-9b93-17669f191e0e",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -50232,38 +50200,49 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Performance -- Teacher Quality Enhancement Grants"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "This page provides information on grantee performance effectiveness for the Title III Part A - Strengthening Institutions Program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Grantee Analysis",
                     "description": "Grantee Analysis -",
-                    "downloadURL": "https://www2.ed.gov/programs/iduestitle3a/grantee.xls"
+                    "downloadURL": "https://www2.ed.gov/programs/iduestitle3a/grantee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Grantee Analysis"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Summary Analysis for All Continuation Awards",
                     "description": "Summary Analysis for All Continuation Awards -",
-                    "downloadURL": "https://data.ed.gov/dataset/96277718-2137-4b06-b086-f79ee970cc41/resource/e5ba4dc8-d17f-4a01-81e0-a0a43e6130d2/download/continuation.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/96277718-2137-4b06-b086-f79ee970cc41/resource/e5ba4dc8-d17f-4a01-81e0-a0a43e6130d2/download/continuation.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Summary Analysis for All Continuation Awards"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Summary Analysis for Recurring Awards",
                     "description": "Summary Analysis for Recurring Awards -",
-                    "downloadURL": "https://data.ed.gov/dataset/96277718-2137-4b06-b086-f79ee970cc41/resource/dab50a0b-ab0c-45d7-b152-bb97c9811060/download/recurring.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/96277718-2137-4b06-b086-f79ee970cc41/resource/dab50a0b-ab0c-45d7-b152-bb97c9811060/download/recurring.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Summary Analysis for Recurring Awards"
                 }
             ],
+            "identifier": "558aedf0-182f-45e8-9b93-17669f191e0e",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "data",
@@ -50280,22 +50259,11 @@
                 "title-iii",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:36:20.769157",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Performance -- Demonstration Projects to Ensure Students With Disabilities Receive a Quality Higher Education",
-            "description": "This page lists annual performance reports, Government Performance and Results Act (GPRA) indicators, success stories, promising practices, data analyses, and performance reports for the Demonstration Projects to Ensure Students With Disabilities Receive a Quality Higher Education program.",
-            "modified": "2023-07-07T18:35:25.133290",
-            "accessLevel": "public",
-            "identifier": "bcd590f5-cdbc-4603-9557-0c642d89b362",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -50316,22 +50284,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Performance Measures Analysis: 2004-05"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "This page lists annual performance reports, Government Performance and Results Act (GPRA) indicators, success stories, promising practices, data analyses, and performance reports for the Demonstration Projects to Ensure Students With Disabilities Receive a Quality Higher Education program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Table 1:  Performance Results:",
                     "description": "Table 1:  Performance Results: -",
-                    "downloadURL": "https://www2.ed.gov/programs/disabilities/dd-perfresults0607.xls"
+                    "downloadURL": "https://www2.ed.gov/programs/disabilities/dd-perfresults0607.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Table 1:  Performance Results:"
                 }
             ],
+            "identifier": "bcd590f5-cdbc-4603-9557-0c642d89b362",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "demonstration-programs",
@@ -50348,28 +50327,17 @@
                 "tpsid",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:35:25.133290",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by selected school characteristics: United States, 2017\u201318",
-            "description": "Table 1. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by selected school characteristics: United States, 2017\u201318",
-            "modified": "2023-07-07T18:34:25.024936",
-            "accessLevel": "public",
-            "identifier": "26a88296-842d-43d6-a79a-14ab97a3cbf7",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
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
@@ -50384,30 +50352,41 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Performance -- Demonstration Projects to Ensure Students With Disabilities Receive a Quality Higher Education"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "Table 1. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by selected school characteristics: United States, 2017\u201318",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Table 1. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by selected school characteristics: United States, 2017\u201318",
                     "description": "n/a",
-                    "downloadURL": "https://data.ed.gov/dataset/2eee13d2-a0de-4439-9234-2732bf49e2c7/resource/71f74e89-19c6-4308-8778-d760c0e59f76/download/table01fl1718.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/2eee13d2-a0de-4439-9234-2732bf49e2c7/resource/71f74e89-19c6-4308-8778-d760c0e59f76/download/table01fl1718.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 1. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by selected school characteristics: United States, 2017\u201318"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Table 1. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by selected school characteristics: United States, 2017\u201318",
                     "description": "n/a",
-                    "downloadURL": "https://data.ed.gov/dataset/2eee13d2-a0de-4439-9234-2732bf49e2c7/resource/713daeb4-bd42-4bdc-bd46-11c42f884748/download/table01fl1718_se.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/2eee13d2-a0de-4439-9234-2732bf49e2c7/resource/713daeb4-bd42-4bdc-bd46-11c42f884748/download/table01fl1718_se.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 1. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by selected school characteristics: United States, 2017\u201318"
                 }
             ],
+            "identifier": "26a88296-842d-43d6-a79a-14ab97a3cbf7",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "education",
@@ -50421,22 +50400,11 @@
                 "teachers",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:34:25.024936",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by religious or nonsectarian orientation of school: United States, 2017\u201318",
-            "description": "Table 2. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by religious or nonsectarian orientation of school: United States, 2017\u201318",
-            "modified": "2023-07-07T18:33:00.309312",
-            "accessLevel": "public",
-            "identifier": "3b79f470-dad7-4df8-a9bd-a2c09b81fd17",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -50457,30 +50425,41 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by selected school characteristics: United States, 2017\u201318"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "Table 2. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by religious or nonsectarian orientation of school: United States, 2017\u201318",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Table 2. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by religious or nonsectarian orientation of school: United States, 2017\u201318",
                     "description": "n/a",
-                    "downloadURL": "https://data.ed.gov/dataset/74ac106e-6e54-4a23-8744-d561f151ce28/resource/b125aaf9-8aeb-48a1-90be-e8e91d76eab3/download/table02fl1718.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/74ac106e-6e54-4a23-8744-d561f151ce28/resource/b125aaf9-8aeb-48a1-90be-e8e91d76eab3/download/table02fl1718.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 2. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by religious or nonsectarian orientation of school: United States, 2017\u201318"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Table 2. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by religious or nonsectarian orientation of school: United States, 2017\u201318",
                     "description": "n/a",
-                    "downloadURL": "https://data.ed.gov/dataset/74ac106e-6e54-4a23-8744-d561f151ce28/resource/5ec008e4-ce22-4ea6-bf32-0e05f166ff8e/download/table02fl1718_se.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/74ac106e-6e54-4a23-8744-d561f151ce28/resource/5ec008e4-ce22-4ea6-bf32-0e05f166ff8e/download/table02fl1718_se.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 2. Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by religious or nonsectarian orientation of school: United States, 2017\u201318"
                 }
             ],
+            "identifier": "3b79f470-dad7-4df8-a9bd-a2c09b81fd17",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "education",
@@ -50494,22 +50473,11 @@
                 "teachers",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:33:00.309312",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Number and percentage distribution of private schools, by urbanicity type and selected school characteristics: United States, 2017\u201318",
-            "description": "Table 4. Number and percentage distribution of private schools, by urbanicity type and selected school characteristics: United States, 2017\u201318",
-            "modified": "2023-07-07T18:11:39.414405",
-            "accessLevel": "public",
-            "identifier": "2b812d66-a93d-440c-934a-f0bc42856aa2",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -50530,30 +50498,41 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Number and percentage distribution of private schools, students, and full-time equivalent (FTE) teachers, by religious or nonsectarian orientation of school: United States, 2017\u201318"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "Table 4. Number and percentage distribution of private schools, by urbanicity type and selected school characteristics: United States, 2017\u201318",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Table 4. Number and percentage distribution of private schools, by urbanicity type and selected school characteristics: United States, 2017\u201318",
                     "description": "n/a",
-                    "downloadURL": "https://data.ed.gov/dataset/f7cb51a3-1a38-4edb-844c-d40d0aeca370/resource/e1ff0c64-95a4-4284-b8c9-df8d705d17b6/download/table04fl1718.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/f7cb51a3-1a38-4edb-844c-d40d0aeca370/resource/e1ff0c64-95a4-4284-b8c9-df8d705d17b6/download/table04fl1718.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 4. Number and percentage distribution of private schools, by urbanicity type and selected school characteristics: United States, 2017\u201318"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Table 4. Number and percentage distribution of private schools, by urbanicity type and selected school characteristics: United States, 2017\u201318",
                     "description": "n/a",
-                    "downloadURL": "https://data.ed.gov/dataset/f7cb51a3-1a38-4edb-844c-d40d0aeca370/resource/7c201a15-1a00-47fb-8873-dae6c5642f94/download/table04fl1718_se.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/f7cb51a3-1a38-4edb-844c-d40d0aeca370/resource/7c201a15-1a00-47fb-8873-dae6c5642f94/download/table04fl1718_se.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 4. Number and percentage distribution of private schools, by urbanicity type and selected school characteristics: United States, 2017\u201318"
                 }
             ],
+            "identifier": "2b812d66-a93d-440c-934a-f0bc42856aa2",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "education",
@@ -50567,28 +50546,17 @@
                 "teachers",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:11:39.414405",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Native American-Serving Nontribal Institutions Program",
-            "description": "This program provides grants and related assistance to Native American-serving, nontribal institutions to enable such institutions to improve and expand their capacity to serve Native Americans and low-income individuals.",
-            "modified": "2023-07-07T18:10:10.457078",
-            "accessLevel": "public",
-            "identifier": "7cb27bf9-dc2a-41e6-b482-5e98800afe80",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
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
@@ -50603,30 +50571,41 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Number and percentage distribution of private schools, by urbanicity type and selected school characteristics: United States, 2017\u201318"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "This program provides grants and related assistance to Native American-serving, nontribal institutions to enable such institutions to improve and expand their capacity to serve Native Americans and low-income individuals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "DOC",
-                    "title": "nasnti-abstracts2015.doc",
                     "description": "nasnti-abstracts2015.doc",
-                    "downloadURL": "https://data.ed.gov/dataset/02d94a28-0245-43af-8f3a-20e2dc3f29d1/resource/cc5f0030-1068-4889-84e3-274b8502a086/download/nasnti-abstracts2015.doc"
+                    "downloadURL": "https://data.ed.gov/dataset/02d94a28-0245-43af-8f3a-20e2dc3f29d1/resource/cc5f0030-1068-4889-84e3-274b8502a086/download/nasnti-abstracts2015.doc",
+                    "format": "DOC",
+                    "mediaType": "application/msword",
+                    "title": "nasnti-abstracts2015.doc"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "DOC",
-                    "title": "nasntigrantees2015.doc",
                     "description": "nasntigrantees2015.doc",
-                    "downloadURL": "https://data.ed.gov/dataset/02d94a28-0245-43af-8f3a-20e2dc3f29d1/resource/e5f203d8-94e0-4f52-a354-147a6a54a74f/download/nasntigrantees2015.doc"
+                    "downloadURL": "https://data.ed.gov/dataset/02d94a28-0245-43af-8f3a-20e2dc3f29d1/resource/e5f203d8-94e0-4f52-a354-147a6a54a74f/download/nasntigrantees2015.doc",
+                    "format": "DOC",
+                    "mediaType": "application/msword",
+                    "title": "nasntigrantees2015.doc"
                 }
             ],
+            "identifier": "7cb27bf9-dc2a-41e6-b482-5e98800afe80",
             "keyword": [
                 "american-indian",
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
@@ -50642,25 +50621,17 @@
                 "title-iii",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2023-07-07T18:10:10.457078",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Native American and Alaska Native Children in School Program | NCELA",
-            "description": "Native American and Alaska Native Children in School Program | NCELA",
-            "modified": "2023-07-07T18:09:00.940573",
-            "accessLevel": "public",
-            "identifier": "537ec256-7700-403a-9b86-954b9bb48eed",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of English Language Acquisition (OELA)",
+                "name": "Office of Postsecondary Education (OPE)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -50673,55 +50644,56 @@
                             }
                         }
                     }
+                }
+            },
+            "spatial": "United States",
+            "title": "Native American-Serving Nontribal Institutions Program"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:oela@ed.gov"
             },
+            "description": "Native American and Alaska Native Children in School Program | NCELA",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2013 List of NAM Grantees",
                     "description": "2013 List of NAM Grantees",
-                    "downloadURL": "https://data.ed.gov/dataset/aa35c232-0049-4f8a-b468-8b69390c10e8/resource/e3f9566b-3e99-4c8b-9d19-1765606c418a/download/2013grantlist.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/aa35c232-0049-4f8a-b468-8b69390c10e8/resource/e3f9566b-3e99-4c8b-9d19-1765606c418a/download/2013grantlist.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2013 List of NAM Grantees"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "2013 List of NAM Grantees",
                     "description": "2013 List of NAM Grantees",
-                    "downloadURL": "https://data.ed.gov/dataset/aa35c232-0049-4f8a-b468-8b69390c10e8/resource/c2090858-cd47-4c6e-81f5-87ccfddc94b6/download/2013grantlist.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/aa35c232-0049-4f8a-b468-8b69390c10e8/resource/c2090858-cd47-4c6e-81f5-87ccfddc94b6/download/2013grantlist.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2013 List of NAM Grantees"
                 }
             ],
+            "identifier": "537ec256-7700-403a-9b86-954b9bb48eed",
             "keyword": [
                 "edgov",
                 "fd01e0d7-b479-4a0b-ab9a-a8b1b5274d71",
                 "oela",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:09:00.940573",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Media Advisories--Department of Education",
-            "description": "Archived: This page provides the most recent media advisories from the US Department of Education.",
-            "modified": "2023-07-07T18:05:12.550144",
-            "accessLevel": "public",
-            "identifier": "ae13d471-526c-46db-9b2c-c11f3a113d08",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Communications and Outreach (OCO)",
+                "name": "Office of English Language Acquisition (OELA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -50735,22 +50707,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Native American and Alaska Native Children in School Program | NCELA"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:oco@ed.gov"
             },
+            "description": "Archived: This page provides the most recent media advisories from the US Department of Education.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "media-advisories",
                     "description": "Press Room\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\n\n\n\n\n\t\t\t\t\t\t\t\t\t\n\n            \n -",
-                    "downloadURL": "https://data.ed.gov/dataset/ab30f3bc-8bd1-46a3-b4a1-d263007c402c/resource/bb41f659-79f1-4a4e-bb51-c912222ba1e0/download/media-advisories.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/ab30f3bc-8bd1-46a3-b4a1-d263007c402c/resource/bb41f659-79f1-4a4e-bb51-c912222ba1e0/download/media-advisories.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "media-advisories"
                 }
             ],
+            "identifier": "ae13d471-526c-46db-9b2c-c11f3a113d08",
             "keyword": [
                 "49cf3636-972f-49b4-8bfc-2d020a10aa57",
                 "education",
@@ -50759,28 +50742,14 @@
                 "public-relations",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:05:12.550144",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Lessons Learned from FIPSE Projects II- Home Page",
-            "description": "Archived:  The Fund for the Improvement of Postsecondary Education (FIPSE) supports pilot tests of new ideas in postsecondary education. This book describes such issues as how to assess student learning objectively while protecting faculty ownership of the assessment process; whether and how to use computers in the teaching of writing, music, and other humanities subjects; how to raise minority--and majority--achievement in math and science at a reasonable cost; and more.",
-            "modified": "2023-07-07T18:04:21.971837",
-            "accessLevel": "public",
-            "identifier": "9b67f3b0-1ebd-4d11-a165-97e18906e350",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                "name": "Office of Communications and Outreach (OCO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -50793,24 +50762,34 @@
                         }
                     }
                 }
-                }
             },
+            "spatial": "United States",
+            "title": "Media Advisories--Department of Education"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "Archived:  The Fund for the Improvement of Postsecondary Education (FIPSE) supports pilot tests of new ideas in postsecondary education. This book describes such issues as how to assess student learning objectively while protecting faculty ownership of the assessment process; whether and how to use computers in the teaching of writing, music, and other humanities subjects; how to raise minority--and majority--achievement in math and science at a reasonable cost; and more.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "For the user's convenience we have also created an",
                     "description": "For the user's convenience we have also created an - ASCII version of this  document and compressed it (118K)",
-                    "downloadURL": "https://data.ed.gov/dataset/b480477a-e41b-47bd-8e7a-e1163b72655f/resource/03b5e738-d0b3-4385-b54d-722403a84f15/download/lessonii.zip"
+                    "downloadURL": "https://data.ed.gov/dataset/b480477a-e41b-47bd-8e7a-e1163b72655f/resource/03b5e738-d0b3-4385-b54d-722403a84f15/download/lessonii.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "For the user's convenience we have also created an"
                 }
             ],
+            "identifier": "9b67f3b0-1ebd-4d11-a165-97e18906e350",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "educational-assessment",
@@ -50824,22 +50803,11 @@
                 "programs",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:04:21.971837",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Legislation -- Minorities and Retirement Security Program",
-            "description": "This page lists statutes, regulations, legislation, policy guidance, and flexibility provisions for the Minorities and Retirement Security (MRS) Program.",
-            "modified": "2023-07-07T18:03:26.645701",
-            "accessLevel": "public",
-            "identifier": "e3edbca4-b91c-43b8-a99d-069eab67b5eb",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -50860,22 +50828,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Lessons Learned from FIPSE Projects II- Home Page"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "This page lists statutes, regulations, legislation, policy guidance, and flexibility provisions for the Minorities and Retirement Security (MRS) Program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/xml",
-                    "format": "XML",
-                    "title": "Regulations:",
                     "description": "Regulations: - (a) The",
-                    "downloadURL": "http://www.gpo.gov/fdsys/pkg/CFR-2012-title20-vol2/xml/CFR-2012-title20-vol2-part435.xml"
+                    "downloadURL": "http://www.gpo.gov/fdsys/pkg/CFR-2012-title20-vol2/xml/CFR-2012-title20-vol2-part435.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml",
+                    "title": "Regulations:"
                 }
             ],
+            "identifier": "e3edbca4-b91c-43b8-a99d-069eab67b5eb",
             "keyword": [
                 "black-colleges",
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
@@ -50891,25 +50870,17 @@
                 "retirement-security",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:03:26.645701",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Information Correction Requests and Appeals - Information Quality Guidelines",
-            "description": "Reports on requests for corrections received.",
-            "modified": "2023-07-07T18:02:39.853791",
-            "accessLevel": "public",
-            "identifier": "47a0037b-edab-4e1f-bb53-ce3326c6ea1d",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Planning, Evaluation and Policy Development (OPEPD)",
+                "name": "Office of Postsecondary Education (OPE)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -50922,71 +50893,83 @@
                             }
                         }
                     }
+                }
+            },
+            "spatial": "United States",
+            "title": "Legislation -- Minorities and Retirement Security Program"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:odp@ed.gov"
             },
+            "description": "Reports on requests for corrections received.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Overview",
                     "description": "Laws &amp; Guidance\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\n\n\n\t\t\n\t\t\t\nGENERAL\n\n\n\t\t\t\t\t\t\t\t\t\n\n            \n - Overview",
-                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/60d29c5b-2f86-414d-a154-c1b8e2591a19/download/fy17iq-reports.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/60d29c5b-2f86-414d-a154-c1b8e2591a19/download/fy17iq-reports.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Overview"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Report\n  on Requests for Corrections Received (0 requests) (",
                     "description": "Overview - Report\n  on Requests for Corrections Received (0 requests) (",
-                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/1c1cbf9e-db2a-41fb-bfb1-b8a2c39611f8/download/2014-ed-iq-annual-report.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/1c1cbf9e-db2a-41fb-bfb1-b8a2c39611f8/download/2014-ed-iq-annual-report.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Report\n  on Requests for Corrections Received (0 requests) ("
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Report\n  on Requests for Corrections Received (0 requests)",
                     "description": "Overview - Report\n  on Requests for Corrections Received (0 requests)",
-                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/a4989507-65d7-46e7-88ee-10eadeb139db/download/2013-ed-iq-annual-report.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/a4989507-65d7-46e7-88ee-10eadeb139db/download/2013-ed-iq-annual-report.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Report\n  on Requests for Corrections Received (0 requests)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Report\n  on Requests for Corrections Received (0 requests) (",
                     "description": "Overview - Report\n  on Requests for Corrections Received (0 requests) (",
-                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/1dc0517b-ba4e-4016-b75d-6bdb954a4f63/download/2012-ed-iq-annual-report.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/1dc0517b-ba4e-4016-b75d-6bdb954a4f63/download/2012-ed-iq-annual-report.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Report\n  on Requests for Corrections Received (0 requests) ("
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Report\n  on Requests for Corrections Received (0 requests)",
                     "description": "Overview - Report\n  on Requests for Corrections Received (0 requests)",
-                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/c790aea1-8861-4695-9aa4-f27c3668bf40/download/2010_ed_iq_annual_report.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/c790aea1-8861-4695-9aa4-f27c3668bf40/download/2010_ed_iq_annual_report.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Report\n  on Requests for Corrections Received (0 requests)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Report\n  on Requests for Corrections Received (0 requests) (",
                     "description": "Overview - Report\n  on Requests for Corrections Received (0 requests) (",
-                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/e57786fd-f446-4b42-ae36-fe6f1a38925f/download/2008_ed_iq_annual_report.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/e57786fd-f446-4b42-ae36-fe6f1a38925f/download/2008_ed_iq_annual_report.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Report\n  on Requests for Corrections Received (0 requests) ("
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Report\n  on Requests for Corrections Received (0 requests) (",
                     "description": "Overview - Report\n  on Requests for Corrections Received (0 requests) (",
-                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/35d5903d-41b2-411f-b830-30d5d0f990c6/download/2007_ed_iq_annual_report.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8c30ce9d-241a-443a-b7e6-dbae50ea20e3/resource/35d5903d-41b2-411f-b830-30d5d0f990c6/download/2007_ed_iq_annual_report.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Report\n  on Requests for Corrections Received (0 requests) ("
                 }
             ],
+            "identifier": "47a0037b-edab-4e1f-bb53-ce3326c6ea1d",
             "keyword": [
                 "__",
                 "fcbc6e9b-a57b-46d9-8246-211eb2309029",
@@ -50995,23 +50978,15 @@
                 "opepd",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:02:39.853791",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Information About the Department's Previous Retrospective Review",
-            "description": "As part of its implementation of Executive Order 13563, \"Improving Regulation and Regulatory Review,\" the Department of Education sought comments and information from interested parties on the Department's \"Preliminary Plan for Retrospective Analysis of Existing Rules\".",
-            "modified": "2023-07-07T18:01:40.567484",
-            "accessLevel": "public",
-            "identifier": "cd482978-a75d-4bdd-9340-bc6171c53c91",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Planning, Evaluation and Policy Development (OPEPD)",
+                "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
                     "subOrganizationOf": {
@@ -51022,39 +50997,51 @@
                             "name": "U.S. Government"
                         }
                     }
+                }
             },
+            "spatial": "United States",
+            "title": "Information Correction Requests and Appeals - Information Quality Guidelines"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:os@ed.gov"
             },
+            "description": "As part of its implementation of Executive Order 13563, \"Improving Regulation and Regulatory Review,\" the Department of Education sought comments and information from interested parties on the Department's \"Preliminary Plan for Retrospective Analysis of Existing Rules\".",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Retrospective Review Report (July 8, 2016)",
                     "description": "Retrospective Review Report (July 8, 2016) - Retrospective Review Report (July 8, 2016)",
-                    "downloadURL": "https://data.ed.gov/dataset/3776bdcc-7458-43cf-81f6-0353e9293b73/resource/60d256b7-99df-4782-af53-2c8cbe7572aa/download/retrospective-review-plan-report-07082016.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3776bdcc-7458-43cf-81f6-0353e9293b73/resource/60d256b7-99df-4782-af53-2c8cbe7572aa/download/retrospective-review-plan-report-07082016.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Retrospective Review Report (July 8, 2016)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Retrospective Review Report (July 13, 2015)",
                     "description": "Retrospective Review Report (July 8, 2016) - Retrospective Review Report (July 13, 2015)",
-                    "downloadURL": "https://data.ed.gov/dataset/3776bdcc-7458-43cf-81f6-0353e9293b73/resource/451365ad-d8b7-45e2-aa35-0c9bdfa4edc0/download/retrospective-review-plan-report-20150713.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3776bdcc-7458-43cf-81f6-0353e9293b73/resource/451365ad-d8b7-45e2-aa35-0c9bdfa4edc0/download/retrospective-review-plan-report-20150713.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Retrospective Review Report (July 13, 2015)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Retrospective Review Report (March 17, 2015)",
                     "description": "Retrospective Review Report (July 8, 2016) - Retrospective Review Report (March 17, 2015)",
-                    "downloadURL": "https://data.ed.gov/dataset/3776bdcc-7458-43cf-81f6-0353e9293b73/resource/e339de86-ab72-416b-b514-9586a7d51eab/download/retrospective-review-plan-report-20150317.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3776bdcc-7458-43cf-81f6-0353e9293b73/resource/e339de86-ab72-416b-b514-9586a7d51eab/download/retrospective-review-plan-report-20150317.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Retrospective Review Report (March 17, 2015)"
                 }
             ],
+            "identifier": "cd482978-a75d-4bdd-9340-bc6171c53c91",
             "keyword": [
                 "2eea0c24-f950-40cc-bf91-9661d805523b",
                 "federal-regulation",
@@ -51063,29 +51050,12 @@
                 "policy",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:01:40.567484",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Awards -- Hispanic-Serving Institutions Division - Home Page",
-            "description": "The Hispanic-Serving Institutions (HSI) Division is a component of the OPE Institutional Service program office.  This division provides grant funding to institutions of higher education to assist with strengthening institutional programs, facilities, and services to expand the educational opportunities for Hispanic Americans and other underrepresented populations.",
-            "modified": "2023-07-07T18:00:51.969427",
-            "accessLevel": "public",
-            "identifier": "760c78ce-c556-4df9-9e9a-ed377d3f01bc",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
-                    "subOrganizationOf": {
                 "@type": "org:Organization",
                 "name": "Office of the Secretary (OS)",
                 "subOrganizationOf": {
@@ -51096,33 +51066,42 @@
                         "name": "U.S. Government"
                     }
                 }
-                    }
-                }
             },
+            "spatial": "United States",
+            "title": "Information About the Department's Previous Retrospective Review"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "The Hispanic-Serving Institutions (HSI) Division is a component of the OPE Institutional Service program office.  This division provides grant funding to institutions of higher education to assist with strengthening institutional programs, facilities, and services to expand the educational opportunities for Hispanic Americans and other underrepresented populations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "2018 Eligibility Matrix",
                     "description": "2018 Eligibility Matrix -",
-                    "downloadURL": "https://data.ed.gov/dataset/8650565f-df8b-4098-bd76-978a23448134/resource/d6871e96-0d71-4012-99c3-956fd5cfc68a/download/copyof2018eligibilitymatrix.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/8650565f-df8b-4098-bd76-978a23448134/resource/d6871e96-0d71-4012-99c3-956fd5cfc68a/download/copyof2018eligibilitymatrix.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2018 Eligibility Matrix"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "This is the current list of",
                     "description": "This is the current list of - Eligible Hispanic-Serving Institutions",
-                    "downloadURL": "https://data.ed.gov/dataset/8650565f-df8b-4098-bd76-978a23448134/resource/67e420fd-2971-4391-b61f-de5893de68ec/download/hsi-eligibles-2016.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8650565f-df8b-4098-bd76-978a23448134/resource/67e420fd-2971-4391-b61f-de5893de68ec/download/hsi-eligibles-2016.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "This is the current list of"
                 }
             ],
+            "identifier": "760c78ce-c556-4df9-9e9a-ed377d3f01bc",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "dhsi",
@@ -51144,22 +51123,11 @@
                 "title-v-part-b",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T18:00:51.969427",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Grantee Performance and Efficiency Measures Analyses:  2005-06 and 2006-07",
-            "description": "This archived file contains an explanation of the grantee-level analysis data for academic years 2005-06 and 2006-07 under the Teacher Quality Enhancement Grants Program.",
-            "modified": "2023-07-07T17:58:52.733853",
-            "accessLevel": "public",
-            "identifier": "ee518704-0bbd-43e6-b88a-69c4245c9b77",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -51180,30 +51148,41 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Awards -- Hispanic-Serving Institutions Division - Home Page"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "This archived file contains an explanation of the grantee-level analysis data for academic years 2005-06 and 2006-07 under the Teacher Quality Enhancement Grants Program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Grantee Analysis and Summary, 2005-06:",
                     "description": "Grantee Analysis and Summary, 2005-06: -",
-                    "downloadURL": "https://data.ed.gov/dataset/b0ff0b69-4816-444e-8f64-f8f6ddce6572/resource/dfb7e8e7-5391-4e71-85ce-e3f6cec029e7/download/tqeanalysis0506.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/b0ff0b69-4816-444e-8f64-f8f6ddce6572/resource/dfb7e8e7-5391-4e71-85ce-e3f6cec029e7/download/tqeanalysis0506.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Grantee Analysis and Summary, 2005-06:"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Grantee Analysis and Summary, 2006-07:",
                     "description": "Grantee Analysis and Summary, 2006-07: -",
-                    "downloadURL": "https://data.ed.gov/dataset/b0ff0b69-4816-444e-8f64-f8f6ddce6572/resource/643c7808-77a9-4893-aafc-910f618a8766/download/tqeanalysis0607.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/b0ff0b69-4816-444e-8f64-f8f6ddce6572/resource/643c7808-77a9-4893-aafc-910f618a8766/download/tqeanalysis0607.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Grantee Analysis and Summary, 2006-07:"
                 }
             ],
+            "identifier": "ee518704-0bbd-43e6-b88a-69c4245c9b77",
             "keyword": [
                 "__",
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
@@ -51218,25 +51197,17 @@
                 "teacher-quality",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T17:58:52.733853",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY 2012 Budget Summary:  Table of Contents",
-            "description": "The FY 2012 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2012 Budget on the programs and activities of the Department.",
-            "modified": "2023-07-07T17:58:04.164347",
-            "accessLevel": "public",
-            "identifier": "16ecf7da-366b-4680-9c0a-f191799bd42a",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Finance and Operations (OFO)",
+                "name": "Office of Postsecondary Education (OPE)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -51249,47 +51220,59 @@
                             }
                         }
                     }
+                }
+            },
+            "spatial": "United States",
+            "title": "Grantee Performance and Efficiency Measures Analyses:  2005-06 and 2006-07"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "The FY 2012 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2012 Budget on the programs and activities of the Department.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 1:   Summary of Discretionary Funds, in",
                     "description": "PDF [29KB] - Appendix 1:   Summary of Discretionary Funds, in",
-                    "downloadURL": "https://data.ed.gov/dataset/469b554f-1dfc-4548-8b5f-18d9ba6394a1/resource/3ad6c7e4-9870-404a-92fc-72aef599b08c/download/appendix1.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/469b554f-1dfc-4548-8b5f-18d9ba6394a1/resource/3ad6c7e4-9870-404a-92fc-72aef599b08c/download/appendix1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 1:   Summary of Discretionary Funds, in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 3:   Summary of Mandatory Funds Funds, in",
                     "description": "PDF [29KB] - Appendix 3:   Summary of Mandatory Funds Funds, in",
-                    "downloadURL": "https://data.ed.gov/dataset/469b554f-1dfc-4548-8b5f-18d9ba6394a1/resource/7d26032b-211c-476b-ba46-e5f5506ce6ba/download/appendix3.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/469b554f-1dfc-4548-8b5f-18d9ba6394a1/resource/7d26032b-211c-476b-ba46-e5f5506ce6ba/download/appendix3.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 3:   Summary of Mandatory Funds Funds, in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 4: Advance Appropriations for Department of Education, in",
                     "description": "PDF [29KB] - Appendix 4: Advance Appropriations for Department of Education, in",
-                    "downloadURL": "https://data.ed.gov/dataset/469b554f-1dfc-4548-8b5f-18d9ba6394a1/resource/f6e6a336-2128-4c39-b5b4-80ad7bf52577/download/appendix4.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/469b554f-1dfc-4548-8b5f-18d9ba6394a1/resource/f6e6a336-2128-4c39-b5b4-80ad7bf52577/download/appendix4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 4: Advance Appropriations for Department of Education, in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 6:  Detailed Budget Table by Program, in",
                     "description": "PDF [29KB] - Appendix 6:  Detailed Budget Table by Program, in",
-                    "downloadURL": "https://data.ed.gov/dataset/469b554f-1dfc-4548-8b5f-18d9ba6394a1/resource/78195948-9226-415d-bf44-78cf0969ac9f/download/appendix6.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/469b554f-1dfc-4548-8b5f-18d9ba6394a1/resource/78195948-9226-415d-bf44-78cf0969ac9f/download/appendix6.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 6:  Detailed Budget Table by Program, in"
                 }
             ],
+            "identifier": "16ecf7da-366b-4680-9c0a-f191799bd42a",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "budgets",
@@ -51302,22 +51285,11 @@
                 "presidents-budget-request",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T17:58:04.164347",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY 2011 Budget Summary:  Table of Contents",
-            "description": "The FY 2011 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2011 Budget on the programs and activities of the Department.",
-            "modified": "2023-07-07T15:38:41.443000",
-            "accessLevel": "public",
-            "identifier": "9e1a5cbc-c5e6-4ca7-a3c1-876c67f4c952",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -51334,38 +51306,49 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "FY 2012 Budget Summary:  Table of Contents"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "The FY 2011 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2011 Budget on the programs and activities of the Department.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 1:   Summary of Discretionary Funds, Fiscal Years 2009-2011, in",
                     "description": "PDF [11KB] - Appendix 1:   Summary of Discretionary Funds, Fiscal Years 2009-2011, in",
-                    "downloadURL": "https://data.ed.gov/dataset/9516b7ce-b323-4e38-b24a-e6960687884e/resource/105cbc92-bbc2-403c-91f0-f95ea54d82d0/download/appendix1.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9516b7ce-b323-4e38-b24a-e6960687884e/resource/105cbc92-bbc2-403c-91f0-f95ea54d82d0/download/appendix1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 1:   Summary of Discretionary Funds, Fiscal Years 2009-2011, in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 2: Advance Appropriations for Department of Education, in",
                     "description": "PDF [11KB] - Appendix 2: Advance Appropriations for Department of Education, in",
-                    "downloadURL": "https://data.ed.gov/dataset/9516b7ce-b323-4e38-b24a-e6960687884e/resource/ab0afbd8-46e9-44d4-89f8-ca9abac80213/download/appendix2.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9516b7ce-b323-4e38-b24a-e6960687884e/resource/ab0afbd8-46e9-44d4-89f8-ca9abac80213/download/appendix2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 2: Advance Appropriations for Department of Education, in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 4:  Detailed Budget Table by Program, in",
                     "description": "PDF [11KB] - Appendix 4:  Detailed Budget Table by Program, in",
-                    "downloadURL": "https://data.ed.gov/dataset/9516b7ce-b323-4e38-b24a-e6960687884e/resource/61a4238f-5236-4726-9017-4f5d9de2ed3b/download/appendix4.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9516b7ce-b323-4e38-b24a-e6960687884e/resource/61a4238f-5236-4726-9017-4f5d9de2ed3b/download/appendix4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 4:  Detailed Budget Table by Program, in"
                 }
             ],
+            "identifier": "9e1a5cbc-c5e6-4ca7-a3c1-876c67f4c952",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "budgets",
@@ -51378,22 +51361,11 @@
                 "presidents-budget-request",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T15:38:41.443000",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY 2010 Budget Summary:  Table of Contents",
-            "description": "The FY 2010 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2010 Budget on the programs and activities of the Department.",
-            "modified": "2023-07-07T15:37:17.222453",
-            "accessLevel": "public",
-            "identifier": "ef00ad2b-c0c3-4685-a81b-3294c864c0f5",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -51410,38 +51382,49 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "FY 2011 Budget Summary:  Table of Contents"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "The FY 2010 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2010 Budget on the programs and activities of the Department.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 1:  American Recovery and Reinvestment Act (ARRA) Funding in",
                     "description": "PDF [8KB] - Appendix 1:  American Recovery and Reinvestment Act (ARRA) Funding in",
-                    "downloadURL": "https://data.ed.gov/dataset/1d8edb5d-4ff7-46d6-a92d-6978c54e429f/resource/5a984d5d-d746-4183-94e9-c134decc8748/download/appendix1.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/1d8edb5d-4ff7-46d6-a92d-6978c54e429f/resource/5a984d5d-d746-4183-94e9-c134decc8748/download/appendix1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 1:  American Recovery and Reinvestment Act (ARRA) Funding in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 2:  Summary of Discretionary Funds, Fiscal Years 2008-2010, in",
                     "description": "PDF [8KB] - Appendix 2:  Summary of Discretionary Funds, Fiscal Years 2008-2010, in",
-                    "downloadURL": "https://data.ed.gov/dataset/1d8edb5d-4ff7-46d6-a92d-6978c54e429f/resource/dfc3ef0f-7cf4-4147-a6d0-235d61b2a367/download/appendix2.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/1d8edb5d-4ff7-46d6-a92d-6978c54e429f/resource/dfc3ef0f-7cf4-4147-a6d0-235d61b2a367/download/appendix2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 2:  Summary of Discretionary Funds, Fiscal Years 2008-2010, in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 4:  Detailed Budget Table by Program in",
                     "description": "PDF [8KB] - Appendix 4:  Detailed Budget Table by Program in",
-                    "downloadURL": "https://data.ed.gov/dataset/1d8edb5d-4ff7-46d6-a92d-6978c54e429f/resource/6702ac1d-7907-4f76-ad46-964ef3e03d24/download/appendix4.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/1d8edb5d-4ff7-46d6-a92d-6978c54e429f/resource/6702ac1d-7907-4f76-ad46-964ef3e03d24/download/appendix4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 4:  Detailed Budget Table by Program in"
                 }
             ],
+            "identifier": "ef00ad2b-c0c3-4685-a81b-3294c864c0f5",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "budgets",
@@ -51454,22 +51437,11 @@
                 "presidents-budget-request",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T15:37:17.222453",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY 2009 Budget Summary:  Table of Contents",
-            "description": "The FY 2009 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2009 Budget on the programs and activities of the Department.",
-            "modified": "2023-07-07T15:35:48.251442",
-            "accessLevel": "public",
-            "identifier": "121a514b-2c2e-48da-90c7-cb48e5c39b70",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -51486,38 +51458,49 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "FY 2010 Budget Summary:  Table of Contents"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "The FY 2009 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2009 Budget on the programs and activities of the Department.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2009 in",
                     "description": "PDF [14KB] - Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2009 in",
-                    "downloadURL": "https://data.ed.gov/dataset/d182ccac-3b1c-4d02-b4c7-de3adfe042b3/resource/86453754-ecfd-42d9-8d94-743330cc967e/download/appendix1.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d182ccac-3b1c-4d02-b4c7-de3adfe042b3/resource/86453754-ecfd-42d9-8d94-743330cc967e/download/appendix1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2009 in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 2:  PART Ratings of ED Programs in",
                     "description": "PDF [14KB] - Appendix 2:  PART Ratings of ED Programs in",
-                    "downloadURL": "https://data.ed.gov/dataset/d182ccac-3b1c-4d02-b4c7-de3adfe042b3/resource/f70952f0-e818-492f-85b6-76dacc5490a7/download/appendix2.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d182ccac-3b1c-4d02-b4c7-de3adfe042b3/resource/f70952f0-e818-492f-85b6-76dacc5490a7/download/appendix2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 2:  PART Ratings of ED Programs in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 4:  Detailed Budget Table by Program in",
                     "description": "PDF [14KB] - Appendix 4:  Detailed Budget Table by Program in",
-                    "downloadURL": "https://data.ed.gov/dataset/d182ccac-3b1c-4d02-b4c7-de3adfe042b3/resource/93e2cf29-a232-45e0-ac7a-5ae4279d0f0e/download/appendix4.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d182ccac-3b1c-4d02-b4c7-de3adfe042b3/resource/93e2cf29-a232-45e0-ac7a-5ae4279d0f0e/download/appendix4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 4:  Detailed Budget Table by Program in"
                 }
             ],
+            "identifier": "121a514b-2c2e-48da-90c7-cb48e5c39b70",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "budgets",
@@ -51530,22 +51513,11 @@
                 "presidents-budget-request",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T15:35:48.251442",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY 2008 Budget Summary: Table of Contents",
-            "description": "The FY 2008 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2008 Budget on the programs and activities of the Department.",
-            "modified": "2023-07-07T15:34:47.558404",
-            "accessLevel": "public",
-            "identifier": "5765f28c-a65d-4e83-b2ee-75ea4ad39ca3",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -51562,38 +51534,49 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "FY 2009 Budget Summary:  Table of Contents"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "The FY 2008 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2008 Budget on the programs and activities of the Department.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2008 in",
                     "description": "PDF [12KB] - Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2008 in",
-                    "downloadURL": "https://data.ed.gov/dataset/8fa75d9b-bdc4-4c5a-8c22-9daa645b83aa/resource/58884eef-bf6d-4303-9799-fb184bc65688/download/appendix1.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8fa75d9b-bdc4-4c5a-8c22-9daa645b83aa/resource/58884eef-bf6d-4303-9799-fb184bc65688/download/appendix1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2008 in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 2:  PART Ratings of ED Programs in",
                     "description": "PDF [12KB] - Appendix 2:  PART Ratings of ED Programs in",
-                    "downloadURL": "https://data.ed.gov/dataset/8fa75d9b-bdc4-4c5a-8c22-9daa645b83aa/resource/6ac60e24-d38d-4bc6-a590-83ae1ba224fb/download/appendix2.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8fa75d9b-bdc4-4c5a-8c22-9daa645b83aa/resource/6ac60e24-d38d-4bc6-a590-83ae1ba224fb/download/appendix2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 2:  PART Ratings of ED Programs in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 4:  Detailed Budget Table by Program in",
                     "description": "PDF [12KB] - Appendix 4:  Detailed Budget Table by Program in",
-                    "downloadURL": "https://data.ed.gov/dataset/8fa75d9b-bdc4-4c5a-8c22-9daa645b83aa/resource/1d01b085-c119-427d-ba62-d8d8d20ed9b1/download/appendix4.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/8fa75d9b-bdc4-4c5a-8c22-9daa645b83aa/resource/1d01b085-c119-427d-ba62-d8d8d20ed9b1/download/appendix4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 4:  Detailed Budget Table by Program in"
                 }
             ],
+            "identifier": "5765f28c-a65d-4e83-b2ee-75ea4ad39ca3",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "budgets",
@@ -51606,22 +51589,11 @@
                 "presidents-budget-request",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T15:34:47.558404",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY 2007 Budget Summary: Table of Contents",
-            "description": "The Archived FY 2007 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2007 Budget on the programs and activities of the Department.",
-            "modified": "2023-07-07T15:28:28.411094",
-            "accessLevel": "public",
-            "identifier": "742dad0f-9838-4024-ab9d-601588dc3920",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -51638,38 +51610,49 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "FY 2008 Budget Summary: Table of Contents"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "The Archived FY 2007 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2007 Budget on the programs and activities of the Department.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2007 in",
                     "description": "PDF [12KB] - Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2007 in",
-                    "downloadURL": "https://data.ed.gov/dataset/2dc90a21-734c-4e84-806a-93a65170593d/resource/81f0ceb1-66b0-4e23-ac14-680075699a67/download/appendix1.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2dc90a21-734c-4e84-806a-93a65170593d/resource/81f0ceb1-66b0-4e23-ac14-680075699a67/download/appendix1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2007 in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 2:  PART Ratings of ED Programs in",
                     "description": "PDF [12KB] - Appendix 2:  PART Ratings of ED Programs in",
-                    "downloadURL": "https://data.ed.gov/dataset/2dc90a21-734c-4e84-806a-93a65170593d/resource/68baec3c-5da4-47e6-b53a-68398190f815/download/appendix2.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2dc90a21-734c-4e84-806a-93a65170593d/resource/68baec3c-5da4-47e6-b53a-68398190f815/download/appendix2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 2:  PART Ratings of ED Programs in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 4:  Detailed Budget Table by Program in",
                     "description": "PDF [12KB] - Appendix 4:  Detailed Budget Table by Program in",
-                    "downloadURL": "https://data.ed.gov/dataset/2dc90a21-734c-4e84-806a-93a65170593d/resource/602c6fbd-e34d-40d9-8f64-ddbde4476911/download/appendix4.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2dc90a21-734c-4e84-806a-93a65170593d/resource/602c6fbd-e34d-40d9-8f64-ddbde4476911/download/appendix4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 4:  Detailed Budget Table by Program in"
                 }
             ],
+            "identifier": "742dad0f-9838-4024-ab9d-601588dc3920",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "budgets",
@@ -51682,22 +51665,11 @@
                 "presidents-budget-request",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T15:28:28.411094",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FY 2006 Budget Summary:  Table of Contents",
-            "description": "The FY 2006 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2006 Budget on the programs and activities of the Department.",
-            "modified": "2023-07-07T14:20:24.416296",
-            "accessLevel": "public",
-            "identifier": "582597e0-207d-4dea-8feb-cfe472795fe8",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -51714,38 +51686,49 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "FY 2007 Budget Summary: Table of Contents"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "The FY 2006 Education Budget Summary provides program information and detailed budget tables showing the effect of the FY 2006 Budget on the programs and activities of the Department.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2006 in",
                     "description": "PDF - Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2006 in",
-                    "downloadURL": "https://data.ed.gov/dataset/b163c87d-2914-466b-9d69-b5600fb02205/resource/6178567d-d3eb-4b0a-89e4-7b1b1e6d8d96/download/appendix1.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/b163c87d-2914-466b-9d69-b5600fb02205/resource/6178567d-d3eb-4b0a-89e4-7b1b1e6d8d96/download/appendix1.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 1:  Summary of Discretionary Funds, Fiscal Years 2001-2006 in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 2:  PART Ratings of ED Programs in",
                     "description": "PDF - Appendix 2:  PART Ratings of ED Programs in",
-                    "downloadURL": "https://data.ed.gov/dataset/b163c87d-2914-466b-9d69-b5600fb02205/resource/9b16d578-ef3a-4f8a-a460-240ebf61a8e8/download/appendix2.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/b163c87d-2914-466b-9d69-b5600fb02205/resource/9b16d578-ef3a-4f8a-a460-240ebf61a8e8/download/appendix2.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 2:  PART Ratings of ED Programs in"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Appendix 4:  Detailed Budget Table by Program in",
                     "description": "PDF - Appendix 4:  Detailed Budget Table by Program in",
-                    "downloadURL": "https://data.ed.gov/dataset/b163c87d-2914-466b-9d69-b5600fb02205/resource/035030e4-da20-4642-b50a-47d1d5586546/download/appendix4.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/b163c87d-2914-466b-9d69-b5600fb02205/resource/035030e4-da20-4642-b50a-47d1d5586546/download/appendix4.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Appendix 4:  Detailed Budget Table by Program in"
                 }
             ],
+            "identifier": "582597e0-207d-4dea-8feb-cfe472795fe8",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "budgets",
@@ -51758,28 +51741,14 @@
                 "presidents-budget-request",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T14:20:24.416296",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Fund for the Improvement of Postsecondary Education - Grant Management Information",
-            "description": "The Fund for the Improvement of Postsecondary Education (FIPSE), a unit within the Office of Postsecondary Education conducts the Comprehensive Grant Program as well as other postsecondary education grant competitions and partnerships that support innovative reform projects for postsecondary education. This page provides links to information about managing grants.",
-            "modified": "2023-07-07T14:19:27.888903",
-            "accessLevel": "public",
-            "identifier": "0052967e-b9c7-45dc-b953-91718a50017b",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                "name": "Office of Finance and Operations (OFO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -51792,24 +51761,34 @@
                         }
                     }
                 }
-                }
             },
+            "spatial": "United States",
+            "title": "FY 2006 Budget Summary:  Table of Contents"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "The Fund for the Improvement of Postsecondary Education (FIPSE), a unit within the Office of Postsecondary Education conducts the Comprehensive Grant Program as well as other postsecondary education grant competitions and partnerships that support innovative reform projects for postsecondary education. This page provides links to information about managing grants.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "National Award Programs - Links to Application Information:",
                     "description": "National Award Programs - Links to Application Information: -",
-                    "downloadURL": "https://data.ed.gov/dataset/7f917746-147f-4a52-ba86-ff3ba26c98ec/resource/e2bbc0e3-f1d5-43c4-8c6f-66105043a543/download/natlawardprograms.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7f917746-147f-4a52-ba86-ff3ba26c98ec/resource/e2bbc0e3-f1d5-43c4-8c6f-66105043a543/download/natlawardprograms.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "National Award Programs - Links to Application Information:"
                 }
             ],
+            "identifier": "0052967e-b9c7-45dc-b953-91718a50017b",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "distance-education",
@@ -51825,23 +51804,18 @@
                 "postsecondary-education",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T14:19:27.888903",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Freedom of Information Act (FOIA) Annual Reports",
-            "description": "The FOIA Annual Reports provide summary statistics, by principal office, of the activities conducted in the administration of the FOIA Program.",
-            "modified": "2023-07-07T14:18:24.760656",
-            "accessLevel": "public",
-            "identifier": "331d1a70-832c-499f-9d80-639214f3bd76",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Postsecondary Education (OPE)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Under Secretary (OUS)",
+                    "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
                         "subOrganizationOf": {
@@ -51852,119 +51826,132 @@
                                 "name": "U.S. Government"
                             }
                         }
+                    }
+                }
+            },
+            "spatial": "United States",
+            "title": "Fund for the Improvement of Postsecondary Education - Grant Management Information"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "na",
                 "hasEmail": "mailto:os@ed.gov"
             },
+            "description": "The FOIA Annual Reports provide summary statistics, by principal office, of the activities conducted in the administration of the FOIA Program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/0682723a-079b-4986-8b43-a9f225619d3e/download/foia-fy18.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/0682723a-079b-4986-8b43-a9f225619d3e/download/foia-fy18.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/018923f8-cc8f-412d-9222-7dfa87e19ec3/download/ed-raw-data-fy18.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/018923f8-cc8f-412d-9222-7dfa87e19ec3/download/ed-raw-data-fy18.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/f5ccaf5b-7ee7-4ba4-974b-a070a3079f52/download/foia-fy17.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/f5ccaf5b-7ee7-4ba4-974b-a070a3079f52/download/foia-fy17.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/cc58b72d-07d1-4643-aa3a-932e9d40a7e5/download/ed-raw-data-fy17.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/cc58b72d-07d1-4643-aa3a-932e9d40a7e5/download/ed-raw-data-fy17.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/0022ba42-cf4a-4a7f-ab03-3cebce81a66f/download/foia-fy16.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/0022ba42-cf4a-4a7f-ab03-3cebce81a66f/download/foia-fy16.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/e6b78d54-bd1a-47cd-a3ef-d119aac978f7/download/ed-raw-data-fy16.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/e6b78d54-bd1a-47cd-a3ef-d119aac978f7/download/ed-raw-data-fy16.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/e731f3cb-e761-408c-975c-5d2b0f1f31f6/download/foia-fy15.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/e731f3cb-e761-408c-975c-5d2b0f1f31f6/download/foia-fy15.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/bf4db097-cf90-4c78-8102-903d659d094f/download/foia-fy14.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/bf4db097-cf90-4c78-8102-903d659d094f/download/foia-fy14.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/91781c28-11b4-4ea2-9f44-34c135e91764/download/foia-fy13.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/91781c28-11b4-4ea2-9f44-34c135e91764/download/foia-fy13.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/06646871-cf1c-40e3-aae8-634c9550fd0f/download/foia-fy12.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/06646871-cf1c-40e3-aae8-634c9550fd0f/download/foia-fy12.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/fc5aea09-9e5b-4fe5-bf0b-7ae100ee03aa/download/foia-fy11.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/fc5aea09-9e5b-4fe5-bf0b-7ae100ee03aa/download/foia-fy11.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/cbed5825-0d48-4200-acce-893ed44289ef/download/foiafy10.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/cbed5825-0d48-4200-acce-893ed44289ef/download/foiafy10.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Annual FOIA Report"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Annual FOIA Report",
                     "description": "PDF - Annual FOIA Report",
-                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/1c8912df-66b6-421d-9dfe-375019ef0462/download/foiafy09.xml"
+                    "downloadURL": "https://data.ed.gov/dataset/c0d198b7-f7f3-4bdc-a8e7-7aec5cf967da/resource/1c8912df-66b6-421d-9dfe-375019ef0462/download/foiafy09.xml",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Annual FOIA Report"
                 }
             ],
+            "identifier": "331d1a70-832c-499f-9d80-639214f3bd76",
             "keyword": [
                 "2eea0c24-f950-40cc-bf91-9661d805523b",
                 "freedom-of-information",
@@ -51974,26 +51961,12 @@
                 "reports",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T14:18:24.760656",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Forecast of ED Contract Opportunities",
-            "description": "This Forecast indicates possible upcoming U.S. Department of Education (ED) acquisitions.",
-            "modified": "2023-07-07T14:17:24.982309",
-            "accessLevel": "public",
-            "identifier": "75ba013a-4ede-4aad-861c-6514e66f3126",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Finance and Operations (OFO)",
-                "subOrganizationOf": {
                 "@type": "org:Organization",
                 "name": "Office of the Secretary (OS)",
                 "subOrganizationOf": {
@@ -52004,31 +51977,41 @@
                         "name": "U.S. Government"
                     }
                 }
-                }
             },
+            "spatial": "United States",
+            "title": "Freedom of Information Act (FOIA) Annual Reports"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ocfo@ed.gov"
             },
+            "description": "This Forecast indicates possible upcoming U.S. Department of Education (ED) acquisitions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "MS Excel (102 KB) - FY 2020 Forecast of Contract Opportunities",
                     "description": "Forecast Date: June 10, 2020 - MS Excel (102 KB) - FY 2020 Forecast of Contract Opportunities",
-                    "downloadURL": "https://data.ed.gov/dataset/a7b2fa09-b63b-411b-8241-e180f34a134b/resource/266f561f-1b96-48c3-8b90-b14b2c380584/download/forecast6920.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/a7b2fa09-b63b-411b-8241-e180f34a134b/resource/266f561f-1b96-48c3-8b90-b14b2c380584/download/forecast6920.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MS Excel (102 KB) - FY 2020 Forecast of Contract Opportunities"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Forecast Date: June 10, 2020",
                     "description": "Forecast Date: June 10, 2020",
-                    "downloadURL": "https://data.ed.gov/dataset/a7b2fa09-b63b-411b-8241-e180f34a134b/resource/6fb26cc3-3446-4ee8-bec9-c83fbb42dc79/download/forecast4320.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/a7b2fa09-b63b-411b-8241-e180f34a134b/resource/6fb26cc3-3446-4ee8-bec9-c83fbb42dc79/download/forecast4320.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Forecast Date: June 10, 2020"
                 }
             ],
+            "identifier": "75ba013a-4ede-4aad-861c-6514e66f3126",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "business",
@@ -52040,22 +52023,11 @@
                 "small-businesses",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T14:17:24.982309",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Fiscal Year 2019-FY 2021 President's Budget State Tables for the U.S. Department of Education",
-            "description": "Tables showing funds for U.S. Department of Education State formula-allocated and selected student aid programs, by program and by State FY 2019, FY 2020, and the FY 2021 President's Budget, in PDF and EXCEL formats.",
-            "modified": "2023-07-07T14:14:59.320542",
-            "accessLevel": "public",
-            "identifier": "c12ca2fd-0e3f-429a-8efb-9d9bca0505dc",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -52072,29 +52044,40 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Forecast of ED Contract Opportunities"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ofo@ed.gov"
             },
+            "description": "Tables showing funds for U.S. Department of Education State formula-allocated and selected student aid programs, by program and by State FY 2019, FY 2020, and the FY 2021 President's Budget, in PDF and EXCEL formats.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "State tables by program",
                     "description": "State tables by program - State tables by program",
-                    "downloadURL": "https://data.ed.gov/dataset/c0dd6856-7b8b-4e7a-b543-1b9b7bb4a140/resource/b0a96ac5-2740-4734-98c4-280f96b49dfc/download/21stbyprogram.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c0dd6856-7b8b-4e7a-b543-1b9b7bb4a140/resource/b0a96ac5-2740-4734-98c4-280f96b49dfc/download/21stbyprogram.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "State tables by program"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "State tables by State",
                     "description": "State tables by program - State tables by State",
-                    "downloadURL": "https://data.ed.gov/dataset/c0dd6856-7b8b-4e7a-b543-1b9b7bb4a140/resource/036f1257-fb32-4f5e-bfe8-0d1b5099658f/download/21stbystate.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c0dd6856-7b8b-4e7a-b543-1b9b7bb4a140/resource/036f1257-fb32-4f5e-bfe8-0d1b5099658f/download/21stbystate.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "State tables by State"
                 }
             ],
+            "identifier": "c12ca2fd-0e3f-429a-8efb-9d9bca0505dc",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "appropriations",
@@ -52108,22 +52091,11 @@
                 "state-tables",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T14:14:59.320542",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ESEA Title I LEA Allocations\u2014FY 2011",
-            "description": "Tables (in PDF and EXCEL formats) showing FY 2011 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
-            "modified": "2023-07-07T14:13:53.599626",
-            "accessLevel": "public",
-            "identifier": "6956e019-8ba4-4c7b-82bb-bc7bdfc0f435",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -52140,430 +52112,441 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Fiscal Year 2019-FY 2021 President's Budget State Tables for the U.S. Department of Education"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "Tables (in PDF and EXCEL formats) showing FY 2011 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/2b9bbf82-fd8e-41fa-b31a-245f9dd2e90a/download/alabama.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/2b9bbf82-fd8e-41fa-b31a-245f9dd2e90a/download/alabama.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alaska - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/67c24dd0-f675-48ff-a9bb-8a1743faf490/download/alaska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/67c24dd0-f675-48ff-a9bb-8a1743faf490/download/alaska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Arizona - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/d5a05986-485d-4739-a4b3-6fe24271dc5c/download/arizona.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/d5a05986-485d-4739-a4b3-6fe24271dc5c/download/arizona.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Arkansas - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/47b79c01-e7b4-40f6-9ced-45f8366e7d3e/download/arkansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/47b79c01-e7b4-40f6-9ced-45f8366e7d3e/download/arkansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "California - California",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/845bf163-74bd-4fb0-a3d1-58d81631bc9e/download/california.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/845bf163-74bd-4fb0-a3d1-58d81631bc9e/download/california.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Colorado - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/7dda08e3-5d9f-43d6-89a9-d5e3e0da1145/download/colorado.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/7dda08e3-5d9f-43d6-89a9-d5e3e0da1145/download/colorado.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Connecticut - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/ea1a71b1-c5ac-4d55-a6ec-0e3dfc6c9947/download/connecticut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/ea1a71b1-c5ac-4d55-a6ec-0e3dfc6c9947/download/connecticut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Delaware - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/e6bd24a8-80a7-458c-bbb1-90d5d7aa59cf/download/delaware.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/e6bd24a8-80a7-458c-bbb1-90d5d7aa59cf/download/delaware.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "District of Columbia - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/72f3cca7-a67a-4477-83f9-88477702a67f/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/72f3cca7-a67a-4477-83f9-88477702a67f/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Florida - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/06c9aa71-535b-42fa-bc78-362dade7d588/download/florida.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/06c9aa71-535b-42fa-bc78-362dade7d588/download/florida.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Georgia - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/a1026923-0b45-4307-9b5f-25cf8bfc680f/download/georgia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/a1026923-0b45-4307-9b5f-25cf8bfc680f/download/georgia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Hawaii - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/848ec75c-bd6e-4163-a704-68c80c967477/download/hawaii.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/848ec75c-bd6e-4163-a704-68c80c967477/download/hawaii.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Idaho - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/25f7da93-5f43-4301-a208-f0ce5a4dc83f/download/idaho.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/25f7da93-5f43-4301-a208-f0ce5a4dc83f/download/idaho.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Illinois - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/1a252464-e953-4812-9ba9-6cf65fb69c6a/download/illinois.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/1a252464-e953-4812-9ba9-6cf65fb69c6a/download/illinois.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Indiana - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/98afacb6-7dd6-4c08-8d1b-6488857afee0/download/indiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/98afacb6-7dd6-4c08-8d1b-6488857afee0/download/indiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Iowa - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/32dfae1c-ff2c-4f12-94f6-f399ba5279b9/download/iowa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/32dfae1c-ff2c-4f12-94f6-f399ba5279b9/download/iowa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Kansas - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/9fb89bc3-d9f2-4bc9-8d25-9af45987dea0/download/kansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/9fb89bc3-d9f2-4bc9-8d25-9af45987dea0/download/kansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Kentucky - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/9e51b400-18b0-4b78-bd4c-e36b2c2face1/download/kentucky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/9e51b400-18b0-4b78-bd4c-e36b2c2face1/download/kentucky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Louisiana - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/285dce08-fe91-48d8-a217-5a3c628f1e85/download/louisiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/285dce08-fe91-48d8-a217-5a3c628f1e85/download/louisiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Maine - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/a4057ef1-3fae-4417-b702-602b5e9ec6b4/download/maine.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/a4057ef1-3fae-4417-b702-602b5e9ec6b4/download/maine.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Maryland - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/7136f03a-c219-455a-b80b-2b4183596c33/download/maryland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/7136f03a-c219-455a-b80b-2b4183596c33/download/maryland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Massachusetts - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/e032bbee-b761-4715-a9b2-91e6663cf4c5/download/massachusetts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/e032bbee-b761-4715-a9b2-91e6663cf4c5/download/massachusetts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Michigan - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/6a2f1e33-5412-4487-8189-0f4eeca14034/download/michigan.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/6a2f1e33-5412-4487-8189-0f4eeca14034/download/michigan.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Minnesota - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/30185ef5-dec2-44ad-b3b8-f4fbeb5c4f8a/download/minnesota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/30185ef5-dec2-44ad-b3b8-f4fbeb5c4f8a/download/minnesota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Mississippi - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/1ab7bb28-7c25-4b27-86a2-24d6e243e1d1/download/mississippi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/1ab7bb28-7c25-4b27-86a2-24d6e243e1d1/download/mississippi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Missouri - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/686acfcf-8155-470c-9849-4c03d8e75e0f/download/missouri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/686acfcf-8155-470c-9849-4c03d8e75e0f/download/missouri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Montana - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/9911442e-62ad-4439-9078-26f466f4d7f4/download/montana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/9911442e-62ad-4439-9078-26f466f4d7f4/download/montana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Nebraska - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/a59d7c2c-ea58-4691-98f1-db75c274195c/download/nebraska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/a59d7c2c-ea58-4691-98f1-db75c274195c/download/nebraska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Nevada - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/1210d4e0-972b-4504-9db3-7a683f76d102/download/nevada.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/1210d4e0-972b-4504-9db3-7a683f76d102/download/nevada.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "New Hampshire - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/9489fe71-e6c8-490a-800f-60a3d4378e6e/download/newhampshire.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/9489fe71-e6c8-490a-800f-60a3d4378e6e/download/newhampshire.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "New Jersey - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/e4ea448e-f7e0-428b-a92d-2666dd409a52/download/newjersey.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/e4ea448e-f7e0-428b-a92d-2666dd409a52/download/newjersey.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "New Mexico - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/561f85fb-5007-4bbe-972d-51a868f17202/download/newmexico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/561f85fb-5007-4bbe-972d-51a868f17202/download/newmexico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "New York - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/fc0df9f1-e06e-49aa-93d1-0f8bbd2104a5/download/newyork.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/fc0df9f1-e06e-49aa-93d1-0f8bbd2104a5/download/newyork.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "North Carolina - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/bd089aff-d651-4398-a261-cadf4526f9c8/download/northcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/bd089aff-d651-4398-a261-cadf4526f9c8/download/northcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "North Dakota - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/b69e96b9-3c8e-456b-8097-d1897bebfcb4/download/northdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/b69e96b9-3c8e-456b-8097-d1897bebfcb4/download/northdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Ohio - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/82ea53ca-d37f-40a7-8f55-5f952896cd17/download/ohio.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/82ea53ca-d37f-40a7-8f55-5f952896cd17/download/ohio.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Oklahoma - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/1cd0c5a3-becd-4dcb-b252-73bc469b75e1/download/oklahoma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/1cd0c5a3-becd-4dcb-b252-73bc469b75e1/download/oklahoma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Oregon - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/a51c9f69-b35c-45a9-a9df-2fec9429e06d/download/oregon.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/a51c9f69-b35c-45a9-a9df-2fec9429e06d/download/oregon.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Pennsylvania - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/b5b87778-3792-400e-b9ac-016242929100/download/pennsylvania.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/b5b87778-3792-400e-b9ac-016242929100/download/pennsylvania.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "Puerto Rico - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/ad1a6165-ecdc-43a5-81fb-307bcd653733/download/puertorico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/ad1a6165-ecdc-43a5-81fb-307bcd653733/download/puertorico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Rhode Island - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/bbf4d1d1-fe45-4a5c-aa5f-44f42ade17ab/download/rhodeisland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/bbf4d1d1-fe45-4a5c-aa5f-44f42ade17ab/download/rhodeisland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "South Carolina - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/0b31e28b-a4aa-4d68-bc84-c2bc71a34b44/download/southcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/0b31e28b-a4aa-4d68-bc84-c2bc71a34b44/download/southcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "South Dakota - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/dfbd27a1-e565-4387-b0a8-2a8475025153/download/southdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/dfbd27a1-e565-4387-b0a8-2a8475025153/download/southdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Tennessee - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/f4ecca08-17cc-4b12-91d1-a9a34368d618/download/tennessee.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/f4ecca08-17cc-4b12-91d1-a9a34368d618/download/tennessee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Texas - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/4887e46b-66b3-49bf-be57-adcbd546539c/download/texas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/4887e46b-66b3-49bf-be57-adcbd546539c/download/texas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Utah - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/f2716c7f-87bb-4354-a33f-f1e92e02b688/download/utah.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/f2716c7f-87bb-4354-a33f-f1e92e02b688/download/utah.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Vermont - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/9fa74fb9-3731-4f5e-bcb3-60895827d602/download/vermont.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/9fa74fb9-3731-4f5e-bcb3-60895827d602/download/vermont.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Virginia - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/008479f1-8a41-416f-a238-6233c87904f3/download/virginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/008479f1-8a41-416f-a238-6233c87904f3/download/virginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Washington - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/b297ee65-a9b6-40a9-9cd1-1a41ebe3adc3/download/washington.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/b297ee65-a9b6-40a9-9cd1-1a41ebe3adc3/download/washington.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "West Virginia - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/4e8c517a-c7f1-4130-8ab5-87e22f7d092b/download/westvirginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/4e8c517a-c7f1-4130-8ab5-87e22f7d092b/download/westvirginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Wisconsin - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/cf787aed-abcf-4029-90fd-59a523b5f36a/download/wisconsin.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/cf787aed-abcf-4029-90fd-59a523b5f36a/download/wisconsin.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Wyoming - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/739948e5-46f6-40ee-8d0a-71f0f1bbe5a3/download/wyoming.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7b5e298a-5b74-463e-8b6d-6a5eab1c1cc1/resource/739948e5-46f6-40ee-8d0a-71f0f1bbe5a3/download/wyoming.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 }
             ],
+            "identifier": "6956e019-8ba4-4c7b-82bb-bc7bdfc0f435",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "compensatory-education",
@@ -52578,22 +52561,11 @@
                 "supplemental-educational-serices",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T14:13:53.599626",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ESEA Title I LEA Allocations\u2014FY 2010",
-            "description": "Tables (in PDF and EXCEL formats) showing FY 2010 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
-            "modified": "2023-07-07T14:13:12.002670",
-            "accessLevel": "public",
-            "identifier": "6f551266-4c0e-42a0-9c05-20149c16df46",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -52610,430 +52582,441 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ESEA Title I LEA Allocations\u2014FY 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "Tables (in PDF and EXCEL formats) showing FY 2010 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/0a11bd2f-b4e7-40f1-bd0c-4902f082fc1d/download/alabama.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/0a11bd2f-b4e7-40f1-bd0c-4902f082fc1d/download/alabama.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alaska - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/fc972198-9169-4e60-a6a9-2c16ff70d269/download/alaska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/fc972198-9169-4e60-a6a9-2c16ff70d269/download/alaska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Arizona - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/50c7c0a3-b810-45d3-ab43-bf4432fd7cb7/download/arizona.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/50c7c0a3-b810-45d3-ab43-bf4432fd7cb7/download/arizona.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Arkansas - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/a59a0700-ad2c-4832-b1fc-d0f62394b1c0/download/arkansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/a59a0700-ad2c-4832-b1fc-d0f62394b1c0/download/arkansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "California - California",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/4a4eda94-2cc7-481e-a0e5-bd4d4e9a0cba/download/california.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/4a4eda94-2cc7-481e-a0e5-bd4d4e9a0cba/download/california.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Colorado - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/37dda964-8d7d-4a72-915d-34ada9772877/download/colorado.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/37dda964-8d7d-4a72-915d-34ada9772877/download/colorado.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Connecticut - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/94fc7f87-7c48-4408-952a-1f259ebf57f9/download/connecticut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/94fc7f87-7c48-4408-952a-1f259ebf57f9/download/connecticut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Delaware - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/d47c7d4c-0ab5-407e-a04d-dc78c09b11ca/download/delaware.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/d47c7d4c-0ab5-407e-a04d-dc78c09b11ca/download/delaware.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "District of Columbia - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/62698dae-f959-4fdd-89a7-1032dbd796ae/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/62698dae-f959-4fdd-89a7-1032dbd796ae/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Florida - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/7e84e7cd-3832-4188-9cd5-376129c5eb57/download/florida.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/7e84e7cd-3832-4188-9cd5-376129c5eb57/download/florida.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Georgia - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/31c2a3ab-e904-46b3-9c21-2b7906fb4901/download/georgia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/31c2a3ab-e904-46b3-9c21-2b7906fb4901/download/georgia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Hawaii - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/0e9e7ec1-05f5-41e5-8c91-a96bebec6394/download/hawaii.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/0e9e7ec1-05f5-41e5-8c91-a96bebec6394/download/hawaii.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Idaho - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/67f8c917-7d75-42cd-aecf-860de133826a/download/idaho.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/67f8c917-7d75-42cd-aecf-860de133826a/download/idaho.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Illinois - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/0e7b13a2-e21b-431c-8663-a022181291e2/download/illinois.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/0e7b13a2-e21b-431c-8663-a022181291e2/download/illinois.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Indiana - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/82ae9d75-3357-4bf0-9cec-b085e6f3c50b/download/indiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/82ae9d75-3357-4bf0-9cec-b085e6f3c50b/download/indiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Iowa - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/5cad623c-0c74-4783-9b71-251a54a9c4fe/download/iowa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/5cad623c-0c74-4783-9b71-251a54a9c4fe/download/iowa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Kansas - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/3012b38b-7cb3-4a09-9fc8-b02459dac787/download/kansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/3012b38b-7cb3-4a09-9fc8-b02459dac787/download/kansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Kentucky - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/dcb24063-1987-4bf3-9d7f-60967f49f24f/download/kentucky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/dcb24063-1987-4bf3-9d7f-60967f49f24f/download/kentucky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Louisiana - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/59a53d8d-64d1-4d93-a046-70c96e3c1693/download/louisiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/59a53d8d-64d1-4d93-a046-70c96e3c1693/download/louisiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Maine - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/a6a77c86-49b9-4158-acc1-40bbafb525ef/download/maine.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/a6a77c86-49b9-4158-acc1-40bbafb525ef/download/maine.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Maryland - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/40298b1e-854f-4239-abb9-83a31dec287f/download/maryland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/40298b1e-854f-4239-abb9-83a31dec287f/download/maryland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Massachusetts - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/ac686f54-77f8-40cc-9b48-638fe3b7f9c0/download/massachusetts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/ac686f54-77f8-40cc-9b48-638fe3b7f9c0/download/massachusetts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Michigan - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/f25f350c-260f-45dd-a2cd-13cb6be4d68a/download/michigan.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/f25f350c-260f-45dd-a2cd-13cb6be4d68a/download/michigan.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Minnesota - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/89e90b78-a6d6-46db-89f0-1a757977b35c/download/minnesota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/89e90b78-a6d6-46db-89f0-1a757977b35c/download/minnesota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Mississippi - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/2c8605bf-4d30-48b6-baf6-809268c5958f/download/mississippi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/2c8605bf-4d30-48b6-baf6-809268c5958f/download/mississippi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Missouri - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/8c871779-608e-4fc2-ba1c-0a4aefd97df6/download/missouri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/8c871779-608e-4fc2-ba1c-0a4aefd97df6/download/missouri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Montana - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/4405dda0-9545-4947-a1f4-eccc30227640/download/montana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/4405dda0-9545-4947-a1f4-eccc30227640/download/montana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Nebraska - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/01f28b4f-8215-437b-a2cf-a769b2a4918a/download/nebraska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/01f28b4f-8215-437b-a2cf-a769b2a4918a/download/nebraska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Nevada - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/9df7d674-9f9b-4afc-94cf-4b1e20d85754/download/nevada.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/9df7d674-9f9b-4afc-94cf-4b1e20d85754/download/nevada.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "New Hampshire - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/8085d178-bff8-4dc7-be21-26d4bc7439b4/download/newhampshire.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/8085d178-bff8-4dc7-be21-26d4bc7439b4/download/newhampshire.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "New Jersey - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/aec75d8d-9e25-4123-8079-16e9c6b334d3/download/newjersey.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/aec75d8d-9e25-4123-8079-16e9c6b334d3/download/newjersey.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "New Mexico - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/32bba527-3997-4e47-aa10-6bed3de4f337/download/newmexico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/32bba527-3997-4e47-aa10-6bed3de4f337/download/newmexico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "New York - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/dff86211-85da-45f5-961e-ab2e50010257/download/newyork.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/dff86211-85da-45f5-961e-ab2e50010257/download/newyork.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "North Carolina - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/ddb9408f-ef01-49bb-a660-a9b2532fb24f/download/northcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/ddb9408f-ef01-49bb-a660-a9b2532fb24f/download/northcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "North Dakota - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/42896de9-918f-47a9-9f03-0f6487c355d4/download/northdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/42896de9-918f-47a9-9f03-0f6487c355d4/download/northdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Ohio - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/9d57ca91-9dba-4b5d-a628-df455982b607/download/ohio.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/9d57ca91-9dba-4b5d-a628-df455982b607/download/ohio.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Oklahoma - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/74726f26-36b4-4db1-aa1a-01eaac72c0bd/download/oklahoma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/74726f26-36b4-4db1-aa1a-01eaac72c0bd/download/oklahoma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Oregon - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/fc841e15-38ca-4e64-b6b9-61790e5cc449/download/oregon.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/fc841e15-38ca-4e64-b6b9-61790e5cc449/download/oregon.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Pennsylvania - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/83539994-2325-4772-b85f-10cb5bee6c2d/download/pennsylvania.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/83539994-2325-4772-b85f-10cb5bee6c2d/download/pennsylvania.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "Puerto Rico - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/d44b0d12-8b03-4507-9344-29f62e700886/download/puertorico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/d44b0d12-8b03-4507-9344-29f62e700886/download/puertorico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Rhode Island - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/d8fde3e3-d7fb-4f3a-99e5-26b79998fb51/download/rhodeisland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/d8fde3e3-d7fb-4f3a-99e5-26b79998fb51/download/rhodeisland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "South Carolina - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/cb694012-eafe-4a80-9c8a-7c81a9ac1b6e/download/southcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/cb694012-eafe-4a80-9c8a-7c81a9ac1b6e/download/southcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "South Dakota - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/1c89bc43-5a24-42dd-860c-6ea5ababadac/download/southdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/1c89bc43-5a24-42dd-860c-6ea5ababadac/download/southdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Tennessee - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/0f901b5c-1dee-4692-8235-2de8642d32cc/download/tennessee.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/0f901b5c-1dee-4692-8235-2de8642d32cc/download/tennessee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Texas - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/827155c0-cdd0-47ba-bb47-ae57175d4f3f/download/texas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/827155c0-cdd0-47ba-bb47-ae57175d4f3f/download/texas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Utah - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/97a0f1ca-1f05-4daf-b0b5-65f9f6801428/download/utah.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/97a0f1ca-1f05-4daf-b0b5-65f9f6801428/download/utah.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Vermont - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/a7fa79dc-53db-4738-809b-83219e874fe3/download/vermont.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/a7fa79dc-53db-4738-809b-83219e874fe3/download/vermont.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Virginia - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/8e951a4e-8647-4f21-8eff-b5db7efe7be4/download/virginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/8e951a4e-8647-4f21-8eff-b5db7efe7be4/download/virginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Washington - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/8b07d739-ec20-4f74-af59-cce0ae4cc927/download/washington.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/8b07d739-ec20-4f74-af59-cce0ae4cc927/download/washington.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "West Virginia - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/4ac87ecb-5ff7-4c0e-b9c0-edc3c6fdcd5b/download/westvirginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/4ac87ecb-5ff7-4c0e-b9c0-edc3c6fdcd5b/download/westvirginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Wisconsin - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/89e24236-bfdb-43de-ad79-f33af420c9f6/download/wisconsin.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/89e24236-bfdb-43de-ad79-f33af420c9f6/download/wisconsin.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Wyoming - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/636a110a-9ac2-4a34-9d89-b63cd26a2997/download/wyoming.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/67695f3c-62a7-4a44-aee8-a2f7ce5bf1de/resource/636a110a-9ac2-4a34-9d89-b63cd26a2997/download/wyoming.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 }
             ],
+            "identifier": "6f551266-4c0e-42a0-9c05-20149c16df46",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "compensatory-education",
@@ -53048,22 +53031,11 @@
                 "supplemental-educational-serices",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T14:13:12.002670",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ESEA Title I LEA Allocations\u2014FY 2009 and the American Recovery and Reinvestment Act",
-            "description": "Tables (in PDF and EXCEL formats) showing FY 2009 and American Recovery and Reinvestment Act ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
-            "modified": "2023-07-07T14:12:29.469512",
-            "accessLevel": "public",
-            "identifier": "e5c023c9-95b5-40ee-b97f-c431d1a8e4ff",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -53080,430 +53052,441 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ESEA Title I LEA Allocations\u2014FY 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "Tables (in PDF and EXCEL formats) showing FY 2009 and American Recovery and Reinvestment Act ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/c7080362-f050-4bd8-a567-9d365f870410/download/alabama.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/c7080362-f050-4bd8-a567-9d365f870410/download/alabama.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alaska - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/4fd5b089-1d07-4d0d-b61a-6ee96431fa8a/download/alaska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/4fd5b089-1d07-4d0d-b61a-6ee96431fa8a/download/alaska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Arizona - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/5bb609de-942e-494f-8304-4f9ef61a9caf/download/arizona.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/5bb609de-942e-494f-8304-4f9ef61a9caf/download/arizona.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Arkansas - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/5dcfb2c5-bf09-491b-9495-9d536a40e950/download/arkansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/5dcfb2c5-bf09-491b-9495-9d536a40e950/download/arkansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "California - California",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/ab864187-3cfc-4b10-984f-44ff97a97017/download/california.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/ab864187-3cfc-4b10-984f-44ff97a97017/download/california.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Colorado - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/a92d74f7-4339-4ed9-896e-60286f6b6aad/download/colorado.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/a92d74f7-4339-4ed9-896e-60286f6b6aad/download/colorado.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Connecticut - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/e3fa3b64-3174-437c-8b02-e9fabfc027d5/download/connecticut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/e3fa3b64-3174-437c-8b02-e9fabfc027d5/download/connecticut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Delaware - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/3d5c5825-3cc9-4fb0-8f6b-aed960a31b27/download/delaware.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/3d5c5825-3cc9-4fb0-8f6b-aed960a31b27/download/delaware.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "District of Columbia - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/3a5a2a80-6cca-4cd8-b1c1-2bf234e4646d/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/3a5a2a80-6cca-4cd8-b1c1-2bf234e4646d/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Florida - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/fc69f09e-74ee-46dd-a4e6-0e14170185cc/download/florida.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/fc69f09e-74ee-46dd-a4e6-0e14170185cc/download/florida.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Georgia - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/01911cdd-facd-402f-8d18-ae0c23d0ab03/download/georgia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/01911cdd-facd-402f-8d18-ae0c23d0ab03/download/georgia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Hawaii - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/6a6d2315-c5a7-4a63-b775-02379113ccca/download/hawaii.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/6a6d2315-c5a7-4a63-b775-02379113ccca/download/hawaii.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Idaho - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/ce549382-1867-478f-af94-afe315efea92/download/idaho.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/ce549382-1867-478f-af94-afe315efea92/download/idaho.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Illinois - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/c4208b2d-60e3-47db-8b42-2d36d2490f68/download/illinois.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/c4208b2d-60e3-47db-8b42-2d36d2490f68/download/illinois.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Indiana - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/7755bb5d-a7c4-45c1-a717-21c28f9cd94c/download/indiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/7755bb5d-a7c4-45c1-a717-21c28f9cd94c/download/indiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Iowa - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/7027a7fa-42ba-4bc7-8fc0-e28e8e514d01/download/iowa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/7027a7fa-42ba-4bc7-8fc0-e28e8e514d01/download/iowa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Kansas - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/59829524-7076-4252-a8c3-190530e3a992/download/kansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/59829524-7076-4252-a8c3-190530e3a992/download/kansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Kentucky - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/4c98bc8c-76c0-45d9-8606-9e7580e98ec5/download/kentucky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/4c98bc8c-76c0-45d9-8606-9e7580e98ec5/download/kentucky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Louisiana - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/ec6ee925-b119-4eb1-9817-dc21d8f1d0b7/download/louisiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/ec6ee925-b119-4eb1-9817-dc21d8f1d0b7/download/louisiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Maine - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/bc5ae169-5869-494e-9f31-b24def796c2b/download/maine.xls"
-                },
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/bc5ae169-5869-494e-9f31-b24def796c2b/download/maine.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
+                },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Maryland - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/d38f0f92-53d7-4ae0-b2c4-03bd8e93deb3/download/maryland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/d38f0f92-53d7-4ae0-b2c4-03bd8e93deb3/download/maryland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Massachusetts - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/37746529-e41e-4b06-9ece-b65391124a29/download/massachusetts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/37746529-e41e-4b06-9ece-b65391124a29/download/massachusetts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Michigan - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/2ebb47b7-87f4-48c8-b428-7e82be874f2d/download/michigan.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/2ebb47b7-87f4-48c8-b428-7e82be874f2d/download/michigan.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Minnesota - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/ad2da809-c0a1-4027-b54e-607aa4287ab5/download/minnesota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/ad2da809-c0a1-4027-b54e-607aa4287ab5/download/minnesota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Mississippi - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/02de8e97-4398-4ee4-8b89-8153ae2701ac/download/mississippi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/02de8e97-4398-4ee4-8b89-8153ae2701ac/download/mississippi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Missouri - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/1e0b9356-8660-4abd-ba8d-ecad8034d27e/download/missouri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/1e0b9356-8660-4abd-ba8d-ecad8034d27e/download/missouri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Montana - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/9ba264ad-876f-40ed-8787-4a326e190bd4/download/montana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/9ba264ad-876f-40ed-8787-4a326e190bd4/download/montana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Nebraska - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/e505e242-d797-46e8-a618-1592eb5b8df8/download/nebraska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/e505e242-d797-46e8-a618-1592eb5b8df8/download/nebraska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Nevada - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/de919502-c0b0-4be3-a20f-45500282d2cc/download/nevada.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/de919502-c0b0-4be3-a20f-45500282d2cc/download/nevada.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "New Hampshire - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/85af4f28-1131-4bc1-ab35-6a88bb34493d/download/newhampshire.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/85af4f28-1131-4bc1-ab35-6a88bb34493d/download/newhampshire.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "New Jersey - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/3544057d-a4a5-47b0-9ab0-fb4d315c558f/download/newjersey.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/3544057d-a4a5-47b0-9ab0-fb4d315c558f/download/newjersey.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "New Mexico - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/f2d80580-a7fd-4590-99b0-97e6645c5389/download/newmexico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/f2d80580-a7fd-4590-99b0-97e6645c5389/download/newmexico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "New York - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/b7d4b4d7-f955-4911-9dce-4592881f6ad6/download/newyork.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/b7d4b4d7-f955-4911-9dce-4592881f6ad6/download/newyork.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "North Carolina - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/fdc27fbf-0c2d-4806-81d2-2c8e2c755fca/download/northcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/fdc27fbf-0c2d-4806-81d2-2c8e2c755fca/download/northcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "North Dakota - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/32955113-e4ef-4d6c-b638-dbb6c0df282b/download/northdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/32955113-e4ef-4d6c-b638-dbb6c0df282b/download/northdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Ohio - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/aa984288-ba62-49f7-8645-df5d49acab3f/download/ohio.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/aa984288-ba62-49f7-8645-df5d49acab3f/download/ohio.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Oklahoma - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/6f8df05b-78fe-4c38-80d6-121a236f6eee/download/oklahoma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/6f8df05b-78fe-4c38-80d6-121a236f6eee/download/oklahoma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Oregon - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/36c26ff9-a65f-441e-8c8f-5dd460174298/download/oregon.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/36c26ff9-a65f-441e-8c8f-5dd460174298/download/oregon.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Pennsylvania - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/cf3f9f97-5033-40aa-a9dd-21808d9190af/download/pennsylvania.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/cf3f9f97-5033-40aa-a9dd-21808d9190af/download/pennsylvania.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "Puerto Rico - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/97b9f73b-dc32-4e3c-9cf7-312e5e1ff827/download/puertorico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/97b9f73b-dc32-4e3c-9cf7-312e5e1ff827/download/puertorico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Rhode Island - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/946e2350-b2a6-4bfb-9c82-32a162e577c9/download/rhodeisland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/946e2350-b2a6-4bfb-9c82-32a162e577c9/download/rhodeisland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "South Carolina - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/a9800a28-3072-4d1b-be00-1a15a5b471b4/download/southcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/a9800a28-3072-4d1b-be00-1a15a5b471b4/download/southcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "South Dakota - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/73077af1-b2cd-42c2-863a-d968cb65d9a5/download/southdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/73077af1-b2cd-42c2-863a-d968cb65d9a5/download/southdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Tennessee - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/763c28eb-9548-4d75-9b74-48cb04df76aa/download/tennessee.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/763c28eb-9548-4d75-9b74-48cb04df76aa/download/tennessee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Texas - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/69c8e9df-10ed-4b1e-8080-ebd1289a392c/download/texas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/69c8e9df-10ed-4b1e-8080-ebd1289a392c/download/texas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Utah - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/5e6e4ccb-819f-4355-a001-964b3e8a887c/download/utah.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/5e6e4ccb-819f-4355-a001-964b3e8a887c/download/utah.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Vermont - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/ed755735-930d-45d1-8615-b94c30fa1d2c/download/vermont.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/ed755735-930d-45d1-8615-b94c30fa1d2c/download/vermont.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Virginia - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/444db4f9-9209-4f01-b061-3f20b829f436/download/virginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/444db4f9-9209-4f01-b061-3f20b829f436/download/virginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Washington - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/dadf9248-8d9b-43cd-9f64-6b7c815d271a/download/washington.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/dadf9248-8d9b-43cd-9f64-6b7c815d271a/download/washington.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "West Virginia - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/534bbbac-bd56-464c-89a1-ecf467db5318/download/westvirginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/534bbbac-bd56-464c-89a1-ecf467db5318/download/westvirginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Wisconsin - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/a83ae11e-9372-47db-b916-446d1823e8f6/download/wisconsin.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/a83ae11e-9372-47db-b916-446d1823e8f6/download/wisconsin.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Wyoming - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/831b6a55-08ff-4fc9-b106-85d73b6ae707/download/wyoming.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7bf838e9-76ce-4ac1-9bd1-26a4231780f8/resource/831b6a55-08ff-4fc9-b106-85d73b6ae707/download/wyoming.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 }
             ],
+            "identifier": "e5c023c9-95b5-40ee-b97f-c431d1a8e4ff",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "compensatory-education",
@@ -53518,22 +53501,11 @@
                 "supplemental-educational-serices",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T14:12:29.469512",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ESEA Title I LEA Allocations\u2014FY 2008 REVISED",
-            "description": "Tables (in PDF and EXCEL formats) showing Revised FY 2008 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
-            "modified": "2023-07-07T14:11:37.871783",
-            "accessLevel": "public",
-            "identifier": "37167aa5-a1bf-44aa-b5cc-2a8c0a7a381a",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -53550,430 +53522,441 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ESEA Title I LEA Allocations\u2014FY 2009 and the American Recovery and Reinvestment Act"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "Tables (in PDF and EXCEL formats) showing Revised FY 2008 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/52344f13-4329-4baf-ae4e-b55ece73099c/download/alabama.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/52344f13-4329-4baf-ae4e-b55ece73099c/download/alabama.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alaska - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/3c4d7681-f96c-4d66-81ac-bafc63909318/download/alaska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/3c4d7681-f96c-4d66-81ac-bafc63909318/download/alaska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Arizona - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/963cc9f1-506b-411c-be52-0354a392a24a/download/arizona.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/963cc9f1-506b-411c-be52-0354a392a24a/download/arizona.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Arkansas - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/bf9fdb92-4b0e-4fb9-8813-baa176d6b8a8/download/arkansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/bf9fdb92-4b0e-4fb9-8813-baa176d6b8a8/download/arkansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "California - California",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/bb1a463d-55e1-4176-ae07-076452237bb8/download/california.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/bb1a463d-55e1-4176-ae07-076452237bb8/download/california.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Colorado - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/963cf602-38a3-4d16-ab5f-953dc0ea454d/download/colorado.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/963cf602-38a3-4d16-ab5f-953dc0ea454d/download/colorado.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Connecticut - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/56be7d22-f23e-45dc-bf5e-a134833f7d90/download/connecticut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/56be7d22-f23e-45dc-bf5e-a134833f7d90/download/connecticut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Delaware - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/eb1c6b35-79a3-495a-9c54-2c5fe7f784e8/download/delaware.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/eb1c6b35-79a3-495a-9c54-2c5fe7f784e8/download/delaware.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "District of Columbia - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/271eb328-3144-4e10-a6b2-c021cec195bd/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/271eb328-3144-4e10-a6b2-c021cec195bd/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Florida - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/3a7c43da-6e49-45ab-89c0-53cd6e7b816e/download/florida.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/3a7c43da-6e49-45ab-89c0-53cd6e7b816e/download/florida.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Georgia - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/4ea9132b-6cd8-402d-a9b3-4c608a91b13c/download/georgia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/4ea9132b-6cd8-402d-a9b3-4c608a91b13c/download/georgia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Hawaii - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/a2bbdeee-20d9-41c0-9b32-b6b928f45d3b/download/hawaii.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/a2bbdeee-20d9-41c0-9b32-b6b928f45d3b/download/hawaii.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Idaho - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/531d91b2-7cf6-4bdd-a219-0afa1aef4826/download/idaho.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/531d91b2-7cf6-4bdd-a219-0afa1aef4826/download/idaho.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Illinois - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/722e5f5a-a6fb-4801-8d0b-a6569f05e5f6/download/illinois.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/722e5f5a-a6fb-4801-8d0b-a6569f05e5f6/download/illinois.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Indiana - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/a1fba687-06a4-4ee6-b141-8028ae344373/download/indiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/a1fba687-06a4-4ee6-b141-8028ae344373/download/indiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Iowa - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/0820f0fc-8bf6-48cc-b2a4-278a12ac2eea/download/iowa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/0820f0fc-8bf6-48cc-b2a4-278a12ac2eea/download/iowa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Kansas - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/a3c5e31f-9b31-4ebe-b42c-0778fc8456ba/download/kansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/a3c5e31f-9b31-4ebe-b42c-0778fc8456ba/download/kansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Kentucky - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/6cb99f0f-2973-4694-9478-4b8236ca11c4/download/kentucky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/6cb99f0f-2973-4694-9478-4b8236ca11c4/download/kentucky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Louisiana - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/c0bfe109-b9c0-4599-a378-d939bf95f793/download/louisiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/c0bfe109-b9c0-4599-a378-d939bf95f793/download/louisiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Maine - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/9a090fd1-7aeb-4105-88fb-8fa367b65034/download/maine.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/9a090fd1-7aeb-4105-88fb-8fa367b65034/download/maine.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Maryland - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/06e9b275-0da6-484c-b478-de411d9ec80f/download/maryland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/06e9b275-0da6-484c-b478-de411d9ec80f/download/maryland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Massachusetts - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/5939f11d-9fc2-47cd-8b2b-cf3e4cf6669e/download/massachusetts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/5939f11d-9fc2-47cd-8b2b-cf3e4cf6669e/download/massachusetts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Michigan - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/db426d97-7645-4521-8cab-4d1a2db38ad5/download/michigan.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/db426d97-7645-4521-8cab-4d1a2db38ad5/download/michigan.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Minnesota - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/c5c2ae03-e4ae-44bf-8c0c-d04950eb9e91/download/minnesota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/c5c2ae03-e4ae-44bf-8c0c-d04950eb9e91/download/minnesota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Mississippi - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/e6832e69-fd2f-4336-9880-15fa8d5af86d/download/mississippi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/e6832e69-fd2f-4336-9880-15fa8d5af86d/download/mississippi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Missouri - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/31b478dc-e305-4882-be18-5fc17689aac0/download/missouri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/31b478dc-e305-4882-be18-5fc17689aac0/download/missouri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Montana - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/ad8ef468-9529-453f-871a-d1188ea5be75/download/montana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/ad8ef468-9529-453f-871a-d1188ea5be75/download/montana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Nebraska - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/386b7148-57b5-4dd4-8e39-0def357b0e2b/download/nebraska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/386b7148-57b5-4dd4-8e39-0def357b0e2b/download/nebraska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Nevada - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/f7d7aaf5-70b8-43d8-a799-3480243bc125/download/nevada.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/f7d7aaf5-70b8-43d8-a799-3480243bc125/download/nevada.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "New Hampshire - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/5b6fbcd6-81c2-446a-8ced-f277330bf8d6/download/newhampshire.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/5b6fbcd6-81c2-446a-8ced-f277330bf8d6/download/newhampshire.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "New Jersey - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/4703ece3-383b-428f-9dfd-e076a334f7f7/download/newjersey.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/4703ece3-383b-428f-9dfd-e076a334f7f7/download/newjersey.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "New Mexico - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/09a13a8c-8e3a-4c58-b9d5-7c7ff40a1535/download/newmexico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/09a13a8c-8e3a-4c58-b9d5-7c7ff40a1535/download/newmexico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "New York - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/c0444d08-c9f2-4772-81b7-acb64033d5a6/download/newyork.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/c0444d08-c9f2-4772-81b7-acb64033d5a6/download/newyork.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "North Carolina - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/861f04b2-b373-4360-a0d6-bfd333898bec/download/northcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/861f04b2-b373-4360-a0d6-bfd333898bec/download/northcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "North Dakota - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/d56a9678-9baa-483a-ac0b-3bbf5caae111/download/northdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/d56a9678-9baa-483a-ac0b-3bbf5caae111/download/northdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Ohio - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/13d97c16-7329-4066-afa7-fc2a8cdff96a/download/ohio.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/13d97c16-7329-4066-afa7-fc2a8cdff96a/download/ohio.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Oklahoma - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/898a290d-a493-4199-bd2d-e3308be0e0fd/download/oklahoma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/898a290d-a493-4199-bd2d-e3308be0e0fd/download/oklahoma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Oregon - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/30f2abae-8873-4e8a-926f-fc213d28017f/download/oregon.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/30f2abae-8873-4e8a-926f-fc213d28017f/download/oregon.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Pennsylvania - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/86336368-bcd8-4deb-b6ae-e95ef3589a80/download/pennsylvania.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/86336368-bcd8-4deb-b6ae-e95ef3589a80/download/pennsylvania.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "Puerto Rico - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/442b371b-94d5-4ecd-bf82-51b45c01ef86/download/puertorico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/442b371b-94d5-4ecd-bf82-51b45c01ef86/download/puertorico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Rhode Island - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/0c091b81-a9e4-4711-a282-f70ce96484cc/download/rhodeisland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/0c091b81-a9e4-4711-a282-f70ce96484cc/download/rhodeisland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "South Carolina - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/2f6bb730-833d-4101-8b0f-24f05799a7aa/download/southcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/2f6bb730-833d-4101-8b0f-24f05799a7aa/download/southcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "South Dakota - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/460af71a-f215-4e2f-a26a-3adf7698050c/download/southdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/460af71a-f215-4e2f-a26a-3adf7698050c/download/southdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Tennessee - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/da740c9c-f29e-424b-bee1-2ab7609eb004/download/tennessee.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/da740c9c-f29e-424b-bee1-2ab7609eb004/download/tennessee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Texas - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/d4cd041c-bca6-43d4-970e-2d9461cdf44a/download/texas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/d4cd041c-bca6-43d4-970e-2d9461cdf44a/download/texas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Utah - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/d85422e9-f4f7-4b39-bc39-56c26aa32a16/download/utah.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/d85422e9-f4f7-4b39-bc39-56c26aa32a16/download/utah.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Vermont - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/1c672cdc-217a-46ec-b834-1de975d3c993/download/vermont.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/1c672cdc-217a-46ec-b834-1de975d3c993/download/vermont.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Virginia - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/68dbf729-7a06-4fd1-bb1b-f7ff8d53fce4/download/virginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/68dbf729-7a06-4fd1-bb1b-f7ff8d53fce4/download/virginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Washington - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/af696025-fca3-4717-864d-633b9be5dfdb/download/washington.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/af696025-fca3-4717-864d-633b9be5dfdb/download/washington.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "West Virginia - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/bf0ab6f9-46b9-4d53-9566-530415832576/download/westvirginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/bf0ab6f9-46b9-4d53-9566-530415832576/download/westvirginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Wisconsin - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/cf2b2c2f-8dce-4b00-b5fd-c9f183da271d/download/wisconsin.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/cf2b2c2f-8dce-4b00-b5fd-c9f183da271d/download/wisconsin.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Wyoming - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/9a69e9b0-a433-44d9-9164-79bad6882c43/download/wyoming.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/2abb7147-289d-439d-8083-8efac8e3a345/resource/9a69e9b0-a433-44d9-9164-79bad6882c43/download/wyoming.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 }
             ],
+            "identifier": "37167aa5-a1bf-44aa-b5cc-2a8c0a7a381a",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "compensatory-education",
@@ -53988,22 +53971,11 @@
                 "supplemental-educational-serices",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T14:11:37.871783",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ESEA Title I LEA Allocations\u2014FY 2007",
-            "description": "Tables (in PDF and EXCEL formats) showing FY 2007 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
-            "modified": "2023-07-07T14:11:01.905580",
-            "accessLevel": "public",
-            "identifier": "a546ccd6-cfce-49f2-a0a1-0a5cffa5de86",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -54020,430 +53992,441 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ESEA Title I LEA Allocations\u2014FY 2008 REVISED"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NA",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "Tables (in PDF and EXCEL formats) showing FY 2007 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/c08844b3-5b07-4fa8-a64e-48fdb970adff/download/alabama.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/c08844b3-5b07-4fa8-a64e-48fdb970adff/download/alabama.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alaska - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/3ae3b4da-e164-4210-ba30-6a0548467e97/download/alaska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/3ae3b4da-e164-4210-ba30-6a0548467e97/download/alaska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Arizona - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/813f89e2-3865-4f58-b340-198f9ff062ec/download/arizona.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/813f89e2-3865-4f58-b340-198f9ff062ec/download/arizona.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Arkansas - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/c61516e4-fd33-4f4b-b260-f034aa04117b/download/arkansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/c61516e4-fd33-4f4b-b260-f034aa04117b/download/arkansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "California - California",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/1843058e-bcad-440a-8981-79096bfbd465/download/california.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/1843058e-bcad-440a-8981-79096bfbd465/download/california.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Colorado - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/c4c59d81-99ae-41c1-9a78-6f53d6fe5a88/download/colorado.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/c4c59d81-99ae-41c1-9a78-6f53d6fe5a88/download/colorado.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Connecticut - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/e0926407-2458-47bd-9a16-f3e1e1ac9701/download/connecticut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/e0926407-2458-47bd-9a16-f3e1e1ac9701/download/connecticut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Delaware - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/85ac015d-7485-4f53-946c-50a88136cd35/download/delaware.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/85ac015d-7485-4f53-946c-50a88136cd35/download/delaware.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "District of Columbia - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/94468a61-cdcc-4ae5-9022-db6bf618b4b6/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/94468a61-cdcc-4ae5-9022-db6bf618b4b6/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Florida - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/4a0fbd33-6b4a-4053-a5a4-ab534362b7f1/download/florida.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/4a0fbd33-6b4a-4053-a5a4-ab534362b7f1/download/florida.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Georgia - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/58ae9827-583b-4213-a82b-b8a4683e59de/download/georgia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/58ae9827-583b-4213-a82b-b8a4683e59de/download/georgia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Hawaii - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/cdd20a85-ee17-4c4b-b6a0-69a9e8df5469/download/hawaii.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/cdd20a85-ee17-4c4b-b6a0-69a9e8df5469/download/hawaii.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Idaho - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/7f4d941f-4894-49a3-be52-b11a2958d760/download/idaho.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/7f4d941f-4894-49a3-be52-b11a2958d760/download/idaho.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Illinois - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/58f5c449-ec36-43fb-9730-52e3c39d13d8/download/illinois.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/58f5c449-ec36-43fb-9730-52e3c39d13d8/download/illinois.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Indiana - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/7c4739c3-2b4e-47a4-80c8-017641fbd884/download/indiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/7c4739c3-2b4e-47a4-80c8-017641fbd884/download/indiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Iowa - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/3e64d739-49b0-4228-b6a0-7b847245466e/download/iowa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/3e64d739-49b0-4228-b6a0-7b847245466e/download/iowa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Kansas - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/ecac32b1-0cea-426d-8c14-207b1e4db25b/download/kansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/ecac32b1-0cea-426d-8c14-207b1e4db25b/download/kansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Kentucky - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/051e4912-4a78-40f8-b902-18757c8ad13f/download/kentucky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/051e4912-4a78-40f8-b902-18757c8ad13f/download/kentucky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Louisiana - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/62b54c3a-42ec-4827-892a-ae126de1f64a/download/louisiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/62b54c3a-42ec-4827-892a-ae126de1f64a/download/louisiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Maine - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/717b9a2d-5007-4a78-96c5-475613e223dd/download/maine.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/717b9a2d-5007-4a78-96c5-475613e223dd/download/maine.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Maryland - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/f713b524-250a-4b4c-b9af-0f2fced16da2/download/maryland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/f713b524-250a-4b4c-b9af-0f2fced16da2/download/maryland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Massachusetts - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/7c5519f7-8d2f-4014-9fcd-449a46f74a0f/download/massachusetts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/7c5519f7-8d2f-4014-9fcd-449a46f74a0f/download/massachusetts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Michigan - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/723dacc3-05a6-407e-aa61-5b35e6b9736f/download/michigan.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/723dacc3-05a6-407e-aa61-5b35e6b9736f/download/michigan.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Minnesota - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/309f8237-14ac-47e0-823f-c0d57b45a625/download/minnesota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/309f8237-14ac-47e0-823f-c0d57b45a625/download/minnesota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Mississippi - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/11ced153-945d-443a-acb5-d8e286c78a18/download/mississippi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/11ced153-945d-443a-acb5-d8e286c78a18/download/mississippi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Missouri - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/0bdfe458-aa2b-4375-843e-d5d142f6bb13/download/missouri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/0bdfe458-aa2b-4375-843e-d5d142f6bb13/download/missouri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Montana - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/3d661e8b-2234-4a31-bfeb-fd80dfbaebf6/download/montana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/3d661e8b-2234-4a31-bfeb-fd80dfbaebf6/download/montana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Nebraska - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/c40b432a-af81-44e0-bbcb-94905a0c0207/download/nebraska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/c40b432a-af81-44e0-bbcb-94905a0c0207/download/nebraska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Nevada - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/b2da116f-1cac-480d-89ff-ff6f89c4c1d7/download/nevada.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/b2da116f-1cac-480d-89ff-ff6f89c4c1d7/download/nevada.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "New Hampshire - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/4e4f3ba3-2824-47c3-9846-1cd4f86d6d2d/download/newhampshire.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/4e4f3ba3-2824-47c3-9846-1cd4f86d6d2d/download/newhampshire.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "New Jersey - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/aed0bff1-f2dc-477b-8866-ed2447bb208e/download/newjersey.xls"
-                },
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/aed0bff1-f2dc-477b-8866-ed2447bb208e/download/newjersey.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
+                },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "New Mexico - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/6a97870d-6eec-4e89-a680-cf1f22f060fb/download/newmexico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/6a97870d-6eec-4e89-a680-cf1f22f060fb/download/newmexico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "New York - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/ea8c2790-83c4-4b00-91af-931966e3529e/download/newyork.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/ea8c2790-83c4-4b00-91af-931966e3529e/download/newyork.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "North Carolina - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/8e5fd58f-6ebb-476c-a9b8-c1ede4817aac/download/northcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/8e5fd58f-6ebb-476c-a9b8-c1ede4817aac/download/northcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "North Dakota - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/38359f0a-b7fe-4599-b065-5f800c53615b/download/northdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/38359f0a-b7fe-4599-b065-5f800c53615b/download/northdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Ohio - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/f222458b-57ba-4c94-aeba-97e043196344/download/ohio.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/f222458b-57ba-4c94-aeba-97e043196344/download/ohio.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Oklahoma - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/10be4307-7c35-48fe-90a1-490dabba47d7/download/oklahoma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/10be4307-7c35-48fe-90a1-490dabba47d7/download/oklahoma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Oregon - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/d7843aa9-0b38-42fd-93e4-9a8e2c7f7983/download/oregon.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/d7843aa9-0b38-42fd-93e4-9a8e2c7f7983/download/oregon.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Pennsylvania - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/3125436d-c07c-4532-81f7-87081841cad1/download/pennsylvania.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/3125436d-c07c-4532-81f7-87081841cad1/download/pennsylvania.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "Puerto Rico - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/4253efe3-e8b1-42b9-883c-47199f19b618/download/puertorico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/4253efe3-e8b1-42b9-883c-47199f19b618/download/puertorico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Rhode Island - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/179b8a0e-4fe3-4939-ba0e-8b4f133ce919/download/rhodeisland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/179b8a0e-4fe3-4939-ba0e-8b4f133ce919/download/rhodeisland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "South Carolina - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/d3161945-0610-4ee8-8020-ebd7ae283226/download/southcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/d3161945-0610-4ee8-8020-ebd7ae283226/download/southcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "South Dakota - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/8a49eb29-0566-4954-98c0-26253da33061/download/southdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/8a49eb29-0566-4954-98c0-26253da33061/download/southdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Tennessee - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/15c12902-72dd-4a3b-9aee-284f5a9efc6a/download/tennessee.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/15c12902-72dd-4a3b-9aee-284f5a9efc6a/download/tennessee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Texas - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/09766939-3281-4d38-94c9-01ac94b407bf/download/texas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/09766939-3281-4d38-94c9-01ac94b407bf/download/texas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Utah - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/3c73719a-cc8f-4e83-9c63-ea6df608498a/download/utah.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/3c73719a-cc8f-4e83-9c63-ea6df608498a/download/utah.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Vermont - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/e4e9971f-c4ef-4621-9720-32f3f4752b98/download/vermont.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/e4e9971f-c4ef-4621-9720-32f3f4752b98/download/vermont.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Virginia - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/d096a1c5-fac3-4932-989a-cdfaea728342/download/virginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/d096a1c5-fac3-4932-989a-cdfaea728342/download/virginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Washington - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/f0944c3d-9a6f-42ba-8565-8aee39e3b1d1/download/washington.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/f0944c3d-9a6f-42ba-8565-8aee39e3b1d1/download/washington.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "West Virginia - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/cfa9ca05-aec7-4152-a54a-5a302a94ec3d/download/westvirginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/cfa9ca05-aec7-4152-a54a-5a302a94ec3d/download/westvirginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Wisconsin - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/7a35c6a5-2f7f-4358-8c10-6b2b35f42ed8/download/wisconsin.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/7a35c6a5-2f7f-4358-8c10-6b2b35f42ed8/download/wisconsin.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Wyoming - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/59f258df-dfe5-489b-954e-af43b1d66c1d/download/wyoming.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/df93e637-349b-4c68-aa46-1d7d04d038a9/resource/59f258df-dfe5-489b-954e-af43b1d66c1d/download/wyoming.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 }
             ],
+            "identifier": "a546ccd6-cfce-49f2-a0a1-0a5cffa5de86",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "compensatory-education",
@@ -54458,22 +54441,11 @@
                 "supplemental-educational-serices",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-07T14:11:01.905580",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ESEA Title I LEA Allocations FY 2006 REVISED",
-            "description": "Tables showing REVISED FY 2006 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
-            "modified": "2023-07-06T22:28:11.067088",
-            "accessLevel": "public",
-            "identifier": "b34d141d-a409-49d2-9d74-9e09b8211e2d",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -54490,430 +54462,441 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ESEA Title I LEA Allocations\u2014FY 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OFO",
                 "hasEmail": "mailto:ofo@ed.gov"
             },
+            "description": "Tables showing REVISED FY 2006 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/aecafa28-464d-4c7b-ade4-3ef2bbbbf2f8/download/alabama.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/aecafa28-464d-4c7b-ade4-3ef2bbbbf2f8/download/alabama.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alaska - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/4e5d1037-6c0e-40c2-9917-a5affb4a7a71/download/alaska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/4e5d1037-6c0e-40c2-9917-a5affb4a7a71/download/alaska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Arizona - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/ef7e0f5c-6381-4ebf-8587-2573628e5daf/download/arizona.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/ef7e0f5c-6381-4ebf-8587-2573628e5daf/download/arizona.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Arkansas - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/30a57af2-96a6-405a-9802-d7e90996de26/download/arkansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/30a57af2-96a6-405a-9802-d7e90996de26/download/arkansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "California - California",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/c3bbb6b8-b751-4060-810a-6a1a2ea59f1e/download/california.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/c3bbb6b8-b751-4060-810a-6a1a2ea59f1e/download/california.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Colorado - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/44f6eeb4-b286-4f0f-886e-7ba6e918d2f8/download/colorado.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/44f6eeb4-b286-4f0f-886e-7ba6e918d2f8/download/colorado.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Connecticut - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/75ab9e4b-4de0-4b09-abdc-76a3b01b14cc/download/connecticut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/75ab9e4b-4de0-4b09-abdc-76a3b01b14cc/download/connecticut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Delaware - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/9032952e-2822-422d-b3b7-d2f7a8eaf8dd/download/delaware.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/9032952e-2822-422d-b3b7-d2f7a8eaf8dd/download/delaware.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "District of Columbia - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/fb141a49-1772-4c4b-aadd-1aaf79326bcd/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/fb141a49-1772-4c4b-aadd-1aaf79326bcd/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Florida - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/042cf8d4-3211-4d11-a84a-58a5ac64de3f/download/florida.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/042cf8d4-3211-4d11-a84a-58a5ac64de3f/download/florida.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Georgia - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/7c4b2b8a-7203-49b3-b259-afa1e3770907/download/georgia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/7c4b2b8a-7203-49b3-b259-afa1e3770907/download/georgia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Hawaii - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/9a56868c-d07d-4825-9115-ef921ac57b02/download/hawaii.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/9a56868c-d07d-4825-9115-ef921ac57b02/download/hawaii.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Idaho - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/28817d7e-2268-4253-8603-a6a3c1871990/download/idaho.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/28817d7e-2268-4253-8603-a6a3c1871990/download/idaho.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Illinois - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/2441d3e5-465b-4278-9061-10e24c56f221/download/illinois.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/2441d3e5-465b-4278-9061-10e24c56f221/download/illinois.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Indiana - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/a46459f4-7e5f-4c07-b4e9-e2228178a683/download/indiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/a46459f4-7e5f-4c07-b4e9-e2228178a683/download/indiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Iowa - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/056af6c1-7a65-44fa-ba3b-f22a7f42743b/download/iowa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/056af6c1-7a65-44fa-ba3b-f22a7f42743b/download/iowa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Kansas - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/2d96bdae-ec74-4694-a426-53199043e090/download/kansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/2d96bdae-ec74-4694-a426-53199043e090/download/kansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Kentucky - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/6547f60f-f080-4848-8242-d0eaac4dd6f2/download/kentucky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/6547f60f-f080-4848-8242-d0eaac4dd6f2/download/kentucky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Louisiana - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/75cd6cd2-f44c-4e0b-9d02-4c06de565b11/download/louisiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/75cd6cd2-f44c-4e0b-9d02-4c06de565b11/download/louisiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Maine - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/2d726628-9867-4060-b383-5e8659517a2a/download/maine.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/2d726628-9867-4060-b383-5e8659517a2a/download/maine.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Maryland - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/e739ccd8-02f7-4a21-b6f2-47edf9a2b9aa/download/maryland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/e739ccd8-02f7-4a21-b6f2-47edf9a2b9aa/download/maryland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Massachusetts - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/b328d510-0ee9-4e0d-a3c2-59eedc1dcb4c/download/massachusetts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/b328d510-0ee9-4e0d-a3c2-59eedc1dcb4c/download/massachusetts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Michigan - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/70123d90-5a6b-48c5-842e-79109b935aa3/download/michigan.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/70123d90-5a6b-48c5-842e-79109b935aa3/download/michigan.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Minnesota - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/94a49cb7-d216-4703-8b96-eb4e364f8627/download/minnesota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/94a49cb7-d216-4703-8b96-eb4e364f8627/download/minnesota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Mississippi - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/9667305e-89ef-4519-b637-420899631731/download/mississippi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/9667305e-89ef-4519-b637-420899631731/download/mississippi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Missouri - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/7bc6c387-1079-4ad0-9c6e-ea0629b390e4/download/missouri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/7bc6c387-1079-4ad0-9c6e-ea0629b390e4/download/missouri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Montana - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/d5bc3a1a-2c45-4187-b549-be0e2d3fe6fa/download/montana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/d5bc3a1a-2c45-4187-b549-be0e2d3fe6fa/download/montana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Nebraska - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/5d1d1862-ae9d-4ac3-8cf4-13ab5ce6c417/download/nebraska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/5d1d1862-ae9d-4ac3-8cf4-13ab5ce6c417/download/nebraska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Nevada - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/03152444-ff21-436f-a9a8-5dcf8788dc2e/download/nevada.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/03152444-ff21-436f-a9a8-5dcf8788dc2e/download/nevada.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "New Hampshire - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/a53bd66d-a1fa-4cf7-a034-395c3b2591f8/download/newhampshire.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/a53bd66d-a1fa-4cf7-a034-395c3b2591f8/download/newhampshire.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "New Jersey - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/650ac1c6-f5a9-4956-92b5-afb41cd731d5/download/newjersey.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/650ac1c6-f5a9-4956-92b5-afb41cd731d5/download/newjersey.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "New Mexico - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/00299ae2-633f-4404-9432-e83517c941ed/download/newmexico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/00299ae2-633f-4404-9432-e83517c941ed/download/newmexico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "New York - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/d19eaeaf-b41a-415d-9be0-6c4ffc9c8dea/download/newyork.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/d19eaeaf-b41a-415d-9be0-6c4ffc9c8dea/download/newyork.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "North Carolina - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/707ebefe-76bb-4ad8-939a-c6f713ebf839/download/northcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/707ebefe-76bb-4ad8-939a-c6f713ebf839/download/northcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "North Dakota - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/51470d53-162b-47ca-9378-136734040d68/download/northdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/51470d53-162b-47ca-9378-136734040d68/download/northdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Ohio - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/7815cf07-ec04-4783-a7fc-01d5ab81acc1/download/ohio.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/7815cf07-ec04-4783-a7fc-01d5ab81acc1/download/ohio.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Oklahoma - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/4e3447fc-ff32-4f5f-8288-b0b2fe187973/download/oklahoma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/4e3447fc-ff32-4f5f-8288-b0b2fe187973/download/oklahoma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Oregon - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/3733db1a-593f-4d87-9f07-a89fbef1e495/download/oregon.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/3733db1a-593f-4d87-9f07-a89fbef1e495/download/oregon.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Pennsylvania - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/83512cf4-87f2-4217-9b70-5a2c5aa883c8/download/pennsylvania.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/83512cf4-87f2-4217-9b70-5a2c5aa883c8/download/pennsylvania.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "Puerto Rico - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/461b4f15-8b9f-4440-9c7d-a90e9f4601f4/download/puertorico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/461b4f15-8b9f-4440-9c7d-a90e9f4601f4/download/puertorico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Rhode Island - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/e93f3dd2-f920-4010-ae0d-42d86e846acb/download/rhodeisland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/e93f3dd2-f920-4010-ae0d-42d86e846acb/download/rhodeisland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "South Carolina - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/c474711f-ef49-4221-a6ef-a426fcc090f3/download/southcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/c474711f-ef49-4221-a6ef-a426fcc090f3/download/southcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "South Dakota - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/f61dec6d-5c46-4194-9370-8e0b9919775e/download/southdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/f61dec6d-5c46-4194-9370-8e0b9919775e/download/southdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Tennessee - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/ec7f9845-665a-4dd3-b09c-4c25c34b188d/download/tennessee.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/ec7f9845-665a-4dd3-b09c-4c25c34b188d/download/tennessee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Texas - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/1248cd33-d9e3-41f5-a305-6cf065af4cc6/download/texas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/1248cd33-d9e3-41f5-a305-6cf065af4cc6/download/texas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Utah - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/b763b010-967d-44ab-9afa-72c27f8ca116/download/utah.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/b763b010-967d-44ab-9afa-72c27f8ca116/download/utah.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Vermont - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/b86c3145-b932-44e9-9918-d52ebcda8a6f/download/vermont.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/b86c3145-b932-44e9-9918-d52ebcda8a6f/download/vermont.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Virginia - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/25845a5c-86f2-44eb-8817-7501e1ddbde6/download/virginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/25845a5c-86f2-44eb-8817-7501e1ddbde6/download/virginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Washington - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/a3560f98-65b1-4739-bea4-488135fbee7b/download/washington.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/a3560f98-65b1-4739-bea4-488135fbee7b/download/washington.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "West Virginia - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/be70d8b7-1feb-4e88-93b3-b007ee8d51e6/download/westvirginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/be70d8b7-1feb-4e88-93b3-b007ee8d51e6/download/westvirginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Wisconsin - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/e31bca70-7a75-4ecb-a1f7-d3374b0e01be/download/wisconsin.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/e31bca70-7a75-4ecb-a1f7-d3374b0e01be/download/wisconsin.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Wyoming - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/9c3dbc91-ac9a-41bb-923f-ada3c1ea6429/download/wyoming.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/d93eb197-ddd2-4566-a157-1a1639c92c62/resource/9c3dbc91-ac9a-41bb-923f-ada3c1ea6429/download/wyoming.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 }
             ],
+            "identifier": "b34d141d-a409-49d2-9d74-9e09b8211e2d",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "compensatory-education",
@@ -54928,22 +54911,11 @@
                 "supplemental-educational-serices",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:28:11.067088",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ESEA Title I LEA Allocations FY 2005",
-            "description": "Tables  showing FY 2005 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
-            "modified": "2023-07-06T22:27:36.628235",
-            "accessLevel": "public",
-            "identifier": "0240bf73-ffc2-412b-9500-deb6c7cdb45e",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -54960,430 +54932,441 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ESEA Title I LEA Allocations FY 2006 REVISED"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ODS",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "Tables  showing FY 2005 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/b65252dd-ba3a-4745-b65a-c56856df87eb/download/alabama.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/b65252dd-ba3a-4745-b65a-c56856df87eb/download/alabama.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alaska - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/4ea17bbb-e68b-4458-b7ec-f88b20cd3fd4/download/alaska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/4ea17bbb-e68b-4458-b7ec-f88b20cd3fd4/download/alaska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Arizona - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/a45e9793-3d02-4e04-a3ea-a74aff71b946/download/arizona.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/a45e9793-3d02-4e04-a3ea-a74aff71b946/download/arizona.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Arkansas - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/781161d5-5430-4c9f-ad3a-06eb37693d18/download/arkansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/781161d5-5430-4c9f-ad3a-06eb37693d18/download/arkansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "California - California",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/58cfe4c8-d23a-43f3-9d07-8c31e76f6525/download/california.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/58cfe4c8-d23a-43f3-9d07-8c31e76f6525/download/california.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Colorado - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/fa10278f-4d5d-47c3-8b70-6c631c5c9d2a/download/colorado.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/fa10278f-4d5d-47c3-8b70-6c631c5c9d2a/download/colorado.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Connecticut - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/f6866ff5-96df-4443-bb67-0ac191d3ec34/download/connecticut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/f6866ff5-96df-4443-bb67-0ac191d3ec34/download/connecticut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Delaware - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/77a2b9cb-88e4-4e6f-ac27-237f9f822edf/download/delaware.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/77a2b9cb-88e4-4e6f-ac27-237f9f822edf/download/delaware.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "District of Columbia - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/54c26e33-8e76-4aa4-a810-a02f1e97a525/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/54c26e33-8e76-4aa4-a810-a02f1e97a525/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Florida - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/7ea64ce6-f238-4527-b453-5028221ac3af/download/florida.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/7ea64ce6-f238-4527-b453-5028221ac3af/download/florida.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Georgia - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/049759b2-9957-4232-82ed-b2f63de6dc88/download/georgia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/049759b2-9957-4232-82ed-b2f63de6dc88/download/georgia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Hawaii - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/1a812d32-72ea-4bc1-a97f-6f69be8553f3/download/hawaii.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/1a812d32-72ea-4bc1-a97f-6f69be8553f3/download/hawaii.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Idaho - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/9c126e46-e614-4b51-8531-ad6221f82195/download/idaho.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/9c126e46-e614-4b51-8531-ad6221f82195/download/idaho.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Illinois - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/7fba8490-86c4-4b39-ae54-e0d10b1990ce/download/illinois.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/7fba8490-86c4-4b39-ae54-e0d10b1990ce/download/illinois.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Indiana - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/26f88d95-440d-49cf-b720-aff1861b62fa/download/indiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/26f88d95-440d-49cf-b720-aff1861b62fa/download/indiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Iowa - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/beb3351f-2d3a-4e1b-b0a8-3adee9ea22fc/download/iowa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/beb3351f-2d3a-4e1b-b0a8-3adee9ea22fc/download/iowa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Kansas - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/bb2c3408-ede4-4199-a181-a7a98ea6ace8/download/kansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/bb2c3408-ede4-4199-a181-a7a98ea6ace8/download/kansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Kentucky - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/bf07ef66-27cd-40f3-a1cc-ece0a0340989/download/kentucky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/bf07ef66-27cd-40f3-a1cc-ece0a0340989/download/kentucky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Louisiana - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/0f4951a0-5adc-470e-93fc-e1cca80fb6fe/download/louisiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/0f4951a0-5adc-470e-93fc-e1cca80fb6fe/download/louisiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Maine - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/658bc807-1398-4fba-b06d-8799bd628ea8/download/maine.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/658bc807-1398-4fba-b06d-8799bd628ea8/download/maine.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Maryland - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/1608018f-ae3e-4e50-82fa-d3f83ec9392c/download/maryland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/1608018f-ae3e-4e50-82fa-d3f83ec9392c/download/maryland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Massachusetts - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/6a5419f0-2481-4302-9a4f-9f309c6ed152/download/massachusetts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/6a5419f0-2481-4302-9a4f-9f309c6ed152/download/massachusetts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Michigan - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/5de8509d-eb93-47da-b413-eae9a7c04baf/download/michigan.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/5de8509d-eb93-47da-b413-eae9a7c04baf/download/michigan.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Minnesota - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/c96cde69-9409-4ea6-8a82-aefb7d8dad52/download/minnesota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/c96cde69-9409-4ea6-8a82-aefb7d8dad52/download/minnesota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Mississippi - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/3bde3360-2b41-4891-b1a4-100f1de51152/download/mississippi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/3bde3360-2b41-4891-b1a4-100f1de51152/download/mississippi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Missouri - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/76db3048-3124-49f2-84e3-d0c77ebe4857/download/missouri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/76db3048-3124-49f2-84e3-d0c77ebe4857/download/missouri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Montana - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/b689afd5-e7b5-4d10-b96c-d9bcba0954bf/download/montana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/b689afd5-e7b5-4d10-b96c-d9bcba0954bf/download/montana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Nebraska - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/fbc95a8f-9077-45e3-a7cf-81cf1ac6f8e9/download/nebraska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/fbc95a8f-9077-45e3-a7cf-81cf1ac6f8e9/download/nebraska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Nevada - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/0d795946-9452-4eeb-b00e-7a2ff74b1fd5/download/nevada.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/0d795946-9452-4eeb-b00e-7a2ff74b1fd5/download/nevada.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "New Hampshire - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/a0dfa10b-2ff9-4086-9da4-aef43eaf01ad/download/newhampshire.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/a0dfa10b-2ff9-4086-9da4-aef43eaf01ad/download/newhampshire.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "New Jersey - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/478e545b-d03c-4748-b465-2f0d8bac5219/download/newjersey.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/478e545b-d03c-4748-b465-2f0d8bac5219/download/newjersey.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "New Mexico - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/e1162dfa-1485-442f-89f2-a00d65af2500/download/newmexico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/e1162dfa-1485-442f-89f2-a00d65af2500/download/newmexico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "New York - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/df0801d9-e06c-4e8e-9020-6cb404b76003/download/newyork.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/df0801d9-e06c-4e8e-9020-6cb404b76003/download/newyork.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "North Carolina - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/39d63c20-fde3-40cf-9296-f868657047de/download/northcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/39d63c20-fde3-40cf-9296-f868657047de/download/northcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "North Dakota - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/10fa377a-a51a-44c0-a6eb-cd2823754bd5/download/northdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/10fa377a-a51a-44c0-a6eb-cd2823754bd5/download/northdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Ohio - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/d184a8c0-bf43-487b-8e1a-36112574c2fb/download/ohio.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/d184a8c0-bf43-487b-8e1a-36112574c2fb/download/ohio.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Oklahoma - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/9e568c7a-f8df-40c2-b882-cf4bd2bcbf15/download/oklahoma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/9e568c7a-f8df-40c2-b882-cf4bd2bcbf15/download/oklahoma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Oregon - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/49de2918-3214-4f40-ae11-b93c06b68d58/download/oregon.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/49de2918-3214-4f40-ae11-b93c06b68d58/download/oregon.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Pennsylvania - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/abcd14d0-a4a2-4834-974f-fcafd440fee7/download/pennsylvania.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/abcd14d0-a4a2-4834-974f-fcafd440fee7/download/pennsylvania.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "Puerto Rico - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/44bda491-9574-4546-b7dd-65360e938551/download/puertorico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/44bda491-9574-4546-b7dd-65360e938551/download/puertorico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Rhode Island - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/32194091-9ce1-4faa-81a3-8026d2e63cbc/download/rhodeisland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/32194091-9ce1-4faa-81a3-8026d2e63cbc/download/rhodeisland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "South Carolina - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/53868cf4-7d24-40a8-8a9e-767d37d72d62/download/southcarolina.xls"
-                },
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/53868cf4-7d24-40a8-8a9e-767d37d72d62/download/southcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
+                },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "South Dakota - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/24915c23-18c4-491d-86a3-0f18e5ae5ac3/download/southdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/24915c23-18c4-491d-86a3-0f18e5ae5ac3/download/southdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Tennessee - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/0a9cf32f-8607-470f-934e-a2d21b692294/download/tennessee.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/0a9cf32f-8607-470f-934e-a2d21b692294/download/tennessee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Texas - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/c22a8f41-42cb-438a-94ab-d21691324392/download/texas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/c22a8f41-42cb-438a-94ab-d21691324392/download/texas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Utah - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/983d86ae-1cdc-49fa-a2e4-6e84e1ba0283/download/utah.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/983d86ae-1cdc-49fa-a2e4-6e84e1ba0283/download/utah.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Vermont - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/65172317-900d-478e-8501-75d166bcf5b7/download/vermont.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/65172317-900d-478e-8501-75d166bcf5b7/download/vermont.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Virginia - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/342e6631-4818-4a64-b178-d0f01adfe10e/download/virginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/342e6631-4818-4a64-b178-d0f01adfe10e/download/virginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Washington - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/b6c153ed-4d20-4c1d-8be2-3b1a64e67654/download/washington.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/b6c153ed-4d20-4c1d-8be2-3b1a64e67654/download/washington.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "West Virginia - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/37211bfd-ab6e-451a-b9b4-1b514ff06571/download/westvirginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/37211bfd-ab6e-451a-b9b4-1b514ff06571/download/westvirginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Wisconsin - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/895e14a5-7b3d-4d75-a5f5-8a03cd235bc2/download/wisconsin.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/895e14a5-7b3d-4d75-a5f5-8a03cd235bc2/download/wisconsin.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Wyoming - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/020734ec-e5c2-4313-91d7-cc67795fb8dd/download/wyoming.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3d0a8f60-4273-48db-93f5-f42f2c3e5308/resource/020734ec-e5c2-4313-91d7-cc67795fb8dd/download/wyoming.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 }
             ],
+            "identifier": "0240bf73-ffc2-412b-9500-deb6c7cdb45e",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "compensatory-education",
@@ -55398,22 +55381,11 @@
                 "supplemental-educational-serices",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:27:36.628235",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ESEA Title I LEA Allocations-FY 2004",
-            "description": "Tables (in PDF and EXCEL formats) showing FY 2004 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
-            "modified": "2023-07-06T22:27:10.567524",
-            "accessLevel": "public",
-            "identifier": "d5c85098-6b50-4b3c-a4fb-86b87323e873",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -55430,430 +55402,441 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ESEA Title I LEA Allocations FY 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ODS",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "Tables (in PDF and EXCEL formats) showing FY 2004 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/b1b9d436-632e-40cc-9c75-b21536bb40ce/download/alabama.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/b1b9d436-632e-40cc-9c75-b21536bb40ce/download/alabama.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alaska - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/46e84d0b-f4f3-4bc7-8e75-b357119a8133/download/alaska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/46e84d0b-f4f3-4bc7-8e75-b357119a8133/download/alaska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Arizona - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/660af7d8-b8e6-47d1-a91e-ce3ce41234cf/download/arizona.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/660af7d8-b8e6-47d1-a91e-ce3ce41234cf/download/arizona.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Arkansas - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/07dac08b-19c1-4b44-88e6-91061b22ace4/download/arkansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/07dac08b-19c1-4b44-88e6-91061b22ace4/download/arkansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "California - California",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/ee158b94-d3c3-49fa-a70a-b5cb417e75e5/download/california.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/ee158b94-d3c3-49fa-a70a-b5cb417e75e5/download/california.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Colorado - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/cebb0a3c-9d69-4b65-a2dd-c24467f7b0a1/download/colorado.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/cebb0a3c-9d69-4b65-a2dd-c24467f7b0a1/download/colorado.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Connecticut - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/6d4fd201-7054-4506-8e42-84ad43e9f183/download/connecticut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/6d4fd201-7054-4506-8e42-84ad43e9f183/download/connecticut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Delaware - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/bc2586ac-f62a-407e-9a47-7ab79eade904/download/delaware.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/bc2586ac-f62a-407e-9a47-7ab79eade904/download/delaware.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "District of Columbia - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/245b1632-116e-45e6-b9d9-ea2df74d2636/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/245b1632-116e-45e6-b9d9-ea2df74d2636/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Florida - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/57db5e9d-e198-4a39-9ee6-860f7a813428/download/florida.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/57db5e9d-e198-4a39-9ee6-860f7a813428/download/florida.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Georgia - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/a696e7e8-fc48-41fc-a761-4794cea1ad49/download/georgia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/a696e7e8-fc48-41fc-a761-4794cea1ad49/download/georgia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Hawaii - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/c32a2341-92c7-4834-8002-53b77d9a146b/download/hawaii.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/c32a2341-92c7-4834-8002-53b77d9a146b/download/hawaii.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Idaho - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/68644867-ec19-4b0f-80cb-27806592684a/download/idaho.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/68644867-ec19-4b0f-80cb-27806592684a/download/idaho.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Illinois - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/9610e015-d7bc-4261-bbd4-88811ea89a19/download/illinois.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/9610e015-d7bc-4261-bbd4-88811ea89a19/download/illinois.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Indiana - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/1a069f01-fb24-4687-9714-3ae99be78796/download/indiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/1a069f01-fb24-4687-9714-3ae99be78796/download/indiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Iowa - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/103f1f8c-55bb-49f9-94ef-8dae9da1e983/download/iowa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/103f1f8c-55bb-49f9-94ef-8dae9da1e983/download/iowa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Kansas - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/818b8a29-35de-4aaa-80c9-ff59d1cc0488/download/kansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/818b8a29-35de-4aaa-80c9-ff59d1cc0488/download/kansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Kentucky - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/d4282c06-e6ab-4ac5-ba59-af67aec6e9f9/download/kentucky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/d4282c06-e6ab-4ac5-ba59-af67aec6e9f9/download/kentucky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Louisiana - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/f9db3505-bbb0-43fb-9963-648e7dd426dd/download/louisiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/f9db3505-bbb0-43fb-9963-648e7dd426dd/download/louisiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Maine - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/19049f81-e938-470c-b15a-9ec8dd8772a2/download/maine.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/19049f81-e938-470c-b15a-9ec8dd8772a2/download/maine.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Maryland - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/cdf184ab-373e-4528-81d5-7ce89bc40498/download/maryland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/cdf184ab-373e-4528-81d5-7ce89bc40498/download/maryland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Massachusetts - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/8b3aaff1-89fb-4fd1-a8b1-ebb1367f36aa/download/massachusetts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/8b3aaff1-89fb-4fd1-a8b1-ebb1367f36aa/download/massachusetts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Michigan - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/05a43c33-f8aa-4f32-9a02-08a58f5b5f8d/download/michigan.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/05a43c33-f8aa-4f32-9a02-08a58f5b5f8d/download/michigan.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Minnesota - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/83185db1-bf84-4a6f-8e5a-e86686ab61ad/download/minnesota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/83185db1-bf84-4a6f-8e5a-e86686ab61ad/download/minnesota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Mississippi - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/de3ae1e9-28dd-485a-a277-e1d95b5cb319/download/mississippi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/de3ae1e9-28dd-485a-a277-e1d95b5cb319/download/mississippi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Missouri - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/ca78d2f2-28e1-47a2-bd76-659b7a297c1d/download/missouri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/ca78d2f2-28e1-47a2-bd76-659b7a297c1d/download/missouri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Montana - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/c7b11ae7-c483-4dd5-8e10-d463a543055d/download/montana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/c7b11ae7-c483-4dd5-8e10-d463a543055d/download/montana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Nebraska - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/f218a994-5979-41ec-b560-24da00a40c0d/download/nebraska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/f218a994-5979-41ec-b560-24da00a40c0d/download/nebraska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Nevada - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/27c1c0fa-7fd8-41c4-9085-53735ced787d/download/nevada.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/27c1c0fa-7fd8-41c4-9085-53735ced787d/download/nevada.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "New Hampshire - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/8b52138c-2bb2-4908-8acf-bb0316b1acb7/download/newhampshire.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/8b52138c-2bb2-4908-8acf-bb0316b1acb7/download/newhampshire.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "New Jersey - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/e43a10a9-5b93-48c7-9e11-7e0be46f1a10/download/newjersey.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/e43a10a9-5b93-48c7-9e11-7e0be46f1a10/download/newjersey.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "New Mexico - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/bb059799-4d4c-49f0-b8b2-7c1ab7900916/download/newmexico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/bb059799-4d4c-49f0-b8b2-7c1ab7900916/download/newmexico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "New York - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/c8cec4cd-aa19-4621-9c91-0c7616153d59/download/newyork.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/c8cec4cd-aa19-4621-9c91-0c7616153d59/download/newyork.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "North Carolina - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/4f8ec943-f18f-4869-9b08-a6569c407b8f/download/northcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/4f8ec943-f18f-4869-9b08-a6569c407b8f/download/northcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "North Dakota - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/01199bce-7f60-4852-95d3-ee27404bfeb5/download/northdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/01199bce-7f60-4852-95d3-ee27404bfeb5/download/northdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Ohio - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/805d11ea-340b-4c6b-86d7-62edc7bd4dbd/download/ohio.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/805d11ea-340b-4c6b-86d7-62edc7bd4dbd/download/ohio.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Oklahoma - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/bf638e26-fb05-4de1-835b-8a8f00f52dd5/download/oklahoma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/bf638e26-fb05-4de1-835b-8a8f00f52dd5/download/oklahoma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Oregon - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/6f7fefac-1693-4d9e-8d36-5c8a3e99fd27/download/oregon.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/6f7fefac-1693-4d9e-8d36-5c8a3e99fd27/download/oregon.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Pennsylvania - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/52c2f949-9176-4e5c-a4d3-dcdef24e7d2c/download/pennsylvania.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/52c2f949-9176-4e5c-a4d3-dcdef24e7d2c/download/pennsylvania.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "Puerto Rico - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/6b9b3897-8d1e-4459-9fc9-1e771515cfb4/download/puertorico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/6b9b3897-8d1e-4459-9fc9-1e771515cfb4/download/puertorico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Rhode Island - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/162ca7d1-20fe-49f0-967c-0f7fd4734c4a/download/rhodeisland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/162ca7d1-20fe-49f0-967c-0f7fd4734c4a/download/rhodeisland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "South Carolina - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/79c8438a-ee30-4b8c-9519-323bf8087a03/download/southcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/79c8438a-ee30-4b8c-9519-323bf8087a03/download/southcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "South Dakota - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/d5553bb7-00da-4824-90d6-8e085c8e991c/download/southdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/d5553bb7-00da-4824-90d6-8e085c8e991c/download/southdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Tennessee - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/fb76c0d7-28b3-4078-bf82-219445c1c1db/download/tennessee.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/fb76c0d7-28b3-4078-bf82-219445c1c1db/download/tennessee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Texas - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/539c13a9-078b-4207-a90c-c8ef2c5be1e4/download/texas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/539c13a9-078b-4207-a90c-c8ef2c5be1e4/download/texas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Utah - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/78f722e9-d4e6-44b5-8983-687ce34092e7/download/utah.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/78f722e9-d4e6-44b5-8983-687ce34092e7/download/utah.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Vermont - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/09abecc4-94dc-4a24-a7cf-630e5e1a306b/download/vermont.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/09abecc4-94dc-4a24-a7cf-630e5e1a306b/download/vermont.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Virginia - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/0a209269-c3e8-4a98-bd10-7ee83eb14489/download/virginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/0a209269-c3e8-4a98-bd10-7ee83eb14489/download/virginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Washington - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/7749f2fa-9077-4464-ada3-fb07dfa5b000/download/washington.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/7749f2fa-9077-4464-ada3-fb07dfa5b000/download/washington.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "West Virginia - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/1ec68867-e1f5-4806-b86a-c1015904102e/download/westvirginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/1ec68867-e1f5-4806-b86a-c1015904102e/download/westvirginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Wisconsin - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/8a8a7923-d51c-42f8-b428-ce6e6fbf2f81/download/wisconsin.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/8a8a7923-d51c-42f8-b428-ce6e6fbf2f81/download/wisconsin.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Wyoming - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/04440fa7-d9e9-4987-af3f-105ef72b45f1/download/wyoming.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/76275ea6-7404-414d-88f0-d85a89dfefe5/resource/04440fa7-d9e9-4987-af3f-105ef72b45f1/download/wyoming.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 }
             ],
+            "identifier": "d5c85098-6b50-4b3c-a4fb-86b87323e873",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "compensatory-education",
@@ -55868,22 +55851,11 @@
                 "supplemental-educational-serices",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:27:10.567524",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ESEA Title I LEA allocations - FY 2003",
-            "description": "Tables (in PDF and EXCEL formats) showing FY 2003 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
-            "modified": "2023-07-06T22:26:24.247649",
-            "accessLevel": "public",
-            "identifier": "785a64bc-9fd8-4704-a814-bde3bb15738a",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -55900,430 +55872,441 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ESEA Title I LEA Allocations-FY 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ODS",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "Tables (in PDF and EXCEL formats) showing FY 2003 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/e53c5aa9-1634-4929-b7b2-bc2aa4205a3c/download/alabama.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/e53c5aa9-1634-4929-b7b2-bc2aa4205a3c/download/alabama.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alaska - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/20907752-f47f-4a86-97d1-0aae3a383f7b/download/alaska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/20907752-f47f-4a86-97d1-0aae3a383f7b/download/alaska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Arizona - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/80cc23aa-3def-43b2-8ab1-7425a43d9753/download/arizona.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/80cc23aa-3def-43b2-8ab1-7425a43d9753/download/arizona.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Arkansas - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/d5f8edff-8106-44e5-8eb0-3fce67b74235/download/arkansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/d5f8edff-8106-44e5-8eb0-3fce67b74235/download/arkansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "California - California",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/7c30390c-acf9-40e9-97ea-dfe4a5333d70/download/california.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/7c30390c-acf9-40e9-97ea-dfe4a5333d70/download/california.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Colorado - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/d5f892b0-fa75-49a4-b207-0cadcfd94aa2/download/colorado.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/d5f892b0-fa75-49a4-b207-0cadcfd94aa2/download/colorado.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Connecticut - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/1db44dab-e075-4ee1-984d-90526e34b1d5/download/connecticut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/1db44dab-e075-4ee1-984d-90526e34b1d5/download/connecticut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Delaware - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/13a7f8f1-94df-4bd3-b0f3-d913cb631183/download/delaware.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/13a7f8f1-94df-4bd3-b0f3-d913cb631183/download/delaware.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "District of Columbia - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/96aa9e1d-114d-4c84-8940-8fa3978f9601/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/96aa9e1d-114d-4c84-8940-8fa3978f9601/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Florida - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/61a01e36-41d2-47a5-b413-1ca59b6d6b81/download/florida.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/61a01e36-41d2-47a5-b413-1ca59b6d6b81/download/florida.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Georgia - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/4a4e55b5-6725-4a08-a48d-9a95ededa833/download/georgia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/4a4e55b5-6725-4a08-a48d-9a95ededa833/download/georgia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Hawaii - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/caecf75b-5de8-4301-ae1d-be3ad14c1a4f/download/hawaii.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/caecf75b-5de8-4301-ae1d-be3ad14c1a4f/download/hawaii.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Idaho - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/0427fa3f-9815-4238-b7b9-54f49bc373ad/download/idaho.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/0427fa3f-9815-4238-b7b9-54f49bc373ad/download/idaho.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Illinois - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/a03e03f8-7591-4102-896e-940151d77155/download/illinois.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/a03e03f8-7591-4102-896e-940151d77155/download/illinois.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Indiana - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/497584e2-368e-4bb6-82c9-4aaa8d294542/download/indiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/497584e2-368e-4bb6-82c9-4aaa8d294542/download/indiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Iowa - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/635d59ae-7ef4-4d64-99be-f1de147d517f/download/iowa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/635d59ae-7ef4-4d64-99be-f1de147d517f/download/iowa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Kansas - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/9208a7bb-16c5-4581-90e8-f913055966ae/download/kansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/9208a7bb-16c5-4581-90e8-f913055966ae/download/kansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Kentucky - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/9afbfd1a-8f33-4de6-9018-e1faf244075c/download/kentucky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/9afbfd1a-8f33-4de6-9018-e1faf244075c/download/kentucky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Louisiana - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/495338af-a35e-4d1d-9a72-6bcfea2c5cae/download/louisiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/495338af-a35e-4d1d-9a72-6bcfea2c5cae/download/louisiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Maine - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/1003b3f7-2376-4c18-bff5-d980c9e3c3f9/download/maine.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/1003b3f7-2376-4c18-bff5-d980c9e3c3f9/download/maine.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Maryland - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/eec1993d-e44d-43dd-b78c-3e53e16736f5/download/maryland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/eec1993d-e44d-43dd-b78c-3e53e16736f5/download/maryland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Massachusetts - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/9f01c8c3-82b9-4f6f-b1f0-702f270e5bb4/download/massachusetts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/9f01c8c3-82b9-4f6f-b1f0-702f270e5bb4/download/massachusetts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Michigan - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/29a6ca13-dc7c-4aa5-a7f1-2df0ca948cd0/download/michigan.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/29a6ca13-dc7c-4aa5-a7f1-2df0ca948cd0/download/michigan.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Minnesota - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/9f3e207c-ffc1-4d0c-a4b4-1f97c92b9fb3/download/minnesota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/9f3e207c-ffc1-4d0c-a4b4-1f97c92b9fb3/download/minnesota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Mississippi - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/e9652db4-f9e1-420c-9ec6-a233e82659a4/download/mississippi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/e9652db4-f9e1-420c-9ec6-a233e82659a4/download/mississippi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Missouri - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/d2121971-350b-4562-b43e-37c296c4906d/download/missouri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/d2121971-350b-4562-b43e-37c296c4906d/download/missouri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Montana - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/ab00a387-95a1-4818-a4ec-c4b3c452b2ba/download/montana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/ab00a387-95a1-4818-a4ec-c4b3c452b2ba/download/montana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Nebraska - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/ea001483-24bc-4b52-832a-114f7ee38481/download/nebraska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/ea001483-24bc-4b52-832a-114f7ee38481/download/nebraska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Nevada - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/a4604038-60ec-45f8-8cad-8f379d662b04/download/nevada.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/a4604038-60ec-45f8-8cad-8f379d662b04/download/nevada.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "New Hampshire - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/db6b8f07-634f-4489-be02-adea7d738839/download/newhampshire.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/db6b8f07-634f-4489-be02-adea7d738839/download/newhampshire.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "New Jersey - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/9e070137-cf84-4165-b97b-d2ec68973b52/download/newjersey.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/9e070137-cf84-4165-b97b-d2ec68973b52/download/newjersey.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "New Mexico - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/b9e44f20-d544-48cd-85cb-0360bb8f0f19/download/newmexico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/b9e44f20-d544-48cd-85cb-0360bb8f0f19/download/newmexico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "New York - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/8bbdbbf2-2857-43a4-ba8e-8627981ee800/download/newyork.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/8bbdbbf2-2857-43a4-ba8e-8627981ee800/download/newyork.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "North Carolina - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/ff5b7ae8-f5c3-481e-9adb-031a756b621a/download/northcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/ff5b7ae8-f5c3-481e-9adb-031a756b621a/download/northcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "North Dakota - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/b6a600d1-c54d-498a-b4d4-4b4f7c88ca3e/download/northdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/b6a600d1-c54d-498a-b4d4-4b4f7c88ca3e/download/northdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Ohio - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/7a91c206-bd13-4fe3-a1d5-68689a098106/download/ohio.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/7a91c206-bd13-4fe3-a1d5-68689a098106/download/ohio.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Oklahoma - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/daba3069-deea-45e9-bf3f-f26aad54d4ac/download/oklahoma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/daba3069-deea-45e9-bf3f-f26aad54d4ac/download/oklahoma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Oregon - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/498fcc35-9660-4aaf-ab97-0819113af97b/download/oregon.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/498fcc35-9660-4aaf-ab97-0819113af97b/download/oregon.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Pennsylvania - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/476ae301-86df-4151-8d61-97e8bbcf7043/download/pennsylvania.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/476ae301-86df-4151-8d61-97e8bbcf7043/download/pennsylvania.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "Puerto Rico - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/c55082f5-67f6-4155-be30-a9109334d709/download/puertorico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/c55082f5-67f6-4155-be30-a9109334d709/download/puertorico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Rhode Island - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/dafb7a6a-692e-4c95-8ef1-6575a61d4535/download/rhodeisland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/dafb7a6a-692e-4c95-8ef1-6575a61d4535/download/rhodeisland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "South Carolina - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/6986a490-a2ef-464c-aac9-44943b500ea4/download/southcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/6986a490-a2ef-464c-aac9-44943b500ea4/download/southcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "South Dakota - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/649ffad8-aaeb-4173-a515-696e2fc61655/download/southdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/649ffad8-aaeb-4173-a515-696e2fc61655/download/southdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Tennessee - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/ea49c4ac-f640-408d-aaa6-b91b0d922cbc/download/tennessee.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/ea49c4ac-f640-408d-aaa6-b91b0d922cbc/download/tennessee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Texas - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/48d7d59c-7676-48c3-9223-4654da03abd3/download/texas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/48d7d59c-7676-48c3-9223-4654da03abd3/download/texas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Utah - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/b95f7b97-08b5-4033-a02f-4f49514512e0/download/utah.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/b95f7b97-08b5-4033-a02f-4f49514512e0/download/utah.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Vermont - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/51b41448-6ab2-4319-acd7-0b70a3b93002/download/vermont.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/51b41448-6ab2-4319-acd7-0b70a3b93002/download/vermont.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Virginia - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/dbbf2883-5109-4345-84ce-a8aeef6a22fd/download/virginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/dbbf2883-5109-4345-84ce-a8aeef6a22fd/download/virginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Washington - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/055d7dbc-8188-4dcd-af0c-ed12caad53b3/download/washington.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/055d7dbc-8188-4dcd-af0c-ed12caad53b3/download/washington.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "West Virginia - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/3d8181f6-20b7-46b3-8330-7b384f268791/download/westvirginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/3d8181f6-20b7-46b3-8330-7b384f268791/download/westvirginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Wisconsin - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/ee29fdc8-3473-43ce-ad2e-2978c0ec54fd/download/wisconsin.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/ee29fdc8-3473-43ce-ad2e-2978c0ec54fd/download/wisconsin.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Wyoming - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/51d888e0-9c7f-48f7-9f7e-131b127c0fcf/download/wyoming.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/7724253b-c98a-4ada-b1e4-0849665dfcce/resource/51d888e0-9c7f-48f7-9f7e-131b127c0fcf/download/wyoming.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 }
             ],
+            "identifier": "785a64bc-9fd8-4704-a814-bde3bb15738a",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "compensatory-education",
@@ -56338,22 +56321,11 @@
                 "supplemental-educational-serices",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:26:24.247649",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ESEA Title I LEA allocations - FY 2002",
-            "description": "Archived: Tables (in PDF and EXCEL formats) showing FY 2002 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
-            "modified": "2023-07-06T22:25:22.880470",
-            "accessLevel": "public",
-            "identifier": "48166173-3f40-4957-bc40-585f6b290c8f",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -56370,430 +56342,441 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "ESEA Title I LEA allocations - FY 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ODS",
                 "hasEmail": "mailto:ods@ed.gov"
             },
+            "description": "Archived: Tables (in PDF and EXCEL formats) showing FY 2002 ESEA Title I LEA Allocations, as well as estimated amounts available for choice-related transportation and supplemental educational services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alabama",
                     "description": "Alabama - Alabama",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/476e3686-a080-4ffb-8e5d-7f97dcc78256/download/alabama.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/476e3686-a080-4ffb-8e5d-7f97dcc78256/download/alabama.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alabama"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Alaska",
                     "description": "Alaska - Alaska",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/1d575ddd-f516-44b8-b8e4-be9340905668/download/alaska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/1d575ddd-f516-44b8-b8e4-be9340905668/download/alaska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alaska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arizona",
                     "description": "Arizona - Arizona",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/16da30ce-97e8-4247-8ece-cafdeaa665be/download/arizona.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/16da30ce-97e8-4247-8ece-cafdeaa665be/download/arizona.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arizona"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Arkansas",
                     "description": "Arkansas - Arkansas",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/fc9af118-9c8d-4124-9925-2f1ce655bd28/download/arkansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/fc9af118-9c8d-4124-9925-2f1ce655bd28/download/arkansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Arkansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "California",
                     "description": "California - California",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/26db6f37-bb8d-4506-8485-acb4990e19bf/download/california.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/26db6f37-bb8d-4506-8485-acb4990e19bf/download/california.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "California"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Colorado",
                     "description": "Colorado - Colorado",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/9677719b-ab45-42e8-b370-ebfefa112798/download/colorado.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/9677719b-ab45-42e8-b370-ebfefa112798/download/colorado.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Colorado"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Connecticut",
                     "description": "Connecticut - Connecticut",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/8e37c6fb-ff6d-4c32-836a-c6af8742d85c/download/connecticut.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/8e37c6fb-ff6d-4c32-836a-c6af8742d85c/download/connecticut.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Connecticut"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Delaware",
                     "description": "Delaware - Delaware",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/0563d47f-2d8d-41b9-b1dc-e1da224df995/download/delaware.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/0563d47f-2d8d-41b9-b1dc-e1da224df995/download/delaware.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Delaware"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "District of Columbia",
                     "description": "District of Columbia - District of Columbia",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/02990105-80db-45d1-b641-56a49eeefed7/download/dc.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/02990105-80db-45d1-b641-56a49eeefed7/download/dc.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "District of Columbia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Florida",
                     "description": "Florida - Florida",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/1f891795-47d1-487a-9346-5798f6b24f09/download/florida.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/1f891795-47d1-487a-9346-5798f6b24f09/download/florida.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Florida"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Georgia",
                     "description": "Georgia - Georgia",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/20d8180e-c5fc-4668-8cca-2d7df5974fc3/download/georgia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/20d8180e-c5fc-4668-8cca-2d7df5974fc3/download/georgia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Georgia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Hawaii",
                     "description": "Hawaii - Hawaii",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/ee5e66c1-3de9-43a8-8112-2d17555838be/download/hawaii.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/ee5e66c1-3de9-43a8-8112-2d17555838be/download/hawaii.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Hawaii"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Idaho",
                     "description": "Idaho - Idaho",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/c169ea98-2084-4d75-93d4-59ea91fa3ea0/download/idaho.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/c169ea98-2084-4d75-93d4-59ea91fa3ea0/download/idaho.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Idaho"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Illinois",
                     "description": "Illinois - Illinois",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/18a36553-e862-4bb7-b9a4-920e97a5afb8/download/illinois.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/18a36553-e862-4bb7-b9a4-920e97a5afb8/download/illinois.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illinois"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Indiana",
                     "description": "Indiana - Indiana",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/164893fd-f76a-4745-874e-94bca75a1c7a/download/indiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/164893fd-f76a-4745-874e-94bca75a1c7a/download/indiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Indiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Iowa",
                     "description": "Iowa - Iowa",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/51b5d563-24e2-47a3-9596-7910dd42b9c6/download/iowa.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/51b5d563-24e2-47a3-9596-7910dd42b9c6/download/iowa.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Iowa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kansas",
                     "description": "Kansas - Kansas",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/3803f1cf-3e65-4f0d-8b95-71dc88005b4f/download/kansas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/3803f1cf-3e65-4f0d-8b95-71dc88005b4f/download/kansas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kansas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Kentucky",
                     "description": "Kentucky - Kentucky",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/fea4ceb5-a7f0-4dc1-9f16-4b38dcd645c8/download/kentucky.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/fea4ceb5-a7f0-4dc1-9f16-4b38dcd645c8/download/kentucky.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Kentucky"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Louisiana",
                     "description": "Louisiana - Louisiana",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/f6d8cfe9-2049-40d6-ab23-75ca8d5dcc32/download/louisiana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/f6d8cfe9-2049-40d6-ab23-75ca8d5dcc32/download/louisiana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Louisiana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maine",
                     "description": "Maine - Maine",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/892b9fb4-fbde-4c46-b97f-73a26f81be9c/download/maine.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/892b9fb4-fbde-4c46-b97f-73a26f81be9c/download/maine.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maine"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Maryland",
                     "description": "Maryland - Maryland",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/787d49e7-73ff-4ee6-b4c2-30d2d88e9e8a/download/maryland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/787d49e7-73ff-4ee6-b4c2-30d2d88e9e8a/download/maryland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Maryland"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Massachusetts",
                     "description": "Massachusetts - Massachusetts",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/4b35c7d3-cf62-4767-be48-402c1c93b8e3/download/massachusetts.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/4b35c7d3-cf62-4767-be48-402c1c93b8e3/download/massachusetts.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Massachusetts"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Michigan",
                     "description": "Michigan - Michigan",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/343d8016-ce29-48c3-946f-94d64d608068/download/michigan.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/343d8016-ce29-48c3-946f-94d64d608068/download/michigan.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Michigan"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Minnesota",
                     "description": "Minnesota - Minnesota",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/103ff3c4-3c02-4faa-be1c-bc8b5ba01071/download/minnesota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/103ff3c4-3c02-4faa-be1c-bc8b5ba01071/download/minnesota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Minnesota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Mississippi",
                     "description": "Mississippi - Mississippi",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/0dd8dc66-518a-4df7-8f81-1e0be929f121/download/mississippi.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/0dd8dc66-518a-4df7-8f81-1e0be929f121/download/mississippi.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mississippi"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Missouri",
                     "description": "Missouri - Missouri",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/eaaa43bc-156c-463a-9307-d786fcb4ef83/download/missouri.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/eaaa43bc-156c-463a-9307-d786fcb4ef83/download/missouri.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Missouri"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Montana",
                     "description": "Montana - Montana",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/3c585731-76a0-4443-b28e-a63c2f61a9f7/download/montana.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/3c585731-76a0-4443-b28e-a63c2f61a9f7/download/montana.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Montana"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nebraska",
                     "description": "Nebraska - Nebraska",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/4d13fdf5-04ff-4217-a52c-b4c7462675bc/download/nebraska.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/4d13fdf5-04ff-4217-a52c-b4c7462675bc/download/nebraska.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nebraska"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Nevada",
                     "description": "Nevada - Nevada",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/c3b2b912-b5ab-45bd-8138-1ed598279574/download/nevada.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/c3b2b912-b5ab-45bd-8138-1ed598279574/download/nevada.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nevada"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Hampshire",
                     "description": "New Hampshire - New Hampshire",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/409bcc89-b1b8-4ddc-b704-6b409d73453a/download/newhampshire.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/409bcc89-b1b8-4ddc-b704-6b409d73453a/download/newhampshire.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Hampshire"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Jersey",
                     "description": "New Jersey - New Jersey",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/75b81840-80d0-4f9e-9853-18ef426e5219/download/newjersey.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/75b81840-80d0-4f9e-9853-18ef426e5219/download/newjersey.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Jersey"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New Mexico",
                     "description": "New Mexico - New Mexico",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/118079bc-ac52-4440-8720-1c1a85c50e7c/download/newmexico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/118079bc-ac52-4440-8720-1c1a85c50e7c/download/newmexico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New Mexico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "New York",
                     "description": "New York - New York",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/fe86f58b-0f9f-44b0-9678-56a9d069cd8b/download/newyork.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/fe86f58b-0f9f-44b0-9678-56a9d069cd8b/download/newyork.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "New York"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Carolina",
                     "description": "North Carolina - North Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/d9b9651e-895f-45fc-9d4f-dcbe2d375870/download/northcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/d9b9651e-895f-45fc-9d4f-dcbe2d375870/download/northcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "North Dakota",
                     "description": "North Dakota - North Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/8009e31d-baec-4b95-a757-5fe3a268a351/download/northdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/8009e31d-baec-4b95-a757-5fe3a268a351/download/northdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "North Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Ohio",
                     "description": "Ohio - Ohio",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/2405aa34-2989-4d10-97a6-e013b973f307/download/ohio.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/2405aa34-2989-4d10-97a6-e013b973f307/download/ohio.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Ohio"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oklahoma",
                     "description": "Oklahoma - Oklahoma",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/c9058f1f-2d6e-4b99-bf59-974bbea065e1/download/oklahoma.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/c9058f1f-2d6e-4b99-bf59-974bbea065e1/download/oklahoma.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oklahoma"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Oregon",
                     "description": "Oregon - Oregon",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/1c2ab037-9bca-4ecd-9280-3fe065395923/download/oregon.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/1c2ab037-9bca-4ecd-9280-3fe065395923/download/oregon.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Oregon"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Pennsylvania",
                     "description": "Pennsylvania - Pennsylvania",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/c52a4492-bc4c-4713-90b8-9cd497c66c41/download/pennsylvania.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/c52a4492-bc4c-4713-90b8-9cd497c66c41/download/pennsylvania.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Pennsylvania"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Puerto Rico",
                     "description": "Puerto Rico - Puerto Rico",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/a464f115-b2e4-4699-8cfa-f580d4b1bf32/download/puertorico.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/a464f115-b2e4-4699-8cfa-f580d4b1bf32/download/puertorico.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Puerto Rico"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Rhode Island",
                     "description": "Rhode Island - Rhode Island",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/e8ced970-30fa-4abf-9d7d-731d76d125f9/download/rhodeisland.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/e8ced970-30fa-4abf-9d7d-731d76d125f9/download/rhodeisland.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rhode Island"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Carolina",
                     "description": "South Carolina - South Carolina",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/0b1b7a5c-4a7a-4419-8d71-37ef534e7618/download/southcarolina.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/0b1b7a5c-4a7a-4419-8d71-37ef534e7618/download/southcarolina.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Carolina"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "South Dakota",
                     "description": "South Dakota - South Dakota",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/b78d7dcb-f2cd-4b88-809e-b5255ea4a2a6/download/southdakota.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/b78d7dcb-f2cd-4b88-809e-b5255ea4a2a6/download/southdakota.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "South Dakota"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Tennessee",
                     "description": "Tennessee - Tennessee",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/7d69c709-8c56-4401-9b54-a09fd60f35e0/download/tennessee.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/7d69c709-8c56-4401-9b54-a09fd60f35e0/download/tennessee.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Tennessee"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Texas",
                     "description": "Texas - Texas",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/a953ada8-c6ae-44f3-b321-3f360e3ae2b0/download/texas.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/a953ada8-c6ae-44f3-b321-3f360e3ae2b0/download/texas.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Texas"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Utah",
                     "description": "Utah - Utah",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/3a6d6ece-74a0-477b-a9c0-8c2e5e2d540a/download/utah.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/3a6d6ece-74a0-477b-a9c0-8c2e5e2d540a/download/utah.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Utah"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Vermont",
                     "description": "Vermont - Vermont",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/ab6f32af-4098-4e41-b298-f66e69dc4897/download/vermont.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/ab6f32af-4098-4e41-b298-f66e69dc4897/download/vermont.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Vermont"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Virginia",
                     "description": "Virginia - Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/0870ca40-00d9-4481-9508-66a8958b02e3/download/virginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/0870ca40-00d9-4481-9508-66a8958b02e3/download/virginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Washington",
                     "description": "Washington - Washington",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/99dc0cfd-e762-4895-b717-9788f574465e/download/washington.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/99dc0cfd-e762-4895-b717-9788f574465e/download/washington.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Washington"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "West Virginia",
                     "description": "West Virginia - West Virginia",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/d34e1812-5d98-41ab-a978-e6af265d64dd/download/westvirginia.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/d34e1812-5d98-41ab-a978-e6af265d64dd/download/westvirginia.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "West Virginia"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wisconsin",
                     "description": "Wisconsin - Wisconsin",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/93214660-2c17-4e39-80b7-a756a6aa1254/download/wisconsin.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/93214660-2c17-4e39-80b7-a756a6aa1254/download/wisconsin.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wisconsin"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Wyoming",
                     "description": "Wyoming - Wyoming",
-                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/0b79e1f0-cdac-4fda-8d70-57076ba43b9b/download/wyoming.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/9de3cf1a-d536-4c33-bd6e-e73cc994891b/resource/0b79e1f0-cdac-4fda-8d70-57076ba43b9b/download/wyoming.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Wyoming"
                 }
             ],
+            "identifier": "48166173-3f40-4957-bc40-585f6b290c8f",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "compensatory-education",
@@ -56808,28 +56791,14 @@
                 "supplemental-educational-serices",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:25:22.880470",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Fund for the Improvement of Postsecondary Education (FIPSE): Award-Winning Projects",
-            "description": "The Fund for the Improvement of Postsecondary Education (FIPSE) provides grants to support innovative educational reform projects that can serve as national models for the improvement of postsecondary education.  This file provides links to award-winning FIPSE-funded projects.",
-            "modified": "2023-07-06T22:23:39.309452",
-            "accessLevel": "public",
-            "identifier": "8d16af1e-b139-47f6-8f05-6e4261eefda4",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                "name": "Office of Finance and Operations (OFO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -56842,32 +56811,42 @@
                         }
                     }
                 }
-                }
             },
+            "spatial": "United States",
+            "title": "ESEA Title I LEA allocations - FY 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "The Fund for the Improvement of Postsecondary Education (FIPSE) provides grants to support innovative educational reform projects that can serve as national models for the improvement of postsecondary education.  This file provides links to award-winning FIPSE-funded projects.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Chronological Listing",
                     "description": "Chronological Listing -",
-                    "downloadURL": "https://data.ed.gov/dataset/6f9b1ddf-5a7c-471c-bc86-c33a5e4cbcd0/resource/900fa355-398d-4d51-a702-8d8b95e7fa7d/download/awardwinning-chrono.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/6f9b1ddf-5a7c-471c-bc86-c33a5e4cbcd0/resource/900fa355-398d-4d51-a702-8d8b95e7fa7d/download/awardwinning-chrono.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Chronological Listing"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "MS Excel",
                     "description": "-",
-                    "downloadURL": "https://data.ed.gov/dataset/6f9b1ddf-5a7c-471c-bc86-c33a5e4cbcd0/resource/82897830-dd4f-4a4a-89fa-eaaa0cd14996/download/natlawardprograms.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/6f9b1ddf-5a7c-471c-bc86-c33a5e4cbcd0/resource/82897830-dd4f-4a4a-89fa-eaaa0cd14996/download/natlawardprograms.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "MS Excel"
                 }
             ],
+            "identifier": "8d16af1e-b139-47f6-8f05-6e4261eefda4",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "fipse",
@@ -56881,25 +56860,17 @@
                 "postsecondary-education",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:23:39.309452",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Disability Employment 101 For Your Business",
-            "description": "A 2007 brochure that targets small- and medium-sized businesses that may or may not have thought of increasing their hiring pool by hiring employees with disabilities and serves as a companion to the 2007 Disability Employment 101 guide.",
-            "modified": "2023-07-06T22:22:27.116157",
-            "accessLevel": "public",
-            "identifier": "99aaa82b-566e-4d6b-8cf7-237f79d7dfa1",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                "name": "Office of Postsecondary Education (OPE)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -56912,23 +56883,35 @@
                             }
                         }
                     }
+                }
+            },
+            "spatial": "United States",
+            "title": "Fund for the Improvement of Postsecondary Education (FIPSE): Award-Winning Projects"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andrew Kerns",
                 "hasEmail": "mailto:rsadata@ed.gov"
             },
+            "description": "A 2007 brochure that targets small- and medium-sized businesses that may or may not have thought of increasing their hiring pool by hiring employees with disabilities and serves as a companion to the 2007 Disability Employment 101 guide.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/plain",
-                    "format": "TXT",
-                    "title": "PDF",
                     "description": "Disability Employment 101 For Your Business -",
-                    "downloadURL": "https://data.ed.gov/dataset/ce5855c7-2cdc-4d42-ab4a-638fc730a85e/resource/4f6e07a3-c161-441f-91b2-af5fc112f579/download/eg101-brochure.txt"
+                    "downloadURL": "https://data.ed.gov/dataset/ce5855c7-2cdc-4d42-ab4a-638fc730a85e/resource/4f6e07a3-c161-441f-91b2-af5fc112f579/download/eg101-brochure.txt",
+                    "format": "TXT",
+                    "mediaType": "text/plain",
+                    "title": "PDF"
                 }
             ],
+            "identifier": "99aaa82b-566e-4d6b-8cf7-237f79d7dfa1",
             "keyword": [
                 "d9ef757b-555e-4337-8247-a8cc5a42ef23",
                 "disabilities",
@@ -56939,22 +56922,11 @@
                 "osers",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:20"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:22:27.116157",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Disability Employment 101",
-            "description": "The updated (August 2007) Disability Employment 101 guide is a comprehensive analysis of hiring employees with disabilities that includes information about how to find qualified workers with disabilities, how to put disability and employment research into practice and how to model what other businesses have done to successfully integrate individuals with disabilities into the workforce.",
-            "modified": "2023-07-06T22:21:37.551652",
-            "accessLevel": "public",
-            "identifier": "136e6e61-71ac-485c-9f50-a53bd427b30e",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Special Education and Rehabilitative Services (OSERS)",
@@ -56971,21 +56943,32 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Disability Employment 101 For Your Business"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OSERS",
                 "hasEmail": "mailto:osers@ed.gov"
             },
+            "description": "The updated (August 2007) Disability Employment 101 guide is a comprehensive analysis of hiring employees with disabilities that includes information about how to find qualified workers with disabilities, how to put disability and employment research into practice and how to model what other businesses have done to successfully integrate individuals with disabilities into the workforce.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/plain",
-                    "format": "TXT",
-                    "title": "Text",
                     "description": "Disability Employment 101 -",
-                    "downloadURL": "https://data.ed.gov/dataset/fa6a8c46-29f1-4aa3-b840-2713508487ee/resource/d53aecc5-ea2a-412c-84b3-f6243c2621e7/download/disabilityemployment101.txt"
+                    "downloadURL": "https://data.ed.gov/dataset/fa6a8c46-29f1-4aa3-b840-2713508487ee/resource/d53aecc5-ea2a-412c-84b3-f6243c2621e7/download/disabilityemployment101.txt",
+                    "format": "TXT",
+                    "mediaType": "text/plain",
+                    "title": "Text"
                 }
             ],
+            "identifier": "136e6e61-71ac-485c-9f50-a53bd427b30e",
             "keyword": [
                 "d9ef757b-555e-4337-8247-a8cc5a42ef23",
                 "disabilities",
@@ -56996,25 +56979,14 @@
                 "osers",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:20"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:21:37.551652",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Education Budget Tables",
-            "description": "The Budget Tables page provides links to tables that illustrate key aspects of the Education Department Budget.",
-            "modified": "2023-07-06T22:20:47.084301",
-            "accessLevel": "public",
-            "identifier": "77d0ba08-b2f1-4c75-a5ff-52a1d04fea60",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Finance and Operations (OFO)",
+                "name": "Office of Special Education and Rehabilitative Services (OSERS)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -57028,190 +57000,201 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Disability Employment 101"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OFO",
                 "hasEmail": "mailto:ofo@ed.gov"
             },
+            "description": "The Budget Tables page provides links to tables that illustrate key aspects of the Education Department Budget.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2021 President\u2019s Budget Request",
                     "description": "FY 2021 President\u2019s Budget Request  - FY 2021 President\u2019s Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/3b0fa7ba-d925-441f-a509-f1cde5abb2db/download/21pbapt.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/3b0fa7ba-d925-441f-a509-f1cde5abb2db/download/21pbapt.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2021 President\u2019s Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2020 Congressional Action",
                     "description": "FY 2020 Congressional Action - FY 2020 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/f5d00bcf-b58e-4914-ba29-a03440e63a9f/download/20action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/f5d00bcf-b58e-4914-ba29-a03440e63a9f/download/20action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2020 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2020 President's Budget Request",
                     "description": "FY 2020 President's Budget Request - FY 2020 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/152b3a61-0150-4104-94a1-76f5ed7ce276/download/20pbapt.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/152b3a61-0150-4104-94a1-76f5ed7ce276/download/20pbapt.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2020 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2019 Congressional Action",
                     "description": "FY 2019 Congressional Action - FY 2019 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/1ff84082-6e9e-49e5-9ccb-153e62cdfc3e/download/19action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/1ff84082-6e9e-49e5-9ccb-153e62cdfc3e/download/19action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2019 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2019 President's Budget Request",
                     "description": "FY 2019 President's Budget Request - FY 2019 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/ed2007c2-2036-4c95-87cf-066394b20d19/download/19pbapt.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/ed2007c2-2036-4c95-87cf-066394b20d19/download/19pbapt.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2019 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2018 Congressional Action",
                     "description": "FY 2018 Congressional Action - FY 2018 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/d0b11352-3ac4-4304-a037-af01a1f75c46/download/18action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/d0b11352-3ac4-4304-a037-af01a1f75c46/download/18action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2018 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2018 President's Budget Request",
                     "description": "FY 2018 President's Budget Request - FY 2018 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/4ae580a5-8e75-43bb-a357-0643c0a7cb9d/download/18pbapt.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/4ae580a5-8e75-43bb-a357-0643c0a7cb9d/download/18pbapt.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2018 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Agency Financial Report (AFR)",
                     "description": "Agency Financial Report (AFR)  - Agency Financial Report (AFR)",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/b71791aa-42b0-48d2-985a-d8930f38de8f/download/idrtables.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/b71791aa-42b0-48d2-985a-d8930f38de8f/download/idrtables.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Agency Financial Report (AFR)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2017 Congressional Action",
                     "description": "FY 2017 Congressional Action - FY 2017 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/44015eab-4b7d-40bc-992f-cc82db66f677/download/17action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/44015eab-4b7d-40bc-992f-cc82db66f677/download/17action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2017 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2017 President's Budget Request",
                     "description": "FY 2017 President's Budget Request - FY 2017 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/039cc04c-4658-424c-82b3-5fedf1feab51/download/17pbapt.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/039cc04c-4658-424c-82b3-5fedf1feab51/download/17pbapt.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2017 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2016 Congressional Action",
                     "description": "FY 2016 Congressional Action  - FY 2016 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/890e26cb-2195-4a2d-a5f5-56e763bc045e/download/16action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/890e26cb-2195-4a2d-a5f5-56e763bc045e/download/16action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2016 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2016 President's Budget Request",
                     "description": "FY 2016 President's Budget Request - FY 2016 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/2bd2eb98-905a-4b15-8338-87ea4ce19ae7/download/16pbapt.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/2bd2eb98-905a-4b15-8338-87ea4ce19ae7/download/16pbapt.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2016 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2015 Congressional Action",
                     "description": "FY 2015 Congressional Action  - FY 2015 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/18b61690-9fcb-456b-9af5-e354df2a069b/download/15action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/18b61690-9fcb-456b-9af5-e354df2a069b/download/15action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2015 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2015 President's Budget Request",
                     "description": "FY 2015 President's Budget Request - FY 2015 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/be230380-39c1-432d-bf33-56e2cb60711c/download/15pbapt.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/be230380-39c1-432d-bf33-56e2cb60711c/download/15pbapt.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2015 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2014 Congressional Action",
                     "description": "FY 2014 Congressional Action  - FY 2014 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/4416df45-ff44-4e7d-bd37-6fabd21aed06/download/14action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/4416df45-ff44-4e7d-bd37-6fabd21aed06/download/14action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2014 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2014 President's Budget Request",
                     "description": "FY 2014 President's Budget Request - FY 2014 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/4c45ab11-bc3a-4fed-9e20-b3c6378573a2/download/14pbapt.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/4c45ab11-bc3a-4fed-9e20-b3c6378573a2/download/14pbapt.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2014 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2013 Congressional Action",
                     "description": "FY 2013 Congressional Action  - FY 2013 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/e4f53a8f-16cc-48cf-a25d-98df24415f0d/download/13action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/e4f53a8f-16cc-48cf-a25d-98df24415f0d/download/13action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2013 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2012 Congressional Action",
                     "description": "FY 2012 Congressional Action - FY 2012 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/c7c29a4c-c374-40b4-95ae-c4ae22a8e4f9/download/12action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/c7c29a4c-c374-40b4-95ae-c4ae22a8e4f9/download/12action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2012 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2011 Congressional Action",
                     "description": "FY 2011 Congressional Action - FY 2011 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/5c6d74c8-11c8-4fe3-82bf-44d46b5d5188/download/11action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/5c6d74c8-11c8-4fe3-82bf-44d46b5d5188/download/11action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2011 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2011 Congressional Action",
                     "description": "FY 2011 Congressional Action - FY 2011 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/49b86f7b-3360-422f-b94a-db987eea3e22/download/compare11action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/49b86f7b-3360-422f-b94a-db987eea3e22/download/compare11action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2011 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Summary of ED Discretionary Funds",
                     "description": "Summary of ED Discretionary Funds - Summary of ED Discretionary Funds",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/338df716-62b9-4c29-925b-bceba7b77593/download/appendix1.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/338df716-62b9-4c29-925b-bceba7b77593/download/appendix1.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Summary of ED Discretionary Funds"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Summary of ED Mandatory Funds",
                     "description": "Summary of ED Mandatory Funds - Summary of ED Mandatory Funds",
-                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/46b72bfc-7007-4a3d-941d-f3c3b50cf8d1/download/appendix2.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/3683c899-b7b5-4ad4-9b5d-152d197ab389/resource/46b72bfc-7007-4a3d-941d-f3c3b50cf8d1/download/appendix2.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Summary of ED Mandatory Funds"
                 }
             ],
+            "identifier": "77d0ba08-b2f1-4c75-a5ff-52a1d04fea60",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "appropriations",
@@ -57224,22 +57207,11 @@
                 "ofo",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:20:47.084301",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Education Budget Tables",
-            "description": "The Budget Tables page provides links to tables that illustrate key aspects of the Education Department Budget.",
-            "modified": "2023-07-06T22:19:04.256818",
-            "accessLevel": "public",
-            "identifier": "e1bd40c4-fc8b-44d8-ad66-7621b191997d",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -57256,189 +57228,200 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Department of Education Budget Tables"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OFO",
                 "hasEmail": "mailto:ofo@ed.gov"
             },
+            "description": "The Budget Tables page provides links to tables that illustrate key aspects of the Education Department Budget.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2021 President\u2019s Budget Request",
                     "description": "FY 2021 President\u2019s Budget Request  - FY 2021 President\u2019s Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/2768ee1e-1040-40d8-aaa5-f521c4935a5c/download/21pbapt.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/2768ee1e-1040-40d8-aaa5-f521c4935a5c/download/21pbapt.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2021 President\u2019s Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2020 Congressional Action",
                     "description": "FY 2020 Congressional Action - FY 2020 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/881d0016-a6fc-46fb-928c-a35670ed0527/download/20action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/881d0016-a6fc-46fb-928c-a35670ed0527/download/20action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2020 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2020 President's Budget Request",
                     "description": "FY 2020 President's Budget Request - FY 2020 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/7baea077-7023-4996-a331-effe94aa387c/download/20pbapt.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/7baea077-7023-4996-a331-effe94aa387c/download/20pbapt.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2020 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2019 Congressional Action",
                     "description": "FY 2019 Congressional Action - FY 2019 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/0fb03945-e6e7-4993-a82a-db2e795d5f84/download/19action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/0fb03945-e6e7-4993-a82a-db2e795d5f84/download/19action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2019 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2019 President's Budget Request",
                     "description": "FY 2019 President's Budget Request - FY 2019 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/2f9a0b20-c90c-4384-b6f2-2e5972fec7d2/download/19pbapt.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/2f9a0b20-c90c-4384-b6f2-2e5972fec7d2/download/19pbapt.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2019 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2018 Congressional Action",
                     "description": "FY 2018 Congressional Action - FY 2018 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/6eedc764-a805-4c16-9a53-379d59308c94/download/18action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/6eedc764-a805-4c16-9a53-379d59308c94/download/18action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2018 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2018 President's Budget Request",
                     "description": "FY 2018 President's Budget Request - FY 2018 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/0e602401-5377-4f4a-be48-013176d93ddb/download/18pbapt.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/0e602401-5377-4f4a-be48-013176d93ddb/download/18pbapt.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2018 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Agency Financial Report (AFR)",
                     "description": "Agency Financial Report (AFR)  - Agency Financial Report (AFR)",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/a821ca37-c543-4341-a2eb-7bf02cc19101/download/idrtables.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/a821ca37-c543-4341-a2eb-7bf02cc19101/download/idrtables.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Agency Financial Report (AFR)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2017 Congressional Action",
                     "description": "FY 2017 Congressional Action - FY 2017 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/4864c485-70bf-4fd5-9469-06e1ee382de6/download/17action.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/4864c485-70bf-4fd5-9469-06e1ee382de6/download/17action.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2017 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "FY 2017 President's Budget Request",
                     "description": "FY 2017 President's Budget Request - FY 2017 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/5378ae31-2e94-4ca5-ac48-e04f29e2e463/download/17pbapt.xlsx"
-                },
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/5378ae31-2e94-4ca5-ac48-e04f29e2e463/download/17pbapt.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FY 2017 President's Budget Request"
+                },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2016 Congressional Action",
                     "description": "FY 2016 Congressional Action  - FY 2016 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/a1f5d893-04c7-4be6-aef8-d58657d3757b/download/16action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/a1f5d893-04c7-4be6-aef8-d58657d3757b/download/16action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2016 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2016 President's Budget Request",
                     "description": "FY 2016 President's Budget Request - FY 2016 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/30d39b19-cc5c-43f3-bab4-11ed553af6a1/download/16pbapt.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/30d39b19-cc5c-43f3-bab4-11ed553af6a1/download/16pbapt.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2016 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2015 Congressional Action",
                     "description": "FY 2015 Congressional Action  - FY 2015 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/cac1edc8-8b18-46c6-83b9-82241af1d3a4/download/15action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/cac1edc8-8b18-46c6-83b9-82241af1d3a4/download/15action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2015 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2015 President's Budget Request",
                     "description": "FY 2015 President's Budget Request - FY 2015 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/b333f5a2-afbf-4abb-8e48-14c42c485de0/download/15pbapt.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/b333f5a2-afbf-4abb-8e48-14c42c485de0/download/15pbapt.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2015 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2014 Congressional Action",
                     "description": "FY 2014 Congressional Action  - FY 2014 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/26ca945b-5347-4dfe-b11e-62abdeedbefa/download/14action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/26ca945b-5347-4dfe-b11e-62abdeedbefa/download/14action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2014 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2014 President's Budget Request",
                     "description": "FY 2014 President's Budget Request - FY 2014 President's Budget Request",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/72bc2206-74bc-4412-8e31-9aa4d448891f/download/14pbapt.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/72bc2206-74bc-4412-8e31-9aa4d448891f/download/14pbapt.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2014 President's Budget Request"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2013 Congressional Action",
                     "description": "FY 2013 Congressional Action  - FY 2013 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/9c02ab91-1007-4e4a-96cf-f8ae33f195e9/download/13action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/9c02ab91-1007-4e4a-96cf-f8ae33f195e9/download/13action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2013 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2012 Congressional Action",
                     "description": "FY 2012 Congressional Action - FY 2012 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/02712991-771c-478a-90f3-8c296bb75516/download/12action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/02712991-771c-478a-90f3-8c296bb75516/download/12action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2012 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2011 Congressional Action",
                     "description": "FY 2011 Congressional Action - FY 2011 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/0a3300bd-6960-4435-8315-729dd845b0a4/download/11action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/0a3300bd-6960-4435-8315-729dd845b0a4/download/11action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2011 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "FY 2011 Congressional Action",
                     "description": "FY 2011 Congressional Action - FY 2011 Congressional Action",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/fb6a8392-e3d1-4adc-9637-996f542069d0/download/compare11action.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/fb6a8392-e3d1-4adc-9637-996f542069d0/download/compare11action.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY 2011 Congressional Action"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Summary of ED Discretionary Funds",
                     "description": "Summary of ED Discretionary Funds - Summary of ED Discretionary Funds",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/6ab8cba7-a1fc-4900-b5d2-30fb5b48660f/download/appendix1.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/6ab8cba7-a1fc-4900-b5d2-30fb5b48660f/download/appendix1.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Summary of ED Discretionary Funds"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Summary of ED Mandatory Funds",
                     "description": "Summary of ED Mandatory Funds - Summary of ED Mandatory Funds",
-                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/8eb4cb5b-a19e-4715-8909-2057104e54c9/download/appendix2.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/674264d7-d2cb-4be1-9d93-20f0d8acf661/resource/8eb4cb5b-a19e-4715-8909-2057104e54c9/download/appendix2.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Summary of ED Mandatory Funds"
                 }
             ],
+            "identifier": "e1bd40c4-fc8b-44d8-ad66-7621b191997d",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "appropriations",
@@ -57450,22 +57433,11 @@
                 "ofo",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:19:04.256818",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Contracts & Acquisitions Management Home Page",
-            "description": "Information on contracting and purchasing at the Department of Education.  Instructions for requesting an RFP, upcoming contracts, contractor registrations, and notices from the FedBizOpps are available",
-            "modified": "2023-07-06T22:18:11.183095",
-            "accessLevel": "public",
-            "identifier": "d0eed15a-e33f-454b-9783-6a71e8fc533c",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Finance and Operations (OFO)",
@@ -57482,22 +57454,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Department of Education Budget Tables"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OCFO",
                 "hasEmail": "mailto:ocfo@ed.gov"
             },
+            "description": "Information on contracting and purchasing at the Department of Education.  Instructions for requesting an RFP, upcoming contracts, contractor registrations, and notices from the FedBizOpps are available",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Active Contracts",
                     "description": "Active Contracts - Active Contracts",
-                    "downloadURL": "https://data.ed.gov/dataset/0cd839fc-f5b1-4f04-8641-2fe9e9f2e71b/resource/9802273b-9ef4-4341-8cdd-1489195f9324/download/active-contracts-list0420.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/0cd839fc-f5b1-4f04-8641-2fe9e9f2e71b/resource/9802273b-9ef4-4341-8cdd-1489195f9324/download/active-contracts-list0420.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Active Contracts"
                 }
             ],
+            "identifier": "d0eed15a-e33f-454b-9783-6a71e8fc533c",
             "keyword": [
                 "972677fb-76cd-4b5e-987c-ff072f2df910",
                 "awards",
@@ -57508,26 +57491,14 @@
                 "proposal-writing",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T22:18:11.183095",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Comparability of State and Local Expenditures Among Schools Within Districts 2011",
-            "description": "Comparability of State and Local Expenditures Among Schools Within Districts: A Report From the Study of School-Level Expenditures (2011). This report presents findings from the first-ever national data collection on school-level expenditures, collected in response to a requirement in the American Recovery and Reinvestment Act of 2009 (ARRA). The report examines the distribution of state and local education expenditures at the school level, including comparisons between Title I and non-Title I schools and between higher-poverty and lower-poverty schools.",
-            "modified": "2023-07-06T22:16:41.696328",
-            "accessLevel": "public",
-            "identifier": "dce0276b-6956-403e-9060-affe0f61cc63",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
-            "temporal": "2011-09-01/2012-05-31",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Planning, Evaluation and Policy Development (OPEPD)",
+                "name": "Office of Finance and Operations (OFO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -57541,22 +57512,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Contracts & Acquisitions Management Home Page"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OCDO",
                 "hasEmail": "mailto:OCDO@ed.gov"
             },
+            "description": "Comparability of State and Local Expenditures Among Schools Within Districts: A Report From the Study of School-Level Expenditures (2011). This report presents findings from the first-ever national data collection on school-level expenditures, collected in response to a requirement in the American Recovery and Reinvestment Act of 2009 (ARRA). The report examines the distribution of state and local education expenditures at the school level, including comparisons between Title I and non-Title I schools and between higher-poverty and lower-poverty schools.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "dataset school level expenditures",
                     "description": "dataset school level expenditures",
-                    "downloadURL": "https://data.ed.gov/dataset/557582d9-84c6-4659-bed7-2ac00dc6e846/resource/755bf1af-b92a-46da-9447-1bfb09e11a63/download/ssleda2.zip"
+                    "downloadURL": "https://data.ed.gov/dataset/557582d9-84c6-4659-bed7-2ac00dc6e846/resource/755bf1af-b92a-46da-9447-1bfb09e11a63/download/ssleda2.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "dataset school level expenditures"
                 }
             ],
+            "identifier": "dce0276b-6956-403e-9060-affe0f61cc63",
             "keyword": [
                 "arra",
                 "expenditures",
@@ -57567,28 +57549,14 @@
                 "title-i",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2023-07-06T22:16:41.696328",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "CARES Act: Higher Education Emergency Relief Fund",
-            "description": "Congress set aside approximately $14.25 billion of the $30.75 billion allotted to the Education Stabilization Fund through the CARES Act for the Higher Education Emergency Relief Fund (HEERF).  The Department will award these grants \ufffdto institutions of higher education (IHE) based on a formula stipulated in the legislation.",
-            "modified": "2023-07-06T20:44:07.898082",
-            "accessLevel": "public",
-            "identifier": "992b42a6-2ede-404a-8253-8dad6f701f65",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                "name": "Office of Planning, Evaluation and Policy Development (OPEPD)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -57601,48 +57569,59 @@
                         }
                     }
                 }
-                }
             },
+            "spatial": "United States",
+            "temporal": "2011-09-01/2012-05-31",
+            "title": "Comparability of State and Local Expenditures Among Schools Within Districts 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "Congress set aside approximately $14.25 billion of the $30.75 billion allotted to the Education Stabilization Fund through the CARES Act for the Higher Education Emergency Relief Fund (HEERF).  The Department will award these grants \ufffdto institutions of higher education (IHE) based on a formula stipulated in the legislation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Allocations for Section 18004(a)(2) of CARES Act:",
                     "description": "Allocations for Section 18004(a)(2) of CARES Act: - EXCEL",
-                    "downloadURL": "https://data.ed.gov/dataset/c213b768-c40c-41df-80d4-d9eec9c4c67d/resource/44be1955-f07b-4fca-af10-f16c727755a4/download/allocationshbcutccumsisip.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c213b768-c40c-41df-80d4-d9eec9c4c67d/resource/44be1955-f07b-4fca-af10-f16c727755a4/download/allocationshbcutccumsisip.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Allocations for Section 18004(a)(2) of CARES Act:"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Allocations for Section 18004(a)(2) of CARES Act:",
                     "description": "Allocations for Section 18004(a)(2) of CARES Act: - EXCEL",
-                    "downloadURL": "https://data.ed.gov/dataset/c213b768-c40c-41df-80d4-d9eec9c4c67d/resource/a63a2288-2165-42dd-87b4-77e269f3d2b0/download/allocationshbcutccumsisip.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c213b768-c40c-41df-80d4-d9eec9c4c67d/resource/a63a2288-2165-42dd-87b4-77e269f3d2b0/download/allocationshbcutccumsisip.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Allocations for Section 18004(a)(2) of CARES Act:"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Allocations for Section 18004(a)(2) of CARES Act:",
                     "description": "Allocations for Section 18004(a)(2) of CARES Act: - EXCEL",
-                    "downloadURL": "https://data.ed.gov/dataset/c213b768-c40c-41df-80d4-d9eec9c4c67d/resource/aca8cf4d-9f41-4948-a93b-ed83f98ebb90/download/allocationshbcutccumsisip.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c213b768-c40c-41df-80d4-d9eec9c4c67d/resource/aca8cf4d-9f41-4948-a93b-ed83f98ebb90/download/allocationshbcutccumsisip.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Allocations for Section 18004(a)(2) of CARES Act:"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "Allocations for Section 18004(a)(2) of CARES Act:",
                     "description": "Allocations for Section 18004(a)(2) of CARES Act: - EXCEL",
-                    "downloadURL": "https://data.ed.gov/dataset/c213b768-c40c-41df-80d4-d9eec9c4c67d/resource/1ab76bb9-5a09-4201-a3e4-dc4c68c68484/download/allocationshbcutccumsisip.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c213b768-c40c-41df-80d4-d9eec9c4c67d/resource/1ab76bb9-5a09-4201-a3e4-dc4c68c68484/download/allocationshbcutccumsisip.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Allocations for Section 18004(a)(2) of CARES Act:"
                 }
             ],
+            "identifier": "992b42a6-2ede-404a-8253-8dad6f701f65",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "cares-act",
@@ -57654,22 +57633,11 @@
                 "ope",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T20:44:07.898082",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Awards -- Underground Railroad Educational and Cultural Program",
-            "description": "This archived page provides information about award recipients and summaries of competitions under the Underground Railroad Educational and Cultural Program.",
-            "modified": "2023-07-06T20:43:21.688823",
-            "accessLevel": "public",
-            "identifier": "534e83ca-51ec-4c69-92c0-bdc933cb6ec4",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -57690,22 +57658,33 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "CARES Act: Higher Education Emergency Relief Fund"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "This archived page provides information about award recipients and summaries of competitions under the Underground Railroad Educational and Cultural Program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "Grant Awards:",
                     "description": "Grant Awards: -",
-                    "downloadURL": "https://www2.ed.gov/programs/ugroundrr/ugrrgrantees2008.xls"
+                    "downloadURL": "https://www2.ed.gov/programs/ugroundrr/ugrrgrantees2008.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Grant Awards:"
                 }
             ],
+            "identifier": "534e83ca-51ec-4c69-92c0-bdc933cb6ec4",
             "keyword": [
                 "african-americans",
                 "awards",
@@ -57719,22 +57698,11 @@
                 "underground-railroad",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-07-06T20:43:21.688823",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Awards -- Transition and Postsecondary Programs for Students with Intellectual Disabilities",
-            "description": "The Model Comprehensive Transition and Postsecondary Programs for Students with Intellectual Disabilities (TPSID) provides grants to institutions of higher education or consortia of institutions of higher education to enable them to create or expand high quality, inclusive model comprehensive transition and postsecondary programs for students with intellectual disabilities.",
-            "modified": "2023-07-06T20:42:41.338244",
-            "accessLevel": "public",
-            "identifier": "4544db75-b202-406a-83f9-cdc50db19efc",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -57755,38 +57723,49 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Awards -- Underground Railroad Educational and Cultural Program"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "The Model Comprehensive Transition and Postsecondary Programs for Students with Intellectual Disabilities (TPSID) provides grants to institutions of higher education or consortia of institutions of higher education to enable them to create or expand high quality, inclusive model comprehensive transition and postsecondary programs for students with intellectual disabilities.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-                    "format": "DOCX",
-                    "title": "fy2020tpsidgranteeabstracts.docx",
                     "description": "fy2020tpsidgranteeabstracts.docx",
-                    "downloadURL": "https://data.ed.gov/dataset/73e775ed-f9b1-4e8b-8583-52a6615a2f07/resource/6ae3a1f7-c97b-454d-9bf3-7f3410c8b629/download/fy2020tpsidgranteeabstracts.docx"
+                    "downloadURL": "https://data.ed.gov/dataset/73e775ed-f9b1-4e8b-8583-52a6615a2f07/resource/6ae3a1f7-c97b-454d-9bf3-7f3410c8b629/download/fy2020tpsidgranteeabstracts.docx",
+                    "format": "DOCX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "fy2020tpsidgranteeabstracts.docx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "DOC",
-                    "title": "tpsidabstracts2010.doc",
                     "description": "tpsidabstracts2010.doc",
-                    "downloadURL": "https://data.ed.gov/dataset/73e775ed-f9b1-4e8b-8583-52a6615a2f07/resource/e0a72038-f749-49a6-8c47-c2f8d7627214/download/tpsidabstracts2010.doc"
+                    "downloadURL": "https://data.ed.gov/dataset/73e775ed-f9b1-4e8b-8583-52a6615a2f07/resource/e0a72038-f749-49a6-8c47-c2f8d7627214/download/tpsidabstracts2010.doc",
+                    "format": "DOC",
+                    "mediaType": "application/msword",
+                    "title": "tpsidabstracts2010.doc"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "PDF",
-                    "title": "tpsidabtracts2015.pdf",
                     "description": "tpsidabtracts2015.pdf",
-                    "downloadURL": "https://data.ed.gov/dataset/73e775ed-f9b1-4e8b-8583-52a6615a2f07/resource/9aa68a75-45e8-418e-bd71-79a7fa64bf82/download/tpsidabtracts2015.pdf"
+                    "downloadURL": "https://data.ed.gov/dataset/73e775ed-f9b1-4e8b-8583-52a6615a2f07/resource/9aa68a75-45e8-418e-bd71-79a7fa64bf82/download/tpsidabtracts2015.pdf",
+                    "format": "PDF",
+                    "mediaType": "application/pdf",
+                    "title": "tpsidabtracts2015.pdf"
                 }
             ],
+            "identifier": "4544db75-b202-406a-83f9-cdc50db19efc",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "disabilities",
@@ -57799,22 +57778,11 @@
                 "transition",
                 "united-states"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2023-07-06T20:42:41.338244",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Awards -- Training for Realtime Writers - FIPSE",
-            "description": "This program, administered by the Fund for the Improvement of Postsecondary Education, provides grants for the recruitment, training and assistance, and job placement of individuals, including ones who have completed a court reporting training program as realtime writers.",
-            "modified": "2023-07-06T20:42:04.461775",
-            "accessLevel": "public",
-            "identifier": "c09cf110-0399-4789-be48-1af707bd1974",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Postsecondary Education (OPE)",
@@ -57835,46 +57803,57 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "title": "Awards -- Transition and Postsecondary Programs for Students with Intellectual Disabilities"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Cottrell",
                 "hasEmail": "mailto:Jason.Cottrell@ed.gov"
             },
+            "description": "This program, administered by the Fund for the Improvement of Postsecondary Education, provides grants for the recruitment, training and assistance, and job placement of individuals, including ones who have completed a court reporting training program as realtime writers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "DOC",
-                    "title": "trtw-abstracts-2010.doc",
                     "description": "trtw-abstracts-2010.doc",
-                    "downloadURL": "https://data.ed.gov/dataset/3f782d2f-9e55-4c79-a0a9-9934a978e2f7/resource/216d4b01-f7e5-4a92-aa55-72647ffda50b/download/trtw-abstracts-2010.doc"
+                    "downloadURL": "https://data.ed.gov/dataset/3f782d2f-9e55-4c79-a0a9-9934a978e2f7/resource/216d4b01-f7e5-4a92-aa55-72647ffda50b/download/trtw-abstracts-2010.doc",
+                    "format": "DOC",
+                    "mediaType": "application/msword",
+                    "title": "trtw-abstracts-2010.doc"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "DOC",
-                    "title": "trtw-abstracts-2011.doc",
                     "description": "trtw-abstracts-2011.doc",
-                    "downloadURL": "https://data.ed.gov/dataset/3f782d2f-9e55-4c79-a0a9-9934a978e2f7/resource/2ced674e-35d5-4466-9e49-b644c83f1487/download/trtw-abstracts-2011.doc"
+                    "downloadURL": "https://data.ed.gov/dataset/3f782d2f-9e55-4c79-a0a9-9934a978e2f7/resource/2ced674e-35d5-4466-9e49-b644c83f1487/download/trtw-abstracts-2011.doc",
+                    "format": "DOC",
+                    "mediaType": "application/msword",
+                    "title": "trtw-abstracts-2011.doc"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "DOC",
-                    "title": "trtw-abstracts2012.doc",
                     "description": "trtw-abstracts2012.doc",
-                    "downloadURL": "https://data.ed.gov/dataset/3f782d2f-9e55-4c79-a0a9-9934a978e2f7/resource/d296ecd9-a523-4994-813f-0320f88ffe4a/download/trtw-abstracts2012.doc"
+                    "downloadURL": "https://data.ed.gov/dataset/3f782d2f-9e55-4c79-a0a9-9934a978e2f7/resource/d296ecd9-a523-4994-813f-0320f88ffe4a/download/trtw-abstracts2012.doc",
+                    "format": "DOC",
+                    "mediaType": "application/msword",
+                    "title": "trtw-abstracts2012.doc"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/msword",
-                    "format": "DOC",
-                    "title": "trtw-abstracts2013.doc",
                     "description": "trtw-abstracts2013.doc",
-                    "downloadURL": "https://data.ed.gov/dataset/3f782d2f-9e55-4c79-a0a9-9934a978e2f7/resource/ed2db1c5-f11f-4fdf-ba99-bc58fbe2b7ca/download/trtw-abstracts2013.doc"
+                    "downloadURL": "https://data.ed.gov/dataset/3f782d2f-9e55-4c79-a0a9-9934a978e2f7/resource/ed2db1c5-f11f-4fdf-ba99-bc58fbe2b7ca/download/trtw-abstracts2013.doc",
+                    "format": "DOC",
+                    "mediaType": "application/msword",
+                    "title": "trtw-abstracts2013.doc"
                 }
             ],
+            "identifier": "c09cf110-0399-4789-be48-1af707bd1974",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "court-reporting",
@@ -57888,22 +57867,11 @@
                 "united-states",
                 "writers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
```

