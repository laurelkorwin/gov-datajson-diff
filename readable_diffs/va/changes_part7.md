# Change History for va.json (Part 7)

### Changes from 31606f9 to dd2190f (Part 7/7)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-OIT-987",
             "description": "<p>VIP is the follow-on framework from PMAS for the development and management of IT projects which will propel the Department with even more rigor toward Veteran-focused delivery of IT capabilities. The VIP framework unifies and streamlines IT delivery oversight and will deliver IT products more efficiently, securely and predictably. The VIP framework creates an environment delivering more frequent releases through a deeper application of Agile practices. In parallel with a single integrated release process, VIP will increase cross-organizational and business stakeholder engagement, provide greater visibility into projects, increase Agile adoption and institute a predictive delivery cadence.</p>",
-            "title": "VIP Guide",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83618,83 +83599,85 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "VA-OIT-OIT-987",
+            "issued": "2017-07-26",
+            "keyword": [
+                "agile",
+                "project management",
+                "veteran-focused integration process",
+                "vip"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vsay-ffng",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-21",
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
+            "title": "VIP Guide"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/vocrehab/subsistence_allowance_rates.asp",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "post 9 11 chapter 31 subsistence",
-                "vba benefits",
-                "vre"
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
-            "identifier": "VA-VBA-INFO-018",
+            "dataQuality": true,
             "description": "<p>Post-9/11 Ch31 Subsistence Rates- VRE</p>",
-            "title": "Post-9/11 Ch31 Subsistence Rates- VRE",
+            "identifier": "VA-VBA-INFO-018",
             "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "post 9 11 chapter 31 subsistence",
+                "vba benefits",
+                "vre"
+            ],
+            "landingPage": "https://www.benefits.va.gov/vocrehab/subsistence_allowance_rates.asp",
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
+            "title": "Post-9/11 Ch31 Subsistence Rates- VRE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vsmc-f78i",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-08-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-10",
-            "keyword": [
-                "age groups",
-                "vetpop"
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
-            "identifier": "https://www.data.va.gov/api/views/vsmc-f78i",
             "description": "",
-            "title": "VetPop Age Projection",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83702,62 +83685,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vsmc-f78i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vsmc-f78i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vsmc-f78i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vsmc-f78i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vsmc-f78i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vsmc-f78i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vsmc-f78i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vsmc-f78i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vsmc-f78i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/vsmc-f78i",
+            "issued": "2024-08-14",
+            "keyword": [
+                "age groups",
+                "vetpop"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vsmc-f78i",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-10",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop Age Projection"
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
-            "identifier": "VA-VBA-ABR2012-035",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Veterans Who Began Receiving Disability Compensation by Combined Degree During FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83765,44 +83745,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-035",
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
+            "title": "Veterans Who Began Receiving Disability Compensation by Combined Degree During FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vtgf-izk6",
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
-            "identifier": "d249650a-b840-42de-83fa-9cf3756759b6",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Connecticut FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83810,25 +83794,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "d249650a-b840-42de-83fa-9cf3756759b6",
+            "issued": "2018-10-29",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vtgf-izk6",
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
+            "title": "State Summary Connecticut FY2017"
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
+            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- February 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING022014-039",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-02-01T05:00:00Z/2013-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 030",
                 "face amount",
@@ -83837,59 +83843,37 @@
                 "new life insurance policies",
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
-            "identifier": "VA-VBA-USASPENDING022014-039",
-            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- February 2013.</p>",
-            "title": "USA Spending file- 02/2014-New Life Insurance Policies-Insurance -  CFDA 64.030",
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
+            "title": "USA Spending file- 02/2014-New Life Insurance Policies-Insurance -  CFDA 64.030"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vu9n-nxat",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "oklahoma"
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
-            "identifier": "VA-OEI-OEI-207",
             "description": "<p>This summary describes the programs and services VA provided in Oklahoma in fiscal year 2015.</p>",
-            "title": "State Summary: Oklahoma FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83898,41 +83882,40 @@
                     "title": "Oklahoma"
                 }
             ],
+            "identifier": "VA-OEI-OEI-207",
+            "issued": "2017-07-26",
+            "keyword": [
+                "oklahoma"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vu9n-nxat",
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
+            "title": "State Summary: Oklahoma FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vvu3-duxs",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "cars",
-                "establishments"
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
-            "identifier": "VA-OM-OM-157",
             "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "COIN 0022 September 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83940,39 +83923,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-157",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cars",
+                "establishments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vvu3-duxs",
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
+            "title": "COIN 0022 September 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vw34-7ctp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-07",
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
-            "identifier": "https://www.data.va.gov/api/views/vw34-7ctp",
+            "dataQuality": true,
             "description": "This data is based on population projections  (6L) provided by the National Center for Veterans Statistics and Analysis, published in 2018.",
-            "title": "2018 - Age Distribution over Time - Chart",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83980,41 +83965,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vw34-7ctp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vw34-7ctp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vw34-7ctp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vw34-7ctp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vw34-7ctp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vw34-7ctp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vw34-7ctp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vw34-7ctp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vw34-7ctp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/vw34-7ctp",
+            "issued": "2021-08-26",
+            "keyword": [
+                "ncvas",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vw34-7ctp",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2021-09-07",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "2018 - Age Distribution over Time - Chart"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR40_022016_Retrospective_Wait_Times_Desired_Date_by_Division_CDW_PDFReady.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 31 Jan 2016"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-738",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2016-01-31T05:00:00Z/2016-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -84028,70 +84043,38 @@
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
-            "identifier": "VA-VHA-OIA-738",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2016 Jan 31",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR40_022016_Retrospective_Wait_Times_Desired_Date_by_Division_CDW_PDFReady.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 31 Jan 2016"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2016-01-31T05:00:00Z/2016-01-31T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2016 Jan 31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vwib-pw92",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "veterans",
-                "washington"
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
-            "identifier": "VA-OEI-OEI-134",
             "description": "<p>This is a summary of the programs and services provided by VA in Washington in fiscal year 2014.</p>",
-            "title": "State Summary:  Washington",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84100,44 +84083,45 @@
                     "title": "State Summary:  Washington"
                 }
             ],
+            "identifier": "VA-OEI-OEI-134",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans",
+                "washington"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vwib-pw92",
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
+            "title": "State Summary:  Washington"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vwx3-bnh6",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-02-01T05:00:00Z/2015-07-28T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "filming"
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
-            "identifier": "VA-NCA-MP-011",
+            "dataQuality": true,
             "description": "<p>This factsheet provides guidelines for filming in a VA National Cemetery.</p>",
-            "title": "Filming in a National Cemetery",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84146,41 +84130,40 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-MP-011",
+            "issued": "2017-07-26",
+            "keyword": [
+                "filming"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vwx3-bnh6",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-02-01T05:00:00Z/2015-07-28T04:00:00Z",
             "theme": [
                 "Filming"
-            ]
+            ],
+            "title": "Filming in a National Cemetery"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vxen-hwsd",
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
-            "identifier": "https://www.data.va.gov/api/views/vxen-hwsd",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE DEC2018",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84188,67 +84171,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vxen-hwsd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vxen-hwsd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vxen-hwsd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vxen-hwsd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vxen-hwsd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vxen-hwsd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vxen-hwsd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vxen-hwsd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vxen-hwsd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/vxen-hwsd",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vxen-hwsd",
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
+            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vxex-2fsu",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Public",
-            "issued": "2024-12-05",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-10-01/2023-09-30",
-            "modified": "2024-12-05",
-            "keyword": [
-                "community care",
-                "diagnosis",
-                "fy23",
-                "icd10",
-                "inpatient",
-                "outpatient"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VSSC Data Analysis and Reporting",
                 "hasEmail": "mailto:VSSCDataAnalysisandReporting@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/vxex-2fsu",
+            "dataQuality": true,
             "description": "Diagnosis entered during outpatient, inpatient, or Community Care that was paid for by VHA. This excludes Non-VA Care and Unknown.",
-            "title": "Diagnosis_FY23",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84256,63 +84235,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vxex-2fsu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vxex-2fsu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vxex-2fsu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vxex-2fsu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vxex-2fsu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vxex-2fsu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vxex-2fsu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vxex-2fsu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vxex-2fsu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/vxex-2fsu",
+            "issued": "2024-12-05",
+            "keyword": [
+                "community care",
+                "diagnosis",
+                "fy23",
+                "icd10",
+                "inpatient",
+                "outpatient"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vxex-2fsu",
             "language": [
                 "N/A"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-05",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Public",
+            "spatial": "U.S.",
+            "temporal": "2022-10-01/2023-09-30",
+            "title": "Diagnosis_FY23"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vxu5-rkfc",
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
-            "identifier": "https://www.data.va.gov/api/views/vxu5-rkfc",
+            "dataQuality": true,
             "description": "<p>VBA COMPENSTATION BENEFITS PRGOGRAM to provide vocational training and rehabilitation to certain children born with spina bifida or other covered birth defects who are children of Vietnam veterans and some Korean veterans. \u201cA child born with spina bifida or other covered birth defects, except spina bifida occulta, who is the natural child of a Vietnam veteran and some Korean veterans, regardless of the age or marital status of the child, conceived after the date on which the veteran first served in the Republic of Vietnam during the Vietnam era and in particular areas near the DMZ in the Korean conflict. VA must also determine that it is feasible for the child to achieve a vocational goal.\u201d</p>",
-            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA JAN2019",
-            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84320,61 +84304,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vxu5-rkfc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vxu5-rkfc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vxu5-rkfc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vxu5-rkfc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vxu5-rkfc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vxu5-rkfc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vxu5-rkfc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vxu5-rkfc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vxu5-rkfc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/vxu5-rkfc",
+            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 127"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vxu5-rkfc",
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
+            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA JAN2019"
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
-            "identifier": "VA-OGC-005",
             "description": "<p>Provision of Primary Care for Residents in State Home Domiciliaries</p>",
-            "title": "OGC Precedent Opinion 1-2014",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84383,44 +84366,44 @@
                     "title": "VAOGCPREC 1-2014"
                 }
             ],
+            "identifier": "VA-OGC-005",
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
+            "title": "OGC Precedent Opinion 1-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vya2-ishn",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "delaware",
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
-            "identifier": "VA-OEI-OEI-093",
             "description": "<p>This is a summary of the programs and services provided in Delaware in fiscal year 2014.</p>",
-            "title": "State Summary:  Delaware",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84429,43 +84412,45 @@
                     "title": "State Summary:  Delaware"
                 }
             ],
+            "identifier": "VA-OEI-OEI-093",
+            "issued": "2017-07-26",
+            "keyword": [
+                "delaware",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vya2-ishn",
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
+            "title": "State Summary:  Delaware"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vyzc-q7jz",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "alabama"
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
-            "identifier": "VA-OEI-OEI-170",
+            "dataQuality": true,
             "description": "<p>This summary describes the programs and services VA provided in Alabama in FY2015.</p>",
-            "title": "State Summary: Alabama",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84474,46 +84459,40 @@
                     "title": "state summaries alabama"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-170",
+            "issued": "2017-07-26",
+            "keyword": [
+                "alabama"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vyzc-q7jz",
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
+            "title": "State Summary: Alabama"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/vyzz-9v4a",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-11-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-11-10",
-            "keyword": [
-                "gulf war",
-                "korean war",
-                "veterans",
-                "vietnam war",
-                "world war i",
-                "world war ii"
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
-            "identifier": "https://www.data.va.gov/api/views/vyzz-9v4a",
             "description": "Data from America's War factsheet with only those who served and living",
-            "title": "Veterans of America's Wars (1917-present)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84521,53 +84500,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vyzz-9v4a/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vyzz-9v4a/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vyzz-9v4a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vyzz-9v4a/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vyzz-9v4a/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vyzz-9v4a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vyzz-9v4a/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vyzz-9v4a/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vyzz-9v4a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/vyzz-9v4a",
+            "issued": "2021-11-10",
+            "keyword": [
+                "gulf war",
+                "korean war",
+                "veterans",
+                "vietnam war",
+                "world war i",
+                "world war ii"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vyzz-9v4a",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-11-10",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans of America's Wars (1917-present)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/vzfm-pdpa",
-            "issued": "2023-06-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/vzfm-pdpa",
             "description": "These data are based on the latest Veteran Population Projection Model, VetPop2020, provided by the National Center for Veterans Statistics and Analysis, published in 2023.",
-            "title": "FY 2021_NCVAS Period of Service Over Time For State Summaries",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84575,56 +84562,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vzfm-pdpa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vzfm-pdpa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vzfm-pdpa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vzfm-pdpa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vzfm-pdpa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vzfm-pdpa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vzfm-pdpa/rows.xml?accessType=DOWNLOAD",
+                {
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vzfm-pdpa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vzfm-pdpa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/vzfm-pdpa",
+            "issued": "2023-06-14",
+            "landingPage": "https://www.data.va.gov/d/vzfm-pdpa",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Period of Service Over Time For State Summaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/w2gm-r57n",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
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
-            "identifier": "VA-OEI-OEI-088",
             "description": "<p>This summary describes the programs and services VA provided in Arizona in fiscal year 2014.</p>",
-            "title": "State Summary:  Arizona",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84633,26 +84617,55 @@
                     "title": "State Summary:  Arizona"
                 }
             ],
+            "identifier": "VA-OEI-OEI-088",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/w2gm-r57n",
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
+            "title": "State Summary:  Arizona"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oprm.va.gov/foia/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VA OM Open Data",
+                "hasEmail": "mailto:VAOMOpenData@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2006.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2006.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-08",
             "issued": "2017-07-26",
-            "temporal": "2005-10-01T04:00:00Z/2006-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2006",
                 "appeals",
@@ -84669,69 +84682,40 @@
                 "response time",
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
-            "identifier": "VA-OIT-ITIS-08",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2006.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2006",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2006.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2005-10-01T04:00:00Z/2006-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/w3e3-3sbk",
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
-            "identifier": "https://www.data.va.gov/api/views/w3e3-3sbk",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist States and federally recognized tribal governments in the establishment, expansion, and improvement of veterans' cemeteries. Monetary assistance is provided under this program to establish, expand, and improve State or Tribal government veterans\u2019 cemeteries. Cemeteries must be State or Tribal Government owned and operated solely for the interment of eligible veterans and their dependents and/or spouses. Construction cost means the amount found necessary to convert a tract of land to an operational cemetery. The cemetery must be used solely for the interment of veterans, their wives, husbands, surviving spouses, minor children, and unmarried adult children who were physically or mentally disabled and incapable of self-support: section 38 CFR Part 38.620.</p>",
-            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM JAN2019",
-            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84739,61 +84723,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/w3e3-3sbk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/w3e3-3sbk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/w3e3-3sbk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/w3e3-3sbk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/w3e3-3sbk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/w3e3-3sbk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/w3e3-3sbk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/w3e3-3sbk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/w3e3-3sbk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/w3e3-3sbk",
+            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
+            "issued": "2019-03-29",
+            "keyword": [
+                "cfda 64 101"
+            ],
+            "landingPage": "https://www.data.va.gov/d/w3e3-3sbk",
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
+            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/w46w-2ri6",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "iowa",
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
-            "identifier": "VA-OEI-OEI-100",
             "description": "<p>This is a summary of the programs and services provided by VA in Iowa in fiscal year 2014.</p>",
-            "title": "State Summary: Iowa",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84802,44 +84785,45 @@
                     "title": "State Summary: Iowa"
                 }
             ],
+            "identifier": "VA-OEI-OEI-100",
+            "issued": "2017-07-26",
+            "keyword": [
+                "iowa",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/w46w-2ri6",
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
+            "title": "State Summary: Iowa"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/w4eg-w5pf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "43b37efb-4733-4d79-b8a6-7cd7fa1178d4",
+            "dataQuality": true,
             "description": "<p>The spreadsheet counts Veteran, Non-Veteran, and Dependent internents at National and State Cemeteries for FY2000 to FY2017</p>",
-            "title": "NCA Summary of Veteran, Non-Veteran, and Dependent Interments by Cemetery Type: FY2000 to FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84847,44 +84831,38 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "43b37efb-4733-4d79-b8a6-7cd7fa1178d4",
+            "issued": "2018-09-11",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/w4eg-w5pf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "NCA Summary of Veteran, Non-Veteran, and Dependent Interments by Cemetery Type: FY2000 to FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/w54d-782x",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-02-15",
-            "temporal": "2019-01-01T12:00:00Z/2019-03-31T11:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "505",
-                "accessions",
-                "mission act",
-                "new hires (time-to-hire-measure)",
-                "public law 115-182",
-                "separations",
-                "vacancy data",
-                "va mission act"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA Workforce Planning and Analysis",
                 "hasEmail": "mailto:vacoWPA@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "59d76722-fc57-479f-9023-0c2b08c6bf5e",
+            "dataQuality": true,
             "description": "<p>VA-wide workforce data, In accordance with Public Law 115-182, the VA Mission Act of 2018, Section 505.</p>",
-            "title": "VA Mission Act Section 505 Data",
-            "programCode": [
-                "029:085"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84893,47 +84871,52 @@
                     "title": "VA Mission Act - Section 505 Data"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "59d76722-fc57-479f-9023-0c2b08c6bf5e",
+            "issued": "2019-02-15",
+            "keyword": [
+                "505",
+                "accessions",
+                "mission act",
+                "new hires (time-to-hire-measure)",
+                "public law 115-182",
+                "separations",
+                "vacancy data",
+                "va mission act"
+            ],
+            "landingPage": "https://www.data.va.gov/d/w54d-782x",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:085"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2019-01-01T12:00:00Z/2019-03-31T11:59:59Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Mission Act Section 505 Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/w55y-pgkb",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "adr",
-                "health"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tony Bennett",
                 "hasEmail": "mailto:Tony.Bennett@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "7ce5a4d6-8f92-4dd0-b3cc-235022fafb0f",
+            "dataQuality": true,
             "description": "<p>ADR provides an authoritative data store for shared administrative, demographic, enrollment, and eligibility information which is managed as a corporate asset. This administrative database system offers mission-critical database support for all VA Medical 21st Century Core applications such as Enrollment Systems, Identity Management System, Community Care Program, Veterans's Choice program, President's Affordable Care Act project, Patient Advocacy Tracking System, Veterans 360, and others.</p>",
-            "title": "Administrative Data Repository (ADR)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84942,72 +84925,69 @@
                     "title": "Administrative Data Repository (ADR)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "7ce5a4d6-8f92-4dd0-b3cc-235022fafb0f",
+            "issued": "2018-02-23",
+            "keyword": [
+                "adr",
+                "health"
+            ],
+            "landingPage": "https://www.data.va.gov/d/w55y-pgkb",
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
+            "title": "Administrative Data Repository (ADR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/w5xx-66mz",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "veterans",
-                "virginia"
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
-            "identifier": "https://www.data.va.gov/api/views/w5xx-66mz",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Virginia",
+            "identifier": "https://www.data.va.gov/api/views/w5xx-66mz",
+            "issued": "2021-08-26",
+            "keyword": [
+                "veterans",
+                "virginia"
+            ],
+            "landingPage": "https://www.data.va.gov/d/w5xx-66mz",
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
+            "title": "State Summaries_Virginia"
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
-            "identifier": "VA-VBA-ABR2012-105",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Nebraska-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85015,52 +84995,51 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-105",
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
+            "title": "Nebraska-FY12 Benefits Summary"
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
-            "temporal": "2009-10-01T04:00:00Z/2014-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cboc",
-                "clinic",
-                "health",
-                "healthcare",
-                "outpatient",
-                "va",
-                "veteran",
-                "visit"
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
-            "identifier": "VA-VHA-OIA-112",
-            "description": "<p>Outpatient visits by Administrative Parent. A visit is counted as a visit to one or more clinics or units within 1 calendar day at the site of care level. A patient can have  multiple appointments, but is counted as only one visit if the collective appointments were within 24 hours.</p>",
-            "title": "VA Outpatient Visits by Administrative Parent, FY2010-2014",
+            "dataQuality": true,
+            "describedBy": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/raw/master/VA_DataDefinitions_VisitsBedsCBOC_2015.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:042"
-            ],
+            "description": "<p>Outpatient visits by Administrative Parent. A visit is counted as a visit to one or more clinics or units within 1 calendar day at the site of care level. A patient can have  multiple appointments, but is counted as only one visit if the collective appointments were within 24 hours.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85068,49 +85047,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/w676-2bvk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/w676-2bvk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/w676-2bvk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/w676-2bvk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/w676-2bvk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/w676-2bvk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/w676-2bvk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/w676-2bvk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/w676-2bvk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/raw/master/VA_DataDefinitions_VisitsBedsCBOC_2015.pdf",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-112",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cboc",
+                "clinic",
+                "health",
+                "healthcare",
+                "outpatient",
+                "va",
+                "veteran",
+                "visit"
+            ],
+            "landingPage": "https://www.va.gov/health/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
+            "temporal": "2009-10-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "VA Healthcare Utilization"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Outpatient Visits by Administrative Parent, FY2010-2014"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/February_2015_Completed_04022015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 28 Feb 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-101",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-02-28T05:00:00Z/2015-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -85124,75 +85139,40 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-101",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Feb 28",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/February_2015_Completed_04022015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 28 Feb 2015"
-                }
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-02-28T05:00:00Z/2015-02-28T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Feb 28"
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
-            "modified": "2022-03-08",
-            "keyword": [
-                "abr",
-                "abr2012",
-                "insurance",
-                "insurance benefits fy12",
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
-            "identifier": "VA-VBA-ABR2012-059",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Life Insurance Policies in Force by Fiscal Year (Number of Policies)",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85201,44 +85181,48 @@
                     "title": "Life Insurance Policies in Force by Fiscal Year (Number of Policies)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-059",
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
+            "modified": "2022-03-08",
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
+            "title": "Life Insurance Policies in Force by Fiscal Year (Number of Policies)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/w76x-wsns",
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
-            "identifier": "c7bba19c-7cf8-44e9-a439-712710b3586e",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Nevada FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85246,75 +85230,75 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "c7bba19c-7cf8-44e9-a439-712710b3586e",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/w76x-wsns",
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
+            "title": "State Summary Nevada FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/w8ba-xp7i",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist States and federally recognized tribal governments in the establishment, expansion, and improvement of veterans' cemeteries. Monetary assistance is provided under this program to establish, expand, and improve State or Tribal government veterans\u2019 cemeteries. Cemeteries must be State or Tribal Government owned and operated solely for the interment of eligible veterans and their dependents and/or spouses. Construction cost means the amount found necessary to convert a tract of land to an operational cemetery. The cemetery must be used solely for the interment of veterans, their wives, husbands, surviving spouses, minor children, and unmarried adult children who were physically or mentally disabled and incapable of self-support: section 38 CFR Part 38.620.</p>",
-            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM FY2019",
+            "identifier": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
+            "issued": "2019-03-29",
+            "keyword": [
+                "cfda 64 101"
+            ],
+            "landingPage": "https://www.data.va.gov/d/w8ba-xp7i",
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
+            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/w8xj-5pss",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "tennessee"
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
-            "identifier": "VA-OEI-OEI-214",
             "description": "<p>This summary describes the programs and services VA provided in  Tennessee in fiscal year 2015.</p>",
-            "title": "State Summary:  Tennessee FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85323,42 +85307,42 @@
                     "title": "Tennessee"
                 }
             ],
+            "identifier": "VA-OEI-OEI-214",
+            "issued": "2017-07-26",
+            "keyword": [
+                "tennessee"
+            ],
+            "landingPage": "https://www.data.va.gov/d/w8xj-5pss",
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
+            "title": "State Summary:  Tennessee FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wa9p-rfey",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2023-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
-            "keyword": [
-                "other outcomes",
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
-            "identifier": "https://www.data.va.gov/api/views/wa9p-rfey",
+            "dataQuality": true,
             "description": "The Other Outcomes dataset includes information on whether the trial includes measures of depression, anxiety, substance use, sleep, anger, quality of life and functioning. Results in this dataset are provided for each treatment arm. The name of the measure is included as well as the between-group effect sizes. Use this dataset to learn how about the effects of PTSD treatments on other outcomes.\nValues abstracted as not applicable (\"NA\") or not reported (\"NR\") from the study are null values (empty cells).\nStudy level variables, like military status and percent female, are included for ease of filtering. These columns are not individual arm or arm comparison level data.",
-            "title": "Other Outcomes",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85366,85 +85350,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wa9p-rfey/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wa9p-rfey/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wa9p-rfey/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wa9p-rfey/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wa9p-rfey/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wa9p-rfey/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wa9p-rfey/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wa9p-rfey/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wa9p-rfey/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/wa9p-rfey",
+            "issued": "2023-10-31",
+            "keyword": [
+                "other outcomes",
+                "ptsd-repository"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wa9p-rfey",
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
+            "title": "Other Outcomes"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wci3-yrsv",
-            "issued": "2024-08-05",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-27",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "This data story explores the demographic and socioeconomic characteristics, along with the utilization of VA benefits and services, of women Veterans in 2023.",
             "identifier": "https://www.data.va.gov/api/views/wci3-yrsv",
+            "issued": "2024-08-05",
+            "landingPage": "https://www.data.va.gov/d/wci3-yrsv",
+            "modified": "2024-08-27",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "This data story explores the demographic and socioeconomic characteristics, along with the utilization of VA benefits and services, of women Veterans in 2023.",
             "title": "Women Veterans in 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wci5-y2m7",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2005-10-01T04:00:00Z/2006-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/vetdata/docs/DataGov_GDX_FY06_Technical_Notes.doc"
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
-            "identifier": "VA-OEI-OEI-002",
-            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
-            "title": "Veterans Affairs Geographic Distribution of Expenditures FY06 by State and County",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/DataGov_GDX_FY06_Technical_Notes.doc",
             "describedByType": "application/msword",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85452,66 +85434,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wci5-y2m7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wci5-y2m7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wci5-y2m7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wci5-y2m7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wci5-y2m7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wci5-y2m7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wci5-y2m7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wci5-y2m7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wci5-y2m7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/DataGov_GDX_FY06_Technical_Notes.doc",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wci5-y2m7",
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
+                "https://www.va.gov/vetdata/docs/DataGov_GDX_FY06_Technical_Notes.doc"
+            ],
+            "temporal": "2005-10-01T04:00:00Z/2006-09-30T04:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Affairs Geographic Distribution of Expenditures FY06 by State and County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wcj8-dfbt",
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
-            "identifier": "936f3160-877c-4ab2-adce-a475753a0343",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary New Jersey FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85519,42 +85503,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "936f3160-877c-4ab2-adce-a475753a0343",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wcj8-dfbt",
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
+            "title": "State Summary New Jersey FY2016"
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
-            "identifier": "VA-VBA-ABR2012-085",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Delaware-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85562,44 +85542,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-085",
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
+            "title": "Delaware-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wcvr-awfe",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 114"
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
-            "identifier": "https://www.data.va.gov/api/views/wcvr-awfe",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located.</p>",
-            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS JAN2019",
-            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85607,105 +85591,102 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wcvr-awfe/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wcvr-awfe/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wcvr-awfe/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wcvr-awfe/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wcvr-awfe/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wcvr-awfe/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wcvr-awfe/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wcvr-awfe/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wcvr-awfe/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/wcvr-awfe",
+            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 114"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wcvr-awfe",
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
+            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS JAN2019"
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
+            "description": "<p>USA Spending- Non Service Connected Disability- March 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING032014-046",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING032014-046",
-            "description": "<p>USA Spending- Non Service Connected Disability- March 2014.</p>",
-            "title": "USA Spending file- 03/2014 Compensation and Pension-  CFDA 64.104",
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
+            "title": "USA Spending file- 03/2014 Compensation and Pension-  CFDA 64.104"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wdtt-7pm9",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-11-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-22",
-            "keyword": [
-                "utilization",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
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
-            "identifier": "https://www.data.va.gov/api/views/wdtt-7pm9",
             "description": "Trend in Percent of Health Care & Compensation Users vs Other Users. Data underlying the first figure of Part 3 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 14, Trend in Percent of Health Care & Compensation Users vs Other Users",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85713,58 +85694,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wdtt-7pm9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wdtt-7pm9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wdtt-7pm9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wdtt-7pm9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wdtt-7pm9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wdtt-7pm9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wdtt-7pm9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wdtt-7pm9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wdtt-7pm9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/wdtt-7pm9",
+            "issued": "2020-11-19",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wdtt-7pm9",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-12-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 14, Trend in Percent of Health Care & Compensation Users vs Other Users"
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
-            "identifier": "VA-OEI-OEI-301",
+            "dataQuality": true,
             "description": "<p>NCVAS Pocket Cards are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization FY16 (Q4)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85773,46 +85757,45 @@
                     "title": "Pocket Card \u2013 FY16 (Q4)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-301",
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
+            "title": "VA Benefits & Health Care Utilization FY16 (Q4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wedg-667g",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-04-01T04:00:00Z/2015-04-30T04:00:00Z",
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
-            "identifier": "VA-OM-OM-126",
             "description": "<p>aged accounts receivable</p>",
-            "title": "COIN 0017 CARS AGE PROFILE REPORT APR 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85820,41 +85803,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-126",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wedg-667g",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-04-01T04:00:00Z/2015-04-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0017 CARS AGE PROFILE REPORT APR 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/weq8-ir6t",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-01-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "female veterans",
-                "statistics"
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
-            "identifier": "c4ba9ca0-1b96-4f05-a74a-07df07804857",
+            "dataQuality": true,
             "description": "<p>Statistics about America's female vets. <a href=\"https://www.data.va.gov/story/women-veterans-forum\">https://www.data.va.gov/story/women-veterans-forum</a></p>",
-            "title": "America's Women Veterans",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85862,65 +85846,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/weq8-ir6t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/weq8-ir6t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/weq8-ir6t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/weq8-ir6t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/weq8-ir6t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/weq8-ir6t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/weq8-ir6t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/weq8-ir6t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/weq8-ir6t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "c4ba9ca0-1b96-4f05-a74a-07df07804857",
+            "issued": "2017-01-27",
+            "keyword": [
+                "female veterans",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/weq8-ir6t",
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
+            "title": "America's Women Veterans"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/weu6-zpb9",
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
-            "identifier": "https://www.data.va.gov/api/views/weu6-zpb9",
             "description": "VetPop2023 projection of living Veterans by gender and period of service at the national level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 National Period of Service Data, 2L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85928,59 +85909,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/weu6-zpb9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/weu6-zpb9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/weu6-zpb9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/weu6-zpb9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/weu6-zpb9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/weu6-zpb9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/weu6-zpb9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/weu6-zpb9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/weu6-zpb9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/weu6-zpb9",
+            "issued": "2024-09-05",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/weu6-zpb9",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 National Period of Service Data, 2L"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wevm-uhuk",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-03-15",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "health care",
-                "income",
-                "statistics"
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
-            "identifier": "https://www.data.va.gov/api/views/wevm-uhuk",
+            "dataQuality": true,
             "description": "<p>This dataset contains information on minority veteran healthcare usage, educational attainment, unemployment rates, median income, and projected population figures.</p>",
-            "title": "Median Household Income of Minorities, by Age and Veteran Status: 2014",
-            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85988,48 +85970,97 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wevm-uhuk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wevm-uhuk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wevm-uhuk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wevm-uhuk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wevm-uhuk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wevm-uhuk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wevm-uhuk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wevm-uhuk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wevm-uhuk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/wevm-uhuk",
+            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
+            "issued": "2017-03-15",
+            "keyword": [
+                "health care",
+                "income",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wevm-uhuk",
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
+            "title": "Median Household Income of Minorities, by Age and Veteran Status: 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/healthequity/data.asp",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://github.com/department-of-veterans-affairs/VHA-Asset/raw/master/Hep%20C%20FACT%20SHEET%20FINAL%2010162015.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://github.com/department-of-veterans-affairs/VHA-Asset/raw/master/Hep%20C%20FACT%20SHEET%20FINAL%2010162015.pdf",
+            "describedByType": "application/pdf",
+            "description": "<p>The Office of Health Equity (OHE) created the Hepatitis C-Advanced Liver Disease (HCV-ALD) dashboard to raise awareness of potential disparities among vulnerable Veterans for this life-threatening condition.  The purpose of the HCV-ALD Dashboard is promote equitable diagnosis and treatment of underserved Veterans with hepatitis C and advanced liver disease.  The Hepatitis C-ALD Dashboard utilizes a set of criteria - age, gender, geography, service era, race/ethnicity - to characterize Veteran groups with ALD due to hepatitis C who may require targeted intervention to improve their health.  The dashboard advances the vision for quality care and improved access to care as identified in the VHA Blueprint for Excellence.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/api/views/wf6y-xpwt/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://www.data.va.gov/api/views/wf6y-xpwt/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://www.data.va.gov/api/views/wf6y-xpwt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://www.data.va.gov/api/views/wf6y-xpwt/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://www.data.va.gov/api/views/wf6y-xpwt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://www.data.va.gov/api/views/wf6y-xpwt/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://www.data.va.gov/api/views/wf6y-xpwt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "VA-VHA-OHE-001",
+            "issued": "2017-07-26",
             "keyword": [
                 "advanced liver disease",
                 "age",
@@ -86060,93 +86091,42 @@
                 "vulnerable",
                 "vulnerable population"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OHE-001",
-            "description": "<p>The Office of Health Equity (OHE) created the Hepatitis C-Advanced Liver Disease (HCV-ALD) dashboard to raise awareness of potential disparities among vulnerable Veterans for this life-threatening condition.  The purpose of the HCV-ALD Dashboard is promote equitable diagnosis and treatment of underserved Veterans with hepatitis C and advanced liver disease.  The Hepatitis C-ALD Dashboard utilizes a set of criteria - age, gender, geography, service era, race/ethnicity - to characterize Veteran groups with ALD due to hepatitis C who may require targeted intervention to improve their health.  The dashboard advances the vision for quality care and improved access to care as identified in the VHA Blueprint for Excellence.</p>",
-            "title": "Hepatitis C \u2013 Advanced Liver Disease Disparities Dashboard",
-            "describedByType": "application/pdf",
+            "landingPage": "https://www.va.gov/healthequity/data.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
             "programCode": [
                 "029:048"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/api/views/wf6y-xpwt/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wf6y-xpwt/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://www.data.va.gov/api/views/wf6y-xpwt/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wf6y-xpwt/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://www.data.va.gov/api/views/wf6y-xpwt/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wf6y-xpwt/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://www.data.va.gov/api/views/wf6y-xpwt/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "https://github.com/department-of-veterans-affairs/VHA-Asset/raw/master/Hep%20C%20FACT%20SHEET%20FINAL%2010162015.pdf"
             ],
-            "describedBy": "https://github.com/department-of-veterans-affairs/VHA-Asset/raw/master/Hep%20C%20FACT%20SHEET%20FINAL%2010162015.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2014-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Awareness and Research"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hepatitis C \u2013 Advanced Liver Disease Disparities Dashboard"
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
-            "identifier": "VA-VBA-ABR2012-099",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Massachusetts-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86154,49 +86134,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-099",
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
+                "029:005"
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
+            "title": "Massachusetts-FY12 Benefits Summary"
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
-            "identifier": "VA-VBA-ABR2012-095",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Kentucky-FY Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86204,48 +86184,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-095",
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
+            "title": "Kentucky-FY Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-04-01T04:00:00Z/2014-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 109",
-                "compensation for service-connected disability",
-                "compensation service",
-                "usa spending"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "monica reyes",
                 "hasEmail": "mailto:monica.reyes@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-USASPENDING042014-060",
+            "dataQuality": true,
             "description": "<p>USA Spending file- 04/2014-Veterans Compensation for Service-Connected Disability-  CFDA 64.109</p>",
-            "title": "USA Spending file- 04/2014-Veterans Compensation for Service-Connected Disability",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86254,60 +86235,48 @@
                     "title": "USA Spending file- 04/2014-Veterans Compensation for Service-Connected Disability"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-USASPENDING042014-060",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cfda 64 109",
+                "compensation for service-connected disability",
+                "compensation service",
+                "usa spending"
+            ],
+            "landingPage": "https://www.usaspending.gov/",
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
+            "temporal": "2014-04-01T04:00:00Z/2014-04-30T04:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 04/2014-Veterans Compensation for Service-Connected Disability"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wh83-r6xy",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-05-04",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-04",
-            "keyword": [
-                "age",
-                "fy20",
-                "fy 20",
-                "fy2020",
-                "fy 2020",
-                "gender",
-                "healthcare",
-                "health care",
-                "va healthcare",
-                "va health care",
-                "va user",
-                "va users",
-                "veteran",
-                "veteran healthcare",
-                "veteran health care",
-                "veterans",
-                "veteran user",
-                "veteran users"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mike Schwaber",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/wh83-r6xy",
+            "dataQuality": true,
             "description": "Note: \"Total Number of Veterans\" represents FY 2020 projected Veteran counts from VA's Veteran Population Projection Model 2018 (VetPop18).  These projections are made with the assumption that Veterans are not missing information (e.g. age, gender, etc.).\nNote: \"Veteran VA Users\" and \"Veteran VA Healthcare Users\" represent historical Veteran counts from VA's United States Veterans Eligibility Trends and Statistics 2020 (USVETS 2020).\nNote: \"Veteran VA Users\" includes Veteran users of VA healthcare or any other VA benefit or service.\nNote: There are 4,214 Veteran VA Users not shown in the table below whose gender is missing.  Of these, 4,126 are missing age.  There are 4,158 Veteran VA Healthcare Users not shown in the table below whose gender is missing.  Of these, 4,125 are missing age.\n\nSources: USVETS 2020 and VetPop18",
-            "title": "FY 2020 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Gender and Age Group",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86315,62 +86284,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wh83-r6xy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wh83-r6xy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wh83-r6xy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wh83-r6xy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wh83-r6xy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wh83-r6xy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wh83-r6xy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wh83-r6xy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wh83-r6xy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/wh83-r6xy",
+            "issued": "2022-05-04",
+            "keyword": [
+                "age",
+                "fy20",
+                "fy 20",
+                "fy2020",
+                "fy 2020",
+                "gender",
+                "healthcare",
+                "health care",
+                "va healthcare",
+                "va health care",
+                "va user",
+                "va users",
+                "veteran",
+                "veteran healthcare",
+                "veteran health care",
+                "veterans",
+                "veteran user",
+                "veteran users"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wh83-r6xy",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-05-04",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2020 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Gender and Age Group"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/whv8-3axt",
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
-            "identifier": "64fb06ff-2c60-41af-8799-2ae18ab5e473",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Idaho FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86378,37 +86362,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "64fb06ff-2c60-41af-8799-2ae18ab5e473",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/whv8-3axt",
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
+            "title": "State Summary Idaho FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/whzv-dw7c",
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
-            "identifier": "23a36ba1-2cde-4a99-95d4-b558bc6bd177",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Puerto Rico FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86416,86 +86400,85 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "23a36ba1-2cde-4a99-95d4-b558bc6bd177",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/whzv-dw7c",
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
+            "title": "State Summary Puerto Rico FY2017"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wibg-a2r3",
-            "issued": "2023-06-20",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-21",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Guam FY2021",
+            "identifier": "https://www.data.va.gov/api/views/wibg-a2r3",
+            "issued": "2023-06-20",
             "keyword": [
                 "fy2021 data",
                 "guam",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/wibg-a2r3",
+            "landingPage": "https://www.data.va.gov/d/wibg-a2r3",
+            "modified": "2024-06-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Guam FY2021",
             "title": "NCVAS State Summary Guam FY2021"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wjcc-nyd8",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "Access an article reviewing the development of the PTSD Repository as well as meta-analyses and journal articles that use PTSD Repository data.",
             "identifier": "https://www.data.va.gov/api/views/wjcc-nyd8",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/wjcc-nyd8",
+            "modified": "2025-01-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Access an article reviewing the development of the PTSD Repository as well as meta-analyses and journal articles that use PTSD Repository data.",
             "title": "Publications"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wjmx-tjt9",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "indiana",
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
-            "identifier": "VA-OEI-OEI-099",
             "description": "<p>This is a summary of the programs and services provided by VA in Indiana in fiscal year 2014.</p>",
-            "title": "State Summary:  Indiana",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86504,49 +86487,46 @@
                     "title": "State Summary:  Indiana"
                 }
             ],
+            "identifier": "VA-OEI-OEI-099",
+            "issued": "2017-07-26",
+            "keyword": [
+                "indiana",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wjmx-tjt9",
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
+            "title": "State Summary:  Indiana"
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
-            "identifier": "VA-VBA-ABR2012-100",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Michigan-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86554,27 +86534,50 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-100",
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
+                "029:005"
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
+            "title": "Michigan-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/wmd3-h26c",
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
+            "description": "<p>The Residency Allocation Database is used to determine allocation of funds for residency programs offered by Veterans Affairs Medical Centers (VAMCs). Information for the database comes from any VAMC that has made a funding request for its residency programs. The Office of Academic Affiliations distributes worksheets and memos are sent to participating VAMCs. VAMC personnel enter the information electronically into the database housed at the Academic Information Management Center (AIMC) located in St. Louis, Missouri. The data entry and collection process is done annually beginning in September and ending in December. The main user of this database is the Office of Academic Affiliations.</p>",
+            "identifier": "VA-VHA-OAA-003",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1993-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "academic",
                 "affiliation",
@@ -86585,61 +86588,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/wmd3-h26c",
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
-            "identifier": "VA-VHA-OAA-003",
-            "description": "<p>The Residency Allocation Database is used to determine allocation of funds for residency programs offered by Veterans Affairs Medical Centers (VAMCs). Information for the database comes from any VAMC that has made a funding request for its residency programs. The Office of Academic Affiliations distributes worksheets and memos are sent to participating VAMCs. VAMC personnel enter the information electronically into the database housed at the Academic Information Management Center (AIMC) located in St. Louis, Missouri. The data entry and collection process is done annually beginning in September and ending in December. The main user of this database is the Office of Academic Affiliations.</p>",
-            "title": "Residency Allocation Database",
-            "programCode": [
-                "029:040"
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
+            "title": "Residency Allocation Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wnay-6yw7",
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
-            "identifier": "https://www.data.va.gov/api/views/wnay-6yw7",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE OCT2018",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86647,66 +86630,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wnay-6yw7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wnay-6yw7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wnay-6yw7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wnay-6yw7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wnay-6yw7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wnay-6yw7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wnay-6yw7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wnay-6yw7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wnay-6yw7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/wnay-6yw7",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wnay-6yw7",
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
+            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE OCT2018"
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
-            "identifier": "VA-VBA-ABR2012-030",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Summary of Beneficiaries Who Began Receiving Compensation Benefits During FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86714,26 +86694,59 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-030",
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
+            "title": "Summary of Beneficiaries Who Began Receiving Compensation Benefits During FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wqi7-sdb3",
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
+            "description": "Why Not the Best VA or WNTBVA is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.  This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/wqi7-sdb3/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/wqi7-sdb3",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2020-10-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2018-10-01/2019-09-30",
-            "modified": "2021-06-24",
             "keyword": [
                 "2019",
                 "fy2019",
@@ -86752,68 +86765,39 @@
                 "veteran",
                 "wntbva"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Sail Operations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/wqi7-sdb3",
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
-            "identifier": "https://www.data.va.gov/api/views/wqi7-sdb3",
-            "description": "Why Not the Best VA or WNTBVA is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.  This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
-            "title": "Why Not the Best VA FY2019 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/wqi7-sdb3/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2018-10-01/2019-09-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Why Not the Best VA FY2019 Hospital Performance - All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wqnh-6zsz",
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
-            "identifier": "https://www.data.va.gov/api/views/wqnh-6zsz",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM BENEFITS to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA\u2019s determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAY2019",
-            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86821,108 +86805,109 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wqnh-6zsz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wqnh-6zsz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wqnh-6zsz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wqnh-6zsz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wqnh-6zsz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wqnh-6zsz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wqnh-6zsz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wqnh-6zsz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wqnh-6zsz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/wqnh-6zsz",
+            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 117"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wqnh-6zsz",
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
+            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAY2019"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wqpg-bgtc",
-            "issued": "2023-06-14",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
+            "description": "NCVAS State Summary Alabama FY 2021",
+            "identifier": "https://www.data.va.gov/api/views/wqpg-bgtc",
+            "issued": "2023-06-14",
             "keyword": [
                 "alabama",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/wqpg-bgtc",
+            "landingPage": "https://www.data.va.gov/d/wqpg-bgtc",
+            "modified": "2024-06-07",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Alabama FY 2021",
             "title": "NCVAS State Summary Alabama FY 2021"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wqz4-tnbm",
-            "issued": "2022-05-24",
             "@type": "dcat:Dataset",
-            "modified": "2022-05-24",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
+            "description": "The U.S. Department of Veterans Affairs honors America\u2019s Veterans by highlighting VA benefits provided to the Survivors of  those who made the ultimate sacrifice.",
+            "identifier": "https://www.data.va.gov/api/views/wqz4-tnbm",
+            "issued": "2022-05-24",
             "keyword": [
                 "benefits",
                 "survivors",
                 "veterans"
             ],
-            "identifier": "https://www.data.va.gov/api/views/wqz4-tnbm",
+            "landingPage": "https://www.data.va.gov/d/wqz4-tnbm",
+            "modified": "2022-05-24",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NCVAS"
             },
-            "description": "The U.S. Department of Veterans Affairs honors America\u2019s Veterans by highlighting VA benefits provided to the Survivors of  those who made the ultimate sacrifice.",
             "title": "On this Memorial Day, VA Honors the Men and Women Who Made the Ultimate Sacrifice Defending Our Country and Our Way of Life."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wria-e4pa",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "249be968-7e56-45f8-9fc1-17bf831a6a23",
+            "dataQuality": true,
             "description": "<p>To show count of Post 9/11 Veterans (Living only) by County for the creation of a heat map to align with Wounded Warrior Projects\u2019 programming.</p>",
-            "title": "Post 9/11 Veterans (Living only) by County",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86930,37 +86915,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "249be968-7e56-45f8-9fc1-17bf831a6a23",
+            "issued": "2019-04-24",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wria-e4pa",
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
+            "title": "Post 9/11 Veterans (Living only) by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wrjh-4pwf",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 116"
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
-            "identifier": "https://www.data.va.gov/api/views/wrjh-4pwf",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAMS to provide, through purchase and/or fabrication, prosthetic and related appliances, equipment and services to eligible veterans so that they may live and work as productive citizens. Veterans eligible for prosthetic services are service-connected veterans seeking care for a service-connected disability; veterans with compensable service-connected disabilities generally rated 10 percent or more; former prisoners of war, veterans discharged or released from active military service for a disability that was incurred or aggravated in the line of duty, and veterans who are in receipt of Section 1151 benefits; veterans who are in receipt of increased pension based on a need of regular aid and attendance or by reason of being permanently housebound; veterans who have annual income and net worth below the \"means test\" threshold; all other veterans who are not required to pay a copayment for their care, i.e., veterans of the Mexican border period and World War I, compensated zero (0) percent service-connected veterans who are receiving statutory awards, veterans exposed to a toxic substance, radiation or environmental hazard (limited to certain disabilities); and veterans who must pay a copayment for their care. Ineligible veterans are nonservice-connected veterans residing or sojourning in foreign lands.</p>",
-            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES JAN2019",
-            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86968,40 +86952,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wrjh-4pwf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wrjh-4pwf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wrjh-4pwf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wrjh-4pwf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wrjh-4pwf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wrjh-4pwf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wrjh-4pwf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wrjh-4pwf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wrjh-4pwf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/wrjh-4pwf",
+            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 116"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wrjh-4pwf",
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
+            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES JAN2019"
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
+            "description": "<p>USA Spending- Reserve Educational Assistance Program (Chapter 1606/1607) for January 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-022",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 028",
                 "chapter 1606 1607",
@@ -87009,66 +87015,38 @@
                 "reap",
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
-            "identifier": "VA-VBA-USASPENDING012014-022",
-            "description": "<p>USA Spending- Reserve Educational Assistance Program (Chapter 1606/1607) for January 2014</p>",
-            "title": "USA Spending file- Education- Chapter 1606/1607- CFDA 64.032",
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
+            "title": "USA Spending file- Education- Chapter 1606/1607- CFDA 64.032"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/AverageAgeByState.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Average_Age_by_State.doc"
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
-            "identifier": "VA-VBA-INS2011-005",
+            "dataQuality": true,
             "description": "<p>The Average Age by State dataset provides the average age of Government life insurance policyholders in the administered programs in each state.  The data is reported at the state level, plus insureds in Military America, Military Europe, Military Pacific, American Samoa, Federated States of Micronesia, Guam, Marshall Islands, Northern Mariana Islands, Puerto Rico, and the Virgin Islands.</p>",
-            "title": "FY11_Average Life Insurance Policyholders' Age by State",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87076,71 +87054,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wsij-s2mv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wsij-s2mv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wsij-s2mv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wsij-s2mv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wsij-s2mv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wsij-s2mv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wsij-s2mv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wsij-s2mv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wsij-s2mv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-005",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/AverageAgeByState.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Average_Age_by_State.doc"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY11_Average Life Insurance Policyholders' Age by State"
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
-                "lgy",
-                "loan guarantee benefits fy12",
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
-            "identifier": "VA-VBA-ABR2012-047",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Purchase Loans Guaranteed Based on Annual Income During Fiscal Year 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87148,45 +87128,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-047",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "lgy",
+                "loan guarantee benefits fy12",
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
+            "title": "Purchase Loans Guaranteed Based on Annual Income During Fiscal Year 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Surveys.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2009-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "survey",
-                "veterans"
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
-            "identifier": "VA-OEI-OEI-048",
+            "dataQuality": true,
             "description": "<p>The 2010 National Survey of Veterans (NSV) is the sixth in a series of comprehensive nationwide surveys designed to help the Department of Veterans Affairs (VA) plan its future programs and services for Veterans. It also provides a snapshot profile of the Veteran population. Data collected through the NSV enables VA to: follow changing trends in the Veteran population; compare characteristics of Veterans who use VA benefits and services with those of Veterans who do not; study VA\u00ef\u00bf\u00bds role in the delivery of all benefits and services that Veterans receive; and update information about Veterans to help the Department develop its policies.</p>",
-            "title": "National Survey of Veterans, Active Duty Service Members, Demobilized National Guard and Reserve Members, Family Members, and Surviving Spouses",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87195,44 +87178,43 @@
                     "title": "National Survey of Veterans, Active Duty Service Members, Demobilized National Guard and Reserve Members, Family Members, and Surviving Spouses"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-048",
+            "issued": "2017-07-26",
+            "keyword": [
+                "survey",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/Surveys.asp",
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
+            "temporal": "2009-10-01T04:00:00Z/2009-03-31T04:00:00Z",
             "theme": [
                 "Data on Veterans"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Survey of Veterans, Active Duty Service Members, Demobilized National Guard and Reserve Members, Family Members, and Surviving Spouses"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wtbd-7s8x",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
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
-            "identifier": "VA-OM-OM-112",
             "description": "<p>FY 2003 Franchise Fund Annual Report Objectives</p>",
-            "title": "FY 2003 Franchise Fund Annual Report Objectives",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87241,24 +87223,54 @@
                     "title": "FY 2003 Franchise Fund Annual Report Objectives"
                 }
             ],
+            "identifier": "VA-OM-OM-112",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wtbd-7s8x",
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
+            "title": "FY 2003 Franchise Fund Annual Report Objectives"
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
-            "temporal": "2016-01-15T05:00:00Z/2016-01-15T05:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR38_012016_Pending_and_EWL_Biweekly_Desired_Date%20Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 January 2016"
+                }
             ],
+            "identifier": "VA-VHA-OIA-732",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -87272,76 +87284,44 @@
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
-            "identifier": "VA-VHA-OIA-732",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 January 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR38_012016_Pending_and_EWL_Biweekly_Desired_Date%20Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 January 2016"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2016-01-15T05:00:00Z/2016-01-15T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 January 15"
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
-            "identifier": "VA-VBA-ABR2012-032",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Veterans Receiving Service Connected Disability Benefits at the End of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87349,46 +87329,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-032",
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
+            "title": "Veterans Receiving Service Connected Disability Benefits at the End of FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wubk-nag4",
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
-            "identifier": "https://www.data.va.gov/api/views/wubk-nag4",
             "description": "VetPop2023 projection of living Veterans by gender and 5-year age groups at the national level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 National Data, 1L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87396,56 +87377,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wubk-nag4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wubk-nag4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wubk-nag4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wubk-nag4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wubk-nag4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wubk-nag4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wubk-nag4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wubk-nag4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wubk-nag4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/wubk-nag4",
+            "issued": "2024-09-05",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wubk-nag4",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 National Data, 1L"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wvu4-6q6e",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "massachusetts"
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
-            "identifier": "VA-OEI-OEI-191",
             "description": "<p>This summary describes the programs and services VA provided in Massachusetts in fiscal year 2015.</p>",
-            "title": "State Summary: Massachusetts",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87454,41 +87438,40 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-191",
+            "issued": "2017-07-26",
+            "keyword": [
+                "massachusetts"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wvu4-6q6e",
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
+            "title": "State Summary: Massachusetts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "annual report",
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
-            "identifier": "VA-OEI-OEI-144",
             "description": "<p>This reports the activities of the Veterans Administration for the fiscal year ending September 30, 1980.</p>",
-            "title": "1980 Annual Report",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87497,21 +87480,52 @@
                     "title": "Annual Report:  1980"
                 }
             ],
+            "identifier": "VA-OEI-OEI-144",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/",
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
                 "Demographics"
-            ]
+            ],
+            "title": "1980 Annual Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/data/VAOpenDataMigration2019/Lives_Insured_by_Fiscal_Year.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Lives Insured by Fiscal Year"
+                }
+            ],
+            "identifier": "VA-VBA-ABR2012-076",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
             "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
             "keyword": [
                 "abr",
                 "abr2012",
@@ -87519,71 +87533,39 @@
                 "insurance benefits fy12",
                 "vba benefits"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
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
-            "identifier": "VA-VBA-ABR2012-076",
-            "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Lives Insured by Fiscal Year",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/data/VAOpenDataMigration2019/Lives_Insured_by_Fiscal_Year.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "Lives Insured by Fiscal Year"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR Reports"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Lives Insured by Fiscal Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/docs/Utilizaiton",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "1800-01-01T05:00:00Z/2012-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "casket",
-                "cremain",
-                "national cemeteries",
-                "veteran interments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Cordes",
                 "hasEmail": "mailto:vicki.cordes@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-NCA-MS-058",
+            "dataQuality": true,
             "description": "<p>Total Veteran Interments at National Cemeteries, and shown by Interment Type, Casketed vs. Cremated Remains, FY 2000 to FY2012.  Source:  Department of Veterans Affairs, National Cemetery Administration, Policy and Planning Service.  Data are compiled from NCA's Burial Operations Support System (BOSS) and Management and Decision Support System (MADSS).</p>",
-            "title": "National Cemetery Administration Summary of Veteran Interments:  FY2000 to FY2012",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87592,68 +87574,70 @@
                     "title": "National Cemetery Administration Summary of Veteran Interments:  FY2000 to FY2012"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-MS-058",
+            "issued": "2017-07-26",
+            "keyword": [
+                "casket",
+                "cremain",
+                "national cemeteries",
+                "veteran interments"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/docs/Utilizaiton",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "1800-01-01T05:00:00Z/2012-12-31T05:00:00Z",
             "theme": [
                 "Interments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Cemetery Administration Summary of Veteran Interments:  FY2000 to FY2012"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wxa3-iimb",
-            "issued": "2023-06-15",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-16",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Alaska FY2021",
+            "identifier": "https://www.data.va.gov/api/views/wxa3-iimb",
+            "issued": "2023-06-15",
             "keyword": [
                 "alaska",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/wxa3-iimb",
+            "landingPage": "https://www.data.va.gov/d/wxa3-iimb",
+            "modified": "2024-05-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Alaska FY2021",
             "title": "NCVAS State Summary Alaska FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wxe2-54qw",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-11-12T05:00:00Z/2015-07-28T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cemerty grants"
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
-            "identifier": "VA-NCA-CG-002",
+            "dataQuality": true,
             "description": "<p>Instructions for applying for Veterans Cemetery Grants for States, Territories, or Federally Recognized Tribal Governments.</p>",
-            "title": "Instructions for Applying for Grants",
-            "programCode": [
-                "029:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87662,42 +87646,42 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-CG-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cemerty grants"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wxe2-54qw",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-11-12T05:00:00Z/2015-07-28T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "Instructions for Applying for Grants"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/wxxh-wr3i",
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
-            "identifier": "https://www.data.va.gov/api/views/wxxh-wr3i",
+            "dataQuality": true,
             "description": "<p>VBA COMPENSTATION BENEFITS PRGOGRAM to provide vocational training and rehabilitation to certain children born with spina bifida or other covered birth defects who are children of Vietnam veterans and some Korean veterans. \u201cA child born with spina bifida or other covered birth defects, except spina bifida occulta, who is the natural child of a Vietnam veteran and some Korean veterans, regardless of the age or marital status of the child, conceived after the date on which the veteran first served in the Republic of Vietnam during the Vietnam era and in particular areas near the DMZ in the Korean conflict. VA must also determine that it is feasible for the child to achieve a vocational goal.\u201d</p>",
-            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA FEB2019",
-            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87705,66 +87689,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wxxh-wr3i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wxxh-wr3i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wxxh-wr3i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wxxh-wr3i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wxxh-wr3i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wxxh-wr3i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wxxh-wr3i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wxxh-wr3i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wxxh-wr3i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/wxxh-wr3i",
+            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 127"
+            ],
+            "landingPage": "https://www.data.va.gov/d/wxxh-wr3i",
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
+            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA FEB2019"
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
-            "identifier": "VA-VBA-ABR2012-006",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Beneficiaries Receiving DIC Benefits by Period of Service at the End of Fiscal Year 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87772,51 +87752,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-006",
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
+            "title": "Beneficiaries Receiving DIC Benefits by Period of Service at the End of Fiscal Year 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/FaceAmountbyProgrambyStateDecember2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-12-01T05:00:00Z/2012-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Face_Amount_by_Program_December_2012.doc"
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
-            "identifier": "VA-VBA-INS2012-002",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 12/31/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Face Amount of Life Insurance Coverage by Program by State 2012/12/31",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87824,71 +87801,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wznr-if7g/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wznr-if7g/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wznr-if7g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/wznr-if7g/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wznr-if7g/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wznr-if7g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/wznr-if7g/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/wznr-if7g/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/wznr-if7g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-002",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/FaceAmountbyProgrambyStateDecember2012.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Face_Amount_by_Program_December_2012.doc"
+            ],
+            "temporal": "2012-12-01T05:00:00Z/2012-12-31T05:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Face Amount of Life Insurance Coverage by Program by State 2012/12/31"
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
-            "identifier": "VA-VBA-ABR2012-119",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Puerto Rico FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87896,43 +87876,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-119",
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
+            "title": "Puerto Rico FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/x34w-w4dp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "new mexico"
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
-            "identifier": "VA-OEI-OEI-202",
             "description": "<p>This summary describes the programs and services VA provided in New Mexico in fiscal year 2015.</p>",
-            "title": "State Summary: New Mexico FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87941,24 +87925,52 @@
                     "title": "New Mexico"
                 }
             ],
+            "identifier": "VA-OEI-OEI-202",
+            "issued": "2017-07-26",
+            "keyword": [
+                "new mexico"
+            ],
+            "landingPage": "https://www.data.va.gov/d/x34w-w4dp",
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
+            "title": "State Summary: New Mexico FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/x3fv-ebud",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Public",
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
+                    "downloadURL": "https://www.data.va.gov/download/x3fv-ebud/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/x3fv-ebud",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2020-08-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-10-01/2015-09-30",
-            "modified": "2021-06-24",
             "keyword": [
                 "2015",
                 "analytics",
@@ -87979,67 +87991,41 @@
                 "veterans health administration",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Sail Operations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/x3fv-ebud",
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
-            "identifier": "https://www.data.va.gov/api/views/x3fv-ebud",
-            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
-            "title": "SAIL FY2015 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/x3fv-ebud/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
+            "rights": "Public",
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2014-10-01/2015-09-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAIL FY2015 Hospital Performance - All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/x3x3-62u4",
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
-            "title": "Equitable Relief Reports 2004",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88047,53 +88033,70 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/x3x3-62u4",
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
+            "title": "Equitable Relief Reports 2004"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/x65v-effz",
-            "issued": "2023-06-29",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-28",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Iowa FY2021",
+            "identifier": "https://www.data.va.gov/api/views/x65v-effz",
+            "issued": "2023-06-29",
             "keyword": [
                 "fy2021 data",
                 "iowa",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/x65v-effz",
+            "landingPage": "https://www.data.va.gov/d/x65v-effz",
+            "modified": "2024-05-28",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Iowa FY2021",
             "title": "NCVAS State Summary Iowa FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/x69m-zikx",
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
+            "description": "<p>The mission of the VA Clinical Assessment Reporting and Tracking (CART) Program for cardiac catheterization laboratories (CART-CL) is to support a national VA reporting system, data repository, and quality improvement program for procedures performed in VA cardiac catheterization laboratories. CART-CL is intended to improve clinical care/communication, support local and national quality improvement, monitor patient safety, capture workload of cardiac catheterization lab procedures, and inform VA system evaluation to maximize operational efficiency and patient outcomes. CART-CL is a collaborative effort between the VA Patient Care Services, Office of Information and Analytics, Ischemic Heart Disease Quality Enhancement Research Initiative (IHD-QUERI), and Office of Information and Technology (OI&amp;T).</p>",
+            "identifier": "VA-VHA-PCS-016",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2005-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "cardiac",
                 "cart",
@@ -88107,84 +88110,65 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/x69m-zikx",
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
-            "identifier": "VA-VHA-PCS-016",
-            "description": "<p>The mission of the VA Clinical Assessment Reporting and Tracking (CART) Program for cardiac catheterization laboratories (CART-CL) is to support a national VA reporting system, data repository, and quality improvement program for procedures performed in VA cardiac catheterization laboratories. CART-CL is intended to improve clinical care/communication, support local and national quality improvement, monitor patient safety, capture workload of cardiac catheterization lab procedures, and inform VA system evaluation to maximize operational efficiency and patient outcomes. CART-CL is a collaborative effort between the VA Patient Care Services, Office of Information and Analytics, Ischemic Heart Disease Quality Enhancement Research Initiative (IHD-QUERI), and Office of Information and Technology (OI&amp;T).</p>",
-            "title": "VA Clinical Assessment Reporting and Tracking (CART) Program",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "2005-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Clinical Assessment Reporting and Tracking (CART) Program"
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/x6jv-ykjw",
-            "issued": "2024-05-20",
+        {
             "@type": "dcat:Dataset",
-            "modified": "2024-05-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis & Statistics",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
+            "description": "2024 Memorial Day data story honoring World War II Veterans.",
+            "identifier": "https://www.data.va.gov/api/views/x6jv-ykjw",
+            "issued": "2024-05-20",
             "keyword": [
                 "memorial day",
                 "world war ii"
             ],
-            "identifier": "https://www.data.va.gov/api/views/x6jv-ykjw",
+            "landingPage": "https://www.data.va.gov/d/x6jv-ykjw",
+            "modified": "2024-05-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "2024 Memorial Day data story honoring World War II Veterans.",
             "title": "Memorial Day 2024 - World War II"
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
-            "modified": "2024-06-07",
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
-            "identifier": "VA-OM-OM-099",
+            "dataQuality": true,
             "description": "<p>FY 2015 Budget Submission Volume III: Benefits and Burial Programs and Departmental Administration</p>",
-            "title": "FY 2015 Budget Submission Volume III",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88193,27 +88177,46 @@
                     "title": "FY 2015 Budget Submission"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-099",
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
+            "modified": "2024-06-07",
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
+            "title": "FY 2015 Budget Submission Volume III"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/x6z5-25xw",
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
+            "description": "<p>The Nuclear Medicine National HQ System database is a series of MS Excel spreadsheets and Access Database Tables by fiscal year. They consist of information from all Veterans Affairs Medical Centers (VAMCs) performing or contracting nuclear medicine services in Veterans Affairs medical facilities. The medical centers are required to complete questionnaires annually (RCS 10-0010-Nuclear Medicine Service Annual Report). The information is then manually entered into the Access Tables, which includes: * Distribution and cost of in-house VA - Contract Physician Services, whether contracted services are made via sharing agreement (with another VA medical facility or other government medical providers) or with private providers. * Workload data for the performance and/or purchase of PET/CT studies. * Organizational structure of services. * Updated changes in key imaging service personnel (chiefs, chief technicians, radiation safety officers). * Workload data on the number and type of studies (scans) performed, including Medicare Relative Value Units (RVUs), also referred to as Weighted Work Units (WWUs). WWUs are a workload measure calculated as the product of a study's Current Procedural Terminology (CPT) code, which consists of total work costs (the cost of physician medical expertise and time), and total practice costs (the costs of running a practice, such as equipment, supplies, salaries, utilities etc). Medicare combines WWUs together with one other parameter to derive RVUs, a workload measure widely used in the health care industry. WWUs allow Nuclear Medicine to account for the complexity of each study in assessing workload, that some studies are more time consuming and require higher levels of expertise. This gives a more accurate picture of workload; productivity etc than using just 'total studies' would yield. * A detailed Full-Time Equivalent Employee (FTEE) grid, and staffing distributions of FTEEs across nuclear medicine services. * Information on Radiation Safety Committees and Radiation Safety Officers (RSOs).  Beginning in 2011 this will include data collection on part-time and non VA (contract) RSOs; other affiliations they may have and if so to whom they report (supervision) at their VA medical center.<em>Collection of data on nuclear medicine services' progress in meeting the special needs of our female veterans.</em> Revolving documentation of all major VA-owned gamma cameras (by type) and computer systems, their specifications and ages. * Revolving data collection for PET/CT cameras owned or leased by VA; and the numbers and types of PET/CT studies performed on VA patients whether produced on-site, via mobile PET/CT contract or from non-VA providers in the community.* Types of educational training/certification programs available at VA sites * Ongoing funded research projects by Nuclear Medicine (NM) staff, identified by source of funding and research purpose. * Data on physician-specific quality indicators at each nuclear medicine service.* Academic achievements by NM staff, including published books/chapters, journals and abstracts. * Information from polling field sites re: relevant issues and programs Headquarters needs to address. * Results of a Congressionally mandated contracted quality assessment exercise, also known as a Proficiency study. Study results are analyzed for comparison within VA facilities (for example by mission or size), and against participating private sector health care groups. * Information collected on current issues in nuclear medicine as they arise.  Radiation Safety Committee structures and membership, Radiation Safety Officer information and information on how nuclear medicine services provided for female Veterans are examples of current issues.The database is now stored completely within MS Access Database Tables with output still presented in the form of Excel graphs and tables.</p>",
+            "identifier": "VA-VHA-PCS-011",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "cost",
                 "cpt",
@@ -88225,70 +88228,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/x6z5-25xw",
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
-            "identifier": "VA-VHA-PCS-011",
-            "description": "<p>The Nuclear Medicine National HQ System database is a series of MS Excel spreadsheets and Access Database Tables by fiscal year. They consist of information from all Veterans Affairs Medical Centers (VAMCs) performing or contracting nuclear medicine services in Veterans Affairs medical facilities. The medical centers are required to complete questionnaires annually (RCS 10-0010-Nuclear Medicine Service Annual Report). The information is then manually entered into the Access Tables, which includes: * Distribution and cost of in-house VA - Contract Physician Services, whether contracted services are made via sharing agreement (with another VA medical facility or other government medical providers) or with private providers. * Workload data for the performance and/or purchase of PET/CT studies. * Organizational structure of services. * Updated changes in key imaging service personnel (chiefs, chief technicians, radiation safety officers). * Workload data on the number and type of studies (scans) performed, including Medicare Relative Value Units (RVUs), also referred to as Weighted Work Units (WWUs). WWUs are a workload measure calculated as the product of a study's Current Procedural Terminology (CPT) code, which consists of total work costs (the cost of physician medical expertise and time), and total practice costs (the costs of running a practice, such as equipment, supplies, salaries, utilities etc). Medicare combines WWUs together with one other parameter to derive RVUs, a workload measure widely used in the health care industry. WWUs allow Nuclear Medicine to account for the complexity of each study in assessing workload, that some studies are more time consuming and require higher levels of expertise. This gives a more accurate picture of workload; productivity etc than using just 'total studies' would yield. * A detailed Full-Time Equivalent Employee (FTEE) grid, and staffing distributions of FTEEs across nuclear medicine services. * Information on Radiation Safety Committees and Radiation Safety Officers (RSOs).  Beginning in 2011 this will include data collection on part-time and non VA (contract) RSOs; other affiliations they may have and if so to whom they report (supervision) at their VA medical center.<em>Collection of data on nuclear medicine services' progress in meeting the special needs of our female veterans.</em> Revolving documentation of all major VA-owned gamma cameras (by type) and computer systems, their specifications and ages. * Revolving data collection for PET/CT cameras owned or leased by VA; and the numbers and types of PET/CT studies performed on VA patients whether produced on-site, via mobile PET/CT contract or from non-VA providers in the community.* Types of educational training/certification programs available at VA sites * Ongoing funded research projects by Nuclear Medicine (NM) staff, identified by source of funding and research purpose. * Data on physician-specific quality indicators at each nuclear medicine service.* Academic achievements by NM staff, including published books/chapters, journals and abstracts. * Information from polling field sites re: relevant issues and programs Headquarters needs to address. * Results of a Congressionally mandated contracted quality assessment exercise, also known as a Proficiency study. Study results are analyzed for comparison within VA facilities (for example by mission or size), and against participating private sector health care groups. * Information collected on current issues in nuclear medicine as they arise.  Radiation Safety Committee structures and membership, Radiation Safety Officer information and information on how nuclear medicine services provided for female Veterans are examples of current issues.The database is now stored completely within MS Access Database Tables with output still presented in the form of Excel graphs and tables.</p>",
-            "title": "Nuclear Medicine National Headquarter System",
-            "programCode": [
-                "029:041"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nuclear Medicine National Headquarter System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_COMP_by_County_2010.doc",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_COMP_by_County_2010.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "compensation",
-                "county",
-                "pension",
-                "state",
-                "va",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amy Hamma",
                 "hasEmail": "mailto:Amy.Hamma@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-CP2010-001",
+            "dataQuality": true,
             "description": "<p>This data set shows the number of veterans and survivors who are receiving either disability compensation or pension benefits from the Department of Veterans Affairs.</p>",
-            "title": "FY10 Compensation and Pension by County",
-            "isPartOf": "VA-VBA-MASTER-COMPENSATIONPENSION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88297,46 +88272,54 @@
                     "title": "xls"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-CP2010-001",
+            "isPartOf": "VA-VBA-MASTER-COMPENSATIONPENSION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "compensation",
+                "county",
+                "pension",
+                "state",
+                "va",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_COMP_by_County_2010.doc",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_COMP_by_County_2010.doc"
+            ],
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Section 10. National Security and Veterans Affairs"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY10 Compensation and Pension by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/x8rf-x7ii",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "NA",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2013-08-01T04:00:00Z/2015-08-03T04:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "inventory",
-                "memorial"
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
-            "identifier": "VA-NCA-HIS-001",
+            "dataQuality": true,
             "description": "<p>This is the most recent list all monuments cataloged by the History Program, as required.  The objects are provided alphabetically by cemetery name; other formats are available on request.</p>",
-            "title": "National Cemetery Administration Memorial Inventory, August 2013",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88345,46 +88328,47 @@
                     "title": "National Cemetery Administration (NCA) Memorial Inventory, August 2013"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-HIS-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "inventory",
+                "memorial"
+            ],
+            "landingPage": "https://www.data.va.gov/d/x8rf-x7ii",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "NA",
+            "temporal": "2013-08-01T04:00:00Z/2015-08-03T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Cemetery Administration Memorial Inventory, August 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xag2-8znm",
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
-            "identifier": "92b9ecc4-18a5-4a20-a5dc-a37a6efdd22b",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Iowa FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88392,153 +88376,156 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "92b9ecc4-18a5-4a20-a5dc-a37a6efdd22b",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xag2-8znm",
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
+            "title": "State Summary Iowa FY2017"
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
+            "description": "<p>USA Spending- Non Service Connected Disability- February 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING022014-032",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING022014-032",
-            "description": "<p>USA Spending- Non Service Connected Disability- February 2014.</p>",
-            "title": "USA Spending file- 02/2014 Compensation and Pension-  CFDA 64.104",
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
+            "title": "USA Spending file- 02/2014 Compensation and Pension-  CFDA 64.104"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "Department of Veterans Affairs"
             ],
-            "landingPage": "https://www.data.va.gov/d/xayc-j8g6",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Veterans Analysis and Statistics",
+                "hasEmail": "mailto:VANCVAS@VA.GOV"
+            },
+            "description": "Veteran Population Projection Model (VetPop) Landing Page containing links to current VetPop data products as well as methodology documentation.",
+            "identifier": "https://www.data.va.gov/api/views/xayc-j8g6",
             "issued": "2024-09-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-25",
             "keyword": [
                 "veteran population",
                 "veterans",
                 "vetpop"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Veterans Analysis and Statistics",
-                "hasEmail": "mailto:VANCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/xayc-j8g6",
+            "modified": "2024-10-25",
+            "programCode": [
+                "Office of Enterprise Integration"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/xayc-j8g6",
-            "description": "Veteran Population Projection Model (VetPop) Landing Page containing links to current VetPop data products as well as methodology documentation.",
-            "title": "Veteran Population Projection Model (VetPop) Landing Page",
-            "programCode": [
-                "Office of Enterprise Integration"
-            ]
+            "title": "Veteran Population Projection Model (VetPop) Landing Page"
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
+            "description": "<p>USA Spending- Veterans Surviving Spouses and Children- January 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-019",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING012014-019",
-            "description": "<p>USA Spending- Veterans Surviving Spouses and Children- January 2014</p>",
-            "title": "USA Spending file- 01/2014 Compensation and Pension-  CFDA 64.105",
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
+            "title": "USA Spending file- 01/2014 Compensation and Pension-  CFDA 64.105"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/xb3x-eesm",
-            "issued": "2024-07-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-25",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/xb3x-eesm",
             "description": "",
-            "title": "Marital Status of Veterans by Gender",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88546,57 +88533,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xb3x-eesm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xb3x-eesm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xb3x-eesm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/xb3x-eesm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xb3x-eesm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xb3x-eesm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xb3x-eesm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xb3x-eesm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xb3x-eesm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/xb3x-eesm",
+            "issued": "2024-07-25",
+            "landingPage": "https://www.data.va.gov/d/xb3x-eesm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-07-25",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Marital Status of Veterans by Gender"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xbrg-ga2x",
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
-            "identifier": "https://www.data.va.gov/api/views/xbrg-ga2x",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located</p>",
-            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS JAN2019",
-            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88604,63 +88588,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xbrg-ga2x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xbrg-ga2x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xbrg-ga2x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/xbrg-ga2x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xbrg-ga2x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xbrg-ga2x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xbrg-ga2x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xbrg-ga2x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xbrg-ga2x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/xbrg-ga2x",
+            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 118"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xbrg-ga2x",
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
+            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS JAN2019"
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
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
-                "franchise fund",
-                "fy 2009"
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
-            "identifier": "VA-OM-OM-036",
+            "dataQuality": true,
             "description": "<p>Franchise Fund FY 2009 Annual Report</p>",
-            "title": "Franchise Fund FY 2009 Annual Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88669,44 +88652,45 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-036",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund",
+                "fy 2009"
+            ],
+            "landingPage": "https://www.va.gov/FUND/VA_Franchise_Fund_Annual_Reports.asp",
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
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Franchise Fund FY 2009 Annual Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xcnp-xf7z",
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
-            "identifier": "539f9e80-3e1b-4376-9782-e4c1c697ee17",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Pennsylvania FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88714,37 +88698,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "539f9e80-3e1b-4376-9782-e4c1c697ee17",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xcnp-xf7z",
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
+            "title": "State Summary Pennsylvania FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xee2-wppd",
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
-            "identifier": "https://www.data.va.gov/api/views/xee2-wppd",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist wartime veterans in need whose non-service- connected disabilities are permanent and total preventing them from following a substantially gainful occupation. A Veteran who meets the wartime service requirements is potential eligible if he/she is: \u2022 permanently and totally disabled for reasons not necessarily due to service, \u2022 age 65 or older, or \u2022 is presumed to be totally and permanently disabled for pension purposes because: o he/she is a patient in a nursing home for long-term care due to a disability, or o being disabled, as determined by the Commissioner of Social Security (SS) for purposes of any benefits administered by the Commissioner, such as SS disability benefits or Supplemental Security Income. Income restrictions are prescribed in 38 U.S.C. 1521. Pension is not payable to those whose estates are so large that it is reasonable they use the estate for maintenance. A Veteran meets wartime service requirements if he/she served: \u2022 a total of 90 days or more during one or more periods of war; \u2022 90 or more consecutive days that began or ended during a period of war; or \u2022 for any length of time during a period of war if he/she was discharged or released for a service-connected disability. Veterans entering service after September 7, 1980, must also meet the minimum active duty requirement of 24 months of continuous service or the full period to which the Veteran was called to active duty. (38 U.S.C.5303(A)).</p>",
-            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS MAR2019",
-            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88752,61 +88736,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xee2-wppd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xee2-wppd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xee2-wppd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/xee2-wppd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xee2-wppd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xee2-wppd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xee2-wppd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xee2-wppd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xee2-wppd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/xee2-wppd",
+            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 104"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xee2-wppd",
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
+            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xg3p-ebyr",
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
-            "identifier": "65a209fc-057a-4276-ba17-47938b1ee08f",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Montana FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88814,39 +88798,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "65a209fc-057a-4276-ba17-47938b1ee08f",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xg3p-ebyr",
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
+            "title": "State Summary Montana FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2014-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "survivor",
-                "survivors",
-                "survivors benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Survivors Assistance",
                 "hasEmail": "mailto:officeofsurvivors@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OSA",
+            "dataQuality": true,
             "description": "<p>This report will provide you with information about the activities and efforts made within OSA to further serve the Survivor community.</p>",
-            "title": "Office of Survivors Assistance Annual Report",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88855,81 +88838,80 @@
                     "title": "Office of Survivors Assistance Annual Report"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OSA",
+            "issued": "2017-07-26",
+            "keyword": [
+                "survivor",
+                "survivors",
+                "survivors benefits"
+            ],
+            "landingPage": "https://www.va.gov/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2010-10-01T04:00:00Z/2014-10-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Office of Survivors Assistance Annual Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/xhx8-6a7y",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary South Carolina FY2023",
+            "identifier": "https://www.data.va.gov/api/views/xhx8-6a7y",
             "issued": "2024-06-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "south carolina"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/xhx8-6a7y",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/xhx8-6a7y",
-            "description": "NCVAS State Summary South Carolina FY2023",
-            "title": "NCVAS State Summary South Carolina FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary South Carolina FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xijb-4jk3",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-09-16",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/DataGov_GDX_FY09_Technical_Notes.doc"
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
-            "identifier": "VA-OEI-OEI-007",
-            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
-            "title": "Veterans Affairs Geographic Distribution of Expenditures FY09 by Congressional District",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/VETDATA/docs/Datagov/DataGov_GDX_FY09_Technical_Notes.doc",
             "describedByType": "application/msword",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88938,28 +88920,50 @@
                     "title": "csv"
                 }
             ],
-            "describedBy": "https://www.va.gov/VETDATA/docs/Datagov/DataGov_GDX_FY09_Technical_Notes.doc",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-007",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xijb-4jk3",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-09-16",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/DataGov_GDX_FY09_Technical_Notes.doc"
+            ],
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Affairs Geographic Distribution of Expenditures FY09 by Congressional District"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/xirr-5jyd",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Contains Health Insurance Portability and Accountabilty Act (HIPAA) protected data.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>SPAN receives data from VHA suicide prevention coordinators relating to suicidal ideation and suicidal behavior of Veterans. Data include relevant historical activities and related medical concerns as reviewed in the Veteran's medical record. Data are submitted to VSSC and are cleaned, processed, and managed by statistical staff and program analysts at the VISN 2 Center of Excellence for Suicide Prevention on behalf of the Mental Health Services.</p>",
+            "identifier": "VA-VHA-10N-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2012-12-01T05:00:00Z/2014-10-31T04:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "attempt",
                 "health",
@@ -88970,62 +88974,40 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/xirr-5jyd",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-10N-001",
-            "description": "<p>SPAN receives data from VHA suicide prevention coordinators relating to suicidal ideation and suicidal behavior of Veterans. Data include relevant historical activities and related medical concerns as reviewed in the Veteran's medical record. Data are submitted to VSSC and are cleaned, processed, and managed by statistical staff and program analysts at the VISN 2 Center of Excellence for Suicide Prevention on behalf of the Mental Health Services.</p>",
-            "title": "Suicide Prevention Applications Network (SPAN)",
-            "programCode": [
-                "029:042"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "rights": "Contains Health Insurance Portability and Accountabilty Act (HIPAA) protected data.",
+            "temporal": "2012-12-01T05:00:00Z/2014-10-31T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suicide Prevention Applications Network (SPAN)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xjvh-dhjy",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "1868",
-                "annual report",
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
-            "identifier": "VA-OEI-OEI-140",
             "description": "<p>VA Historical Annual Reports detail services provided by the Department for each Fiscal Year, including Benefits, Healthcare, and Burial/Memorial services.  The Reports also describe the topics of administration and management within VA, ranging from data on personnel to information on construction projects.  Statistical tables for a variety of subjects are also included.</p>",
-            "title": "Annual Report:  1868",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89034,41 +89016,43 @@
                     "title": "Annual Report:  1868"
                 }
             ],
+            "identifier": "VA-OEI-OEI-140",
+            "issued": "2017-07-26",
+            "keyword": [
+                "1868",
+                "annual report",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xjvh-dhjy",
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
                 "Demographics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Annual Report:  1868"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xkpw-b93n",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ohio"
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
-            "identifier": "VA-OEI-OEI-206",
             "description": "<p>This summary describes the programs and services VA provided in Ohio in fiscal year 2015.</p>",
-            "title": "State Summary: Ohio FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89077,37 +89061,40 @@
                     "title": "Ohio"
                 }
             ],
+            "identifier": "VA-OEI-OEI-206",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ohio"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xkpw-b93n",
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
+            "title": "State Summary: Ohio FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/xmgc-qy2m",
-            "issued": "2024-07-18",
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
-            "identifier": "https://www.data.va.gov/api/views/xmgc-qy2m",
             "description": "VetPop2020 projections by gender and period of service from 2020 to 2050.",
-            "title": "VetPop2020_GenderPeriodOfService",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89115,39 +89102,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xmgc-qy2m/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xmgc-qy2m/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xmgc-qy2m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/xmgc-qy2m/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xmgc-qy2m/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xmgc-qy2m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xmgc-qy2m/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xmgc-qy2m/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xmgc-qy2m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/xmgc-qy2m",
+            "issued": "2024-07-18",
+            "landingPage": "https://www.data.va.gov/d/xmgc-qy2m",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020_GenderPeriodOfService"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xmxj-urpw",
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
+                    "downloadURL": "https://www.data.va.gov/download/xmxj-urpw/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/xmxj-urpw",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2023-08-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-10-01/2023-09-30",
-            "modified": "2024-05-06",
             "keyword": [
                 "2023",
                 "analytics",
@@ -89170,50 +89183,43 @@
                 "sail",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHASailOperations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/xmxj-urpw",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-05-06",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/xmxj-urpw",
-            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).",
-            "title": "SAIL FY2023 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/xmxj-urpw/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2022-10-01/2023-09-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAIL FY2023 Hospital Performance - All Facilities"
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
+            "description": "<p>USA Spending- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects- March 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING132013-057",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "birth defects",
                 "cfda 64 128",
@@ -89223,60 +89229,38 @@
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
-            "identifier": "VA-VBA-USASPENDING132013-057",
-            "description": "<p>USA Spending- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects- March 2013.</p>",
-            "title": "USA Spending file- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects 03/2014-  CFDA 64.128",
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
+            "title": "USA Spending file- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects 03/2014-  CFDA 64.128"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xr5w-fet9",
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
-            "identifier": "e0955918-1281-41be-9a2e-9151b41ddfd1",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Oklahoma FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89284,37 +89268,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "e0955918-1281-41be-9a2e-9151b41ddfd1",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xr5w-fet9",
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
+            "title": "State Summary Oklahoma FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xts3-vap3",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2023-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
-            "keyword": [
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
-            "identifier": "https://www.data.va.gov/api/views/xts3-vap3",
+            "dataQuality": true,
             "description": "This dataset provides within-arm results for dichotomous outcomes: loss of diagnosis and clinically meaningful response. Included is information on how loss of diagnosis and clinically meaningful response were defined as well as the percent of participants who achieved loss of PTSD diagnosis/clinically meaningful response Each treatment arm is presented on its own row. There are also separate rows for studies with more than one measure, time point and analysis type or when there is more than one definition of diagnostic change or clinically meaningful change.",
-            "title": "PTSD Dichotomous Outcomes Within Arms",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89322,69 +89307,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xts3-vap3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xts3-vap3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xts3-vap3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/xts3-vap3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xts3-vap3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xts3-vap3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xts3-vap3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xts3-vap3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xts3-vap3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/xts3-vap3",
+            "issued": "2023-10-31",
+            "keyword": [
+                "ptsd-repository"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xts3-vap3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-09-04",
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
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "PTSD Dichotomous Outcomes Within Arms"
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
-            "identifier": "VA-VBA-ABR2012-002",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Age of Surviving Spouses Who Began Receiving DIC Benefits During FY2012-ABR2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89392,29 +89372,61 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-002",
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
+            "title": "Age of Surviving Spouses Who Began Receiving DIC Benefits During FY2012-ABR2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xxvt-n865",
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
+            "description": "<p>Adjusted mortality rate for three defined populations: Pneumonia, Congestive Heart Failure, and Acute Myocardial Infarction. 30d unadjusted readmission rates: all cause and Congestive Heart Failure. Surgical morbidity and mortality.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset6_Morbidity_Mortality.xml",
+                    "mediaType": "application/xml",
+                    "title": "Morbidity and Mortality"
+                }
             ],
+            "identifier": "VA-VHA-OIA-042",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -89437,71 +89449,41 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/xxvt-n865",
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
-            "identifier": "VA-VHA-OIA-042",
-            "description": "<p>Adjusted mortality rate for three defined populations: Pneumonia, Congestive Heart Failure, and Acute Myocardial Infarction. 30d unadjusted readmission rates: all cause and Congestive Heart Failure. Surgical morbidity and mortality.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Morbidity and Mortality",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset6_Morbidity_Mortality.xml",
-                    "mediaType": "application/xml",
-                    "title": "Morbidity and Mortality"
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
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Morbidity and Mortality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/xykt-5dut",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-24",
-            "keyword": [
-                "gender",
-                "take-up rate",
-                "use",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/xykt-5dut",
+            "dataQuality": true,
             "description": "Take-up rate within 2 fiscal years after separation from military service by race/ethnicity and gender.",
-            "title": "Take-up Rate by Race/Etnicity and Gender",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89509,59 +89491,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xykt-5dut/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xykt-5dut/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xykt-5dut/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/xykt-5dut/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xykt-5dut/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xykt-5dut/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/xykt-5dut/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/xykt-5dut/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/xykt-5dut/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/xykt-5dut",
+            "issued": "2021-02-19",
+            "keyword": [
+                "gender",
+                "take-up rate",
+                "use",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/xykt-5dut",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2021-03-24",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Take-up Rate by Race/Etnicity and Gender"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y2ct-dtid",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
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
-            "identifier": "VA-OM-OM-111",
             "description": "<p>FY 2003 Franchise Fund Annual Report Highlights</p>",
-            "title": "FY 2003 Franchise Fund Annual Report Highlights",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89570,76 +89552,70 @@
                     "title": "FY 2003 Franchise Fund Annual Report Highlights"
                 }
             ],
+            "identifier": "VA-OM-OM-111",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund"
+            ],
+            "landingPage": "https://www.data.va.gov/d/y2ct-dtid",
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
+            "title": "FY 2003 Franchise Fund Annual Report Highlights"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/y2eh-9yiu",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Washington FY2023",
+            "identifier": "https://www.data.va.gov/api/views/y2eh-9yiu",
             "issued": "2024-06-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "washington"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/y2eh-9yiu",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/y2eh-9yiu",
-            "description": "NCVAS State Summary Washington FY2023",
-            "title": "NCVAS State Summary Washington FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Washington FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y326-jukp",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2024-03-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-15",
-            "keyword": [
-                "compensation benefits",
-                "fy 2022",
-                "fy 2023",
-                "fy22",
-                "fy23",
-                "period of service",
-                "pos",
-                "state of residence",
-                "veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/y326-jukp",
             "description": "1. This provides a count of Veterans who are on the rolls for Compensation Service benefits by Veteran period of service and the state or country of residence for theyears identified.\n2. See VBA's Annual Benefits Report for additional information: www.benefits.va.gov/REPORTS/abr/\n3. To protect Veteran privacy any counts consisting of fewer than ten Veterans are not included.",
-            "title": "Veterans Receiving Compensation Service Benefits On the Rolls by Period of Service and Residence FY22 and FY23",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89647,39 +89623,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/y326-jukp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y326-jukp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y326-jukp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/y326-jukp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y326-jukp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y326-jukp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/y326-jukp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y326-jukp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y326-jukp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/y326-jukp",
+            "issued": "2024-03-08",
+            "keyword": [
+                "compensation benefits",
+                "fy 2022",
+                "fy 2023",
+                "fy22",
+                "fy23",
+                "period of service",
+                "pos",
+                "state of residence",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/y326-jukp",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-03-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Receiving Compensation Service Benefits On the Rolls by Period of Service and Residence FY22 and FY23"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y38q-zpnj",
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
+            "description": "Learn about studies of trauma-focused psychotherapies, the most effective approach to treating PTSD, found in the PTSD-Repository.",
+            "identifier": "https://www.data.va.gov/api/views/y38q-zpnj",
             "issued": "2021-05-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
             "keyword": [
                 "cpt",
                 "emdr",
@@ -89688,56 +89692,32 @@
                 "ptsd-repository",
                 "trauma-focused"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for PTSD",
-                "hasEmail": "mailto:ncptsd@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/y38q-zpnj",
+            "modified": "2024-09-04",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for PTSD"
             },
-            "identifier": "https://www.data.va.gov/api/views/y38q-zpnj",
-            "description": "Learn about studies of trauma-focused psychotherapies, the most effective approach to treating PTSD, found in the PTSD-Repository.",
-            "title": "Trauma-Focused Psychotherapy for PTSD",
-            "programCode": [
-                "029:000"
-            ],
-            "accrualPeriodicity": "R/P1Y"
+            "rights": "All data is within the public domain and is currently available for download.",
+            "title": "Trauma-Focused Psychotherapy for PTSD"
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
-            "identifier": "VA-VBA-ABR2012-004",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Age of Veterans Who Began Receiving Service Connected Compensation During FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89745,66 +89725,99 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-004",
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
+            "title": "Age of Veterans Who Began Receiving Service Connected Compensation During FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/y3hn-h8hq",
             "bureauCode": [
                 "029:00"
             ],
-            "rights": "Content is for internal Board use and is subject to change without notice in the Federal Register.  If made public the danger is that reviewers will possibly rely on outdated guidance.  Memoranda can be requested under the Freedom of Information Act.",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1991-01-01T05:00:00Z/2011-12-31T05:00:00Z",
-            "modified": "2020-12-01",
-            "keyword": [
-                "chairman s memoranda"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Margaret L. Peak",
                 "hasEmail": "mailto:margaret.peak@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-BVA-BVA-002",
+            "dataQuality": true,
             "description": "<p>Internal guidance on matters of BVA policy and practice</p>",
-            "title": "Board of Veterans' Appeals Chairman's Memoranda",
+            "identifier": "VA-BVA-BVA-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "chairman s memoranda"
+            ],
+            "landingPage": "https://www.data.va.gov/d/y3hn-h8hq",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:082"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Content is for internal Board use and is subject to change without notice in the Federal Register.  If made public the danger is that reviewers will possibly rely on outdated guidance.  Memoranda can be requested under the Freedom of Information Act.",
+            "temporal": "1991-01-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Board of Veterans' Appeals Chairman's Memoranda"
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
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/GDX/GDX_FY11.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-037",
             "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -89818,97 +89831,67 @@
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
-            "identifier": "VA-OEI-OEI-037",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2011",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/GDX/GDX_FY11.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/y4gk-3i96",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Louisiana FY2023",
+            "identifier": "https://www.data.va.gov/api/views/y4gk-3i96",
             "issued": "2024-06-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fy2024",
                 "louisiana",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/y4gk-3i96",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/y4gk-3i96",
-            "description": "NCVAS State Summary Louisiana FY2023",
-            "title": "NCVAS State Summary Louisiana FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Louisiana FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y5i7-75gp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-12-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
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
-            "identifier": "VA-OM-OM-120",
             "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT DEC 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89916,42 +89899,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-120",
+            "issued": "2017-07-26",
+            "keyword": [
+                "establishments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/y5i7-75gp",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
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
+            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT DEC 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/webservices/email/documentation/utilities.cfm",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "email",
-                "public consumption",
-                "utilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Reid",
                 "hasEmail": "mailto:vawebservices@med.va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-WSG-04",
             "description": "<p>This dataset offers a high-level look at the web service and the methods it has to offer for public consumption.</p>",
-            "title": "Email Utilities",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89960,23 +89942,54 @@
                     "title": "Email Utilities"
                 }
             ],
+            "identifier": "VA-OIT-WSG-04",
+            "issued": "2017-07-26",
+            "keyword": [
+                "email",
+                "public consumption",
+                "utilities"
+            ],
+            "landingPage": "https://www.va.gov/webservices/email/documentation/utilities.cfm",
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
+            "title": "Email Utilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Rita Grewal",
+                "hasEmail": "mailto:Rita.Grewal@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This is a monthly report that the VA Office of Information Technology provides to congress about data incidents that took place during the month (June 2014).  The report contains details about and total numbers of mis-handling incidents;  mis-mailed incidents; mis-mailed CMOP incidents; IT equipment inventory incidents; missing stolen PC incidents; missing/stolen laptop incident; lost blackberry incidents;  and lost non-blackberry mobile devices (tablets, iPhones, androids, etc.) incidents.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/ABOUT_VA/docs/monthly_rfc_jun2014.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-20",
             "issued": "2017-07-26",
-            "temporal": "2014-06-02T04:00:00Z/2014-06-29T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "blackberry",
                 "congress",
@@ -90000,93 +90013,63 @@
                 "va",
                 "va-nsoc"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Rita Grewal",
-                "hasEmail": "mailto:Rita.Grewal@va.gov"
-            },
+            "landingPage": "https://www.va.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:080"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OIT-ITIS-20",
-            "description": "<p>This is a monthly report that the VA Office of Information Technology provides to congress about data incidents that took place during the month (June 2014).  The report contains details about and total numbers of mis-handling incidents;  mis-mailed incidents; mis-mailed CMOP incidents; IT equipment inventory incidents; missing stolen PC incidents; missing/stolen laptop incident; lost blackberry incidents;  and lost non-blackberry mobile devices (tablets, iPhones, androids, etc.) incidents.</p>",
-            "title": "Department of Veterans Affairs - Monthly Report to Congress of Data Incidents (June 2014)",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/ABOUT_VA/docs/monthly_rfc_jun2014.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-06-02T04:00:00Z/2014-06-29T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs - Monthly Report to Congress of Data Incidents (June 2014)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y6if-ynpq",
-            "issued": "2023-06-28",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Indiana FY2021",
+            "identifier": "https://www.data.va.gov/api/views/y6if-ynpq",
+            "issued": "2023-06-28",
             "keyword": [
                 "fy2021 data",
                 "indiana",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/y6if-ynpq",
+            "landingPage": "https://www.data.va.gov/d/y6if-ynpq",
+            "modified": "2024-06-02",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Indiana FY2021",
             "title": "NCVAS State Summary Indiana FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y6jj-gsxt",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-10-04",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-04",
-            "keyword": [
-                "percent change by state",
-                "veteran population"
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
-            "identifier": "https://www.data.va.gov/api/views/y6jj-gsxt",
             "description": "The Department of Veterans Affairs provides official estimates and projections of the Veteran population using the Veteran Population Projection Model (VetPop). Based on the available information through September 30, 2020, the latest model VetPop2020 projected a steady decrease in the Veteran population over the next 30 years. The \u201cPercent Change in Veteran Population\u201d data table shows the change in the Veteran population from 2000 to 2022 by state. During this period, the average decrease in the Veteran population is 30% at the state level.",
-            "title": "Percent Change in Veteran Population by State from 2000 to 2022",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90094,57 +90077,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/y6jj-gsxt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y6jj-gsxt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y6jj-gsxt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/y6jj-gsxt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y6jj-gsxt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y6jj-gsxt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/y6jj-gsxt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y6jj-gsxt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y6jj-gsxt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/y6jj-gsxt",
+            "issued": "2022-10-04",
+            "keyword": [
+                "percent change by state",
+                "veteran population"
+            ],
+            "landingPage": "https://www.data.va.gov/d/y6jj-gsxt",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-10-04",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Percent Change in Veteran Population by State from 2000 to 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y6q9-ska6",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-08-15",
-            "@type": "dcat:Dataset",
-            "modified": "2020-09-16",
-            "keyword": [
-                "veterans",
-                "vietnam"
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
-            "identifier": "00902738-f6f0-4fe7-8aa5-ed697c66b9a5",
+            "dataQuality": true,
             "description": "<p>The Profile of Vietnam War Veterans uses the 2015 ACS to provide a view into the demographic characteristics and socioeconomic conditions of the Vietnam War Veteran cohort.</p>",
-            "title": "Profile of Vietnam War Veterans (2015).",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90153,19 +90137,47 @@
                     "title": "Profile of Vietnam War Veterans: 2015"
                 }
             ],
+            "identifier": "00902738-f6f0-4fe7-8aa5-ed697c66b9a5",
+            "issued": "2017-08-15",
+            "keyword": [
+                "veterans",
+                "vietnam"
+            ],
+            "landingPage": "https://www.data.va.gov/d/y6q9-ska6",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-09-16",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Profile of Vietnam War Veterans (2015)."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y7hu-8w78",
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
+            "description": "VA Community Care Comparison or VAC3 is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.  This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality. VAC3 data tables are updated every quarter.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/y7hu-8w78/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/y7hu-8w78",
             "issued": "2024-05-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-10-01/2024-03-31",
-            "modified": "2024-10-01",
             "keyword": [
                 "2024",
                 "fy2024",
@@ -90187,71 +90199,40 @@
                 "veteran",
                 "wntbva"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHASailOperations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/y7hu-8w78",
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
-            "identifier": "https://www.data.va.gov/api/views/y7hu-8w78",
-            "description": "VA Community Care Comparison or VAC3 is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.  This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality. VAC3 data tables are updated every quarter.",
-            "title": "VA Community Care Comparison (VAC3) - FY2024 All Facilities",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/y7hu-8w78/application/x-zip-compressed",
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
+            "title": "VA Community Care Comparison (VAC3) - FY2024 All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-04-01T04:00:00Z/2017-07-27T00:14:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 104",
-                "compensation and pension",
-                "non service connected disability",
-                "usa spending"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Monica Reyes",
                 "hasEmail": "mailto:monica.reyes@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-USASPENDING042014-058",
+            "dataQuality": true,
             "description": "<p>USA Spending- Non Service Connected Disability- April 2013.</p>",
-            "title": "USA Spending file- Compensation and Pension-  CFDA 64.104- April 2014",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90260,26 +90241,57 @@
                     "title": "USA Spending file- Compensation and Pension- CFDA 64.104- April 2014"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-USASPENDING042014-058",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cfda 64 104",
+                "compensation and pension",
+                "non service connected disability",
+                "usa spending"
+            ],
+            "landingPage": "https://www.usaspending.gov",
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
+            "temporal": "2014-04-01T04:00:00Z/2017-07-27T00:14:00Z",
             "theme": [
                 "USA Spending"
-            ]
+            ],
+            "title": "USA Spending file- Compensation and Pension-  CFDA 64.104- April 2014"
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
-            "temporal": "2015-07-15T04:00:00Z/2015-07-15T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_PendingAccess_20150715RptDate_Final.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 July 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-420",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -90293,53 +90305,54 @@
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
-            "identifier": "VA-VHA-OIA-420",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 July 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_PendingAccess_20150715RptDate_Final.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 July 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-07-15T04:00:00Z/2015-07-15T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 July 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ptsd.va.gov/about/divisions/evaluation",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.data.va.gov/dataset/va-ptsd-veteran-patient-statistics-2014/resource/e7ecb39c-6a66-4e1e-b7e6-063f2934dadb",
+            "description": "<p>National-level, VISN-level, and/or VAMC-level statistics on the numbers and percentages of users of VHA care form the Northeast Program Evaluation Center (NEPEC).  Some datasets focus on PTSD others on mental health.  There is no record-level data.  Information is for fiscal year 2014.  <b> This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/y8p8-zp6j/text/plain",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "VA-VHA-10N-009",
+            "isPartOf": "VA-VHA-10N-014",
             "issued": "2017-07-26",
-            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-29",
             "keyword": [
                 "2014",
                 "disorder",
@@ -90354,70 +90367,38 @@
                 "veteran",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.ptsd.va.gov/about/divisions/evaluation",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-06-29",
+            "programCode": [
+                "029:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-10N-009",
-            "description": "<p>National-level, VISN-level, and/or VAMC-level statistics on the numbers and percentages of users of VHA care form the Northeast Program Evaluation Center (NEPEC).  Some datasets focus on PTSD others on mental health.  There is no record-level data.  Information is for fiscal year 2014.  <b> This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>",
-            "title": "VA PTSD Veteran Patient Statistics - 2014",
-            "isPartOf": "VA-VHA-10N-014",
-            "programCode": [
-                "029:042"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/y8p8-zp6j/text/plain",
-                    "mediaType": "text/plain"
-                }
-            ],
-            "describedBy": "https://www.data.va.gov/dataset/va-ptsd-veteran-patient-statistics-2014/resource/e7ecb39c-6a66-4e1e-b7e6-063f2934dadb",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "PTSD",
                 "Mental Health"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA PTSD Veteran Patient Statistics - 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y94k-kvst",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-18",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-23",
-            "keyword": [
-                "employment program",
-                "veteran",
-                "veteran benefits",
-                "vocational rehabilitation"
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
-            "identifier": "https://www.data.va.gov/api/views/y94k-kvst",
             "description": "Vocational Rehabilitation: All Veterans who participated in various stages of the Vocational Rehabilitation and Employment program were included. Veterans Benefits Administration (VBA) provides Vocational Rehabilitation/employment services.",
-            "title": "Veterans who participated in Vocational Rehabilitation & Employment Programs",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90425,62 +90406,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/y94k-kvst/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y94k-kvst/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y94k-kvst/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/y94k-kvst/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y94k-kvst/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y94k-kvst/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/y94k-kvst/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y94k-kvst/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y94k-kvst/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "State",
-            "license": "https://www.usa.gov/government-works",
+            "identifier": "https://www.data.va.gov/api/views/y94k-kvst",
+            "issued": "2021-02-18",
+            "keyword": [
+                "employment program",
+                "veteran",
+                "veteran benefits",
+                "vocational rehabilitation"
+            ],
+            "landingPage": "https://www.data.va.gov/d/y94k-kvst",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2021-03-23",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "spatial": "State",
+            "title": "Veterans who participated in Vocational Rehabilitation & Employment Programs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y9f2-6a5w",
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
-            "identifier": "https://www.data.va.gov/api/views/y9f2-6a5w",
-            "description": "<p>These spreadsheets contain the percent of Veteran farmers and dairymen  by county for the state of California.</p>",
-            "title": "Veteran Farmers by County",
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
@@ -90488,65 +90473,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/y9f2-6a5w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y9f2-6a5w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y9f2-6a5w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/y9f2-6a5w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y9f2-6a5w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y9f2-6a5w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/y9f2-6a5w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/y9f2-6a5w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/y9f2-6a5w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/data/VAOpenDataMigration2019/Data-Dictionary-Apps-for-Ag.pdf",
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/y9f2-6a5w",
+            "isPartOf": "64971372-40a2-4207-937c-892283f391ba",
+            "issued": "2017-07-07",
+            "keyword": [
+                "veterans farmer"
+            ],
+            "landingPage": "https://www.data.va.gov/d/y9f2-6a5w",
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
+            "title": "Veteran Farmers by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y9g9-wju5",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "pow",
-                "purple heart",
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
-            "identifier": "3eeffbb0-f1d0-4863-a2ba-afd358ae7a0f",
+            "dataQuality": true,
             "description": "<p>To show count of Medal of Honor, Purple Heart, or POW recipients by county (Living only)</p>",
-            "title": "Special Medal of Honor Recipients (2017) Living Only",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90554,39 +90537,45 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "3eeffbb0-f1d0-4863-a2ba-afd358ae7a0f",
+            "issued": "2019-04-24",
+            "keyword": [
+                "pow",
+                "purple heart",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/y9g9-wju5",
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
+            "title": "Special Medal of Honor Recipients (2017) Living Only"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y9gb-p7uj",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2023-09-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-12",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA National Center for Organization Development (NCOD)",
                 "hasEmail": "mailto:vhancod@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/y9gb-p7uj",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) items also on Federal Employee Viewpoint Survey, reported as percents as required per Federal statute.",
-            "title": "AES 2023 FEVS Percents",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90594,20 +90583,36 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/y9gb-p7uj",
+            "issued": "2023-09-12",
+            "landingPage": "https://www.data.va.gov/d/y9gb-p7uj",
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
+            "title": "AES 2023 FEVS Percents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://veteran.mobilehealth.va.gov/AHBurnPitRegistry/#page/home",
+            "accrualPeriodicity": "R/P1D",
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
+            "description": "<p>The VA's Veteran Health Administration, in support of PL 112 260 established an Airborne Hazards and Open Burn Pit Registry to study the potential exposure of concern that may result in long-term health impacts to Veterans.</p>",
+            "identifier": "VA-VHA-EHP-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "ahobpr",
                 "airborne",
@@ -90621,60 +90626,39 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://veteran.mobilehealth.va.gov/AHBurnPitRegistry/#page/home",
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
-            "identifier": "VA-VHA-EHP-001",
-            "description": "<p>The VA's Veteran Health Administration, in support of PL 112 260 established an Airborne Hazards and Open Burn Pit Registry to study the potential exposure of concern that may result in long-term health impacts to Veterans.</p>",
-            "title": "Airborne Hazard and Open Burn Pit Registry (AHOBPR)",
-            "programCode": [
-                "029:048"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1D",
             "theme": [
                 "Research of potential impact of exposure to Airborne Hazards and Open Burn Pits."
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Airborne Hazard and Open Burn Pit Registry (AHOBPR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y9tp-xtq8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "board of veterans appeals",
-                "demographics"
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
-            "identifier": "02d9636a-80a0-4a93-ba48-927f90b437a1",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary New Hampshire FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90682,79 +90666,108 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "02d9636a-80a0-4a93-ba48-927f90b437a1",
+            "issued": "2018-10-30",
+            "keyword": [
+                "board of veterans appeals",
+                "demographics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/y9tp-xtq8",
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
+            "title": "State Summary New Hampshire FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/y9vr-w4nk",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Idaho FY2023",
+            "identifier": "https://www.data.va.gov/api/views/y9vr-w4nk",
             "issued": "2024-05-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fy2024 data",
                 "id",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/y9vr-w4nk",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/y9vr-w4nk",
-            "description": "NCVAS State Summary Idaho FY2023",
-            "title": "NCVAS State Summary Idaho FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Idaho FY2023"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y9wt-vgy5",
-            "issued": "2023-06-15",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-16",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Arizona FY2021",
+            "identifier": "https://www.data.va.gov/api/views/y9wt-vgy5",
+            "issued": "2023-06-15",
             "keyword": [
                 "arizona",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/y9wt-vgy5",
+            "landingPage": "https://www.data.va.gov/d/y9wt-vgy5",
+            "modified": "2024-05-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Arizona FY2021",
             "title": "NCVAS State Summary Arizona FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/y9x8-349i",
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
+                    "downloadURL": "https://www.data.va.gov/download/y9x8-349i/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/y9x8-349i",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2021-06-24",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-10-01/2021-9-30",
-            "modified": "2022-01-10",
             "keyword": [
                 "2021",
                 "analytics",
@@ -90777,50 +90790,42 @@
                 "sail",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHASailOperations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/y9x8-349i",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-01-10",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/y9x8-349i",
-            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).",
-            "title": "SAIL FY2021 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/y9x8-349i/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2020-10-01/2021-9-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAIL FY2021 Hospital Performance - All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nvsbe.com/why-attend/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Armando.Herrera",
+                "hasEmail": "mailto:Armando.Herrera@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>National Veterans Small Business Engagement website - why attend webpage</p>",
+            "identifier": "VA-00SB-NVSBE0002",
             "issued": "2017-07-26",
-            "temporal": "2014-06-11T04:00:00Z/2015-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "conference",
                 "engagement",
@@ -90832,46 +90837,53 @@
                 "vets",
                 "why attend"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Armando.Herrera",
-                "hasEmail": "mailto:Armando.Herrera@va.gov"
-            },
+            "landingPage": "http://www.nvsbe.com/why-attend/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:081"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-00SB-NVSBE0002",
-            "description": "<p>National Veterans Small Business Engagement website - why attend webpage</p>",
-            "title": "NVSBE Website - Why Attend",
-            "programCode": [
-                "029:081"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-06-11T04:00:00Z/2015-04-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NVSBE Website - Why Attend"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN3FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 3 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-077",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -90887,71 +90899,43 @@
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
-            "identifier": "VA-VHA-OIA-077",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 3",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN3FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 3 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ybdi-5ur2",
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
-            "identifier": "e36725f7-8a76-4c8a-a754-12ea8b5c07ec",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Colorado FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90959,37 +90943,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "e36725f7-8a76-4c8a-a754-12ea8b5c07ec",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ybdi-5ur2",
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
+            "title": "State Summary Colorado FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ybfs-xp53",
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
-            "identifier": "https://www.data.va.gov/api/views/ybfs-xp53",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide direct loans to certain veterans who are, or whose spouses are, Native Americans for the purchase or construction of homes on trust lands. Veterans who are, or whose spouses are, recognized by a Federally Recognized Tribal Government as a Native American and who: (a) Served on active duty on or after September 16, 1940, and were discharged or released under conditions other than dishonorable. If service was any time during World War II, the Korean Conflict, the Vietnam-era, or the Persian Gulf War, then the Native American Veteran must have served on active duty for 90 days or more; peacetime service only must have served a minimum of 181 days continuous active duty. If separated from enlisted service which began after September 7, 1980, or service as an officer which began after October 16, 1981, a veteran must also have served at least 24 months of continuous active duty or the full period for which called or ordered to active duty. Veterans of such recent service may qualify with less service time if they have a compensable service-connected disability or were discharged after at least 181 days, under the authority of 10 U.S.C 1171 or 1173. (b) Any veteran in the above classes with less service but discharged with a service-connected disability. (c) If acknowledged as a Native American by a Federally Recognized Tribal Government, unmarried surviving spouses of otherwise eligible veterans who died in service or whose deaths were attributable to service-connected disabilities and spouses of members of the Armed Forces serving on active duty, who are listed as missing in action, or as prisoners of war and who have been so listed 90 days or more. (d) Members of the Selected Reservists who ae, or whose spouses ae, recognized by a Federally Recognized Tribal Government as Native Americans and who are not otherwise eligible for home loan benefits and who have completed a total of 6 years in the Selected Reserves followed by an honorable discharge, placement on the retired list, or continued service.</p>",
-            "title": "USA SPENDING LGY B126 NATIVE AMERICAN VETERAN DIRECT LOAN PROGRAM OCT2018",
-            "isPartOf": "e30045ea-2153-40e3-91bc-23c0014ae69c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90997,62 +90981,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ybfs-xp53/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ybfs-xp53/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ybfs-xp53/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ybfs-xp53/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ybfs-xp53/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ybfs-xp53/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ybfs-xp53/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ybfs-xp53/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ybfs-xp53/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/ybfs-xp53",
+            "isPartOf": "e30045ea-2153-40e3-91bc-23c0014ae69c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 126"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ybfs-xp53",
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
+            "title": "USA SPENDING LGY B126 NATIVE AMERICAN VETERAN DIRECT LOAN PROGRAM OCT2018"
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
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "budget",
-                "fy2010"
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
-            "identifier": "VA-OM-OM-029",
+            "dataQuality": true,
             "description": "<p>FY2010 VA Budget Submission.</p>",
-            "title": "FY2010 VA Budget Submission",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91061,48 +91045,45 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-029",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "fy2010"
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
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY2010 VA Budget Submission"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/yd5e-48pf",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2022-09-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
-            "keyword": [
-                "demographic",
-                "ncptsd",
-                "population",
-                "population characteristics",
-                "ptsd"
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
-            "identifier": "https://www.data.va.gov/api/views/yd5e-48pf",
+            "dataQuality": true,
             "description": "The Sample Characteristics dataset includes information on the participants who are included in the studies. This information is provided at the study level\u2014meaning, data are not broken down into the specific treatment arms such as the intervention or control groups. Use this dataset if you want to learn more about the number of participants in the study; inclusion and exclusion criteria related to substance use and suicidality; baseline clinical characteristics such as PTSD severity, trauma type, military status, and comorbidities; and, basic demographic information such as age, gender or race for the sample as a whole (not individual participants). Visualizations made from this dataset will be based on the 496 RCTs included in the PTSD-Repository. Values reported as \"NA\" or not reported \"NR\" by the study are null values (empty cells). Data is at the study level.",
-            "title": "Sample Characteristics",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91110,64 +91091,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/yd5e-48pf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/yd5e-48pf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/yd5e-48pf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/yd5e-48pf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/yd5e-48pf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/yd5e-48pf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/yd5e-48pf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/yd5e-48pf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/yd5e-48pf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/yd5e-48pf",
+            "issued": "2022-09-28",
+            "keyword": [
+                "demographic",
+                "ncptsd",
+                "population",
+                "population characteristics",
+                "ptsd"
+            ],
+            "landingPage": "https://www.data.va.gov/d/yd5e-48pf",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-09-04",
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
+            "title": "Sample Characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/yf8u-xhuu",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-10-19",
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
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/yf8u-xhuu",
             "description": "Rate of Use by Race/Ethnicity, any VA program - FY2018. Data underlying the sixth figure of Part 1 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 7, Participation by Race/Ethnicity - FY2018",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91175,62 +91156,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/yf8u-xhuu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/yf8u-xhuu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/yf8u-xhuu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/yf8u-xhuu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/yf8u-xhuu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/yf8u-xhuu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/yf8u-xhuu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/yf8u-xhuu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/yf8u-xhuu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/yf8u-xhuu",
+            "issued": "2020-10-19",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/yf8u-xhuu",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 7, Participation by Race/Ethnicity - FY2018"
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
-                "lgy",
-                "loan guarantee benefits fy12",
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
-            "identifier": "VA-VBA-ABR2012-048",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Percent of Loans Guaranteed by Age by Fiscal Year",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91238,51 +91218,74 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-048",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "lgy",
+                "loan guarantee benefits fy12",
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
+            "title": "Percent of Loans Guaranteed by Age by Fiscal Year"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ygbk-evf6",
-            "issued": "2023-07-14",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-14",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary New Hampshire FY2021",
+            "identifier": "https://www.data.va.gov/api/views/ygbk-evf6",
+            "issued": "2023-07-14",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "new hampshire"
             ],
-            "identifier": "https://www.data.va.gov/api/views/ygbk-evf6",
+            "landingPage": "https://www.data.va.gov/d/ygbk-evf6",
+            "modified": "2024-06-14",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary New Hampshire FY2021",
             "title": "NCVAS State Summary New Hampshire FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/ygdi-ec2z",
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
+            "description": "<p>The Report of VA Medical Training Programs Database is used to track medical center health services trainees and VA physicians serving as faculty. The database also tracks the number of U.S. and international medical residents on-duty at a Veterans Affairs Medical Center (VAMC). Information in the database comes from all VAMCs that have residency programs. The Office of Academic Affiliations distributes worksheets and memos to participating VAMCs annually. VAMC personnel enter the information electronically into the database located at the Academic Information Management Center (AIMC) in St. Louis, Missouri. The main user of this database is the Office of Academic Affiliations which uses the reports from the system to assist in its decision making.</p>",
+            "identifier": "VA-VHA-OAA-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1996-01-01T05:00:00Z/2005-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "academic",
                 "affiliation",
@@ -91293,60 +91296,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/ygdi-ec2z",
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
-            "identifier": "VA-VHA-OAA-002",
-            "description": "<p>The Report of VA Medical Training Programs Database is used to track medical center health services trainees and VA physicians serving as faculty. The database also tracks the number of U.S. and international medical residents on-duty at a Veterans Affairs Medical Center (VAMC). Information in the database comes from all VAMCs that have residency programs. The Office of Academic Affiliations distributes worksheets and memos to participating VAMCs annually. VAMC personnel enter the information electronically into the database located at the Academic Information Management Center (AIMC) in St. Louis, Missouri. The main user of this database is the Office of Academic Affiliations which uses the reports from the system to assist in its decision making.</p>",
-            "title": "Report of VA Medical Training Programs",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1996-01-01T05:00:00Z/2005-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Report of VA Medical Training Programs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/yhcv-v3uc",
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
-            "identifier": "b82b6920-05ef-4a6d-a9a5-8322259fda5c",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Arkansas FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91354,48 +91338,45 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "b82b6920-05ef-4a6d-a9a5-8322259fda5c",
+            "issued": "2018-10-29",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/yhcv-v3uc",
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
@@ -91403,50 +91384,49 @@
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
-                "lgy",
-                "loan guarantee benefits fy12",
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
-            "identifier": "VA-VBA-ABR2012-045",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Loans Guaranteed by Race During Fiscal Year 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91454,49 +91434,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-045",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "lgy",
+                "loan guarantee benefits fy12",
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
+            "title": "Loans Guaranteed by Race During Fiscal Year 2012"
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
-            "identifier": "VA-VBA-ABR2012-089",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Hawaii-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91504,44 +91484,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-089",
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
+            "title": "Hawaii-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/yip7-ky8f",
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
-            "identifier": "b4e8a7b5-15b0-4510-9a5f-0c2b0dcd1ba8",
+            "dataQuality": true,
             "description": "<p>\u00a0The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.\u00a0</p>",
-            "title": "State Summary Hawaii FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91549,42 +91533,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "b4e8a7b5-15b0-4510-9a5f-0c2b0dcd1ba8",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/yip7-ky8f",
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
+            "title": "State Summary Hawaii FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/yj2w-nxxg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-09-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "women veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA Open Data",
                 "hasEmail": "mailto:OITopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/yj2w-nxxg",
             "description": "Number of female veterans, sorted by age, between 2010 and 2017",
-            "title": "Female Veterans by Age Group, 2010-2017",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91592,57 +91576,56 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/yj2w-nxxg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/yj2w-nxxg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/yj2w-nxxg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/yj2w-nxxg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/yj2w-nxxg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/yj2w-nxxg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/yj2w-nxxg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/yj2w-nxxg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/yj2w-nxxg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/yj2w-nxxg",
+            "issued": "2019-09-19",
+            "keyword": [
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/yj2w-nxxg",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Female Veterans by Age Group, 2010-2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/yj3w-msgp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "tennessee",
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
-            "identifier": "VA-OEI-OEI-129",
             "description": "<p>This is a summary of the programs and services provided by VA in Tennessee in fiscal year 2014.</p>",
-            "title": "State Summary:  Tennessee",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91651,74 +91634,74 @@
                     "title": "State Summary:  Tennessee"
                 }
             ],
+            "identifier": "VA-OEI-OEI-129",
+            "issued": "2017-07-26",
+            "keyword": [
+                "tennessee",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/yj3w-msgp",
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
+            "title": "State Summary:  Tennessee"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ym5g-jit9",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "maryland",
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
-            "identifier": "https://www.data.va.gov/api/views/ym5g-jit9",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Maryland",
+            "identifier": "https://www.data.va.gov/api/views/ym5g-jit9",
+            "issued": "2021-08-26",
+            "keyword": [
+                "maryland",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ym5g-jit9",
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
+            "title": "State Summaries_Maryland"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ymks-my9h",
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
-            "identifier": "OM-OM-165",
             "description": "<p>COIN report 022 April 2016</p>",
-            "title": "COIN 022 Apr 16",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91726,40 +91709,40 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-165",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ymks-my9h",
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
                 "finance"
-            ]
+            ],
+            "title": "COIN 022 Apr 16"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ynfx-tk97",
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
-            "identifier": "https://www.data.va.gov/api/views/ynfx-tk97",
-            "description": "All Survivors Pension Recipients by Veteran's Period of Service, FY2022. Pension is a needs-based benefit designed to provide certain wartime Veterans and their survivors with a minimum level of income that raises their standard of living.",
-            "title": "All Survivors Pension Recipients by Veteran's Period of Service, FY2022",
-            "programCode": [
-                "029:086"
-            ],
+            "dataQuality": true,
+            "description": "All Survivors Pension Recipients by Veteran's Period of Service, FY2022. Pension is a needs-based benefit designed to provide certain wartime Veterans and their survivors with a minimum level of income that raises their standard of living.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91767,41 +91750,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ynfx-tk97/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ynfx-tk97/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ynfx-tk97/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ynfx-tk97/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ynfx-tk97/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ynfx-tk97/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ynfx-tk97/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ynfx-tk97/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ynfx-tk97/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/ynfx-tk97",
+            "issued": "2023-03-21",
+            "keyword": [
+                "pension",
+                "veterans",
+                "veterans surviving spouses and children"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ynfx-tk97",
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
+            "title": "All Survivors Pension Recipients by Veteran's Period of Service, FY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/ynhd-fgt2",
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
+            "description": "<p>The Home Based Primary Care (HBPC) database receives and compiles data from local Hospital Based Home Care (HBHC) sanctioned programs at Veterans Affairs Medical Centers (VAMCs) that run home care programs under the Home Based Primary Care program. The primary purpose is to provide HBPC management with case mix, case load, and other performance information. The HBPC information system is referred to as HBC at the VA Austin Information Technology Center and as HBHC at the local level. The HBHC automated a paper-based system of reporting home care episodes. When an admission form is completed, an episode is opened and input into HBHC for a potential home care patient. The patient is evaluated and accepted to or rejected from the program. When a patient leaves the program for any reason an episode is closed and a discharge form completed and input into HBHC. HBHC runs a nightly extract of information within the Veterans Health Information Systems and Technology Architecture. Extractions include information on all Patient Care Encounters (PCEs) with the patient and home visits made by home care providers. Details of which provider(s) made the visit, the date, any diagnosis and any procedures performed are included. Each local application sends its data to the Austin HBC database on a monthly basis. A monthly report is prepared based on this information identifying the active cases at each VAMC. A more detailed quarterly report is produced that includes national comparisons among sites.</p>",
+            "identifier": "VA-VHA-PCS-009",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1983-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "care",
                 "case",
@@ -91813,113 +91816,126 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/ynhd-fgt2",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:058"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PCS-009",
-            "description": "<p>The Home Based Primary Care (HBPC) database receives and compiles data from local Hospital Based Home Care (HBHC) sanctioned programs at Veterans Affairs Medical Centers (VAMCs) that run home care programs under the Home Based Primary Care program. The primary purpose is to provide HBPC management with case mix, case load, and other performance information. The HBPC information system is referred to as HBC at the VA Austin Information Technology Center and as HBHC at the local level. The HBHC automated a paper-based system of reporting home care episodes. When an admission form is completed, an episode is opened and input into HBHC for a potential home care patient. The patient is evaluated and accepted to or rejected from the program. When a patient leaves the program for any reason an episode is closed and a discharge form completed and input into HBHC. HBHC runs a nightly extract of information within the Veterans Health Information Systems and Technology Architecture. Extractions include information on all Patient Care Encounters (PCEs) with the patient and home visits made by home care providers. Details of which provider(s) made the visit, the date, any diagnosis and any procedures performed are included. Each local application sends its data to the Austin HBC database on a monthly basis. A monthly report is prepared based on this information identifying the active cases at each VAMC. A more detailed quarterly report is produced that includes national comparisons among sites.</p>",
-            "title": "Home Based Primary Care (HBC)",
-            "programCode": [
-                "029:058"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1983-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Home Based Primary Care (HBC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/yp2b-3tsz",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-21",
-            "keyword": [
-                "new york",
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
-            "identifier": "https://www.data.va.gov/api/views/yp2b-3tsz",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_New York",
+            "identifier": "https://www.data.va.gov/api/views/yp2b-3tsz",
+            "issued": "2021-08-26",
+            "keyword": [
+                "new york",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/yp2b-3tsz",
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
+            "title": "State Summaries_New York"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://va.cficloud.com/",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Non-Public access level is warranted because of the contract and financial data aggreated in the system.  Knowledge of this information could possibly compromise contract negoiations for construction services.",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2009-01-01T05:00:00Z/2014-05-01T04:00:00Z",
-            "modified": "2024-08-26",
-            "keyword": [
-                "construction management",
-                "project management"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Gail Smith",
                 "hasEmail": "mailto:Gail.Smith3@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-CFM-Tririga-002",
+            "dataQuality": true,
             "description": "<p>The Paragon and Tririga Applications are project management programs utilized by CFM for construction programs.  The contents of the databases are a compiliation of the electronic contract management system(eCMS), the financial management system(FMS), and status information provided by CFM's engineering staff.  Due to the nature of the contract and financial management system information, the systems access is restricted to CFM personnel and select contractors working for CFM.  The reason for two project management programs is because Tririga is a replacement program for Paragon.  Once training has been completed and the Paragon data has been migrated to Tririga, Paragon use will be discontinued.  Paragon and Tririga are web based applications hosted by contractors outside of the VA intranet system.  Tririga will be the main construction management program as of June 2014.</p>",
-            "title": "Tririga",
+            "identifier": "VA-CFM-Tririga-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "construction management",
+                "project management"
+            ],
+            "landingPage": "https://va.cficloud.com/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
             "programCode": [
                 "029:090"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1D",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Non-Public access level is warranted because of the contract and financial data aggreated in the system.  Knowledge of this information could possibly compromise contract negoiations for construction services.",
+            "temporal": "2009-01-01T05:00:00Z/2014-05-01T04:00:00Z",
             "theme": [
                 "Construction Project Management"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tririga"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.pbm.va.gov/nationalformulary.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.pbm.va.gov/PBM/nationalformulary/NDFDataStructure.pdf",
+            "describedByType": "application/pdf",
+            "description": "<p>The VA National Drug File is a centrally maintained electronic drug list used by the VA hospitals and clinics. Facilities use the VA National Drug File to check drug interactions, to manage orders, and to send outpatient prescriptions to regional automated mail-out pharmacies.  The VA National Drug File includes information on clinical drugs, drug classes, ingredients and National Drug Code (NDC) Directory codes.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.pbm.va.gov/nationalformulary.asp",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "VA Product Name List"
+                }
+            ],
+            "identifier": "VA-VHA-PBM-007",
+            "isPartOf": "VA-VHA-PBM-008",
             "issued": "2017-07-26",
-            "temporal": "1998-10-01T04:00:00Z/2016-01-01T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "drug",
                 "drug class",
@@ -91931,103 +91947,70 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.pbm.va.gov/nationalformulary.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:047"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PBM-007",
-            "description": "<p>The VA National Drug File is a centrally maintained electronic drug list used by the VA hospitals and clinics. Facilities use the VA National Drug File to check drug interactions, to manage orders, and to send outpatient prescriptions to regional automated mail-out pharmacies.  The VA National Drug File includes information on clinical drugs, drug classes, ingredients and National Drug Code (NDC) Directory codes.</p>",
-            "title": "VA National Drug File",
-            "isPartOf": "VA-VHA-PBM-008",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "029:047"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.pbm.va.gov/nationalformulary.asp",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "VA Product Name List"
-                }
-            ],
-            "describedBy": "https://www.pbm.va.gov/PBM/nationalformulary/NDFDataStructure.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "1998-10-01T04:00:00Z/2016-01-01T05:00:00Z",
             "theme": [
                 "Pharmacy"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA National Drug File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "Department of Veterans Affairs"
             ],
-            "landingPage": "https://www.data.va.gov/d/yr7p-v5my",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Veterans Analysis and Statistics",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "This data story highlights results from the Veteran Population Projection Model 2023 (VetPop2023).",
+            "identifier": "https://www.data.va.gov/api/views/yr7p-v5my",
             "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-25",
             "keyword": [
                 "veteran population",
                 "veterans",
                 "vetpop",
                 "vetpop2023"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Veterans Analysis and Statistics",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/yr7p-v5my",
+            "modified": "2024-10-25",
+            "programCode": [
+                "Office of Enterprise Integration"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/yr7p-v5my",
-            "description": "This data story highlights results from the Veteran Population Projection Model 2023 (VetPop2023).",
-            "title": "VetPop2023 Data Story",
-            "programCode": [
-                "Office of Enterprise Integration"
-            ]
+            "title": "VetPop2023 Data Story"
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
-            "identifier": "VA-OM-OM-011",
+            "dataQuality": true,
             "description": "<p>2007 VA Performance and Accountability Report.</p>",
-            "title": "2007 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92036,51 +92019,48 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-011",
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
+            "temporal": "2007-01-01T05:00:00Z/2007-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2007 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/HEALTHPOLICYPLANNING/PAF.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "county",
-                "enrollee",
-                "fips",
-                "health",
-                "healthcare",
-                "state",
-                "veteran"
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
-            "identifier": "VA-VHA-OPP-001",
-            "description": "<p>The VA's Veteran Health Administration, in support of the Open Data Initiative, is providing the number of Veteran enrollees by state/county for fiscal year 2015.  For additional information about Veteran Priority Groups, see the data assets metadata.</p>",
-            "title": "FY2015 VHA Enrollees by County",
+            "dataQuality": true,
+            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/VAEnrolleesByCountyDataDictionary/master/VAEnrolleesByCountyDataDictionary.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:080"
-            ],
+            "description": "<p>The VA's Veteran Health Administration, in support of the Open Data Initiative, is providing the number of Veteran enrollees by state/county for fiscal year 2015.  For additional information about Veteran Priority Groups, see the data assets metadata.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92088,46 +92068,50 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/VAEnrolleesByCountyDataDictionary/master/VAEnrolleesByCountyDataDictionary.xlsx",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OPP-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "county",
+                "enrollee",
+                "fips",
+                "health",
+                "healthcare",
+                "state",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/HEALTHPOLICYPLANNING/PAF.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:080"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
             "theme": [
                 "Veteran Health Administration Enrollee by County"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY2015 VHA Enrollees by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ys4z-rqyp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-04-01T04:00:00Z/2013-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-01",
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
-            "identifier": "VA-OM-OM-083",
+            "dataQuality": true,
             "description": "<p>FY 2013 Third Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2013 Third Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92136,45 +92120,43 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-083",
+            "issued": "2017-07-26",
+            "keyword": [
+                "improper payments",
+                "overpayments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ys4z-rqyp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2022-11-01",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2013-04-01T04:00:00Z/2013-06-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2013 Third Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ytxn-wfc3",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-18",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-23",
-            "keyword": [
-                "education benefits",
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
-            "identifier": "https://www.data.va.gov/api/views/ytxn-wfc3",
             "description": "Education: All Veterans who received benefits for Chapter 30, 32, 33, 1606, and 1607 education programs were included. Veterans Benefits Administration (VBA) provides Education Assistance.",
-            "title": "Veterans who used GI Bill Education Benefits",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92182,61 +92164,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ytxn-wfc3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ytxn-wfc3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ytxn-wfc3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ytxn-wfc3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ytxn-wfc3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ytxn-wfc3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ytxn-wfc3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ytxn-wfc3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ytxn-wfc3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "State",
-            "license": "https://www.usa.gov/government-works",
+            "identifier": "https://www.data.va.gov/api/views/ytxn-wfc3",
+            "issued": "2021-02-18",
+            "keyword": [
+                "education benefits",
+                "veteran",
+                "veteran benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ytxn-wfc3",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2021-03-23",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "spatial": "State",
+            "title": "Veterans who used GI Bill Education Benefits"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/yvct-yuic",
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
-            "identifier": "c9d806c0-9b7e-4807-a24d-1912a7ae3cdf",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Ohio FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92244,22 +92228,50 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "c9d806c0-9b7e-4807-a24d-1912a7ae3cdf",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/yvct-yuic",
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
+            "title": "State Summary Ohio FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ywkf-kij4",
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
+            "description": "<p>Number of admissions by bed section, admissions per 1000 uniques, and average length of stay by bed sections. Total number of outpatient visits, number of unique patients and number of outpatient endoscopies.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset2_Hospital_Facility_Services.xml",
+                    "mediaType": "application/xml",
+                    "title": "Hospital and Facility Services"
+                }
             ],
+            "identifier": "VA-VHA-OIA-039",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -92282,40 +92294,28 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/ywkf-kij4",
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
-            "identifier": "VA-VHA-OIA-039",
-            "description": "<p>Number of admissions by bed section, admissions per 1000 uniques, and average length of stay by bed sections. Total number of outpatient visits, number of unique patients and number of outpatient endoscopies.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Hospital and Facility Services",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset2_Hospital_Facility_Services.xml",
-                    "mediaType": "application/xml",
-                    "title": "Hospital and Facility Services"
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
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Hospital and Facility Services"
         }
-    ]
+    ],
+    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
 }
```

