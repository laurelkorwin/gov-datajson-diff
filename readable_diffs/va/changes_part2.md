# Change History for va.json (Part 2)

### Changes from 31606f9 to dd2190f (Part 2/7)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAR2019"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6484-2sq8",
-            "issued": "2023-07-18",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-14",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary New Jersey FY2021",
+            "identifier": "https://www.data.va.gov/api/views/6484-2sq8",
+            "issued": "2023-07-18",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "new jersey"
             ],
-            "identifier": "https://www.data.va.gov/api/views/6484-2sq8",
+            "landingPage": "https://www.data.va.gov/d/6484-2sq8",
+            "modified": "2024-06-14",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary New Jersey FY2021",
             "title": "NCVAS State Summary New Jersey FY2021"
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
-            "temporal": "2014-01-01T05:00:00Z/2014-03-31T04:00:00Z",
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
-            "identifier": "VA-OM-OM-079",
+            "dataQuality": true,
             "description": "<p>FY 2014 Second Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2014 Second Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13743,43 +13727,43 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-079",
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
+            "temporal": "2014-01-01T05:00:00Z/2014-03-31T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2014 Second Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/65cr-ztpg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "nebraska"
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
-            "identifier": "VA-OEI-OEI-198",
             "description": "<p>This summary describes the programs and services VA provided in Nebraska in fiscal year 2015.</p>",
-            "title": "State Summary: Nebraska FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13788,23 +13772,52 @@
                     "title": "Nebraska"
                 }
             ],
+            "identifier": "VA-OEI-OEI-198",
+            "issued": "2017-07-26",
+            "keyword": [
+                "nebraska"
+            ],
+            "landingPage": "https://www.data.va.gov/d/65cr-ztpg",
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
+            "title": "State Summary: Nebraska FY15"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2011.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/va-fy11-final.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-03",
             "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2011",
                 "appeals",
@@ -13821,68 +13834,39 @@
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
-            "identifier": "VA-OIT-ITIS-03",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2011.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2011",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/va-fy11-final.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/66d3-mn9x",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "texas"
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
-            "identifier": "VA-OEI-OEI-215",
             "description": "<p>This summary describes the programs and services VA provided in  Texas in fiscal year 2015.</p>",
-            "title": "State Summary:  Texas FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13891,23 +13875,52 @@
                     "title": "Texas"
                 }
             ],
+            "identifier": "VA-OEI-OEI-215",
+            "issued": "2017-07-26",
+            "keyword": [
+                "texas"
+            ],
+            "landingPage": "https://www.data.va.gov/d/66d3-mn9x",
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
+            "title": "State Summary:  Texas FY15"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2007.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2007.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-07",
             "issued": "2017-07-26",
-            "temporal": "2006-10-01T04:00:00Z/2007-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2007",
                 "appeals",
@@ -13924,69 +13937,39 @@
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
-            "identifier": "VA-OIT-ITIS-07",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2007.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2007",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2007.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2006-10-01T04:00:00Z/2007-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/67gx-5e9i",
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
-            "identifier": "VA-OGC-039",
             "description": "<p>Osborn v. Nicholson 21 Vet. App. 223 (2007) - Effect on Existing General Counsel Opinions, Application to other Benefit Programs, and Applicability to Series HH U.S. Savings Bonds and Bonds Issued by Other Political Subdivisions - 38 U.S.C. \u00a7 1503(a)(6), 38 C.F.R. 21 3.272(e)</p>",
-            "title": "OGC Precedent Opinion 2-2010",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13995,41 +13978,42 @@
                     "title": "OGC Precedent Opinion 2-2010"
                 }
             ],
+            "identifier": "VA-OGC-039",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/67gx-5e9i",
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
+            "title": "OGC Precedent Opinion 2-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/683q-3f85",
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
-            "identifier": "6836af03-4278-4e2f-94bd-f285f435b493",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Vermont FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14037,42 +14021,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "6836af03-4278-4e2f-94bd-f285f435b493",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/683q-3f85",
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
+            "title": "State Summary Vermont FY2016"
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
-            "identifier": "VA-VBA-ABR2012-016",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries</p>",
-            "title": "Individual Service Connected Disabilities by Evaluation for Veterans Receiving Compensation at the End of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14080,44 +14060,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-016",
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
+            "title": "Individual Service Connected Disabilities by Evaluation for Veterans Receiving Compensation at the End of FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/68wg-i6vk",
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
-            "identifier": "https://www.data.va.gov/api/views/68wg-i6vk",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE NOV2018",
-            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14125,63 +14109,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/68wg-i6vk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/68wg-i6vk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/68wg-i6vk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/68wg-i6vk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/68wg-i6vk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/68wg-i6vk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/68wg-i6vk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/68wg-i6vk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/68wg-i6vk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/68wg-i6vk",
+            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 120"
+            ],
+            "landingPage": "https://www.data.va.gov/d/68wg-i6vk",
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
+            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE NOV2018"
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
-            "identifier": "VA-VBA-ABR2012-098",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Maryland-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14189,49 +14169,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-098",
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
+            "title": "Maryland-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_July_2011.xls",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-07-01T04:00:00Z/2011-07-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program.doc"
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
-            "identifier": "VA-VBA-INS2011-002",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 7-31-11.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "EOM July FY2011 - Face Amount of Life Insurance Coverage by Program by State",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14240,27 +14219,63 @@
                     "title": "xls"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_July_2011.xls",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program.doc"
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
+            "title": "EOM July FY2011 - Face Amount of Life Insurance Coverage by Program by State"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_Completed_Access_Data_20150630RptDate_Final_New.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 30 June 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-417",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-06-30T04:00:00Z/2015-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -14274,94 +14289,63 @@
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
-            "identifier": "VA-VHA-OIA-417",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Jun 30",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_Completed_Access_Data_20150630RptDate_Final_New.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 30 June 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-06-30T04:00:00Z/2015-06-30T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Jun 30"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6c82-9j9k",
-            "issued": "2023-07-14",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-14",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Nevada FY2021",
+            "identifier": "https://www.data.va.gov/api/views/6c82-9j9k",
+            "issued": "2023-07-14",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "nevada"
             ],
-            "identifier": "https://www.data.va.gov/api/views/6c82-9j9k",
+            "landingPage": "https://www.data.va.gov/d/6c82-9j9k",
+            "modified": "2024-06-14",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Nevada FY2021",
             "title": "NCVAS State Summary Nevada FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6cg3-e4y4",
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
-            "identifier": "https://www.data.va.gov/api/views/6cg3-e4y4",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist wartime veterans in need whose non-service- connected disabilities are permanent and total preventing them from following a substantially gainful occupation. A Veteran who meets the wartime service requirements is potential eligible if he/she is: \u2022 permanently and totally disabled for reasons not necessarily due to service, \u2022 age 65 or older, or \u2022 is presumed to be totally and permanently disabled for pension purposes because: o he/she is a patient in a nursing home for long-term care due to a disability, or o being disabled, as determined by the Commissioner of Social Security (SS) for purposes of any benefits administered by the Commissioner, such as SS disability benefits or Supplemental Security Income. Income restrictions are prescribed in 38 U.S.C. 1521. Pension is not payable to those whose estates are so large that it is reasonable they use the estate for maintenance. A Veteran meets wartime service requirements if he/she served: \u2022 a total of 90 days or more during one or more periods of war; \u2022 90 or more consecutive days that began or ended during a period of war; or \u2022 for any length of time during a period of war if he/she was discharged or released for a service-connected disability. Veterans entering service after September 7, 1980, must also meet the minimum active duty requirement of 24 months of continuous service or the full period to which the Veteran was called to active duty. (38 U.S.C.5303(A)).</p>",
-            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS JAN2019",
-            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14369,61 +14353,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6cg3-e4y4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6cg3-e4y4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6cg3-e4y4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6cg3-e4y4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6cg3-e4y4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6cg3-e4y4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6cg3-e4y4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6cg3-e4y4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6cg3-e4y4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/6cg3-e4y4",
+            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 104"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6cg3-e4y4",
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
+            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6dbz-5z8a",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-11-01T04:00:00Z/2014-11-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "debt referral"
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
-            "identifier": "VA-OM-OM-107",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT Nov 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14431,41 +14414,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-107",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referral"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6dbz-5z8a",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-11-01T04:00:00Z/2014-11-30T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT Nov 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6e7u-v8pg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-04-01T04:00:00Z/2015-04-30T04:00:00Z",
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
-            "identifier": "VA-OM-OM-135",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT APR 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14473,40 +14456,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-135",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6e7u-v8pg",
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
+            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT APR 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6et8-yryh",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-11-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "facilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff Lyttle",
                 "hasEmail": "mailto:JLyttle@microsoft.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "94f5c918-7f36-4058-b228-44134294fe49",
+            "dataQuality": true,
             "description": "<p>This dataset provides information about facilities within a specified radius of a geographic location.  The geographic location can bet a latitude/longitude combination, zip code or name of city or state.  Includes address, phone numbers, estimated wait time, in addition to information on same day or walk in availability.</p>",
-            "title": "Access to Care",
-            "programCode": [
-                "029:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14515,41 +14500,38 @@
                     "title": "Access to Care "
                 }
             ],
-            "dataQuality": true,
+            "identifier": "94f5c918-7f36-4058-b228-44134294fe49",
+            "issued": "2017-11-12",
+            "keyword": [
+                "facilities"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6et8-yryh",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "Access to Care"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/6f79-zus4",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-04",
-            "keyword": [
-                "pension",
-                "veterans",
-                "veterans surviving spouses and children"
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
-            "identifier": "https://www.data.va.gov/api/views/6f79-zus4",
             "description": "All Survivors Pension Recipients by Veteran's Period of Service FY2020.  Pension is a needs-based benefit designed to provide certain wartime Veterans and their survivors with a minimum level of income that raises their standard of living.",
-            "title": "All Survivors Pension Recipients by Veteran's Period of Service FY2020",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14557,40 +14539,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6f79-zus4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6f79-zus4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6f79-zus4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6f79-zus4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6f79-zus4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6f79-zus4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6f79-zus4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6f79-zus4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6f79-zus4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/6f79-zus4",
+            "issued": "2022-04-29",
+            "keyword": [
+                "pension",
+                "veterans",
+                "veterans surviving spouses and children"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6f79-zus4",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-05-04",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "All Survivors Pension Recipients by Veteran's Period of Service FY2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/6fns-gt2m",
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
+            "description": "<p>The Emergency Department Integration Software (EDIS) is a VHA-wide application used to track and manage the delivery off care to patients in the Emergency Care System (ECS).  This critical IT solution directly supports the Major Initiative 'Enhance the Veteran Experience and Access to Healthcare (EVEAH).  EDIS v1.0 is currently being deployed in each VHA hospital and is scheduled for deployment completion by 7/31/2011.  The application improves emergency department care by introducing the systematic collection, display and reporting on patient status information.  It is able to integrate with Appointment Management and Patient Care Encounter within VistA.  EDIS v2.0 is currently being planned and will provide enhancements, better functionality and improved reports.</p>",
+            "identifier": "VA-VHA-PCS-006",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "care",
                 "department",
@@ -14602,77 +14605,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/6fns-gt2m",
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
-            "identifier": "VA-VHA-PCS-006",
-            "description": "<p>The Emergency Department Integration Software (EDIS) is a VHA-wide application used to track and manage the delivery off care to patients in the Emergency Care System (ECS).  This critical IT solution directly supports the Major Initiative 'Enhance the Veteran Experience and Access to Healthcare (EVEAH).  EDIS v1.0 is currently being deployed in each VHA hospital and is scheduled for deployment completion by 7/31/2011.  The application improves emergency department care by introducing the systematic collection, display and reporting on patient status information.  It is able to integrate with Appointment Management and Patient Care Encounter within VistA.  EDIS v2.0 is currently being planned and will provide enhancements, better functionality and improved reports.</p>",
-            "title": "Emergency Department Integration Software (EDIS)",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "2011-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Emergency Department Integration Software (EDIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6fsh-rj6s",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-11-25",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-28",
-            "keyword": [
-                "2021",
-                "age",
-                "fy2021",
-                "fy 2021",
-                "fy21",
-                "fy 21",
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
-            "identifier": "https://www.data.va.gov/api/views/6fsh-rj6s",
+            "dataQuality": true,
             "description": "Notes:\n\n\"Total Number of Veterans\" represents FY 2021 projected Veteran counts from VA's Veteran Population Projection Model 2020 (VetPop20). These projections represent living Veterans as of 9/30/2021 and are made with the assumption that Veterans are not missing information (e.g., gender, age, etc.).\n\n\"Veteran VA Users\" represents historical Veteran VA user counts from VA's United States Veterans Eligibility Trends and Statistics 2021 (USVETS 2021). These counts represent Veterans who used any VA benefit or service during FY 2021 (includes both living and deceased Veterans as of end of FY 2021).\n\n\"Veteran VA Healthcare Users\" represents historical Veteran VA healthcare user counts from VA's United States Veterans Eligibility Trends and Statistics 2021 (USVETS 2021). These counts represent Veterans who used VA healthcare during FY 2021 (includes both living and deceased Veterans as of end of FY 2021).\n\n\"Veteran VA Users\" includes Veteran users of VA healthcare or any other VA benefit or service.\n\nThere are 1,458 Veteran VA Users not shown in the table below whose gender is missing. Of these, 1,360 are missing age. There are 1,387 Veteran VA Healthcare Users not shown in the table below whose gender is missing. Of these, 1,360 are missing age.\n\nSources: USVETS 2021 and VetPop20\nEffective Date: 9/30/2021",
-            "title": "FY 2021 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Gender and Age Group",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14680,44 +14648,89 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6fsh-rj6s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6fsh-rj6s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6fsh-rj6s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6fsh-rj6s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6fsh-rj6s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6fsh-rj6s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6fsh-rj6s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6fsh-rj6s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6fsh-rj6s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/6fsh-rj6s",
+            "issued": "2022-11-25",
+            "keyword": [
+                "2021",
+                "age",
+                "fy2021",
+                "fy 2021",
+                "fy21",
+                "fy 21",
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
+            "landingPage": "https://www.data.va.gov/d/6fsh-rj6s",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-11-28",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Gender and Age Group"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 1998.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report1998.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-16",
             "issued": "2017-07-26",
-            "temporal": "1997-10-01T04:00:00Z/1998-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "1998",
                 "appeals",
@@ -14734,68 +14747,40 @@
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
-            "identifier": "VA-OIT-ITIS-16",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 1998.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 1998",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report1998.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "1997-10-01T04:00:00Z/1998-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 1998"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6gz9-k6g7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "illinois"
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
-            "identifier": "VA-OEI-OEI-183",
+            "dataQuality": true,
             "description": "<p>This summary describes the programs and services VA provided in Illinois in fiscal year 2015.</p>",
-            "title": "State Summary: Illinois",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14804,43 +14789,41 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-183",
+            "issued": "2017-07-26",
+            "keyword": [
+                "illinois"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6gz9-k6g7",
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
+            "title": "State Summary: Illinois"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6h4r-nxbw",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "congressional district",
-                "va facilities"
-            ],
             "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:florinda.balfour@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-067",
             "description": "<p>National Center for Veterans Analysis and Statistics aggregates a list of VA Facilities by Congressional District representatives</p>",
-            "title": "Department of Veterans Affairs Facilities by Congressional District",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14849,50 +14832,42 @@
                     "title": "Department of Veterans Affairs Facilities by Congressional District"
                 }
             ],
+            "identifier": "VA-OEI-OEI-067",
+            "issued": "2017-07-26",
+            "keyword": [
+                "congressional district",
+                "va facilities"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6h4r-nxbw",
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
+            "title": "Department of Veterans Affairs Facilities by Congressional District"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oprm.va.gov/privacy/systems_of_records.aspx",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-07-01T04:00:00Z/2020-07-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "citation",
-                "hyperlink to federal register",
-                "privacy act",
-                "pub date",
-                "sor",
-                "sorn",
-                "system of record",
-                "system or record notices",
-                "system title",
-                "va"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amy Rose",
                 "hasEmail": "mailto:Amy.Rose1@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-ITIS-23",
+            "dataQuality": true,
             "description": "<p>A system of records is a file, database, or program from which personal information is retrieved by name or other personal identifier. The Privacy Act provides a number of protections for your personal information. These typically include how information is collected, used, disclosed, stored, and disposed.As part of our privacy policy, VA conducts an annual review of our Privacy Act system of record notices to make sure that they are current and republishes those that require changes or updates.Please select the link to download the excel spreadsheet via the link labeled:   'Privacy Act System of Record'.The spreadsheet contains the following fields:  SOR #, PUB DATE, CITATION, HYPERLINK TO FEDERAL REGISTER, SYSTEM TITLE,  and POC.</p>",
-            "title": "VA System of Records Notices (SORNs)",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14901,49 +14876,57 @@
                     "title": "xls"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "theme": [
+            "identifier": "VA-OIT-ITIS-23",
+            "issued": "2017-07-26",
+            "keyword": [
+                "citation",
+                "hyperlink to federal register",
+                "privacy act",
+                "pub date",
+                "sor",
+                "sorn",
+                "system of record",
+                "system or record notices",
+                "system title",
+                "va"
+            ],
+            "landingPage": "https://www.oprm.va.gov/privacy/systems_of_records.aspx",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:080"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2013-07-01T04:00:00Z/2020-07-01T04:00:00Z",
+            "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA System of Records Notices (SORNs)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Utilization.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "1999-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "expenditures per patient",
-                "healthcare",
-                "priority group",
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
-            "identifier": "VA-OEI-OEI-046",
-            "description": "<p>This table shows the average expenditures per patient in each of the Department of Veterans Affairs\u00ef\u00bf\u00bd healthcare enrollment priority group categories.</p>",
-            "title": "Average Expenditures Per Patient by HealthCare Priority Group: FY00 to FY13",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/Utilization/AvgCost_FINAL2.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This table shows the average expenditures per patient in each of the Department of Veterans Affairs\u00ef\u00bf\u00bd healthcare enrollment priority group categories.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14952,69 +14935,66 @@
                     "title": "xls"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/Utilization/AvgCost_FINAL2.xlsx",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-046",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditures per patient",
+                "healthcare",
+                "priority group",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/Utilization.asp",
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
+            "temporal": "1999-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Expenditures per patient by heathcare priority group"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Average Expenditures Per Patient by HealthCare Priority Group: FY00 to FY13"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6icf-9xmu",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "PTSD treatment studies may include people of all different backgrounds. Learning who participates in research tells us whether the findings from given studies apply to the rest of the population.",
             "identifier": "https://www.data.va.gov/api/views/6icf-9xmu",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/6icf-9xmu",
+            "modified": "2024-09-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "PTSD treatment studies may include people of all different backgrounds. Learning who participates in research tells us whether the findings from given studies apply to the rest of the population.",
             "title": "Who participates in PTSD treatment research?"
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
-            "identifier": "VA-VBA-ABR2012-094",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Kansas-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15022,29 +15002,61 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-094",
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
+            "title": "Kansas-FY12 Benefits Summary"
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
-            "temporal": "2015-04-15T04:00:00Z/2015-04-15T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/health/docs/15_April_2015_Pending_04302015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 April 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-103",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -15058,73 +15070,43 @@
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
-            "identifier": "VA-VHA-OIA-103",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Apr 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/15_April_2015_Pending_04302015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 April 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-04-15T04:00:00Z/2015-04-15T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Apr 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/6jjc-ikcv",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "efss",
-                "electronic",
-                "form"
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
-            "identifier": "VA-ORCH-13",
+            "dataQuality": true,
             "description": "<p>The D2D EFSS (Inc 1 and 2) provides a common access point to standardize, centralize, and integrate the universal collection of Benefit Claim Forms and supporting evidence data to produce a streamlined paperless Veteran/Service member centric claims process. Allow VSOs to submit claims and documents digitially to the VA system, enable the claim to be automatically established, automatically upload the associated dcument and evidence to the Veterans eFolder or document storage repository, notifying the correct Station of Jurisdiction(SOJ) that a claim folder or eFolder is available to be worked, and notify the VSO of successful submissions and errors experienced, if applicble during submittal. This service provides claims profile data functionality.D2D. Electronic Post Office (formerly D2D Service) MSTI SR 52. Enables exteranal systems to submit (through VLER) structured official VA Forms with/without attachment documents and orchestrates temporary storage, virus checking and message durability. When complete, submits form to appropriate Form Submission Service for orchestration This service is not nationally published as of June 2014</p>",
-            "title": "VIERS Electronic Form Submission Service (EFSS)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15133,43 +15115,42 @@
                     "title": "VIERS Electronic Form Submission Service (EFSS)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-13",
+            "issued": "2017-11-17",
+            "keyword": [
+                "efss",
+                "electronic",
+                "form"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6jjc-ikcv",
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
+            "title": "VIERS Electronic Form Submission Service (EFSS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6jzx-xyg7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "employment",
-                "gulf war",
-                "occupation",
-                "veterans",
-                "world war i"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ncvas mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "b406f1a3-ba79-463a-9555-604c31502325",
+            "dataQuality": true,
             "description": "<p>To show how occupations of WWI Veterans in 1930 have evolved and changed from the Gulf War I Era Veterans\u2019 occupations in 2008.</p>",
-            "title": "Veterans Day 2018: A World War I Visualization",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15177,42 +15158,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "b406f1a3-ba79-463a-9555-604c31502325",
+            "issued": "2018-11-09",
+            "keyword": [
+                "employment",
+                "gulf war",
+                "occupation",
+                "veterans",
+                "world war i"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6jzx-xyg7",
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
+            "title": "Veterans Day 2018: A World War I Visualization"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6kr5-skza",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-09-09",
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
-            "identifier": "https://www.data.va.gov/api/views/6kr5-skza",
             "description": "VetPop2023 projection of living Veterans by gender and period of service at the state level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 State Period of Service Data, 7L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15220,57 +15201,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6kr5-skza/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6kr5-skza/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6kr5-skza/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6kr5-skza/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6kr5-skza/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6kr5-skza/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6kr5-skza/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6kr5-skza/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6kr5-skza/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/6kr5-skza",
+            "issued": "2024-09-09",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6kr5-skza",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 State Period of Service Data, 7L"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6kz8-7xru",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-07-01T04:00:00Z/2015-07-31T04:00:00Z",
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
-            "identifier": "VA-OM-OM-142",
+            "dataQuality": true,
             "description": "<p>aged accounts receivable</p>",
-            "title": "June 2015 Coin 0017",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15278,48 +15262,44 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-142",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6kz8-7xru",
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
+            "title": "June 2015 Coin 0017"
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
-            "identifier": "VA-VBA-ABR2012-124",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "UTAH-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15327,43 +15307,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-124",
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
+            "title": "UTAH-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6n9q-hu5x",
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
-            "identifier": "VA-OEI-OEI-089",
             "description": "<p>This summaries the services  and programs VA provided in Arkansas in fiscal year 2014.</p>",
-            "title": "State Summary:  Arkansas",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15372,45 +15356,46 @@
                     "title": "State Summary:  Arkansas"
                 }
             ],
+            "identifier": "VA-OEI-OEI-089",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6n9q-hu5x",
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
+            "title": "State Summary:  Arkansas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6nmt-j2dd",
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
-            "identifier": "https://www.data.va.gov/api/views/6nmt-j2dd",
-            "description": "<p>These spreadsheets contain the percent of Veteran farmers and dairymen  by county for the state of California.</p>",
-            "title": "Veteran Farmer Gender",
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
@@ -15418,84 +15403,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6nmt-j2dd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6nmt-j2dd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6nmt-j2dd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6nmt-j2dd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6nmt-j2dd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6nmt-j2dd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6nmt-j2dd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6nmt-j2dd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6nmt-j2dd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/data/VAOpenDataMigration2019/Data-Dictionary-Apps-for-Ag.pdf",
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/6nmt-j2dd",
+            "isPartOf": "64971372-40a2-4207-937c-892283f391ba",
+            "issued": "2017-07-07",
+            "keyword": [
+                "veterans farmer"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6nmt-j2dd",
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
+            "title": "Veteran Farmer Gender"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6nq3-evbf",
-            "issued": "2024-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-28",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "The PTSD Repository will help you learn about PTSD treatment research. Our data stories below explain what we know from research using charts and tables\u2014called visualizations.",
             "identifier": "https://www.data.va.gov/api/views/6nq3-evbf",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/6nq3-evbf",
+            "modified": "2024-08-28",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "The PTSD Repository will help you learn about PTSD treatment research. Our data stories below explain what we know from research using charts and tables\u2014called visualizations.",
             "title": "For Everyone"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6nqd-cnms",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "1866",
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
-            "identifier": "VA-OEI-OEI-142",
             "description": "<p>VA Historical Annual Reports detail services provided by the Department for each Fiscal Year, including Benefits, Healthcare, and Burial/Memorial services.  The Reports also describe the topics of administration and management within VA, ranging from data on personnel to information on construction projects.  Statistical tables for a variety of subjects are also included.</p>",
-            "title": "Annual Report:  1866",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15504,44 +15486,43 @@
                     "title": "Annual Report: 1866"
                 }
             ],
+            "identifier": "VA-OEI-OEI-142",
+            "issued": "2017-07-26",
+            "keyword": [
+                "1866",
+                "annual report",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6nqd-cnms",
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
+            "title": "Annual Report:  1866"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6q9d-it97",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-06-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "fy2021",
-                "ncvas",
-                "state summary",
-                "va facilities"
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
-            "identifier": "https://www.data.va.gov/api/views/6q9d-it97",
             "description": "FY2021 VA facilities data provided by the National Center for Veterans Statistics and Analysis, published in 2023.",
-            "title": "FY 2021_NCVAS Facilities Data For State Summaries",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15549,59 +15530,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6q9d-it97/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6q9d-it97/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6q9d-it97/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6q9d-it97/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6q9d-it97/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6q9d-it97/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6q9d-it97/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6q9d-it97/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6q9d-it97/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/6q9d-it97",
+            "issued": "2023-06-06",
+            "keyword": [
+                "fy2021",
+                "ncvas",
+                "state summary",
+                "va facilities"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6q9d-it97",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Facilities Data For State Summaries"
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
-            "temporal": "2005-10-01T04:00:00Z/2006-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
-                "franchise fund",
-                "fy 2006"
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
-            "identifier": "VA-OM-OM-039",
+            "dataQuality": true,
             "description": "<p>Franchise Fund FY 2006 Annual Report</p>",
-            "title": "Franchise Fund FY 2006 Annual Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15610,44 +15593,46 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-039",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund",
+                "fy 2006"
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
+            "temporal": "2005-10-01T04:00:00Z/2006-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Franchise Fund FY 2006 Annual Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6qey-r9qt",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2023-03-16",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-20",
-            "keyword": [
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
-            "identifier": "https://www.data.va.gov/api/views/6qey-r9qt",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) 2019 deidentified individual-level public release data file.",
-            "title": "AES 2019 PRDF",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15655,65 +15640,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6qey-r9qt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6qey-r9qt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6qey-r9qt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6qey-r9qt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6qey-r9qt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6qey-r9qt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6qey-r9qt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6qey-r9qt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6qey-r9qt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/6qey-r9qt",
+            "issued": "2023-03-16",
+            "keyword": [
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6qey-r9qt",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-03-20",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "AES 2019 PRDF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6qjy-mtj5",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2006-10-01T04:00:00Z/2007-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "references": [
-                "https://www1.va.gov/vetdata/docs/DataGov_Compensation_and_Pension_by_County_Technical_Notes.doc"
-            ],
-            "keyword": [
-                "disability compensation",
-                "pension",
-                "veteran"
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
-            "identifier": "VA-VBA-CP2007-001",
+            "dataQuality": true,
             "description": "<p>The Compensation and Pension by County dataset is a count of the number of veterans receiving disability compensation or pension payments from the Department of Veterans Affairs.   The data is reported at the county level, by age group and by % disability rating for each state plus recipients in Guam, Philippines and Puerto Rico.</p>",
-            "title": "FY07  Veterans Compensation and Pension by County",
-            "isPartOf": "VA-VBA-MASTER-COMPENSATIONPENSION-001",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15721,46 +15700,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-CP2007-001",
+            "isPartOf": "VA-VBA-MASTER-COMPENSATIONPENSION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "disability compensation",
+                "pension",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6qjy-mtj5",
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
+                "https://www1.va.gov/vetdata/docs/DataGov_Compensation_and_Pension_by_County_Technical_Notes.doc"
+            ],
+            "temporal": "2006-10-01T04:00:00Z/2007-09-30T04:00:00Z",
             "theme": [
                 "Section 11. Social Insurance and Human Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY07  Veterans Compensation and Pension by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6rv8-6vr9",
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
-            "identifier": "https://www.data.va.gov/api/views/6rv8-6vr9",
             "description": "Rate of Veteran use of VA programs and services by gender within each era of conflict in which they first served. Data underlying the eighth figure of Part 1 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig. 9 - Use Rate of Genders within Era",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15768,42 +15749,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6rv8-6vr9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6rv8-6vr9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6rv8-6vr9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6rv8-6vr9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6rv8-6vr9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6rv8-6vr9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6rv8-6vr9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6rv8-6vr9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6rv8-6vr9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/6rv8-6vr9",
+            "issued": "2020-10-19",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6rv8-6vr9",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig. 9 - Use Rate of Genders within Era"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/BLUEBUTTON/Resources.asp",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-01-01T05:00:00Z/2012-09-29T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/bluebutton"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/bluebutton",
+            "description": "<p>My HealtheVet (<a href=\"http://www.myhealth.va.gov\">www.myhealth.va.gov</a>) is a Personal Health Record portal designed to improve the delivery of health care services to Veterans, to promote health and wellness, and to engage Veterans as more active participants in their health care. The My HealtheVet portal enables Veterans to create and maintain a web-based PHR that provides access to patient health education information and resources, a comprehensive personal health journal, and electronic services such as online VA prescription refill requests and Secure Messaging. Veterans can visit the My HealtheVet website and self-register to create an account, although registration is not required to view the professionally-sponsored health education resources, including topics of special interest to the Veteran population. Once registered, Veterans can create a customized PHR that is accessible from any computer with Internet access.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/BLUEBUTTON/Resources.asp",
+                    "mediaType": "text/html",
+                    "title": "VA Personal Health Record Sample Data"
+                }
             ],
+            "identifier": "VA-VHA-OIA-022",
+            "issued": "2017-07-26",
             "keyword": [
                 "bluebutton",
                 "blue button",
@@ -15824,97 +15834,72 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/BLUEBUTTON/Resources.asp",
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
-            "identifier": "VA-VHA-OIA-022",
-            "description": "<p>My HealtheVet (<a href=\"http://www.myhealth.va.gov\">www.myhealth.va.gov</a>) is a Personal Health Record portal designed to improve the delivery of health care services to Veterans, to promote health and wellness, and to engage Veterans as more active participants in their health care. The My HealtheVet portal enables Veterans to create and maintain a web-based PHR that provides access to patient health education information and resources, a comprehensive personal health journal, and electronic services such as online VA prescription refill requests and Secure Messaging. Veterans can visit the My HealtheVet website and self-register to create an account, although registration is not required to view the professionally-sponsored health education resources, including topics of special interest to the Veteran population. Once registered, Veterans can create a customized PHR that is accessible from any computer with Internet access.</p>",
-            "title": "VA Personal Health Record Sample Data",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/BLUEBUTTON/Resources.asp",
-                    "mediaType": "text/html",
-                    "title": "VA Personal Health Record Sample Data"
-                }
+            "references": [
+                "https://www.va.gov/bluebutton"
             ],
-            "describedBy": "https://www.va.gov/bluebutton",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2010-01-01T05:00:00Z/2012-09-29T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Personal Health Record Sample Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/6rxk-ghfh",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-07",
-            "keyword": [
-                "connecticut",
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
-            "identifier": "https://www.data.va.gov/api/views/6rxk-ghfh",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Connecticut",
+            "identifier": "https://www.data.va.gov/api/views/6rxk-ghfh",
+            "issued": "2021-08-26",
+            "keyword": [
+                "connecticut",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6rxk-ghfh",
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
+            "title": "State Summaries_Connecticut"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6s3x-wuyi",
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
-            "identifier": "https://www.data.va.gov/api/views/6s3x-wuyi",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE NOV2018",
-            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15922,62 +15907,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6s3x-wuyi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6s3x-wuyi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6s3x-wuyi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6s3x-wuyi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6s3x-wuyi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6s3x-wuyi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6s3x-wuyi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6s3x-wuyi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6s3x-wuyi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/6s3x-wuyi",
+            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "issued": "2019-03-20",
+            "keyword": [
+                "cdfa 64.124"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6s3x-wuyi",
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
+            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE NOV2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6sdp-biwm",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "nevada",
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
-            "identifier": "VA-OEI-OEI-115",
             "description": "<p>This is a summary of the programs and services provided by VA in Nevada in fiscal year 2014.</p>",
-            "title": "State Summary:  Nevada",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15986,27 +15969,47 @@
                     "title": "State Summary:  Nevada"
                 }
             ],
+            "identifier": "VA-OEI-OEI-115",
+            "issued": "2017-07-26",
+            "keyword": [
+                "nevada",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6sdp-biwm",
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
+            "title": "State Summary:  Nevada"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/6stm-bwji",
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
+            "description": "<p>The Performance and Operational Web-Enabled Reports (POWER) system is a state-of-the-art data warehouse containing data on Veterans Health Administration (VHA) performance metrics that are obtained daily from the individual Veterans Health Information Systems and Technology Architecture (VistA) systems.The POWER system was developed to measure the key performance indicators across VHA facilities and is helping to improve VHA's Medical Care Collections Fund (MCCF) revenue operational performance by providing accurate, reliable, and up-to-date performance measure information. POWER leverages a data warehouse to maintain data used in VHA performance measure calculations. The site provides Web-based analytical reporting capabilities, allowing users to view data by dimensions, such as, National, Consolidated Patient Account Center (CPAC), Veterans Integrated Service Network (VISN), or Station locations and by month. The data can also be displayed in tables, graphs and spreadsheets. It should be noted that POWER is not an accounting system; rather, it is a strategic and operational performance reporting system.The POWER system supports VHA's efforts to improve its revenue business operations by providing accurate and reliable performance information on the following metrics: Collections, Gross Days Revenue Outstanding (GDRO), Percentage of Accounts Receivable (AR) Greater than 90 Days, Days to Bill, Total Billings, Percentage of Collections to Billings, and Cost to Collect. POWER is VHA's revenue performance metric dashboard monitoring system that tracks MCCF performance by National, CPAC, VISN and Station.</p>",
+            "identifier": "VA-VHA-CBO-009",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "account",
                 "billing",
@@ -16022,62 +16025,42 @@
                 "veteran",
                 "web"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/6stm-bwji",
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
-            "identifier": "VA-VHA-CBO-009",
-            "description": "<p>The Performance and Operational Web-Enabled Reports (POWER) system is a state-of-the-art data warehouse containing data on Veterans Health Administration (VHA) performance metrics that are obtained daily from the individual Veterans Health Information Systems and Technology Architecture (VistA) systems.The POWER system was developed to measure the key performance indicators across VHA facilities and is helping to improve VHA's Medical Care Collections Fund (MCCF) revenue operational performance by providing accurate, reliable, and up-to-date performance measure information. POWER leverages a data warehouse to maintain data used in VHA performance measure calculations. The site provides Web-based analytical reporting capabilities, allowing users to view data by dimensions, such as, National, Consolidated Patient Account Center (CPAC), Veterans Integrated Service Network (VISN), or Station locations and by month. The data can also be displayed in tables, graphs and spreadsheets. It should be noted that POWER is not an accounting system; rather, it is a strategic and operational performance reporting system.The POWER system supports VHA's efforts to improve its revenue business operations by providing accurate and reliable performance information on the following metrics: Collections, Gross Days Revenue Outstanding (GDRO), Percentage of Accounts Receivable (AR) Greater than 90 Days, Days to Bill, Total Billings, Percentage of Collections to Billings, and Cost to Collect. POWER is VHA's revenue performance metric dashboard monitoring system that tracks MCCF performance by National, CPAC, VISN and Station.</p>",
-            "title": "Performance and Operational Web-Enabled Reports (POWER)",
-            "programCode": [
-                "029:041"
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
+            "title": "Performance and Operational Web-Enabled Reports (POWER)"
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
-            "temporal": "2001-01-01T05:00:00Z/2001-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-018",
+            "dataQuality": true,
             "description": "<p>2001 VA Performance and Accountability Report.</p>",
-            "title": "2001 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16086,51 +16069,46 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-018",
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
+            "temporal": "2001-01-01T05:00:00Z/2001-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2001 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.pbm.va.gov/PBM/index.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2000-12-31T05:00:00Z/2015-08-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "drug",
-                "health",
-                "healthcare",
-                "medication",
-                "pbm",
-                "pharmacy",
-                "prescription",
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
-            "identifier": "VA-VHA-PBM-008",
+            "dataQuality": true,
             "description": "<p>The VA Pharmacy Benefits Management Services offer a broad range of services and are committed to provide and deliver Veterans personalized, proactive, patient-driven health care.  Our Mission:  To improve the health status of Veterans by encouraging the appropriate use of medications in a comprehensive medical care setting.  Our Goal:  To provide Veterans with reliable, evidence-based medication information in an efficient manner so you along with your health care team can make informed decisions about your medications and improve your overall health.</p>",
-            "title": "VA Pharmacy Benefits Management Services",
-            "programCode": [
-                "029:047"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16139,26 +16117,61 @@
                     "title": "Tiered Copay List"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VHA-PBM-008",
+            "issued": "2017-07-26",
+            "keyword": [
+                "drug",
+                "health",
+                "healthcare",
+                "medication",
+                "pbm",
+                "pharmacy",
+                "prescription",
+                "veteran"
+            ],
+            "landingPage": "https://www.pbm.va.gov/PBM/index.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:047"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2000-12-31T05:00:00Z/2015-08-01T04:00:00Z",
             "theme": [
                 "Pharmacy"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Pharmacy Benefits Management Services"
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
+                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX-FY2000-NOVETPOP-ALL.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-026",
             "issued": "2017-07-26",
-            "temporal": "1999-10-01T04:00:00Z/2000-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -16172,70 +16185,40 @@
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
+            "modified": "2024-11-19",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OEI-OEI-026",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2000",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX-FY2000-NOVETPOP-ALL.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "1999-10-01T04:00:00Z/2000-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6x97-ah68",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-01-01T05:00:00Z/2015-07-28T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "burials",
-                "interments"
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
-            "identifier": "VA-NCA-IS-001",
+            "dataQuality": true,
             "description": "<p>This documents informs about interment eligibility, assignment of space, and entitlement to burial benefits for Veterans in National Cemeteries.</p>",
-            "title": "Interments in Department of Veterans Affairs National Cemeteries",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16244,40 +16227,41 @@
                     "title": "Interments in VA National Cemeteries"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-IS-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "burials",
+                "interments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6x97-ah68",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-01-01T05:00:00Z/2015-07-28T04:00:00Z",
             "theme": [
                 "Interment"
-            ]
+            ],
+            "title": "Interments in Department of Veterans Affairs National Cemeteries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6xbp-wie2",
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
-            "identifier": "https://www.data.va.gov/api/views/6xbp-wie2",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE MAY2019",
-            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16285,129 +16269,128 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6xbp-wie2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6xbp-wie2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6xbp-wie2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6xbp-wie2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6xbp-wie2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6xbp-wie2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6xbp-wie2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6xbp-wie2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6xbp-wie2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/6xbp-wie2",
+            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 120"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6xbp-wie2",
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
+            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/6yaj-dzgn",
-            "issued": "2019-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-09",
-            "keyword": [
-                "cemetaries"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Danielle Gervalis",
                 "hasEmail": "mailto:Danielle.gervalis@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/6yaj-dzgn",
             "description": "The U.S. Department of Veterans Affairs (VA), National Cemetery Administration (NCA), honors Veterans and their eligible family members with final resting places in national shrines and with lasting tributes that commemorate their service and sacrifice to our nation.",
-            "title": "National Cemetery Administration",
+            "identifier": "https://www.data.va.gov/api/views/6yaj-dzgn",
+            "issued": "2019-09-10",
+            "keyword": [
+                "cemetaries"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6yaj-dzgn",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-04-09",
             "programCode": [
                 "029:001"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "National Cemetery Administration"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6yqt-n4tt",
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
+            "description": "<p>USA Spending file- 01/2014-Veterans Compensation for Service-Connected Disability-  CFDA 64.109</p>",
+            "identifier": "VA-VBA-USASPENDING012014-030",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 109",
                 "compensation for service-connected disability",
                 "compensation service",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/6yqt-n4tt",
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
-            "identifier": "VA-VBA-USASPENDING012014-030",
-            "description": "<p>USA Spending file- 01/2014-Veterans Compensation for Service-Connected Disability-  CFDA 64.109</p>",
-            "title": "USA Spending file- 01/2014-Veterans Compensation for Service-Connected Disability-  CFDA 64.109",
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
+            "title": "USA Spending file- 01/2014-Veterans Compensation for Service-Connected Disability-  CFDA 64.109"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/6ywg-xptn",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-08-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-10",
-            "keyword": [
-                "veterans",
-                "women veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:NCVAS"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/6ywg-xptn",
             "description": "",
-            "title": "Marital Status of Veterans by Gender",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16415,57 +16398,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6ywg-xptn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6ywg-xptn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6ywg-xptn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6ywg-xptn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6ywg-xptn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6ywg-xptn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6ywg-xptn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6ywg-xptn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6ywg-xptn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/6ywg-xptn",
+            "issued": "2024-08-27",
+            "keyword": [
+                "veterans",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6ywg-xptn",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-10",
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
-            "landingPage": "https://www.data.va.gov/d/6z4s-zi7y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-08-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "1c5d1972-7927-4b96-8cb8-690f7969f133",
+            "dataQuality": true,
             "description": "<p>The product displays data related to Disability Compensation and VA Healthcare for FY 2000 to FY 2016.</p>",
-            "title": "Disability Compensation and Patient Expenditures: FY2000 to FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16473,42 +16457,43 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "1c5d1972-7927-4b96-8cb8-690f7969f133",
+            "issued": "2018-08-24",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6z4s-zi7y",
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
                 "Demographics"
-            ]
+            ],
+            "title": "Disability Compensation and Patient Expenditures: FY2000 to FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
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
-            "identifier": "VA-OEI-OEI-014",
-            "description": "<p>This report uses data from the 2011 American Community Survey to compare the demographic and socioeconomic characteristics of Veterans and non-Veterans. It also explores the differences between male and female Veterans.</p>",
-            "title": "Women Veteran Profile",
+            "dataQuality": true,
+            "describedBy": "https://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict10.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This report uses data from the 2011 American Community Survey to compare the demographic and socioeconomic characteristics of Veterans and non-Veterans. It also explores the differences between male and female Veterans.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16517,45 +16502,44 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict10.pdf",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-014",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans",
+                "women"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/",
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
+            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Women Veterans"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Women Veteran Profile"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6zg5-knvn",
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
-            "identifier": "https://www.data.va.gov/api/views/6zg5-knvn",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located.</p>",
-            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS DEC2018",
-            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16563,62 +16547,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6zg5-knvn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6zg5-knvn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6zg5-knvn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6zg5-knvn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6zg5-knvn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6zg5-knvn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6zg5-knvn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6zg5-knvn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6zg5-knvn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/6zg5-knvn",
+            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 114"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6zg5-knvn",
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
+            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/73qg-hhpj",
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
-            "identifier": "https://www.data.va.gov/api/views/73qg-hhpj",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE DEC2018",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16626,61 +16609,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/73qg-hhpj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/73qg-hhpj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/73qg-hhpj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/73qg-hhpj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/73qg-hhpj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/73qg-hhpj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/73qg-hhpj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/73qg-hhpj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/73qg-hhpj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/73qg-hhpj",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/73qg-hhpj",
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
+            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/73zb-hqbm",
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
-            "identifier": "252c53d0-a878-4569-8160-5d8360f33ae7",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Virginia FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16688,38 +16672,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "252c53d0-a878-4569-8160-5d8360f33ae7",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/73zb-hqbm",
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
+            "title": "State Summary Virginia FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/74dp-ziah",
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
-            "identifier": "VA-OM-OM-113",
             "description": "<p>FY 2003 Franchise Fund Annual Report Management's Decision and Analysis</p>",
-            "title": "FY 2003 Franchise Fund Annual Report Management's Decision and Analysis",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16728,42 +16710,42 @@
                     "title": "FY 2003 Franchise Fund Annual Report Management's Discussion and Analysis"
                 }
             ],
+            "identifier": "VA-OM-OM-113",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund"
+            ],
+            "landingPage": "https://www.data.va.gov/d/74dp-ziah",
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
+            "title": "FY 2003 Franchise Fund Annual Report Management's Decision and Analysis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/754e-p9yd",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "demographic",
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
-            "identifier": "VA-OEI-OEI-156",
             "description": "<p>This report uses 2014 American Community Survey data to compare the demographic and socioeconomic characteristics of Veterans and non-Veterans.</p>",
-            "title": "Profile of Veterans: 2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16772,25 +16754,46 @@
                     "title": "Profile of Veterans: 2014"
                 }
             ],
+            "identifier": "VA-OEI-OEI-156",
+            "issued": "2017-07-26",
+            "keyword": [
+                "demographic",
+                "socioeconomic",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/754e-p9yd",
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
+            "title": "Profile of Veterans: 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/755v-erad",
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
+            "description": "<p>The Real Property Project Tracking System (RPPTS), formerly known as the Lease/Project Tracking (LEASE) database, contains information about lease and land projects that are handled by the Office of Construction &amp; Facilities Management. Through a delegation of leasing authority from General Services Administration (GSA), VA directly leases its space. Information collected includes type of space, type of lease, proposed space dimensions and budget, type of land acquisition, brief description of the project, acquisition milestone dates, and project manager's contact information. The information is provided and entered in by the responsible project manager. RPPTS was developed by the VA Headquarters Automation Center in collaboration with Real Property Management Service to provide on-line access to information concerning VA's direct leasing projects.</p>",
+            "identifier": "VA-VHA-VHA-004",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "construction",
                 "facility",
@@ -16801,60 +16804,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/755v-erad",
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
-            "identifier": "VA-VHA-VHA-004",
-            "description": "<p>The Real Property Project Tracking System (RPPTS), formerly known as the Lease/Project Tracking (LEASE) database, contains information about lease and land projects that are handled by the Office of Construction &amp; Facilities Management. Through a delegation of leasing authority from General Services Administration (GSA), VA directly leases its space. Information collected includes type of space, type of lease, proposed space dimensions and budget, type of land acquisition, brief description of the project, acquisition milestone dates, and project manager's contact information. The information is provided and entered in by the responsible project manager. RPPTS was developed by the VA Headquarters Automation Center in collaboration with Real Property Management Service to provide on-line access to information concerning VA's direct leasing projects.</p>",
-            "title": "Real Property Project Tracking System (RPPTS)",
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
+            "title": "Real Property Project Tracking System (RPPTS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/75cu-qzav",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "district of columbia",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS mailbox",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-102",
+            "dataQuality": true,
             "description": "<p>This is a summary of the programs and services provided by VA in the District of Columbia in fiscal year 2014.</p>",
-            "title": "State Summary:  District of Columbia FY2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16862,44 +16846,44 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-102",
+            "issued": "2017-07-26",
+            "keyword": [
+                "district of columbia",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/75cu-qzav",
+            "language": [
+                "en-US"
+            ],
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
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  District of Columbia FY2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/75i2-bi8h",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "wisconsin"
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
-            "identifier": "VA-OEI-OEI-221",
             "description": "<p>This summary describes the programs and services VA provided in Wisconsin in fiscal year 2015.</p>",
-            "title": "State Summary: Wisconsin FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16908,24 +16892,43 @@
                     "title": "Wisconsin"
                 }
             ],
+            "identifier": "VA-OEI-OEI-221",
+            "issued": "2017-07-26",
+            "keyword": [
+                "wisconsin"
+            ],
+            "landingPage": "https://www.data.va.gov/d/75i2-bi8h",
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
+            "title": "State Summary: Wisconsin FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/75t4-vg4c",
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
+            "description": "<p>The VA National Clozapine Registry tracks the health and demographics of patients who have been prescribed clozapine by the VA. Clozapine, or the brand name Clozaril, is a drug used to treat the most serious cases of schizophrenia. Unfortunately, clozapine may also affect portions of the blood, lowering the body's resistance to infection and sometimes creating life-threatening circumstances. Realizing the severity of the problem, the Food and Drug Administration (FDA) established guidelines for analysis of White Blood Cells and Neutrophils and set strict minimum limits. The FDA also mandated that any manufacturer of clozapine must maintain a Clozapine Registry. These registries are to track the location and the health of clozapine patients and to ensure 'weekly White Blood Cell testing prior to delivery of the next week's supply of medication'. To date, the clozapine manufacturer registries have been unable to develop sufficient controls to meet these requirements, especially the ability to prevent dispensing clozapine when blood results are abnormal. However, because of the unique structure of Veterans Health Information Systems and Technology Architecture, the Veterans Health Administration obtained permission from the FDA and clozapine manufacturers to use its in-place computer network to gather and evaluate weekly patient information, then export this data to manufacturer clozapine registries. The VA assigned functional administration of this effort to the National Clozapine Coordinating Center (NCCC) located in Dallas, Texas. Weekly data on each VA clozapine patient is processed at two locations. Facility Level --When a clozapine prescription is written, a computer program in each facility's internal computer system retrieves white blood cell count, neutrophil count, and clozapine dose and evaluates the information according to FDA guidelines. If an adverse blood condition is found, the computer may warn to trigger a physician reevaluation, or lock out entirely to prevent dispensing, depending on the severity. Weekly, this information, along with certain patient demographic information, is gathered locally and transmitted to Hines Office of Information &amp; Technology Field Office for centralized storage. This data can only be accessed by the NCCC. Raw data is downloaded from the Hines OI Field Office database on a weekly basis. An ancillary computer program reformats the data and evaluates the information for inconsistencies and data gathering errors. The computer-corrected data is manually compared with hand-written facsimile information sent to the NCCC by each site. This manually corrected data is again reformatted for data storage in MS Access format at the NCCC. The corrected data is also reformatted into American Standard Code for Information Interchange fixed-length fields and transmitted via modem to the manufacturers' Clozapine Registry and, in turn, to the FDA.</p>",
+            "identifier": "VA-VHA-PBM-005",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1991-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "clozapine",
                 "clozaril",
@@ -16939,62 +16942,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/75t4-vg4c",
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
-            "identifier": "VA-VHA-PBM-005",
-            "description": "<p>The VA National Clozapine Registry tracks the health and demographics of patients who have been prescribed clozapine by the VA. Clozapine, or the brand name Clozaril, is a drug used to treat the most serious cases of schizophrenia. Unfortunately, clozapine may also affect portions of the blood, lowering the body's resistance to infection and sometimes creating life-threatening circumstances. Realizing the severity of the problem, the Food and Drug Administration (FDA) established guidelines for analysis of White Blood Cells and Neutrophils and set strict minimum limits. The FDA also mandated that any manufacturer of clozapine must maintain a Clozapine Registry. These registries are to track the location and the health of clozapine patients and to ensure 'weekly White Blood Cell testing prior to delivery of the next week's supply of medication'. To date, the clozapine manufacturer registries have been unable to develop sufficient controls to meet these requirements, especially the ability to prevent dispensing clozapine when blood results are abnormal. However, because of the unique structure of Veterans Health Information Systems and Technology Architecture, the Veterans Health Administration obtained permission from the FDA and clozapine manufacturers to use its in-place computer network to gather and evaluate weekly patient information, then export this data to manufacturer clozapine registries. The VA assigned functional administration of this effort to the National Clozapine Coordinating Center (NCCC) located in Dallas, Texas. Weekly data on each VA clozapine patient is processed at two locations. Facility Level --When a clozapine prescription is written, a computer program in each facility's internal computer system retrieves white blood cell count, neutrophil count, and clozapine dose and evaluates the information according to FDA guidelines. If an adverse blood condition is found, the computer may warn to trigger a physician reevaluation, or lock out entirely to prevent dispensing, depending on the severity. Weekly, this information, along with certain patient demographic information, is gathered locally and transmitted to Hines Office of Information &amp; Technology Field Office for centralized storage. This data can only be accessed by the NCCC. Raw data is downloaded from the Hines OI Field Office database on a weekly basis. An ancillary computer program reformats the data and evaluates the information for inconsistencies and data gathering errors. The computer-corrected data is manually compared with hand-written facsimile information sent to the NCCC by each site. This manually corrected data is again reformatted for data storage in MS Access format at the NCCC. The corrected data is also reformatted into American Standard Code for Information Interchange fixed-length fields and transmitted via modem to the manufacturers' Clozapine Registry and, in turn, to the FDA.</p>",
-            "title": "VA National Clozapine Registry",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1991-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA National Clozapine Registry"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/75yf-ztdh",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cpe",
-                "provider"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joseph Enderle",
                 "hasEmail": "mailto:joseph.enderle@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-ORCH-7",
+            "dataQuality": true,
             "description": "<p>Web service proxy/wrapper for CP&amp;E capabilities/data. This interface will retrieve a Bill of Collection record from CP&amp;E and enable a CRM user to view the Bill information. Back office CRM users (primarily DCU Unit) require the ability to review Bills to respond to customer inquiries about Bills and Offsets. The interface will be triggered when a user attempts to query for a Bill using the Bill # (K#).</p>",
-            "title": "CP&E Provider Adapters Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17003,36 +16986,40 @@
                     "title": "CP&E Provider Adapters Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-7",
+            "issued": "2017-11-17",
+            "keyword": [
+                "cpe",
+                "provider"
+            ],
+            "landingPage": "https://www.data.va.gov/d/75yf-ztdh",
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
+            "title": "CP&E Provider Adapters Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/76zg-mjxm",
-            "issued": "2024-05-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-09",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/76zg-mjxm",
             "description": "VetPop2020 projected number of Veterans who served in World War II by state for fiscal year 2023.",
-            "title": "WWII Veterans by State, FY2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17040,100 +17027,116 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/76zg-mjxm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/76zg-mjxm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/76zg-mjxm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/76zg-mjxm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/76zg-mjxm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/76zg-mjxm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/76zg-mjxm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/76zg-mjxm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/76zg-mjxm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/76zg-mjxm",
+            "issued": "2024-05-06",
+            "landingPage": "https://www.data.va.gov/d/76zg-mjxm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "WWII Veterans by State, FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/7765-4ury",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Arkansas FY2023",
+            "identifier": "https://www.data.va.gov/api/views/7765-4ury",
             "issued": "2024-05-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "arkansas",
                 "fy2024 data",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/7765-4ury",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/7765-4ury",
-            "description": "NCVAS State Summary Arkansas FY2023",
-            "title": "NCVAS State Summary Arkansas FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Arkansas FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/779c-9i7w",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "tennessee",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@VA.Gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/779c-9i7w",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Tennessee",
+            "identifier": "https://www.data.va.gov/api/views/779c-9i7w",
+            "issued": "2021-08-26",
+            "keyword": [
+                "tennessee",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/779c-9i7w",
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
+            "title": "State Summaries_Tennessee"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/77h2-qfg5",
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
+            "description": "<p>The Automated Safety Incident Surveillance and Tracking System (ASISTS) is a repository of Veterans Health Administration (VHA) employee accident data. Many types of accidents are captured, but the primary focus of the ASISTS database is to track and to report on employee exposures to blood borne pathogens through needlesticks, sharps and body fluids. Accident data is captured locally at medical centers using the Veterans Health Information Systems and Technology Architecture (VistA) ASISTS package. Federal Employee Compensation claims are transmitted electronically in order to provide efficient and timely submission to the Department of Labor, Office of Workers' Compensation Programs; and to ensure that the Occupational Safety and Health Administration's (OSHA) Log of Work-Related Injuries and Illnesses is maintained. On a daily basis the Federal Employee Compensation claims are transmitted by Electronic Data Interchange extraction. A weekly download of the accident reports are sent to the national database using MailMan messages. On a monthly basis, extracts are sent to the ASISTS central repository located at the Austin Information Technology Center. The VHA Support Service Center (VSSC) provides multiple customized reports on the VSSC Web portal available on the VA Intranet. The primary users of ASISTS include OSHA, VA Headquarters, the VISN Directors, and occupational safety and health professionals located at each VA medical facility.</p>",
+            "identifier": "VA-VHA-OPH-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1999-01-01T05:00:00Z/2013-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "accident",
                 "employee",
@@ -17142,61 +17145,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/77h2-qfg5",
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
-            "identifier": "VA-VHA-OPH-002",
-            "description": "<p>The Automated Safety Incident Surveillance and Tracking System (ASISTS) is a repository of Veterans Health Administration (VHA) employee accident data. Many types of accidents are captured, but the primary focus of the ASISTS database is to track and to report on employee exposures to blood borne pathogens through needlesticks, sharps and body fluids. Accident data is captured locally at medical centers using the Veterans Health Information Systems and Technology Architecture (VistA) ASISTS package. Federal Employee Compensation claims are transmitted electronically in order to provide efficient and timely submission to the Department of Labor, Office of Workers' Compensation Programs; and to ensure that the Occupational Safety and Health Administration's (OSHA) Log of Work-Related Injuries and Illnesses is maintained. On a daily basis the Federal Employee Compensation claims are transmitted by Electronic Data Interchange extraction. A weekly download of the accident reports are sent to the national database using MailMan messages. On a monthly basis, extracts are sent to the ASISTS central repository located at the Austin Information Technology Center. The VHA Support Service Center (VSSC) provides multiple customized reports on the VSSC Web portal available on the VA Intranet. The primary users of ASISTS include OSHA, VA Headquarters, the VISN Directors, and occupational safety and health professionals located at each VA medical facility.</p>",
-            "title": "Automated Safety Incident Surveillance and Tracking System (ASISTS)",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1999-01-01T05:00:00Z/2013-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Automated Safety Incident Surveillance and Tracking System (ASISTS)"
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
-                "va",
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
-            "identifier": "VA-OEI-OEI-145",
+            "dataQuality": true,
             "description": "<p>This reports the activities of the Veterans Administration for the fiscal year ending September 30, 1981.</p>",
-            "title": "Annual Report: 1981",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17205,44 +17188,45 @@
                     "title": "Annual Report: 1981"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-145",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "va",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/",
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
+            "title": "Annual Report: 1981"
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
-            "temporal": "2010-07-01T04:00:00Z/2010-09-30T04:00:00Z",
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
-            "identifier": "VA-OM-OM-096",
+            "dataQuality": true,
             "description": "<p>FY 2010 Fourth Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2010 Fourth Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17251,45 +17235,43 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-096",
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
+            "temporal": "2010-07-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2010 Fourth Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/78jd-jt77",
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
-            "identifier": "https://www.data.va.gov/api/views/78jd-jt77",
             "description": "",
-            "title": "Table 6 - U. S. Veterans Life Table for Female 2000-2009",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17297,62 +17279,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/78jd-jt77/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/78jd-jt77/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/78jd-jt77/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/78jd-jt77/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/78jd-jt77/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/78jd-jt77/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/78jd-jt77/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/78jd-jt77/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/78jd-jt77/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/78jd-jt77",
+            "issued": "2023-04-18",
+            "keyword": [
+                "death rate",
+                "life expectancy",
+                "life table"
+            ],
+            "landingPage": "https://www.data.va.gov/d/78jd-jt77",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Table 6 - U. S. Veterans Life Table for Female 2000-2009"
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
-            "identifier": "VA-VBA-ABR2012-014",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "GWOT Disabilities by Body System and Gender for Veterans Receiving Comp at the End of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17360,50 +17340,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-014",
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
+            "title": "GWOT Disabilities by Body System and Gender for Veterans Receiving Comp at the End of FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/79ex-hbqv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "rights": "public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
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
-            "identifier": "VA-VBA-ABR2012-127",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Washington-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17411,43 +17390,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-127",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.data.va.gov/d/79ex-hbqv",
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
+            "rights": "public",
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Washington-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/79ry-anma",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "indiana"
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
-            "identifier": "VA-OEI-OEI-184",
             "description": "<p>This summary describes the programs and services VA provided in Indiana in fiscal year 2015.</p>",
-            "title": "State Summary: Indiana",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17456,40 +17440,40 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-184",
+            "issued": "2017-07-26",
+            "keyword": [
+                "indiana"
+            ],
+            "landingPage": "https://www.data.va.gov/d/79ry-anma",
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
+            "title": "State Summary: Indiana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7abb-78r5",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "kentucky"
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
-            "identifier": "VA-OEI-OEI-187",
             "description": "<p>This summary describes the programs and services VA provided in Kentucky in fiscal year 2015.</p>",
-            "title": "State Summary: Kentucky",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17498,24 +17482,43 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-187",
+            "issued": "2017-07-26",
+            "keyword": [
+                "kentucky"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7abb-78r5",
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
+            "title": "State Summary: Kentucky"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/7ahm-cn5f",
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
+            "description": "<p>Effective management of Pathology and Laboratory Medicine Service (P&amp;LMS) laboratories requires indicators capable of demonstrating each individual laboratory's productivity and efficiency. Local sites require the capability to determine in real time, the effects of any procedural or policy changes relating to productivity and efficiency. Data collected by each individual medical center is compiled on a national level at the Austin Information Technology Center (AITC) for P&amp;LMS Central Office utilization. Each local medical center will have the capability to independently monitor laboratory trends and make appropriate decisions. A detailed view of workload data will be provided to support a variety of management and clinical requirements and needs. Measurements of productivity and efficiency data are capable of providing medical center to medical center comparisons. In addition, workload data is suitable for comparison to private sector facilities that capture laboratory workload based on Current Procedure Terminology (CPT). The National Laboratory Workload &amp; Laboratory Management Index Program has been selected as the efficiency and productivity logic model. The National Laboratory Workload &amp; Laboratory Management Index Program report replaces the Lab Automated Management Information System (AMIS) segment used in the past. Each local site identifies the reportable units based on CPT and VA guidelines. Reportable units are extracted by laboratory software and are transmitted to the AITC. The transmitted data is compiled and stored in the National Laboratory Workload &amp; Laboratory Management Index Program database. This database supports P&amp;LMS Headquarters and Veterans Integrated Service Network director's office.</p>",
+            "identifier": "VA-VHA-PCS-017",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1996-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "cpt",
                 "lab",
@@ -17526,61 +17529,41 @@
                 "veteran",
                 "workload"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/7ahm-cn5f",
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
-            "identifier": "VA-VHA-PCS-017",
-            "description": "<p>Effective management of Pathology and Laboratory Medicine Service (P&amp;LMS) laboratories requires indicators capable of demonstrating each individual laboratory's productivity and efficiency. Local sites require the capability to determine in real time, the effects of any procedural or policy changes relating to productivity and efficiency. Data collected by each individual medical center is compiled on a national level at the Austin Information Technology Center (AITC) for P&amp;LMS Central Office utilization. Each local medical center will have the capability to independently monitor laboratory trends and make appropriate decisions. A detailed view of workload data will be provided to support a variety of management and clinical requirements and needs. Measurements of productivity and efficiency data are capable of providing medical center to medical center comparisons. In addition, workload data is suitable for comparison to private sector facilities that capture laboratory workload based on Current Procedure Terminology (CPT). The National Laboratory Workload &amp; Laboratory Management Index Program has been selected as the efficiency and productivity logic model. The National Laboratory Workload &amp; Laboratory Management Index Program report replaces the Lab Automated Management Information System (AMIS) segment used in the past. Each local site identifies the reportable units based on CPT and VA guidelines. Reportable units are extracted by laboratory software and are transmitted to the AITC. The transmitted data is compiled and stored in the National Laboratory Workload &amp; Laboratory Management Index Program database. This database supports P&amp;LMS Headquarters and Veterans Integrated Service Network director's office.</p>",
-            "title": "National Laboratory Workload and Laboratory Management Index Program",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1996-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Laboratory Workload and Laboratory Management Index Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7auc-r8ph",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "new york",
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
-            "identifier": "VA-OEI-OEI-118",
             "description": "<p>This is a summary of the programs and services provided by VA in New York in fiscal year 2014.</p>",
-            "title": "State Summary:  New York",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17589,44 +17572,45 @@
                     "title": "State Summary:  New York"
                 }
             ],
+            "identifier": "VA-OEI-OEI-118",
+            "issued": "2017-07-26",
+            "keyword": [
+                "new york",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7auc-r8ph",
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
+            "title": "State Summary:  New York"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7bg4-bqun",
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
-            "identifier": "0ff0232d-fb2a-4bd9-8dee-bd3a8d856e2a",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Michigan FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17634,42 +17618,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "0ff0232d-fb2a-4bd9-8dee-bd3a8d856e2a",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7bg4-bqun",
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
+            "title": "State Summary Michigan FY2016"
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
-            "identifier": "VA-VBA-ABR2012-081",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "California-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17677,57 +17657,80 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-081",
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
+            "title": "California-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/7bt9-ycpy",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "pennsylvania",
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
-            "identifier": "https://www.data.va.gov/api/views/7bt9-ycpy",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Pennsylvania",
+            "identifier": "https://www.data.va.gov/api/views/7bt9-ycpy",
+            "issued": "2021-08-26",
+            "keyword": [
+                "pennsylvania",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7bt9-ycpy",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-13",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Pennsylvania"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/7cau-jd89",
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
+            "description": "<p>The Administrative Data Repository (ADR) was established to provide support for the administrative data elements relative to multiple categories of a person entity such as demographic and eligibility information. Although initially focused on the computing needs of the Veterans Health Administration, the ADR is positioned to provide identity management and demographics support for all IT systems within the Department of Veterans Affairs.</p>",
+            "identifier": "VA-VHA-CBO-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2009-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "demographics",
                 "enrollment",
@@ -17736,43 +17739,43 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/7cau-jd89",
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
-            "identifier": "VA-VHA-CBO-001",
-            "description": "<p>The Administrative Data Repository (ADR) was established to provide support for the administrative data elements relative to multiple categories of a person entity such as demographic and eligibility information. Although initially focused on the computing needs of the Veterans Health Administration, the ADR is positioned to provide identity management and demographics support for all IT systems within the Department of Veterans Affairs.</p>",
-            "title": "Administrative Data Repository (ADR)",
-            "programCode": [
-                "029:041"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "2009-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Administrative Data Repository (ADR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/7d79-cxw8",
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
+            "description": "<p>The Associated Health Allocation Database is used to determine the allocation of positions and funds for VA Associated Health programs offered by Veterans Affairs Medical Centers (VAMC).</p>",
+            "identifier": "VA-VHA-VHA-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1998-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "funds",
                 "health",
@@ -17780,65 +17783,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/7d79-cxw8",
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
-            "identifier": "VA-VHA-VHA-001",
-            "description": "<p>The Associated Health Allocation Database is used to determine the allocation of positions and funds for VA Associated Health programs offered by Veterans Affairs Medical Centers (VAMC).</p>",
-            "title": "Associated Health Allocation",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1998-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Associated Health Allocation"
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
-            "identifier": "VA-VBA-ABR2012-107",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "New Hampshire-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17847,49 +17827,49 @@
                     "title": "New Hampshire-FY12 Benefits Summary"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "ABR 2012"
+            "identifier": "VA-VBA-ABR2012-107",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
             ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/FY11_3rd_qtr_ED_recp_by_State.csv",
-            "bureauCode": [
-                "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-04-01T04:00:00Z/2011-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.gibill.va.gov/"
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-08",
+            "programCode": [
+                "029:005"
             ],
-            "keyword": [
-                "education",
-                "veteran"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
+            "theme": [
+                "ABR 2012"
+            ],
+            "title": "New Hampshire-FY12 Benefits Summary"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "029:25"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Salminio Garner",
                 "hasEmail": "mailto:salminio.garner1@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-EDU2011-005",
+            "dataQuality": true,
             "description": "<p>FY 11 Education Recipients by State (Through the 3rd qtr. FY11). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2011(Through the 3rd qtr. FY11). State statistics may include individuals who used their education benefits in more than one state, therefore the total within this table may be different than the  total number of beneficiaries during the fiscal year.</p>",
-            "title": "FY 11_3rd Qtr_Education Recipients by State",
-            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17897,94 +17877,98 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7fzj-mwh9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7fzj-mwh9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7fzj-mwh9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7fzj-mwh9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7fzj-mwh9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7fzj-mwh9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7fzj-mwh9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7fzj-mwh9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7fzj-mwh9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2011-005",
+            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/FY11_3rd_qtr_ED_recp_by_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.gibill.va.gov/"
+            ],
+            "temporal": "2011-04-01T04:00:00Z/2011-06-30T04:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 11_3rd Qtr_Education Recipients by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/7g2p-v3sr",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "iowa",
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
-            "identifier": "https://www.data.va.gov/api/views/7g2p-v3sr",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Iowa",
+            "identifier": "https://www.data.va.gov/api/views/7g2p-v3sr",
+            "issued": "2021-08-26",
+            "keyword": [
+                "iowa",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7g2p-v3sr",
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
+            "title": "State Summaries_Iowa"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7g46-r93g",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "burial ledgers"
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
-            "identifier": "VA-NCA-MPS-003",
             "description": "<p>This document provides some history and current status of cemetery burial ledgers.</p>",
-            "title": "National Cemetery Burial Ledgers",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17993,41 +17977,40 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-NCA-MPS-003",
+            "issued": "2017-07-26",
+            "keyword": [
+                "burial ledgers"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7g46-r93g",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
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
+            "title": "National Cemetery Burial Ledgers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7g4a-u8we",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "hawaii",
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
-            "identifier": "VA-OEI-OEI-096",
             "description": "<p>This is a summary of the services and programs provided by VA in Hawaii in fiscal year 2014.</p>",
-            "title": "State Summary:  Hawaii",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18036,44 +18019,44 @@
                     "title": "State Summary:  Hawaii"
                 }
             ],
+            "identifier": "VA-OEI-OEI-096",
+            "issued": "2017-07-26",
+            "keyword": [
+                "hawaii",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7g4a-u8we",
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
+            "title": "State Summary:  Hawaii"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7g63-fxp3",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-09-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "keyword": [
-                "healthcare",
-                "health equity"
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
-            "identifier": "https://www.data.va.gov/api/views/7g63-fxp3",
             "description": "Summary level data from the National Veteran Health Equity Report - FY2013, filtered by age group.",
-            "title": "VA-OHE-NVHER-FY13-Sociodemographic-Age",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18081,42 +18064,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7g63-fxp3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7g63-fxp3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7g63-fxp3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7g63-fxp3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7g63-fxp3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7g63-fxp3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7g63-fxp3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7g63-fxp3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7g63-fxp3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/7g63-fxp3",
+            "issued": "2019-09-19",
+            "keyword": [
+                "healthcare",
+                "health equity"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7g63-fxp3",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA-OHE-NVHER-FY13-Sociodemographic-Age"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN18FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 18 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-090",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -18132,70 +18144,42 @@
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
-            "identifier": "VA-VHA-OIA-090",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 18",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN18FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 18 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 18"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7hng-ndbp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-01-16",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "median household income"
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
-            "identifier": "https://www.data.va.gov/api/views/7hng-ndbp",
             "description": "American Community Survey 5-year Estimate data on median income for veterans and non-veterans, from 2010 to 2017.",
-            "title": "Median Income - Veterans vs. Non-Veterans, 2010 - 2017",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18203,81 +18187,112 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7hng-ndbp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7hng-ndbp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7hng-ndbp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7hng-ndbp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7hng-ndbp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7hng-ndbp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7hng-ndbp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7hng-ndbp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7hng-ndbp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/7hng-ndbp",
+            "issued": "2020-01-16",
+            "keyword": [
+                "median household income"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7hng-ndbp",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Median Income - Veterans vs. Non-Veterans, 2010 - 2017"
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
+            "description": "<p>USA Spending- Compensation and Pension- Burial Expenses Allowance for Vets for January 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-016",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "burial expenses allowance for vets",
                 "cfda 64 101",
                 "compensation and pension",
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
-            "identifier": "VA-VBA-USASPENDING012014-016",
-            "description": "<p>USA Spending- Compensation and Pension- Burial Expenses Allowance for Vets for January 2014</p>",
-            "title": "USA Spending file- 01/2014 Compensation and Pension-  CFDA 64.101",
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
+            "title": "USA Spending file- 01/2014 Compensation and Pension-  CFDA 64.101"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_Completed_Access_Data_20150731RptDate_Final_New.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 31 July 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-418",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-07-31T04:00:00Z/2015-07-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -18291,70 +18306,39 @@
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
-            "identifier": "VA-VHA-OIA-418",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Jul 31",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_Completed_Access_Data_20150731RptDate_Final_New.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 31 July 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-07-31T04:00:00Z/2015-07-31T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Jul 31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7kds-tnwf",
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
-            "identifier": "https://www.data.va.gov/api/views/7kds-tnwf",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE FEB2019",
-            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18362,60 +18346,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7kds-tnwf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7kds-tnwf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7kds-tnwf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7kds-tnwf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7kds-tnwf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7kds-tnwf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7kds-tnwf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7kds-tnwf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7kds-tnwf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/7kds-tnwf",
+            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 120"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7kds-tnwf",
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
+            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7m5v-drhy",
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
-            "identifier": "https://www.data.va.gov/api/views/7m5v-drhy",
+            "dataQuality": true,
             "description": "<p>This dataset contains information on minority veteran healthcare usage, educational attainment, unemployment rates, median income, and projected population figures.</p>",
-            "title": "Veterans with No Service Connected Disability Enrollment and VA Healthcare Usage by Race/Ethnicity",
-            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18423,68 +18405,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7m5v-drhy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7m5v-drhy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7m5v-drhy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7m5v-drhy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7m5v-drhy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7m5v-drhy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7m5v-drhy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7m5v-drhy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7m5v-drhy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/7m5v-drhy",
+            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
+            "issued": "2017-03-15",
+            "keyword": [
+                "health care",
+                "income",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7m5v-drhy",
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
+            "title": "Veterans with No Service Connected Disability Enrollment and VA Healthcare Usage by Race/Ethnicity"
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
-            "identifier": "VA-VBA-ABR2012-118",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Philippines-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18492,27 +18472,50 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-118",
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
+            "title": "Philippines-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/7mwh-82f2",
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
+            "description": "<p>The Post-Deployment Health Strategic Healthcare Group (PDHSHG) Registry System of Records is the information system encompassing the Ionizing Radiation Registry (IRR), the Agent Orange Registry (AOR), and the Gulf War Registry (GWR) which also includes related Depleted Uranium (DU) exams. The AOR area of the PDH database contains VA entered information about U.S. Veterans who served in the Republic of Vietnam between 1962 and 1975, in Korea between April 1968 and August 1971, or who had a registry exam because of possible exposure to dioxin or another toxic substance in an herbicide during the conduct of, or as a result of, the testing, transporting, or spraying of herbicides for military purposes.</p>",
+            "identifier": "VA-VHA-OPH-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2002-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "agent orange",
                 "cancer",
@@ -18522,67 +18525,44 @@
                 "veteran",
                 "vietnam"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/7mwh-82f2",
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
-            "identifier": "VA-VHA-OPH-001",
-            "description": "<p>The Post-Deployment Health Strategic Healthcare Group (PDHSHG) Registry System of Records is the information system encompassing the Ionizing Radiation Registry (IRR), the Agent Orange Registry (AOR), and the Gulf War Registry (GWR) which also includes related Depleted Uranium (DU) exams. The AOR area of the PDH database contains VA entered information about U.S. Veterans who served in the Republic of Vietnam between 1962 and 1975, in Korea between April 1968 and August 1971, or who had a registry exam because of possible exposure to dioxin or another toxic substance in an herbicide during the conduct of, or as a result of, the testing, transporting, or spraying of herbicides for military purposes.</p>",
-            "title": "Agent Orange Registry (AOR) - The Environmental Hazards Strategic Healthcare Group (EHSHG) Registry System of Records",
-            "programCode": [
-                "029:041"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "2002-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Agent Orange Registry (AOR) - The Environmental Hazards Strategic Healthcare Group (EHSHG) Registry System of Records"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7n8t-uiin",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
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
-            "identifier": "VA-VHA-OIA-001",
-            "description": "<p>The 2008 Hospital Report Card was mandated by the FY08 Appropriations Act, and focused on Congressionally-mandated metrics applicable to general patient populations. The 2009 VHA Facility Quality and Safety Report report, not required by Congress, shifts to Veteran-centered metrics, and includes information related to infrastructure, care provided in outpatient and hospital settings, quality of care within given patient populations, accreditation status, patient satisfaction and patient outcomes for FY2008.  The data in this report have been compiled from multiple sources throughout VHA.  This dataset includes adjusted mortality rate for three defined populations: Pneumonia, Congestive Heart Failure, and Acute Myocardial Infarction, Nosocomisal Infections, Percent of patients on prophalaxis for deep vein thrombosis and Observed minus expected length of stay.</p>",
-            "title": "2009 VHA Facility Quality and Safety Report - Hospital Settings",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/VHA_2009_Facility_Quality_and_Safety_Report_Final.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>The 2008 Hospital Report Card was mandated by the FY08 Appropriations Act, and focused on Congressionally-mandated metrics applicable to general patient populations. The 2009 VHA Facility Quality and Safety Report report, not required by Congress, shifts to Veteran-centered metrics, and includes information related to infrastructure, care provided in outpatient and hospital settings, quality of care within given patient populations, accreditation status, patient satisfaction and patient outcomes for FY2008.  The data in this report have been compiled from multiple sources throughout VHA.  This dataset includes adjusted mortality rate for three defined populations: Pneumonia, Congestive Heart Failure, and Acute Myocardial Infarction, Nosocomisal Infections, Percent of patients on prophalaxis for deep vein thrombosis and Observed minus expected length of stay.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18590,133 +18570,133 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7n8t-uiin/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7n8t-uiin/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7n8t-uiin/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7n8t-uiin/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7n8t-uiin/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7n8t-uiin/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7n8t-uiin/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7n8t-uiin/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7n8t-uiin/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/VHA_2009_Facility_Quality_and_Safety_Report_Final.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-001",
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
+            "landingPage": "https://www.data.va.gov/d/7n8t-uiin",
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
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2009 VHA Facility Quality and Safety Report - Hospital Settings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Farm Loans: VA Home Loans for Rural Residents</p>",
+            "identifier": "VA-VBA-MEDIAPUB-036",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2013-11-01T04:00:00Z/2013-11-01T04:00:00Z",
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
-            "identifier": "VA-VBA-MEDIAPUB-036",
-            "description": "<p>Farm Loans: VA Home Loans for Rural Residents</p>",
-            "title": "Farm Loans: VA Home Loans for Rural Residents",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-11-01T04:00:00Z/2013-11-01T04:00:00Z",
             "theme": [
                 "General Benefit Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Farm Loans: VA Home Loans for Rural Residents"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7qps-5ezy",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "Learn about these therapies that use different techniques to help people process traumatic experiences. Some involve visualizing, talking or thinking about the traumatic memory. Others focus on changing unhelpful beliefs about the trauma.",
             "identifier": "https://www.data.va.gov/api/views/7qps-5ezy",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/7qps-5ezy",
+            "modified": "2024-09-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Learn about these therapies that use different techniques to help people process traumatic experiences. Some involve visualizing, talking or thinking about the traumatic memory. Others focus on changing unhelpful beliefs about the trauma.",
             "title": "What is trauma-focused psychotherapy?"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/surveys.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-01-01T05:00:00Z/2007-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-09-16",
-            "references": [
-                "https://www1.va.gov/vetdata/docs/VERS_FINAL_REPORT_2-8-08.pdf"
-            ],
-            "keyword": [
-                "employment",
-                "veteran",
-                "vocational rehabilitation"
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
-            "identifier": "VA-OEI-OEI-001",
-            "description": "<p>The 2007 Veterans Employability Research Survey (VERS) was conducted to determine the factors that impact veterans' employability resulting from participation in the VR&amp;E Program. The study consists of a nationally representative survey of veterans who have applied to the VR&amp;E Program, but who discontinued the program at various points as well as a comparison group of veterans who have completed the program.</p>",
-            "title": "2007 Veterans Employability Research Survey",
+            "dataQuality": true,
+            "describedBy": "https://www1.va.gov/vetdata/docs/DataGov_Employability_Survey_Data_Elements.doc",
             "describedByType": "application/msword",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>The 2007 Veterans Employability Research Survey (VERS) was conducted to determine the factors that impact veterans' employability resulting from participation in the VR&amp;E Program. The study consists of a nationally representative survey of veterans who have applied to the VR&amp;E Program, but who discontinued the program at various points as well as a comparison group of veterans who have completed the program.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18725,49 +18705,49 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www1.va.gov/vetdata/docs/DataGov_Employability_Survey_Data_Elements.doc",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "employment",
+                "veteran",
+                "vocational rehabilitation"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/surveys.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-09-16",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www1.va.gov/vetdata/docs/VERS_FINAL_REPORT_2-8-08.pdf"
+            ],
+            "temporal": "2007-01-01T05:00:00Z/2007-12-31T05:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2007 Veterans Employability Research Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Datagov_2nd_qtr_FY11_EDU_recp_by_State.csv",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-01-01T05:00:00Z/2011-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Datagov_2nd_qtr_FY11_EDU_recp_by_State.csv"
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
-            "identifier": "VA-VBA-EDU2011-006",
+            "dataQuality": true,
             "description": "<p>FY 11 Education Recipients by State (Through the 2nd qtr. FY11). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2011(Through the 2nd qtr. FY11). State statistics may include individuals who used their education benefits in more than one state, therefore the total within this table may be different than the  total number of beneficiaries during the fiscal year.</p>",
-            "title": "FY 11_Q2 Education Recipients by State",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18775,65 +18755,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7rcw-hs62/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7rcw-hs62/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7rcw-hs62/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7rcw-hs62/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7rcw-hs62/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7rcw-hs62/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7rcw-hs62/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7rcw-hs62/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7rcw-hs62/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2011-006",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Datagov_2nd_qtr_FY11_EDU_recp_by_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Datagov_2nd_qtr_FY11_EDU_recp_by_State.csv"
+            ],
+            "temporal": "2011-01-01T05:00:00Z/2011-03-31T04:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 11_Q2 Education Recipients by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7rj2-yazg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "georgia",
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
-            "identifier": "VA-OEI-OEI-095",
             "description": "<p>This is a summary of the programs and services provided by VA in Georgia in fiscal year 2014.</p>",
-            "title": "State Summary:  Georgia",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18842,45 +18825,44 @@
                     "title": "State Summaries:  Georgia"
                 }
             ],
+            "identifier": "VA-OEI-OEI-095",
+            "issued": "2017-07-26",
+            "keyword": [
+                "georgia",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7rj2-yazg",
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
+            "title": "State Summary:  Georgia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7s2y-gs9a",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "korean conflict",
-                "korean war",
-                "veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/7s2y-gs9a",
             "description": "Korean War Era Veterans by Year, 2000-2040. This data set supports the Korean War data story at: https://www.datahub.va.gov/stories/s/7wja-85c3",
-            "title": "Korean War Era Veterans by Year, 2000-2040",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18888,62 +18870,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7s2y-gs9a/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7s2y-gs9a/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7s2y-gs9a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7s2y-gs9a/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7s2y-gs9a/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7s2y-gs9a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7s2y-gs9a/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7s2y-gs9a/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7s2y-gs9a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/7s2y-gs9a",
+            "issued": "2020-12-15",
+            "keyword": [
+                "korean conflict",
+                "korean war",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7s2y-gs9a",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Korean War Era Veterans by Year, 2000-2040"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_amount_by_program_by_state_Oct2011.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2011-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technicalnotes_face_amount_by_program_Oct2011.doc"
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
-            "identifier": "VA-VBA-INS2011-008",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 10-31-11.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "FY11_EOM_Oct_Face Amount of Life Insurance Coverage by Program by State",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18951,48 +18930,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7ses-ja3u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7ses-ja3u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7ses-ja3u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7ses-ja3u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7ses-ja3u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7ses-ja3u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7ses-ja3u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7ses-ja3u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7ses-ja3u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-008",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_amount_by_program_by_state_Oct2011.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technicalnotes_face_amount_by_program_Oct2011.doc"
+            ],
+            "temporal": "2011-10-01T04:00:00Z/2011-10-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY11_EOM_Oct_Face Amount of Life Insurance Coverage by Program by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7sj2-ymyh",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/VeteransCrisisLineDataDictionary/master/VeteransCrisisLineDataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "<p>Record-level data released on Freedom of Information Act (FOIA) Request 15-00242-F appeal.  Fields with value of b6 indicate data withheld in accordance with VHA Expert Determination methodology and/or VA Office of General Counsel direction.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/7sj2-ymyh/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "VA-VHA-10N-006",
+            "isPartOf": "VA-VHA-10N-013",
             "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
             "keyword": [
                 "crisis",
                 "foia",
@@ -19005,70 +19019,38 @@
                 "veteran",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/7sj2-ymyh",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-10N-006",
-            "description": "<p>Record-level data released on Freedom of Information Act (FOIA) Request 15-00242-F appeal.  Fields with value of b6 indicate data withheld in accordance with VHA Expert Determination methodology and/or VA Office of General Counsel direction.</p>",
-            "title": "Veterans Crisis Line calls FY2012 Record-Level Data",
-            "isPartOf": "VA-VHA-10N-013",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:042"
+            "systemOfRecords": "https://www.federalregister.gov/articles/2015/04/24/2015-09567/privacy-act-of-1974-system-of-records",
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
+            "theme": [
+                "Suicide Prevention"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/7sj2-ymyh/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
-            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/VeteransCrisisLineDataDictionary/master/VeteransCrisisLineDataDictionary.xlsx",
-            "systemOfRecords": "https://www.federalregister.gov/articles/2015/04/24/2015-09567/privacy-act-of-1974-system-of-records",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "theme": [
-                "Suicide Prevention"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
+            "title": "Veterans Crisis Line calls FY2012 Record-Level Data"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7su8-paki",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-08-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-20",
-            "keyword": [
-                "state",
-                "veterans",
-                "vetpop2023"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/7su8-paki",
             "description": "VetPop2023 top 10 states where Veterans reside in fiscal year 2024",
-            "title": "VetPop2023 Top 10 States: FY 2024",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19076,57 +19058,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7su8-paki/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7su8-paki/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7su8-paki/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7su8-paki/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7su8-paki/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7su8-paki/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7su8-paki/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7su8-paki/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7su8-paki/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/7su8-paki",
+            "issued": "2024-08-20",
+            "keyword": [
+                "state",
+                "veterans",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7su8-paki",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-20",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 Top 10 States: FY 2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7tmk-t8ud",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-02-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "korea",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "10c0ea18-87a2-4392-a56b-71fab0a465f1",
+            "dataQuality": true,
             "description": "<p>The spreadsheet of Korean War Veterans by State includes the total Korean War Veteran population for each state and broken out by age and gender. It also includes Korean War casualties by state from the Congressional Research Service.</p>",
-            "title": "Korean War Veterans by State",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19134,42 +19118,41 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "10c0ea18-87a2-4392-a56b-71fab0a465f1",
+            "issued": "2018-02-01",
+            "keyword": [
+                "korea",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7tmk-t8ud",
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
                 "and Operational Data"
-            ]
+            ],
+            "title": "Korean War Veterans by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7tvx-3vqk",
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
-            "identifier": "VA-OGC-012",
             "description": "<p>Authority to Solicit Gifts under 38 USC 8301</p>",
-            "title": "OGC Precedent Opinion 2-2015",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19178,41 +19161,42 @@
                     "title": "OGC Precedent Opinion 2-2015"
                 }
             ],
+            "identifier": "VA-OGC-012",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7tvx-3vqk",
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
+            "title": "OGC Precedent Opinion 2-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7uh3-s75z",
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
-            "identifier": "e75cf129-6c3c-4432-b4e0-0c07e6a4bfed",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Colorado FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19220,20 +19204,39 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "e75cf129-6c3c-4432-b4e0-0c07e6a4bfed",
+            "issued": "2018-10-29",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7uh3-s75z",
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
+            "title": "State Summary Colorado FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/7v23-r9tp",
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
+            "description": "<p>The National Item File (NIF) is used to uniquely identify products used in the supply chain. The Universal Product Number is placed as a bar code on products to enable users of the products to readily identify the product's characteristics.</p>",
+            "identifier": "VA-VHA-PL-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2005-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "bar code",
                 "item",
@@ -19243,61 +19246,40 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/7v23-r9tp",
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
-            "identifier": "VA-VHA-PL-001",
-            "description": "<p>The National Item File (NIF) is used to uniquely identify products used in the supply chain. The Universal Product Number is placed as a bar code on products to enable users of the products to readily identify the product's characteristics.</p>",
-            "title": "National Item File (NIF)",
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
+            "title": "National Item File (NIF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7w4m-xjv8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "benefits",
-                "services",
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
-            "identifier": "VA-OEI-OEI-160",
             "description": "<p>This reports shows the services and benefits the Department of Veterans Affairs provided in 1982.</p>",
-            "title": "Annual Report 1982",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19306,74 +19288,76 @@
                     "title": "Annual Report 1982"
                 }
             ],
+            "identifier": "VA-OEI-OEI-160",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "services",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7w4m-xjv8",
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
+            "title": "Annual Report 1982"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/7wja-85c3",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mark Guagliardo",
+                "hasEmail": "mailto:VANCVAS@va.gov"
+            },
+            "description": "To mark the 70th anniversary of the Korean War this data story recognizes the 6.8 million Veterans who served during the Korean War Era. It presents their age profile in 2020, documents their decreasing numbers, recognizes women who served, and includes an interactive map showing their locations by state. Finally, these and all Veterans are invited to apply for VA benefits and services.",
+            "identifier": "https://www.data.va.gov/api/views/7wja-85c3",
             "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-17",
             "keyword": [
                 "korean conflict",
                 "korean war",
                 "veteran population",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Mark Guagliardo",
-                "hasEmail": "mailto:VANCVAS@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/7wja-85c3",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-12-17",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/7wja-85c3",
-            "description": "To mark the 70th anniversary of the Korean War this data story recognizes the 6.8 million Veterans who served during the Korean War Era. It presents their age profile in 2020, documents their decreasing numbers, recognizes women who served, and includes an interactive map showing their locations by state. Finally, these and all Veterans are invited to apply for VA benefits and services.",
-            "title": "Korean War Veterans",
-            "programCode": [
-                "029:000"
-            ],
-            "license": "https://www.usa.gov/government-works"
+            "title": "Korean War Veterans"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7wpw-qnnz",
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
-            "identifier": "b755aac5-4ff5-4c8d-b276-59af3d600fd3",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Kansas FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19381,38 +19365,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "b755aac5-4ff5-4c8d-b276-59af3d600fd3",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7wpw-qnnz",
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
+            "title": "State Summary Kansas FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/7x7x-tk3t",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-23",
-            "keyword": [
-                "memorial benefits",
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
-            "identifier": "https://www.data.va.gov/api/views/7x7x-tk3t",
             "description": "Memorial Affairs: All Veterans who were interred in a National, State, Interior, or Military cemeteries, or Veterans who were interred in private cemeteries and requested headstones/markers from VA were included. Due to data unavailability, Veterans who only received Presidential Memorial Certificates or a flag were not included. National Cemetery Administration (NCA) provides memorial benefits including graves, markers, flags, medallions, and burial allowances.",
-            "title": "Veterans who used VA Memorial Benefits",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19420,61 +19402,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7x7x-tk3t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7x7x-tk3t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7x7x-tk3t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/7x7x-tk3t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7x7x-tk3t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7x7x-tk3t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/7x7x-tk3t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/7x7x-tk3t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/7x7x-tk3t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "State",
-            "license": "https://www.usa.gov/government-works",
+            "identifier": "https://www.data.va.gov/api/views/7x7x-tk3t",
+            "issued": "2021-02-19",
+            "keyword": [
+                "memorial benefits",
+                "veteran",
+                "veteran benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/7x7x-tk3t",
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
+            "title": "Veterans who used VA Memorial Benefits"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/83s9-pnfp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "female veterans",
-                "historic"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veteran Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/83s9-pnfp",
             "description": "NOTE: 2001-2013 enlisted totals include \"cadets-midshipmen\" so officer+enlisted=total.\nThis may not be the correct assumption, but the historical tables only have \"officer\" and \"enlisted\" totals.",
-            "title": "Female Active Duty Military Personnel, Officers and Enlisted, 1945-2015",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19482,58 +19465,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/83s9-pnfp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/83s9-pnfp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/83s9-pnfp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/83s9-pnfp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/83s9-pnfp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/83s9-pnfp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/83s9-pnfp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/83s9-pnfp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/83s9-pnfp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/83s9-pnfp",
+            "issued": "2019-10-24",
+            "keyword": [
+                "female veterans",
+                "historic"
+            ],
+            "landingPage": "https://www.data.va.gov/d/83s9-pnfp",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
+            "title": "Female Active Duty Military Personnel, Officers and Enlisted, 1945-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/86fh-pf4n",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "account",
-                "cpe"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joseph Enderle",
                 "hasEmail": "mailto:joseph.enderle@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-ORCH-3",
+            "dataQuality": true,
             "description": "<p>Web service proxy/wrapper for CP&amp;E capabilities/data. This interface will retrieve a Bill of Collection record from CP&amp;E and enable a CRM user to view the Bill information. Back office CRM users (primarily DCU Unit) require the ability to review Bills to respond to customer inquiries about Bills and Offsets. The interface will be triggered when a user attempts to query for a Bill using the Bill # (K#).</p>",
-            "title": "CP&E Account Adapters Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19542,45 +19525,42 @@
                     "title": "CP&E Account Adapters Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-3",
+            "issued": "2017-11-17",
+            "keyword": [
+                "account",
+                "cpe"
+            ],
+            "landingPage": "https://www.data.va.gov/d/86fh-pf4n",
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
+            "title": "CP&E Account Adapters Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Tech_Doc_for_Education_Recipients_by_State.doc",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-01-01T05:00:00Z/2011-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Datagov_2nd_qtr_FY11_EDU_recp_by_State.csv"
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
-            "identifier": "VA-VBA-EDU2011-009",
+            "dataQuality": true,
             "description": "<p>FY 2011 Education Recipients by State (Through the 2nd qtr. FY11). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2011(Through the 2nd qtr. FY11). State statistics may include individuals who used their education benefits in more than one state, therefore the total within this table may be different than the  total number of beneficiaries during the fiscal year.</p>",
-            "title": "FY 2011_Q2 Use of VA Education Benefits-Recipients by State",
-            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19588,65 +19568,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/86kq-vsua/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/86kq-vsua/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/86kq-vsua/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/86kq-vsua/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/86kq-vsua/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/86kq-vsua/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/86kq-vsua/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/86kq-vsua/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/86kq-vsua/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2011-009",
+            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Tech_Doc_for_Education_Recipients_by_State.doc",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Datagov_2nd_qtr_FY11_EDU_recp_by_State.csv"
+            ],
+            "temporal": "2011-01-01T05:00:00Z/2011-03-31T04:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2011_Q2 Use of VA Education Benefits-Recipients by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/86mf-smjg",
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
-            "identifier": "VA-OGC-042",
             "description": "<p>Presidential Memorandum \u2013 Do Not Pay List</p>",
-            "title": "OGC Precedent Opinion 6-2010",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19655,41 +19638,41 @@
                     "title": "OGC Precedent Opinion 6-2010"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "theme": [
+            "identifier": "VA-OGC-042",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/86mf-smjg",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "OGC Precedent Opinion 6-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/88at-dhx6",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "nebraska",
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
-            "identifier": "VA-OEI-OEI-114",
             "description": "<p>This is a summary of the programs and services provided by VA in Nebraska in fiscal year 2014.</p>",
-            "title": "State Summary:  Nebraska",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19698,44 +19681,45 @@
                     "title": "State Summary:  Nebraska"
                 }
             ],
+            "identifier": "VA-OEI-OEI-114",
+            "issued": "2017-07-26",
+            "keyword": [
+                "nebraska",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/88at-dhx6",
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
+            "title": "State Summary:  Nebraska"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/89zn-mnrq",
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
-            "identifier": "beecc052-d922-4c03-b5b7-b93c6a7cbbe6",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Georgia FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19743,102 +19727,99 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "beecc052-d922-4c03-b5b7-b93c6a7cbbe6",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/89zn-mnrq",
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
+            "title": "State Summary Georgia FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8aav-9d7v",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to help servicepersons adjust to civilian life after separation from military service, assist in the recruitment and retention of highly qualified personnel in the active and reserve components in the Armed Forces by providing education benefits, and to provide educational opportunities to the dependents of certain service members and veterans. Individuals who entered active duty after September 10, 2001 may be eligible for the Post-9/11 GI Bill. Individuals can use the Post-9/11 GI Bill after serving 90 days on active duty (excluding entry level and skill training). Only periods of active duty under title 10 will be used to establish eligibility for the Post 9/11 GI Bill. A high school diploma or equivalency certificate is always required for eligibility. Individuals who are eligible for the Montgomery GI Bill \u2013 Active Duty (chapter 30), the Montgomery GI Bill \u2013 Selected Reserve (chapter 1606), or the Reserve Educational Assistance Program (REAP) will have to make an irrevocable election to relinquish eligibility under one of those benefit programs to establish eligibility under the Post-9/11 GI Bill. The dependent children of a person who died in the line of duty while serving as a member of the Armed Forces may be eligible to use benefits under the Fry Scholarship provision of the Post-9/11 GI Bill. The spouse and/or child(ren) of a veteran or service member may be eligible for the Post 9/11 GI Bill if the veteran or service member transfers entitlement to those dependents. Eligibility to transfer entitlement to dependents is determined by the Department of Defense. This is not a complete list of eligibility requirements. For more information on the latest changes to the Post-9/11 GI Bill go to the VA web-site.</p>",
-            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE FY2019",
+            "identifier": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 028"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8aav-9d7v",
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
+            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:25"
             ],
-            "landingPage": "https://www.data.va.gov/d/8acn-szxg",
-            "issued": "2021-02-07",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-08",
-            "keyword": [
-                "veterans benefits covid claims backlog disability examinations"
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
-            "identifier": "https://www.data.va.gov/api/views/8acn-szxg",
             "description": "In response to an increased demand for insightful and timely data from Veterans and other stakeholders, the Veterans Benefits Administration (VBA) developed an interactive map that shows where  in-person medical examinations have resumed following COVID-19 lockdowns.",
-            "title": "VBA Compensation and Pension Medical Exams Resume",
+            "identifier": "https://www.data.va.gov/api/views/8acn-szxg",
+            "issued": "2021-02-07",
+            "keyword": [
+                "veterans benefits covid claims backlog disability examinations"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8acn-szxg",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-02-08",
             "programCode": [
                 "029:003"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VBA Compensation and Pension Medical Exams Resume"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8auz-xxqs",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2021-01-29",
-            "temporal": "2013-11-01T04:00:00Z/2013-11-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-29",
-            "keyword": [
-                "life insurance policies",
-                "vgli",
-                "vgli enrollment 2013"
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
-            "identifier": "https://www.data.va.gov/api/views/8auz-xxqs",
+            "dataQuality": true,
             "description": "VBA- Insurance Lob- VGLI Enrollment by State 11-30-2013.\n\n* Report run on 11/27/2013\n** Includes all records with an Active and Pre-Lapse status",
-            "title": "VGLI Enrollment by state 2013-11-30",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19846,121 +19827,152 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8auz-xxqs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8auz-xxqs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8auz-xxqs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8auz-xxqs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8auz-xxqs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8auz-xxqs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8auz-xxqs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8auz-xxqs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8auz-xxqs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "systemOfRecords": "VA-VBA-INS2014-006",
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/8auz-xxqs",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2021-01-29",
+            "keyword": [
+                "life insurance policies",
+                "vgli",
+                "vgli enrollment 2013"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8auz-xxqs",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-01-29",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "systemOfRecords": "VA-VBA-INS2014-006",
+            "temporal": "2013-11-01T04:00:00Z/2013-11-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VGLI Enrollment by state 2013-11-30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/8c55-ivqr",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary North Carolina FY2023",
+            "identifier": "https://www.data.va.gov/api/views/8c55-ivqr",
             "issued": "2024-06-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "north carolina"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/8c55-ivqr",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/8c55-ivqr",
-            "description": "NCVAS State Summary North Carolina FY2023",
-            "title": "NCVAS State Summary North Carolina FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary North Carolina FY2023"
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
+                "fn": "Thomas.elwell@va.gov",
+                "hasEmail": "mailto:Thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Benefits for Survivors of Filipino Veterans</p>",
+            "identifier": "VA-VBA-MEDIAPUB-040",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2008-10-01T04:00:00Z",
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
-                "fn": "Thomas.elwell@va.gov",
-                "hasEmail": "mailto:Thomas.elwell@va.gov"
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
-            "identifier": "VA-VBA-MEDIAPUB-040",
-            "description": "<p>Benefits for Survivors of Filipino Veterans</p>",
-            "title": "Benefits for Survivors of Filipino Veterans",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2008-10-01T04:00:00Z/2008-10-01T04:00:00Z",
             "theme": [
                 "General Benefit Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Benefits for Survivors of Filipino Veterans"
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
-            "temporal": "2015-05-01T04:00:00Z/2015-05-01T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/health/docs/15_May_2015_Public_Data_Pending.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 May 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-106",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -19974,71 +19986,43 @@
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
-            "identifier": "VA-VHA-OIA-106",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 May 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/15_May_2015_Public_Data_Pending.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 May 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-05-01T04:00:00Z/2015-05-01T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 May 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8e72-8evv",
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
-            "identifier": "https://www.data.va.gov/api/views/8e72-8evv",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to help servicepersons adjust to civilian life after separation from military service, assist in the recruitment and retention of highly qualified personnel in the active and reserve components in the Armed Forces by providing education benefits, and to provide educational opportunities to the dependents of certain service members and veterans. Individuals who entered active duty after September 10, 2001 may be eligible for the Post-9/11 GI Bill. Individuals can use the Post-9/11 GI Bill after serving 90 days on active duty (excluding entry level and skill training). Only periods of active duty under title 10 will be used to establish eligibility for the Post 9/11 GI Bill. A high school diploma or equivalency certificate is always required for eligibility. Individuals who are eligible for the Montgomery GI Bill \u2013 Active Duty (chapter 30), the Montgomery GI Bill \u2013 Selected Reserve (chapter 1606), or the Reserve Educational Assistance Program (REAP) will have to make an irrevocable election to relinquish eligibility under one of those benefit programs to establish eligibility under the Post-9/11 GI Bill. The dependent children of a person who died in the line of duty while serving as a member of the Armed Forces may be eligible to use benefits under the Fry Scholarship provision of the Post-9/11 GI Bill. The spouse and/or child(ren) of a veteran or service member may be eligible for the Post 9/11 GI Bill if the veteran or service member transfers entitlement to those dependents. Eligibility to transfer entitlement to dependents is determined by the Department of Defense. This is not a complete list of eligibility requirements. For more information on the latest changes to the Post-9/11 GI Bill go to the VA web-site.</p>",
-            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE MAR2019",
-            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20046,65 +20030,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8e72-8evv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8e72-8evv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8e72-8evv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8e72-8evv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8e72-8evv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8e72-8evv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8e72-8evv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8e72-8evv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8e72-8evv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/8e72-8evv",
+            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 028"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8e72-8evv",
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
+            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fedshirevets.gov/hire/hrp/reports/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "rights": "Public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-10-01T04:00:00Z/2012-10-01T04:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "employment",
-                "federal executive branch",
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
-            "identifier": "VA-OEI-OEI-020",
-            "description": "<p>These quick facts use data from the 2011 Employment of Veterans in the Federal Executive Branch to compare Veteran employment in the Federal Government by agency, occupation, and level of disability. Three of the four charts focus on new hires.</p>",
-            "title": "Employment of Veterans in the Federal Executive Branch",
+            "dataQuality": true,
+            "describedBy": "https://www.fedshirevets.gov/hire/hrp/reports/EmploymentOfVets-FY12.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>These quick facts use data from the 2011 Employment of Veterans in the Federal Executive Branch to compare Veteran employment in the Federal Government by agency, occupation, and level of disability. Three of the four charts focus on new hires.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20113,45 +20096,46 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.fedshirevets.gov/hire/hrp/reports/EmploymentOfVets-FY12.pdf",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-020",
+            "issued": "2017-07-26",
+            "keyword": [
+                "employment",
+                "federal executive branch",
+                "veterans"
+            ],
+            "landingPage": "https://www.fedshirevets.gov/hire/hrp/reports/",
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
+            "rights": "Public",
+            "temporal": "2011-10-01T04:00:00Z/2012-10-01T04:00:00Z",
             "theme": [
                 "Data on Veterans"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Employment of Veterans in the Federal Executive Branch"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8fry-twrr",
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
-            "identifier": "https://www.data.va.gov/api/views/8fry-twrr",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAMS to provide, through purchase and/or fabrication, prosthetic and related appliances, equipment and services to eligible veterans so that they may live and work as productive citizens. Veterans eligible for prosthetic services are service-connected veterans seeking care for a service-connected disability; veterans with compensable service-connected disabilities generally rated 10 percent or more; former prisoners of war, veterans discharged or released from active military service for a disability that was incurred or aggravated in the line of duty, and veterans who are in receipt of Section 1151 benefits; veterans who are in receipt of increased pension based on a need of regular aid and attendance or by reason of being permanently housebound; veterans who have annual income and net worth below the \"means test\" threshold; all other veterans who are not required to pay a copayment for their care, i.e., veterans of the Mexican border period and World War I, compensated zero (0) percent service-connected veterans who are receiving statutory awards, veterans exposed to a toxic substance, radiation or environmental hazard (limited to certain disabilities); and veterans who must pay a copayment for their care. Ineligible veterans are nonservice-connected veterans residing or sojourning in foreign lands.</p>",
-            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES OCT2018",
-            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20159,58 +20143,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8fry-twrr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8fry-twrr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8fry-twrr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8fry-twrr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8fry-twrr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8fry-twrr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8fry-twrr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8fry-twrr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8fry-twrr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/8fry-twrr",
+            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 116"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8fry-twrr",
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
+            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8g9x-p9qy",
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
-            "identifier": "https://www.data.va.gov/api/views/8g9x-p9qy",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located.</p>",
-            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS FEB2019",
-            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20218,109 +20202,112 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8g9x-p9qy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8g9x-p9qy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8g9x-p9qy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8g9x-p9qy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8g9x-p9qy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8g9x-p9qy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8g9x-p9qy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8g9x-p9qy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8g9x-p9qy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/8g9x-p9qy",
+            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 114"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8g9x-p9qy",
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
+            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2008-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-23",
-            "keyword": [
-                "benefits fact sheet",
-                "general benefit information",
-                "va benefits",
-                "va fact sheet"
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
-            "identifier": "VA-VBA-MEDIAPUB-003",
+            "dataQuality": true,
             "description": "<p>Fact sheet to guide Veterans and Beneficiaries on the benefits available to them.</p>",
-            "title": "VA Benefits for Veterans Entering the Physical Evaluation Board",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.benefits.va.gov/BENEFITS/factsheets.asp",
-                    "description": "https://www.benefits.va.gov/BENEFITS/factsheets.asp\n",
                     "@type": "dcat:Distribution",
+                    "description": "https://www.benefits.va.gov/BENEFITS/factsheets.asp\n",
+                    "downloadURL": "https://www.benefits.va.gov/BENEFITS/factsheets.asp",
+                    "mediaType": "text/html",
                     "title": "VA Benefits for Veterans Entering the Physical Evaluation Board"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-MEDIAPUB-003",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits fact sheet",
+                "general benefit information",
+                "va benefits",
+                "va fact sheet"
+            ],
+            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-23",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2008-10-01T04:00:00Z/2008-10-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Benefits for Veterans Entering the Physical Evaluation Board"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/8gsu-4add",
-            "issued": "2023-06-13",
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
-            "identifier": "https://www.data.va.gov/api/views/8gsu-4add",
             "description": "FY2021 VA Health and Benefits and FY2021 VA Education data provided by the National Center for Veterans Statistics and Analysis, published in 2023.",
-            "title": "FY 2021_NCVAS Healthcare and Benefits Data For State Summaries",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20328,57 +20315,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8gsu-4add/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8gsu-4add/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8gsu-4add/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8gsu-4add/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8gsu-4add/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8gsu-4add/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8gsu-4add/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8gsu-4add/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8gsu-4add/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/8gsu-4add",
+            "issued": "2023-06-13",
+            "landingPage": "https://www.data.va.gov/d/8gsu-4add",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Healthcare and Benefits Data For State Summaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8ie7-cs3f",
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
-            "identifier": "https://www.data.va.gov/api/views/8ie7-cs3f",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist wartime veterans in need whose non-service- connected disabilities are permanent and total preventing them from following a substantially gainful occupation. A Veteran who meets the wartime service requirements is potential eligible if he/she is: \u2022 permanently and totally disabled for reasons not necessarily due to service, \u2022 age 65 or older, or \u2022 is presumed to be totally and permanently disabled for pension purposes because: o he/she is a patient in a nursing home for long-term care due to a disability, or o being disabled, as determined by the Commissioner of Social Security (SS) for purposes of any benefits administered by the Commissioner, such as SS disability benefits or Supplemental Security Income. Income restrictions are prescribed in 38 U.S.C. 1521. Pension is not payable to those whose estates are so large that it is reasonable they use the estate for maintenance. A Veteran meets wartime service requirements if he/she served: \u2022 a total of 90 days or more during one or more periods of war; \u2022 90 or more consecutive days that began or ended during a period of war; or \u2022 for any length of time during a period of war if he/she was discharged or released for a service-connected disability. Veterans entering service after September 7, 1980, must also meet the minimum active duty requirement of 24 months of continuous service or the full period to which the Veteran was called to active duty. (38 U.S.C.5303(A)).</p>",
-            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS NOV2018",
-            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20386,66 +20370,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8ie7-cs3f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8ie7-cs3f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8ie7-cs3f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8ie7-cs3f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8ie7-cs3f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8ie7-cs3f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8ie7-cs3f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8ie7-cs3f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8ie7-cs3f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/8ie7-cs3f",
+            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 104"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8ie7-cs3f",
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
+            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS NOV2018"
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
-            "identifier": "VA-VBA-ABR2012-049",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Adapted Housing Grants and Direct Loans During Fiscal Year 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20453,74 +20433,77 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-049",
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
+            "title": "Adapted Housing Grants and Direct Loans During Fiscal Year 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/8jnp-dq5n",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "hawaii",
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
-            "identifier": "https://www.data.va.gov/api/views/8jnp-dq5n",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Hawaii",
+            "identifier": "https://www.data.va.gov/api/views/8jnp-dq5n",
+            "issued": "2021-08-26",
+            "keyword": [
+                "hawaii",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8jnp-dq5n",
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
+            "title": "State Summaries_Hawaii"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8jz9-ru8d",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "puerto rico",
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
-            "identifier": "VA-OEI-OEI-125",
             "description": "<p>This is a summary of the programs and services provided by VA in Puerto Rico in fiscal year 2014.</p>",
-            "title": "State Summary:  Puerto Rico",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20529,44 +20512,44 @@
                     "title": "State Summary:  Puerto Rico"
                 }
             ],
+            "identifier": "VA-OEI-OEI-125",
+            "issued": "2017-07-26",
+            "keyword": [
+                "puerto rico",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8jz9-ru8d",
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
+            "title": "State Summary:  Puerto Rico"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8m2t-gni8",
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
-            "identifier": "VA-OM-OM-124",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT DEC 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20574,42 +20557,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-124",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8m2t-gni8",
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
+            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT DEC 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8ng6-caq7",
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
-            "identifier": "https://www.data.va.gov/api/views/8ng6-caq7",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE JAN2019",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20617,61 +20600,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8ng6-caq7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8ng6-caq7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8ng6-caq7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8ng6-caq7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8ng6-caq7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8ng6-caq7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8ng6-caq7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8ng6-caq7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8ng6-caq7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/8ng6-caq7",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8ng6-caq7",
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
+            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8pfk-8tyt",
             "bureauCode": [
                 "029:40"
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
-            "identifier": "fb32ae5d-2a09-4b73-8d43-9106cc8be5ef",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Kansas FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20679,38 +20663,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "fb32ae5d-2a09-4b73-8d43-9106cc8be5ef",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8pfk-8tyt",
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
+            "title": "State Summary Kansas FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/ogc/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "This is a public-facing web site currently accessible through standard web browsing methods",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-08-01T04:00:00Z/2015-08-01T04:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "web site"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Hogan",
                 "hasEmail": "mailto:OGCOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-001",
+            "dataQuality": true,
             "description": "<p>The public-facing web site for the Office of General Counsel</p>",
-            "title": "OGC Web Site",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20719,46 +20703,45 @@
                     "title": "OGC Website"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OGC-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "web site"
+            ],
+            "landingPage": "https://www.va.gov/ogc/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "This is a public-facing web site currently accessible through standard web browsing methods",
+            "temporal": "2014-08-01T04:00:00Z/2015-08-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OGC Web Site"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8rjg-7kdw",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "mississippi",
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
-            "identifier": "VA-OEI-OEI-111",
             "description": "<p>This is a summary of the programs and services provided by VA in Mississippi in fiscal year 2014</p>",
-            "title": "State Summary:  Mississippi",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20767,51 +20750,45 @@
                     "title": "State Summary:  Mississippi"
                 }
             ],
+            "identifier": "VA-OEI-OEI-111",
+            "issued": "2017-07-26",
+            "keyword": [
+                "mississippi",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8rjg-7kdw",
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
+            "title": "State Summary:  Mississippi"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_April_2012.CSV",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-04-01T04:00:00Z/2012-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program_April_2012.doc"
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
-            "identifier": "VA-VBA-INS2012-004",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 04/30/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Face Amount of Life Insurance Coverage by Program by State 2012/04/30",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20819,51 +20796,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8s4q-e3ex/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8s4q-e3ex/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8s4q-e3ex/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8s4q-e3ex/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8s4q-e3ex/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8s4q-e3ex/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8s4q-e3ex/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8s4q-e3ex/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8s4q-e3ex/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-004",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_April_2012.CSV",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program_April_2012.doc"
+            ],
+            "temporal": "2012-04-01T04:00:00Z/2012-04-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Face Amount of Life Insurance Coverage by Program by State 2012/04/30"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN23FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 23 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-095",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -20879,53 +20891,54 @@
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
-            "identifier": "VA-VHA-OIA-095",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 23",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN23FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 23 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 23"
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
+            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/NepecPtsdDataDictionary/master/NepecPtsdDataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "<p>VAMC-level statistics on the prevalence, mental health utilization, non-mental health utilization, mental health workload, and psychological testing of Veterans with a possible or confirmed diagnosis of mental illness.   Information prepared by the VA Northeast Program Evaluation Center (NEPEC) for fiscal year 2015.  <b> This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/8stm-cdgw/text/plain",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "VA-VHA-10N-010",
             "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-29",
             "keyword": [
                 "2015",
                 "health",
@@ -20936,67 +20949,38 @@
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
-            "identifier": "VA-VHA-10N-010",
-            "description": "<p>VAMC-level statistics on the prevalence, mental health utilization, non-mental health utilization, mental health workload, and psychological testing of Veterans with a possible or confirmed diagnosis of mental illness.   Information prepared by the VA Northeast Program Evaluation Center (NEPEC) for fiscal year 2015.  <b> This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>",
-            "title": "VA National Mental Health Statistics - 2015",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:042"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/8stm-cdgw/text/plain",
-                    "mediaType": "text/plain"
-                }
-            ],
-            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/NepecPtsdDataDictionary/master/NepecPtsdDataDictionary.xlsx",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
             "theme": [
                 "PTSD",
                 "Mental Health"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA National Mental Health Statistics - 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8suv-9mbn",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "california"
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
-            "identifier": "VA-OEI-OEI-174",
             "description": "<p>This summary describes the programs and services VA provided in California in fiscal year 2015.</p>",
-            "title": "State Summary California",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21005,47 +20989,42 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-174",
+            "issued": "2017-07-26",
+            "keyword": [
+                "california"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8suv-9mbn",
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
+            "title": "State Summary California"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/docs/Datagov/DataGov_CnP_Technical_Notes.doc",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/vetdata/docs/Datagov/DataGov_CnP_Technical_Notes.doc"
-            ],
-            "keyword": [
-                "disability compensation",
-                "pension",
-                "veterans"
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
-            "identifier": "VA-VBA-CP2009-001",
+            "dataQuality": true,
             "description": "<p>The Compensation and Pension by County dataset is a count of the number of veterans receiving disability compensation or pension payments from the Department of Veterans Affairs. The data is reported at the county level, by age group and by percent disability rating for each state plus recipients in Guam, Philippines and Puerto Rico.</p>",
-            "title": "FY09 Compensation and Pension Recipients by County",
-            "isPartOf": "VA-VBA-MASTER-COMPENSATIONPENSION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21053,65 +21032,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8t2x-da5t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8t2x-da5t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8t2x-da5t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8t2x-da5t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8t2x-da5t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8t2x-da5t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8t2x-da5t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8t2x-da5t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8t2x-da5t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-CP2009-001",
+            "isPartOf": "VA-VBA-MASTER-COMPENSATIONPENSION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "disability compensation",
+                "pension",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/docs/Datagov/DataGov_CnP_Technical_Notes.doc",
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
+                "https://www.va.gov/vetdata/docs/Datagov/DataGov_CnP_Technical_Notes.doc"
+            ],
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Section 11. Social Insurance and Human Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY09 Compensation and Pension Recipients by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8tej-sktb",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-01-01T05:00:00Z/2015-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "debt referrals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.SOukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-123",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT JAN 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21119,41 +21102,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-123",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8tej-sktb",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-01-01T05:00:00Z/2015-01-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT JAN 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8tjq-9c7g",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-05-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "dependency and indemnity compensation for service connected death",
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
-            "identifier": "2691062e-9fb2-40aa-ac21-e235e2311df7",
+            "dataQuality": true,
             "description": "<p>This infographic shows not only service members who died in battle, but all those who have served and died since their military service.  It also highlights the memorial benefits VA provides to those who have served and died.</p>",
-            "title": "Veteran Deaths During and After Military Service (as of 9/30/2017)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21161,38 +21145,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "2691062e-9fb2-40aa-ac21-e235e2311df7",
+            "issued": "2019-05-31",
+            "keyword": [
+                "dependency and indemnity compensation for service connected death",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8tjq-9c7g",
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
+            "title": "Veteran Deaths During and After Military Service (as of 9/30/2017)"
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
-                "mortality",
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
-            "identifier": "VA-OEI-OEI-231",
+            "dataQuality": true,
             "description": "<p>This report generates estimates of mortality rates and life expectancy for Veterans for ages 20 to 85, in the 10 to 15 year periods population. The report also estimates the education and income differentials in life expectancy for Veterans in 2011 to 2014</p>",
-            "title": "Veteran Mortality Report",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21201,46 +21185,45 @@
                     "title": "Mortality Rates and Life Expectancy of Veterans"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-231",
+            "issued": "2017-07-26",
+            "keyword": [
+                "mortality",
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
+            "title": "Veteran Mortality Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8ue3-x4fh",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "connecticut",
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
-            "identifier": "VA-OEI-OEI-092",
             "description": "<p>This is a summary of the programs and services VA provided in Connecticut in fiscal year 2014.</p>",
-            "title": "State Summary:  Connecticut",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21249,45 +21232,44 @@
                     "title": "State Summary:  Connecticut"
                 }
             ],
+            "identifier": "VA-OEI-OEI-092",
+            "issued": "2017-07-26",
+            "keyword": [
+                "connecticut",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8ue3-x4fh",
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
+            "title": "State Summary:  Connecticut"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8uia-zhs2",
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
-            "identifier": "https://www.data.va.gov/api/views/8uia-zhs2",
             "description": "",
-            "title": "Table 4 - U. S. Veterans Life Table for Female 1990-1999",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21295,57 +21277,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8uia-zhs2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8uia-zhs2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8uia-zhs2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8uia-zhs2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8uia-zhs2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8uia-zhs2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8uia-zhs2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8uia-zhs2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8uia-zhs2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/8uia-zhs2",
+            "issued": "2023-04-18",
+            "keyword": [
+                "death rate",
+                "life expectancy",
+                "life table"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8uia-zhs2",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Table 4 - U. S. Veterans Life Table for Female 1990-1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8v4h-xzam",
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
-            "identifier": "https://www.data.va.gov/api/views/8v4h-xzam",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE OCT2018",
-            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21353,63 +21338,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8v4h-xzam/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8v4h-xzam/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8v4h-xzam/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8v4h-xzam/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8v4h-xzam/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8v4h-xzam/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8v4h-xzam/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8v4h-xzam/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8v4h-xzam/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/8v4h-xzam",
+            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "issued": "2019-03-20",
+            "keyword": [
+                "cdfa 64.124"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8v4h-xzam",
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
+            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8vam-eukt",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2000-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "va facilities"
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
-            "identifier": "VA-OEI-OEI-059",
+            "dataQuality": true,
             "description": "<p>Maps are organized by state and depict the Veteran population using VetPop2011 data as of 9/30/2013 and VA facilities using Veteran Affairs Site Tracking (VAST) data as of FY14Q1.</p>",
-            "title": "VA Facilities by Congressional District (FY2011): Overview",
-            "programCode": [
-                "029:006"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21418,74 +21402,69 @@
                     "title": "xls"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-059",
+            "issued": "2017-07-26",
+            "keyword": [
+                "va facilities"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8vam-eukt",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:006"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "public",
+            "temporal": "2000-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "facilities"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Facilities by Congressional District (FY2011): Overview"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8vmb-86pa",
-            "issued": "2023-07-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-28",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Maryland FY2021",
+            "identifier": "https://www.data.va.gov/api/views/8vmb-86pa",
+            "issued": "2023-07-03",
             "keyword": [
                 "fy2021 data",
                 "maryland",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/8vmb-86pa",
+            "landingPage": "https://www.data.va.gov/d/8vmb-86pa",
+            "modified": "2024-05-28",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Maryland FY2021",
             "title": "NCVAS State Summary Maryland FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_CD_11-13-09_GDX.csv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_CD_11-13-09_GDX.csv"
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
-            "identifier": "VA-VBA-INS2009-001",
+            "dataQuality": true,
             "description": "<p>2009 Veteran life insurance expenditures by congressional district.  Expenditures represented the actual disbursements from Insurance's Award and Inforce systems.</p>",
-            "title": "2009 Veterans' Insurance Expenditure by Congressional District",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21493,67 +21472,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8vq9-n2kh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8vq9-n2kh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8vq9-n2kh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8vq9-n2kh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8vq9-n2kh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8vq9-n2kh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8vq9-n2kh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8vq9-n2kh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8vq9-n2kh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2009-001",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "insurance",
+                "veteran"
+            ],
+            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_CD_11-13-09_GDX.csv",
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
+                "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_CD_11-13-09_GDX.csv"
+            ],
+            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2009 Veterans' Insurance Expenditure by Congressional District"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8vy2-ejkq",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-08-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-20",
-            "keyword": [
-                "branch of service",
-                "female veterans",
-                "vetpop2023",
-                "women veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/8vy2-ejkq",
             "description": "VetPop2023 branch of service distribution of female Veterans in fiscal years 2024 and 2053.",
-            "title": "VetPop2023 Branch Distribution of Female Veterans: FY 2024 and 2053",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21561,61 +21542,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8vy2-ejkq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8vy2-ejkq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8vy2-ejkq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8vy2-ejkq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8vy2-ejkq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8vy2-ejkq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8vy2-ejkq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8vy2-ejkq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8vy2-ejkq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/8vy2-ejkq",
+            "issued": "2024-08-20",
+            "keyword": [
+                "branch of service",
+                "female veterans",
+                "vetpop2023",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8vy2-ejkq",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-20",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 Branch Distribution of Female Veterans: FY 2024 and 2053"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VBA/blob/master/PolicyholdersbyProgrambyStateOctober2013.xls",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-10-01T04:00:00Z/2013-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-09",
-            "keyword": [
-                "2013",
-                "life insurance policies",
-                "policy holders",
-                "policy holders by state"
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
-            "identifier": "VA-VBA-INS2014-002",
+            "dataQuality": true,
             "description": "<p>VBA- Insurance Lob- Policy Holders by program by State- October 2013.</p>",
-            "title": "Policy Holders by Program by State- October  2013",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21624,57 +21605,46 @@
                     "title": "xls"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2014-002",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "2013",
+                "life insurance policies",
+                "policy holders",
+                "policy holders by state"
+            ],
+            "landingPage": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VBA/blob/master/PolicyholdersbyProgrambyStateOctober2013.xls",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-11-09",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2013-10-01T04:00:00Z/2013-10-31T04:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Policy Holders by Program by State- October  2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8w9f-mpv7",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-11-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-09-01",
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
-            "identifier": "https://www.data.va.gov/api/views/8w9f-mpv7",
             "description": "A subset of the FY13 National Veteran Health Equity Report, filtered by mental illness.\n\nThe National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. Specifically, this report is designed to provide basic comparative information on the sociodemographics, utilization patterns and rates of diagnosed health conditions among the groups over which the VHA Office of Health Equity (OHE) has responsibility with respect to monitoring, evaluating and acting on identified disparities in access, use, care, quality and outcomes. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.",
-            "title": "VA-OHE-NVHER-FY13-Diagnoses-Mental-Illness",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21682,57 +21652,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8w9f-mpv7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8w9f-mpv7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8w9f-mpv7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8w9f-mpv7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8w9f-mpv7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8w9f-mpv7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8w9f-mpv7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8w9f-mpv7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8w9f-mpv7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/8w9f-mpv7",
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
+            "landingPage": "https://www.data.va.gov/d/8w9f-mpv7",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-09-01",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA-OHE-NVHER-FY13-Diagnoses-Mental-Illness"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8waz-aacf",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-14",
-            "keyword": [
-                "cfda 64 100"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:Annette.Brown2@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/8waz-aacf",
+            "dataQuality": true,
             "description": "<p>VBA PROGRAM BENEFITS for Automobiles and Adaptive Equipment for Certain Disabled Veterans and Members of the Armed Forces. Veterans with honorable service and servicepersons on duty having a service-connected disability due to loss or permanent loss of use of one or both feet, one or both hands, or a permanent impairment of vision of both eyes to a prescribed degree. For adaptive equipment only, eligibility also exists if there is service-connected ankylosis of one or both knees or one or both hips. Personnel on active duty also qualify under the same criteria as veterans. Uses &amp; Use Restrictions:  Assistance toward purchase of an automobile or other conveyance is a one-time payment only. Necessary adaptive equipment may be furnished, repaired, replaced, or reinstalled on a conveyance which may be purchased with assistance or any other conveyance subsequently or previously acquired. Adaptive equipment will be provided for no more than two conveyances during any four-year period unless one of those two vehicles becomes unavailable to the veteran.</p>",
-            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE DEC2018",
-            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21740,60 +21724,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8waz-aacf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8waz-aacf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8waz-aacf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8waz-aacf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8waz-aacf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8waz-aacf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8waz-aacf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8waz-aacf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8waz-aacf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/8waz-aacf",
+            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 100"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8waz-aacf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-14",
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
+            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8xsv-dkdr",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "e-government"
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
-            "identifier": "VA-OIT-OIT-021",
             "description": "<p>This report describes VA\u2019s accomplishments inimplementing the requirements of the E-Government Act of 2002, Section 202(g)and the Open Government Directive dated December 8, 2009.</p>",
-            "title": "2010 E-Government Act Report",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21802,43 +21786,42 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OIT-OIT-021",
+            "issued": "2017-07-26",
+            "keyword": [
+                "e-government"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8xsv-dkdr",
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
+            "title": "2010 E-Government Act Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cfm.va.gov/til/sepsNTG.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Public access for VA construction standards utilized within the building industry.",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2012-01-01T05:00:00Z/2014-05-01T04:00:00Z",
-            "modified": "2024-08-26",
-            "keyword": [
-                "construction management",
-                "construction standards"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elizabeth Bunn",
                 "hasEmail": "mailto:Elizabeth.Bunn@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-CFM-TIL-009",
+            "dataQuality": true,
             "description": "<p>The Office of Construction &amp; Facilities Management (CFM) is located in Washington DC with regional offices in Silver Spring MD, North Chicago IL, and Mare Island (Vallejo) CA. CFM provides design, major construction, and lease project management, design and construction standards, and historic preservation services and expertise to the Department of Veterans Affairs to delivery high quality and cost effective facilities in support of our Nation's veterans.</p>",
-            "title": "Construction and Facilities Management Technical Information Library (TIL)",
-            "programCode": [
-                "029:090"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21847,88 +21830,86 @@
                     "title": "Construction and Facilities Management Technical Information Library (TIL)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-CFM-TIL-009",
+            "issued": "2017-07-26",
+            "keyword": [
+                "construction management",
+                "construction standards"
+            ],
+            "landingPage": "https://www.cfm.va.gov/til/sepsNTG.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:090"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Public access for VA construction standards utilized within the building industry.",
+            "temporal": "2012-01-01T05:00:00Z/2014-05-01T04:00:00Z",
             "theme": [
                 "Construction Project Standards and Management Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Construction and Facilities Management Technical Information Library (TIL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/warms/",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "vba benefits",
-                "warms",
-                "warms reference"
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
-            "identifier": "VA-VBA-INFO-022",
+            "dataQuality": true,
             "description": "<p>The Web Automated Reference Manual System (WARMS) includes manuals, directives, handbooks, Title 38 Code of Federal Regulations and more. The publications provide information about the Department of Veterans Affairs benefits policies.</p>",
-            "title": "Web Automated Reference Manual System (WARMS) - VBA",
+            "identifier": "VA-VBA-INFO-022",
             "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "vba benefits",
+                "warms",
+                "warms reference"
+            ],
+            "landingPage": "https://www.benefits.va.gov/warms/",
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
+            "title": "Web Automated Reference Manual System (WARMS) - VBA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8zhc-knsi",
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
-            "identifier": "https://www.data.va.gov/api/views/8zhc-knsi",
             "description": "VetPop2023 projection of living Veterans by gender and race/ethnicity at the national level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 National Race/Ethnicity Data, 3L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21936,57 +21917,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8zhc-knsi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8zhc-knsi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8zhc-knsi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/8zhc-knsi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8zhc-knsi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8zhc-knsi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/8zhc-knsi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/8zhc-knsi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/8zhc-knsi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/8zhc-knsi",
+            "issued": "2024-09-05",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8zhc-knsi",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 National Race/Ethnicity Data, 3L"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/8zsn-5ma7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "alabama",
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
-            "identifier": "VA-OEI-OEI-086",
             "description": "<p>This summary describes the services and benefits provided by VA in Alabama.</p>",
-            "title": "State Summary:  Alabama",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21995,29 +21978,58 @@
                     "title": "State Summary:  Alabama"
                 }
             ],
+            "identifier": "VA-OEI-OEI-086",
+            "issued": "2017-07-26",
+            "keyword": [
+                "alabama",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/8zsn-5ma7",
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
+            "title": "State Summary:  Alabama"
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
-            "temporal": "2016-03-15T04:00:00Z/2016-03-15T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR42_032016_Pending_and_EWL_Biweekly_Desired_Date_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 March 2016"
+                }
             ],
+            "identifier": "VA-VHA-OIA-736",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -22031,71 +22043,42 @@
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
-            "identifier": "VA-VHA-OIA-736",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 March 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR42_032016_Pending_and_EWL_Biweekly_Desired_Date_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 March 2016"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2016-03-15T04:00:00Z/2016-03-15T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 March 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/938k-49h7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-10-01T04:00:00Z",
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
-            "identifier": "VA-OEI-OEI-083",
             "description": "<p>This report uses data from the 2013 American Community Survey to compare the demographic and socioeconomic characteristics of minority Veterans and minority non-Veterans.</p>",
-            "title": "2013 Minority Veterans Report",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22104,24 +22087,54 @@
                     "title": "http://www.va.gov/vetdata/docs/SpecialReports/Minority_Veterans_2013.pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-083",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/938k-49h7",
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
+            "temporal": "2012-10-01T04:00:00Z/2013-10-01T04:00:00Z",
             "theme": [
                 "Use of Benefits and Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2013 Minority Veterans Report"
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
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/GDX/GDX_FY13.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-038",
             "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -22135,48 +22148,48 @@
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
-            "identifier": "VA-OEI-OEI-038",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2013",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/GDX/GDX_FY13.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2013"
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
+                    "downloadURL": "https://www.data.va.gov/download/9478-kz49/text/plain",
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
@@ -22195,50 +22208,49 @@
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
-                    "downloadURL": "https://www.data.va.gov/download/9478-kz49/text/plain",
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
-            "landingPage": "https://www.data.va.gov/d/94b9-ak44",
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
+                    "downloadURL": "https://www.data.va.gov/download/94b9-ak44/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/94b9-ak44",
             "issued": "2020-08-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-10-01/2017-09-30",
-            "modified": "2021-06-24",
             "keyword": [
                 "2017",
                 "analytics",
@@ -22259,69 +22271,37 @@
                 "veterans health administration",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Sail Operations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/94b9-ak44",
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
-            "identifier": "https://www.data.va.gov/api/views/94b9-ak44",
-            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
-            "title": "SAIL FY2017 Hospital Performance - All Facilities",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/94b9-ak44/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
-            "language": [
-                "en-US"
-            ]
+            "temporal": "2016-10-01/2017-09-30",
+            "title": "SAIL FY2017 Hospital Performance - All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Datagov_End_of_Feb_FY11_EDU_recp_by_Training_Type.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Datagov_End_of_Feb_FY11_EDU_recp_by_Training_Type.csv"
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
-            "identifier": "VA-VBA-EDU2011-004",
+            "dataQuality": true,
             "description": "<p>FY 11 Education Recipients by training type  and VA Education Benefit Program (Through Feb. FY11). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2011(Through the Feb. FY11). Training type statistics may include individuals who used their education benefits in more than one training type, therefore the total within this table may be different than the total number of beneficiaries during the fiscal year.</p>",
-            "title": "FY 11 Feb Education Recipients by Training Type and VA Education Benefit Program",
-            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22329,65 +22309,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/94c5-ux3z/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/94c5-ux3z/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/94c5-ux3z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/94c5-ux3z/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/94c5-ux3z/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/94c5-ux3z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/94c5-ux3z/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/94c5-ux3z/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/94c5-ux3z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2011-004",
+            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Datagov_End_of_Feb_FY11_EDU_recp_by_Training_Type.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Datagov_End_of_Feb_FY11_EDU_recp_by_Training_Type.csv"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-02-28T05:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 11 Feb Education Recipients by Training Type and VA Education Benefit Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/94qk-9n28",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-08-15",
-            "@type": "dcat:Dataset",
-            "modified": "2020-09-16",
-            "keyword": [
-                "healthcare",
-                "veteran"
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
-            "identifier": "56a0a0a8-27af-49a6-b373-50798755e0f8",
+            "dataQuality": true,
             "description": "<p>This spreadsheet contains data for Total Enrollees, Outpatient Visits, and Inpatient Admissions from FY 2002 to FY 2015.</p>",
-            "title": "Veterans Health Administration Characteristics: FY2002 to FY2015",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22396,37 +22380,37 @@
                     "title": "Veterans Health Administration Characteristics: FY2002 to FY2015"
                 }
             ],
+            "identifier": "56a0a0a8-27af-49a6-b373-50798755e0f8",
+            "issued": "2017-08-15",
+            "keyword": [
+                "healthcare",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/94qk-9n28",
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
+            "title": "Veterans Health Administration Characteristics: FY2002 to FY2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/953t-8sb6",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-14",
-            "keyword": [
-                "cfda 64 100"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:Annette.Brown2@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/953t-8sb6",
+            "dataQuality": true,
             "description": "<p>VBA PROGRAM BENEFITS for Automobiles and Adaptive Equipment for Certain Disabled Veterans and Members of the Armed Forces. Veterans with honorable service and servicepersons on duty having a service-connected disability due to loss or permanent loss of use of one or both feet, one or both hands, or a permanent impairment of vision of both eyes to a prescribed degree. For adaptive equipment only, eligibility also exists if there is service-connected ankylosis of one or both knees or one or both hips. Personnel on active duty also qualify under the same criteria as veterans. Uses &amp; Use Restrictions:  Assistance toward purchase of an automobile or other conveyance is a one-time payment only. Necessary adaptive equipment may be furnished, repaired, replaced, or reinstalled on a conveyance which may be purchased with assistance or any other conveyance subsequently or previously acquired. Adaptive equipment will be provided for no more than two conveyances during any four-year period unless one of those two vehicles becomes unavailable to the veteran.</p>",
-            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE JAN2019",
-            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22434,43 +22418,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/953t-8sb6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/953t-8sb6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/953t-8sb6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/953t-8sb6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/953t-8sb6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/953t-8sb6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/953t-8sb6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/953t-8sb6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/953t-8sb6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/953t-8sb6",
+            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 100"
+            ],
+            "landingPage": "https://www.data.va.gov/d/953t-8sb6",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-14",
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
+            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/healthequity/NVHER.asp",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Office of Health Equity",
+                "hasEmail": "mailto:healthequity@VA.GOV"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/HEALTHEQUITY/docs/National_Veterans_Health_Equity_Report_FY2013_FINAL_508_Comp.pdf#page=165",
+            "description": "<p>The National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. Specifically, this report is designed to provide basic comparative information on the sociodemographics, utilization patterns and rates of diagnosed health conditions among the groups over which the VHA Office of Health Equity (OHE) has responsibility with respect to monitoring, evaluating and acting on identified disparities in access, use, care, quality and outcomes. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/95my-tier/text/plain",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "VA-VHA-OHE-002",
             "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
             "keyword": [
                 "age",
                 "demographics",
@@ -22488,71 +22500,39 @@
                 "va",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Office of Health Equity",
-                "hasEmail": "mailto:healthequity@VA.GOV"
-            },
+            "landingPage": "https://www.va.gov/healthequity/NVHER.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OHE-002",
-            "description": "<p>The National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. Specifically, this report is designed to provide basic comparative information on the sociodemographics, utilization patterns and rates of diagnosed health conditions among the groups over which the VHA Office of Health Equity (OHE) has responsibility with respect to monitoring, evaluating and acting on identified disparities in access, use, care, quality and outcomes. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.</p>",
-            "title": "National Veteran Health Equity Report - FY13",
-            "programCode": [
-                "029:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/95my-tier/text/plain",
-                    "mediaType": "text/plain"
-                }
-            ],
-            "describedBy": "https://www.va.gov/HEALTHEQUITY/docs/National_Veterans_Health_Equity_Report_FY2013_FINAL_508_Comp.pdf#page=165",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Veteran health equity"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Veteran Health Equity Report - FY13"
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
-            "identifier": "VA-VBA-ABR2012-053",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Types and Characteristics of Loans Guaranteed During Fiscal Year 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22560,68 +22540,92 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-053",
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
+            "title": "Types and Characteristics of Loans Guaranteed During Fiscal Year 2012"
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
+            "description": "<p>USA Spending- Home Loan Guaranty- January 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING012014-026",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-01-01T05:00:00Z/2014-01-31T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING012014-026",
-            "description": "<p>USA Spending- Home Loan Guaranty- January 2014.</p>",
-            "title": "USA Spending file- 01/2014 -Home Loan  Guaranty-  CFDA 64.114",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-01-01T05:00:00Z/2014-01-31T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 01/2014 -Home Loan  Guaranty-  CFDA 64.114"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/96uh-n45u",
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
+            "description": "Learn about treatments for those who have both PTSD and substance use disorder (SUD).",
+            "identifier": "https://www.data.va.gov/api/views/96uh-n45u",
             "issued": "2021-06-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
             "keyword": [
                 "alcohol",
                 "co-occurring conditions",
@@ -22630,54 +22634,34 @@
                 "substance use",
                 "sud"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for PTSD",
-                "hasEmail": "mailto:ncptsd@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/96uh-n45u",
+            "modified": "2024-09-04",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for PTSD"
             },
-            "identifier": "https://www.data.va.gov/api/views/96uh-n45u",
-            "description": "Learn about treatments for those who have both PTSD and substance use disorder (SUD).",
-            "title": "Treatments for Co-occurring PTSD and Substance Use Disorder",
-            "programCode": [
-                "029:000"
-            ],
-            "accrualPeriodicity": "R/P1Y",
+            "rights": "All data is within the public domain and is currently available for download.",
             "theme": [
                 "PTSD-Repository"
-            ]
+            ],
+            "title": "Treatments for Co-occurring PTSD and Substance Use Disorder"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/96vj-twyw",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-08-21",
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
-            "identifier": "172201b2-096d-4158-bc86-8ce10a5ac49b",
+            "dataQuality": true,
             "description": "<p>This data table provides the number of Veterans who used VA programs each year and a unique count of VBA users and All users.</p>",
-            "title": "Number of Veterans who Used VA Benefits, FY 2007-2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22685,37 +22669,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "172201b2-096d-4158-bc86-8ce10a5ac49b",
+            "issued": "2018-08-21",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/96vj-twyw",
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
+            "title": "Number of Veterans who Used VA Benefits, FY 2007-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/97hh-vzkm",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-02-01T05:00:00Z/2015-02-28T05:00:00Z",
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
-            "identifier": "VA-OM-OM-136",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT FEB 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22723,46 +22706,76 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-136",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/97hh-vzkm",
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
+            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT FEB 2015"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/97tf-aqpv",
-            "issued": "2023-08-11",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Virginia FY2021",
+            "identifier": "https://www.data.va.gov/api/views/97tf-aqpv",
+            "issued": "2023-08-11",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "virginia"
             ],
-            "identifier": "https://www.data.va.gov/api/views/97tf-aqpv",
+            "landingPage": "https://www.data.va.gov/d/97tf-aqpv",
+            "modified": "2024-06-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Virginia FY2021",
             "title": "NCVAS State Summary Virginia FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/983m-xn66",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "description": "The link provides access to VBA's Weekly benefits claims inventory reports from 2004 through present.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Monday Morning Workload Reports and underlying data is available at this link:  https://www.benefits.va.gov/REPORTS/detailed_claims_data.asp",
+                    "downloadURL": "https://www.benefits.va.gov/REPORTS/detailed_claims_data.asp",
+                    "mediaType": "text/html",
+                    "title": "VBA Monday Morning Workload Report and Data Assets"
+                }
+            ],
+            "identifier": "VA-VBA-Monday Morning Workload-001",
             "issued": "2019-09-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-11",
             "keyword": [
                 "mmwl",
                 "monday",
@@ -22772,77 +22785,70 @@
                 "workload",
                 "workload reports"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/983m-xn66",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-11",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-Monday Morning Workload-001",
-            "description": "The link provides access to VBA's Weekly benefits claims inventory reports from 2004 through present.",
-            "title": "VBA Monday Morning Workload Report (MMWR) 2004 To Present",
-            "programCode": [
-                "029:003"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.benefits.va.gov/REPORTS/detailed_claims_data.asp",
-                    "description": "Monday Morning Workload Reports and underlying data is available at this link:  https://www.benefits.va.gov/REPORTS/detailed_claims_data.asp",
-                    "@type": "dcat:Distribution",
-                    "title": "VBA Monday Morning Workload Report and Data Assets"
-                }
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "VBA Monday Morning Workload Report (MMWR) 2004 To Present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/98bg-sm56",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "ohio",
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
-            "identifier": "https://www.data.va.gov/api/views/98bg-sm56",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Ohio",
+            "identifier": "https://www.data.va.gov/api/views/98bg-sm56",
+            "issued": "2021-08-26",
+            "keyword": [
+                "ohio",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/98bg-sm56",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-13",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Ohio"
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
+            "description": "<p>USA Spending- Reserve Educational Assistance Program (Chapter 1606/1607) for December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-002",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 028",
                 "chapter 1606 1607",
@@ -22850,61 +22856,38 @@
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
-            "identifier": "VA-VBA-USASPENDING122013-002",
-            "description": "<p>USA Spending- Reserve Educational Assistance Program (Chapter 1606/1607) for December 2013.</p>",
-            "title": "USA Spending file- Education- Chapter 1606/1607- CFDA 64.032",
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
+            "title": "USA Spending file- Education- Chapter 1606/1607- CFDA 64.032"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/9arq-96be",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "claim",
-                "cpe"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joseph Enderle",
                 "hasEmail": "mailto:joseph.enderle@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-ORCH-5",
+            "dataQuality": true,
             "description": "<p>Web service proxy/wrapper for CP&amp;E capabilities/data. This interface will retrieve a Bill of Collection record from CP&amp;E and enable a CRM user to view the Bill information. Back office CRM users (primarily DCU Unit) require the ability to review Bills to respond to customer inquiries about Bills and Offsets. The interface will be triggered when a user attempts to query for a Bill using the Bill # (K#).</p>",
-            "title": "CP&E Claim Adapters Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22913,41 +22896,41 @@
                     "title": "CP&E Claim Adapters Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-5",
+            "issued": "2017-11-17",
+            "keyword": [
+                "claim",
+                "cpe"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9arq-96be",
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
+            "title": "CP&E Claim Adapters Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/9c46-aqd7",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "healthcare",
-                "scheduling"
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
-            "identifier": "VA-VIA-8",
+            "dataQuality": true,
             "description": "<p>This service provides web services used to obtain patients data. The service does not support multiple Vista sites data access. Users of this service are intended to be healthcare providers.</p>",
-            "title": "Scheduling Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22956,42 +22939,42 @@
                     "title": "Scheduling Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VIA-8",
+            "issued": "2017-11-17",
+            "keyword": [
+                "healthcare",
+                "scheduling"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9c46-aqd7",
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
+            "title": "Scheduling Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9cwq-gzce",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2012-01-01T05:00:00Z/2012-01-01T05:00:00Z",
-            "modified": "2020-11-12",
-            "keyword": [
-                "veterans",
-                "women"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:noemailprovided@usa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-061",
+            "dataQuality": true,
             "description": "<p>Women Veterans Profile 2012 uses 2012 data from the 2012 American Community Survey to compare the demographic and socioeconomic characteristics of women Veterans and women non-Veterans.</p>",
-            "title": "Women Veteran Profile: 2012",
-            "programCode": [
-                "029:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22999,44 +22982,45 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-061",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans",
+                "women"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9cwq-gzce",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "public",
+            "temporal": "2012-01-01T05:00:00Z/2012-01-01T05:00:00Z",
             "theme": [
                 "Use of Benefits and Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Women Veteran Profile: 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9d3f-ka7w",
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
-            "identifier": "6a4f9cdc-a364-480b-b317-009bef2bb488",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Tennessee FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23044,38 +23028,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "6a4f9cdc-a364-480b-b317-009bef2bb488",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9d3f-ka7w",
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
+            "title": "State Summary Tennessee FY2016"
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
-            "temporal": "2013-10-01T04:00:00Z/2013-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-078",
+            "dataQuality": true,
             "description": "<p>FY 2014 First Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2014 First Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23084,49 +23068,45 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-078",
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
+            "temporal": "2013-10-01T04:00:00Z/2013-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2014 First Quarter High-Dollar Overpayments Report"
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
-            "identifier": "VA-VBA-ABR2012-015",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "GWOT Service Connected Disability Benefits by Combined PCT of Disability for Veterans Receiving Comp at the End of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23134,46 +23114,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-015",
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
+            "title": "GWOT Service Connected Disability Benefits by Combined PCT of Disability for Veterans Receiving Comp at the End of FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9fby-e2tq",
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
-            "identifier": "https://www.data.va.gov/api/views/9fby-e2tq",
             "description": "Percentage distributions of genders across eras of initial service. Data underlying the seventh figure of Part 1 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 8, Percentage distributions of genders across eras of initial service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23181,59 +23162,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9fby-e2tq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9fby-e2tq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9fby-e2tq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/9fby-e2tq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9fby-e2tq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9fby-e2tq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9fby-e2tq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9fby-e2tq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9fby-e2tq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/9fby-e2tq",
+            "issued": "2020-10-19",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9fby-e2tq",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 8, Percentage distributions of genders across eras of initial service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9fkf-pcw5",
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
-            "identifier": "https://www.data.va.gov/api/views/9fkf-pcw5",
+            "dataQuality": true,
             "description": "<p>This dataset contains information on minority veteran healthcare usage, educational attainment, unemployment rates, median income, and projected population figures.</p>",
-            "title": "Benefits Utilization by Program and Minority Status: 2014",
-            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23241,59 +23223,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9fkf-pcw5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9fkf-pcw5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9fkf-pcw5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/9fkf-pcw5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9fkf-pcw5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9fkf-pcw5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9fkf-pcw5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9fkf-pcw5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9fkf-pcw5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/9fkf-pcw5",
+            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
+            "issued": "2017-03-15",
+            "keyword": [
+                "health care",
+                "income",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9fkf-pcw5",
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
+            "title": "Benefits Utilization by Program and Minority Status: 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/9fw8-eb9n",
-            "issued": "2023-06-13",
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
-            "identifier": "https://www.data.va.gov/api/views/9fw8-eb9n",
             "description": "This dataset is comprised of 1-year estimate data from the American Community Survey published as of 2021.",
-            "title": "FY 2021_NCVAS Demographics Data For State Summary Visuals",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23301,72 +23288,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9fw8-eb9n/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9fw8-eb9n/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9fw8-eb9n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/9fw8-eb9n/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9fw8-eb9n/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9fw8-eb9n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9fw8-eb9n/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9fw8-eb9n/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9fw8-eb9n/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/9fw8-eb9n",
+            "issued": "2023-06-13",
+            "landingPage": "https://www.data.va.gov/d/9fw8-eb9n",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Demographics Data For State Summary Visuals"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9ged-xx5g",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "Although those who serve in the military are at risk for certain types of trauma, other traumatic events affect civilians (those in the community).",
             "identifier": "https://www.data.va.gov/api/views/9ged-xx5g",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/9ged-xx5g",
+            "modified": "2024-09-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Although those who serve in the military are at risk for certain types of trauma, other traumatic events affect civilians (those in the community).",
             "title": "How often do PTSD treatment studies include military samples?"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/9gma-2znm",
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
-            "identifier": "https://www.data.va.gov/api/views/9gma-2znm",
             "description": "",
-            "title": "VetPop 30years For Tables FY2024",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23374,62 +23361,55 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9gma-2znm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9gma-2znm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9gma-2znm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/9gma-2znm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9gma-2znm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9gma-2znm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9gma-2znm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9gma-2znm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9gma-2znm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/9gma-2znm",
+            "issued": "2024-04-23",
+            "landingPage": "https://www.data.va.gov/d/9gma-2znm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop 30years For Tables FY2024"
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
-            "identifier": "VA-VBA-ABR2012-033",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Total Service Connected Disabilities for Veterans Receiving Compensation at the End of FY2012 by pct and body system",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23437,43 +23417,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-033",
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
+            "title": "Total Service Connected Disabilities for Veterans Receiving Compensation at the End of FY2012 by pct and body system"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9h9v-dhi6",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "mental health"
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
-            "identifier": "VA-OEI-OEI-195",
+            "dataQuality": true,
             "description": "<p>This application provided a way for the public to explore and analyze VA Mental Health Statistics (FY2015 Annual Datasheet).</p>",
-            "title": "Mental Health Statistics Explorer",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23482,24 +23467,52 @@
                     "title": "html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-195",
+            "issued": "2017-07-26",
+            "keyword": [
+                "mental health"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9h9v-dhi6",
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
+            "title": "Mental Health Statistics Explorer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9hbf-9jzg",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "The Department of Veterans Affairs (VA) provides healthcare services to its veterans across the USA including territories and possessions. Healthcare services are delivered through 18 geographically divided administrative areas called Veterans Integrated Services Networks (VISN). Each VISN is divided into healthcare areas called Markets and Submarkets. Each Submarket is divided into Sectors and each Sector comprises one or more counties. In 1995 a process was created to coordinate and review the realignment of the Heath Care Networks. The Capital Asset Realignment for Enhanced Services (CARES) process established VISN 'subsets' called Markets, Submarkets and Sectors which, being smaller than VISNs, allowed for more precise analyses for greater access measurement to health care.\n\n\nThe County layer is the base geographic unit of the VISN-Market-Submarket-Sector-County hierarchy. The key attribute in this data set is the FIPS which is defined as a string of 5 characters with unique alphanumeric combinations for each site. The first 2 are the State FIPS code and the next 3 designate the County FIPS code. Example: '01031' is the FIPS for Coffee County, Alabama.\n\n\nA Sector is a cluster of geographically adjacent counties within a VA Submarket. The process of aggregating counties into sectors uses a combination of automated algorithms and manual inspection of maps. The key attribute in this data set is the SECTOR which is defined as a string of eight characters broken down into four parts in the order of VISN (2-char), Market (1-char), Submarket (1-char), and Sector(1-char) connected by a hyphen. For example, Sector 12-a-3-A indicates VISN 12, Market a, Submarket 3 and Sector A.\n\n\nSub-markets reflect a clustering of the enrollee population within a market and are an aggregation of Sectors. The key attribute in this data set is the SUBMARKET which is defined as a string of six characters broken down in three parts in the order of VISN (2-char), Market (1-char), and Submarket (1-char) connected by a hyphen. For example, Submarket 12-a-3 indicates VISN 12, Market a, and Submarket 3.\n\n\nCARES defines Markets as \"an aggregated geographic area having a sufficient population and geographic size to both benefit from the coordination and planning of health care services and to support a full healthcare delivery system (i.e. primary care, mental health care, inpatient care, tertiary care, and long term care)\". Each Market is built from Submarkets. The key attribute in this data set is the MARKET which is defined as a string of four characters broken down in two parts in the order of HCN (2-char) and Market (1-char) connected by a hyphen. For example, Market 12-a indicates VISN 12 and Market a.\n\n\nThe key attribute in the VISN data set is defined as a string of two characters from 01-23, excluding 3, 11, 13, 14 and 18; a VISN also has an officially recognized VA title. For example, VISN 06 is the Mid-Atlantic Health Care Network. VISNs can span across neighboring countries to include areas that are not contiguous. For example, VISN 08 includes Florida and Puerto Rico in addition to most of Florida and southern Georgia, and VISN 20 includes Alaska and parts of the northwest conterminous United States. Each VISN is built from Markets, Submarkets, Sectors and Counties derived from Census (2010) County data.\n\n\nBecause VISNs are composed of VHA markets, VISN boundaries align with the outer edges of their constituent markets\u2019 boundaries. Markets cross state borders wherever it is necessary to keep outpatient clinics (e.g. Community-Based Outpatient Clinics(CBOCs)) and their catchment areas in the same market as their parent medical centers. Thus, VISN boundaries also cross state borders. In 2016 senior leadership considered the challenge of conforming VISN boundaries to MyVA Districts, which coincide with state boundaries. It was agreed that VHA would not separate outpatient clinics from their parent medical centers due to added complexity. Many outpat",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/9hbf-9jzg/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/9hbf-9jzg",
+            "isPartOf": "Veterans Integrated Services Networks (VISN), Markets, Submarkets, Sectors and Counties by Geographic Location",
             "issued": "2017-12-07",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-06-01/2017-08-31",
-            "modified": "2024-02-15",
             "keyword": [
                 "boundries",
                 "markets",
@@ -23510,105 +23523,70 @@
                 "vha",
                 "visn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/9hbf-9jzg",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-02-15",
+            "programCode": [
+                "029:080"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/9hbf-9jzg",
-            "description": "The Department of Veterans Affairs (VA) provides healthcare services to its veterans across the USA including territories and possessions. Healthcare services are delivered through 18 geographically divided administrative areas called Veterans Integrated Services Networks (VISN). Each VISN is divided into healthcare areas called Markets and Submarkets. Each Submarket is divided into Sectors and each Sector comprises one or more counties. In 1995 a process was created to coordinate and review the realignment of the Heath Care Networks. The Capital Asset Realignment for Enhanced Services (CARES) process established VISN 'subsets' called Markets, Submarkets and Sectors which, being smaller than VISNs, allowed for more precise analyses for greater access measurement to health care.\n\n\nThe County layer is the base geographic unit of the VISN-Market-Submarket-Sector-County hierarchy. The key attribute in this data set is the FIPS which is defined as a string of 5 characters with unique alphanumeric combinations for each site. The first 2 are the State FIPS code and the next 3 designate the County FIPS code. Example: '01031' is the FIPS for Coffee County, Alabama.\n\n\nA Sector is a cluster of geographically adjacent counties within a VA Submarket. The process of aggregating counties into sectors uses a combination of automated algorithms and manual inspection of maps. The key attribute in this data set is the SECTOR which is defined as a string of eight characters broken down into four parts in the order of VISN (2-char), Market (1-char), Submarket (1-char), and Sector(1-char) connected by a hyphen. For example, Sector 12-a-3-A indicates VISN 12, Market a, Submarket 3 and Sector A.\n\n\nSub-markets reflect a clustering of the enrollee population within a market and are an aggregation of Sectors. The key attribute in this data set is the SUBMARKET which is defined as a string of six characters broken down in three parts in the order of VISN (2-char), Market (1-char), and Submarket (1-char) connected by a hyphen. For example, Submarket 12-a-3 indicates VISN 12, Market a, and Submarket 3.\n\n\nCARES defines Markets as \"an aggregated geographic area having a sufficient population and geographic size to both benefit from the coordination and planning of health care services and to support a full healthcare delivery system (i.e. primary care, mental health care, inpatient care, tertiary care, and long term care)\". Each Market is built from Submarkets. The key attribute in this data set is the MARKET which is defined as a string of four characters broken down in two parts in the order of HCN (2-char) and Market (1-char) connected by a hyphen. For example, Market 12-a indicates VISN 12 and Market a.\n\n\nThe key attribute in the VISN data set is defined as a string of two characters from 01-23, excluding 3, 11, 13, 14 and 18; a VISN also has an officially recognized VA title. For example, VISN 06 is the Mid-Atlantic Health Care Network. VISNs can span across neighboring countries to include areas that are not contiguous. For example, VISN 08 includes Florida and Puerto Rico in addition to most of Florida and southern Georgia, and VISN 20 includes Alaska and parts of the northwest conterminous United States. Each VISN is built from Markets, Submarkets, Sectors and Counties derived from Census (2010) County data.\n\n\nBecause VISNs are composed of VHA markets, VISN boundaries align with the outer edges of their constituent markets\u2019 boundaries. Markets cross state borders wherever it is necessary to keep outpatient clinics (e.g. Community-Based Outpatient Clinics(CBOCs)) and their catchment areas in the same market as their parent medical centers. Thus, VISN boundaries also cross state borders. In 2016 senior leadership considered the challenge of conforming VISN boundaries to MyVA Districts, which coincide with state boundaries. It was agreed that VHA would not separate outpatient clinics from their parent medical centers due to added complexity. Many outpat",
-            "title": "Veterans Integrated Services Networks (VISN), Markets, Submarkets, Sectors and Counties by Geographic Location",
-            "isPartOf": "Veterans Integrated Services Networks (VISN), Markets, Submarkets, Sectors and Counties by Geographic Location",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/9hbf-9jzg/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
             "spatial": "US",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2017-06-01/2017-08-31",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Integrated Services Networks (VISN), Markets, Submarkets, Sectors and Counties by Geographic Location"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/9huk-uqy2",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "veterans",
-                "wyoming"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/9huk-uqy2",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Wyoming",
+            "identifier": "https://www.data.va.gov/api/views/9huk-uqy2",
+            "issued": "2021-08-26",
+            "keyword": [
+                "veterans",
+                "wyoming"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9huk-uqy2",
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
+            "title": "State Summaries_Wyoming"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9hvj-6md7",
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
-            "identifier": "https://www.data.va.gov/api/views/9hvj-6md7",
             "description": "VA Program Use Rates within Age Groups by Sex - FY2021. Data underlying the fifth figure of Part 1 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Rates of Use within Age Group by Sex, FY2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23616,69 +23594,95 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9hvj-6md7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9hvj-6md7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9hvj-6md7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/9hvj-6md7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9hvj-6md7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9hvj-6md7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9hvj-6md7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9hvj-6md7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9hvj-6md7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/9hvj-6md7",
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
+            "landingPage": "https://www.data.va.gov/d/9hvj-6md7",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Rates of Use within Age Group by Sex, FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/9jtx-xawd",
-            "issued": "2021-02-08",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-26",
-            "keyword": [
-                "utilization",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/9jtx-xawd",
             "description": "This Data Story explores the take-up rate of Veterans using VA benefits and services within the first two years of transitioning out of military service.",
-            "title": "Are Transitioning Veterans Using the VA Benefits and Services?",
+            "identifier": "https://www.data.va.gov/api/views/9jtx-xawd",
+            "issued": "2021-02-08",
+            "keyword": [
+                "utilization",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9jtx-xawd",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-02-26",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Are Transitioning Veterans Using the VA Benefits and Services?"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9knx-sjj5",
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
+            "description": "Learn how risk of bias was included for each study in the PTSD Repository, with a description of domain elements and overall ratings.",
+            "identifier": "https://www.data.va.gov/api/views/9knx-sjj5",
             "issued": "2021-11-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
             "keyword": [
                 "ahrq",
                 "ptsd",
@@ -23686,51 +23690,30 @@
                 "risk of bias",
                 "rob rating"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for PTSD",
-                "hasEmail": "mailto:ncptsd@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/9knx-sjj5",
+            "modified": "2024-09-04",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for PTSD"
             },
-            "identifier": "https://www.data.va.gov/api/views/9knx-sjj5",
-            "description": "Learn how risk of bias was included for each study in the PTSD Repository, with a description of domain elements and overall ratings.",
-            "title": "Risk of Bias Assessment in the PTSD Repository",
-            "programCode": [
-                "029:000"
-            ],
-            "accrualPeriodicity": "R/P1Y"
+            "rights": "All data is within the public domain and is currently available for download.",
+            "title": "Risk of Bias Assessment in the PTSD Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9mtq-5n8d",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "kansas",
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
-            "identifier": "VA-OEI-OEI-101",
             "description": "<p>This is a summary of the programs and services provided by VA in Kansas in fiscal year 2014.</p>",
-            "title": "State Summary:  Kansas",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23739,44 +23722,45 @@
                     "title": "State Summary:  Kansas"
                 }
             ],
+            "identifier": "VA-OEI-OEI-101",
+            "issued": "2017-07-26",
+            "keyword": [
+                "kansas",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9mtq-5n8d",
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
+            "title": "State Summary:  Kansas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9mw6-uag6",
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
-            "identifier": "a19219f2-0397-4430-bdb3-c982a31505c9",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Missouri FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23784,69 +23768,68 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "a19219f2-0397-4430-bdb3-c982a31505c9",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9mw6-uag6",
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
+            "title": "State Summary Missouri FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/9ntj-nqv4",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "south dakota",
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
-            "identifier": "https://www.data.va.gov/api/views/9ntj-nqv4",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_South Dakota",
+            "identifier": "https://www.data.va.gov/api/views/9ntj-nqv4",
+            "issued": "2021-08-26",
+            "keyword": [
+                "south dakota",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9ntj-nqv4",
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
+            "title": "State Summaries_South Dakota"
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
-            "temporal": "2006-10-01T04:00:00Z/2007-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
-                "franchise fund",
-                "fy 2007"
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
-            "identifier": "VA-OM-OM-038",
+            "dataQuality": true,
             "description": "<p>Franchise Fund FY 2007 Annual Report</p>",
-            "title": "Franchise Fund FY 2007 Annual Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23855,49 +23838,44 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-038",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund",
+                "fy 2007"
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
+            "temporal": "2006-10-01T04:00:00Z/2007-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Franchise Fund FY 2007 Annual Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9pkf-7vp3",
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
-            "identifier": "https://www.data.va.gov/api/views/9pkf-7vp3",
             "description": "Rate of Use by Race/Ethnicity, any VA program - FY2021. Data underlying the sixth figure of Part 1 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Rate of Use by Race/Ethnicity, FY2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23905,39 +23883,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9pkf-7vp3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9pkf-7vp3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9pkf-7vp3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/9pkf-7vp3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9pkf-7vp3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9pkf-7vp3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9pkf-7vp3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9pkf-7vp3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9pkf-7vp3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/9pkf-7vp3",
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
+            "landingPage": "https://www.data.va.gov/d/9pkf-7vp3",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Rate of Use by Race/Ethnicity, FY2021"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2008.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/0338_001.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-06",
             "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2008",
                 "appeals",
@@ -23954,51 +23967,51 @@
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
-            "identifier": "VA-OIT-ITIS-06",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2008.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2008",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/0338_001.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2008"
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
+                    "downloadURL": "http://www.va.gov/vetdata/docs/GDX/GDX96.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Geographic Distribution of VA Expenditures FY1996"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-022",
             "issued": "2017-07-26",
-            "temporal": "1995-10-01T04:00:00Z/1996-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -24012,133 +24025,125 @@
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
-            "identifier": "VA-OEI-OEI-022",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY1996",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.va.gov/vetdata/docs/GDX/GDX96.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Geographic Distribution of VA Expenditures FY1996"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "1995-10-01T04:00:00Z/1996-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY1996"
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
+            "description": "<p>USA Spending- Vocational Rehabilitation for Disabled Veterans - Chapter 31- March 2014</p>",
+            "identifier": "VA-VBA-USASPENDING032014-056",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING032014-056",
-            "description": "<p>USA Spending- Vocational Rehabilitation for Disabled Veterans - Chapter 31- March 2014</p>",
-            "title": "USA Spending file-03/2014- Vocational Rehabilitation for Disabled Veterans-  CFDA 64.116",
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
+            "title": "USA Spending file-03/2014- Vocational Rehabilitation for Disabled Veterans-  CFDA 64.116"
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
+            "description": "<p>USA Spending file- 03/2014-Veterans Compensation for Service-Connected Disability-  CFDA 64.109</p>",
+            "identifier": "VA-VBA-USASPENDING032014-048",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 109",
                 "compensation for service-connected disability",
                 "compensation service",
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
-            "identifier": "VA-VBA-USASPENDING032014-048",
-            "description": "<p>USA Spending file- 03/2014-Veterans Compensation for Service-Connected Disability-  CFDA 64.109</p>",
-            "title": "USA Spending file- 03/2014-Veterans Compensation for Service-Connected Disability",
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
+            "title": "USA Spending file- 03/2014-Veterans Compensation for Service-Connected Disability"
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
+            "description": "<p>USA Spending- Post-Vietnam Era Veterans Educational Assistance- Chapter 32- for March 2014</p>",
+            "identifier": "VA-VBA-USASPENDING132014-052",
             "issued": "2017-07-26",
-            "temporal": "2013-03-01T05:00:00Z/2013-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 120",
                 "chapter 35",
@@ -24146,70 +24151,41 @@
                 "usa spending",
                 "veap"
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
-            "identifier": "VA-VBA-USASPENDING132014-052",
-            "description": "<p>USA Spending- Post-Vietnam Era Veterans Educational Assistance- Chapter 32- for March 2014</p>",
-            "title": "USA Spending file- March 2014-Education- Chapter 32- CFDA 64.120",
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
+            "title": "USA Spending file- March 2014-Education- Chapter 32- CFDA 64.120"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9r44-pm2u",
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
-            "identifier": "VA-VHA-OIA-032",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset defines the quality of care in defined hospital settings: Inpatient, Outpatient and Emergency Room.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Quality of Care - Hospital Settings",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset defines the quality of care in defined hospital settings: Inpatient, Outpatient and Emergency Room.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24217,66 +24193,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9r44-pm2u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9r44-pm2u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9r44-pm2u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/9r44-pm2u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9r44-pm2u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9r44-pm2u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9r44-pm2u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9r44-pm2u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9r44-pm2u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-032",
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
+            "landingPage": "https://www.data.va.gov/d/9r44-pm2u",
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
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Quality of Care - Hospital Settings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9rtn-nqtk",
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
-            "identifier": "06fe131f-3173-4ebb-bab6-7bfe6a857ad1",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Kentucky FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24284,42 +24268,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "06fe131f-3173-4ebb-bab6-7bfe6a857ad1",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9rtn-nqtk",
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
+            "title": "State Summary Kentucky FY2016"
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
-            "identifier": "VA-VBA-ABR2012-093",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Iowa-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24327,46 +24307,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-093",
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
+            "title": "Iowa-FY12 Benefits Summary"
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
-            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-008",
+            "dataQuality": true,
             "description": "<p>2009 VA Performance and Accountability Report Highlights.</p>",
-            "title": "2009 VA Performance and Accountability Report Highlights",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24375,44 +24358,45 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "Financial"
+            "identifier": "VA-OM-OM-008",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accountability",
+                "performance",
+                "report"
             ],
+            "landingPage": "https://www.va.gov/budget/report/",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9u8y-zaby",
-            "bureauCode": [
-                "029:00"
             ],
-            "issued": "2019-06-10",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
+            "theme": [
+                "Financial"
+            ],
+            "title": "2009 VA Performance and Accountability Report Highlights"
+        },
+        {
             "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "c31758da-32e4-43d0-8228-acee66a2536b",
+            "dataQuality": true,
             "description": "<p>To show Number of Living Air Force (at last separation) Veterans by county</p>",
-            "title": "Air Force Veterans (2017) Living Only",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24420,42 +24404,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "c31758da-32e4-43d0-8228-acee66a2536b",
+            "issued": "2019-06-10",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9u8y-zaby",
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
+            "title": "Air Force Veterans (2017) Living Only"
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
-            "identifier": "VA-VBA-ABR2012-128",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "West_Virginia-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24463,45 +24443,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-128",
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
+            "title": "West_Virginia-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "aian",
-                "american indian and alaskan native"
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
-            "identifier": "VA-OEI-OEI-077",
             "description": "<p>This report uses data from the 2013 American Community Survey Public Use Microdata Sample to report data concerning the demographics, socioeconomic status, and health characteristics of AIAN Servicemembers and Veterans.</p>",
-            "title": "American Indian and Alaska Native Servicemembers and Veterans 2013 (AIAN)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24510,44 +24493,44 @@
                     "title": "American Indian and Alaska Native Servicemembers and Veterans 2013 (AIAN)"
                 }
             ],
+            "identifier": "VA-OEI-OEI-077",
+            "issued": "2017-07-26",
+            "keyword": [
+                "aian",
+                "american indian and alaskan native"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/",
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
+            "temporal": "2012-10-01T04:00:00Z/2013-10-01T04:00:00Z",
             "theme": [
                 "AIAN Veterans"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "American Indian and Alaska Native Servicemembers and Veterans 2013 (AIAN)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9v7z-aha2",
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
-            "identifier": "https://www.data.va.gov/api/views/9v7z-aha2",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAR2019",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24555,60 +24538,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9v7z-aha2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9v7z-aha2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9v7z-aha2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/9v7z-aha2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9v7z-aha2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9v7z-aha2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9v7z-aha2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9v7z-aha2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9v7z-aha2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/9v7z-aha2",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9v7z-aha2",
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
+            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9w7r-7xq5",
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
-            "title": "Equitable Relief Reports 2015",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24616,29 +24602,46 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9w7r-7xq5",
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
+            "title": "Equitable Relief Reports 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/9wyu-8bgh",
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
+            "description": "<p>The Remote Order Entry System (ROES) is the front end of the Denver Acquisition &amp; Logistics Center's (DALC) order fulfillment production system. ROES is used by VA and Department of Defense clinicians to place orders for certain types of medical products and services that are maintained under contract by the DALC. The most substantial product line handled through ROES is hearing aids. The ROES application and database are tailored for efficiency in ordering the specified devices and other items available from the DALC, and tracking them upon issue to an individual patient when appropriate. Other product lines handled through ROES include hearing aid accessories and batteries, cochlear implants, prosthetic items, aids for the visually impaired, and assistive devices. A line of service provided by the DALC and facilitated by ROES is that of hearing aid repair. The ROES application and database tie together the DALC enterprise business functions of contracting/acquisition management, order fulfillment, distribution management, finance, and product life cycle support. Extensive order tracking, serialized device registration, patient/device history, and sales/financial reporting are also supported by the database.</p>",
+            "identifier": "VA-VHA-PL-003",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1990-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "acquistion",
                 "aids",
@@ -24657,60 +24660,41 @@
                 "visual",
                 "visually"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/9wyu-8bgh",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:052"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PL-003",
-            "description": "<p>The Remote Order Entry System (ROES) is the front end of the Denver Acquisition &amp; Logistics Center's (DALC) order fulfillment production system. ROES is used by VA and Department of Defense clinicians to place orders for certain types of medical products and services that are maintained under contract by the DALC. The most substantial product line handled through ROES is hearing aids. The ROES application and database are tailored for efficiency in ordering the specified devices and other items available from the DALC, and tracking them upon issue to an individual patient when appropriate. Other product lines handled through ROES include hearing aid accessories and batteries, cochlear implants, prosthetic items, aids for the visually impaired, and assistive devices. A line of service provided by the DALC and facilitated by ROES is that of hearing aid repair. The ROES application and database tie together the DALC enterprise business functions of contracting/acquisition management, order fulfillment, distribution management, finance, and product life cycle support. Extensive order tracking, serialized device registration, patient/device history, and sales/financial reporting are also supported by the database.</p>",
-            "title": "Remote Order Entry System (ROES)",
-            "programCode": [
-                "029:052"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1990-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Remote Order Entry System (ROES)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9x95-drd9",
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
-            "identifier": "https://www.data.va.gov/api/views/9x95-drd9",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located.</p>",
-            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS MAY2019",
-            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24718,62 +24702,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9x95-drd9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9x95-drd9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9x95-drd9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/9x95-drd9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9x95-drd9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9x95-drd9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9x95-drd9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9x95-drd9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9x95-drd9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/9x95-drd9",
+            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 114"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9x95-drd9",
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
+            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/9xtt-j9ch",
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
-            "identifier": "https://www.data.va.gov/api/views/9xtt-j9ch",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE FEB2019",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24781,121 +24764,122 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9xtt-j9ch/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9xtt-j9ch/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9xtt-j9ch/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/9xtt-j9ch/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9xtt-j9ch/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9xtt-j9ch/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/9xtt-j9ch/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/9xtt-j9ch/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/9xtt-j9ch/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/9xtt-j9ch",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9xtt-j9ch",
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
+            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/9ybn-2xqx",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Connecticut FY2023",
+            "identifier": "https://www.data.va.gov/api/views/9ybn-2xqx",
             "issued": "2024-05-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "ct",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/9ybn-2xqx",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/9ybn-2xqx",
-            "description": "NCVAS State Summary Connecticut FY2023",
-            "title": "NCVAS State Summary Connecticut FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Connecticut FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/9zgc-itmj",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "maine",
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
-            "identifier": "https://www.data.va.gov/api/views/9zgc-itmj",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Maine",
+            "identifier": "https://www.data.va.gov/api/views/9zgc-itmj",
+            "issued": "2021-08-26",
+            "keyword": [
+                "maine",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/9zgc-itmj",
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
+            "title": "State Summaries_Maine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/a23g-khhe",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "validation"
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
-            "identifier": "c6614866-a81a-48b8-8847-4e1770378774",
+            "dataQuality": true,
             "description": "<p>Validation to ensure data and identity integrity. DAS will also ensure security compliant standards are met.</p>",
-            "title": "Validation",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24904,75 +24888,71 @@
                     "title": "Validation"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "c6614866-a81a-48b8-8847-4e1770378774",
+            "issued": "2018-02-23",
+            "keyword": [
+                "validation"
+            ],
+            "landingPage": "https://www.data.va.gov/d/a23g-khhe",
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
+            "title": "Validation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/a2aa-kbq6",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
-            "keyword": [
-                "cfda 64 106"
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
-            "identifier": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "dataQuality": true,
             "description": "<p>VBA SPECIALLY ADAPTED HOUSING BENEFIT PROGRAMS. The Specially Adapted Housing (SAH) grant program helps Veterans with certain service-connected disabilities live independently in a barrier-free environment. SAH grants can be used in one of the following ways: (1) construct a suitable home on suitable land either already owned or to be acquired by the veteran, or (2) remodel an existing home if it can be suitably adapted, or (3) acquire a suitably adapted home or reduce the outstanding mortgage on a suitably adapted home already owned by the veteran. b. The Special Housing Adaptation (SHA) grant program helps veterans with certain service-connected disabilities adapt or purchase a home to accommodate the disability. SHA grants can be used in one of the following ways: (1) adapt an existing home the veteran or a family member already owns in which the veteran lives; (2) adapt a home the veteran or family member intends to purchase in which the veteran will live; (3) help a veteran purchase a home already adapted in which the veteran will live. c. . The Temporary Residence Adaptations (TRA) program provides adaptation assistance to veterans who are residing, but do not intend to permanently reside, in the a residence owned by a family member. If a veteran is otherwise eligible for SAH or SHA, the assistance is limited. d. SAH and SHA grants may be used up to three times, as long as the aggregate grant amount does not exceed the statutory dollar limitation. TRA grants may only be used once (and count as a grant usage for purposes of the limit of three), and the amount of assistance provided will be subtracted from the veteran's available statutory maximum.</p>",
-            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS FY2019",
+            "identifier": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 106"
+            ],
+            "landingPage": "https://www.data.va.gov/d/a2aa-kbq6",
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
+            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS FY2019"
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
-            "identifier": "VA-VBA-ABR2012-078",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Alaska FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24980,88 +24960,92 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "ABR 2012"
+            "identifier": "VA-VBA-ABR2012-078",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
             ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
+            "theme": [
+                "ABR 2012"
+            ],
+            "title": "Alaska FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Family Servicemembers Group Life Insurance</p>",
+            "identifier": "VA-VBA-MEDIAPUB-050",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2012-09-01T04:00:00Z/2012-09-01T04:00:00Z",
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
-            "identifier": "VA-VBA-MEDIAPUB-050",
-            "description": "<p>Family Servicemembers Group Life Insurance</p>",
-            "title": "Family Servicemembers Group Life Insurance",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2012-09-01T04:00:00Z/2012-09-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Family Servicemembers Group Life Insurance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/a3pe-xk7b",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "colorado",
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
-            "identifier": "VA-OEI-OEI-091",
+            "dataQuality": true,
             "description": "<p>This provides a summary of the services and programs provided by VA in Colorado in fiscal year 2014.</p>",
-            "title": "State Summary:  Colorado",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25070,50 +25054,46 @@
                     "title": "State Summaries:  Colorado"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-091",
+            "issued": "2017-07-26",
+            "keyword": [
+                "colorado",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/a3pe-xk7b",
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
+            "title": "State Summary:  Colorado"
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
-            "identifier": "VA-VBA-ABR2012-051",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Status of Loans Guaranteed by Fiscal Year",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25121,43 +25101,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-051",
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
+            "title": "Status of Loans Guaranteed by Fiscal Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/a63r-24dv",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "minorities"
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
-            "identifier": "https://www.data.va.gov/api/views/a63r-24dv",
             "description": "Dataset showing various statistics and measures of minority veterans and minority non-veterans as of 2014",
-            "title": "2014 Minority Veterans vs Minority Non-Veterans Characteristics",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25165,62 +25149,56 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/a63r-24dv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/a63r-24dv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/a63r-24dv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/a63r-24dv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/a63r-24dv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/a63r-24dv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/a63r-24dv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/a63r-24dv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/a63r-24dv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/a63r-24dv",
+            "issued": "2019-10-24",
+            "keyword": [
+                "minorities"
+            ],
+            "landingPage": "https://www.data.va.gov/d/a63r-24dv",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
+            "title": "2014 Minority Veterans vs Minority Non-Veterans Characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/a643-9yth",
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
-            "identifier": "https://www.data.va.gov/api/views/a643-9yth",
             "description": "Percent Users vs Non-Users Distribution by Era of Service - Females. Data underlying the fifth figure of Part 2 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Percentage Era Distribution of Female Users and Non-Users, FY 2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25228,38 +25206,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/a643-9yth/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/a643-9yth/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/a643-9yth/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/a643-9yth/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/a643-9yth/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/a643-9yth/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/a643-9yth/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/a643-9yth/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/a643-9yth/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/a643-9yth",
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
+            "landingPage": "https://www.data.va.gov/d/a643-9yth",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Percentage Era Distribution of Female Users and Non-Users, FY 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/a7eq-b347",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Joseph Brooks",
+                "hasEmail": "mailto:Joseph.Brooks2@va.gov"
+            },
+            "description": "<p>Provides architectural guidance and constraints associated with authentication of internal users to VA applications via internal single sign-on solutions, Active Directory, and PIV-only authentication.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/a7eq-b347/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "VA-OIT-OIT-142",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
             "keyword": [
                 "509",
                 "active directory",
@@ -25272,46 +25283,38 @@
                 "saml",
                 "single sign-on"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Joseph Brooks",
-                "hasEmail": "mailto:Joseph.Brooks2@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/a7eq-b347",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:080"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OIT-OIT-142",
-            "description": "<p>Provides architectural guidance and constraints associated with authentication of internal users to VA applications via internal single sign-on solutions, Active Directory, and PIV-only authentication.</p>",
-            "title": "VA Enterprise Design Patterns - 1.1 (Privacy and Security) Internal User Identity Authentication V1.0",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/a7eq-b347/application/pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "VA Enterprise Design Patterns - 1.1 (Privacy and Security) Internal User Identity Authentication V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/a873-9h5w",
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
+            "description": "<p>In 2009, the Department of Defense estimated that approximately 40,000 service members who served in OEF/OIF may have embedded fragment wounds as the result of small arms fire or a blast or explosion caused by an Improvised Explosive Device (IED), rocket propelled grenade (RPG), landmine, grenade, or enemy or friendly fire. Studies have shown that embedded fragments are not inert in the body, but may breakdown slowly over time and potentially affect an individual\u00ef\u00bf\u00bds health. The recognition of potential short and long-term health effects of embedded fragments and the large number of soldiers with injuries resulting in embedded fragments led the Presidential Task Force on Returning Global War on Terror Heroes to recommend that the VHA establish a registry and medical surveillance program for Veterans with retained fragments. The Toxic Embedded Fragment Surveillance Center (TEFSC) has been established at the Baltimore VA Medical Center to coordinate this charge. A critical component of the TEFSC medical surveillance program is the development of an Embedded Fragment Registry. This registry provides a mechanism to identify Veterans with embedded fragments, manage clinical data related to embedded fragments, and develop medical and surgical guidelines that will enable the TEFSC staff and VA clinicians to deliver appropriate medical care to these Veterans.</p>",
+            "identifier": "VA-VHA-OPH-005",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2008-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "afghanistan",
                 "baltimore",
@@ -25329,61 +25332,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/a873-9h5w",
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
-            "identifier": "VA-VHA-OPH-005",
-            "description": "<p>In 2009, the Department of Defense estimated that approximately 40,000 service members who served in OEF/OIF may have embedded fragment wounds as the result of small arms fire or a blast or explosion caused by an Improvised Explosive Device (IED), rocket propelled grenade (RPG), landmine, grenade, or enemy or friendly fire. Studies have shown that embedded fragments are not inert in the body, but may breakdown slowly over time and potentially affect an individual\u00ef\u00bf\u00bds health. The recognition of potential short and long-term health effects of embedded fragments and the large number of soldiers with injuries resulting in embedded fragments led the Presidential Task Force on Returning Global War on Terror Heroes to recommend that the VHA establish a registry and medical surveillance program for Veterans with retained fragments. The Toxic Embedded Fragment Surveillance Center (TEFSC) has been established at the Baltimore VA Medical Center to coordinate this charge. A critical component of the TEFSC medical surveillance program is the development of an Embedded Fragment Registry. This registry provides a mechanism to identify Veterans with embedded fragments, manage clinical data related to embedded fragments, and develop medical and surgical guidelines that will enable the TEFSC staff and VA clinicians to deliver appropriate medical care to these Veterans.</p>",
-            "title": "Embedded Fragments Registry (EFR)",
-            "programCode": [
-                "029:040"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2008-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Embedded Fragments Registry (EFR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/a87h-qjcf",
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
-            "identifier": "VA-OGC-022",
             "description": "<p>Impact of veteran's death on dispute regarding potential attorney's fees; Impact of accrued-benefits claim on potential attorney's fees   Author: Thompson, B.</p>",
-            "title": "OGC Precedent Opinion 4-2015",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25392,41 +25375,41 @@
                     "title": "OGC Precedent Opinion 4-2015"
                 }
             ],
+            "identifier": "VA-OGC-022",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/a87h-qjcf",
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
+            "title": "OGC Precedent Opinion 4-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/a8if-tjb9",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-07-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-28",
-            "keyword": [
-                "vre",
-                "women veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/a8if-tjb9",
             "description": "VRE - Pre and Post Rehab by gender for fy2023",
-            "title": "VRE - Pre and Post Rehab",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25434,42 +25417,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/a8if-tjb9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/a8if-tjb9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/a8if-tjb9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/a8if-tjb9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/a8if-tjb9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/a8if-tjb9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/a8if-tjb9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/a8if-tjb9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/a8if-tjb9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/a8if-tjb9",
+            "issued": "2024-07-30",
+            "keyword": [
+                "vre",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/a8if-tjb9",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-28",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VRE - Pre and Post Rehab"
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
-            "temporal": "2016-02-01T05:00:00Z/2016-02-01T05:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR39_022016_Pending_EWL_Biweekly_Desired_Date_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 February 2016"
+                }
             ],
+            "identifier": "VA-VHA-OIA-733",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -25483,70 +25495,42 @@
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
-            "identifier": "VA-VHA-OIA-733",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 February 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR39_022016_Pending_EWL_Biweekly_Desired_Date_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 February 2016"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2016-02-01T05:00:00Z/2016-02-01T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 February 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/a9ab-xfct",
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
-            "identifier": "VA-OM-OM-162",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.  Monthly CRS Totals Report 9/30/15</p>",
-            "title": "COIN 145 Monthly CRS Totals Report - 9/30/2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25554,22 +25538,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-162",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/a9ab-xfct",
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
+            "title": "COIN 145 Monthly CRS Totals Report - 9/30/2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/a9br-jwgn",
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
+            "description": "<p>The Monthly Program Cost Report (MPCR) replaces the Cost Distribution Report (CDR). The MPCR provides summary information about Veterans Affairs operational costs, Full Time Equivalents (FTE), and workload (number of patient bed days, outpatient clinic stops, etc.). MPCR receives financial data feeds from Decision Support System and workload data feeds from National Patient Care Database, Home Based Primary Care and Veterans Health Administration (VHA) Work Measurement in order to provide the VHA with a flexible cost reporting system. The MPCR is assembled from information from all Veterans Affairs Medical Centers (VAMCs). MPCR is processed monthly and consists of two reports: station level and a national level rollup. These two reports are available to users via Roger's Software Development (RSD) on the Austin Information Technology Center mainframe and CD ROM. The primary users of MPCR are the VAMC staff, VHA Budget Office, Medical Care Cost Recovery, and Deputy Assistant Secretary for Budget.</p>",
+            "identifier": "VA-VHA-FM-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "bed",
                 "clinic",
@@ -25583,65 +25586,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/a9br-jwgn",
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
-            "identifier": "VA-VHA-FM-002",
-            "description": "<p>The Monthly Program Cost Report (MPCR) replaces the Cost Distribution Report (CDR). The MPCR provides summary information about Veterans Affairs operational costs, Full Time Equivalents (FTE), and workload (number of patient bed days, outpatient clinic stops, etc.). MPCR receives financial data feeds from Decision Support System and workload data feeds from National Patient Care Database, Home Based Primary Care and Veterans Health Administration (VHA) Work Measurement in order to provide the VHA with a flexible cost reporting system. The MPCR is assembled from information from all Veterans Affairs Medical Centers (VAMCs). MPCR is processed monthly and consists of two reports: station level and a national level rollup. These two reports are available to users via Roger's Software Development (RSD) on the Austin Information Technology Center mainframe and CD ROM. The primary users of MPCR are the VAMC staff, VHA Budget Office, Medical Care Cost Recovery, and Deputy Assistant Secretary for Budget.</p>",
-            "title": "Monthly Program Cost Report (MPCR)",
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
+            "title": "Monthly Program Cost Report (MPCR)"
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
-            "identifier": "VA-VBA-ABR2012-018",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Most Prevalent Disabilities by Period of Service at the End of Fiscal Year 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25649,43 +25629,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-018",
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
+            "title": "Most Prevalent Disabilities by Period of Service at the End of Fiscal Year 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/a9qx-kvcc",
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
-            "title": "Equitable Relief Reports 2003",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25693,28 +25679,55 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/a9qx-kvcc",
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
+            "title": "Equitable Relief Reports 2003"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2004.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2004.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-10",
             "issued": "2017-07-26",
-            "temporal": "2003-10-01T04:00:00Z/2004-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2004",
                 "appeals",
@@ -25731,71 +25744,39 @@
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
-            "identifier": "VA-OIT-ITIS-10",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2004.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2004",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2004.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2003-10-01T04:00:00Z/2004-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2004"
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
-                "interments",
-                "nca",
-                "va",
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
-            "identifier": "VA-OEI-OEI-151",
             "description": "<p>This table provides a summary of Veteran interments by type of interment for fiscal years 2000 through 2014.</p>",
-            "title": "National Cemetery Administration Summary of Veteran Interments: FY2000 to FY2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25804,42 +25785,45 @@
                     "title": "National Cemetery Administration Summary of Veteran Interments: FY2000 to FY2014"
                 }
             ],
+            "identifier": "VA-OEI-OEI-151",
+            "issued": "2017-07-26",
+            "keyword": [
+                "interments",
+                "nca",
+                "va",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/",
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
+            "title": "National Cemetery Administration Summary of Veteran Interments: FY2000 to FY2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/aa48-kduw",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographic",
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
-            "identifier": "1a1418e5-0709-49c6-8411-4b6a274955a1",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Arkansas FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25847,37 +25831,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "1a1418e5-0709-49c6-8411-4b6a274955a1",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographic",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/aa48-kduw",
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
+            "title": "State Summary Arkansas FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/abgs-5mss",
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
-            "identifier": "https://www.data.va.gov/api/views/abgs-5mss",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist States and federally recognized tribal governments in the establishment, expansion, and improvement of veterans' cemeteries. Monetary assistance is provided under this program to establish, expand, and improve State or Tribal government veterans\u2019 cemeteries. Cemeteries must be State or Tribal Government owned and operated solely for the interment of eligible veterans and their dependents and/or spouses. Construction cost means the amount found necessary to convert a tract of land to an operational cemetery. The cemetery must be used solely for the interment of veterans, their wives, husbands, surviving spouses, minor children, and unmarried adult children who were physically or mentally disabled and incapable of self-support: section 38 CFR Part 38.620.</p>",
-            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM MAY2019",
-            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25885,46 +25869,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/abgs-5mss/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/abgs-5mss/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/abgs-5mss/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/abgs-5mss/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/abgs-5mss/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/abgs-5mss/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/abgs-5mss/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/abgs-5mss/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/abgs-5mss/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/abgs-5mss",
+            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
+            "issued": "2019-03-29",
+            "keyword": [
+                "cfda 64 101"
+            ],
+            "landingPage": "https://www.data.va.gov/d/abgs-5mss",
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
+            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM MAY2019"
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
-            "temporal": "2015-08-15T04:00:00Z/2015-08-15T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_PendingAccess_20150811RptDate_Final.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 August 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-422",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -25938,72 +25950,44 @@
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
-            "identifier": "VA-VHA-OIA-422",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 August 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_PendingAccess_20150811RptDate_Final.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 August 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-08-15T04:00:00Z/2015-08-15T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 August 15"
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
-            "identifier": "VA-OEI-OEI-232",
+            "dataQuality": true,
             "description": "<p>The Veteran Households with Children spreadsheet is broken out by state and county for 2015. This spreadsheet is the first time that VA has identified Veteran Households with and without children at the state and county levels.</p>",
-            "title": "Veteran Household with Children Spreadsheet FY2015",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26012,51 +25996,47 @@
                     "title": "Veteran Household with Children FY15"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-232",
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
+            "title": "Veteran Household with Children Spreadsheet FY2015"
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
-            "identifier": "VA-VBA-ABR2012-011",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Disabilities by Gender for GWOT Veterans Receiving Comp at the End of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26064,47 +26044,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-011",
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
+            "title": "Disabilities by Gender for GWOT Veterans Receiving Comp at the End of FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/abwq-ukrv",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "call",
-                "healthcare",
-                "patient",
-                "provider"
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
-            "identifier": "VA-VIA-1",
+            "dataQuality": true,
             "description": "<p>This service provides web services used to obtain call-related data for patients. Users of this service are intended to be healthcare providers</p>",
-            "title": "Call Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26113,22 +26094,53 @@
                     "title": "Call Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VIA-1",
+            "issued": "2017-11-17",
+            "keyword": [
+                "call",
+                "healthcare",
+                "patient",
+                "provider"
+            ],
+            "landingPage": "https://www.data.va.gov/d/abwq-ukrv",
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
+            "title": "Call Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/acry-f5hs",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHASAILOperations",
+                "hasEmail": "mailto:VHASAILOperations@va.gov"
+            },
+            "dataQuality": true,
+            "description": "VA Community Care Comparison or VAC3 is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.\u00a0 This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.\u00a0VAC3 data tables are updated every quarter.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/acry-f5hs/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/acry-f5hs",
             "issued": "2023-08-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-10-01/2023-09-30",
-            "modified": "2024-05-08",
             "keyword": [
                 "2023",
                 "fy2023",
@@ -26152,52 +26164,52 @@
                 "veteran",
                 "wntbva"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHASAILOperations",
-                "hasEmail": "mailto:VHASAILOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/acry-f5hs",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-05-08",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/acry-f5hs",
-            "description": "VA Community Care Comparison or VAC3 is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.\u00a0 This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.\u00a0VAC3 data tables are updated every quarter.",
-            "title": "VA Community Care Comparison (VAC3) - FY2023 All Facilities",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/acry-f5hs/application/x-zip-compressed",
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
+            "title": "VA Community Care Comparison (VAC3) - FY2023 All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/acux-mt5p",
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
+            "description": "<p>Hospitalizations for all ambulatory care sensitive conditions, for congestive heart failure, and for pneumonia.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset12_Ambulatory_Care_Sensitive_Conditions.xml",
+                    "mediaType": "application/xml",
+                    "title": "Ambulatory Care Sensitive Conditions"
+                }
             ],
+            "identifier": "VA-VHA-OIA-037",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -26220,72 +26232,44 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/acux-mt5p",
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
-            "identifier": "VA-VHA-OIA-037",
-            "description": "<p>Hospitalizations for all ambulatory care sensitive conditions, for congestive heart failure, and for pneumonia.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Ambulatory Care Sensitive Conditions",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset12_Ambulatory_Care_Sensitive_Conditions.xml",
-                    "mediaType": "application/xml",
-                    "title": "Ambulatory Care Sensitive Conditions"
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
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Ambulatory Care Sensitive Conditions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "rights": "Public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "minority",
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
-            "identifier": "VA-OEI-OEI-016",
-            "description": "<p>This report uses data from the 2011 American Community Survey to compare the demographic and socioeconomic characteristics of minority Veterans and minority non-Veterans. It also explores future projections of the minority Veteran population using VetPop 2011 and possible health issues that may affect the minority Veterans.</p>",
-            "title": "Profile of Minority Veterans",
+            "dataQuality": true,
+            "describedBy": "https://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict10.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This report uses data from the 2011 American Community Survey to compare the demographic and socioeconomic characteristics of minority Veterans and minority non-Veterans. It also explores future projections of the minority Veteran population using VetPop 2011 and possible health issues that may affect the minority Veterans.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26294,50 +26278,46 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict10.pdf",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-016",
+            "issued": "2017-07-26",
+            "keyword": [
+                "minority",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/",
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
+            "rights": "Public",
+            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Data on Minority Veterans"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Profile of Minority Veterans"
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
-            "identifier": "VA-VBA-ABR2012-111",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "North Carolina-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26346,46 +26326,47 @@
                     "title": "North Carolina-FY12 Benefits Summary"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-111",
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
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "North Carolina-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oit.va.gov/docs/OIT_CIO_Annual_Report_FY_2011_Final.pdf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "annual",
-                "cio",
-                "fy11",
-                "va"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rodney Emery",
                 "hasEmail": "mailto:rodney.emery@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-OIT-023",
             "description": "<p>CIO Annual Report for FY11</p>",
-            "title": "OIT CIO Annual Report FY 2011",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26394,45 +26375,43 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OIT-OIT-023",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual",
+                "cio",
+                "fy11",
+                "va"
+            ],
+            "landingPage": "https://www.oit.va.gov/docs/OIT_CIO_Annual_Report_FY_2011_Final.pdf",
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
+            "title": "OIT CIO Annual Report FY 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/afe7-k5a9",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-02-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "rural",
-                "rural veterans",
-                "urban",
-                "veteran",
-                "veteran population",
-                "veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/afe7-k5a9",
             "description": "The Department of Veterans Affairs provides official estimates and projections of the Veteran population using the Veteran Population Projection Model (VetPop). Based on the latest model VetPop2020 and the most recent national survey estimates from the 2021 American Community Survey 5-Year (ACS) data, the projected number of Veterans living in 50 states, DC and Puerto Rico for the fiscal years, 2021 to 2023, are allocated to Urban and Rural areas. As defined by the Census Bureau, those not residing in Urban areas are assumed to be in Rural areas (https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural/2010-urban-rural.html). \n\nThis table contains the Veteran estimates by urban/rural, gender, age group, and ethnicity.\n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2020 Urban/Rural by Ethnicity FY2021-2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26440,53 +26419,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/afe7-k5a9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/afe7-k5a9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/afe7-k5a9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/afe7-k5a9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/afe7-k5a9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/afe7-k5a9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/afe7-k5a9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/afe7-k5a9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/afe7-k5a9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/afe7-k5a9",
+            "issued": "2023-02-21",
+            "keyword": [
+                "rural",
+                "rural veterans",
+                "urban",
+                "veteran",
+                "veteran population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/afe7-k5a9",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-06",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 Urban/Rural by Ethnicity FY2021-2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/aftv-s6aw",
-            "issued": "2022-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-09",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/aftv-s6aw",
             "description": "Veterans by period of service as of 9/30/2022",
-            "title": "Period of Service, 9/30/2022",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26494,59 +26481,55 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/aftv-s6aw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aftv-s6aw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aftv-s6aw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/aftv-s6aw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aftv-s6aw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aftv-s6aw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/aftv-s6aw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aftv-s6aw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aftv-s6aw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/aftv-s6aw",
+            "issued": "2022-10-24",
+            "landingPage": "https://www.data.va.gov/d/aftv-s6aw",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-11-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Period of Service, 9/30/2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/docs/Utilization",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "1800-01-01T05:00:00Z/2012-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "interments",
-                "non-veteran casket cremain",
-                "veteran"
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
-            "identifier": "VA-NCA-MS-057",
+            "dataQuality": true,
             "description": "<p>Total Veteran and Non-Veteran Interments at National Cemetery, and shown by Interment Type of Casket or Cremain, FY2000 to FY2012.  Non-Veteran includes dependents, active duty service members, and reservists.  Cremains include in-ground, columbaria, and scattered cremains.</p>",
-            "title": "National Cemetery Administration Summary of Veteran and Non-Veteran Interments:  FY2000 to FY2012",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26555,49 +26538,46 @@
                     "title": "National Cemetery Administration Summary of Veteran and Non-Veteran Interments:  FY2000 to FY2002"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-MS-057",
+            "issued": "2017-07-26",
+            "keyword": [
+                "interments",
+                "non-veteran casket cremain",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/docs/Utilization",
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
                 "Use of Benefits and Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Cemetery Administration Summary of Veteran and Non-Veteran Interments:  FY2000 to FY2012"
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
-            "identifier": "VA-VBA-ABR2012-125",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Vermont-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26605,26 +26585,61 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-125",
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
+            "title": "Vermont-FY12 Benefits Summary"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/1_January_2015_Pending_Access_Data_using_Preferred_Date_01222015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Access Preferred Date 2015-01-22"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-070",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-01-01T05:00:00Z/2015-01-01T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -26638,70 +26653,38 @@
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
-            "identifier": "VA-VHA-OIA-070",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Jan 22",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/1_January_2015_Pending_Access_Data_using_Preferred_Date_01222015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Access Preferred Date 2015-01-22"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-01-01T05:00:00Z/2015-01-01T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Jan 22"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/agxf-p39a",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "legal help",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff M. Martin",
                 "hasEmail": "mailto:Jeffrey.Martin6@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-013",
             "description": "<p>Some VA facilities host non-VA legal service providers that can assist Veterans free of charge.</p>",
-            "title": "Legal Help for Veterans",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26710,26 +26693,55 @@
                     "title": "Legal Help for Veterans"
                 }
             ],
+            "identifier": "VA-OGC-013",
+            "issued": "2017-07-26",
+            "keyword": [
+                "legal help",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/agxf-p39a",
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
+            "title": "Legal Help for Veterans"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN19FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 19 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-091",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -26745,67 +26757,42 @@
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
-            "identifier": "VA-VHA-OIA-091",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 19",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN19FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 19 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ah7b-igy2",
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
-            "identifier": "https://www.data.va.gov/api/views/ah7b-igy2",
             "description": "These data are based on the latest Veteran Population Projection Model, VetPop2020, provided by the National Center for Veterans Statistics and Analysis, published in 2023.",
-            "title": "FY 2021_NCVAS Vet Pop Change Data For State Summaries",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26813,57 +26800,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ah7b-igy2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ah7b-igy2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ah7b-igy2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ah7b-igy2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ah7b-igy2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ah7b-igy2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ah7b-igy2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ah7b-igy2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ah7b-igy2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ah7b-igy2",
+            "issued": "2023-06-14",
+            "landingPage": "https://www.data.va.gov/d/ah7b-igy2",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Vet Pop Change Data For State Summaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ahda-pdz8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ohio",
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
-            "identifier": "VA-OEI-OEI-121",
             "description": "<p>This is a summary of the programs and services provided by VA in Ohio in fiscal year 2014.</p>",
-            "title": "State Summary:  Ohio",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26872,27 +26855,47 @@
                     "title": "State Summary:  Ohio"
                 }
             ],
+            "identifier": "VA-OEI-OEI-121",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ohio",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ahda-pdz8",
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
+            "title": "State Summary:  Ohio"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/ahm2-ztdw",
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
+            "description": "<p>This database is part of the National Medical Information System (NMIS). The Patient Treatment File (PTF) contains a record for each inpatient care episode provided under VA auspices in VA and non-VA facilities nationwide. Each episode contains data on admission, diagnosis, procedures, surgical episodes, and disposition (discharge) information and Diagnostic Related Group (DRG). Each transfer is recorded to allocate days of care properly to the service(s) responsible for that care. Recurring and special purpose reports are used for studies on patient movement trends, diagnostic frequency, workload, budget preparation, Diagnostic Related Group (DRG) assignment and accreditation requirements. Reports are available for online access via Roger's Software Development's (RSD) Online Report Viewing. Several large data files are installed on-line at the Austin Information Technology Center for remote access. Selected data can be downloaded to perform end user processing, including report generation. Information is received from a variety of modules in Veterans Health Information Systems and Technology Architecture. This batch system is written in Common Business Oriented Language and ALC. Processing is done on a daily, weekly, and monthly basis.</p>",
+            "identifier": "VA-VHA-OIA-017",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1975-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "admission",
                 "care",
@@ -26912,61 +26915,41 @@
                 "veteran",
                 "ward"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/ahm2-ztdw",
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
-            "identifier": "VA-VHA-OIA-017",
-            "description": "<p>This database is part of the National Medical Information System (NMIS). The Patient Treatment File (PTF) contains a record for each inpatient care episode provided under VA auspices in VA and non-VA facilities nationwide. Each episode contains data on admission, diagnosis, procedures, surgical episodes, and disposition (discharge) information and Diagnostic Related Group (DRG). Each transfer is recorded to allocate days of care properly to the service(s) responsible for that care. Recurring and special purpose reports are used for studies on patient movement trends, diagnostic frequency, workload, budget preparation, Diagnostic Related Group (DRG) assignment and accreditation requirements. Reports are available for online access via Roger's Software Development's (RSD) Online Report Viewing. Several large data files are installed on-line at the Austin Information Technology Center for remote access. Selected data can be downloaded to perform end user processing, including report generation. Information is received from a variety of modules in Veterans Health Information Systems and Technology Architecture. This batch system is written in Common Business Oriented Language and ALC. Processing is done on a daily, weekly, and monthly basis.</p>",
-            "title": "Patient Treatment File (PTF)",
-            "programCode": [
-                "029:040"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1975-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Patient Treatment File (PTF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ahvc-pqda",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-10-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-10",
-            "keyword": [
-                "class of work",
-                "veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/ahvc-pqda",
             "description": "",
-            "title": "Veterans Class of Work",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26974,58 +26957,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ahvc-pqda/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ahvc-pqda/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ahvc-pqda/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ahvc-pqda/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ahvc-pqda/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ahvc-pqda/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ahvc-pqda/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ahvc-pqda/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ahvc-pqda/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ahvc-pqda",
+            "issued": "2024-10-01",
+            "keyword": [
+                "class of work",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ahvc-pqda",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-10",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Class of Work"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/aijs-q9hs",
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
-            "identifier": "https://www.data.va.gov/api/views/aijs-q9hs",
             "description": "",
-            "title": "Table 5 - U. S. Veterans Life Table for Male 2000-2009",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27033,39 +27015,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/aijs-q9hs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aijs-q9hs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aijs-q9hs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/aijs-q9hs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aijs-q9hs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aijs-q9hs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/aijs-q9hs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aijs-q9hs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aijs-q9hs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/aijs-q9hs",
+            "issued": "2023-04-18",
+            "keyword": [
+                "death rate",
+                "life expectancy",
+                "life table"
+            ],
+            "landingPage": "https://www.data.va.gov/d/aijs-q9hs",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Table 5 - U. S. Veterans Life Table for Male 2000-2009"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2000.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2000.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-14",
             "issued": "2017-07-26",
-            "temporal": "1999-10-01T04:00:00Z/2000-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2000",
                 "appeals",
@@ -27082,96 +27095,95 @@
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
-            "identifier": "VA-OIT-ITIS-14",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2000.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2000",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2000.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "1999-10-01T04:00:00Z/2000-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2000"
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
-                "chapter 31 subsistence",
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
-            "identifier": "VA-VBA-INFO-017",
+            "dataQuality": true,
             "description": "<p>Standard Ch31 Subsistence Rates  from VRE</p>",
-            "title": "Standard Ch31 Subsistence Rates - VRE",
+            "identifier": "VA-VBA-INFO-017",
             "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "chapter 31 subsistence",
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
+            "title": "Standard Ch31 Subsistence Rates - VRE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/aizy-unmw",
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
+            "description": "<p>Represents patient satisfaction based on survey data broken out by inpatient/outpatient and stratified ethnicity.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset11_Patient_Satisfaction.xml",
+                    "mediaType": "application/xml",
+                    "title": "Patient Satisfaction"
+                }
             ],
+            "identifier": "VA-VHA-OIA-045",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -27194,75 +27206,42 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/aizy-unmw",
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
-            "identifier": "VA-VHA-OIA-045",
-            "description": "<p>Represents patient satisfaction based on survey data broken out by inpatient/outpatient and stratified ethnicity.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Patient Satisfaction",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset11_Patient_Satisfaction.xml",
-                    "mediaType": "application/xml",
-                    "title": "Patient Satisfaction"
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
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Patient Satisfaction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY_08_Insurance_Expenditure_by_County_and_State.csv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-01-01T05:00:00Z/2008-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www1.va.gov/VETDATA/docs/Datagov/FY_08_Insurance_Expenditure_by_County_and_State.csv"
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
-            "identifier": "VA-VBA-INS2008-001",
+            "dataQuality": true,
             "description": "<p>2008 Veteran life insurance expenditures by state and county.   Expenditures represented the actual disbursements from Insurance's Award and Inforce systems.</p>",
-            "title": "2008 Veterans' Insurance Expenditure by State and County",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27270,95 +27249,94 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/aj7p-yvuh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aj7p-yvuh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aj7p-yvuh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/aj7p-yvuh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aj7p-yvuh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aj7p-yvuh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/aj7p-yvuh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aj7p-yvuh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aj7p-yvuh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2008-001",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "insurance",
+                "veteran"
+            ],
+            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY_08_Insurance_Expenditure_by_County_and_State.csv",
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
+                "https://www1.va.gov/VETDATA/docs/Datagov/FY_08_Insurance_Expenditure_by_County_and_State.csv"
+            ],
+            "temporal": "2008-01-01T05:00:00Z/2008-12-31T05:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2008 Veterans' Insurance Expenditure by State and County"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/aj8q-vjvh",
-            "issued": "2023-08-10",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-19",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Texas FY2021",
+            "identifier": "https://www.data.va.gov/api/views/aj8q-vjvh",
+            "issued": "2023-08-10",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "texas"
             ],
-            "identifier": "https://www.data.va.gov/api/views/aj8q-vjvh",
+            "landingPage": "https://www.data.va.gov/d/aj8q-vjvh",
+            "modified": "2024-06-19",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Texas FY2021",
             "title": "NCVAS State Summary Texas FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policyholders_by_program_by_state_April_2012.CSV",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-04-01T04:00:00Z/2012-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Policyholders_by_Program_April_2012.doc"
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
-            "identifier": "VA-VBA-INS2012-007",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policyholders for each administered life insurance program listed by state. Data is current as of 04/30/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Number of Life Insurance Policyholders by Program by State 2012/04/30",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27366,67 +27344,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ajhv-9pjw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ajhv-9pjw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ajhv-9pjw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ajhv-9pjw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ajhv-9pjw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ajhv-9pjw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ajhv-9pjw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ajhv-9pjw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ajhv-9pjw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-007",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policyholders_by_program_by_state_April_2012.CSV",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Policyholders_by_Program_April_2012.doc"
+            ],
+            "temporal": "2012-04-01T04:00:00Z/2012-04-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Life Insurance Policyholders by Program by State 2012/04/30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ajhz-kudy",
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
-            "identifier": "https://www.data.va.gov/api/views/ajhz-kudy",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE NOV2018",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27434,61 +27417,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ajhz-kudy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ajhz-kudy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ajhz-kudy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ajhz-kudy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ajhz-kudy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ajhz-kudy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ajhz-kudy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ajhz-kudy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ajhz-kudy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/ajhz-kudy",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ajhz-kudy",
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
+            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE NOV2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/aji8-5vsz",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "florida",
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
-            "identifier": "VA-OEI-OEI-094",
             "description": "<p>This is a summary of the programs and services provided by VA in Florida in fiscal year 2014.</p>",
-            "title": "State Summary:  Florida",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27497,27 +27480,43 @@
                     "title": "State Summary:  Florida"
                 }
             ],
+            "identifier": "VA-OEI-OEI-094",
+            "issued": "2017-07-26",
+            "keyword": [
+                "florida",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/aji8-5vsz",
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
+            "title": "State Summary:  Florida"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ajqx-r8gc",
-            "issued": "2022-12-09",
             "@type": "dcat:Dataset",
-            "modified": "2023-01-12",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
+            "description": "Introduction to a three-part study on Veterans who have used at least one of 22 benefits or services (referred to as \"users\") provided by VA during Fiscal Years 2010 through 2021.",
+            "identifier": "https://www.data.va.gov/api/views/ajqx-r8gc",
+            "issued": "2022-12-09",
             "keyword": [
                 "utilization",
                 "va programs",
@@ -27526,42 +27525,27 @@
                 "veterans",
                 "veterans benefits"
             ],
-            "identifier": "https://www.data.va.gov/api/views/ajqx-r8gc",
+            "landingPage": "https://www.data.va.gov/d/ajqx-r8gc",
+            "modified": "2023-01-12",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Introduction to a three-part study on Veterans who have used at least one of 22 benefits or services (referred to as \"users\") provided by VA during Fiscal Years 2010 through 2021.",
             "title": "Use of VA Benefits and Services: 2021 (Introduction)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/am3n-jg4e",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-14",
-            "keyword": [
-                "cfda 64 100"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:Annette.Brown2@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/am3n-jg4e",
+            "dataQuality": true,
```

