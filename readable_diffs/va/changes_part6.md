# Change History for va.json (Part 6)

### Changes from 31606f9 to dd2190f (Part 6/7)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "identifier": "https://www.data.va.gov/api/views/r6kz-mc37",
+            "dataQuality": true,
             "description": "The Harms dataset includes information on serious adverse events and participant withdrawals from the studies due to adverse events. Adverse events are reported as the percent of participants within a treatment group that experienced an adverse event or who withdrew from the study. Detail on the specific adverse event or reason for withdrawal is provided when available. This dataset also reports on the percentage of patients who attempted or completed suicide (when available).\nValues abstracted as \"NA\" or \"NR\" from the study are represented as null values/empty cells in this dataset.\nStudy level variables like military status and percent female are included for filtering purposes",
-            "title": "Harms",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69365,64 +69349,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/r6kz-mc37/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/r6kz-mc37/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/r6kz-mc37/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/r6kz-mc37/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/r6kz-mc37/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/r6kz-mc37/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/r6kz-mc37/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/r6kz-mc37/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/r6kz-mc37/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "PTSD-Repository"
+            "identifier": "https://www.data.va.gov/api/views/r6kz-mc37",
+            "issued": "2022-09-29",
+            "keyword": [
+                "harms",
+                "ptsd-repository"
             ],
+            "landingPage": "https://www.data.va.gov/d/r6kz-mc37",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2023-09-06",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
+            "theme": [
+                "PTSD-Repository"
+            ],
+            "title": "Harms"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r6wi-ujk5",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "louisiana",
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
-            "identifier": "VA-OEI-OEI-105",
             "description": "<p>This is a summary of the programs and services provided by VA in Louisiana in fiscal year 2014.</p>",
-            "title": "State Summary:  Louisiana",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69431,53 +69414,82 @@
                     "title": "State Summary:  Louisiana"
                 }
             ],
+            "identifier": "VA-OEI-OEI-105",
+            "issued": "2017-07-26",
+            "keyword": [
+                "louisiana",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r6wi-ujk5",
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
+            "title": "State Summary:  Louisiana"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r72w-cp7u",
-            "issued": "2023-07-18",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-16",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary North Carolina FY2021",
+            "identifier": "https://www.data.va.gov/api/views/r72w-cp7u",
+            "issued": "2023-07-18",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "north carolina"
             ],
-            "identifier": "https://www.data.va.gov/api/views/r72w-cp7u",
+            "landingPage": "https://www.data.va.gov/d/r72w-cp7u",
+            "modified": "2024-06-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary North Carolina FY2021",
             "title": "NCVAS State Summary North Carolina FY2021"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN16FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 16 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-088",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -69493,71 +69505,43 @@
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
-            "identifier": "VA-VHA-OIA-088",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 16",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN16FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 16 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 16"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r88w-z7g6",
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
-            "identifier": "c4605e25-f851-4a3d-8ba0-73ea4b65d9b5",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Utah FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69565,43 +69549,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "c4605e25-f851-4a3d-8ba0-73ea4b65d9b5",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r88w-z7g6",
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
+            "title": "State Summary Utah FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r8hi-8mp6",
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
-            "identifier": "db6a54e3-0ca8-420b-9d79-d2adc8f62334",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Virginia FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69609,122 +69593,123 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "db6a54e3-0ca8-420b-9d79-d2adc8f62334",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r8hi-8mp6",
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
+            "title": "State Summary Virginia FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r8hi-e3p7",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAMS to provide, through purchase and/or fabrication, prosthetic and related appliances, equipment and services to eligible veterans so that they may live and work as productive citizens. Veterans eligible for prosthetic services are service-connected veterans seeking care for a service-connected disability; veterans with compensable service-connected disabilities generally rated 10 percent or more; former prisoners of war, veterans discharged or released from active military service for a disability that was incurred or aggravated in the line of duty, and veterans who are in receipt of Section 1151 benefits; veterans who are in receipt of increased pension based on a need of regular aid and attendance or by reason of being permanently housebound; veterans who have annual income and net worth below the \"means test\" threshold; all other veterans who are not required to pay a copayment for their care, i.e., veterans of the Mexican border period and World War I, compensated zero (0) percent service-connected veterans who are receiving statutory awards, veterans exposed to a toxic substance, radiation or environmental hazard (limited to certain disabilities); and veterans who must pay a copayment for their care. Ineligible veterans are nonservice-connected veterans residing or sojourning in foreign lands.</p>",
-            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES FY2019",
-            "programCode": [
-                "029:003"
+            "identifier": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 116"
             ],
+            "landingPage": "https://www.data.va.gov/d/r8hi-e3p7",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r8zf-rv7r",
-            "bureauCode": [
-                "029:25"
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
             ],
-            "rights": "This data asset points to publicly available ABR reports developed by VBA's PA&I (20B)",
-            "issued": "2021-12-06",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-06",
-            "keyword": [
-                "benefits",
-                "benefits participation rates",
-                "dependent benefits usage",
-                "veterans"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES FY2019"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
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
-            "identifier": "https://www.data.va.gov/api/views/r8zf-rv7r",
             "description": "The Annual Benefits Report (ABR) summarizes the benefit programs delivered by VBA, identifies the current level of program participation, and profiles the beneficiaries. The report is intended to accomplish the following:\n1--Present a clear, complete, data-driven picture of the extent to which Veterans and their dependents use these benefits: and\n2--Provide insights into the nature of the benefit programs.",
-            "title": "VBA Annual Benefits Report (1999-current)",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.benefits.va.gov/REPORTS/abr/docs/2020_ABR.pdf",
-                    "description": "VBA Annual Benefits Report current year and Archive Link.   The current annual report is usually updated by end of the first quarter of the following calendar year and is available via the first link (PDF).  Archived ABRs may be be accessed by the second link (ASP).\n\nThe Annual Benefits Report (ABR) summarizes the benefit programs delivered by VBA, identifies the current level of program participation, and profiles the beneficiaries. The report is intended to present a clear, complete, data-driven picture of the extent to which Veterans and their dependents use these benefits, and provide insights into the nature of the benefit programs.",
                     "@type": "dcat:Distribution",
+                    "description": "VBA Annual Benefits Report current year and Archive Link.   The current annual report is usually updated by end of the first quarter of the following calendar year and is available via the first link (PDF).  Archived ABRs may be be accessed by the second link (ASP).\n\nThe Annual Benefits Report (ABR) summarizes the benefit programs delivered by VBA, identifies the current level of program participation, and profiles the beneficiaries. The report is intended to present a clear, complete, data-driven picture of the extent to which Veterans and their dependents use these benefits, and provide insights into the nature of the benefit programs.",
+                    "downloadURL": "https://www.benefits.va.gov/REPORTS/abr/docs/2020_ABR.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Veterans Benefits Administration Report---1999-current"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.benefits.va.gov/REPORTS/abr/archive.asp",
-                    "description": "VBA Annual Benefits Report current year and Archive Link.   The current annual report is usually updated by end of the first quarter of the following calendar year and is available via the first link (PDF).  Archived ABRs may be be accessed by the second link (ASP).\n\nThe Annual Benefits Report (ABR) summarizes the benefit programs delivered by VBA, identifies the current level of program participation, and profiles the beneficiaries. The report is intended to present a clear, complete, data-driven picture of the extent to which Veterans and their dependents use these benefits, and provide insights into the nature of the benefit programs.",
                     "@type": "dcat:Distribution",
+                    "description": "VBA Annual Benefits Report current year and Archive Link.   The current annual report is usually updated by end of the first quarter of the following calendar year and is available via the first link (PDF).  Archived ABRs may be be accessed by the second link (ASP).\n\nThe Annual Benefits Report (ABR) summarizes the benefit programs delivered by VBA, identifies the current level of program participation, and profiles the beneficiaries. The report is intended to present a clear, complete, data-driven picture of the extent to which Veterans and their dependents use these benefits, and provide insights into the nature of the benefit programs.",
+                    "downloadURL": "https://www.benefits.va.gov/REPORTS/abr/archive.asp",
+                    "mediaType": "text/html",
                     "title": "Veterans Benefits Administration Report---1999-current"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/r8zf-rv7r",
+            "issued": "2021-12-06",
+            "keyword": [
+                "benefits",
+                "benefits participation rates",
+                "dependent benefits usage",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r8zf-rv7r",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-12-06",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "This data asset points to publicly available ABR reports developed by VBA's PA&I (20B)",
+            "title": "VBA Annual Benefits Report (1999-current)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/r95b-ba7t",
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
-            "identifier": "https://www.data.va.gov/api/views/r95b-ba7t",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) items also on Federal Employee Viewpoint Survey, reported as percents as required per Federal statute.",
-            "title": "AES 2019 FEVS Percents",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69732,38 +69717,37 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/r95b-ba7t",
+            "issued": "2023-03-16",
+            "keyword": [
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/r95b-ba7t",
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
+            "title": "AES 2019 FEVS Percents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ra9c-d3ke",
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
-            "identifier": "https://www.data.va.gov/api/views/ra9c-d3ke",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to compensate veterans for disabilities incurred or aggravated during military service according to the average impairment in earning capacity such disability would cause in civilian occupations. Persons who have suffered disabilities resulting from service in the Armed Forces of the United States. The disability must have been incurred or aggravated by service in the line of duty. Separation from service must have been under other than dishonorable conditions for the period in which the disability was incurred or aggravated.</p>",
-            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY MAY2019",
-            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69771,62 +69755,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ra9c-d3ke/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ra9c-d3ke/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ra9c-d3ke/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ra9c-d3ke/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ra9c-d3ke/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ra9c-d3ke/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ra9c-d3ke/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ra9c-d3ke/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ra9c-d3ke/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/ra9c-d3ke",
+            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 109"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ra9c-d3ke",
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
+            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rb9m-86xp",
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
-            "identifier": "https://www.data.va.gov/api/views/rb9m-86xp",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE JAN2019",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69834,44 +69817,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rb9m-86xp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rb9m-86xp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rb9m-86xp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/rb9m-86xp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rb9m-86xp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rb9m-86xp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rb9m-86xp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rb9m-86xp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rb9m-86xp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/rb9m-86xp",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rb9m-86xp",
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
+            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/rbgi-mv2f",
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
+            "description": "<p>The Converged Registries Solution (CRS) has been replaced by the Veterans Integrated Registries Platform (VIRP).  The information contained in this entry discusses the CRS prior to its replacement.  The Converged Registries platform was a hardware and software architecture designed to host individual patient registries and eliminate duplicative development effort while maximizing VAs ability to create new patient registries.  The common platform included a relational database, software classes, security modules, extraction services and other components.  The Converged Registries obtained data from the Corporate Data Warehouse (CDW), directly from the Veterans Health Information Systems and Technology Architecture (VistA) as well as by direct user input. Registries Projects - Embedded Fragment Registry (EFR), Eye Injury Data Store, Traumatic Brain Injury (TBI) Registry and Veterans Implant Tracking and Alert System (VITAS).</p>",
+            "identifier": "VA-VHA-OIA-005",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "health",
                 "platform",
@@ -69881,62 +69884,42 @@
                 "vista",
                 "warehouse"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/rbgi-mv2f",
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
-            "identifier": "VA-VHA-OIA-005",
-            "description": "<p>The Converged Registries Solution (CRS) has been replaced by the Veterans Integrated Registries Platform (VIRP).  The information contained in this entry discusses the CRS prior to its replacement.  The Converged Registries platform was a hardware and software architecture designed to host individual patient registries and eliminate duplicative development effort while maximizing VAs ability to create new patient registries.  The common platform included a relational database, software classes, security modules, extraction services and other components.  The Converged Registries obtained data from the Corporate Data Warehouse (CDW), directly from the Veterans Health Information Systems and Technology Architecture (VistA) as well as by direct user input. Registries Projects - Embedded Fragment Registry (EFR), Eye Injury Data Store, Traumatic Brain Injury (TBI) Registry and Veterans Implant Tracking and Alert System (VITAS).</p>",
-            "title": "Converged Registries Solution (CRS)",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2011-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Converged Registries Solution (CRS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/rbjg-6ka2",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cpe",
-                "eligibility"
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
-            "identifier": "VA-ORCH-6",
+            "dataQuality": true,
             "description": "<p>Web service proxy/wrapper for CP&amp;E capabilities/data. This interface will retrieve a Bill of Collection record from CP&amp;E and enable a CRM user to view the Bill information. Back office CRM users (primarily DCU Unit) require the ability to review Bills to respond to customer inquiries about Bills and Offsets. The interface will be triggered when a user attempts to query for a Bill using the Bill # (K#).</p>",
-            "title": "CP&E Eligibility Adapters Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69945,22 +69928,52 @@
                     "title": "CP&E Eligibility Adapters Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-6",
+            "issued": "2017-11-17",
+            "keyword": [
+                "cpe",
+                "eligibility"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rbjg-6ka2",
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
+            "title": "CP&E Eligibility Adapters Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rc4s-93qz",
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
+                    "downloadURL": "https://www.data.va.gov/download/rc4s-93qz/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/rc4s-93qz",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2022-08-22",
-            "@type": "dcat:Dataset",
-            "temporal": "2021-10-01/2022-09-30",
-            "modified": "2023-03-21",
             "keyword": [
                 "2022",
                 "analytics",
@@ -69983,98 +69996,69 @@
                 "sail",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHASailOperations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/rc4s-93qz",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-03-21",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/rc4s-93qz",
-            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).",
-            "title": "SAIL FY2022 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/rc4s-93qz/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2021-10-01/2022-09-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAIL FY2022 Hospital Performance - All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/rd2u-r3i2",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Virginia FY2023",
+            "identifier": "https://www.data.va.gov/api/views/rd2u-r3i2",
             "issued": "2024-06-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "virginia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/rd2u-r3i2",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/rd2u-r3i2",
-            "description": "NCVAS State Summary Virginia FY2023",
-            "title": "NCVAS State Summary Virginia FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Virginia FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/rd3i-9sv2",
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
-            "identifier": "c261c11c-8594-4fc3-a771-fa4b0fda1ef0",
+            "dataQuality": true,
             "description": "<p>Collect and combine data from multiple internal and external data sources for exposure to consumers. Data for any individual is made available via a standard set of hierarchical HTTP resources through the Read Service. The VRS calls the ISIC external Producer endpoints to fetch and aggregate Care Coordinator Profiles VLER document type data and convert it to an XML Atom feed format for the Consumer.</p>",
-            "title": "Aggregation Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70083,60 +70067,61 @@
                     "title": "Aggregation Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "c261c11c-8594-4fc3-a771-fa4b0fda1ef0",
+            "issued": "2018-02-23",
+            "keyword": [
+                "aggregation"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rd3i-9sv2",
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
+            "title": "Aggregation Service"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rdda-xpre",
-            "issued": "2023-06-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-29",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Idaho FY2021",
+            "identifier": "https://www.data.va.gov/api/views/rdda-xpre",
+            "issued": "2023-06-27",
             "keyword": [
                 "fy2021 data",
                 "idaho",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/rdda-xpre",
+            "landingPage": "https://www.data.va.gov/d/rdda-xpre",
+            "modified": "2024-05-29",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Idaho FY2021",
             "title": "NCVAS State Summary Idaho FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rdpw-mtbs",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2024-08-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-20",
-            "keyword": [
-                "employee engagement"
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
-            "identifier": "https://www.data.va.gov/api/views/rdpw-mtbs",
             "description": "VA All Employee Survey (AES) items also on Federal Employee Viewpoint Survey, reported as percents as required per Federal statute.",
-            "title": "AES 2024 FEVS Percents",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70144,58 +70129,56 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rdpw-mtbs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rdpw-mtbs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rdpw-mtbs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/rdpw-mtbs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rdpw-mtbs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rdpw-mtbs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rdpw-mtbs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rdpw-mtbs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rdpw-mtbs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/rdpw-mtbs",
+            "issued": "2024-08-01",
+            "keyword": [
+                "employee engagement"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rdpw-mtbs",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2024-09-20",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "AES 2024 FEVS Percents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rejs-3diz",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "demographics",
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
-            "identifier": "VA-OEI-OEI-157",
             "description": "<p>This report summarizes results from several profiles produced in the last year.</p>",
-            "title": "Selected Research Highlights",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70204,25 +70187,45 @@
                     "title": "Selected Research Highlights"
                 }
             ],
+            "identifier": "VA-OEI-OEI-157",
+            "issued": "2017-07-26",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rejs-3diz",
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
+            "title": "Selected Research Highlights"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/rfmm-8zsr",
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
+            "description": "<p>The Veterans Health Administration (VHA) Resident Supervision Handbook (VHA Handbook 1400.1) requires facility directors to report annually the status of their residency training programs to their Veterans Integrated Service Network (VISN) Director. VISN Directors review and then forward those reports to the VHA Chief Academic Affiliations Officer. This database enables electronic, paperless reporting of this information from VA Medical Centers to the VISN and from the VISN to the Office of Academic Affiliations.</p>",
+            "identifier": "VA-VHA-OAA-004",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2002-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "academic",
                 "residency",
@@ -70232,60 +70235,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/rfmm-8zsr",
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
-            "identifier": "VA-VHA-OAA-004",
-            "description": "<p>The Veterans Health Administration (VHA) Resident Supervision Handbook (VHA Handbook 1400.1) requires facility directors to report annually the status of their residency training programs to their Veterans Integrated Service Network (VISN) Director. VISN Directors review and then forward those reports to the VHA Chief Academic Affiliations Officer. This database enables electronic, paperless reporting of this information from VA Medical Centers to the VISN and from the VISN to the Office of Academic Affiliations.</p>",
-            "title": "Annual Report of Residency Training Programs (ARRTP)",
-            "programCode": [
-                "029:040"
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
+            "title": "Annual Report of Residency Training Programs (ARRTP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rfms-xysn",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-06-01T04:00:00Z/2015-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
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
-            "identifier": "VA-OM-OM-143",
+            "dataQuality": true,
             "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "June 2015 Coin 0022",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70293,43 +70277,43 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-143",
+            "issued": "2017-07-26",
+            "keyword": [
+                "establishments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rfms-xysn",
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
+            "title": "June 2015 Coin 0022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rfz9-i4ms",
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
-            "identifier": "542460e4-9f8d-47a1-b563-a8c555052a07",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Texas FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70337,40 +70321,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "542460e4-9f8d-47a1-b563-a8c555052a07",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rfz9-i4ms",
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
+            "title": "State Summary Texas FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rh54-rye2",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "veteran employment rates",
-                "veteran employment rates by age",
-                "veteran employment rates by gender",
-                "veteran employment rates by period of service",
-                "veteran employment statistics"
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
-            "identifier": "VA-OEI-OEI-101-102",
+            "dataQuality": true,
             "description": "<p>Details include presentation of Veterans Employment rates by gender, age, and period of service.</p>",
-            "title": "Veterans Employment 2000 to 2013",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70378,42 +70359,43 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-101-102",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veteran employment rates",
+                "veteran employment rates by age",
+                "veteran employment rates by gender",
+                "veteran employment rates by period of service",
+                "veteran employment statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rh54-rye2",
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
+            "title": "Veterans Employment 2000 to 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rh6c-gvvp",
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
-            "identifier": "https://www.data.va.gov/api/views/rh6c-gvvp",
+            "dataQuality": true,
             "description": "<p>This dataset contains information on minority veteran healthcare usage, educational attainment, unemployment rates, median income, and projected population figures.</p>",
-            "title": "Veterans with Service Connected Disability Using VA Healthcare by Race/Ethnicity",
-            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70421,62 +70403,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rh6c-gvvp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rh6c-gvvp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rh6c-gvvp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/rh6c-gvvp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rh6c-gvvp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rh6c-gvvp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rh6c-gvvp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rh6c-gvvp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rh6c-gvvp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/rh6c-gvvp",
+            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
+            "issued": "2017-03-15",
+            "keyword": [
+                "health care",
+                "income",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rh6c-gvvp",
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
+            "title": "Veterans with Service Connected Disability Using VA Healthcare by Race/Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rhg7-ud9c",
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
-            "title": "Equitable Relief Reports 2002",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70484,76 +70470,75 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rhg7-ud9c",
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
+            "title": "Equitable Relief Reports 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/rhj2-6ahb",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "illinois",
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
-            "identifier": "https://www.data.va.gov/api/views/rhj2-6ahb",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Illinois",
+            "identifier": "https://www.data.va.gov/api/views/rhj2-6ahb",
+            "issued": "2021-08-26",
+            "keyword": [
+                "illinois",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rhj2-6ahb",
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
+            "title": "State Summaries_Illinois"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ri6s-s648",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-06-28",
-            "@type": "dcat:Dataset",
-            "modified": "2021-08-27",
-            "keyword": [
-                "nvcas",
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
-            "identifier": "https://www.data.va.gov/api/views/ri6s-s648",
+            "dataQuality": true,
             "description": "This dataset is comprised of 1 year estimate data from the American Community Survey published as of 2019.",
-            "title": "NCVAS State Summaries - POS Percentages (chart)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70561,61 +70546,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ri6s-s648/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ri6s-s648/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ri6s-s648/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ri6s-s648/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ri6s-s648/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ri6s-s648/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ri6s-s648/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ri6s-s648/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ri6s-s648/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/ri6s-s648",
+            "issued": "2021-06-28",
+            "keyword": [
+                "nvcas",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ri6s-s648",
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
+            "title": "NCVAS State Summaries - POS Percentages (chart)"
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
-            "temporal": "2004-01-01T05:00:00Z/2004-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-015",
+            "dataQuality": true,
             "description": "<p>2004 VA Performance and Accountability Report.</p>",
-            "title": "2004 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70624,45 +70607,45 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-015",
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
+            "temporal": "2004-01-01T05:00:00Z/2004-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2004 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/FUND/Strategic_Plans.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2005-01-01T05:00:00Z/2010-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "franchise fund",
-                "strategic plan"
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
-            "identifier": "VA-OM-OM-043",
+            "dataQuality": true,
             "description": "<p>Department of Veterans Affairs Franchise Fund Strategic Plan 2005-2010</p>",
-            "title": "Department of Veterans Affairs Franchise Fund Strategic Plan 2005-2010",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70671,48 +70654,45 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-043",
+            "issued": "2017-07-26",
+            "keyword": [
+                "franchise fund",
+                "strategic plan"
+            ],
+            "landingPage": "https://www.va.gov/FUND/Strategic_Plans.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2005-01-01T05:00:00Z/2010-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Franchise Fund Strategic Plan 2005-2010"
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
-            "temporal": "2011-01-10T05:00:00Z/2012-09-30T04:00:00Z",
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
-            "identifier": "VA-VBA-ABR2012-086",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "District of Columbia-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70720,44 +70700,48 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-086",
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
+            "temporal": "2011-01-10T05:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "District of Columbia-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/riw3-s4nt",
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
-            "identifier": "379ea790-b699-4075-8795-26c890c22f13",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Michigan FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70765,78 +70749,74 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "379ea790-b699-4075-8795-26c890c22f13",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/riw3-s4nt",
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
+            "title": "State Summary Michigan FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/rjy3-fryf",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Michigan FY2023",
+            "identifier": "https://www.data.va.gov/api/views/rjy3-fryf",
             "issued": "2024-06-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fy2024",
                 "michigan",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/rjy3-fryf",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/rjy3-fryf",
-            "description": "NCVAS State Summary Michigan FY2023",
-            "title": "NCVAS State Summary Michigan FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Michigan FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Tech_Doc_for_Education_Recipients_by_Training_Type.doc",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-07-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/FY11July_EDU_recp_by_Training_Type.csv"
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
-            "identifier": "VA-VBA-EDU2011-007",
+            "dataQuality": true,
             "description": "<p>FY 2011 VA Education Recipients by training type  and VA Education Benefit Program (Through July FY11). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2011(Through the July FY11). Training type statistics may include individuals who used their education benefits in more than one training type, therefore the total within this table may be different than the total number of beneficiaries during the fiscal year.</p>",
-            "title": "FY 2011 Use of VA Education Benefits by Training Type and VA Education Benefit Program",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70844,100 +70824,100 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rkm5-jfba/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rkm5-jfba/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rkm5-jfba/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/rkm5-jfba/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rkm5-jfba/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rkm5-jfba/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rkm5-jfba/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rkm5-jfba/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rkm5-jfba/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2011-007",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Tech_Doc_for_Education_Recipients_by_Training_Type.doc",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/FY11July_EDU_recp_by_Training_Type.csv"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-07-31T04:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2011 Use of VA Education Benefits by Training Type and VA Education Benefit Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/rn4h-hxd7",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary New Mexico FY2023",
+            "identifier": "https://www.data.va.gov/api/views/rn4h-hxd7",
             "issued": "2024-06-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "new mexico"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/rn4h-hxd7",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/rn4h-hxd7",
-            "description": "NCVAS State Summary New Mexico FY2023",
-            "title": "NCVAS State Summary New Mexico FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary New Mexico FY2023"
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
-            "identifier": "VA-VBA-ABR2012-097",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Maine-FY Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70945,47 +70925,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-097",
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
+            "title": "Maine-FY Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/homeloans/documents/docs/foreclosure_avoidance_fact_sheet.pdf",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-04-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "delinquency assistance",
-                "loan guaranty service",
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
-            "identifier": "VA-VBA-INFO-019",
+            "dataQuality": true,
             "description": "<p>Delinquency Assistance info- Loan Guaranty Service</p>",
-            "title": "Delinquency Assistance info- Loan Guaranty Service",
-            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70994,56 +70975,51 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INFO-019",
+            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "delinquency assistance",
+                "loan guaranty service",
+                "vba benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/homeloans/documents/docs/foreclosure_avoidance_fact_sheet.pdf",
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
+            "temporal": "2013-04-01T04:00:00Z/2014-12-30T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delinquency Assistance info- Loan Guaranty Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rqvv-zp9h",
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
-            "identifier": "VA-VHA-OIA-030",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset represents patient satisfaction based on survey data broken out by ethnicity.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Patient Satisfaction",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset represents patient satisfaction based on survey data broken out by ethnicity.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71051,96 +71027,104 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rqvv-zp9h/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rqvv-zp9h/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rqvv-zp9h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/rqvv-zp9h/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rqvv-zp9h/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rqvv-zp9h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rqvv-zp9h/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rqvv-zp9h/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rqvv-zp9h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-030",
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
+            "landingPage": "https://www.data.va.gov/d/rqvv-zp9h",
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
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Patient Satisfaction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/rrgh-fkt8",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "Archived State Summary Landing Page",
+            "identifier": "https://www.data.va.gov/api/views/rrgh-fkt8",
             "issued": "2024-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-13",
             "keyword": [
                 "archived",
                 "ncvas",
                 "state summaries"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/rrgh-fkt8",
+            "modified": "2024-02-13",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/rrgh-fkt8",
-            "description": "Archived State Summary Landing Page",
-            "title": "Archived State Summary Landing Page",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "Archived State Summary Landing Page"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rsgt-etcb",
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
-            "identifier": "49251859-bd45-4661-850e-4eb0c0a25679",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Wyoming FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71148,56 +71132,55 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "49251859-bd45-4661-850e-4eb0c0a25679",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rsgt-etcb",
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
+            "title": "State Summary Wyoming FY2016"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rssm-v4rt",
-            "issued": "2024-10-31",
             "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Henrietta Bynem",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "",
             "identifier": "https://www.data.va.gov/api/views/rssm-v4rt",
+            "issued": "2024-10-31",
+            "landingPage": "https://www.data.va.gov/d/rssm-v4rt",
+            "modified": "2024-10-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "",
             "title": "How to Access Synthetic Data in the VA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rtmm-hjaz",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-09-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "keyword": [
-                "healthcare",
-                "mental health"
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
-            "identifier": "https://www.data.va.gov/api/views/rtmm-hjaz",
             "description": "Summary level data from the National Veteran Health Equity Report - FY2013, filtered by mental illness.",
-            "title": "VA-OHE-NVHER-FY13-Sociodemographic-Mental-Illness",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71205,75 +71188,104 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rtmm-hjaz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rtmm-hjaz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rtmm-hjaz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/rtmm-hjaz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rtmm-hjaz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rtmm-hjaz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/rtmm-hjaz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/rtmm-hjaz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/rtmm-hjaz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/rtmm-hjaz",
+            "issued": "2019-09-19",
+            "keyword": [
+                "healthcare",
+                "mental health"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rtmm-hjaz",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA-OHE-NVHER-FY13-Sociodemographic-Mental-Illness"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ru26-46qf",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located.</p>",
-            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS FY2019",
+            "identifier": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 114"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ru26-46qf",
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
+            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS FY2019"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN11FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 11 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-085",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -71289,80 +71301,46 @@
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
-            "identifier": "VA-VHA-OIA-085",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 11",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN11FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 11 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 11"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rw54-s8nj",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-21",
-            "references": [
-                "https://search.usa.gov/search/docs?affiliate=bvadecisions"
-            ],
-            "keyword": [
-                "appeal",
-                "appeals",
-                "appeals decisions",
-                "board of veterans appeals",
-                "bva",
-                "bva decisions"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kary Charlebois",
                 "hasEmail": "mailto:Kary.Charlebois@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-BVA-BVA-001",
-            "description": "<p>The Board of Veterans' Appeals (also known as 'BVA' or 'the Board') is a part of the VA, located in Washington, D.C. Members of the Board review benefit claims determinations made by local VA offices and issue decision on appeals.  These Law Judges, attorneys experienced in veterans law and in reviewing benefit claims, are the only ones who can issue Board decisions.  Staff attorneys, also trained in veterans law, review the facts of each appeal and assist the Board members.   {38 U.S.C. 7103, 7104}   BVA decisions are discoverabled via this search engine tool.</p>",
-            "title": "Board of Veterans' Appeals Decisions",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/sitemap_bva.xml",
             "describedByType": "text/xml",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>The Board of Veterans' Appeals (also known as 'BVA' or 'the Board') is a part of the VA, located in Washington, D.C. Members of the Board review benefit claims determinations made by local VA offices and issue decision on appeals.  These Law Judges, attorneys experienced in veterans law and in reviewing benefit claims, are the only ones who can issue Board decisions.  Staff attorneys, also trained in veterans law, review the facts of each appeal and assist the Board members.   {38 U.S.C. 7103, 7104}   BVA decisions are discoverabled via this search engine tool.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71371,48 +71349,52 @@
                     "title": "Board of Veterans' Appeals Decisions"
                 }
             ],
-            "describedBy": "https://www.va.gov/sitemap_bva.xml",
-            "dataQuality": true,
+            "identifier": "VA-BVA-BVA-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "appeal",
+                "appeals",
+                "appeals decisions",
+                "board of veterans appeals",
+                "bva",
+                "bva decisions"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rw54-s8nj",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2023-09-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://search.usa.gov/search/docs?affiliate=bvadecisions"
+            ],
+            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Section 5. Law Enforcement",
                 "Courts",
                 "and Prisons"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Board of Veterans' Appeals Decisions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rwgn-ekjg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-09-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-25",
-            "keyword": [
-                "veterans",
-                "vetpop",
-                "vetpop2023"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nation Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/rwgn-ekjg",
             "description": "Document describing the data sources and methodology used to produce the Veteran Population Projection Model 2023 (VetPop2023).",
-            "title": "VetPop2023 A Brief Description",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71420,36 +71402,37 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/rwgn-ekjg",
+            "issued": "2024-09-04",
+            "keyword": [
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rwgn-ekjg",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-10-25",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 A Brief Description"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/rwy2-29i8",
-            "bureauCode": [
-                "029:00"
-            ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "california",
-                "veterans"
+            "@type": "dcat:Dataset",
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
-            "identifier": "VA-OEI-OEI-090",
             "description": "<p>This is a summary of the services and programs VA provided in California in fiscal year 2014.</p>",
-            "title": "State Summary:  California",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71458,46 +71441,46 @@
                     "title": "State Summary:  California"
                 }
             ],
+            "identifier": "VA-OEI-OEI-090",
+            "issued": "2017-07-26",
+            "keyword": [
+                "california",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/rwy2-29i8",
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
+            "title": "State Summary:  California"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/FUND/FY_2013_Annual_Report.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
-                "franchise fund",
-                "fy 2013"
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
-            "identifier": "VA-OM-OM-032",
+            "dataQuality": true,
             "description": "<p>Franchise Fund FY 2013 Annual Report</p>",
-            "title": "Franchise Fund FY 2013 Annual Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71506,29 +71489,58 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-032",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund",
+                "fy 2013"
+            ],
+            "landingPage": "https://www.va.gov/FUND/FY_2013_Annual_Report.asp",
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
+            "title": "Franchise Fund FY 2013 Annual Report"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN2FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 2 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-076",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -71544,53 +71556,54 @@
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
-            "identifier": "VA-VHA-OIA-076",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 2",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN2FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 2 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 2"
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
+                    "downloadURL": "http://www.va.gov/vetdata/docs/GDX/GDX_FY08_V2.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-034",
             "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -71604,68 +71617,37 @@
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
-            "identifier": "VA-OEI-OEI-034",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2008",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.va.gov/vetdata/docs/GDX/GDX_FY08_V2.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s26u-kpe2",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-08-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
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
-            "identifier": "https://www.data.va.gov/api/views/s26u-kpe2",
             "description": "VetPop2023 top 10 states where Veterans will reside in fiscal year 2053",
-            "title": "VetPop2023 Top 10 States: FY 2053",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71673,57 +71655,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/s26u-kpe2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/s26u-kpe2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/s26u-kpe2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/s26u-kpe2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/s26u-kpe2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/s26u-kpe2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/s26u-kpe2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/s26u-kpe2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/s26u-kpe2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/s26u-kpe2",
+            "issued": "2024-08-20",
+            "keyword": [
+                "state",
+                "veterans",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s26u-kpe2",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-04",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 Top 10 States: FY 2053"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s27h-np3x",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
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
-            "identifier": "VA-OGC-046",
             "description": "<p>Litigation Files-VA</p>",
-            "title": "OGC Privacy Act System of Records Notice 16VA026",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71732,56 +71715,85 @@
                     "title": "OGC Privacy Act System of Records Notice 16VA026"
                 }
             ],
+            "identifier": "VA-OGC-046",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "system of records"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s27h-np3x",
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
+            "title": "OGC Privacy Act System of Records Notice 16VA026"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/s35n-2kvp",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "indiana",
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
-            "identifier": "https://www.data.va.gov/api/views/s35n-2kvp",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Indiana",
+            "identifier": "https://www.data.va.gov/api/views/s35n-2kvp",
+            "issued": "2021-08-26",
+            "keyword": [
+                "indiana",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s35n-2kvp",
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
+            "title": "State Summaries_Indiana"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN21FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 21 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-093",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -71797,70 +71809,42 @@
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
-            "identifier": "VA-VHA-OIA-093",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 21",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN21FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 21 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s4se-bfig",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "west virginia"
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
-            "identifier": "VA-OEI-OEI-220",
             "description": "<p>This summary describes the programs and services VA provided in West Virginia in fiscal year 2015.</p>",
-            "title": "State Summary: West Virginia FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71869,23 +71853,44 @@
                     "title": "West Virginia"
                 }
             ],
+            "identifier": "VA-OEI-OEI-220",
+            "issued": "2017-07-26",
+            "keyword": [
+                "west virginia"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s4se-bfig",
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
+            "title": "State Summary: West Virginia FY15"
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
+            "description": "<p>The Breast Care Registry is an Office of Women's Health sponsored intranet based registry providing data for the longitudinal tracking of breast care.</p>",
+            "identifier": "VA-VHA-BCR-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "breast cancer",
                 "breast care",
@@ -71902,59 +71907,38 @@
                 "veteran",
                 "womens health"
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
-            "identifier": "VA-VHA-BCR-001",
-            "description": "<p>The Breast Care Registry is an Office of Women's Health sponsored intranet based registry providing data for the longitudinal tracking of breast care.</p>",
-            "title": "Breast Care Registry (BCR)",
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
+            "title": "Breast Care Registry (BCR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s5yd-ysxg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "mississippi"
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
-            "identifier": "VA-OEI-OEI-194",
             "description": "<p>This summary describes the programs and services VA provided in Mississippi</p>",
-            "title": "State Summary: Mississippi",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71963,42 +71947,40 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-194",
+            "issued": "2017-07-26",
+            "keyword": [
+                "mississippi"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s5yd-ysxg",
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
+            "title": "State Summary: Mississippi"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s6st-yikd",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-04-01T04:00:00Z/2015-04-30T04:00:00Z",
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
-            "identifier": "VA-OM-OM-129",
             "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT APR 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72006,41 +71988,43 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-129",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cars",
+                "establishments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s6st-yikd",
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
+            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT APR 2015"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s6yd-tmr5",
-            "bureauCode": [
-                "029:00"
-            ],
-            "issued": "2017-11-13",
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
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "9631474e-e6a7-4d0c-b190-9a33c6fd0b5e",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary West Virginia FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72048,40 +72032,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "9631474e-e6a7-4d0c-b190-9a33c6fd0b5e",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s6yd-tmr5",
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
+            "title": "State Summary West Virginia FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s72r-ahnf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "facilities",
-                "utilization",
-                "veteran hires",
-                "veteran population"
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
-            "identifier": "VA-OEI-OEI-065",
             "description": "<p>Department of Veterans Affairs Statistics at a Glance including Veteran Population, Number of VA Facilities, VA Benefits and Healthcare Utilization, Period of Service, New Hires</p>",
-            "title": "Department of Veterans Affairs Quickfacts Statistics Slideshow",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72090,41 +72071,43 @@
                     "title": "Department of Veterans Affairs Quickfacts Statistics Slideshow"
                 }
             ],
+            "identifier": "VA-OEI-OEI-065",
+            "issued": "2017-07-26",
+            "keyword": [
+                "facilities",
+                "utilization",
+                "veteran hires",
+                "veteran population"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s72r-ahnf",
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
+            "title": "Department of Veterans Affairs Quickfacts Statistics Slideshow"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s7d7-edky",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "veterans",
-                "wyoming"
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
-            "identifier": "VA-OEI-OEI-137",
             "description": "<p>This is a summary of the programs and services provided by VA in Wyoming in fiscal year 2014.</p>",
-            "title": "State Summary:  Wyoming",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72133,46 +72116,44 @@
                     "title": "State Summary:  Wyoming"
                 }
             ],
+            "identifier": "VA-OEI-OEI-137",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans",
+                "wyoming"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s7d7-edky",
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
+            "title": "State Summary:  Wyoming"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s7u9-7cq9",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "korean conflict",
-                "korean war",
-                "veteran population",
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
-            "identifier": "https://www.data.va.gov/api/views/s7u9-7cq9",
             "description": "Korean War Veterans by State, FY 2020. Dataset created from an Esri shapefile. Source: VetPop 2018 Model (for the Korean War veteran counts), and an Esri feature class of state polygons. This data set supports the Korean War data story at: https://www.datahub.va.gov/stories/s/7wja-85c3",
-            "title": "Korean War Veterans by State, FY 2020 (VetPop Model 2018)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72180,61 +72161,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/s7u9-7cq9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/s7u9-7cq9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/s7u9-7cq9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/s7u9-7cq9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/s7u9-7cq9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/s7u9-7cq9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/s7u9-7cq9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/s7u9-7cq9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/s7u9-7cq9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/s7u9-7cq9",
+            "issued": "2020-12-15",
+            "keyword": [
+                "korean conflict",
+                "korean war",
+                "veteran population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s7u9-7cq9",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Korean War Veterans by State, FY 2020 (VetPop Model 2018)"
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
-                "healthcare",
-                "patients",
-                "priority group",
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
-            "identifier": "VA-OEI-OEI-045",
-            "description": "<p>This table shows the total number of patients in each of the Department of Veterans Affairs\u00ef\u00bf\u00bd healthcare enrollment priority group categories.</p>",
-            "title": "Number of Veteran Patients by Healthcare Priority Groups: FY00 to FY13",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/Utilization/PriorityGroup_FINAL3.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This table shows the total number of patients in each of the Department of Veterans Affairs\u00ef\u00bf\u00bd healthcare enrollment priority group categories.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72243,52 +72226,49 @@
                     "title": "xls"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/Utilization/PriorityGroup_FINAL3.xlsx",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-045",
+            "issued": "2017-07-26",
+            "keyword": [
+                "healthcare",
+                "patients",
+                "priority group",
+                "veteran"
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
                 "Veteran Patients Healthcare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Veteran Patients by Healthcare Priority Groups: FY00 to FY13"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s8nt-h89j",
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
-            "identifier": "VA-VHA-OIA-003",
-            "description": "<p>The 2008 Hospital Report Card was mandated by the FY08 Appropriations Act, and focused on Congressionally-mandated metrics applicable to general patient populations. The 2009 VHA Facility Quality and Safety Report report, not required by Congress, shifts to Veteran-centered metrics, and includes information related to infrastructure, care provided in outpatient and hospital settings, quality of care within given patient populations, accreditation status, patient satisfaction and patient outcomes for FY2008.  The data in this report have been compiled from multiple sources throughout VHA.  This dataset represents patient satisfaction based on survey data broken out by inpatient/outpatient and stratified ethnicity.</p>",
-            "title": "2009 VHA Facility Quality and Safety Report - Patient Satisfaction",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/VHA_2009_Facility_Quality_and_Safety_Report_Final.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>The 2008 Hospital Report Card was mandated by the FY08 Appropriations Act, and focused on Congressionally-mandated metrics applicable to general patient populations. The 2009 VHA Facility Quality and Safety Report report, not required by Congress, shifts to Veteran-centered metrics, and includes information related to infrastructure, care provided in outpatient and hospital settings, quality of care within given patient populations, accreditation status, patient satisfaction and patient outcomes for FY2008.  The data in this report have been compiled from multiple sources throughout VHA.  This dataset represents patient satisfaction based on survey data broken out by inpatient/outpatient and stratified ethnicity.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72296,68 +72276,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/s8nt-h89j/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/s8nt-h89j/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/s8nt-h89j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/s8nt-h89j/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/s8nt-h89j/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/s8nt-h89j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/s8nt-h89j/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/s8nt-h89j/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/s8nt-h89j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/VHA_2009_Facility_Quality_and_Safety_Report_Final.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-003",
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
+            "landingPage": "https://www.data.va.gov/d/s8nt-h89j",
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
+            "title": "2009 VHA Facility Quality and Safety Report - Patient Satisfaction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/s9dt-cvrg",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-22",
-            "keyword": [
-                "access",
-                "identity",
-                "security"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff Podolec",
                 "hasEmail": "mailto:jeff.podolec@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "da5853bf-3a88-4619-8b4a-402a9ff40359",
+            "dataQuality": true,
             "description": "<p>The Department of Veterans Affairs is providing a Veterans Health Identification Card (VHIC) for veterans to use at VA medical facilities. The VIC will be issued only to veterans who are eligible for VA medical benefits and only for the purpose of identification and check-in for VA medical appointments. The new card protects personal privacy by not showing Social Security Numbers or dates of birth on the front of the cards</p>",
-            "title": "Veterans Health Identification Card (VHIC)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72366,36 +72348,38 @@
                     "title": "Veterans Health Identification Card (VHIC)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "da5853bf-3a88-4619-8b4a-402a9ff40359",
+            "issued": "2018-02-23",
+            "keyword": [
+                "access",
+                "identity",
+                "security"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s9dt-cvrg",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Veterans Health Identification Card (VHIC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/s9ih-p8bz",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "colorado"
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
-            "identifier": "VA-OEI-OEI-175",
             "description": "<p>This summary describes the programs and services VA provided in Colorado in fiscal year 2015.</p>",
-            "title": "State Summary Colorado",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72404,24 +72388,44 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-175",
+            "issued": "2017-07-26",
+            "keyword": [
+                "colorado"
+            ],
+            "landingPage": "https://www.data.va.gov/d/s9ih-p8bz",
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
+            "title": "State Summary Colorado"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/saca-pui8",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "The dataset contains confidential inforamation related to compliance cases.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Office of Research Oversight case management database</p>",
+            "identifier": "VA-VHA-ORO-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-03-01T05:00:00Z/2014-10-20T04:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "adverse event",
                 "audits",
@@ -72436,61 +72440,41 @@
                 "research safety",
                 "technical assistance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/saca-pui8",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:080"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-ORO-001",
-            "description": "<p>Office of Research Oversight case management database</p>",
-            "title": "ORO Compliance Assessment Tracking System",
-            "programCode": [
-                "029:080"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "rights": "The dataset contains confidential inforamation related to compliance cases.",
+            "temporal": "2004-03-01T05:00:00Z/2014-10-20T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ORO Compliance Assessment Tracking System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/sb68-vz35",
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
-            "identifier": "bb53079b-6811-488c-ba00-6f08bc73dc1d",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Wisconsin FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72498,38 +72482,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "bb53079b-6811-488c-ba00-6f08bc73dc1d",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sb68-vz35",
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
+            "title": "State Summary Wisconsin FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/sbxw-spf9",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "healthcare",
-                "myhealthevet"
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
-            "identifier": "VA-VIA-5",
+            "dataQuality": true,
             "description": "<p>This service provides web services used to obtain MyHealtheVet related data. The service does not support multiple Vista sites data access. Users of this service are intended to be healthcare providers</p>",
-            "title": "MyHealtheVet Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72538,52 +72521,82 @@
                     "title": "MyHealtheVet Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VIA-5",
+            "issued": "2017-11-17",
+            "keyword": [
+                "healthcare",
+                "myhealthevet"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sbxw-spf9",
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
+            "title": "MyHealtheVet Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/scsv-3xi4",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "louisiana",
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
-            "identifier": "https://www.data.va.gov/api/views/scsv-3xi4",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Louisiana",
+            "identifier": "https://www.data.va.gov/api/views/scsv-3xi4",
+            "issued": "2021-08-26",
+            "keyword": [
+                "louisiana",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/scsv-3xi4",
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
+            "title": "State Summaries_Louisiana"
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
+                    "downloadURL": "https://www.data.va.gov/download/sdfi-mdkf/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "identifier": "VA-VBA-ABR2012-008",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
             "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
             "keyword": [
                 "abr",
                 "abr2012",
@@ -72591,67 +72604,38 @@
                 "dic benefits",
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
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-ABR2012-008",
-            "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Beneficiaries Who Began Receiving Comp and DIC Benefits During FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/sdfi-mdkf/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
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
+            "title": "Beneficiaries Who Began Receiving Comp and DIC Benefits During FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/se8p-ujfr",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "appeals"
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
-            "identifier": "VA-ORCH-11",
+            "dataQuality": true,
             "description": "<p>Queries the Veterans Appeals Control and Locator System (VACOLS) database and retrieves electronically attached copies of Board of Veterans' Appeals decisions, remands and development memoranda; personal information on appellants and contesting parties including names, addresses, identifying numbers, phone numbers, service dates, and issues on appeal; names, addresses, and phone numbers of representatives, powers of attorney, and attorney fee agreements; information on and dates of procedural steps taken in claims; records of and copies of correspondence concerning appeals, diary entries, notations of mail received, and information requests; verbatim recordings and transcripts of hearings; tracking information as to file location and custodian; and employee productivity information.</p>",
-            "title": "VIERS Appeals Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72660,25 +72644,53 @@
                     "title": "VIERS Appeals Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-11",
+            "issued": "2017-11-17",
+            "keyword": [
+                "appeals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/se8p-ujfr",
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
+            "title": "VIERS Appeals Service"
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
-            "temporal": "2015-08-01T04:00:00Z/2015-08-01T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/health/docs/PublicData_PendingAccess_20150801RptDate_Final.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 August 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-421",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -72692,70 +72704,42 @@
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
-            "identifier": "VA-VHA-OIA-421",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 August 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/PublicData_PendingAccess_20150801RptDate_Final.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 August 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-08-01T04:00:00Z/2015-08-01T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 August 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/sese-hsz4",
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
-            "identifier": "VA-OM-OM-158",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 145 September 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72763,63 +72747,63 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-158",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sese-hsz4",
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
+            "title": "COIN 145 September 2015"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/sf2a-mpj6",
-            "issued": "2023-07-20",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-17",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Oklahoma FY2021",
+            "identifier": "https://www.data.va.gov/api/views/sf2a-mpj6",
+            "issued": "2023-07-20",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "oklahoma"
             ],
-            "identifier": "https://www.data.va.gov/api/views/sf2a-mpj6",
+            "landingPage": "https://www.data.va.gov/d/sf2a-mpj6",
+            "modified": "2024-06-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Oklahoma FY2021",
             "title": "NCVAS State Summary Oklahoma FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/sf6z-dm4e",
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
-            "identifier": "https://www.data.va.gov/api/views/sf6z-dm4e",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM BENEFITS to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA\u2019s determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE FEB2019",
-            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72827,101 +72811,102 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/sf6z-dm4e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sf6z-dm4e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sf6z-dm4e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/sf6z-dm4e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sf6z-dm4e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sf6z-dm4e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/sf6z-dm4e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sf6z-dm4e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sf6z-dm4e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/sf6z-dm4e",
+            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 117"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sf6z-dm4e",
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
+            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/benefits/offices.asp",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "vba offices",
-                "vba regional offices"
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
-            "identifier": "VA-VBA-INFO-004",
+            "dataQuality": true,
             "description": "<p>List of VBA Regional Benefit Offices includes Central Area, Eastern Area, Southern Area and Western Area</p>",
-            "title": "VBA Regional benefit Office list",
+            "identifier": "VA-VBA-INFO-004",
             "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "vba offices",
+                "vba regional offices"
+            ],
+            "landingPage": "https://www.benefits.va.gov/benefits/offices.asp",
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
+            "title": "VBA Regional benefit Office list"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/sg3h-czz6",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-06-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
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
-            "identifier": "012bb5c0-fce3-4dec-9d06-eee27e639e60",
+            "dataQuality": true,
             "description": "<p>Disability Compensation and Patient Expenditures: FY2000 to FY2018</p>",
-            "title": "Disability Compensation and Patient Expenditures: FY2000 to FY2018",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72929,37 +72914,35 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "012bb5c0-fce3-4dec-9d06-eee27e639e60",
+            "issued": "2019-06-10",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sg3h-czz6",
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
+            "title": "Disability Compensation and Patient Expenditures: FY2000 to FY2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/shyq-u96s",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-10",
-            "keyword": [
-                "veteran population",
-                "veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/shyq-u96s",
             "description": "",
-            "title": "Era of Service Distribution: FY 2023 and FY 2050",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72967,39 +72950,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/shyq-u96s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/shyq-u96s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/shyq-u96s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/shyq-u96s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/shyq-u96s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/shyq-u96s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/shyq-u96s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/shyq-u96s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/shyq-u96s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/shyq-u96s",
+            "issued": "2024-08-08",
+            "keyword": [
+                "veteran population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/shyq-u96s",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-10",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Era of Service Distribution: FY 2023 and FY 2050"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2M",
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
+            "description": "<p>Wait Times Calculated Using Create Date for New Patients and Desired Date for Established Patients.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/Pending_Access_Data_using_CD_and_DD_11052014.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "November 5, 2014"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-066",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -73013,74 +73028,39 @@
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
-            "identifier": "VA-VHA-OIA-066",
-            "description": "<p>Wait Times Calculated Using Create Date for New Patients and Desired Date for Established Patients.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2014 November 5",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/Pending_Access_Data_using_CD_and_DD_11052014.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "November 5, 2014"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2014-10-01T04:00:00Z/2014-10-01T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2014 November 5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/si36-p5pd",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2021-01-27",
-            "temporal": "2013-10-01T04:00:00Z/2013-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-27",
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
-            "identifier": "https://www.data.va.gov/api/views/si36-p5pd",
+            "dataQuality": true,
             "description": "VBA- Insurance Lob- Policy Holders by program by State- October 2013.",
-            "title": "Policy Holders by Program by State- October 2013",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73088,61 +73068,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/si36-p5pd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/si36-p5pd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/si36-p5pd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/si36-p5pd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/si36-p5pd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/si36-p5pd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/si36-p5pd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/si36-p5pd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/si36-p5pd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "systemOfRecords": "VA-VBA-INS2014-002",
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/si36-p5pd",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2021-01-27",
+            "keyword": [
+                "2013",
+                "life insurance policies",
+                "policy holders",
+                "policy holders by state"
+            ],
+            "landingPage": "https://www.data.va.gov/d/si36-p5pd",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-01-27",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "systemOfRecords": "VA-VBA-INS2014-002",
+            "temporal": "2013-10-01T04:00:00Z/2013-10-31T04:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Policy Holders by Program by State- October 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/si6j-66f7",
-            "issued": "2023-02-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-21",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/si6j-66f7",
             "description": "VetPop2020 Branch of Service distribution in FY 2023 and 2050",
-            "title": "VetPop2020 Branch of Service FY23 & FY50",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73150,62 +73137,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/si6j-66f7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/si6j-66f7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/si6j-66f7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/si6j-66f7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/si6j-66f7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/si6j-66f7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/si6j-66f7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/si6j-66f7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/si6j-66f7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/si6j-66f7",
+            "issued": "2023-02-21",
+            "landingPage": "https://www.data.va.gov/d/si6j-66f7",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-02-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 Branch of Service FY23 & FY50"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/siag-m3kg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-03-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-12",
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
-            "identifier": "https://www.data.va.gov/api/views/siag-m3kg",
             "description": "Percentage Users of Either Health Care or Disability Compensation Compared to Other Programs. Data underlying the first figure of Part 3 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Trend in Percent of Health Care & Disability Compensation Users vs Other Users, FY2010-2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73213,99 +73191,105 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/siag-m3kg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/siag-m3kg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/siag-m3kg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/siag-m3kg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/siag-m3kg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/siag-m3kg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/siag-m3kg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/siag-m3kg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/siag-m3kg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/siag-m3kg",
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
+            "landingPage": "https://www.data.va.gov/d/siag-m3kg",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Trend in Percent of Health Care & Disability Compensation Users vs Other Users, FY2010-2021"
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
+                "hasEmail": "mailto:Monica.Reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- All-Volunteer Force Educational Assistance- Chapter 30- for March 2014</p>",
+            "identifier": "VA-VBA-USASPENDING032014-053",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 124",
                 "chapter 30",
                 "education",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:Monica.Reyes@va.gov"
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
-            "identifier": "VA-VBA-USASPENDING032014-053",
-            "description": "<p>USA Spending- All-Volunteer Force Educational Assistance- Chapter 30- for March 2014</p>",
-            "title": "USA Spending file-03/2014- Education- Chapter 30- CFDA 64.124",
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
+            "title": "USA Spending file-03/2014- Education- Chapter 30- CFDA 64.124"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/sj3u-c367",
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
-            "identifier": "7263f555-86cf-4f7b-a804-a3eddda7b3fd",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Iowa FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73313,38 +73297,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "7263f555-86cf-4f7b-a804-a3eddda7b3fd",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sj3u-c367",
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
+            "title": "State Summary Iowa FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/sj6n-r8t4",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "official opinion",
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
-            "identifier": "VA-OGC-048",
             "description": "<p>Surviving Spouse's Benefit for Month of Veteran's Death - 38 U.S.C. \u00a7 5310(b)</p>",
-            "title": "OGC Precedent Opinion 1-2009",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73353,42 +73335,43 @@
                     "title": "OGC Precedent Opinion 1-2009"
                 }
             ],
+            "identifier": "VA-OGC-048",
+            "issued": "2017-07-26",
+            "keyword": [
+                "official opinion",
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sj6n-r8t4",
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
+            "title": "OGC Precedent Opinion 1-2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/sji8-8jgm",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "beneficiary",
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
-            "identifier": "VA-ORCH-4",
+            "dataQuality": true,
             "description": "<p>Web service proxy/wrapper for CP&amp;E capabilities/data. This interface will retrieve a Bill of Collection record from CP&amp;E and enable a CRM user to view the Bill information. Back office CRM users (primarily DCU Unit) require the ability to review Bills to respond to customer inquiries about Bills and Offsets. The interface will be triggered when a user attempts to query for a Bill using the Bill # (K#).</p>",
-            "title": "CP&E Beneficiary Adapters Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73397,40 +73380,41 @@
                     "title": "CP&E Beneficiary Adapters Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-4",
+            "issued": "2017-11-17",
+            "keyword": [
+                "beneficiary",
+                "cpe"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sji8-8jgm",
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
+            "title": "CP&E Beneficiary Adapters Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/sjjm-jq7y",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "metrics"
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
-            "identifier": "4ec6c9fa-45e6-4d75-8f62-f6aa0785160e",
+            "dataQuality": true,
             "description": "<p>Reporting on storage, performance, traffic, security, and event activity.</p>",
-            "title": "Metrics",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73439,37 +73423,37 @@
                     "title": "Metrics"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "4ec6c9fa-45e6-4d75-8f62-f6aa0785160e",
+            "issued": "2018-02-23",
+            "keyword": [
+                "metrics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sjjm-jq7y",
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
+            "title": "Metrics"
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
-            "temporal": "2008-10-01T04:00:00Z/2013-10-01T04:00:00Z",
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
-            "identifier": "VA-OEI-OEI-076",
             "description": "<p>This chart summarizes Veteran employment in the federal government using data from the Office of Personnel Management's (OPM) report, Employment of Veterans in the Federal Executive Branch FY2013.</p>",
-            "title": "Employment of Veterans in the Federal Executive Branch: Fiscal Year (FY) 2008 to 2013",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73478,44 +73462,42 @@
                     "title": "http://www.va.gov/vetdata/docs/Quickfacts/Homepage_opm_vets_quickfacts.pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-076",
+            "issued": "2017-07-26",
+            "keyword": [
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
+            "temporal": "2008-10-01T04:00:00Z/2013-10-01T04:00:00Z",
             "theme": [
                 "Veteran Federal Employees"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Employment of Veterans in the Federal Executive Branch: Fiscal Year (FY) 2008 to 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/skh2-afg2",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "female veterans",
-                "median household income",
-                "mhi"
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
-            "identifier": "https://www.data.va.gov/api/views/skh2-afg2",
             "description": "Dataset representing household income for female veterans and female non-veterans, by age, for the year 2015",
-            "title": "2015 Median Household Income Female Vets and Non-Vets by Age",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73523,82 +73505,103 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/skh2-afg2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/skh2-afg2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/skh2-afg2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/skh2-afg2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/skh2-afg2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/skh2-afg2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/skh2-afg2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/skh2-afg2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/skh2-afg2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/skh2-afg2",
+            "issued": "2019-10-24",
+            "keyword": [
+                "female veterans",
+                "median household income",
+                "mhi"
+            ],
+            "landingPage": "https://www.data.va.gov/d/skh2-afg2",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
+            "title": "2015 Median Household Income Female Vets and Non-Vets by Age"
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
+            "description": "<p>USA Spending- Compensation and Pension- Burial Expenses Allowance for Vets for December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-005",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING122013-005",
-            "description": "<p>USA Spending- Compensation and Pension- Burial Expenses Allowance for Vets for December 2013.</p>",
-            "title": "USA Spending file- Compensation and Pension-  CFDA 64.101",
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
+            "title": "USA Spending file- Compensation and Pension-  CFDA 64.101"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/sm99-dpn9",
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
+            "description": "<p>The Spinal Cord Dysfunction (SCD) module supports the maintenance of local and national registries for the tracking of patients with spinal cord injury and disease from both traumatic and non-traumatic causes. SCD includes features for clinical, management, and research staff. Clinicians benefit from the ability to see profiles of SCD patients, ensure that regular annual exams are completed, and measure patient outcomes. Managers have a suite of reports that reflect the resources needed to care for SCD patients. Researchers have access to a national registry for all Veteran SCD patients and their associated health care events.</p>",
+            "identifier": "VA-VHA-PCS-012",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1995-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "cord",
                 "disease",
@@ -73611,60 +73614,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/sm99-dpn9",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:049"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PCS-012",
-            "description": "<p>The Spinal Cord Dysfunction (SCD) module supports the maintenance of local and national registries for the tracking of patients with spinal cord injury and disease from both traumatic and non-traumatic causes. SCD includes features for clinical, management, and research staff. Clinicians benefit from the ability to see profiles of SCD patients, ensure that regular annual exams are completed, and measure patient outcomes. Managers have a suite of reports that reflect the resources needed to care for SCD patients. Researchers have access to a national registry for all Veteran SCD patients and their associated health care events.</p>",
-            "title": "Spinal Cord Dysfunction (SCD)",
-            "programCode": [
-                "029:049"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1995-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Spinal Cord Dysfunction (SCD)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/smig-idw8",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "transformation"
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
-            "identifier": "eceed11a-3705-4eff-8802-889e4ec05d07",
+            "dataQuality": true,
             "description": "<p>DAS converts data from one format to another format based on customer requirements (ie. CCDA To FHIR.)</p>",
-            "title": "Transformation",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73673,36 +73657,36 @@
                     "title": "Transformation"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "eceed11a-3705-4eff-8802-889e4ec05d07",
+            "issued": "2018-02-23",
+            "keyword": [
+                "transformation"
+            ],
+            "landingPage": "https://www.data.va.gov/d/smig-idw8",
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
+            "title": "Transformation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/spcb-jsmv",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "georgia"
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
-            "identifier": "VA-OEI-OEI-179",
             "description": "<p>This summary describes the programs and services VA provided in Georgia in fiscal year 2015.</p>",
-            "title": "State Summary: Georgia",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73711,26 +73695,54 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-179",
+            "issued": "2017-07-26",
+            "keyword": [
+                "georgia"
+            ],
+            "landingPage": "https://www.data.va.gov/d/spcb-jsmv",
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
+            "title": "State Summary: Georgia"
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
-            "temporal": "2014-08-01T04:00:00Z/2014-08-01T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140814.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "August 14, 2014"
+                }
             ],
+            "identifier": "VA-VHA-OIA-061",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -73744,75 +73756,43 @@
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
-            "identifier": "VA-VHA-OIA-061",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative - Report 2014 August 14",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140814.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "August 14, 2014"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2014-08-01T04:00:00Z/2014-08-01T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative - Report 2014 August 14"
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
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
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
-            "identifier": "VA-VBA-ABR2012-090",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Idaho-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73820,110 +73800,115 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-090",
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
+            "title": "Idaho-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VSO/",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "directory",
-                "veterans service organizations",
-                "vso"
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
-            "identifier": "VA-VBA-INFO-003",
+            "dataQuality": true,
             "description": "<p>Online list of directory of Veterans Service Organizations for 2013-2014</p>",
-            "title": "Directory of Veteran Service Organizations",
+            "identifier": "VA-VBA-INFO-003",
             "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "directory",
+                "veterans service organizations",
+                "vso"
+            ],
+            "landingPage": "https://www.va.gov/VSO/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-04-18",
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
+            "title": "Directory of Veteran Service Organizations"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ssb5-qdfx",
-            "issued": "2023-07-19",
             "@type": "dcat:Dataset",
-            "modified": "2023-08-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Ohio FY2021",
+            "identifier": "https://www.data.va.gov/api/views/ssb5-qdfx",
+            "issued": "2023-07-19",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "ohio"
             ],
-            "identifier": "https://www.data.va.gov/api/views/ssb5-qdfx",
+            "landingPage": "https://www.data.va.gov/d/ssb5-qdfx",
+            "modified": "2023-08-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Ohio FY2021",
             "title": "NCVAS State Summary Ohio FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ssn7-z3k8",
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
-            "identifier": "https://www.data.va.gov/api/views/ssn7-z3k8",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) 2018 deidentified individual-level public release data file.",
-            "title": "AES 2018 PRDF",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73931,67 +73916,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ssn7-z3k8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ssn7-z3k8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ssn7-z3k8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ssn7-z3k8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ssn7-z3k8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ssn7-z3k8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ssn7-z3k8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ssn7-z3k8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ssn7-z3k8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/ssn7-z3k8",
+            "issued": "2023-03-16",
+            "keyword": [
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ssn7-z3k8",
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
+            "title": "AES 2018 PRDF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ssqr-ywc8",
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
-                "hospital",
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
-            "identifier": "VA-VHA-OIA-004",
-            "description": "<p>The 2008 Hospital Report Card was mandated by the FY08 Appropriations Act, and focused on Congressionally-mandated metrics applicable to general patient populations. The 2009 VHA Facility Quality and Safety Report report, not required by Congress, shifts to Veteran-centered metrics, and includes information related to infrastructure, care provided in outpatient and hospital settings, quality of care within given patient populations, accreditation status, patient satisfaction and patient outcomes for FY2008.  The data in this report have been compiled from multiple sources throughout VHA.  This dataset includes composite scores reflecting quality of care for outpatients (NEXUS) and inpatients (ORYX). Quality of outpatient care is further stratified by comparison of outpatient care by gender, age, and mental health diagnosis.</p>",
-            "title": "2009 VHA Facility Quality and Safety Report - Population Quality of Care",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/VHA_2009_Facility_Quality_and_Safety_Report_Final.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>The 2008 Hospital Report Card was mandated by the FY08 Appropriations Act, and focused on Congressionally-mandated metrics applicable to general patient populations. The 2009 VHA Facility Quality and Safety Report report, not required by Congress, shifts to Veteran-centered metrics, and includes information related to infrastructure, care provided in outpatient and hospital settings, quality of care within given patient populations, accreditation status, patient satisfaction and patient outcomes for FY2008.  The data in this report have been compiled from multiple sources throughout VHA.  This dataset includes composite scores reflecting quality of care for outpatients (NEXUS) and inpatients (ORYX). Quality of outpatient care is further stratified by comparison of outpatient care by gender, age, and mental health diagnosis.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73999,66 +73978,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ssqr-ywc8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ssqr-ywc8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ssqr-ywc8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ssqr-ywc8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ssqr-ywc8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ssqr-ywc8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ssqr-ywc8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ssqr-ywc8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ssqr-ywc8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/VHA_2009_Facility_Quality_and_Safety_Report_Final.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-004",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health",
+                "healthcare",
+                "hospital",
+                "hospital accreditation",
+                "patient safety",
+                "quality of care",
+                "satisfaction",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ssqr-ywc8",
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
+            "title": "2009 VHA Facility Quality and Safety Report - Population Quality of Care"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/sue5-ppyd",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
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
-            "identifier": "https://www.data.va.gov/api/views/sue5-ppyd",
+            "dataQuality": true,
             "description": "<p>VBA SPECIALLY ADAPTED HOUSING BENEFIT PROGRAMS. The Specially Adapted Housing (SAH) grant program helps Veterans with certain service-connected disabilities live independently in a barrier-free environment. SAH grants can be used in one of the following ways: (1) construct a suitable home on suitable land either already owned or to be acquired by the veteran, or (2) remodel an existing home if it can be suitably adapted, or (3) acquire a suitably adapted home or reduce the outstanding mortgage on a suitably adapted home already owned by the veteran. b. The Special Housing Adaptation (SHA) grant program helps veterans with certain service-connected disabilities adapt or purchase a home to accommodate the disability. SHA grants can be used in one of the following ways: (1) adapt an existing home the veteran or a family member already owns in which the veteran lives; (2) adapt a home the veteran or family member intends to purchase in which the veteran will live; (3) help a veteran purchase a home already adapted in which the veteran will live. c. . The Temporary Residence Adaptations (TRA) program provides adaptation assistance to veterans who are residing, but do not intend to permanently reside, in the a residence owned by a family member. If a veteran is otherwise eligible for SAH or SHA, the assistance is limited. d. SAH and SHA grants may be used up to three times, as long as the aggregate grant amount does not exceed the statutory dollar limitation. TRA grants may only be used once (and count as a grant usage for purposes of the limit of three), and the amount of assistance provided will be subtracted from the veteran's available statutory maximum.</p>",
-            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS MAR2019",
-            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74066,61 +74050,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/sue5-ppyd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sue5-ppyd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sue5-ppyd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/sue5-ppyd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sue5-ppyd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sue5-ppyd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/sue5-ppyd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sue5-ppyd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sue5-ppyd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/sue5-ppyd",
+            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 106"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sue5-ppyd",
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
+            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/suxu-5hjt",
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
-            "identifier": "9732a5e3-1715-470d-817d-e6b3083ce9a6",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary New York FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74128,45 +74112,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "9732a5e3-1715-470d-817d-e6b3083ce9a6",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/suxu-5hjt",
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
+            "title": "State Summary New York FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/sv43-6nsu",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-21",
-            "keyword": [
-                "access",
-                "identity",
-                "security"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff Podolec",
                 "hasEmail": "mailto:jeff.podolec@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "5f0d7eac-f3f4-48b9-b0bb-2b9586125355",
+            "dataQuality": true,
             "description": "<p>Provides the capability to monitor integrated applications and services to produce reports and generate alerts triggered by events or breach of predetermined event thresholds.</p>",
-            "title": "Compliance Audit and Reporting (CAR)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74175,44 +74157,39 @@
                     "title": "Compliance Audit and Reporting (CAR)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "5f0d7eac-f3f4-48b9-b0bb-2b9586125355",
+            "issued": "2018-02-23",
+            "keyword": [
+                "access",
+                "identity",
+                "security"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sv43-6nsu",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-21",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Compliance Audit and Reporting (CAR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Coverage_Amount_by_state_of_June_2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-06-01T04:00:00Z/2012-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_VGLI_Coverage_Amount_by_State.doc"
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
-            "identifier": "VA-VBA-INS2012-020",
+            "dataQuality": true,
             "description": "<p>Provides the amount of Veterans' Group Life Insurance (VGLI) coverage by state.  This report provides a snapshot of the amount of VGLI coverage as of June 30, 2012.  For members who reside outside the United States, coverage is not identified by individual country.  The total amount of coverage was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "VGLI Coverage Amount by State as of June 30, 2012",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74220,98 +74197,102 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/sv83-ab64/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sv83-ab64/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sv83-ab64/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/sv83-ab64/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sv83-ab64/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sv83-ab64/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/sv83-ab64/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sv83-ab64/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sv83-ab64/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-020",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Coverage_Amount_by_state_of_June_2012.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_VGLI_Coverage_Amount_by_State.doc"
+            ],
+            "temporal": "2012-06-01T04:00:00Z/2012-06-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VGLI Coverage Amount by State as of June 30, 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/svwp-s4cw",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-21",
-            "keyword": [
-                "new hampshire",
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
-            "identifier": "https://www.data.va.gov/api/views/svwp-s4cw",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_New Hampshire",
+            "identifier": "https://www.data.va.gov/api/views/svwp-s4cw",
+            "issued": "2021-08-26",
+            "keyword": [
+                "new hampshire",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/svwp-s4cw",
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
+            "title": "State Summaries_New Hampshire"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/swib-fgka",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "1867",
-                "annual report",
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
-            "identifier": "VA-OEI-OEI-141",
             "description": "<p>VA Historical Annual Reports detail services provided by the Department for each Fiscal Year, including Benefits, Healthcare, and Burial/Memorial services.  The Reports also describe the topics of administration and management within VA, ranging from data on personnel to information on construction projects.  Statistical tables for a variety of subjects are also included.</p>",
-            "title": "Annual Report:  1867",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74320,43 +74301,46 @@
                     "title": "Annual Report:  1867"
                 }
             ],
+            "identifier": "VA-OEI-OEI-141",
+            "issued": "2017-07-26",
+            "keyword": [
+                "1867",
+                "annual report",
+                "va",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/swib-fgka",
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
+            "title": "Annual Report:  1867"
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
-            "temporal": "2011-01-01T05:00:00Z/2011-03-31T04:00:00Z",
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
-            "identifier": "VA-OM-OM-090",
+            "dataQuality": true,
             "description": "<p>FY 2011 Second Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2011 Second Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74365,46 +74349,45 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-090",
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
+            "temporal": "2011-01-01T05:00:00Z/2011-03-31T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2011 Second Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
-                "029:25"
-            ],
-            "issued": "2017-07-26",
-            "temporal": "2015-06-01T04:00:00Z/2015-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "vba insurance",
-                "vgli"
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
-            "identifier": "VA-VBA-INS2015-001",
+            "dataQuality": true,
             "description": "<p>Provides the amount of Veterans' Group Life Insurance (VGLI) coverage by state. This report provides a snapshot of the amount of VGLI coverage as of June 30, 2015. For members who reside outside the United States, coverage is not identified by individual country. The total amount of coverage was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "VGLI Coverage Amount by State by 2015-06-30",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74412,26 +74395,57 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2015-001",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "vba insurance",
+                "vgli"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-06-01T04:00:00Z/2015-06-30T04:00:00Z",
             "theme": [
                 "Use of Benefits and Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VGLI Coverage Amount by State by 2015-06-30"
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
+            "description": "<p>VAMC-level statistics on the prevalence, mental health utilization, non-mental health utilization, mental health workload, and psychological testing of Veterans with a confirmed diagnosis of posttraumatic stress disorder (PTSD).  Information prepared by the VA Northeast Program Evaluation Center (NEPEC) for fiscal year 2015.  <b> This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/sxeh-t2ri/text/plain",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "VA-VHA-10N-011",
+            "isPartOf": "VA-VHA-10N-014",
             "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-29",
             "keyword": [
                 "2015",
                 "disorder",
@@ -74447,70 +74461,39 @@
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
-            "identifier": "VA-VHA-10N-011",
-            "description": "<p>VAMC-level statistics on the prevalence, mental health utilization, non-mental health utilization, mental health workload, and psychological testing of Veterans with a confirmed diagnosis of posttraumatic stress disorder (PTSD).  Information prepared by the VA Northeast Program Evaluation Center (NEPEC) for fiscal year 2015.  <b> This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>",
-            "title": "VA PTSD Medical Center Statistics - 2015",
-            "isPartOf": "VA-VHA-10N-014",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:042"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/sxeh-t2ri/text/plain",
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
+            "title": "VA PTSD Medical Center Statistics - 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/index.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "expenditure",
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
-            "identifier": "VA-OEI-OEI-167",
+            "dataQuality": true,
             "description": "<p>Geographic Distribution of VA Expenditures Report (GDX) located on the Expenditures page in the Expenditure Tables category. This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veterans population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures Report FY2015",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74519,45 +74502,46 @@
                     "title": "Geographic Distribution of VA Expenditures Report (GDX)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-167",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "va",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/index.asp",
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
+            "title": "Geographic Distribution of VA Expenditures Report FY2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/syst-9g2z",
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
-            "identifier": "cb50801e-8cd8-47af-ab6e-96ef13df44cb",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary North Carolina FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74565,43 +74549,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "cb50801e-8cd8-47af-ab6e-96ef13df44cb",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/syst-9g2z",
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
+            "title": "State Summary North Carolina FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/sywf-qkby",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-08-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-25",
-            "keyword": [
-                "veteran population",
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
-            "identifier": "https://www.data.va.gov/api/views/sywf-qkby",
             "description": "FY2023 Total Veterans Population by Gender",
-            "title": "VetPop Total Population by Gender",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74609,57 +74592,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/sywf-qkby/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sywf-qkby/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sywf-qkby/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/sywf-qkby/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sywf-qkby/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sywf-qkby/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/sywf-qkby/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/sywf-qkby/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/sywf-qkby/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/sywf-qkby",
+            "issued": "2024-08-15",
+            "keyword": [
+                "veteran population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/sywf-qkby",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-10-25",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop Total Population by Gender"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/szj6-akzt",
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
-            "identifier": "7e0630bd-8581-416f-be57-684616e305ef",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Indiana FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74667,76 +74651,77 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "7e0630bd-8581-416f-be57-684616e305ef",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/szj6-akzt",
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
+            "title": "State Summary Indiana FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/t237-i93a",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "279f1b11-a128-4135-825a-5530f04cb050",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist wartime veterans in need whose non-service- connected disabilities are permanent and total preventing them from following a substantially gainful occupation. A Veteran who meets the wartime service requirements is potential eligible if he/she is: \u2022 permanently and totally disabled for reasons not necessarily due to service, \u2022 age 65 or older, or \u2022 is presumed to be totally and permanently disabled for pension purposes because: o he/she is a patient in a nursing home for long-term care due to a disability, or o being disabled, as determined by the Commissioner of Social Security (SS) for purposes of any benefits administered by the Commissioner, such as SS disability benefits or Supplemental Security Income. Income restrictions are prescribed in 38 U.S.C. 1521. Pension is not payable to those whose estates are so large that it is reasonable they use the estate for maintenance. A Veteran meets wartime service requirements if he/she served: \u2022 a total of 90 days or more during one or more periods of war; \u2022 90 or more consecutive days that began or ended during a period of war; or \u2022 for any length of time during a period of war if he/she was discharged or released for a service-connected disability. Veterans entering service after September 7, 1980, must also meet the minimum active duty requirement of 24 months of continuous service or the full period to which the Veteran was called to active duty. (38 U.S.C.5303(A)).</p>",
-            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS FY2019",
+            "identifier": "279f1b11-a128-4135-825a-5530f04cb050",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 104"
+            ],
+            "landingPage": "https://www.data.va.gov/d/t237-i93a",
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
+            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cfm.va.gov/cost/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-07-07T04:00:00Z/2014-10-20T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "cost estimates construction management"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Connor",
                 "hasEmail": "mailto:robert.connor@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-CFM-CE-0014",
+            "dataQuality": true,
             "description": "<p>This site provides guides and other resoruces to help sites archive the goal of managing and executing a construction project within the funding limit approved by Congress.  This site includes links to the Manual of Preparation for Cost Estimates and Related Documents for VA Facilities.</p>",
-            "title": "Cost Estimation CFM",
-            "programCode": [
-                "029:090"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74745,42 +74730,44 @@
                     "title": "html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-CFM-CE-0014",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cost estimates construction management"
+            ],
+            "landingPage": "https://www.cfm.va.gov/cost/",
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
+            "temporal": "2014-07-07T04:00:00Z/2014-10-20T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Cost Estimation CFM"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/t2vu-q3x4",
-            "issued": "2024-04-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-02",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/t2vu-q3x4",
             "description": "",
-            "title": "vetpop_gender",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74788,65 +74775,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/t2vu-q3x4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/t2vu-q3x4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/t2vu-q3x4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/t2vu-q3x4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/t2vu-q3x4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/t2vu-q3x4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/t2vu-q3x4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/t2vu-q3x4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/t2vu-q3x4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/t2vu-q3x4",
+            "issued": "2024-04-19",
+            "landingPage": "https://www.data.va.gov/d/t2vu-q3x4",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-05-02",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "vetpop_gender"
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
-                "beds",
-                "health",
-                "healthcare",
-                "operating beds",
-                "staffed bed",
-                "staffed beds",
-                "va",
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
-            "identifier": "VA-VHA-OIA-113",
-            "description": "<p>Beds by Administrative Parent site. Operating Beds are defined as beds open and accepting patients for care. Data is self reported by facility.</p>",
-            "title": "VA Operating Beds by Administrative Parent, FY2010-FY2014",
+            "dataQuality": true,
+            "describedBy": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/raw/master/VA_DataDefinitions_VisitsBedsCBOC_2015.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Beds by Administrative Parent site. Operating Beds are defined as beds open and accepting patients for care. Data is self reported by facility.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74854,69 +74833,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/t2zd-sk7z/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/t2zd-sk7z/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/t2zd-sk7z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/t2zd-sk7z/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/t2zd-sk7z/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/t2zd-sk7z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/t2zd-sk7z/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/t2zd-sk7z/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/t2zd-sk7z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/raw/master/VA_DataDefinitions_VisitsBedsCBOC_2015.pdf",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-113",
+            "issued": "2017-07-26",
+            "keyword": [
+                "beds",
+                "health",
+                "healthcare",
+                "operating beds",
+                "staffed bed",
+                "staffed beds",
+                "va",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/health/",
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
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
+            "temporal": "2009-10-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "VA Healthcare Utilization"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Operating Beds by Administrative Parent, FY2010-FY2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/t3gj-uw4s",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-11-18",
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
-            "identifier": "https://www.data.va.gov/api/views/t3gj-uw4s",
             "description": "Percent Users vs Non-Users Distribution by Age Group - Females. Data underlying the third figure of Part 2 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 11, Percent Users vs Non-Users Distribution by Age Group - Females",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74924,56 +74905,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/t3gj-uw4s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/t3gj-uw4s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/t3gj-uw4s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/t3gj-uw4s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/t3gj-uw4s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/t3gj-uw4s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/t3gj-uw4s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/t3gj-uw4s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/t3gj-uw4s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/t3gj-uw4s",
+            "issued": "2020-11-18",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/t3gj-uw4s",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-12-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 11, Percent Users vs Non-Users Distribution by Age Group - Females"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/t3gj-z7ig",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "rhode island"
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
-            "identifier": "VA-OEI-OEI-211",
             "description": "<p>This summary describes the programs and services VA provided in Rhode Island in fiscal year 2015.</p>",
-            "title": "State Summary: Rhode Island FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74982,41 +74966,41 @@
                     "title": "Rhode Island"
                 }
             ],
+            "identifier": "VA-OEI-OEI-211",
+            "issued": "2017-07-26",
+            "keyword": [
+                "rhode island"
+            ],
+            "landingPage": "https://www.data.va.gov/d/t3gj-z7ig",
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
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/t4an-icyt",
-            "bureauCode": [
-                "029:00"
             ],
-            "issued": "2018-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "demographics",
-                "veterans"
+            "title": "State Summary: Rhode Island FY15"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "5d54bab2-8e7d-44d5-9fe1-8b31ae9df11b",
+            "dataQuality": true,
             "description": "<p>The speadsheets shows the total Veteran and Non-Veteran interments at National Cemeteries. It breaks out interment type as casket and cremain.</p>",
-            "title": "Summary of Veterans and Non-Veteran Interments at National Cemeteries",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75024,22 +75008,44 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "5d54bab2-8e7d-44d5-9fe1-8b31ae9df11b",
+            "issued": "2018-09-11",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/t4an-icyt",
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
+            "title": "Summary of Veterans and Non-Veteran Interments at National Cemeteries"
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
+            "description": "<p>USA Spending- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects- January 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-025",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "birth defects",
                 "cfda 64 128",
@@ -75049,80 +75055,56 @@
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
-            "identifier": "VA-VBA-USASPENDING012014-025",
-            "description": "<p>USA Spending- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects- January 2014</p>",
-            "title": "USA Spending file- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects- 01/2014  CFDA 64.128",
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
+            "title": "USA Spending file- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects- 01/2014  CFDA 64.128"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/t65f-tiwq",
-            "issued": "2023-12-13",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-05",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "The PTSD Repository is a useful tool for staying up-to-date with PTSD clinical trials research, to inform your work and to support patient education.",
             "identifier": "https://www.data.va.gov/api/views/t65f-tiwq",
+            "issued": "2023-12-13",
+            "landingPage": "https://www.data.va.gov/d/t65f-tiwq",
+            "modified": "2024-09-05",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "The PTSD Repository is a useful tool for staying up-to-date with PTSD clinical trials research, to inform your work and to support patient education.",
             "title": "For Providers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/t6eb-4dv7",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-01-03T05:00:00Z/2015-07-28T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "cemeteries",
-                "memorials"
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
-            "identifier": "VA-NCA-MPS-010",
             "description": "<p>This documents provides guidance on the appropriate design, size, and procedures for the acceptance of donations of memorials to the National Cemetery Administration</p>",
-            "title": "Guidelines and Requirements for Review and Acceptance of Memorials at National Cemeteries",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75130,75 +75112,105 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "VA-NCA-MPS-010",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cemeteries",
+                "memorials"
+            ],
+            "landingPage": "https://www.data.va.gov/d/t6eb-4dv7",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2008-01-03T05:00:00Z/2015-07-28T04:00:00Z",
             "theme": [
                 "Memorials"
-            ]
+            ],
+            "title": "Guidelines and Requirements for Review and Acceptance of Memorials at National Cemeteries"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/t6pr-iduk",
-            "issued": "2024-04-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "FY2023 State Summary Kentucky",
+            "identifier": "https://www.data.va.gov/api/views/t6pr-iduk",
+            "issued": "2024-04-23",
             "keyword": [
                 "fy2024",
                 "kentucky",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/t6pr-iduk",
+            "landingPage": "https://www.data.va.gov/d/t6pr-iduk",
+            "modified": "2024-07-11",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "FY2023 State Summary Kentucky",
             "title": "NCVAS State Summary Kentucky FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/t7tf-fdw7",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Wyoming FY2023",
+            "identifier": "https://www.data.va.gov/api/views/t7tf-fdw7",
             "issued": "2024-06-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "wyoming"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/t7tf-fdw7",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/t7tf-fdw7",
-            "description": "NCVAS State Summary Wyoming FY2023",
-            "title": "NCVAS State Summary Wyoming FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Wyoming FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oit.va.gov/dashboard.asp",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Carol Macha",
+                "hasEmail": "mailto:Carol.Macha@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This reports shows visibility into the status of projects that comprise VA\u00ef\u00bf\u00bds IT development activities.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oit.va.gov/docs/dashboard/201301_OIT_PMAS_Dashboard_Active_Jan_2013.pdf",
+                    "mediaType": "text/html",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-PD-02",
             "issued": "2017-07-26",
-            "temporal": "2012-09-30T04:00:00Z/2013-04-02T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "active",
                 "cost",
@@ -75211,69 +75223,41 @@
                 "schedule",
                 "va"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Carol Macha",
-                "hasEmail": "mailto:Carol.Macha@va.gov"
-            },
+            "landingPage": "https://www.oit.va.gov/dashboard.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:079"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OIT-PD-02",
-            "description": "<p>This reports shows visibility into the status of projects that comprise VA\u00ef\u00bf\u00bds IT development activities.</p>",
-            "title": "Department of Veterans Affairs - Office of Information Technology Program Management Accountability Dashboard  Active Project Reports",
-            "programCode": [
-                "029:079"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oit.va.gov/docs/dashboard/201301_OIT_PMAS_Dashboard_Active_Jan_2013.pdf",
-                    "mediaType": "text/html",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2012-09-30T04:00:00Z/2013-04-02T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs - Office of Information Technology Program Management Accountability Dashboard  Active Project Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/taib-w5nd",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2000-01-01T05:00:00Z/2013-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "compensation",
-                "disability"
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
-            "identifier": "VA-OEI-OEI-058",
+            "dataQuality": true,
             "description": "<p>This report contains FY2000 through FY2013 data on disability compensation expenditures and recipients and on VA healthcare system patients and patient expenditures.</p>",
-            "title": "Disability Compensation and Patient Expenditures: FY2000 to FY2013",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75282,26 +75266,57 @@
                     "title": "xls"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-058",
+            "issued": "2017-07-26",
+            "keyword": [
+                "compensation",
+                "disability"
+            ],
+            "landingPage": "https://www.data.va.gov/d/taib-w5nd",
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
+            "temporal": "2000-01-01T05:00:00Z/2013-12-31T05:00:00Z",
             "theme": [
                 "disability comp"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Disability Compensation and Patient Expenditures: FY2000 to FY2013"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/Dec_15_Pending_Access_Data_using_Preferred_Date_Released_01082015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Preferred Date 2015-01-08"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-068",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2014-12-15T05:00:00Z/2014-12-15T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -75315,71 +75330,38 @@
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
-            "identifier": "VA-VHA-OIA-068",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Jan 8",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/Dec_15_Pending_Access_Data_using_Preferred_Date_Released_01082015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Preferred Date 2015-01-08"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2014-12-15T05:00:00Z/2014-12-15T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Jan 8"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tcj6-esgn",
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
-            "identifier": "VA-OM-OM-116",
             "description": "<p>FY 2003 Franchise Fund Annual Report Points of Contact</p>",
-            "title": "FY 2003 Franchise Fund Annual Report Points of Contact",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75388,39 +75370,41 @@
                     "title": "FY 2003 Franchise Fund Annual Report Points of Contact"
                 }
             ],
+            "identifier": "VA-OM-OM-116",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tcj6-esgn",
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
+            "title": "FY 2003 Franchise Fund Annual Report Points of Contact"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tcyz-v7jh",
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
-            "identifier": "https://www.data.va.gov/api/views/tcyz-v7jh",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located.</p>",
-            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS MAR2019",
-            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75428,43 +75412,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tcyz-v7jh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tcyz-v7jh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tcyz-v7jh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/tcyz-v7jh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tcyz-v7jh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tcyz-v7jh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tcyz-v7jh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tcyz-v7jh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tcyz-v7jh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/tcyz-v7jh",
+            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 114"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tcyz-v7jh",
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
+            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nvsbe.com/official-headquarter-hotels/atlanta-ga/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Armando Herrera",
+                "hasEmail": "mailto:Armando.Herrera@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>National Veterans Small Business Engagement website - Atlanta webpage</p>",
+            "identifier": "VA-00SB-NVSBE0004",
             "issued": "2017-07-26",
-            "temporal": "2014-06-11T04:00:00Z/2015-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "atlanta",
                 "conference",
@@ -75476,60 +75481,39 @@
                 "veterans affairs",
                 "vets"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Armando Herrera",
-                "hasEmail": "mailto:Armando.Herrera@va.gov"
-            },
+            "landingPage": "http://www.nvsbe.com/official-headquarter-hotels/atlanta-ga/",
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
-            "identifier": "VA-00SB-NVSBE0004",
-            "description": "<p>National Veterans Small Business Engagement website - Atlanta webpage</p>",
-            "title": "NVSBE Website - Atlanta",
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
+            "title": "NVSBE Website - Atlanta"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/te4z-niyg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "idaho"
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
-            "identifier": "VA-OEI-OEI-182",
             "description": "<p>This summary describes the programs and services VA provided in Idaho in fiscal year 2015.</p>",
-            "title": "State Summary: Idaho",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75538,46 +75522,42 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-182",
+            "issued": "2017-07-26",
+            "keyword": [
+                "idaho"
+            ],
+            "landingPage": "https://www.data.va.gov/d/te4z-niyg",
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
+            "title": "State Summary: Idaho"
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
-            "identifier": "VA-VBA-ABR2012-110",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "New York-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75586,26 +75566,50 @@
                     "title": "New York-FY12 Benefits Summary"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-110",
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
+            "title": "New York-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tena-2py9",
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
+            "description": "In acknowledgement of National PTSD Awareness Day, the National Center for PTSD has launched its PTSD-Repository.  The PTSD-Repository is a platform hosting data more than 300 RCTs of the treatment of PTSD in adults and resources created by NCPTSD to illustrate the data.",
+            "identifier": "https://www.data.va.gov/api/views/tena-2py9",
             "issued": "2020-06-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
             "keyword": [
                 "launch",
                 "ptsd awareness",
@@ -75613,53 +75617,33 @@
                 "ptsd treatment",
                 "rct"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for PTSD",
-                "hasEmail": "mailto:ncptsd@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/tena-2py9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-11",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for PTSD"
             },
-            "identifier": "https://www.data.va.gov/api/views/tena-2py9",
-            "description": "In acknowledgement of National PTSD Awareness Day, the National Center for PTSD has launched its PTSD-Repository.  The PTSD-Repository is a platform hosting data more than 300 RCTs of the treatment of PTSD in adults and resources created by NCPTSD to illustrate the data.",
-            "title": "Launch of the PTSD-Repository",
-            "programCode": [
-                "029:000"
-            ],
-            "accrualPeriodicity": "R/P1Y",
-            "language": [
-                "en-US"
-            ]
+            "rights": "All data is within the public domain and is currently available for download.",
+            "title": "Launch of the PTSD-Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tev9-tkuh",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "new hampshire"
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
-            "identifier": "VA-OEI-OEI-200",
             "description": "<p>This summary describes the programs and services VA provided in New Hampshire in fiscal year 2015.</p>",
-            "title": "State Summary: New Hampshire FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75668,47 +75652,42 @@
                     "title": "New Hampshire"
                 }
             ],
+            "identifier": "VA-OEI-OEI-200",
+            "issued": "2017-07-26",
+            "keyword": [
+                "new hampshire"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tev9-tkuh",
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
+            "title": "State Summary: New Hampshire FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_coverage_amount_by_state.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-09-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotesVGLI_Coverage_Amount_by_State.doc"
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
-            "identifier": "VA-VBA-INS2011-018",
+            "dataQuality": true,
             "description": "<p>Provides the amount of Veterans' Group Life Insurance (VGLI) coverage by state.  This report provides a snapshot of the amount of VGLI coverage as of September 30, 2011.  For members who reside outside the United States, coverage is not identified by individual country.  The total amount of coverage was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "FY11_EOM_Sep_VGLI Coverage Amount by State as of September 30, 2011",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75716,77 +75695,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tfdk-b69t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tfdk-b69t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tfdk-b69t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/tfdk-b69t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tfdk-b69t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tfdk-b69t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tfdk-b69t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tfdk-b69t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tfdk-b69t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-018",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_coverage_amount_by_state.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotesVGLI_Coverage_Amount_by_State.doc"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-09-01T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY11_EOM_Sep_VGLI Coverage Amount by State as of September 30, 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tgfn-8ipp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-05-04",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-04",
-            "keyword": [
-                "ethnicity",
-                "fy20",
-                "fy2020",
-                "fy 2020",
-                "fy 20 va user",
-                "healthcare",
-                "health care",
-                "race",
-                "va healthcare",
-                "va health care",
-                "va user",
-                "veteran"
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
-            "identifier": "https://www.data.va.gov/api/views/tgfn-8ipp",
+            "dataQuality": true,
             "description": "Note: \"Total Number of Veterans\" represents FY 2020 projected Veteran counts from VA's Veteran Population Projection Model 2018 (VetPop18). These projections are made with the assumption that Veterans are not missing information (e.g. race, etc.).\nNote: \"Veteran VA Users\" and \"Veteran VA Healthcare Users\" represent historical Veteran counts from VA's United States Veterans Eligibility Trends and Statistics 2020 (USVETS 2020).\nNote: \"Veteran VA Users\" includes Veteran users of VA healthcare or any other VA benefit or service.\n\nSources: USVETS 2020 and VetPop18",
-            "title": "FY 2020 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Race",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75794,60 +75769,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tgfn-8ipp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tgfn-8ipp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tgfn-8ipp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/tgfn-8ipp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tgfn-8ipp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tgfn-8ipp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tgfn-8ipp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tgfn-8ipp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tgfn-8ipp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/tgfn-8ipp",
+            "issued": "2022-05-04",
+            "keyword": [
+                "ethnicity",
+                "fy20",
+                "fy2020",
+                "fy 2020",
+                "fy 20 va user",
+                "healthcare",
+                "health care",
+                "race",
+                "va healthcare",
+                "va health care",
+                "va user",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tgfn-8ipp",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2022-05-04",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2020 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Race"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tk8e-6ktt",
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
-            "identifier": "https://www.data.va.gov/api/views/tk8e-6ktt",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE  NOV2018",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75855,66 +75838,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tk8e-6ktt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tk8e-6ktt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tk8e-6ktt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/tk8e-6ktt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tk8e-6ktt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tk8e-6ktt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tk8e-6ktt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tk8e-6ktt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tk8e-6ktt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/tk8e-6ktt",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tk8e-6ktt",
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
+            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE  NOV2018"
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
-            "identifier": "VA-VBA-ABR2012-091",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Illinois-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75922,48 +75902,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-091",
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
+            "title": "Illinois-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tkbc-8bzd",
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
-            "identifier": "https://www.data.va.gov/api/views/tkbc-8bzd",
             "description": "The Department of Veterans Affairs provides official estimates and projections of the Veteran population using the Veteran Population Projection Model (VetPop). Based on the latest model VetPop2020 and the most recent national survey estimates from the 2021 American Community Survey 5-Year (ACS) data, the projected number of Veterans living in 50 states, DC and Puerto Rico for the fiscal years, 2021 to 2023, are allocated to Urban and Rural areas. As defined by the Census Bureau, those not residing in Urban areas are assumed to be in Rural areas (https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural/2010-urban-rural.html).\n\nThis table contains the Veteran estimates by urban/rural, gender, age group, and race.\n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2020 Urban/Rural by Race FY2021-2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75971,58 +75950,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tkbc-8bzd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tkbc-8bzd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tkbc-8bzd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/tkbc-8bzd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tkbc-8bzd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tkbc-8bzd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tkbc-8bzd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tkbc-8bzd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tkbc-8bzd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/tkbc-8bzd",
+            "issued": "2023-02-21",
+            "keyword": [
+                "rural",
+                "rural veterans",
+                "urban",
+                "veteran",
+                "veteran population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tkbc-8bzd",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-06",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 Urban/Rural by Race FY2021-2023"
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
-            "temporal": "2012-10-01T04:00:00Z/2012-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-081",
+            "dataQuality": true,
             "description": "<p>FY 2013 First Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2013 First Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76031,70 +76015,68 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-081",
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
+            "temporal": "2012-10-01T04:00:00Z/2012-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2013 First Quarter High-Dollar Overpayments Report"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tkvp-e9rs",
-            "issued": "2023-04-18",
             "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHARLES.LIN2@VA.GOV",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "The United States Veterans Life Tables are computed for the years of 1980-1989, 1990-1999, 2000-2009, and 2010-2019, and for males and females.",
+            "identifier": "https://www.data.va.gov/api/views/tkvp-e9rs",
+            "issued": "2023-04-18",
             "keyword": [
                 "life expectancy",
                 "life table"
             ],
-            "identifier": "https://www.data.va.gov/api/views/tkvp-e9rs",
+            "landingPage": "https://www.data.va.gov/d/tkvp-e9rs",
+            "modified": "2023-06-08",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "The United States Veterans Life Tables are computed for the years of 1980-1989, 1990-1999, 2000-2009, and 2010-2019, and for males and females.",
             "title": "United States Veterans Life Tables, 1980-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tm9a-bubg",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion",
-                "public law 110-181"
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
-            "identifier": "VA-OGC-053",
             "description": "<p>Servicemembers' Entitlement to Rehabilitation and Vocational Benefits under Public Law 110-181</p>",
-            "title": "OGC Precedent Opinion 3-2008",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76103,46 +76085,44 @@
                     "title": "OGC Precedent Opinion 3-2008"
                 }
             ],
+            "identifier": "VA-OGC-053",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion",
+                "public law 110-181"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tm9a-bubg",
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
+            "title": "OGC Precedent Opinion 3-2008"
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
-            "identifier": "VA-VBA-ABR2012-023",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Number of Veterans with Service Connected Disabilities Receiving Compensation by Combined Percent by FY",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76150,45 +76130,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-023",
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
+            "title": "Number of Veterans with Service Connected Disabilities Receiving Compensation by Combined Percent by FY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tmnn-2iqd",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-07-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-02",
-            "keyword": [
-                "pension",
-                "period of service",
-                "women veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VACONCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/tmnn-2iqd",
             "description": "Male and Female Pensioner by Period of Service FY2023",
-            "title": "FY2023 Period of Service - Pension",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76196,40 +76178,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tmnn-2iqd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tmnn-2iqd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tmnn-2iqd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/tmnn-2iqd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tmnn-2iqd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tmnn-2iqd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tmnn-2iqd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tmnn-2iqd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tmnn-2iqd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/tmnn-2iqd",
+            "issued": "2024-07-25",
+            "keyword": [
+                "pension",
+                "period of service",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tmnn-2iqd",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-02",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY2023 Period of Service - Pension"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/tn38-y365",
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
+            "description": "<p>As of June 28, 2010, the Master Veteran Index (MVI) database based on the enhanced Master Patient Index (MPI) is the authoritative identity service within the VA, establishing, maintaining and synchronizing identities for VA clients, Veterans and beneficiaries.  The MVI includes authoritative sources for health identity data and contains over 17 million patient entries populated from all VHA facilities nationwide.  The MVI provides the access point mechanism for linking patient's information to enable an enterprise-wide view of patient information, uniquely identifies all active patients who have been admitted, treated, or registered in any VHA facility, and assigns a unique identifier to the patient.  The MVI correlates a patient's identity across the enterprise, including all VistA systems and external systems, such as Department of Defense (DoD) and the Nationwide Health Information Network (NwHIN).  The MVI facilitates the sharing of health information, resulting in coordinated and integrated health care for Veterans.  New Information Technology systems must be interoperable with the MVI and legacy systems will establish integration by October 1, 2012.  The Healthcare Identity Management (HC IdM) Team within VHA's Data Quality Program is the steward of patient identity data, performing maintenance and support activities.</p>",
+            "identifier": "VA-VHA-OIA-010",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1999-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "identifier",
                 "identity",
@@ -76238,74 +76241,74 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/tn38-y365",
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
-            "identifier": "VA-VHA-OIA-010",
-            "description": "<p>As of June 28, 2010, the Master Veteran Index (MVI) database based on the enhanced Master Patient Index (MPI) is the authoritative identity service within the VA, establishing, maintaining and synchronizing identities for VA clients, Veterans and beneficiaries.  The MVI includes authoritative sources for health identity data and contains over 17 million patient entries populated from all VHA facilities nationwide.  The MVI provides the access point mechanism for linking patient's information to enable an enterprise-wide view of patient information, uniquely identifies all active patients who have been admitted, treated, or registered in any VHA facility, and assigns a unique identifier to the patient.  The MVI correlates a patient's identity across the enterprise, including all VistA systems and external systems, such as Department of Defense (DoD) and the Nationwide Health Information Network (NwHIN).  The MVI facilitates the sharing of health information, resulting in coordinated and integrated health care for Veterans.  New Information Technology systems must be interoperable with the MVI and legacy systems will establish integration by October 1, 2012.  The Healthcare Identity Management (HC IdM) Team within VHA's Data Quality Program is the steward of patient identity data, performing maintenance and support activities.</p>",
-            "title": "Master Veteran Index (MVI)",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1999-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Master Veteran Index (MVI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/tp2c-aerz",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "michigan",
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
-            "identifier": "https://www.data.va.gov/api/views/tp2c-aerz",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Michigan",
+            "identifier": "https://www.data.va.gov/api/views/tp2c-aerz",
+            "issued": "2021-08-26",
+            "keyword": [
+                "michigan",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tp2c-aerz",
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
+            "title": "State Summaries_Michigan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/tq29-drkf",
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
+            "description": "<p>The Veterans Equitable Resource Allocation (VERA) database, is operated by the Allocation Resource Center (ARC) in Braintree, MA. The ARC is part of the Resource Allocation &amp; Execution Office of the Office of Finance. The database is developed from the Patient Treatment File, National Patient Care Database, Fee Basis Medical and Pharmacy System, Decision Support System (DSS) National extracts, DSS Derived Monthly Program Cost Report (MPCR), Resident Assessment Instrument (RAI) Minimum Data Set (MDS), Clinical Case Registry (CCR), and Home Dialysis Data Collection System, the Pharmacy Benefits Management database and the Consolidated Enrollment File. Most of the clinical data is Veterans Health Information Systems and Technology Architecture data which is transmitted to the Austin Information Technology Center (AITC) where it is retrieved by the ARC each month. The ARC also retrieves DSS cost data from the AITC as well. Some additional information is received from the Hines Pharmacy Benefits Management and the CCR databases. The data from these sources is combined to develop patient-specific care and cost data for each hospitalization or visit at the location or treatment level. Aggregate tables summarize this data for reporting and analysis purposes. The VERA databases are the basis for resource allocation in the Veterans Health Administration.</p>",
+            "identifier": "VA-VHA-OF-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1989-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "allocation",
                 "budget",
@@ -76318,65 +76321,42 @@
                 "veteran",
                 "visn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/tq29-drkf",
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
-            "identifier": "VA-VHA-OF-001",
-            "description": "<p>The Veterans Equitable Resource Allocation (VERA) database, is operated by the Allocation Resource Center (ARC) in Braintree, MA. The ARC is part of the Resource Allocation &amp; Execution Office of the Office of Finance. The database is developed from the Patient Treatment File, National Patient Care Database, Fee Basis Medical and Pharmacy System, Decision Support System (DSS) National extracts, DSS Derived Monthly Program Cost Report (MPCR), Resident Assessment Instrument (RAI) Minimum Data Set (MDS), Clinical Case Registry (CCR), and Home Dialysis Data Collection System, the Pharmacy Benefits Management database and the Consolidated Enrollment File. Most of the clinical data is Veterans Health Information Systems and Technology Architecture data which is transmitted to the Austin Information Technology Center (AITC) where it is retrieved by the ARC each month. The ARC also retrieves DSS cost data from the AITC as well. Some additional information is received from the Hines Pharmacy Benefits Management and the CCR databases. The data from these sources is combined to develop patient-specific care and cost data for each hospitalization or visit at the location or treatment level. Aggregate tables summarize this data for reporting and analysis purposes. The VERA databases are the basis for resource allocation in the Veterans Health Administration.</p>",
-            "title": "Veterans Equitable Resource Allocation (VERA)",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1989-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Equitable Resource Allocation (VERA)"
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
-            "identifier": "VA-VBA-ABR2012-069",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Insurance Death Awards (Number) by Fiscal Year",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76385,49 +76365,49 @@
                     "title": "Insurance Death Awards (Number) by Fiscal Year"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-069",
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
+            "title": "Insurance Death Awards (Number) by Fiscal Year"
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
-            "identifier": "VA-VBA-ABR2012-043",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Home Loans Guaranteed Based on Gender and Age During Fiscal Year 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76435,147 +76415,151 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-043",
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
+            "title": "Home Loans Guaranteed Based on Gender and Age During Fiscal Year 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ts5k-et8w",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "veterans",
-                "wisconsin"
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
-            "identifier": "https://www.data.va.gov/api/views/ts5k-et8w",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Wisconsin",
+            "identifier": "https://www.data.va.gov/api/views/ts5k-et8w",
+            "issued": "2021-08-26",
+            "keyword": [
+                "veterans",
+                "wisconsin"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ts5k-et8w",
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
+            "title": "State Summaries_Wisconsin"
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
+            "description": "<p>USA Spending- All-Volunteer Force Educational Assistance- Chapter 30- for December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-004",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 124",
                 "chapter 30",
                 "education",
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
-            "identifier": "VA-VBA-USASPENDING122013-004",
-            "description": "<p>USA Spending- All-Volunteer Force Educational Assistance- Chapter 30- for December 2013.</p>",
-            "title": "USA Spending file- Education- Chapter 30- CFDA 64.124",
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
+            "title": "USA Spending file- Education- Chapter 30- CFDA 64.124"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tt55-ceha",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "694144cc-d720-4122-a5da-0edc2ade15e7",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary South Carolina FY2016",
+            "identifier": "694144cc-d720-4122-a5da-0edc2ade15e7",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tt55-ceha",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary South Carolina FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tt9r-btrg",
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
-            "identifier": "59f7d5df-afe1-4a6d-9649-07cb863fcd6b",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary California FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76583,28 +76567,56 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "59f7d5df-afe1-4a6d-9649-07cb863fcd6b",
+            "issued": "2018-10-29",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tt9r-btrg",
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
+            "title": "State Summary California FY2017"
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
-            "temporal": "2015-11-15T05:00:00Z/2015-11-15T05:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR34_112015_Pending_and_EWL_Biweekly_Desired_Date_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 November 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-429",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -76618,73 +76630,43 @@
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
-            "identifier": "VA-VHA-OIA-429",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 November 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR34_112015_Pending_and_EWL_Biweekly_Desired_Date_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 November 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-11-15T05:00:00Z/2015-11-15T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 November 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Surveys.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-07-03T04:00:00Z/2007-11-06T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "employment",
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
-            "identifier": "VA-OEI-OEI-50",
+            "dataQuality": true,
             "description": "<p>The goal of the Department of Veterans Affairs\u00ef\u00bf\u00bd Vocational Rehabilitation and Employment (VR&amp;E) Program is to enable veterans to live independently, achieve the highest quality of life possible and, given advances in medical science and technology, to secure gainful employment. In 2004, an independent task force assessed the VR&amp;E program and concluded that approximately one-third of veterans enrolled in the program did not persist and complete the program.</p>",
-            "title": "2007 Veterans Employability Research Survey",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76693,45 +76675,46 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-50",
+            "issued": "2017-07-26",
+            "keyword": [
+                "employment",
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
+            "temporal": "2007-07-03T04:00:00Z/2007-11-06T05:00:00Z",
             "theme": [
                 "Socioeconomics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2007 Veterans Employability Research Survey"
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
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
-                "franchise fund",
-                "fy 2010"
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
-            "identifier": "VA-OM-OM-035",
+            "dataQuality": true,
             "description": "<p>Franchise Fund FY 2010 Annual Report</p>",
-            "title": "Franchise Fund FY 2010 Annual Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76740,26 +76723,55 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-035",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund",
+                "fy 2010"
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
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Franchise Fund FY 2010 Annual Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/twqi-8g6f",
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
+            "description": "VA Community Care Comparison or VAC3 (formerly Why Not the Best VA) is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.\u00a0 This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.\u00a0VAC3 data tables are updated every quarter.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/twqi-8g6f/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/twqi-8g6f",
             "issued": "2022-08-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2021-10-01/2022-09-30",
-            "modified": "2023-03-21",
             "keyword": [
                 "2022",
                 "fy2022",
@@ -76783,49 +76795,52 @@
                 "veteran",
                 "wntbva"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHASAILOperations",
-                "hasEmail": "mailto:VHASAILOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/twqi-8g6f",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-03-21",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/twqi-8g6f",
-            "description": "VA Community Care Comparison or VAC3 (formerly Why Not the Best VA) is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.\u00a0 This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.\u00a0VAC3 data tables are updated every quarter.",
-            "title": "VA Community Care Comparison (VAC3) - FY2022 All Facilities",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/twqi-8g6f/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2021-10-01/2022-09-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Community Care Comparison (VAC3) - FY2022 All Facilities"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/January_15_2015_Pending_Access_Data_using_Preferred_Date_020515.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Access Data using Perferred Date 2015-02-05"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-071",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-01-15T05:00:00Z/2015-01-15T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -76839,71 +76854,40 @@
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
-            "identifier": "VA-VHA-OIA-071",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Feb 5",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/January_15_2015_Pending_Access_Data_using_Preferred_Date_020515.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Access Data using Perferred Date 2015-02-05"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-01-15T05:00:00Z/2015-01-15T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Feb 5"
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
-            "temporal": "2011-04-01T04:00:00Z/2011-06-30T04:00:00Z",
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
-            "identifier": "VA-OM-OM-091",
+            "dataQuality": true,
             "description": "<p>FY 2011 Third Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2011 Third Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76912,43 +76896,43 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-091",
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
+            "temporal": "2011-04-01T04:00:00Z/2011-06-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2011 Third Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/txzr-vagh",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "minnesota"
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
-            "identifier": "VA-OEI-OEI-193",
             "description": "<p>This summary describes the programs and services VA provided in Minnesota in fiscal year 2015.</p>",
-            "title": "State Summary: Minnesota",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76957,41 +76941,41 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-193",
+            "issued": "2017-07-26",
+            "keyword": [
+                "minnesota"
+            ],
+            "landingPage": "https://www.data.va.gov/d/txzr-vagh",
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
+            "title": "State Summary: Minnesota"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tytr-2nb3",
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
-            "identifier": "c116beef-ed56-4212-a5e9-65cb41132b5c",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Missouri FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76999,43 +76983,44 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "c116beef-ed56-4212-a5e9-65cb41132b5c",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tytr-2nb3",
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
+            "title": "State Summary Missouri FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tz36-rieh",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2023-07-07",
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
-            "identifier": "https://www.data.va.gov/api/views/tz36-rieh",
+            "dataQuality": true,
             "description": "This dataset provides results for between-arm comparisons of continuous measures. Included is information on score differences, p-value for statistical test, and study-reported effect sizes. \n\nWhere possible, the between-arm standardized effect size was calculated, using Hedges\u2019 g. We calculated Hedges\u2019 g based on the following (in order of preference): 1) adjusted mean difference; 2) follow-up scores; 3) unadjusted mean difference; 4) change scores. For the calculated effect size, information on the basis for calculation is included along with measures of variance. Negative values for Hedges\u2019 g indicate a larger decrease (or lower follow-up score) in the first arm than in the second arm, while positive values indicate the reverse. \n\nEach comparison is on a separate row, and pairwise as well as omnibus (multi-arm) comparisons are included. There are also separate rows for each measure, time point and analysis type.",
-            "title": "PTSD Dichotomous Outcomes Between Arms",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77043,46 +77028,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tz36-rieh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tz36-rieh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tz36-rieh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/tz36-rieh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tz36-rieh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tz36-rieh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/tz36-rieh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/tz36-rieh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/tz36-rieh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "PTSD-Repository"
+            "identifier": "https://www.data.va.gov/api/views/tz36-rieh",
+            "issued": "2023-07-07",
+            "keyword": [
+                "ptsd-repository"
             ],
+            "landingPage": "https://www.data.va.gov/d/tz36-rieh",
             "language": [
                 "en-US"
-            ]
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
+            "theme": [
+                "PTSD-Repository"
+            ],
+            "title": "PTSD Dichotomous Outcomes Between Arms"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR42_032016_Retrospective_Wait_Times_Desired_Date_by_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 29 Feb 2016"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-739",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2016-02-29T05:00:00Z/2016-02-29T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -77096,70 +77111,38 @@
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
-            "identifier": "VA-VHA-OIA-739",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2016 Feb 29",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR42_032016_Retrospective_Wait_Times_Desired_Date_by_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 29 Feb 2016"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2016-02-29T05:00:00Z/2016-02-29T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2016 Feb 29"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/tzpf-8r7q",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-11-01T04:00:00Z/2014-11-30T05:00:00Z",
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
-            "identifier": "VA-OM-OM-106",
             "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "COIN 0022 CARS MONTHLY TOTALS Nov 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77167,41 +77150,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-106",
+            "issued": "2017-07-26",
+            "keyword": [
+                "establishments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/tzpf-8r7q",
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
+            "title": "COIN 0022 CARS MONTHLY TOTALS Nov 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/u25i-tmwr",
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
-            "identifier": "d11b744e-0537-42bf-9155-7a5b4167771c",
+            "dataQuality": true,
             "description": "<p>\u00a0The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Illinois FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77209,22 +77193,50 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "d11b744e-0537-42bf-9155-7a5b4167771c",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/u25i-tmwr",
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
+            "title": "State Summary Illinois FY2017"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN4FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 4 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-078",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -77240,56 +77252,56 @@
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
-            "identifier": "VA-VHA-OIA-078",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 4",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN4FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 4 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 4"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VAAccessAuditSystemWideFACTSHEET060914.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Nationwide Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-074",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -77304,71 +77316,43 @@
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
-            "identifier": "VA-VHA-OIA-074",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: System-Wide Overview",
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
-                    "downloadURL": "https://www.va.gov/health/docs/VAAccessAuditSystemWideFACTSHEET060914.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Nationwide Fact Sheet"
-                }
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: System-Wide Overview"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/u47w-6bf8",
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
-            "identifier": "https://www.data.va.gov/api/views/u47w-6bf8",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to encourage membership in units of the Selected Reserve of the Ready Reserve and to provide educational assistance to members of the reserve components called or ordered to active service in response to a war or national emergency declared by the President or Congress. Generally, to qualify for benefits under MGIB-SR you must (1) Have a six-year obligation to serve in the Selected Reserve signed after June 30, 1985. If you are an officer, you must have agreed to serve six years in addition to your original obligation. For some types of training, it is necessary to have a six-year commitment that begins after September 30, 1990; (2) Complete your initial active duty for training (IADT); (3) Meet the requirement to receive a high school diploma or equivalency certificate before completing IADT. You may not use 12 hours toward a college degree to meet this requirement; and (4) Remain in good standing while serving in an active Selected Reserve unit. Generally, to qualify for benefits under REAP you must have served at least 90 consecutive days on active duty as a result of a call or order to active duty from a reserve component in response to a war or national emergency declared by the President or Congress. This is not a complete list of eligibility requirements. For more information on MGIB-SR and REAP visit <a href=\"http://www.gibill.va.gov\">http://www.gibill.va.gov</a>.</p>",
-            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM DEC2018",
-            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77376,62 +77360,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/u47w-6bf8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/u47w-6bf8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/u47w-6bf8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/u47w-6bf8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/u47w-6bf8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/u47w-6bf8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/u47w-6bf8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/u47w-6bf8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/u47w-6bf8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/u47w-6bf8",
+            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 032"
+            ],
+            "landingPage": "https://www.data.va.gov/d/u47w-6bf8",
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
+            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ea.oit.va.gov/docs/VA_Enterprise_Roadmap_2_FINAL_20140409.pdf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "enterprise",
-                "roadmap",
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
-            "identifier": "VA-OIT-OIT-022",
             "description": "<p>Enterprise Roadmap 2</p>",
-            "title": "Enterprise Roadmap 2 Final",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77440,41 +77422,43 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OIT-OIT-022",
+            "issued": "2017-07-26",
+            "keyword": [
+                "enterprise",
+                "roadmap",
+                "va"
+            ],
+            "landingPage": "https://www.ea.oit.va.gov/docs/VA_Enterprise_Roadmap_2_FINAL_20140409.pdf",
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
+            "title": "Enterprise Roadmap 2 Final"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/u4yv-4ckh",
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
-            "identifier": "d5a98001-851f-41ed-bb35-524f437c8be5",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Florida FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77482,37 +77466,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "d5a98001-851f-41ed-bb35-524f437c8be5",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/u4yv-4ckh",
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
+            "title": "State Summary Florida FY2016"
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
-                "fy 2011",
-                "report"
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
-            "identifier": "VA-OIT-OIT-019",
             "description": "<p>CIO Annual Report</p>",
-            "title": "OIT CIO Annual Report for FY 2011",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77521,53 +77504,83 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OIT-OIT-019",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy 2011",
+                "report"
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
+            "title": "OIT CIO Annual Report for FY 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/u6fj-tfsk",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "mississippi",
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
-            "identifier": "https://www.data.va.gov/api/views/u6fj-tfsk",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Mississippi",
+            "identifier": "https://www.data.va.gov/api/views/u6fj-tfsk",
+            "issued": "2021-08-26",
+            "keyword": [
+                "mississippi",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/u6fj-tfsk",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-12",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Mississippi"
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
+                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX_FY07_Rev_090401.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-033",
             "issued": "2017-07-26",
-            "temporal": "2006-10-01T04:00:00Z/2007-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -77581,66 +77594,38 @@
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
-            "identifier": "VA-OEI-OEI-033",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2007",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX_FY07_Rev_090401.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2006-10-01T04:00:00Z/2007-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/u7r4-u4u8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "arizona"
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
-            "identifier": "VA-OEI-OEI-172",
+            "dataQuality": true,
             "description": "<p>This summary describes the programs and services VA provided in Arizona in FY2015.</p>",
-            "title": "State Summary: Arizona",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77649,71 +77634,71 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-172",
+            "issued": "2017-07-26",
+            "keyword": [
+                "arizona"
+            ],
+            "landingPage": "https://www.data.va.gov/d/u7r4-u4u8",
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
+            "title": "State Summary: Arizona"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/u7w8-rf26",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Kansas FY2023",
+            "identifier": "https://www.data.va.gov/api/views/u7w8-rf26",
             "issued": "2024-06-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fy2024",
                 "kansas",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/u7w8-rf26",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/u7w8-rf26",
-            "description": "NCVAS State Summary Kansas FY2023",
-            "title": "NCVAS State Summary Kansas FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Kansas FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/u994-zxht",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
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
-            "identifier": "7ef68f38-59e6-436f-be37-8bd24818a617",
+            "dataQuality": true,
             "description": "<p>To show count of Veterans with an SCD rating (including 0%) (Living only) by County for DoD.</p>",
-            "title": "SCD rating (including 0%) by county",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77721,38 +77706,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "7ef68f38-59e6-436f-be37-8bd24818a617",
+            "issued": "2019-04-24",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/u994-zxht",
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
+            "title": "SCD rating (including 0%) by county"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/FUND/Strategic_Plans.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-01-01T05:00:00Z/2015-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "franchise fund",
-                "strategic plan"
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
-            "identifier": "VA-OM-OM-042",
+            "dataQuality": true,
             "description": "<p>Department of Veterans Affairs Franchise Fund Strategic Plan 2010-2015</p>",
-            "title": "Department of Veterans Affairs Franchise Fund Strategic Plan 2010-2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77761,46 +77744,43 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-042",
+            "issued": "2017-07-26",
+            "keyword": [
+                "franchise fund",
+                "strategic plan"
+            ],
+            "landingPage": "https://www.va.gov/FUND/Strategic_Plans.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2010-01-01T05:00:00Z/2015-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Franchise Fund Strategic Plan 2010-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uafb-ne25",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-25",
-            "keyword": [
-                "fy2021",
-                "ncvas",
-                "state summary",
-                "territories",
-                "va facilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alysia D. Blake",
                 "hasEmail": "mailto:alysia.blake@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/uafb-ne25",
             "description": "FY 2021 VA facilities data used to populate the NCVAS State summaries created in FY2023.",
-            "title": "FY2021 NCVAS Facilities Data Summary Including Territories for 2023 State Summaries",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77808,63 +77788,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uafb-ne25/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uafb-ne25/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uafb-ne25/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/uafb-ne25/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uafb-ne25/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uafb-ne25/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uafb-ne25/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uafb-ne25/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uafb-ne25/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/uafb-ne25",
+            "issued": "2023-06-19",
+            "keyword": [
+                "fy2021",
+                "ncvas",
+                "state summary",
+                "territories",
+                "va facilities"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uafb-ne25",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-25",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY2021 NCVAS Facilities Data Summary Including Territories for 2023 State Summaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Veterans_enrolled_in_VGLI_by_state_as_of_10_31_10.xls",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2010-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Veterans_enrolled_in_VGLI_by_state_as_of_10_31_10.xls"
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
-            "identifier": "VA-VBA-INS2010-003",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of October 31, 2010.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "Number of Veterans Insured by VGLI by State as of October 31, 2010",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77872,46 +77851,51 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2010-003",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Veterans_enrolled_in_VGLI_by_state_as_of_10_31_10.xls",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Veterans_enrolled_in_VGLI_by_state_as_of_10_31_10.xls"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2010-10-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Veterans Insured by VGLI by State as of October 31, 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uaxc-gye5",
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
-            "identifier": "20e24c5f-23d5-441e-8207-3e080086b167",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Guam FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77919,42 +77903,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "20e24c5f-23d5-441e-8207-3e080086b167",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uaxc-gye5",
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
+            "title": "State Summary Guam FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ucby-28h2",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "florida"
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
-            "identifier": "VA-OEI-OEI-178",
             "description": "<p>This summary describes the programs and services VA provided in Florida in fiscal year 2015.</p>",
-            "title": "State Summary: Florida",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77963,54 +77947,73 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-178",
+            "issued": "2017-07-26",
+            "keyword": [
+                "florida"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ucby-28h2",
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
+            "title": "State Summary: Florida"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ud6n-i3kg",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Texas FY2023",
+            "identifier": "https://www.data.va.gov/api/views/ud6n-i3kg",
             "issued": "2024-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "texas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/ud6n-i3kg",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/ud6n-i3kg",
-            "description": "NCVAS State Summary Texas FY2023",
-            "title": "NCVAS State Summary Texas FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Texas FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/uddx-ppad",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "VA Volunteer Information",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Voluntary Service System (VSS) is a national-level application which replaced the site-based Voluntary Timekeeping System (VTK). VTK was used for many years at the Veterans Affairs Medical Centers to track and manage the hours of service contributed by volunteers and volunteer organizations. Consistency of data between sites was a problem and the process of compiling national VTK reports was slow and costly. Many steps were involved because national data was only consolidated once a month and it was usually out of sync. Improved data collection and reporting is now available since users interact directly with a centralized national database. Rehosted VSS uses .NET technology that replaced data transmissions between sites and the Austin Information Technology Center to produce the consolidated national reports. Direct access to data provides instantaneous updates and up-to-the-minute reporting for all users. Central Office administrators and Voluntary staff now have broader more reliable data for managing Volunteer Services.</p>",
+            "identifier": "VA-VHA-OM-003",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2003-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "tracking",
                 "va",
@@ -78018,63 +78021,42 @@
                 "voluntary",
                 "volunteer"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/uddx-ppad",
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
-            "identifier": "VA-VHA-OM-003",
-            "description": "<p>Voluntary Service System (VSS) is a national-level application which replaced the site-based Voluntary Timekeeping System (VTK). VTK was used for many years at the Veterans Affairs Medical Centers to track and manage the hours of service contributed by volunteers and volunteer organizations. Consistency of data between sites was a problem and the process of compiling national VTK reports was slow and costly. Many steps were involved because national data was only consolidated once a month and it was usually out of sync. Improved data collection and reporting is now available since users interact directly with a centralized national database. Rehosted VSS uses .NET technology that replaced data transmissions between sites and the Austin Information Technology Center to produce the consolidated national reports. Direct access to data provides instantaneous updates and up-to-the-minute reporting for all users. Central Office administrators and Voluntary staff now have broader more reliable data for managing Volunteer Services.</p>",
-            "title": "Voluntary Service System (VSS)",
-            "programCode": [
-                "029:040"
-            ],
+            "rights": "VA Volunteer Information",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2003-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Voluntary Service System (VSS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ude6-nw2w",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "N/A",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-09-08T04:00:00Z/2015-09-08T04:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "historic",
-                "register"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James KillensIII",
                 "hasEmail": "mailto:james.killensiii@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-NCA-HIS-002",
+            "dataQuality": true,
             "description": "<p>The Department of the Interior, National Park Service, which oversees the National Register of Historic Places (NRHP), in 2011 determined that all developed sections of all national cemeteries are eligible for the NRHP regardless of age. This means that all undertakings or projects at these cemeteries must be reviewed by state historic preservation officers per Section 106, National Historic Preservation Act of 1966, prior to NCA awarding contracts or initiating work.</p>",
-            "title": "National Register Eligibility of National Cemeteries - A Clarification of Policy",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78083,45 +78065,48 @@
                     "title": "National Register Eligibility of National Cemeteries - A Clarification of Policy"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-HIS-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "historic",
+                "register"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ude6-nw2w",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "N/A",
+            "temporal": "2011-09-08T04:00:00Z/2015-09-08T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Register Eligibility of National Cemeteries - A Clarification of Policy"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/udp2-wgg5",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2023-07-07",
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
-            "identifier": "https://www.data.va.gov/api/views/udp2-wgg5",
+            "dataQuality": true,
             "description": "This dataset provides between-arm results for dichotomous outcomes: loss of diagnosis and clinically meaningful response. Included is information on how loss of diagnosis and clinically meaningful response were defined, p-value for statistical test, and study-reported effect sizes. \n\nEach comparison is on a separate row, and pairwise as well as omnibus (multi-arm) comparisons are included. There are also separate rows for studies with more than one measure, time point and analysis type or when there is with more than one definition of diagnostic change or clinically meaningful change.",
-            "title": "PTSD Continuous Outcomes Between Arms",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78129,66 +78114,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/udp2-wgg5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/udp2-wgg5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/udp2-wgg5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/udp2-wgg5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/udp2-wgg5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/udp2-wgg5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/udp2-wgg5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/udp2-wgg5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/udp2-wgg5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "PTSD-Repository"
+            "identifier": "https://www.data.va.gov/api/views/udp2-wgg5",
+            "issued": "2023-07-07",
+            "keyword": [
+                "ptsd-repository"
             ],
+            "landingPage": "https://www.data.va.gov/d/udp2-wgg5",
             "language": [
                 "en-US"
-            ]
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
+            "theme": [
+                "PTSD-Repository"
+            ],
+            "title": "PTSD Continuous Outcomes Between Arms"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ufuk-sphg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "korean conflict",
-                "korean war",
-                "veteran population",
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
-            "identifier": "https://www.data.va.gov/api/views/ufuk-sphg",
             "description": "Korean War Era Veterans by Age Group, Fiscal Year 2020. This data set supports the Korean War data story at: https://www.datahub.va.gov/stories/s/7wja-85c3",
-            "title": "Korean War Era Veterans by Age Group, FY 2020",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78196,57 +78177,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ufuk-sphg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ufuk-sphg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ufuk-sphg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ufuk-sphg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ufuk-sphg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ufuk-sphg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ufuk-sphg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ufuk-sphg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ufuk-sphg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/ufuk-sphg",
+            "issued": "2020-12-15",
+            "keyword": [
+                "korean conflict",
+                "korean war",
+                "veteran population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ufuk-sphg",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Korean War Era Veterans by Age Group, FY 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ufv8-ir84",
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
-            "identifier": "https://www.data.va.gov/api/views/ufv8-ir84",
+            "dataQuality": true,
             "description": "<p>VBA PROGRAM BENEFITS for Automobiles and Adaptive Equipment for Certain Disabled Veterans and Members of the Armed Forces. Veterans with honorable service and servicepersons on duty having a service-connected disability due to loss or permanent loss of use of one or both feet, one or both hands, or a permanent impairment of vision of both eyes to a prescribed degree. For adaptive equipment only, eligibility also exists if there is service-connected ankylosis of one or both knees or one or both hips. Personnel on active duty also qualify under the same criteria as veterans. Uses &amp; Use Restrictions:  Assistance toward purchase of an automobile or other conveyance is a one-time payment only. Necessary adaptive equipment may be furnished, repaired, replaced, or reinstalled on a conveyance which may be purchased with assistance or any other conveyance subsequently or previously acquired. Adaptive equipment will be provided for no more than two conveyances during any four-year period unless one of those two vehicles becomes unavailable to the veteran.</p>",
-            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE NOV2018",
-            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78254,61 +78238,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ufv8-ir84/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ufv8-ir84/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ufv8-ir84/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ufv8-ir84/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ufv8-ir84/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ufv8-ir84/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ufv8-ir84/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ufv8-ir84/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ufv8-ir84/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/ufv8-ir84",
+            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 100"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ufv8-ir84",
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
+            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE NOV2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ug6a-238s",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "pennsylvania",
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
-            "identifier": "VA-OEI-OEI-124",
             "description": "<p>This is a summary of the programs or services provided by VA in Pennsylvania in fiscal year 2014.</p>",
-            "title": "State Summary:  Pennsylvania",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78317,44 +78300,44 @@
                     "title": "State Summary:  Pennsylvania"
                 }
             ],
+            "identifier": "VA-OEI-OEI-124",
+            "issued": "2017-07-26",
+            "keyword": [
+                "pennsylvania",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ug6a-238s",
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
+            "title": "State Summary:  Pennsylvania"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ugb5-p35y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-10-04",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "historical period estimate",
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
-            "identifier": "https://www.data.va.gov/api/views/ugb5-p35y",
             "description": "The Department of Veterans Affairs provides official estimates and projections of the Veteran population using the Veteran Population Projection Model (VetPop). Based on the available information through September 30, 2020, the latest model VetPop2020 estimated the Veteran population for the period from 2000 to 2020. The \u201cNumber of Estimated Veterans by Gender and Age Group, 9/30/2000 to 9/30/2020\u201d data table shows the number of living Veterans at the end of each fiscal year from 2000 to 2020.",
-            "title": "VetPop2020 National Estimates 2000 to 2020",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78362,58 +78345,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ugb5-p35y/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ugb5-p35y/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ugb5-p35y/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ugb5-p35y/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ugb5-p35y/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ugb5-p35y/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ugb5-p35y/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ugb5-p35y/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ugb5-p35y/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ugb5-p35y",
+            "issued": "2022-10-04",
+            "keyword": [
+                "historical period estimate",
+                "veteran population"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ugb5-p35y",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-06",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 National Estimates 2000 to 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.techstrategies.oit.va.gov/docs/CTSNotes/TS%20Note%20Vol%202%20Issue%206%2006032015.pdf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cloud",
-                "it",
-                "service models"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Peterson",
                 "hasEmail": "mailto:mark.peterson3@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-ASD-TSNV2-006",
             "description": "<p>VA Executive's Guide to Cloud Computing: Service Models</p>",
-            "title": "TS Note Vol 2 Issue 6",
-            "programCode": [
-                "029:078"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78422,95 +78404,127 @@
                     "title": "TS Note Vol 2 Issue 6"
                 }
             ],
+            "identifier": "VA-OIT-ASD-TSNV2-006",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cloud",
+                "it",
+                "service models"
+            ],
+            "landingPage": "https://www.techstrategies.oit.va.gov/docs/CTSNotes/TS%20Note%20Vol%202%20Issue%206%2006032015.pdf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:078"
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
+            "title": "TS Note Vol 2 Issue 6"
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
+            "description": "<p>USA Spending- All-Volunteer Force Educational Assistance- Chapter 30- for January 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-023",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 124",
                 "chapter 30",
                 "education",
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
-            "identifier": "VA-VBA-USASPENDING012014-023",
-            "description": "<p>USA Spending- All-Volunteer Force Educational Assistance- Chapter 30- for January 2014</p>",
-            "title": "USA Spending file- Education- Chapter 30- CFDA 64.124",
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
+            "title": "USA Spending file- Education- Chapter 30- CFDA 64.124"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ui2h-b5mh",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Guam FY2023",
+            "identifier": "https://www.data.va.gov/api/views/ui2h-b5mh",
             "issued": "2024-06-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fy2023",
                 "guam",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/ui2h-b5mh",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/ui2h-b5mh",
-            "description": "NCVAS State Summary Guam FY2023",
-            "title": "NCVAS State Summary Guam FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Guam FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uiey-mvxj",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://github.com/vacobrydsk/VeteransCrisisLineDataDictionary/raw/master/VeteransCrisisLineDataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "<p>Aggregation data released on Freedom of Information Act (FOIA) Request 15-00242-F appeal.  Fields with value of b6 indicate data withheld in accordance with VHA Expert Determination methodology and/or VA Office of General Counsel direction.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/uiey-mvxj/text/plain",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "VA-VHA-10N-004",
+            "isPartOf": "VA-VHA-10N-013",
             "issued": "2017-07-26",
-            "temporal": "2011-01-01T05:00:00Z/2014-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
             "keyword": [
                 "ai",
                 "crisis",
@@ -78526,68 +78540,37 @@
                 "veteran",
                 "vha"
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
-            "identifier": "VA-VHA-10N-004",
-            "description": "<p>Aggregation data released on Freedom of Information Act (FOIA) Request 15-00242-F appeal.  Fields with value of b6 indicate data withheld in accordance with VHA Expert Determination methodology and/or VA Office of General Counsel direction.</p>",
-            "title": "Veterans Crisis Line calls CY2011-FY2014 Aggregate Data",
-            "isPartOf": "VA-VHA-10N-013",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:042"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/uiey-mvxj/text/plain",
-                    "mediaType": "text/plain"
-                }
+            "landingPage": "https://www.data.va.gov/d/uiey-mvxj",
+            "language": [
+                "en-US"
             ],
-            "describedBy": "https://github.com/vacobrydsk/VeteransCrisisLineDataDictionary/raw/master/VeteransCrisisLineDataDictionary.xlsx",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-01-01T05:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "Suicide Prevention"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Crisis Line calls CY2011-FY2014 Aggregate Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uiu8-pf4g",
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
-            "identifier": "OM-OM-169",
             "description": "<p>COIN report 0022 March 2016</p>",
-            "title": "COIN 0022 March 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78595,41 +78578,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-169",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uiu8-pf4g",
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
+            "title": "COIN 0022 March 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/uj56-gy9u",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-10",
-            "keyword": [
-                "veteran population",
-                "veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/uj56-gy9u",
             "description": "",
-            "title": "Veteran Race Ethnicity Distribution: FY 2023-2050",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78637,39 +78620,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uj56-gy9u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uj56-gy9u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uj56-gy9u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/uj56-gy9u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uj56-gy9u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uj56-gy9u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uj56-gy9u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uj56-gy9u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uj56-gy9u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/uj56-gy9u",
+            "issued": "2024-08-08",
+            "keyword": [
+                "veteran population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uj56-gy9u",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-10",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veteran Race Ethnicity Distribution: FY 2023-2050"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ujhx-xnby",
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
+            "description": "Why Not the Best VA or WNTBVA is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.  This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.  This currently only has Q1 and Q4 data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/ujhx-xnby/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/ujhx-xnby",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2020-10-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-10-01/2020-09-30",
-            "modified": "2021-06-24",
             "keyword": [
                 "2020",
                 "fy2020",
@@ -78691,73 +78704,40 @@
                 "veteran",
                 "wntbva"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Sail Operations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/ujhx-xnby",
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
-            "identifier": "https://www.data.va.gov/api/views/ujhx-xnby",
-            "description": "Why Not the Best VA or WNTBVA is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.  This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.  This currently only has Q1 and Q4 data.",
-            "title": "Why Not the Best VA FY2020 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/ujhx-xnby/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2019-10-01/2020-09-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Why Not the Best VA FY2020 Hospital Performance - All Facilities"
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
-            "identifier": "VA-VBA-ABR2012-088",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Georgia-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78765,49 +78745,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-088",
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
+            "title": "Georgia-FY12 Benefits Summary"
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
-            "identifier": "VA-VBA-ABR2012-021",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Most Prevalent Service Connected Disabilities for Veterans Who Began Receiving Compensation During FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78815,46 +78795,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-021",
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
+            "title": "Most Prevalent Service Connected Disabilities for Veterans Who Began Receiving Compensation During FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ukth-b7hr",
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
-            "identifier": "https://www.data.va.gov/api/views/ukth-b7hr",
             "description": "Veterans Utilization Profile FY18 - Fig 15, Trend in Percent Health Care Enrolled Users, Enrolled Non-Users & Non-Enrolled among Service-Connected Disabled. Data underlying the second figure of Part 3 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 15, Trend in Percent Health Care Enrolled Users, Enrolled Non-Users & Non-Enrolled among Service-Connected Disabled",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78862,38 +78843,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ukth-b7hr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ukth-b7hr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ukth-b7hr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ukth-b7hr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ukth-b7hr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ukth-b7hr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ukth-b7hr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ukth-b7hr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ukth-b7hr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/ukth-b7hr",
+            "issued": "2020-11-19",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ukth-b7hr",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-12-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 15, Trend in Percent Health Care Enrolled Users, Enrolled Non-Users & Non-Enrolled among Service-Connected Disabled"
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
+                    "downloadURL": "https://www.data.va.gov/download/um24-98en/text/plain",
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
@@ -78912,73 +78925,40 @@
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
-                    "downloadURL": "https://www.data.va.gov/download/um24-98en/text/plain",
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
-                "education",
-                "education benefits fy12",
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
-            "identifier": "VA-VBA-ABR2012-040",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Unique Beneficiaries and Payments by Fiscal Year ($000)",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78987,70 +78967,77 @@
                     "title": "Unique Beneficiaries and Payments by Fiscal Year ($000)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-040",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "education",
+                "education benefits fy12",
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
+            "title": "Unique Beneficiaries and Payments by Fiscal Year ($000)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/umiy-kxpr",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Oklahoma FY2023",
+            "identifier": "https://www.data.va.gov/api/views/umiy-kxpr",
             "issued": "2024-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "oklahoma"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/umiy-kxpr",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/umiy-kxpr",
-            "description": "NCVAS State Summary Oklahoma FY2023",
-            "title": "NCVAS State Summary Oklahoma FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Oklahoma FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/unhx-5tdv",
-            "issued": "2024-06-21",
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
-            "identifier": "https://www.data.va.gov/api/views/unhx-5tdv",
             "description": "",
-            "title": "VA Facilities Aggregated and Order FY2024",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79058,68 +79045,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/unhx-5tdv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/unhx-5tdv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/unhx-5tdv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/unhx-5tdv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/unhx-5tdv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/unhx-5tdv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/unhx-5tdv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/unhx-5tdv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/unhx-5tdv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/unhx-5tdv",
+            "issued": "2024-06-21",
+            "landingPage": "https://www.data.va.gov/d/unhx-5tdv",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA Facilities Aggregated and Order FY2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/unpa-2pxe",
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
-            "identifier": "VA-VHA-OIA-031",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset contains the data regarding the volume of surgical procedures performed at a facility.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Procedure Volume",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset contains the data regarding the volume of surgical procedures performed at a facility.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79127,66 +79103,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/unpa-2pxe/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/unpa-2pxe/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/unpa-2pxe/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/unpa-2pxe/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/unpa-2pxe/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/unpa-2pxe/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/unpa-2pxe/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/unpa-2pxe/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/unpa-2pxe/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-031",
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
+            "landingPage": "https://www.data.va.gov/d/unpa-2pxe",
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
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Procedure Volume"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/unsi-yiy6",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "burial grants",
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
-            "identifier": "VA-NCA-CGP-001",
             "description": "<p>This fact sheet provides background and historical information on the Cemtery Grants Program</p>",
-            "title": "Veterans Cemetery Grants Program Fact Sheet",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79195,46 +79178,43 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-NCA-CGP-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "burial grants",
+                "cemerty grants"
+            ],
+            "landingPage": "https://www.data.va.gov/d/unsi-yiy6",
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
+            "title": "Veterans Cemetery Grants Program Fact Sheet"
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
-            "identifier": "VA-VBA-ABR2012-044",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report( ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the benefitciaries</p>",
-            "title": "Loans Guaranteed by Period of Service Entitlement During Fiscal Year 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79242,45 +79222,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-044",
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
                 "Use of Benefits and Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Loans Guaranteed by Period of Service Entitlement During Fiscal Year 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/upex-ajwq",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "json",
-                "mumps",
-                "vista"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RON DIMICELI",
                 "hasEmail": "mailto:ron.dimiceli@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-OIT-998",
             "description": "<p>Encode MUMPS array to JSON string and decode a JSON formatted string into a MUMPS array.</p>",
-            "title": "VistA JSON Utility",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79289,46 +79271,44 @@
                     "title": "VistA JSON Utility"
                 }
             ],
+            "identifier": "VA-OIT-OIT-998",
+            "issued": "2017-07-26",
+            "keyword": [
+                "json",
+                "mumps",
+                "vista"
+            ],
+            "landingPage": "https://www.data.va.gov/d/upex-ajwq",
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
+            "title": "VistA JSON Utility"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uq82-m9cd",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-09-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-27",
-            "keyword": [
-                "2019",
-                "fy19",
-                "fy 19",
-                "fy2019",
-                "fy 2019",
-                "pension",
-                "state"
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
-            "identifier": "https://www.data.va.gov/api/views/uq82-m9cd",
+            "dataQuality": true,
             "description": "This report provides state-level estimates of the number of Veterans who received VA Pension benefits during fiscal year 2019. It includes the Veterans\u2019 gender. Blank values represent small cell counts that have been suppressed to protect the identity of Veterans. Some categories may not sum to the total due to missing information (e.g., gender, etc.).\n\nSource: Department of Veterans Affairs, Office of Enterprise Integration, United States Veterans Eligibility Trends & Statistics (USVETS) 2019 and Veterans Benefits Administration VETSNET FY 2019 pension data.\n\nPrepared by National Center for Veterans Analysis & Statistics, www.va.gov/vetdata.",
-            "title": "FY 2019 Pension Recipients by State",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79336,47 +79316,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uq82-m9cd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uq82-m9cd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uq82-m9cd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/uq82-m9cd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uq82-m9cd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uq82-m9cd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uq82-m9cd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uq82-m9cd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uq82-m9cd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/uq82-m9cd",
+            "issued": "2024-09-27",
+            "keyword": [
+                "2019",
+                "fy19",
+                "fy 19",
+                "fy2019",
+                "fy 2019",
+                "pension",
+                "state"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uq82-m9cd",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-27",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2019 Pension Recipients by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uq8f-egtz",
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
+            "description": "<p>Primary care and specialty care visits seen and completed within 30 days or less.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset10_Access_To_Care.xml",
+                    "mediaType": "application/xml",
+                    "title": "Access to Care"
+                }
             ],
+            "identifier": "VA-VHA-OIA-036",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -79399,81 +79411,75 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/uq8f-egtz",
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
-            "identifier": "VA-VHA-OIA-036",
-            "description": "<p>Primary care and specialty care visits seen and completed within 30 days or less.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Access to Care",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset10_Access_To_Care.xml",
-                    "mediaType": "application/xml",
-                    "title": "Access to Care"
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
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Access to Care"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/uqw3-kmqf",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Minnesota FY2023",
+            "identifier": "https://www.data.va.gov/api/views/uqw3-kmqf",
             "issued": "2024-06-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2024",
                 "minnesota",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/uqw3-kmqf",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/uqw3-kmqf",
-            "description": "NCVAS State Summary Minnesota FY2023",
-            "title": "NCVAS State Summary Minnesota FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Minnesota FY2023"
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
+            "description": "<p>USA Spending- Education-Post 9/11 Veterans Educational Assistance ( Chapter33) for February 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING022014-036",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 028",
                 "ch33",
@@ -79481,45 +79487,51 @@
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
-            "identifier": "VA-VBA-USASPENDING022014-036",
-            "description": "<p>USA Spending- Education-Post 9/11 Veterans Educational Assistance ( Chapter33) for February 2014.</p>",
-            "title": "USA Spending file- 02/2014-Education- Chapter 33/ CFDA 64.028",
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
+            "title": "USA Spending file- 02/2014-Education- Chapter 33/ CFDA 64.028"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/urkv-fawm",
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
+            "description": "<p>Medical Center physician and nurse staffing, and nurse turnover rates.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset4_Medical_Center_Staffing.xml",
+                    "mediaType": "application/xml",
+                    "title": "Medical Center Staffing"
+                }
             ],
+            "identifier": "VA-VHA-OIA-041",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -79542,69 +79554,40 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/urkv-fawm",
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
-            "identifier": "VA-VHA-OIA-041",
-            "description": "<p>Medical Center physician and nurse staffing, and nurse turnover rates.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Medical Center Staffing",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset4_Medical_Center_Staffing.xml",
-                    "mediaType": "application/xml",
-                    "title": "Medical Center Staffing"
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
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Medical Center Staffing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/usud-j663",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "new hampshire",
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
-            "identifier": "VA-OEI-OEI-116",
             "description": "<p>This is a summary of the programs and services provided by VA in New Hampshire in fiscal year 2014.</p>",
-            "title": "State Summary:  New Hampshire",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79613,26 +79596,56 @@
                     "title": "State Summary:  New Hampshire"
                 }
             ],
+            "identifier": "VA-OEI-OEI-116",
+            "issued": "2017-07-26",
+            "keyword": [
+                "new hampshire",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/usud-j663",
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
+            "title": "State Summary:  New Hampshire"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Quick_Facts.asp",
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
+            "description": "<p>This document shows trends in the geographic distribution of VA expenditures.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/vetdata/docs/QuickFacts/Gdx-trends.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-040",
             "issued": "2017-07-26",
-            "temporal": "1999-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -79646,67 +79659,38 @@
                 "insurance",
                 "medical care"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Andrew Bickel",
-                "hasEmail": "mailto:andrew.bickel@va.gov"
-            },
+            "landingPage": "https://www.va.gov/vetdata/Quick_Facts.asp",
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
-            "identifier": "VA-OEI-OEI-040",
-            "description": "<p>This document shows trends in the geographic distribution of VA expenditures.</p>",
-            "title": "Trends in Geographic Distribution of VA Expenditures",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/QuickFacts/Gdx-trends.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "1999-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Trends in Geographic Distribution of VA Expenditures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uuw9-ayv7",
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
-            "identifier": "https://www.data.va.gov/api/views/uuw9-ayv7",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to help servicepersons adjust to civilian life after separation from military service, assist in the recruitment and retention of highly qualified personnel in the active and reserve components in the Armed Forces by providing education benefits, and to provide educational opportunities to the dependents of certain service members and veterans. Individuals who entered active duty after September 10, 2001 may be eligible for the Post-9/11 GI Bill. Individuals can use the Post-9/11 GI Bill after serving 90 days on active duty (excluding entry level and skill training). Only periods of active duty under title 10 will be used to establish eligibility for the Post 9/11 GI Bill. A high school diploma or equivalency certificate is always required for eligibility. Individuals who are eligible for the Montgomery GI Bill \u2013 Active Duty (chapter 30), the Montgomery GI Bill \u2013 Selected Reserve (chapter 1606), or the Reserve Educational Assistance Program (REAP) will have to make an irrevocable election to relinquish eligibility under one of those benefit programs to establish eligibility under the Post-9/11 GI Bill. The dependent children of a person who died in the line of duty while serving as a member of the Armed Forces may be eligible to use benefits under the Fry Scholarship provision of the Post-9/11 GI Bill. The spouse and/or child(ren) of a veteran or service member may be eligible for the Post 9/11 GI Bill if the veteran or service member transfers entitlement to those dependents. Eligibility to transfer entitlement to dependents is determined by the Department of Defense. This is not a complete list of eligibility requirements. For more information on the latest changes to the Post-9/11 GI Bill go to the VA web-site.</p>",
-            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE FEB2019",
-            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79714,61 +79698,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uuw9-ayv7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uuw9-ayv7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uuw9-ayv7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/uuw9-ayv7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uuw9-ayv7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uuw9-ayv7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uuw9-ayv7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uuw9-ayv7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uuw9-ayv7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/uuw9-ayv7",
+            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 028"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uuw9-ayv7",
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
+            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ux9a-eq4m",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-09-20",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "minorities",
-                "minority veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/ux9a-eq4m",
             "description": "Count of minority veterans, by period of service",
-            "title": "Minority Veterans by Period of Service",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79776,61 +79759,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ux9a-eq4m/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ux9a-eq4m/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ux9a-eq4m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ux9a-eq4m/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ux9a-eq4m/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ux9a-eq4m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ux9a-eq4m/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ux9a-eq4m/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ux9a-eq4m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ux9a-eq4m",
+            "issued": "2019-09-20",
+            "keyword": [
+                "minorities",
+                "minority veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ux9a-eq4m",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Minority Veterans by Period of Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uxdr-h8rv",
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
-            "identifier": "https://www.data.va.gov/api/views/uxdr-h8rv",
             "description": "The Department of Veterans Affairs provides official estimates and projections of the Veteran population using the Veteran Population Projection Model (VetPop). Based on the latest model VetPop2020 and the most recent national survey estimates from the 2021 American Community Survey 5-Year (ACS) data, the projected number of Veterans living in 50 states, DC and Puerto Rico for the fiscal years, 2021 to 2023, are allocated to Urban and Rural areas. As defined by the Census Bureau, those not residing in Urban areas are assumed to be in Rural areas (https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural/2010-urban-rural.html). \n\nThis table contains the Veteran estimates by urban/rural, age group, poverty, and disability. The poverty level and disability are determined by ACS based on responses on total income and functional difficulties. Refer to the sections on Poverty and Disability Status in the document, https://www2.census.gov/programs-surveys/acs/tech_docs/subject_definitions/2021_ACSSubjectDefinitions.pdf\n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2020 Urban/Rural by Poverty & Disability FY2021-2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79838,91 +79817,93 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uxdr-h8rv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uxdr-h8rv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uxdr-h8rv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/uxdr-h8rv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uxdr-h8rv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uxdr-h8rv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uxdr-h8rv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uxdr-h8rv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uxdr-h8rv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/uxdr-h8rv",
+            "issued": "2023-02-21",
+            "keyword": [
+                "rural",
+                "rural veterans",
+                "urban",
+                "veteran",
+                "veteran population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uxdr-h8rv",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-06",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 Urban/Rural by Poverty & Disability FY2021-2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/uxfi-pzk8",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "vermont",
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
-            "identifier": "https://www.data.va.gov/api/views/uxfi-pzk8",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Vermont",
+            "identifier": "https://www.data.va.gov/api/views/uxfi-pzk8",
+            "issued": "2021-08-26",
+            "keyword": [
+                "vermont",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uxfi-pzk8",
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
+            "title": "State Summaries_Vermont"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uxsx-yqmx",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2022-09-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
-            "keyword": [
-                "citation",
-                "clinicaltrials.gov",
-                "ptsdpubs",
-                "ptsd-repository",
-                "pubmed"
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
-            "identifier": "https://www.data.va.gov/api/views/uxsx-yqmx",
+            "dataQuality": true,
             "description": "Identifying information about each study, including citation, PubMed ID, PTSDPubs ID, ClinicalTrials.gov ID, and funding source(s).",
-            "title": "References and Study Identifiers",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79930,63 +79911,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uxsx-yqmx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uxsx-yqmx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uxsx-yqmx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/uxsx-yqmx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uxsx-yqmx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uxsx-yqmx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uxsx-yqmx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uxsx-yqmx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uxsx-yqmx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "PTSD-Repository"
+            "identifier": "https://www.data.va.gov/api/views/uxsx-yqmx",
+            "issued": "2022-09-28",
+            "keyword": [
+                "citation",
+                "clinicaltrials.gov",
+                "ptsdpubs",
+                "ptsd-repository",
+                "pubmed"
             ],
+            "landingPage": "https://www.data.va.gov/d/uxsx-yqmx",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2020-06-11",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
+            "theme": [
+                "PTSD-Repository"
+            ],
+            "title": "References and Study Identifiers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uy7i-khgi",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "alaska"
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
-            "identifier": "VA-OEI-OEI-171",
+            "dataQuality": true,
             "description": "<p>This summary describes the programs and services VA provided in Alaska in FY2015.</p>",
-            "title": "State Summary: Alaska",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79995,42 +79980,41 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-171",
+            "issued": "2017-07-26",
+            "keyword": [
+                "alaska"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uy7i-khgi",
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
+            "title": "State Summary: Alaska"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uya4-d7pk",
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
-            "identifier": "https://www.data.va.gov/api/views/uya4-d7pk",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located.</p>",
-            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS NOV2018",
-            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80038,46 +80022,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uya4-d7pk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uya4-d7pk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uya4-d7pk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/uya4-d7pk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uya4-d7pk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uya4-d7pk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uya4-d7pk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uya4-d7pk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uya4-d7pk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/uya4-d7pk",
+            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 114"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uya4-d7pk",
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
+            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS NOV2018"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN5FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 5 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-079",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -80093,71 +80105,43 @@
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
-            "identifier": "VA-VHA-OIA-079",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 5",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN5FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 5 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uzfn-9vc6",
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
-            "identifier": "8e108665-c1b5-4468-8628-789d85e658a2",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary District of Columbia FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80165,38 +80149,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "8e108665-c1b5-4468-8628-789d85e658a2",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uzfn-9vc6",
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
+            "title": "State Summary District of Columbia FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uzn8-u342",
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
-            "identifier": "https://www.data.va.gov/api/views/uzn8-u342",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE APR2019",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80204,60 +80187,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uzn8-u342/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uzn8-u342/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uzn8-u342/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/uzn8-u342/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uzn8-u342/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uzn8-u342/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uzn8-u342/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uzn8-u342/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uzn8-u342/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/uzn8-u342",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uzn8-u342",
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
+            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uznq-vi63",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cemeteries"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bill Barnes",
                 "hasEmail": "mailto:bill.barnes@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/uznq-vi63",
             "description": "Brief dataset displaying the percentage of Veterans that served within 75 miles of a state or national cemetery, from FY00 - FY13",
-            "title": "Percentage of Veterans Served Within 75 Miles of a State or National Cemetery",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80265,102 +80249,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uznq-vi63/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uznq-vi63/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uznq-vi63/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/uznq-vi63/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uznq-vi63/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uznq-vi63/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/uznq-vi63/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/uznq-vi63/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/uznq-vi63/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/uznq-vi63",
+            "issued": "2019-12-10",
+            "keyword": [
+                "cemeteries"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uznq-vi63",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Percentage of Veterans Served Within 75 Miles of a State or National Cemetery"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/uzux-me3d",
-            "issued": "2023-06-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
-            "keyword": [
-                "fy2021 data",
-                "illinois",
-                "ncvas state summary"
-            ],
-            "identifier": "https://www.data.va.gov/api/views/uzux-me3d",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "www.data.va.gov"
-            },
             "description": "NCVAS State Summary Illinois FY2021",
-            "title": "NCVAS State Summary Illinois FY2021"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.medicare.gov/hospitalcompare/VAData/main.html",
-            "bureauCode": [
-                "029:15"
-            ],
-            "issued": "2017-07-26",
-            "temporal": "2008-07-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.medicare.gov/hospitalcompare/VAData/main.html"
-            ],
-            "keyword": [
-                "caregiver",
-                "chf",
-                "congestive heart failure",
-                "doctor",
-                "family",
-                "health",
-                "heart attack",
-                "hospital",
-                "mortality",
-                "outcome measures",
-                "pneumonia",
-                "readmissions",
-                "surgical care",
-                "va",
-                "vamc",
-                "va medical center",
-                "veteran",
-                "veterans affairs",
-                "vha"
+            "identifier": "https://www.data.va.gov/api/views/uzux-me3d",
+            "issued": "2023-06-27",
+            "keyword": [
+                "fy2021 data",
+                "illinois",
+                "ncvas state summary"
+            ],
+            "landingPage": "https://www.data.va.gov/d/uzux-me3d",
+            "modified": "2024-06-02",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "www.data.va.gov"
+            },
+            "title": "NCVAS State Summary Illinois FY2021"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "029:15"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-020",
+            "dataQuality": true,
             "description": "<p>The Veterans Health Administration (VHA) has now collaborated with the Centers for Medicare &amp; Medicaid Services (CMS) to present information to consumers about the quality and safety of health care in VHA. VHA has approximately 50 percent of Veterans enrolled in the healthcare system who are eligible for Medicare and, therefore, have some choice in how and where they receive inpatient services. VHA has adopted healthcare transparency as a strategy to enhance public trust and to help Veterans make informed choices about their health care.VHA currently reports the following types of quality measures on Hospital Compare:<em>Timely and effective care.</em>Behavioral health.<em>Readmissions and deaths.</em>Patient safety.*Experience of care.</p>",
-            "title": "VA Hospital Compare",
-            "programCode": [
-                "029:040"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80393,43 +80357,63 @@
                     "title": "Experience of Care"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-020",
+            "issued": "2017-07-26",
+            "keyword": [
+                "caregiver",
+                "chf",
+                "congestive heart failure",
+                "doctor",
+                "family",
+                "health",
+                "heart attack",
+                "hospital",
+                "mortality",
+                "outcome measures",
+                "pneumonia",
+                "readmissions",
+                "surgical care",
+                "va",
+                "vamc",
+                "va medical center",
+                "veteran",
+                "veterans affairs",
+                "vha"
+            ],
+            "landingPage": "https://www.medicare.gov/hospitalcompare/VAData/main.html",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.medicare.gov/hospitalcompare/VAData/main.html"
+            ],
+            "temporal": "2008-07-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Section 10. National Security and Veterans Affairs"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Hospital Compare"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/v2bm-iz8v",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "women veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/v2bm-iz8v",
             "description": "Dataset showing educational attainment levels for female veterans as well as non-veterans for the year 2015",
-            "title": "Educational Attainment for Female Vets and Non-Vets, 2015",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80437,83 +80421,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v2bm-iz8v/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v2bm-iz8v/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v2bm-iz8v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/v2bm-iz8v/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v2bm-iz8v/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v2bm-iz8v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v2bm-iz8v/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v2bm-iz8v/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v2bm-iz8v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/v2bm-iz8v",
+            "issued": "2019-10-24",
+            "keyword": [
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/v2bm-iz8v",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
+            "title": "Educational Attainment for Female Vets and Non-Vets, 2015"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/v2pe-rix9",
-            "issued": "2023-06-30",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Louisiana FY2021",
+            "identifier": "https://www.data.va.gov/api/views/v2pe-rix9",
+            "issued": "2023-06-30",
             "keyword": [
                 "fy2021 data",
                 "louisiana",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/v2pe-rix9",
+            "landingPage": "https://www.data.va.gov/d/v2pe-rix9",
+            "modified": "2024-06-02",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Louisiana FY2021",
             "title": "NCVAS State Summary Louisiana FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/v36w-f99q",
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
-            "identifier": "https://www.data.va.gov/api/views/v36w-f99q",
             "description": "VA Program Use Rates within Age Groups by Gender - FY2018. Data underlying the fifth figure of Part 1 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 6, Rates of Use within Age Groups by Gender - FY2018",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80521,42 +80502,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v36w-f99q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v36w-f99q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v36w-f99q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/v36w-f99q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v36w-f99q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v36w-f99q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v36w-f99q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v36w-f99q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v36w-f99q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/v36w-f99q",
+            "issued": "2020-10-19",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/v36w-f99q",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 6, Rates of Use within Age Groups by Gender - FY2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2W",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-08-15T04:00:00Z/2014-08-15T04:00:00Z",
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
+            "description": "<p>Accelerating Access to Care Initiative Pending Appointments- Report 2014 August 28</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140828_pending.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "August 28, 2014"
+                }
             ],
+            "identifier": "VA-VHA-OIA-063",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -80570,70 +80582,42 @@
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
-            "identifier": "VA-VHA-OIA-063",
-            "description": "<p>Accelerating Access to Care Initiative Pending Appointments- Report 2014 August 28</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments- Report 2014 August 28",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140828_pending.pdf",
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
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2014-08-15T04:00:00Z/2014-08-15T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments- Report 2014 August 28"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/v3hi-h8y3",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-09-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-08-12",
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
-            "identifier": "https://www.data.va.gov/api/views/v3hi-h8y3",
             "description": "Count of women who served, including casualty counts, sorted by the wartime period in which they served",
-            "title": "Number of Women Who Served and Casualty Counts by Wartime Period, 1898 to 2015",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80641,58 +80625,56 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v3hi-h8y3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v3hi-h8y3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v3hi-h8y3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/v3hi-h8y3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v3hi-h8y3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v3hi-h8y3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v3hi-h8y3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v3hi-h8y3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v3hi-h8y3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/v3hi-h8y3",
+            "issued": "2019-09-19",
+            "keyword": [
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/v3hi-h8y3",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-08-12",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Number of Women Who Served and Casualty Counts by Wartime Period, 1898 to 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/v657-ycmh",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "1871",
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
-            "identifier": "VA-OEI-OEI-139",
             "description": "<p>VA Historical Annual Reports detail services provided by the Department for each Fiscal Year, including Benefits, Healthcare, and Burial/Memorial services.  The Reports also describe the topics of administration and management within VA, ranging from data on personnel to information on construction projects.  Statistical tables for a variety of subjects are also included.</p>",
-            "title": "Annual Report:  1871",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80701,42 +80683,44 @@
                     "title": "Annual Report:  1871"
                 }
             ],
+            "identifier": "VA-OEI-OEI-139",
+            "issued": "2017-07-26",
+            "keyword": [
+                "1871",
+                "annual report",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/v657-ycmh",
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
+            "title": "Annual Report:  1871"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/v6tv-sgr7",
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
-            "identifier": "https://www.data.va.gov/api/views/v6tv-sgr7",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to help servicepersons adjust to civilian life after separation from military service, assist in the recruitment and retention of highly qualified personnel in the active and reserve components in the Armed Forces by providing education benefits, and to provide educational opportunities to the dependents of certain service members and veterans. Individuals who entered active duty after September 10, 2001 may be eligible for the Post-9/11 GI Bill. Individuals can use the Post-9/11 GI Bill after serving 90 days on active duty (excluding entry level and skill training). Only periods of active duty under title 10 will be used to establish eligibility for the Post 9/11 GI Bill. A high school diploma or equivalency certificate is always required for eligibility. Individuals who are eligible for the Montgomery GI Bill \u2013 Active Duty (chapter 30), the Montgomery GI Bill \u2013 Selected Reserve (chapter 1606), or the Reserve Educational Assistance Program (REAP) will have to make an irrevocable election to relinquish eligibility under one of those benefit programs to establish eligibility under the Post-9/11 GI Bill. The dependent children of a person who died in the line of duty while serving as a member of the Armed Forces may be eligible to use benefits under the Fry Scholarship provision of the Post-9/11 GI Bill. The spouse and/or child(ren) of a veteran or service member may be eligible for the Post 9/11 GI Bill if the veteran or service member transfers entitlement to those dependents. Eligibility to transfer entitlement to dependents is determined by the Department of Defense. This is not a complete list of eligibility requirements. For more information on the latest changes to the Post-9/11 GI Bill go to the VA web-site.</p>",
-            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE NOV2018",
-            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80744,44 +80728,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v6tv-sgr7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v6tv-sgr7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v6tv-sgr7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/v6tv-sgr7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v6tv-sgr7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v6tv-sgr7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v6tv-sgr7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v6tv-sgr7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v6tv-sgr7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/v6tv-sgr7",
+            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 028"
+            ],
+            "landingPage": "https://www.data.va.gov/d/v6tv-sgr7",
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
+            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE NOV2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/v6x8-u8e3",
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
+            "description": "<p>Patient appointment information is obtained from the Veterans Health Information Systems and Technology Architecture Scheduling module.  The Patient Appointment Information application gathers appointment data to be loaded into a national database for statistical reporting. Patient appointments are scanned from September 1, 2002 to the present, and appointment data meeting specified criteria are transmitted to the Austin Information Technology Center Patient Appointment Information Transmission (PAIT) national database.  Subsequent transmissions (bi-monthly) update PAIT bi-monthly via Health Level Seven message transmissions through Vitria Interface Engine (VIE) connections. A Statistical Analysis Software (SAS) program in Austin utilizes PAIT data to create a bi-monthly SAS dataset on the Austin mainframe.  This additional data is used to supplement the existing Clinic Appointment Wait Time and Clinic Utilization extracts created by the Veterans Health Administration Support Service Center (VSSC).</p>",
+            "identifier": "VA-VHA-OIA-051",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "appointment",
                 "clinic",
@@ -80793,61 +80796,42 @@
                 "veteran",
                 "wait"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/v6x8-u8e3",
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
-            "identifier": "VA-VHA-OIA-051",
-            "description": "<p>Patient appointment information is obtained from the Veterans Health Information Systems and Technology Architecture Scheduling module.  The Patient Appointment Information application gathers appointment data to be loaded into a national database for statistical reporting. Patient appointments are scanned from September 1, 2002 to the present, and appointment data meeting specified criteria are transmitted to the Austin Information Technology Center Patient Appointment Information Transmission (PAIT) national database.  Subsequent transmissions (bi-monthly) update PAIT bi-monthly via Health Level Seven message transmissions through Vitria Interface Engine (VIE) connections. A Statistical Analysis Software (SAS) program in Austin utilizes PAIT data to create a bi-monthly SAS dataset on the Austin mainframe.  This additional data is used to supplement the existing Clinic Appointment Wait Time and Clinic Utilization extracts created by the Veterans Health Administration Support Service Center (VSSC).</p>",
-            "title": "VHA Support Service Center Patient Appointment",
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
+            "title": "VHA Support Service Center Patient Appointment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/v7et-tw39",
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
-            "identifier": "https://www.data.va.gov/api/views/v7et-tw39",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE MAR2019",
-            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80855,64 +80839,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v7et-tw39/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v7et-tw39/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v7et-tw39/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/v7et-tw39/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v7et-tw39/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v7et-tw39/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v7et-tw39/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v7et-tw39/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v7et-tw39/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/v7et-tw39",
+            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 120"
+            ],
+            "landingPage": "https://www.data.va.gov/d/v7et-tw39",
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
+            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_Cnty_11-13-09_GDX.csv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_Cnty_11-13-09_GDX.csv"
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
-            "identifier": "VA-VBA-INS2009-002",
+            "dataQuality": true,
             "description": "<p>2009 Veteran life insurance expenditures by county.  Expenditures represented the actual disbursements from Insurance's Award and Inforce systems.</p>",
-            "title": "2009 Veterans' Insurance Expenditure by County",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80920,97 +80899,99 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v8tu-sa79/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v8tu-sa79/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v8tu-sa79/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/v8tu-sa79/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v8tu-sa79/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v8tu-sa79/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/v8tu-sa79/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/v8tu-sa79/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/v8tu-sa79/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2009-002",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "insurance",
+                "veteran"
+            ],
+            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_Cnty_11-13-09_GDX.csv",
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
+                "https://www1.va.gov/VETDATA/docs/Datagov/FY09_insurance_Cnty_11-13-09_GDX.csv"
+            ],
+            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2009 Veterans' Insurance Expenditure by County"
         },
         {
-            "accessLevel": "public",
-            "bureauCode": [
-                "029:00"
-            ],
-            "landingPage": "https://www.data.va.gov/d/v92f-7dq3",
-            "issued": "2021-08-26",
             "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "idaho",
-                "veterans"
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/v92f-7dq3",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Idaho",
+            "identifier": "https://www.data.va.gov/api/views/v92f-7dq3",
+            "issued": "2021-08-26",
+            "keyword": [
+                "idaho",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/v92f-7dq3",
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
+            "title": "State Summaries_Idaho"
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
-            "identifier": "VA-OEI-OEI-152",
             "description": "<p>This table provides a summary of Veteran and Non-Veteran interments by type of interment for fiscal years 2000 through 2014.</p>",
-            "title": "National Cemetery Administration Summary of Veteran and Non-Veteran Interments: FY2000 to FY2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81019,40 +81000,41 @@
                     "title": "National Cemetery Administration Summary of Veteran and Non-Veteran Interments: FY2000 to FY2014"
                 }
             ],
+            "identifier": "VA-OEI-OEI-152",
+            "issued": "2017-07-26",
+            "keyword": [
+                "interments",
+                "nca",
+                "va",
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
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "National Cemetery Administration Summary of Veteran and Non-Veteran Interments: FY2000 to FY2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/v9d3-795t",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "process",
-                "propath",
-                "raci"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Claude T. Shehane",
                 "hasEmail": "mailto:claude.shehane2@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-WSG-002",
             "description": "<p>Displays the process' RACI in its conventional RACI format/chart</p>",
-            "title": "ProPath Display RACI API",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81061,66 +81043,66 @@
                     "title": "API"
                 }
             ],
+            "identifier": "VA-OIT-WSG-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "process",
+                "propath",
+                "raci"
+            ],
+            "landingPage": "https://www.data.va.gov/d/v9d3-795t",
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
+            "title": "ProPath Display RACI API"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/v9rk-5gjz",
-            "issued": "2023-08-10",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-18",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary South Dakota FY2021",
+            "identifier": "https://www.data.va.gov/api/views/v9rk-5gjz",
+            "issued": "2023-08-10",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "south dakota"
             ],
-            "identifier": "https://www.data.va.gov/api/views/v9rk-5gjz",
+            "landingPage": "https://www.data.va.gov/d/v9rk-5gjz",
+            "modified": "2024-06-18",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary South Dakota FY2021",
             "title": "NCVAS State Summary South Dakota FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/v9tv-dnqp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-01-01T05:00:00Z/2015-01-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-121",
             "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT JAN 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81128,40 +81110,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-121",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cars",
+                "establishments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/v9tv-dnqp",
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
+            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT JAN 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/va2s-5jfc",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "guam"
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
-            "identifier": "VA-OEI-OEI-180",
             "description": "<p>This summary describes the programs and services VA provided in Guam in fiscal year 2015.</p>",
-            "title": "State Summary: Guam",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81169,42 +81153,40 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-180",
+            "issued": "2017-07-26",
+            "keyword": [
+                "guam"
+            ],
+            "landingPage": "https://www.data.va.gov/d/va2s-5jfc",
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
+            "title": "State Summary: Guam"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/va4a-ptj8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-05",
-            "keyword": [
-                "utilization",
-                "veterans",
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
-            "identifier": "https://www.data.va.gov/api/views/va4a-ptj8",
             "description": "Percent of Veterans that use VA benefits by program and gender in FY 2023",
-            "title": "Percent of Veterans who Use VA Benefits by Program and Gender, FY2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81212,57 +81194,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/va4a-ptj8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/va4a-ptj8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/va4a-ptj8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/va4a-ptj8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/va4a-ptj8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/va4a-ptj8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/va4a-ptj8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/va4a-ptj8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/va4a-ptj8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/va4a-ptj8",
+            "issued": "2024-07-19",
+            "keyword": [
+                "utilization",
+                "veterans",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/va4a-ptj8",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Percent of Veterans who Use VA Benefits by Program and Gender, FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/va4p-g3aa",
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
-            "identifier": "https://www.data.va.gov/api/views/va4p-g3aa",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAMS to provide, through purchase and/or fabrication, prosthetic and related appliances, equipment and services to eligible veterans so that they may live and work as productive citizens. Veterans eligible for prosthetic services are service-connected veterans seeking care for a service-connected disability; veterans with compensable service-connected disabilities generally rated 10 percent or more; former prisoners of war, veterans discharged or released from active military service for a disability that was incurred or aggravated in the line of duty, and veterans who are in receipt of Section 1151 benefits; veterans who are in receipt of increased pension based on a need of regular aid and attendance or by reason of being permanently housebound; veterans who have annual income and net worth below the \"means test\" threshold; all other veterans who are not required to pay a copayment for their care, i.e., veterans of the Mexican border period and World War I, compensated zero (0) percent service-connected veterans who are receiving statutory awards, veterans exposed to a toxic substance, radiation or environmental hazard (limited to certain disabilities); and veterans who must pay a copayment for their care. Ineligible veterans are nonservice-connected veterans residing or sojourning in foreign lands.</p>",
-            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES FEB2019",
-            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81270,43 +81254,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/va4p-g3aa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/va4p-g3aa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/va4p-g3aa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/va4p-g3aa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/va4p-g3aa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/va4p-g3aa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/va4p-g3aa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/va4p-g3aa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/va4p-g3aa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/va4p-g3aa",
+            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 116"
+            ],
+            "landingPage": "https://www.data.va.gov/d/va4p-g3aa",
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
+            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES FEB2019"
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
-            "temporal": "2014-07-15T04:00:00Z/2014-07-15T04:00:00Z",
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
+            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140731.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "July 31, 2014"
+                }
             ],
+            "identifier": "VA-VHA-OIA-060",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -81320,69 +81332,43 @@
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
-            "identifier": "VA-VHA-OIA-060",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.</p>",
-            "title": "Accelerating Access to Care Initiative - Report 2014 July 31",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140731.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "July 31, 2014"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2014-07-15T04:00:00Z/2014-07-15T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative - Report 2014 July 31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vaqy-ed4f",
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
-            "title": "Equitable Relief Reports 2005",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81390,91 +81376,83 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vaqy-ed4f",
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
+            "title": "Equitable Relief Reports 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://cfm.vaco.va.gov/cfmis/uiProjectSearch.aspx",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Non-Public access level is warranted because of the contract and financial data aggreated in the system.  Knowledge of this information could possibly compromise contract negoiations for construction services.",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2009-01-01T05:00:00Z/2014-05-01T04:00:00Z",
-            "modified": "2024-08-26",
-            "keyword": [
-                "financial construction management",
-                "project management"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Anthony Horty",
                 "hasEmail": "mailto:Anthony.Horty@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-CFM-CFMIS-004",
+            "dataQuality": true,
             "description": "<p>The Construction and Facilities Management Information System (CFMIS) is a program for project management and quality control of construction projects.  The information supplied to this application originates from the Paragon/Tririga applications and contains information from the eCMS and FMS applications.  Due to the nature of the contract and financial management system information, the systems access is restricted to CFM personnel and select contractors working for CFM. CFMIS is a web based system hosted within the VA intranet.  CFMIS will most likely be deactivated in 2014 as the Tririga Application will contain all necessary functions.</p>",
-            "title": "Construction and Facilities Management Information System (CFMIS)",
+            "identifier": "VA-CFM-CFMIS-004",
+            "issued": "2017-07-26",
+            "keyword": [
+                "financial construction management",
+                "project management"
+            ],
+            "landingPage": "https://cfm.vaco.va.gov/cfmis/uiProjectSearch.aspx",
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
-            "accrualPeriodicity": "R/P1W",
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
+            "title": "Construction and Facilities Management Information System (CFMIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vatu-cx2c",
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
-            "identifier": "https://www.data.va.gov/api/views/vatu-cx2c",
             "description": "Percentage of Service-Connected Disabled Who Did and Did Not Use Health Care, by Disability Rating, FY 2021. Data underlying the third figure of Part 3 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Percentage of Service-Connected Disabled Who Did and Did Not Use Health Care, by Disability Rating, FY2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81482,57 +81460,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vatu-cx2c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vatu-cx2c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vatu-cx2c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vatu-cx2c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vatu-cx2c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vatu-cx2c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vatu-cx2c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vatu-cx2c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vatu-cx2c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/vatu-cx2c",
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
+            "landingPage": "https://www.data.va.gov/d/vatu-cx2c",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Percentage of Service-Connected Disabled Who Did and Did Not Use Health Care, by Disability Rating, FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vb6z-z5xy",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-11-01T04:00:00Z/2014-11-30T05:00:00Z",
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
-            "identifier": "VA-OM-OM-105",
             "description": "<p>Aged accounts receivable report</p>",
-            "title": "COIN 0017 CARS AGE PROFILE REPORT Nov 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81540,41 +81523,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-105",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vb6z-z5xy",
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
+            "title": "COIN 0017 CARS AGE PROFILE REPORT Nov 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vb8c-nibk",
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
-            "identifier": "https://www.data.va.gov/api/views/vb8c-nibk",
-            "description": "<p>VBA EDUCATION BENEFITS PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE OCT2018",
-            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
-            "programCode": [
-                "029:003"
-            ],
+            "dataQuality": true,
+            "description": "<p>VBA EDUCATION BENEFITS PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81582,61 +81566,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vb8c-nibk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vb8c-nibk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vb8c-nibk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vb8c-nibk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vb8c-nibk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vb8c-nibk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vb8c-nibk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vb8c-nibk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vb8c-nibk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/vb8c-nibk",
+            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 120"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vb8c-nibk",
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
+            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE OCT2018"
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
-            "temporal": "2008-01-01T05:00:00Z/2008-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "accountability",
-                "hightlights",
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
-            "identifier": "VA-OM-OM-010",
+            "dataQuality": true,
             "description": "<p>2008 VA Performance and Accountability Report Highlights.</p>",
-            "title": "2008 VA Performance and Accountability Report Highlights",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81645,43 +81627,45 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-010",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accountability",
+                "hightlights",
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
+            "temporal": "2008-01-01T05:00:00Z/2008-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2008 VA Performance and Accountability Report Highlights"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vc59-pe9d",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "hawaii"
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
-            "identifier": "VA-OEI-OEI-181",
             "description": "<p>This summary describes the programs and services VA provided in Hawaii in fiscal year 2015.</p>",
-            "title": "State Summary: Hawaii",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81690,83 +81674,80 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-181",
+            "issued": "2017-07-26",
+            "keyword": [
+                "hawaii"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vc59-pe9d",
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
+            "title": "State Summary: Hawaii"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vcec-bu3r",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dr. Marco Zenati",
+                "hasEmail": "mailto:MRCAS@va.gov"
+            },
+            "dataQuality": true,
+            "description": "Compendium of 40 surgery records containing ECG, SLM and annotations collected for OR team members over the course of a procedure.",
+            "identifier": "https://www.data.va.gov/api/views/vcec-bu3r",
             "issued": "2023-12-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-12",
             "keyword": [
                 "ecg",
                 "electrocardiogram",
                 "surgery"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dr. Marco Zenati",
-                "hasEmail": "mailto:MRCAS@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/vcec-bu3r",
+            "language": [
+                "English"
+            ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2023-12-12",
+            "programCode": [
+                "029:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/vcec-bu3r",
-            "description": "Compendium of 40 surgery records containing ECG, SLM and annotations collected for OR team members over the course of a procedure.",
-            "title": "MRCAS Heart Surgery Performance Data",
-            "programCode": [
-                "029:048"
-            ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
             "theme": [
                 "Surgical Improvements"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "MRCAS Heart Surgery Performance Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vcgs-isai",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-03-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
-            "keyword": [
-                "2013",
-                "insurance",
-                "life insurance policies",
-                "vgli",
-                "vgli 2013"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dorothy Glasgow",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/vcgs-isai",
+            "dataQuality": true,
             "description": "This report provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state as of January 31, 2013, February 28, 2013, and November 30, 2013.  This report also provides the VGLI coverage amount by state as of January 31, 2013 and November 30, 2013.",
-            "title": "Number of Veterans Insured by VGLI by State 2013-11-30",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81774,66 +81755,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vcgs-isai/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vcgs-isai/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vcgs-isai/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vcgs-isai/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vcgs-isai/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vcgs-isai/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vcgs-isai/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vcgs-isai/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vcgs-isai/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/vcgs-isai",
+            "issued": "2021-03-09",
+            "keyword": [
+                "2013",
+                "insurance",
+                "life insurance policies",
+                "vgli",
+                "vgli 2013"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vcgs-isai",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-25",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Number of Veterans Insured by VGLI by State 2013-11-30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vcsm-9zxa",
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
-            "identifier": "https://www.data.va.gov/api/views/vcsm-9zxa",
             "description": "Percent Users vs Non-Users Distribution by Era of Service - Males. Data underlying the fourth figure of Part 2 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Percentage Era Distribution of Male Users and Non-Users, FY 2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81841,40 +81819,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vcsm-9zxa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vcsm-9zxa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vcsm-9zxa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vcsm-9zxa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vcsm-9zxa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vcsm-9zxa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vcsm-9zxa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vcsm-9zxa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vcsm-9zxa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/vcsm-9zxa",
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
+            "landingPage": "https://www.data.va.gov/d/vcsm-9zxa",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Percentage Era Distribution of Male Users and Non-Users, FY 2021"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vcsz-q2jk",
-            "issued": "2022-12-14",
             "@type": "dcat:Dataset",
-            "modified": "2023-01-12",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
+            "description": "Part 3 of a three-part study on Veterans who have used at least one of 22 benefits or services (referred to as \"users\") provided by VA during Fiscal Years 2010 through 2021. Part 3 presents more detailed information on the two largest VA programs, Health Care and Disability Compensation.",
+            "identifier": "https://www.data.va.gov/api/views/vcsz-q2jk",
+            "issued": "2022-12-14",
             "keyword": [
                 "utilization",
                 "veteran benefits",
@@ -81884,43 +81883,27 @@
                 "\u00a0va programs",
                 "\u00a0va services"
             ],
-            "identifier": "https://www.data.va.gov/api/views/vcsz-q2jk",
+            "landingPage": "https://www.data.va.gov/d/vcsz-q2jk",
+            "modified": "2023-01-12",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Part 3 of a three-part study on Veterans who have used at least one of 22 benefits or services (referred to as \"users\") provided by VA during Fiscal Years 2010 through 2021. Part 3 presents more detailed information on the two largest VA programs, Health Care and Disability Compensation.",
             "title": "Use of VA Benefits and Services: 2021 (Part 3)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/vdep-pqu3",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "contact",
-                "ecis"
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
-            "identifier": "VA-ORCH-9",
+            "dataQuality": true,
             "description": "<p>The service is the authoritative service for a veteran's contact information (postal address, phone, email) for a variety of purposes.</p>",
-            "title": "Enterprise Contact Information Service (eCIS)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81929,42 +81912,44 @@
                     "title": "Enterprise Contact Information Service (eCIS)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-9",
+            "issued": "2017-11-17",
+            "keyword": [
+                "contact",
+                "ecis"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vdep-pqu3",
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
+            "title": "Enterprise Contact Information Service (eCIS)"
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
-            "temporal": "2001-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "health administration characteristics",
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
-            "identifier": "VA-OEI-OEI-047",
-            "description": "<p>This table shows a brief summary of enrollees, outpatient visits, and inpatient admissions.</p>",
-            "title": "Selected Veterans Health Administration Characteristics: FY2002-FY2013",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/Utilization/VHAStats.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This table shows a brief summary of enrollees, outpatient visits, and inpatient admissions.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81973,41 +81958,43 @@
                     "title": "xls"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/Utilization/VHAStats.xlsx",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-047",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health administration characteristics",
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
+            "temporal": "2001-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Veterans Administration Characteristics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Selected Veterans Health Administration Characteristics: FY2002-FY2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ve97-jdsp",
-            "issued": "2024-04-24",
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
-            "identifier": "https://www.data.va.gov/api/views/ve97-jdsp",
             "description": "",
-            "title": "Population Demographics ETL",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82015,57 +82002,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ve97-jdsp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ve97-jdsp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ve97-jdsp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ve97-jdsp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ve97-jdsp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ve97-jdsp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ve97-jdsp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ve97-jdsp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ve97-jdsp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ve97-jdsp",
+            "issued": "2024-04-24",
+            "landingPage": "https://www.data.va.gov/d/ve97-jdsp",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Population Demographics ETL"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/veaj-fmv9",
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
                 "hasEmail": "mailto:ogclawlibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-011",
             "description": "<p>Compensation of Fee-Basis Employees</p>",
-            "title": "OGC Precedent Opinion 1-2015",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82074,48 +82057,44 @@
                     "title": "OGC Precedent Opinion 1-2015"
                 }
             ],
+            "identifier": "VA-OGC-011",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/veaj-fmv9",
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
+            "title": "OGC Precedent Opinion 1-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/",
             "bureauCode": [
                 "029:00"
             ],
-            "rights": "Public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2009-10-16T04:00:00Z/2010-03-19T04:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "active duty",
-                "family members",
-                "national guard",
-                "reserve",
-                "surviviors",
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
-            "identifier": "VA-OEI-OEI-017",
-            "description": "<p>This report uses data from the 2010 National Survey of Veterans, Active Duty Service Members, Activated National Guards and Reserve Members, Family Members and Survivors (NSV) to compare the awareness and knowledge of VA services and benefits among Veterans' groups. It also explores the differences in levels of awareness between male Veterans and female Veterans.</p>",
-            "title": "National Survey of Veterans",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/SurveysAndStudies/NVSSurveyFinalWeightedReport.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This report uses data from the 2010 National Survey of Veterans, Active Duty Service Members, Activated National Guards and Reserve Members, Family Members and Survivors (NSV) to compare the awareness and knowledge of VA services and benefits among Veterans' groups. It also explores the differences in levels of awareness between male Veterans and female Veterans.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82124,50 +82103,49 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/SurveysAndStudies/NVSSurveyFinalWeightedReport.pdf",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-017",
+            "issued": "2017-07-26",
+            "keyword": [
+                "active duty",
+                "family members",
+                "national guard",
+                "reserve",
+                "surviviors",
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
+            "rights": "Public",
+            "temporal": "2009-10-16T04:00:00Z/2010-03-19T04:00:00Z",
             "theme": [
                 "Veteran Survey Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Survey of Veterans"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Enrollment_by_State_as_of_103112.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2012-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Number_of_Veterans_Enrolled_in_VGLI_by_State2.doc"
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
-            "identifier": "VA-VBA-INS2012-013",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of October 31, 2012.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "Number of Veterans Insured by VGLI by State as of October 31, 2012",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82175,70 +82153,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vejz-hdzu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vejz-hdzu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vejz-hdzu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vejz-hdzu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vejz-hdzu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vejz-hdzu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vejz-hdzu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vejz-hdzu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vejz-hdzu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-013",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Enrollment_by_State_as_of_103112.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Number_of_Veterans_Enrolled_in_VGLI_by_State2.doc"
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
+            "title": "Number of Veterans Insured by VGLI by State as of October 31, 2012"
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
-                "fy2012",
-                "montana 2012 vba benefits",
-                "state benefit summary",
-                "vba benfit summary"
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
-            "identifier": "VA-VBA-ABR2012-104",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Montana-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82246,49 +82227,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-104",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012",
+                "montana 2012 vba benefits",
+                "state benefit summary",
+                "vba benfit summary"
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
+            "title": "Montana-FY12 Benefits Summary"
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
-            "identifier": "VA-VBA-ABR2012-019",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report( ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the benefitciaries</p>",
-            "title": "Most Prevalent Service Connected Disabilities",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82296,46 +82276,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-019",
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
+            "title": "Most Prevalent Service Connected Disabilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vggh-gqm3",
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
-            "identifier": "https://www.data.va.gov/api/views/vggh-gqm3",
             "description": "VetPop2023 projection of living Veterans by gender, age group (<65 and 65+), and congressional district at the state level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 118th Congressional Districts, 10L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82343,59 +82324,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vggh-gqm3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vggh-gqm3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vggh-gqm3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vggh-gqm3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vggh-gqm3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vggh-gqm3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vggh-gqm3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vggh-gqm3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vggh-gqm3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/vggh-gqm3",
+            "issued": "2024-09-09",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vggh-gqm3",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 118th Congressional Districts, 10L"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vgm9-a2if",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-11-18",
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
-            "identifier": "https://www.data.va.gov/api/views/vgm9-a2if",
             "description": "Percent Users vs Non-Users Distribution by Era - Females. Data underlying the fifth figure of Part 2 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 13, Percent Users vs Non-Users Distribution by Era - Females",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82403,56 +82384,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vgm9-a2if/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vgm9-a2if/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vgm9-a2if/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vgm9-a2if/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vgm9-a2if/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vgm9-a2if/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vgm9-a2if/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vgm9-a2if/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vgm9-a2if/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/vgm9-a2if",
+            "issued": "2020-11-18",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vgm9-a2if",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-12-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 13, Percent Users vs Non-Users Distribution by Era - Females"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vgsw-mfi7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "michigan"
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
-            "identifier": "VA-OEI-OEI-192",
             "description": "<p>This summary describes the programs and services VA provided in Michigan in fiscal year 2015.</p>",
-            "title": "State Summary: Michigan",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82461,47 +82445,42 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-192",
+            "issued": "2017-07-26",
+            "keyword": [
+                "michigan"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vgsw-mfi7",
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
+            "title": "State Summary: Michigan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Veterans_enrolled_in_VGLI_by_state_as_of_10_31_10.xls",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2010-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Insurance_Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State.doc"
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
-            "identifier": "VA-VBA-INS2010-004",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of October 31, 2010.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "Number of Veterans Insured by VGLI by State as of October 31, 2010",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82509,51 +82488,52 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2010-004",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Veterans_enrolled_in_VGLI_by_state_as_of_10_31_10.xls",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Insurance_Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State.doc"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2010-10-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Veterans Insured by VGLI by State as of October 31, 2010"
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
-            "identifier": "VA-VBA-ABR2012-114",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Oklahoma-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82561,44 +82541,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-114",
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
+            "title": "Oklahoma-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vhan-a9vn",
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
-            "identifier": "https://www.data.va.gov/api/views/vhan-a9vn",
+            "dataQuality": true,
             "description": "<p>VBA COMPENSTATION BENEFITS PRGOGRAM to provide vocational training and rehabilitation to certain children born with spina bifida or other covered birth defects who are children of Vietnam veterans and some Korean veterans. \u201cA child born with spina bifida or other covered birth defects, except spina bifida occulta, who is the natural child of a Vietnam veteran and some Korean veterans, regardless of the age or marital status of the child, conceived after the date on which the veteran first served in the Republic of Vietnam during the Vietnam era and in particular areas near the DMZ in the Korean conflict. VA must also determine that it is feasible for the child to achieve a vocational goal.\u201d</p>",
-            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA DEC2018",
-            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82606,63 +82590,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vhan-a9vn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vhan-a9vn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vhan-a9vn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vhan-a9vn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vhan-a9vn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vhan-a9vn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vhan-a9vn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vhan-a9vn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vhan-a9vn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/vhan-a9vn",
+            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 127"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vhan-a9vn",
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
+            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA DEC2018"
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
-            "temporal": "2005-01-01T05:00:00Z/2005-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-014",
+            "dataQuality": true,
             "description": "<p>2005 VA Performance and Accountability Report.</p>",
-            "title": "2005 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82671,45 +82654,44 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-014",
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
+            "temporal": "2005-01-01T05:00:00Z/2005-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2005 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vir3-awzy",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-07-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "health care",
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
-            "identifier": "VA-OEI-OEI-084",
             "description": "<p>This summarizes VA benefits and health care utilization.</p>",
-            "title": "Pocket Card, as of 8/10/15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82718,89 +82700,89 @@
                     "title": "Pocket Card, as of 8/10/15"
                 }
             ],
+            "identifier": "VA-OEI-OEI-084",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health care",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vir3-awzy",
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
+            "temporal": "2014-10-01T04:00:00Z/2015-07-01T04:00:00Z",
             "theme": [
                 "Use of Benefits and Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pocket Card, as of 8/10/15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vixt-w8ax",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "rhode island",
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
-            "identifier": "VA-OEI-OEI-126",
             "description": "<p>This is a summary of the programs and services provided by VA in Rhode Island in fiscal year 2014.</p>",
-            "title": "State Summary:  Rhode Island",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/vetdata/docs/SpecialReports/State_Summaries_Rhode_Island.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "State Summary:  Rhode Island"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-126",
+            "issued": "2017-07-26",
+            "keyword": [
+                "rhode island",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vixt-w8ax",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
             "programCode": [
                 "029:086"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/SpecialReports/State_Summaries_Rhode_Island.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "State Summary:  Rhode Island"
-                }
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
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
+            "title": "State Summary:  Rhode Island"
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
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-150",
             "description": "<p>This reports the activities of the Veterans Administration for the fiscal year ending September 30, 1987.</p>",
-            "title": "Annual Report:  1987",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82809,24 +82791,55 @@
                     "title": "Annual Report:  1987"
                 }
             ],
+            "identifier": "VA-OEI-OEI-150",
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
+            "title": "Annual Report:  1987"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vkt7-i9a6",
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
+                    "downloadURL": "https://www.data.va.gov/download/vkt7-i9a6/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/vkt7-i9a6",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2020-08-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2018-10-01/2019-09-30",
-            "modified": "2021-06-24",
             "keyword": [
                 "2019",
                 "analytics",
@@ -82847,68 +82860,39 @@
                 "veterans health administration",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Sail Operations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/vkt7-i9a6",
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
-            "identifier": "https://www.data.va.gov/api/views/vkt7-i9a6",
-            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
-            "title": "SAIL FY2019 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/vkt7-i9a6/application/zip",
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
+            "title": "SAIL FY2019 Hospital Performance - All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vku6-87ur",
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
-            "identifier": "e24594a9-35d6-4d90-a00d-f5222758bb34",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Wyoming FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82916,43 +82900,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "e24594a9-35d6-4d90-a00d-f5222758bb34",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vku6-87ur",
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
+            "title": "State Summary Wyoming FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vmme-krmq",
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
-            "identifier": "https://www.data.va.gov/api/views/vmme-krmq",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to encourage membership in units of the Selected Reserve of the Ready Reserve and to provide educational assistance to members of the reserve components called or ordered to active service in response to a war or national emergency declared by the President or Congress. Generally, to qualify for benefits under MGIB-SR you must (1) Have a six-year obligation to serve in the Selected Reserve signed after June 30, 1985. If you are an officer, you must have agreed to serve six years in addition to your original obligation. For some types of training, it is necessary to have a six-year commitment that begins after September 30, 1990; (2) Complete your initial active duty for training (IADT); (3) Meet the requirement to receive a high school diploma or equivalency certificate before completing IADT. You may not use 12 hours toward a college degree to meet this requirement; and (4) Remain in good standing while serving in an active Selected Reserve unit. Generally, to qualify for benefits under REAP you must have served at least 90 consecutive days on active duty as a result of a call or order to active duty from a reserve component in response to a war or national emergency declared by the President or Congress. This is not a complete list of eligibility requirements. For more information on MGIB-SR and REAP visit <a href=\"http://www.gibill.va.gov\">http://www.gibill.va.gov</a>.</p>",
-            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM APR2019",
-            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82960,43 +82944,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vmme-krmq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vmme-krmq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vmme-krmq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vmme-krmq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vmme-krmq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vmme-krmq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vmme-krmq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vmme-krmq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vmme-krmq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/vmme-krmq",
+            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 032"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vmme-krmq",
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
+            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.techstrategies.oit.va.gov/docs_design_patterns_soa.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mark Peterson",
+                "hasEmail": "mailto:mark.peterson3@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.techstrategies.oit.va.gov/docs_ctsnotes.asp",
+            "description": "<p>Enterprise design pattern documents that provide references to the use of enterprise capabilities that will enable the VA to access and exchange data securely through the use of Enterprise Shared Services (ESS) and open standards.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.techstrategies.oit.va.gov/docs_design_patterns_soa.asp",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ASD-001-1",
             "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2016-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "apm",
                 "application performance monitoring",
@@ -83012,75 +83026,43 @@
                 "soa",
                 "web technologies"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Mark Peterson",
-                "hasEmail": "mailto:mark.peterson3@va.gov"
-            },
+            "landingPage": "https://www.techstrategies.oit.va.gov/docs_design_patterns_soa.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:078"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OIT-ASD-001-1",
-            "description": "<p>Enterprise design pattern documents that provide references to the use of enterprise capabilities that will enable the VA to access and exchange data securely through the use of Enterprise Shared Services (ESS) and open standards.</p>",
-            "title": "Design Pattern: Service Oriented Architecture (SOA)",
-            "programCode": [
-                "029:078"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.techstrategies.oit.va.gov/docs_design_patterns_soa.asp",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "describedBy": "https://www.techstrategies.oit.va.gov/docs_ctsnotes.asp",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-10-01T04:00:00Z/2016-10-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Design Pattern: Service Oriented Architecture (SOA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vn8v-7r5k",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
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
-            "identifier": "VA-OEI-OEI-008",
-            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
-            "title": "Veterans Affairs Geographic Distribution of Expenditures FY09 by State and County",
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
@@ -83088,66 +83070,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vn8v-7r5k/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vn8v-7r5k/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vn8v-7r5k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vn8v-7r5k/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vn8v-7r5k/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vn8v-7r5k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vn8v-7r5k/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vn8v-7r5k/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vn8v-7r5k/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/VETDATA/docs/Datagov/DataGov_GDX_FY09_Technical_Notes.doc",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-008",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vn8v-7r5k",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/DataGov_GDX_FY09_Technical_Notes.doc"
+            ],
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Affairs Geographic Distribution of Expenditures FY09 by State and County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vne6-2zez",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-08-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-22",
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
-            "identifier": "ba68d338-535a-4d64-a983-eb47f2b572c5",
+            "dataQuality": true,
             "description": "<p>The SCD Veterans are broken out by SCD ratings (0-20 percent; 30-40 percent; 50-60 percent and 70-100 percent) for FY 1986 to FY 2020.</p>\n\nSource: Department of Veterans Affairs, Veterans Benefits Administration; 1985-1998: COIN CP-127 Reports; 1999-2019: Annual Benefits Reports\t\t\t\t\t\n\nPrepared by the National Center for Veterans Analysis and Statistics, Office of Enterprise Integration, Department of Veterans Affairs, May 2021",
-            "title": "Service Connected Disability (SCD) Veterans by Disability Rating Group: FY1986 to FY2020",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83155,37 +83139,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "ba68d338-535a-4d64-a983-eb47f2b572c5",
+            "issued": "2018-08-21",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vne6-2zez",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2021-07-22",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Service Connected Disability (SCD) Veterans by Disability Rating Group: FY1986 to FY2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vnn6-jkib",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "construction",
-                "environmental"
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
-            "identifier": "VA-NCA-CSD-001",
             "description": "<p>This guide provides information on federal environmental requirements for construction projects. It is written primarily for owners of construction projects and for general contractors who supervise construction projects. Subcontractors also may find the information useful.</p>",
-            "title": "Federal Environmental Requirements for Construction",
-            "programCode": [
-                "029:090"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83200,45 +83183,41 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-NCA-CSD-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "construction",
+                "environmental"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vnn6-jkib",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:090"
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
+            "title": "Federal Environmental Requirements for Construction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vnnk-5fd7",
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
-            "identifier": "https://www.data.va.gov/api/views/vnnk-5fd7",
             "description": "The Department of Veterans Affairs provides official estimates and projections of the Veteran population using the Veteran Population Projection Model (VetPop). Based on the latest model VetPop2020 and the most recent national survey estimates from the 2021 American Community Survey 5-Year (ACS) data, the projected number of Veterans living in 50 states, DC and Puerto Rico for the fiscal years, 2021 to 2023, are allocated to Urban and Rural areas. As defined by the Census Bureau, those not residing in Urban areas are assumed to be in Rural areas (https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural/2010-urban-rural.html).\n\nThis table contains the Veteran estimates by urban/rural, gender, and age group.\n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2020 Urban/Rural FY2021-2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83246,64 +83225,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vnnk-5fd7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vnnk-5fd7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vnnk-5fd7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vnnk-5fd7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vnnk-5fd7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vnnk-5fd7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vnnk-5fd7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vnnk-5fd7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vnnk-5fd7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/vnnk-5fd7",
+            "issued": "2023-02-21",
+            "keyword": [
+                "rural",
+                "rural veterans",
+                "urban",
+                "veteran",
+                "veteran population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/vnnk-5fd7",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-06",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 Urban/Rural FY2021-2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_August2012.CSV",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-08-01T04:00:00Z/2012-08-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Face_Amount_by_Program_August_2012.doc"
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
-            "identifier": "VA-VBA-INS2012-001",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 08/31/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Face Amount of Life Insurance Coverage by Program by State 2012/08/31",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83311,49 +83288,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vnut-btzz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vnut-btzz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vnut-btzz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/vnut-btzz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vnut-btzz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vnut-btzz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/vnut-btzz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/vnut-btzz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/vnut-btzz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-001",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_August2012.CSV",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Face_Amount_by_Program_August_2012.doc"
+            ],
+            "temporal": "2012-08-01T04:00:00Z/2012-08-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Face Amount of Life Insurance Coverage by Program by State 2012/08/31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/vnza-ndun",
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
+            "description": "<p>Lockbox First Party provides automated processing of payments made by Veterans who are required to make co-payments for health care services at VA facilities. Veterans receive their bills through the Consolidated Co-payment Processing Center (CCPC) and make payment through Lockbox First Party. Lockbox First Party provides a central collection point for payments through a commercial bank. In addition, Lockbox First Party provides reporting and inquiry capability.</p>",
+            "identifier": "VA-VHA-CBO-005",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1999-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "billing",
                 "co-payment",
@@ -83362,43 +83365,53 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/vnza-ndun",
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
-            "identifier": "VA-VHA-CBO-005",
-            "description": "<p>Lockbox First Party provides automated processing of payments made by Veterans who are required to make co-payments for health care services at VA facilities. Veterans receive their bills through the Consolidated Co-payment Processing Center (CCPC) and make payment through Lockbox First Party. Lockbox First Party provides a central collection point for payments through a commercial bank. In addition, Lockbox First Party provides reporting and inquiry capability.</p>",
-            "title": "Lockbox, First Party",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1999-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Lockbox, First Party"
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
+                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX-F-000-JAN-VP03-FY2003-re.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-029",
             "issued": "2017-07-26",
-            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -83412,79 +83425,81 @@
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
-            "identifier": "VA-OEI-OEI-029",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2003",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX-F-000-JAN-VP03-FY2003-re.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/vp7u-4iv2",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Utah FY2023",
+            "identifier": "https://www.data.va.gov/api/views/vp7u-4iv2",
             "issued": "2024-06-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-15",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "utah"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/vp7u-4iv2",
+            "modified": "2024-07-15",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/vp7u-4iv2",
-            "description": "NCVAS State Summary Utah FY2023",
-            "title": "NCVAS State Summary Utah FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Utah FY2023"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/January_2015_Public_Data_Completed_03192015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 31 Jan 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-098",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-01-31T05:00:00Z/2015-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -83498,71 +83513,40 @@
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
-            "identifier": "VA-VHA-OIA-098",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Jan 31",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/January_2015_Public_Data_Completed_03192015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 31 Jan 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-01-31T05:00:00Z/2015-01-31T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Jan 31"
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
-            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
-            "keyword": [
-                "budget",
-                "fy2014"
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
-            "identifier": "VA-OM-OM-020",
+            "dataQuality": true,
             "description": "<p>FY2014 VA Budget Submission</p>",
-            "title": "FY2014 VA Budget Submission",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83571,46 +83555,43 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-020",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "fy2014"
+            ],
+            "landingPage": "https://www.va.gov/budget/products.asp",
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
+            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY2014 VA Budget Submission"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/vsay-ffng",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "agile",
-                "project management",
-                "veteran-focused integration process",
-                "vip"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shawn Hurford",
                 "hasEmail": "mailto:shawn.hurford@va.vog"
             },
-            "publisher": {
-                "@type": "org:Organization",
```

