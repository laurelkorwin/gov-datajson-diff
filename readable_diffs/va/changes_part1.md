# Change History for va.json

### Changes from 8a4b201 to ad6f778
**Author:** Automated

**Date:** 2025-02-04 17:12:56+00:00

**Message:** Updated data: Tue Feb  4 17:12:56 UTC 2025

```diff
diff --git a/va.json b/va.json
index eb4a4e0..7e84677 100644
--- a/va.json
+++ b/va.json
@@ -51429,11 +51429,11 @@
             "identifier": "https://www.data.va.gov/api/views/ik8k-3hpf",
             "issued": "2024-12-11",
             "keyword": [
+                "community care",
                 "diagnosis",
-                "icd10",
                 "fy24",
+                "icd10",
                 "inpatient",
-                "community care",
                 "outpatient"
             ],
             "landingPage": "https://www.data.va.gov/d/ik8k-3hpf",
```

### Changes from 3054934 to 8a4b201
**Author:** Automated

**Date:** 2025-02-04 15:12:28+00:00

**Message:** Updated data: Tue Feb  4 15:12:28 UTC 2025

```diff
diff --git a/va.json b/va.json
index 566b869..eb4a4e0 100644
--- a/va.json
+++ b/va.json
@@ -84259,11 +84259,11 @@
             "identifier": "https://www.data.va.gov/api/views/vxex-2fsu",
             "issued": "2024-12-05",
             "keyword": [
+                "community care",
                 "diagnosis",
-                "icd10",
                 "fy23",
+                "icd10",
                 "inpatient",
-                "community care",
                 "outpatient"
             ],
             "landingPage": "https://www.data.va.gov/d/vxex-2fsu",
```

### Changes from dd2190f to 3054934
**Author:** Automated

**Date:** 2025-02-04 14:12:12+00:00

**Message:** Updated data: Tue Feb  4 14:12:12 UTC 2025

```diff
diff --git a/va.json b/va.json
index de7655a..566b869 100644
--- a/va.json
+++ b/va.json
@@ -51429,16 +51429,16 @@
             "identifier": "https://www.data.va.gov/api/views/ik8k-3hpf",
             "issued": "2024-12-11",
             "keyword": [
-                "community care",
                 "diagnosis",
-                "fy24",
                 "icd10",
+                "fy24",
                 "inpatient",
+                "community care",
                 "outpatient"
             ],
             "landingPage": "https://www.data.va.gov/d/ik8k-3hpf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "modified": "2024-12-11",
+            "modified": "2025-02-04",
             "programCode": [
                 "029:000"
             ],
@@ -84259,11 +84259,11 @@
             "identifier": "https://www.data.va.gov/api/views/vxex-2fsu",
             "issued": "2024-12-05",
             "keyword": [
-                "community care",
                 "diagnosis",
-                "fy23",
                 "icd10",
+                "fy23",
                 "inpatient",
+                "community care",
                 "outpatient"
             ],
             "landingPage": "https://www.data.va.gov/d/vxex-2fsu",
@@ -84271,7 +84271,7 @@
                 "N/A"
             ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "modified": "2024-12-05",
+            "modified": "2025-02-04",
             "programCode": [
                 "029:000"
             ],
```

### Changes from 31606f9 to dd2190f (Part 1/7)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/va.json b/va.json
index 3728bab..de7655a 100644
--- a/va.json
+++ b/va.json
@@ -3,41 +3,21 @@
     "@id": "https://www.data.va.gov/data.json",
     "@type": "dcat:Catalog",
     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "dataset": [
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
-            "identifier": "VA-VBA-ABR2012-082",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Colorado-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45,44 +25,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-082",
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
+            "title": "Colorado-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/233r-dqvb",
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
-            "identifier": "VA-OGC-045",
             "description": "<p>Claimant Private Relief Legislative Files-VA</p>",
-            "title": "OGC Privacy Act System of Records Notice 06VA026",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91,46 +74,43 @@
                     "title": "OGC Privacy Act System of Records Notice 06VA026"
                 }
             ],
+            "identifier": "VA-OGC-045",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "system of records"
+            ],
+            "landingPage": "https://www.data.va.gov/d/233r-dqvb",
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
+            "title": "OGC Privacy Act System of Records Notice 06VA026"
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
-            "identifier": "VA-VBA-ABR2012-108",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "New Jersey-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139,44 +119,48 @@
                     "title": "New Jersey-FY12 Benefits Summary"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-108",
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
+            "title": "New Jersey-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/23kb-i2b8",
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
-            "identifier": "https://www.data.va.gov/api/views/23kb-i2b8",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist States and federally recognized tribal governments in the establishment, expansion, and improvement of veterans' cemeteries. Monetary assistance is provided under this program to establish, expand, and improve State or Tribal government veterans\u2019 cemeteries. Cemeteries must be State or Tribal Government owned and operated solely for the interment of eligible veterans and their dependents and/or spouses. Construction cost means the amount found necessary to convert a tract of land to an operational cemetery. The cemetery must be used solely for the interment of veterans, their wives, husbands, surviving spouses, minor children, and unmarried adult children who were physically or mentally disabled and incapable of self-support: section 38 CFR Part 38.620.</p>",
-            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM FEB2019",
-            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -184,61 +168,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/23kb-i2b8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/23kb-i2b8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/23kb-i2b8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/23kb-i2b8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/23kb-i2b8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/23kb-i2b8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/23kb-i2b8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/23kb-i2b8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/23kb-i2b8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/23kb-i2b8",
+            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
+            "issued": "2019-03-29",
+            "keyword": [
+                "cfda 64 101"
+            ],
+            "landingPage": "https://www.data.va.gov/d/23kb-i2b8",
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
+            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/24a3-s74n",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
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
-            "identifier": "1b6f6e49-a5d4-470e-9b70-94df01a30fbe",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Oklahoma FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -246,26 +230,45 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "1b6f6e49-a5d4-470e-9b70-94df01a30fbe",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/24a3-s74n",
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
+            "title": "State Summary Oklahoma FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/256r-ggtd",
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
+            "description": "<p>The Plan Library Information and Retrieval System (PLIARS) is an electronic catalogue of microfilmed Contract and As-Built drawings of VA building plans and cemeteries. It is a single flat file list of the more than 500,000 aperture cards stored at the Veterans Affairs Central Office (VACO). Each record contains an entry for Veterans Affairs Medical Center (VAMC) station number, date, building number, a code representing the discipline, project number, floor, and wing. Disciplines include architectural, electrical, mechanical, structural, etc. Hard copy of the plans are stored at each VAMC. The plans are microfilmed at the National Archives and aperture cards are produced for both Contract and As-Built stages of the contract. An original copy of each aperture card is kept at the National Archives, with copies to VACO and the VAMC. The Program Planning and Management Office enters a record into PLIARS for each new card the VACO receives. They are also responsible for maintaining the database. Primary users of the PLIARS database are contractors hired to do work. In-house technical staff and the Engineering offices at the VAMC's. Users of PLIARS can request aperture cards for the buildings, disciplines, projects and medical centers as needed. Staff pull the aperture cards from the files and make either half or full size blow-ups of the drawings.</p>",
+            "identifier": "VA-VHA-OM-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1979-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "architectural",
                 "architecture",
@@ -278,66 +281,76 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/256r-ggtd",
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
-            "identifier": "VA-VHA-OM-001",
-            "description": "<p>The Plan Library Information and Retrieval System (PLIARS) is an electronic catalogue of microfilmed Contract and As-Built drawings of VA building plans and cemeteries. It is a single flat file list of the more than 500,000 aperture cards stored at the Veterans Affairs Central Office (VACO). Each record contains an entry for Veterans Affairs Medical Center (VAMC) station number, date, building number, a code representing the discipline, project number, floor, and wing. Disciplines include architectural, electrical, mechanical, structural, etc. Hard copy of the plans are stored at each VAMC. The plans are microfilmed at the National Archives and aperture cards are produced for both Contract and As-Built stages of the contract. An original copy of each aperture card is kept at the National Archives, with copies to VACO and the VAMC. The Program Planning and Management Office enters a record into PLIARS for each new card the VACO receives. They are also responsible for maintaining the database. Primary users of the PLIARS database are contractors hired to do work. In-house technical staff and the Engineering offices at the VAMC's. Users of PLIARS can request aperture cards for the buildings, disciplines, projects and medical centers as needed. Staff pull the aperture cards from the files and make either half or full size blow-ups of the drawings.</p>",
-            "title": "Plan Library Information and Retrieval System (PLIARS)",
-            "programCode": [
-                "029:041"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1979-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Plan Library Information and Retrieval System (PLIARS)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/26ff-xw8u",
-            "issued": "2023-08-10",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-18",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary South Carolina FY2021",
+            "identifier": "https://www.data.va.gov/api/views/26ff-xw8u",
+            "issued": "2023-08-10",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "south carolina"
             ],
-            "identifier": "https://www.data.va.gov/api/views/26ff-xw8u",
+            "landingPage": "https://www.data.va.gov/d/26ff-xw8u",
+            "modified": "2024-06-18",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary South Carolina FY2021",
             "title": "NCVAS State Summary South Carolina FY2021"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2013.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/VA-FY13-Report.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-01",
             "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2013",
                 "backlog",
@@ -351,69 +364,40 @@
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
-            "identifier": "VA-OIT-ITIS-01",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2013.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2013",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/VA-FY13-Report.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/27bh-jkvk",
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
-            "identifier": "b34ed7aa-807d-432b-ad3f-5ad63b5764ce",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Mississippi FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -421,86 +405,77 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "b34ed7aa-807d-432b-ad3f-5ad63b5764ce",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/27bh-jkvk",
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
+            "title": "State Summary Mississippi FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/28bt-ayg7",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to compensate veterans for disabilities incurred or aggravated during military service according to the average impairment in earning capacity such disability would cause in civilian occupations. Persons who have suffered disabilities resulting from service in the Armed Forces of the United States. The disability must have been incurred or aggravated by service in the line of duty. Separation from service must have been under other than dishonorable conditions for the period in which the disability was incurred or aggravated.</p>",
-            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY FY2019",
+            "identifier": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 109"
+            ],
+            "landingPage": "https://www.data.va.gov/d/28bt-ayg7",
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
+            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_COMP_by_County_2011.doc",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_COMP_by_County_2011.doc"
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
-            "identifier": "VA-VBA-CP2011-001",
+            "dataQuality": true,
             "description": "<p>This data set shows the number of veterans and survivors who are receiving either disability compensation or pension benefits from the Department of Veterans Affairs.</p>",
-            "title": "FY2011 Compensation and Pension by County",
-            "isPartOf": "VA-VBA-MASTER-COMPENSATIONPENSION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -509,26 +484,64 @@
                     "title": "xls"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-CP2011-001",
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
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_COMP_by_County_2011.doc",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_COMP_by_County_2011.doc"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Section 10. National Security and Veterans Affairs"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY2011 Compensation and Pension by County"
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
+                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX99-VETPOP-99-ALL.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-025",
             "issued": "2017-07-26",
-            "temporal": "1998-10-01T04:00:00Z/1999-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -542,98 +555,67 @@
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
-            "identifier": "VA-OEI-OEI-025",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY1999",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX99-VETPOP-99-ALL.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "1998-10-01T04:00:00Z/1999-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/2acs-r85i",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-21",
-            "keyword": [
-                "nevada",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@va.gvo"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/2acs-r85i",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Nevada",
+            "identifier": "https://www.data.va.gov/api/views/2acs-r85i",
+            "issued": "2021-08-26",
+            "keyword": [
+                "nevada",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2acs-r85i",
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
+            "title": "State Summaries_Nevada"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2aez-zviz",
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
-            "identifier": "VA-OEI-OEI-162",
             "description": "<p>This reports shows the services and benefits the Department of Veterans Affairs provided in 1995.</p>",
-            "title": "Annual Report:  1995",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -642,44 +624,43 @@
                     "title": "Annual Report:  1995"
                 }
             ],
+            "identifier": "VA-OEI-OEI-162",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "services",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2aez-zviz",
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
+            "title": "Annual Report:  1995"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/directory/guide/home.asp?isFlash=0",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "building information",
-                "facilities",
-                "location",
-                "va"
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
-            "identifier": "VA-OIT-WSG-01",
             "description": "<p>The facilities web service provides VA facility information. The VA facilities locator is a feature that is available across the enterprise, on any webpage, for the Department of Veterans Affairs. It is comprised of data from across the different facilities, and is updated multiple times a day by multiple personnel. This API gives external users the ability to interact with the most up to date information about VA facilities.</p>",
-            "title": "Facilities & Leadership",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -688,40 +669,43 @@
                     "title": "VA Facilities & Leadership"
                 }
             ],
+            "identifier": "VA-OIT-WSG-01",
+            "issued": "2017-07-26",
+            "keyword": [
+                "building information",
+                "facilities",
+                "location",
+                "va"
+            ],
+            "landingPage": "https://www.va.gov/directory/guide/home.asp?isFlash=0",
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
+            "title": "Facilities & Leadership"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2b2z-s8vt",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "south carolina"
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
-            "identifier": "VA-OEI-OEI-212",
             "description": "<p>This summary describes the programs and services VA provided in South Carolina in fiscal year 2015.</p>",
-            "title": "State Summary: South Carolina FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -730,100 +714,84 @@
                     "title": "South Carolina"
                 }
             ],
+            "identifier": "VA-OEI-OEI-212",
+            "issued": "2017-07-26",
+            "keyword": [
+                "south carolina"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2b2z-s8vt",
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
+            "title": "State Summary: South Carolina FY15"
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
+            "description": "<p>USA Spending- All-Volunteer Force Educational Assistance- Chapter 30- for February 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-038",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING012014-038",
-            "description": "<p>USA Spending- All-Volunteer Force Educational Assistance- Chapter 30- for February 2014</p>",
-            "title": "USA Spending file-02/2014- Education- Chapter 30- CFDA 64.124",
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
+            "title": "USA Spending file-02/2014- Education- Chapter 30- CFDA 64.124"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2bm9-5ve7",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-11-25",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-28",
-            "keyword": [
-                "2021",
-                "ethnicity",
-                "fy2021",
-                "fy 2021",
-                "fy21",
-                "fy 21",
-                "healthcare",
-                "health care",
-                "race",
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
                 "hasEmail": "mailto:\tvancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/2bm9-5ve7",
+            "dataQuality": true,
             "description": "Notes:\n\n\"Total Number of Veterans\" represents FY 2021 projected Veteran counts from VA's Veteran Population Projection Model 2020 (VetPop20). These projections represent living Veterans as of 9/30/2021 and are made with the assumption that Veterans are not missing information (e.g., ethnicity, etc.).\n\n\"Veteran VA Users\" represents historical Veteran VA user counts from VA's United States Veterans Eligibility Trends and Statistics 2021 (USVETS 2021).  These counts represent Veterans who used any VA benefit or service during FY 2021 (includes both living and deceased Veterans as of end of FY 2021).\n\n\"Veteran VA Healthcare Users\" represents historical Veteran VA healthcare user counts from VA's United States Veterans Eligibility Trends and Statistics 2021 (USVETS 2021).  These counts represent Veterans who used VA healthcare during FY 2021 (includes both living and deceased Veterans as of end of FY 2021).\n\n\"Veteran VA Users\" includes Veteran users of VA healthcare or any other VA benefit or service.\n\nSources: USVETS 2021 and VetPop20\nEffective Date: 9/30/2021",
-            "title": "FY 2021 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Ethnicity",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -831,42 +799,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2bm9-5ve7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2bm9-5ve7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2bm9-5ve7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2bm9-5ve7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2bm9-5ve7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2bm9-5ve7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2bm9-5ve7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2bm9-5ve7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2bm9-5ve7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/2bm9-5ve7",
+            "issued": "2022-11-25",
+            "keyword": [
+                "2021",
+                "ethnicity",
+                "fy2021",
+                "fy 2021",
+                "fy21",
+                "fy 21",
+                "healthcare",
+                "health care",
+                "race",
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
+            "landingPage": "https://www.data.va.gov/d/2bm9-5ve7",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2022-11-28",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/2cbx-yjw5",
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
+            "description": "<p>This database is part of the National Medical Information System (NMIS). The National Health Care Practitioner Database (NHCPD) supports Veterans Health Administration Privacy Act requirements by segregating personal information about health care practitioners such as name and social security number from patient information recorded in the National Patient Care Database for Ambulatory Care Reporting and Primary Care Management Module.</p>",
+            "identifier": "VA-VHA-OIA-013",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2001-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "ambulatory",
                 "clinical",
@@ -877,72 +880,45 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/2cbx-yjw5",
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
-            "identifier": "VA-VHA-OIA-013",
-            "description": "<p>This database is part of the National Medical Information System (NMIS). The National Health Care Practitioner Database (NHCPD) supports Veterans Health Administration Privacy Act requirements by segregating personal information about health care practitioners such as name and social security number from patient information recorded in the National Patient Care Database for Ambulatory Care Reporting and Primary Care Management Module.</p>",
-            "title": "National Health Care Practitioner Database (NHCPD)",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2001-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Health Care Practitioner Database (NHCPD)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2cuc-kdvy",
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
-            "identifier": "VA-VHA-OIA-025",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset defines the scope of services provided at a facility.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Availability of Services",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset defines the scope of services provided at a facility.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -950,48 +926,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2cuc-kdvy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2cuc-kdvy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2cuc-kdvy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2cuc-kdvy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2cuc-kdvy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2cuc-kdvy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2cuc-kdvy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2cuc-kdvy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2cuc-kdvy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-025",
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
+            "landingPage": "https://www.data.va.gov/d/2cuc-kdvy",
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
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Availability of Services"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/Nov_2014_Completed_Access_Data_using_Preferred_Date_01082015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Access Data using Preferred Date 2015-01-08"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-069",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2014-11-30T05:00:00Z/2014-11-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -1005,70 +1020,38 @@
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
-            "identifier": "VA-VHA-OIA-069",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Jan 8",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/Nov_2014_Completed_Access_Data_using_Preferred_Date_01082015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Access Data using Preferred Date 2015-01-08"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2014-11-30T05:00:00Z/2014-11-30T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Jan 8"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.techstrategies.oit.va.gov/docs/CTSNotes/TS%20Note%20Vol%202%20Issue%207_07082015_Post-508.pdf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "communications",
-                "it"
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
-            "identifier": "VA-OIT-ASD-TSNV2-7",
             "description": "<p>VA Executive's Guide to Unified Communications</p>",
-            "title": "TS Note Vol 2 Issue 7",
-            "programCode": [
-                "029:078"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1077,26 +1060,55 @@
                     "title": "TS Note Vol 2 Issue 6"
                 }
             ],
+            "identifier": "VA-OIT-ASD-TSNV2-7",
+            "issued": "2017-07-26",
+            "keyword": [
+                "communications",
+                "it"
+            ],
+            "landingPage": "https://www.techstrategies.oit.va.gov/docs/CTSNotes/TS%20Note%20Vol%202%20Issue%207_07082015_Post-508.pdf",
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
+            "title": "TS Note Vol 2 Issue 7"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN9FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 9 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-083",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -1112,72 +1124,43 @@
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
-            "identifier": "VA-VHA-OIA-083",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 9",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN9FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 9 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 9"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/2eq6-fbx3",
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
-            "identifier": "https://www.data.va.gov/api/views/2eq6-fbx3",
+            "dataQuality": true,
             "description": "All Survivors Pension Recipients by Age FY2020.  Surviving spouses and dependent children of deceased wartime Veterans are eligible for monthly pension benefits if they meet the net worth and income requirements.",
-            "title": "All Survivors Pension Recipients by Age FY2020",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1185,41 +1168,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2eq6-fbx3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2eq6-fbx3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2eq6-fbx3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2eq6-fbx3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2eq6-fbx3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2eq6-fbx3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2eq6-fbx3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2eq6-fbx3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2eq6-fbx3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/2eq6-fbx3",
+            "issued": "2022-04-29",
+            "keyword": [
+                "pension",
+                "veterans",
+                "veterans surviving spouses and children"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2eq6-fbx3",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2022-05-04",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "All Survivors Pension Recipients by Age FY2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/2fr5-sktm",
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
+            "description": "<p>The VHA Support Service Center Capital Assets Databases is a web based project application and tracking database. This is used for capital project application submissions and capital project tracking for the Veterans Health Administration (VHA) Minor, Clinical Specific Initiative (CSI) and Non-recurring Maintenance (NRM) Programs. Annually, VHA Facilities enter project applications. Monthly, the VHA facilities update the schedule and cost information for approved projects.</p>",
+            "identifier": "VA-VHA-OIA-049",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2001-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "assets",
                 "capital",
@@ -1230,81 +1233,61 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/2fr5-sktm",
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
-            "identifier": "VA-VHA-OIA-049",
-            "description": "<p>The VHA Support Service Center Capital Assets Databases is a web based project application and tracking database. This is used for capital project application submissions and capital project tracking for the Veterans Health Administration (VHA) Minor, Clinical Specific Initiative (CSI) and Non-recurring Maintenance (NRM) Programs. Annually, VHA Facilities enter project applications. Monthly, the VHA facilities update the schedule and cost information for approved projects.</p>",
-            "title": "VHA Support Service Center Capital Assets (VSSC)",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2001-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VHA Support Service Center Capital Assets (VSSC)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2g8z-bnwf",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "Although all studies in the PTSD Repository are published in English, the research is done in many countries around the world.",
             "identifier": "https://www.data.va.gov/api/views/2g8z-bnwf",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/2g8z-bnwf",
+            "modified": "2024-09-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Although all studies in the PTSD Repository are published in English, the research is done in many countries around the world.",
             "title": "Where in the world are PTSD treatments being studied?"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/2hkn-faaa",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "emr",
-                "healthcare"
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
-            "identifier": "VA-VIA-3",
+            "dataQuality": true,
             "description": "<p>This service provides web services used to obtain clinical data for patients. There are three service methods that allow write functionality signNote, writeNote and writeSimpleOrder all of the other functionality exposed by this service is read only access. The service supports multiple Vista sites data access. Users of this service are intended to be healthcare providers</p>",
-            "title": "Electronic Medical Record Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1313,41 +1296,42 @@
                     "title": "\"Electronic Medical Record Service\""
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VIA-3",
+            "issued": "2017-11-17",
+            "keyword": [
+                "emr",
+                "healthcare"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2hkn-faaa",
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
+            "title": "Electronic Medical Record Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2hnn-8vkt",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-07",
-            "keyword": [
-                "demographics",
-                "gdx",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS mailbox",
                 "hasEmail": "mailto:\tvancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/2hnn-8vkt",
+            "dataQuality": true,
             "description": "The Geographic Distribution of VA Expenditures (GDX) is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.",
-            "title": "GDX FY22",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1355,62 +1339,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2hnn-8vkt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2hnn-8vkt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2hnn-8vkt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2hnn-8vkt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2hnn-8vkt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2hnn-8vkt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2hnn-8vkt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2hnn-8vkt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2hnn-8vkt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/2hnn-8vkt",
+            "issued": "2023-04-24",
+            "keyword": [
+                "demographics",
+                "gdx",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2hnn-8vkt",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-09-07",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "GDX FY22"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2hns-7v4f",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2021-12-14",
-            "temporal": "2020 - 2021",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-17",
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
-            "identifier": "https://www.data.va.gov/api/views/2hns-7v4f",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) data from the 2020 & 2021 AES administrations. Scores are provided at the station level and up, and the occupation level within hospitals.",
-            "title": "All Employee Survey (AES) 2020 - 2021",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1418,44 +1400,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2hns-7v4f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2hns-7v4f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2hns-7v4f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2hns-7v4f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2hns-7v4f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2hns-7v4f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2hns-7v4f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2hns-7v4f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2hns-7v4f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/2hns-7v4f",
+            "issued": "2021-12-14",
+            "keyword": [
+                "engagement",
+                "satisfaction",
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2hns-7v4f",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-03-17",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2020 - 2021",
+            "title": "All Employee Survey (AES) 2020 - 2021"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN22FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 22 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-094",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -1471,101 +1483,73 @@
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
-            "identifier": "VA-VHA-OIA-094",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 22",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN22FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 22 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 22"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/2idy-mcc4",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-06",
-            "keyword": [
-                "arizona",
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
-            "identifier": "https://www.data.va.gov/api/views/2idy-mcc4",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Arizona",
+            "identifier": "https://www.data.va.gov/api/views/2idy-mcc4",
+            "issued": "2021-08-26",
+            "keyword": [
+                "arizona",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2idy-mcc4",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-06",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Arizona"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2iia-69a8",
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
-            "identifier": "https://www.data.va.gov/api/views/2iia-69a8",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE JAN2019",
-            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1573,41 +1557,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2iia-69a8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2iia-69a8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2iia-69a8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2iia-69a8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2iia-69a8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2iia-69a8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2iia-69a8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2iia-69a8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2iia-69a8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/2iia-69a8",
+            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 120"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2iia-69a8",
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
+            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/2jyn-znvf",
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
+            "description": "<p>The tracking system is for patients identified in the Creutzfeldt Jakob Disease (CJD) lookback notification initiative established in January 1995 as part of the lookback notification of all Department of Veterans Affairs (VA) patients who may have received certain lot numbers of blood derivatives or blood components produced from donors with CJD. Even though the Centers of Disease Control and Prevention characterized the risk of transmission of CJD from blood derivative products as 'small and immeasurable' and 'theoretical', VA believed it had an ethical obligation to inform patients of the exposure to potentially contaminated blood components or plasma derivative products while under VA's care. The patients were notified. The Veterans Health Administration (VHA) established a tracking system for individuals who received these products to determine if there was an increase in VA CJD cases. Every two years, the VHA National Infectious Diseases Service updates the status of patients who had previously been identified through the VA CJD lookback notification initiative. The Creutzfeldt-Jakob Disease Lookback Dataset (CJDLD) is a prospective collection of data; requests for individual reports are not accepted.</p>",
+            "identifier": "VA-VHA-PCS-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1995-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "blood",
                 "cjd",
@@ -1618,80 +1621,59 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/2jyn-znvf",
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
-            "identifier": "VA-VHA-PCS-002",
-            "description": "<p>The tracking system is for patients identified in the Creutzfeldt Jakob Disease (CJD) lookback notification initiative established in January 1995 as part of the lookback notification of all Department of Veterans Affairs (VA) patients who may have received certain lot numbers of blood derivatives or blood components produced from donors with CJD. Even though the Centers of Disease Control and Prevention characterized the risk of transmission of CJD from blood derivative products as 'small and immeasurable' and 'theoretical', VA believed it had an ethical obligation to inform patients of the exposure to potentially contaminated blood components or plasma derivative products while under VA's care. The patients were notified. The Veterans Health Administration (VHA) established a tracking system for individuals who received these products to determine if there was an increase in VA CJD cases. Every two years, the VHA National Infectious Diseases Service updates the status of patients who had previously been identified through the VA CJD lookback notification initiative. The Creutzfeldt-Jakob Disease Lookback Dataset (CJDLD) is a prospective collection of data; requests for individual reports are not accepted.</p>",
-            "title": "Creutzfeldt-Jakob Disease Lookback Dataset (CJDLD)",
-            "programCode": [
-                "029:041"
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
+            "title": "Creutzfeldt-Jakob Disease Lookback Dataset (CJDLD)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2ke8-mfsz",
-            "issued": "2021-11-10",
             "@type": "dcat:Dataset",
-            "modified": "2021-11-17",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "Veterans Day 2021 data story honoring 100 anniversary of the Tomb of Unknown Soldier.",
             "identifier": "https://www.data.va.gov/api/views/2ke8-mfsz",
+            "issued": "2021-11-10",
+            "landingPage": "https://www.data.va.gov/d/2ke8-mfsz",
+            "modified": "2021-11-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Veterans Day 2021 data story honoring 100 anniversary of the Tomb of Unknown Soldier.",
             "title": "Veterans Day 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2ks5-yvrc",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "demographics",
-                "veterans",
-                "women"
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
-            "identifier": "VA-OEI-OEI-165",
             "description": "<p>This profile shows the demographics and socioeconomic characteristics of women Veterans. It compares women to men Veterans and women to non-Veterans. This report uses data from the 2014 American Community Survey Public Use Microdata Sample.</p>",
-            "title": "Profile of Women Veterans:  2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1700,24 +1682,48 @@
                     "title": "Profile of Women Veterans: 2014"
                 }
             ],
+            "identifier": "VA-OEI-OEI-165",
+            "issued": "2017-07-26",
+            "keyword": [
+                "demographics",
+                "veterans",
+                "women"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2ks5-yvrc",
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
+            "title": "Profile of Women Veterans:  2014"
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
+            "description": "<p>USA Spending- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects- December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-010",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "birth defects",
                 "cfda 64 128",
@@ -1727,62 +1733,38 @@
                 "vocational rehabilatition for vietnam veterans children",
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
-            "identifier": "VA-VBA-USASPENDING122013-010",
-            "description": "<p>USA Spending- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects- December 2013.</p>",
-            "title": "USA Spending file- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects-  CFDA 64.128",
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
+            "title": "USA Spending file- Vocational Rehabilitation for Vietnam Veterans Children with Spina Bifida or other covered Birth Defects-  CFDA 64.128"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/2mgp-3fgd",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "healthcare",
-                "order",
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
-            "identifier": "VA-VIA-7",
+            "dataQuality": true,
             "description": "<p>This service provides web services used to obtain order releated data. Users of this service are intended to be healthcare providers</p>",
-            "title": "Order Management Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1791,45 +1773,43 @@
                     "title": "Order Management Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VIA-7",
+            "issued": "2017-11-17",
+            "keyword": [
+                "healthcare",
+                "order",
+                "provider"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2mgp-3fgd",
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
+            "title": "Order Management Service"
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
-            "identifier": "VA-VBA-ABR2012-031",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Surviving Spouses Receiving DIC by Age at the End of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1837,44 +1817,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-031",
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
+            "title": "Surviving Spouses Receiving DIC by Age at the End of FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.techstrategies.oit.va.gov/docs/CTSNotes/TS%20Note%20Vol%202%20Issue%208_Post-508.pdf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "configuration",
-                "it"
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
-            "identifier": "VA-OIT-ASD-TSNV2-008",
             "description": "<p>VA Executive's Guide to Configuration Management</p>",
-            "title": "TS Note Vol 2 Issue 8",
-            "programCode": [
-                "029:078"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1883,41 +1866,41 @@
                     "title": "TS Note Vol 2 Issue 8"
                 }
             ],
+            "identifier": "VA-OIT-ASD-TSNV2-008",
+            "issued": "2017-07-26",
+            "keyword": [
+                "configuration",
+                "it"
+            ],
+            "landingPage": "https://www.techstrategies.oit.va.gov/docs/CTSNotes/TS%20Note%20Vol%202%20Issue%208_Post-508.pdf",
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
+            "title": "TS Note Vol 2 Issue 8"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2psu-74cv",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "oklahoma",
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
-            "identifier": "VA-OEI-OEI-122",
             "description": "<p>This is summary of the programs and services provided by VA in Oklahoma in fiscal year 2014.</p>",
-            "title": "State Summary:  Oklahoma",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1926,44 +1909,45 @@
                     "title": "State Summary:  Oklahoma"
                 }
             ],
+            "identifier": "VA-OEI-OEI-122",
+            "issued": "2017-07-26",
+            "keyword": [
+                "oklahoma",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2psu-74cv",
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
+            "title": "State Summary:  Oklahoma"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2qdi-cvfb",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterabs"
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
-            "identifier": "2364f13c-1614-4db7-bbad-50c48356d6ab",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Maine FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1971,33 +1955,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "2364f13c-1614-4db7-bbad-50c48356d6ab",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterabs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2qdi-cvfb",
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
+            "title": "State Summary Maine FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/2rci-xm64",
-            "issued": "2024-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-02",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VACONCVAS",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/2rci-xm64",
             "description": "VetPop2020 estimate of Veterans by gender from 2000 to 2023",
-            "title": "VetPop2020_Gender_2000to2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2005,57 +1992,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2rci-xm64/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2rci-xm64/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2rci-xm64/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2rci-xm64/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2rci-xm64/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2rci-xm64/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2rci-xm64/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2rci-xm64/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2rci-xm64/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/2rci-xm64",
+            "issued": "2024-07-17",
+            "landingPage": "https://www.data.va.gov/d/2rci-xm64",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-02",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020_Gender_2000to2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2rzp-vjiu",
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
-            "identifier": "b8882557-ca8b-4e3c-9257-df8b555f165b",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary New York FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2063,37 +2047,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "b8882557-ca8b-4e3c-9257-df8b555f165b",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2rzp-vjiu",
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
+            "title": "State Summary New York FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2s3r-6uhz",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "population",
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
-            "identifier": "ed245a4c-a452-4a77-b698-2a27a773a154",
+            "dataQuality": true,
             "description": "<p>This file shows the number of Veterans in each state who used each of 7 VA benefits during fiscal year 2016.  It also shows the unique count of users across all VA programs and an estimate of the total Veteran population in each state.</p>",
-            "title": "Number of Veterans who Used VA Benefits by State FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2101,49 +2085,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ed245a4c-a452-4a77-b698-2a27a773a154",
+            "issued": "2017-11-09",
+            "keyword": [
+                "population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2s3r-6uhz",
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
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "Number of Veterans who Used VA Benefits by State FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Coverage_Amount_by_State_April_2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-04-01T04:00:00Z/2012-04-30T04:00:00Z",
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
-            "identifier": "VA-VBA-INS2012-019",
+            "dataQuality": true,
             "description": "<p>Provides the amount of Veterans' Group Life Insurance (VGLI) coverage by state.  This report provides a snapshot of the amount of VGLI coverage as of April 30, 2012.  For members who reside outside the United States, coverage is not identified by individual country.  The total amount of coverage was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "VGLI Coverage Amount by State as of April 30, 2012",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2151,68 +2128,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2s5p-ac6s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2s5p-ac6s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2s5p-ac6s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2s5p-ac6s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2s5p-ac6s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2s5p-ac6s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2s5p-ac6s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2s5p-ac6s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2s5p-ac6s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-019",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Coverage_Amount_by_State_April_2012.csv",
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
+            "temporal": "2012-04-01T04:00:00Z/2012-04-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VGLI Coverage Amount by State as of April 30, 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2sc2-zyk7",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2024-03-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-08",
-            "keyword": [
-                "age group",
-                "expenditures",
-                "state",
-                "veteran compensation benefits"
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
-            "identifier": "https://www.data.va.gov/api/views/2sc2-zyk7",
             "description": "1. This provides a count of Veterans on the rolls for Compensation Service in FY 2023 with expenditures for compensation claims by state and the age groups of Veterans in each category.\n2. See VBA's Annual Benefits Report for additional information:  www.benefits.va.gov/REPORTS/abr/\n3. To protect Veteran privacy any categories containing less than ten Veterans are not included.",
-            "title": "Veteran Compensation Expenditures By State of Residence and Age Group FY 2023",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2220,57 +2201,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2sc2-zyk7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2sc2-zyk7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2sc2-zyk7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2sc2-zyk7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2sc2-zyk7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2sc2-zyk7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2sc2-zyk7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2sc2-zyk7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2sc2-zyk7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/2sc2-zyk7",
+            "issued": "2024-03-08",
+            "keyword": [
+                "age group",
+                "expenditures",
+                "state",
+                "veteran compensation benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2sc2-zyk7",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-03-08",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veteran Compensation Expenditures By State of Residence and Age Group FY 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2sxd-wsdp",
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
-            "identifier": "https://www.data.va.gov/api/views/2sxd-wsdp",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM BENEFITS to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA\u2019s determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE JAN FY2019",
-            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2278,61 +2262,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2sxd-wsdp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2sxd-wsdp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2sxd-wsdp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2sxd-wsdp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2sxd-wsdp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2sxd-wsdp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2sxd-wsdp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2sxd-wsdp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2sxd-wsdp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/2sxd-wsdp",
+            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 117"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2sxd-wsdp",
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
+            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE JAN FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2uc8-akx6",
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
-            "identifier": "https://www.data.va.gov/api/views/2uc8-akx6",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM BENEFITS to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA\u2019s determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE APR2019",
-            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2340,62 +2324,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2uc8-akx6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2uc8-akx6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2uc8-akx6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2uc8-akx6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2uc8-akx6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2uc8-akx6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2uc8-akx6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2uc8-akx6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2uc8-akx6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/2uc8-akx6",
+            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 117"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2uc8-akx6",
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
+            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2va3-b9uq",
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
-            "identifier": "https://www.data.va.gov/api/views/2va3-b9uq",
+            "dataQuality": true,
             "description": "All DIC Recipients by their Relationship to the Veterans, FY2022. DIC is a tax-free monetary benefit generally payable to a surviving spouse, child, or parent of deceased Servicemembers or Veterans.",
-            "title": "All Dependency and Indemnity Compensation (DIC) Recipients by Relationship to Veteran, FY2022",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2403,57 +2386,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2va3-b9uq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2va3-b9uq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2va3-b9uq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/2va3-b9uq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2va3-b9uq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2va3-b9uq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/2va3-b9uq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/2va3-b9uq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/2va3-b9uq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/2va3-b9uq",
+            "issued": "2023-03-21",
+            "keyword": [
+                "dic benefits",
+                "veterans",
+                "veterans surviving spouses and children"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2va3-b9uq",
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
+            "title": "All Dependency and Indemnity Compensation (DIC) Recipients by Relationship to Veteran, FY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2vnr-6gca",
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
-            "title": "Equitable Relief Reports 2007",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2461,31 +2447,57 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2vnr-6gca",
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
+            "title": "Equitable Relief Reports 2007"
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
-            "temporal": "2015-10-01T04:00:00Z/2015-10-01T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR31_102015_Pending_and_EWL_Biweekly_Desired_Date_Division_PDFReady.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 October 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-426",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -2499,70 +2511,42 @@
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
-            "identifier": "VA-VHA-OIA-426",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 October 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR31_102015_Pending_and_EWL_Biweekly_Desired_Date_Division_PDFReady.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 October 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-10-01T04:00:00Z/2015-10-01T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 October 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/2wry-r4tv",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "central iowa"
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
-            "identifier": "VA-OEI-OEI-185",
             "description": "<p>This summary describes the programs and services VA provided in Iowa in fiscal year 2015.</p>",
-            "title": "State Summary: Iowa",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2571,26 +2555,54 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-185",
+            "issued": "2017-07-26",
+            "keyword": [
+                "central iowa"
+            ],
+            "landingPage": "https://www.data.va.gov/d/2wry-r4tv",
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
+            "title": "State Summary: Iowa"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN7FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 7 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-081",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -2606,73 +2618,44 @@
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
-            "identifier": "VA-VHA-OIA-081",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 7",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN7FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 7 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 7"
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
-            "identifier": "VA-OEI-OEI-018",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/Surveys.asp",
             "description": "<p>This survey is the sixth in a series of comprehensive nationwide surveys designed to help the Department of Veterans Affairs (VA) plan its future programs and services for Veterans. This is the first time VA has included groups other than Veterans.</p>",
-            "title": "The National Survey of Veterans, Active Duty Service Members, Activated National Guard and Reserve Members, Family Members and Survivors",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2681,26 +2664,48 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/Surveys.asp",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-018",
+            "issued": "2017-07-26",
+            "keyword": [
+                "survey",
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
                 "Data on Veterans Survey"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "The National Survey of Veterans, Active Duty Service Members, Activated National Guard and Reserve Members, Family Members and Survivors"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3274-thx4",
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
+            "dataQuality": true,
+            "description": "Learn which PTSD treatments have been studied scientifically using randomized controlled trial (RCT) design.",
+            "identifier": "https://www.data.va.gov/api/views/3274-thx4",
             "issued": "2020-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
             "keyword": [
                 "medication",
                 "psychotherapy",
@@ -2708,37 +2713,45 @@
                 "ptsd treatment",
                 "treatment option"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for PTSD",
-                "hasEmail": "mailto:ncptsd@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/3274-thx4",
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
-            "identifier": "https://www.data.va.gov/api/views/3274-thx4",
-            "description": "Learn which PTSD treatments have been studied scientifically using randomized controlled trial (RCT) design.",
-            "title": "Which PTSD treatments have been studied?",
-            "programCode": [
-                "029:000"
-            ],
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
-            "language": [
-                "en-US"
-            ]
+            "rights": "All data is within the public domain and is currently available for download.",
+            "title": "Which PTSD treatments have been studied?"
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
+                    "downloadURL": "http://www.va.gov/vetdata/docs/GDX/02geo98.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Geographic Distribution of VA Expenditures FY1998"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-024",
             "issued": "2017-07-26",
-            "temporal": "1997-10-01T04:00:00Z/1998-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -2752,67 +2765,37 @@
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
-            "identifier": "VA-OEI-OEI-024",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY1998",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.va.gov/vetdata/docs/GDX/02geo98.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Geographic Distribution of VA Expenditures FY1998"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "1997-10-01T04:00:00Z/1998-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY1998"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/33fk-kbpk",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "maine",
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
-            "identifier": "VA-OEI-OEI-107",
             "description": "<p>This is a summary of the programs and benefits provided by VA in Maine in fiscal year 2014.</p>",
-            "title": "State Summary:  Maryland",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2821,44 +2804,44 @@
                     "title": "State Summary:  Maryland"
                 }
             ],
+            "identifier": "VA-OEI-OEI-107",
+            "issued": "2017-07-26",
+            "keyword": [
+                "maine",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/33fk-kbpk",
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
+            "title": "State Summary:  Maryland"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/33w6-bgr2",
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
-            "identifier": "OM-OM-181",
             "description": "<p>COIN report 145 for Feb 2017</p>",
-            "title": "COIN 145 Feb 2017",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2866,41 +2849,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-181",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/33w6-bgr2",
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
+            "title": "COIN 145 Feb 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/34aa-5ss9",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "texas",
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
-            "identifier": "VA-OEI-OEI-130",
             "description": "<p>This is a summary of the programs and services provided by VA in Texas in fiscal year 2014.</p>",
-            "title": "State Summary:  Texas",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2909,49 +2892,46 @@
                     "title": "State Summary:  Texas"
                 }
             ],
+            "identifier": "VA-OEI-OEI-130",
+            "issued": "2017-07-26",
+            "keyword": [
+                "texas",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/34aa-5ss9",
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
+            "title": "State Summary:  Texas"
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
-            "identifier": "VA-VBA-ABR2012-103",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Missouri-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2959,26 +2939,9 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "ABR 2012"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
-            "bureauCode": [
-                "029:25"
-            ],
+            "identifier": "VA-VBA-ABR2012-103",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
             "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
             "keyword": [
                 "fy2012 benefits",
                 "fy2012 vba",
@@ -2986,22 +2949,39 @@
                 "vba benefits",
                 "vba benefits by state"
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
-            "identifier": "VA-VBA-ABR2012-109",
-            "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "New Mexico-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:005"
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
+            "theme": [
+                "ABR 2012"
+            ],
+            "title": "Missouri-FY12 Benefits Summary"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3010,26 +2990,60 @@
                     "title": "New Mexico-FY12 Benefits Summary"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-109",
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
+            "title": "New Mexico-FY12 Benefits Summary"
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
+            "description": "<p>National-level, VISN-level, and VAMC-level statistics on the numbers and percentages of users of VHA care with a diagnosis of posttraumatic stress disorder (PTSD) for fiscal year 2015.  Prepared by the VA Northeast Program Evaluation Center (NEPEC).  <b> This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/34rw-t2f9/text/plain",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "VA-VHA-10N-012",
+            "isPartOf": "VA-VHA-10N-014",
             "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-29",
             "keyword": [
                 "2015",
                 "diagnosis",
@@ -3045,54 +3059,52 @@
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
-            "identifier": "VA-VHA-10N-012",
-            "description": "<p>National-level, VISN-level, and VAMC-level statistics on the numbers and percentages of users of VHA care with a diagnosis of posttraumatic stress disorder (PTSD) for fiscal year 2015.  Prepared by the VA Northeast Program Evaluation Center (NEPEC).  <b> This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>",
-            "title": "VA PTSD Veteran Patient Statistics - 2015",
-            "isPartOf": "VA-VHA-10N-014",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:042"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/34rw-t2f9/text/plain",
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
+            "title": "VA PTSD Veteran Patient Statistics - 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/354t-3ffa",
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
+            "description": "<p>Observed minus expected length of stay.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset8_OMELOS.xml",
+                    "mediaType": "application/xml",
+                    "title": "Observed Minus Expected Length of Stay (OMELOS)"
+                }
             ],
+            "identifier": "VA-VHA-OIA-044",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -3115,69 +3127,40 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/354t-3ffa",
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
-            "identifier": "VA-VHA-OIA-044",
-            "description": "<p>Observed minus expected length of stay.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - OMELOS",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset8_OMELOS.xml",
-                    "mediaType": "application/xml",
-                    "title": "Observed Minus Expected Length of Stay (OMELOS)"
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
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - OMELOS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/355n-9dhx",
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
-            "identifier": "OM-OM-174",
             "description": "<p>COIN report 145 Feb 2016</p>",
-            "title": "COIN 145 Feb 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3185,123 +3168,155 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-174",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/355n-9dhx",
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
+            "title": "COIN 145 Feb 2016"
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
+            "description": "<p>USA Spending- Vocational Rehabilitation for Disabled Veterans - Chapter 31- February 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-041",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING012014-041",
-            "description": "<p>USA Spending- Vocational Rehabilitation for Disabled Veterans - Chapter 31- February 2014</p>",
-            "title": "USA Spending file-02/2014- Vocational Rehabilitation for Disabled Veterans-  CFDA 64.116",
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
+            "title": "USA Spending file-02/2014- Vocational Rehabilitation for Disabled Veterans-  CFDA 64.116"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/35pk-ekmk",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Tennessee FY2023",
+            "identifier": "https://www.data.va.gov/api/views/35pk-ekmk",
             "issued": "2024-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "tennessee"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/35pk-ekmk",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/35pk-ekmk",
-            "description": "NCVAS State Summary Tennessee FY2023",
-            "title": "NCVAS State Summary Tennessee FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Tennessee FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/38ij-jq95",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Maryland FY2023",
+            "identifier": "https://www.data.va.gov/api/views/38ij-jq95",
             "issued": "2024-06-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-22",
             "keyword": [
                 "fy2024",
                 "maryland",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/38ij-jq95",
+            "modified": "2024-07-22",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/38ij-jq95",
-            "description": "NCVAS State Summary Maryland FY2023",
-            "title": "NCVAS State Summary Maryland FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Maryland FY2023"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR34_112015_Retrospective_Wait_Times_Desired_Date_by_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 31 Oct 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-433",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-10-31T04:00:00Z/2015-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -3315,53 +3330,41 @@
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
-            "identifier": "VA-VHA-OIA-433",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Oct 31",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR34_112015_Retrospective_Wait_Times_Desired_Date_by_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 31 Oct 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-10-31T04:00:00Z/2015-10-31T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Oct 31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/39pc-24dr",
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
+            "description": "<p>The Emerging Pathogens Initiative (EPI) database contains emerging pathogens information from the local Veterans Affairs Medical Centers (VAMCs). The EPI software package allows the VA to track emerging pathogens on the national level without additional data entry at the local level. The results from aggregation of data can be shared with the appropriate public health authorities including non-VA and the private health care sector allowing national planning, formulation of intervention strategies, and resource allocations. EPI is designed to automatically collect data on emerging diseases for Veterans Affairs Central Office (VACO) to analyze. The data is sent to the Austin Information Technology Center (AITC) from all Veterans Health Information Systems and Technology Architecture (VistA) systems for initial processing and combination with related workload data. VACO data retrieval and analysis is then carried out. The AITC creates two file structures both in Statistical Analysis Software (SAS) file format, which are used as a source of data for the Veterans Affairs Headquarters (VAHQ) Infectious Diseases Program Office. These files are manipulated and used for analysis and reporting by the National Infectious Diseases Service. Emerging Pathogens (as characterized by VACO) act as triggers for data acquisition activities in the automated program. The system retrieves relevant, predetermined, patient-specific information in the form of a Health Level Seven (HL7) message that is transmitted to the central data repository at the AITC. Once at that location, the data is converted to a SAS dataset for analysis by the VACO National Infectious Diseases Service. Before data transmission an Emerging Pathogens Verification Report is produced for the local sites to review, verify, and make corrections as needed. After data transmission to the AITC it is added to the EPI database.</p>",
+            "identifier": "VA-VHA-PCS-007",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1998-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "disease",
                 "emerging",
@@ -3372,61 +3375,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/39pc-24dr",
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
-            "identifier": "VA-VHA-PCS-007",
-            "description": "<p>The Emerging Pathogens Initiative (EPI) database contains emerging pathogens information from the local Veterans Affairs Medical Centers (VAMCs). The EPI software package allows the VA to track emerging pathogens on the national level without additional data entry at the local level. The results from aggregation of data can be shared with the appropriate public health authorities including non-VA and the private health care sector allowing national planning, formulation of intervention strategies, and resource allocations. EPI is designed to automatically collect data on emerging diseases for Veterans Affairs Central Office (VACO) to analyze. The data is sent to the Austin Information Technology Center (AITC) from all Veterans Health Information Systems and Technology Architecture (VistA) systems for initial processing and combination with related workload data. VACO data retrieval and analysis is then carried out. The AITC creates two file structures both in Statistical Analysis Software (SAS) file format, which are used as a source of data for the Veterans Affairs Headquarters (VAHQ) Infectious Diseases Program Office. These files are manipulated and used for analysis and reporting by the National Infectious Diseases Service. Emerging Pathogens (as characterized by VACO) act as triggers for data acquisition activities in the automated program. The system retrieves relevant, predetermined, patient-specific information in the form of a Health Level Seven (HL7) message that is transmitted to the central data repository at the AITC. Once at that location, the data is converted to a SAS dataset for analysis by the VACO National Infectious Diseases Service. Before data transmission an Emerging Pathogens Verification Report is produced for the local sites to review, verify, and make corrections as needed. After data transmission to the AITC it is added to the EPI database.</p>",
-            "title": "Emerging Pathogens Initiative (EPI)",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1998-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Emerging Pathogens Initiative (EPI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/39za-rb3r",
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
-            "identifier": "https://www.data.va.gov/api/views/39za-rb3r",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to encourage membership in units of the Selected Reserve of the Ready Reserve and to provide educational assistance to members of the reserve components called or ordered to active service in response to a war or national emergency declared by the President or Congress. Generally, to qualify for benefits under MGIB-SR you must (1) Have a six-year obligation to serve in the Selected Reserve signed after June 30, 1985. If you are an officer, you must have agreed to serve six years in addition to your original obligation. For some types of training, it is necessary to have a six-year commitment that begins after September 30, 1990; (2) Complete your initial active duty for training (IADT); (3) Meet the requirement to receive a high school diploma or equivalency certificate before completing IADT. You may not use 12 hours toward a college degree to meet this requirement; and (4) Remain in good standing while serving in an active Selected Reserve unit. Generally, to qualify for benefits under REAP you must have served at least 90 consecutive days on active duty as a result of a call or order to active duty from a reserve component in response to a war or national emergency declared by the President or Congress. This is not a complete list of eligibility requirements. For more information on MGIB-SR and REAP visit <a href=\"http://www.gibill.va.gov\">http://www.gibill.va.gov</a>.</p>",
-            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM OCT2018",
-            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3434,103 +3418,100 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/39za-rb3r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/39za-rb3r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/39za-rb3r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/39za-rb3r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/39za-rb3r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/39za-rb3r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/39za-rb3r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/39za-rb3r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/39za-rb3r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/39za-rb3r",
+            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 032"
+            ],
+            "landingPage": "https://www.data.va.gov/d/39za-rb3r",
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
+            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3a67-rjkm",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "description": "The National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.",
+            "identifier": "https://www.data.va.gov/api/views/3a67-rjkm",
             "issued": "2019-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-30",
             "keyword": [
                 "demographics",
                 "equity",
                 "health equity"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/3a67-rjkm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-01-30",
+            "programCode": [
+                "029:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/3a67-rjkm",
-            "description": "The National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.",
-            "title": "National Veteran Health Equity Report",
-            "programCode": [
-                "029:048"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "theme": [
                 "Veteran Health Equity"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Veteran Health Equity Report"
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
@@ -3538,47 +3519,47 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "describedBy": "https://github.com/department-of-veterans-affairs/VHA-Facilities/blob/master/Report-HCV%20Registry%20Veterans%20in%20VHA%20Care%20in%202015%20by%20Nationa-VISN-Station.xlsx?raw=true",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "HCV Infected Veterans in VHA Care"
-            ],
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
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-01-01T05:00:00Z/2015-12-31T05:00:00Z",
+            "theme": [
+                "HCV Infected Veterans in VHA Care"
+            ],
+            "title": "Hepatitis C Virus (HCV) Registry Veterans in VHA Care in 2015, for the Nation, by VISN and by Station"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3aej-m45q",
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
-            "identifier": "https://www.data.va.gov/api/views/3aej-m45q",
             "description": "VetPop2023 projection of living Veterans by gender and 4 age groups at the VISN level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 Veterans Integrated Services Networks (VISNs), 11L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3586,82 +3567,104 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3aej-m45q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3aej-m45q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3aej-m45q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3aej-m45q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3aej-m45q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3aej-m45q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3aej-m45q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3aej-m45q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3aej-m45q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/3aej-m45q",
+            "issued": "2024-09-09",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3aej-m45q",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 Veterans Integrated Services Networks (VISNs), 11L"
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
+            "description": "This link provides access to Department of Veterans Affairs, Veterans Benefits Administration Media and Publications Fact Sheets, electronic brochures, videos and  other publications.",
+            "identifier": "VA-VBA-MEDIAPUB-019",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2012-08-01T04:00:00Z/2012-08-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
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
+            "modified": "2022-04-18",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-MEDIAPUB-019",
-            "description": "This link provides access to Department of Veterans Affairs, Veterans Benefits Administration Media and Publications Fact Sheets, electronic brochures, videos and  other publications.",
-            "title": "Veteran Benefits Fact Sheets Benefit Brochures videos and eBenefits Publications",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2012-08-01T04:00:00Z/2012-08-01T04:00:00Z",
             "theme": [
                 "General Benefit Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veteran Benefits Fact Sheets Benefit Brochures videos and eBenefits Publications"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/3anw-i7mn",
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
+            "description": "<p>Clinical Information Support System (CISS) is a web-based portal application that provides a framework of services for the VA enterprise and supplies an integration point for its partner systems. The initial CISS partner system is the Occupational Health Record-keeping System (OHRS), a web-based application that enables employee occupational health staff to create, maintain, and monitor medical records for VA employees and generate national, Veterans Integrated Service Network (VISN), and site-specific reports.The CISS portal is development in the delivery of information and applications to the clinical user community. It provides a single point of access for the clinical user's application and information needs, facilitating faster and more efficient patient care.The CISS framework further establishes a foundation for publishing any type of application, including clinical, non-clinical, HealtheVet, and legacy applications. These plug-in applications, called 'partner systems', can be developed independently and published to the users through the CISS portal. The CISS Program development team uses repeatable Agile development, management and support processes to rapidly develop quality software in 6-month release cycles, improving efficiency and customer satisfaction.</p>",
+            "identifier": "VA-VHA-OPH-004",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2009-09-09T04:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "clinical",
                 "framework",
@@ -3673,42 +3676,52 @@
                 "visn",
                 "web"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/3anw-i7mn",
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
-            "identifier": "VA-VHA-OPH-004",
-            "description": "<p>Clinical Information Support System (CISS) is a web-based portal application that provides a framework of services for the VA enterprise and supplies an integration point for its partner systems. The initial CISS partner system is the Occupational Health Record-keeping System (OHRS), a web-based application that enables employee occupational health staff to create, maintain, and monitor medical records for VA employees and generate national, Veterans Integrated Service Network (VISN), and site-specific reports.The CISS portal is development in the delivery of information and applications to the clinical user community. It provides a single point of access for the clinical user's application and information needs, facilitating faster and more efficient patient care.The CISS framework further establishes a foundation for publishing any type of application, including clinical, non-clinical, HealtheVet, and legacy applications. These plug-in applications, called 'partner systems', can be developed independently and published to the users through the CISS portal. The CISS Program development team uses repeatable Agile development, management and support processes to rapidly develop quality software in 6-month release cycles, improving efficiency and customer satisfaction.</p>",
-            "title": "Clinical Information Support System (CISS)",
-            "programCode": [
-                "029:041"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "2009-09-09T04:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Clinical Information Support System (CISS)"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2002.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2002.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-12",
             "issued": "2017-07-26",
-            "temporal": "2001-10-01T04:00:00Z/2002-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2002",
                 "appeals",
@@ -3725,69 +3738,39 @@
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
-            "identifier": "VA-OIT-ITIS-12",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2002.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2002",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2002.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2001-10-01T04:00:00Z/2002-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3b6s-egcv",
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
-            "identifier": "OM-OM-175",
             "description": "<p>COIN report 146 Feb 2016</p>",
-            "title": "COIN 146 Feb 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3795,63 +3778,64 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-175",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3b6s-egcv",
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
+            "title": "COIN 146 Feb 2016"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3b7z-de66",
-            "issued": "2023-07-18",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-15",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary New Mexico FY2021",
+            "identifier": "https://www.data.va.gov/api/views/3b7z-de66",
+            "issued": "2023-07-18",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "new mexico"
             ],
-            "identifier": "https://www.data.va.gov/api/views/3b7z-de66",
+            "landingPage": "https://www.data.va.gov/d/3b7z-de66",
+            "modified": "2024-06-15",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary New Mexico FY2021",
             "title": "NCVAS State Summary New Mexico FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3b9m-cxuq",
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
-            "identifier": "725508ee-e6d1-47f0-8a12-7a3d3cd6c24e",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Hawaii FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3859,39 +3843,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "725508ee-e6d1-47f0-8a12-7a3d3cd6c24e",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3b9m-cxuq",
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
+            "title": "State Summary Hawaii FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3bpv-5eec",
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
-            "identifier": "https://www.data.va.gov/api/views/3bpv-5eec",
             "description": "VetPop2023 projection of living Veterans by gender and rank (Officer or Enlisted) at the national level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 National Rank (Officer or Enlisted) Data, 5L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3899,57 +3880,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3bpv-5eec/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3bpv-5eec/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3bpv-5eec/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3bpv-5eec/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3bpv-5eec/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3bpv-5eec/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3bpv-5eec/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3bpv-5eec/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3bpv-5eec/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/3bpv-5eec",
+            "issued": "2024-09-09",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3bpv-5eec",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 National Rank (Officer or Enlisted) Data, 5L"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3cf7-re8m",
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
-            "identifier": "https://www.data.va.gov/api/views/3cf7-re8m",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located</p>",
-            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS FEB2019",
-            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3957,61 +3941,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3cf7-re8m/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3cf7-re8m/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3cf7-re8m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3cf7-re8m/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3cf7-re8m/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3cf7-re8m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3cf7-re8m/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3cf7-re8m/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3cf7-re8m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/3cf7-re8m",
+            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 118"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3cf7-re8m",
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
+            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3ci3-3ihi",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-03-01T05:00:00Z/2015-03-31T04:00:00Z",
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
-            "identifier": "VA-OM-OM-128",
             "description": "<p>aged accounts receivable</p>",
-            "title": "COIN 0017 CARS AGE PROFILE REPORT MAR 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4019,45 +4002,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-128",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3ci3-3ihi",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-03-01T05:00:00Z/2015-03-31T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0017 CARS AGE PROFILE REPORT MAR 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3ctr-s4s9",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2021-01-27",
-            "temporal": "2013-10-01T04:00:00Z/2013-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-27",
-            "keyword": [
-                "2013",
-                "face amount",
-                "face amount by state",
-                "life insurance policies"
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
-            "identifier": "https://www.data.va.gov/api/views/3ctr-s4s9",
+            "dataQuality": true,
             "description": "VBA- Insurance Lob- Face Mount by program by State- October 2013.",
-            "title": "Face Amount by Program by State- October 2013",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4065,46 +4045,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3ctr-s4s9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3ctr-s4s9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3ctr-s4s9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3ctr-s4s9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3ctr-s4s9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3ctr-s4s9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3ctr-s4s9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3ctr-s4s9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3ctr-s4s9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/3ctr-s4s9",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2021-01-27",
+            "keyword": [
+                "2013",
+                "face amount",
+                "face amount by state",
+                "life insurance policies"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3ctr-s4s9",
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
+            "temporal": "2013-10-01T04:00:00Z/2013-10-31T04:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Face Amount by Program by State- October 2013"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2001.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2001.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-13",
             "issued": "2017-07-26",
-            "temporal": "2000-10-01T04:00:00Z/2001-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2001",
                 "appeals",
@@ -4121,72 +4134,40 @@
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
-            "identifier": "VA-OIT-ITIS-13",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2001.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2001",
-            "programCode": [
-                "029:080"
+            "temporal": "2000-10-01T04:00:00Z/2001-09-30T04:00:00Z",
+            "theme": [
+                "Basic Statistics",
+                "Use",
+                "and Operational Data"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2001.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "Basic Statistics",
-                "Use",
-                "and Operational Data"
-            ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2001"
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
-                "american community survey",
-                "demographics",
-                "veterans",
-                "women",
-                "women veterans"
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
-            "identifier": "VA-OEI-OEI-168",
+            "dataQuality": true,
             "description": "<p>VA released Profile of Women Veterans: 2016 located on the Reports page under the Population category. This profile shows the demographics and socioeconomic characteristics of women Veterans. It compares women to men Veterans and women Veterans to women non-Veterans. This report uses data from the 2014 American Community Survey Public Use Microdata Sample.</p>",
-            "title": "Profile of Women Veterans:  2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4195,40 +4176,43 @@
                     "title": "Profile of Women Veterans:  2016"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-168",
+            "issued": "2017-07-26",
+            "keyword": [
+                "american community survey",
+                "demographics",
+                "veterans",
+                "women",
+                "women veterans"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/index.asp",
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
+            "title": "Profile of Women Veterans:  2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3ebx-u9da",
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
-            "identifier": "https://www.data.va.gov/api/views/3ebx-u9da",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist wartime veterans in need whose non-service- connected disabilities are permanent and total preventing them from following a substantially gainful occupation. A Veteran who meets the wartime service requirements is potential eligible if he/she is: \u2022 permanently and totally disabled for reasons not necessarily due to service, \u2022 age 65 or older, or \u2022 is presumed to be totally and permanently disabled for pension purposes because: o he/she is a patient in a nursing home for long-term care due to a disability, or o being disabled, as determined by the Commissioner of Social Security (SS) for purposes of any benefits administered by the Commissioner, such as SS disability benefits or Supplemental Security Income. Income restrictions are prescribed in 38 U.S.C. 1521. Pension is not payable to those whose estates are so large that it is reasonable they use the estate for maintenance. A Veteran meets wartime service requirements if he/she served: \u2022 a total of 90 days or more during one or more periods of war; \u2022 90 or more consecutive days that began or ended during a period of war; or \u2022 for any length of time during a period of war if he/she was discharged or released for a service-connected disability. Veterans entering service after September 7, 1980, must also meet the minimum active duty requirement of 24 months of continuous service or the full period to which the Veteran was called to active duty. (38 U.S.C.5303(A)).</p>",
-            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS MAY2019",
-            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4236,43 +4220,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3ebx-u9da/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3ebx-u9da/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3ebx-u9da/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3ebx-u9da/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3ebx-u9da/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3ebx-u9da/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3ebx-u9da/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3ebx-u9da/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3ebx-u9da/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/3ebx-u9da",
+            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 104"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3ebx-u9da",
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
+            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS MAY2019"
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
+                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/WEB-2-GDX-FY2001.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-027",
             "issued": "2017-07-26",
-            "temporal": "2000-10-01T04:00:00Z/2001-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -4286,67 +4299,38 @@
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
-            "identifier": "VA-OEI-OEI-027",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2001",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/WEB-2-GDX-FY2001.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2000-10-01T04:00:00Z/2001-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3emx-6ppt",
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
-            "identifier": "https://www.data.va.gov/api/views/3emx-6ppt",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM BENEFITS to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA\u2019s determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE NOV2018",
-            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4354,67 +4338,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3emx-6ppt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3emx-6ppt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3emx-6ppt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3emx-6ppt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3emx-6ppt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3emx-6ppt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3emx-6ppt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3emx-6ppt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3emx-6ppt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/3emx-6ppt",
+            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 117"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3emx-6ppt",
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
+            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE NOV2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3equ-c3kz",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2020-11-02",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
-            "references": [
-                "https://doi.org/10.1002/jts22520"
-            ],
-            "keyword": [
-                "development",
-                "journal of traumatic stress",
-                "ptsd-repository",
-                "randomized controlled trials for ptsd"
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
-            "identifier": "https://www.data.va.gov/api/views/3equ-c3kz",
+            "dataQuality": true,
             "description": "Article from the Journal of Traumatic Stress (2020) by Maya E. O\u2019Neil, Juliette M. Harik, Marian S. McDonagh, Tamara P. Cheney, Frances C. Hsu, David C. Cameron, Kathleen F. Carlson, Sonya B. Norman, and Jessica L. Hamblen. \n\nAbstract: Given the extensive research on posttraumatic stress disorder (PTSD) treatment, a single, updatable repository of data from PTSD treatment studies would be useful for clinical, research, and policy stakeholders. To meet this need, we established a preliminary dataset of abstracted PTSD trial data, which serve as the basis for the PTSD Trials Standardized Data Repository (PTSD-Repository), maintained by the National Center for PTSD (NCPTSD).We followed systematic review methods to identify published randomized controlled trials (RCTs) of PTSD interventions. We consulted with a panel of experts to determine a priori inclusion criteria, ensure that we captured all relevant studies, and identify variables for abstraction. We searched multiple databases for materials published from 1980 to 2018 and reviewed reference lists of relevant systematic reviews and clinical practice guidelines. In total, 318 RCTs of PTSD interventions that enrolled almost 25,000 participants were included. We abstracted 337 variables across all studies, including study, participant, and intervention characteristics as well as results. In the present paper, we describe our methods and define data elements included in the data tables. We explain coding challenges, identify inconsistencies in reporting across study types, and discuss ways stakeholders can use PTSD-Repository data to enhance research, education, and policy. The abstracted data are currently publicly available on the NCPTSD website and can be used for future systematic reviews and identifying research gaps and as an information resource for clinicians, patients, and family members.\n\nCitation: O'Neil, M. E., Harik, J. M., McDonagh, M. S., Cheney, T. P., Hsu, F. C., Cameron, D. C., Carlson, K. F., Norman, S. B., & Hamblen, J. L. (2020). Development of the PTSD-Repository: A publicly available repository of randomized controlled trials for posttraumatic stress disorder. Journal of Traumatic Stress, 33, 410-419. https://doi.org/10.1002/jts22520",
-            "title": "Journal of Traumatic Stress: Development of the PTSD-Repository, O'Neil et al. (2020)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4422,44 +4401,49 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "PTSD-Repository"
+            "identifier": "https://www.data.va.gov/api/views/3equ-c3kz",
+            "issued": "2020-11-02",
+            "keyword": [
+                "development",
+                "journal of traumatic stress",
+                "ptsd-repository",
+                "randomized controlled trials for ptsd"
             ],
+            "landingPage": "https://www.data.va.gov/d/3equ-c3kz",
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
+            "references": [
+                "https://doi.org/10.1002/jts22520"
+            ],
+            "rights": "All data is within the public domain and is currently available for download.",
+            "theme": [
+                "PTSD-Repository"
+            ],
+            "title": "Journal of Traumatic Stress: Development of the PTSD-Repository, O'Neil et al. (2020)"
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
-            "temporal": "2010-04-01T04:00:00Z/2010-06-30T04:00:00Z",
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
-            "identifier": "VA-OM-OM-095",
+            "dataQuality": true,
             "description": "<p>FY 2010 Third Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2010 Third Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4468,50 +4452,45 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-095",
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
+            "temporal": "2010-04-01T04:00:00Z/2010-06-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2010 Third Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/State_Dist_FY10.xls",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Insurance_Technical_Notes_State_DistFY10.doc"
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
-            "identifier": "VA-VBA-INS2010-002",
+            "dataQuality": true,
             "description": "<p>Fiscal Year 2010 life insurance payments, face value of Insurance, and total number of policies by state.  Data were derived from Actuarial reports, including FY 2010 Statement of Cash Flows, FY 2010 Policy Exhibit, and FY 2010 State of Residency Report.</p>",
-            "title": "Life Insurance Payments, Face Value of Insurance, and Number of Policies",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4519,50 +4498,53 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2010-002",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/State_Dist_FY10.xls",
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
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Insurance_Technical_Notes_State_DistFY10.doc"
+            ],
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Life Insurance Payments, Face Value of Insurance, and Number of Policies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.techstrategies.oit.va.gov/docs_design_patterns_aaa.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2016-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "active directory",
-                "identity and access management",
-                "pki",
-                "single sign-on",
-                "user authentication"
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
-            "identifier": "VA-OIT-ASD-001",
+            "dataQuality": true,
+            "describedBy": "https://www.techstrategies.oit.va.gov/docs_design_patterns_aaa.asp",
             "description": "<p>Design Pattern: \u00ef\u00bf\u00bdAuthentication, Authorization &amp; Audit. Describes  how applications should consume the enterprise internal user authentication services</p>",
-            "title": "Design Pattern: Authentication, Authorization & Audit",
-            "programCode": [
-                "029:078"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4571,49 +4553,49 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.techstrategies.oit.va.gov/docs_design_patterns_aaa.asp",
-            "dataQuality": true,
+            "identifier": "VA-OIT-ASD-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "active directory",
+                "identity and access management",
+                "pki",
+                "single sign-on",
+                "user authentication"
+            ],
+            "landingPage": "https://www.techstrategies.oit.va.gov/docs_design_patterns_aaa.asp",
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
+            "temporal": "2014-10-01T04:00:00Z/2016-10-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Design Pattern: Authentication, Authorization & Audit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3g57-mg76",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-01-01T05:00:00Z/2015-07-28T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "complaints",
-                "consumer",
-                "veterans"
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
-            "identifier": "VA-NCA-MP-003",
+            "dataQuality": true,
             "description": "<p>This document informs consumers in the private sector where to file complaints regarding Veteran burial concerns.</p>",
-            "title": "Consumer Affairs:  What You Can Do",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4621,40 +4603,42 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-MP-003",
+            "issued": "2017-07-26",
+            "keyword": [
+                "complaints",
+                "consumer",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3g57-mg76",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-01-01T05:00:00Z/2015-07-28T04:00:00Z",
             "theme": [
                 "Consumer"
-            ]
+            ],
+            "title": "Consumer Affairs:  What You Can Do"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3g9g-aft2",
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
-            "identifier": "https://www.data.va.gov/api/views/3g9g-aft2",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM BENEFITS to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA\u2019s determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE OCT2018",
-            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4662,67 +4646,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3g9g-aft2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3g9g-aft2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3g9g-aft2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3g9g-aft2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3g9g-aft2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3g9g-aft2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3g9g-aft2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3g9g-aft2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3g9g-aft2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/3g9g-aft2",
+            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 117"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3g9g-aft2",
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
+            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_Feb_2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-02-01T05:00:00Z/2012-02-29T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program_Feb_2012.doc"
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
-            "identifier": "VA-VBA-INS2012-003",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 02/29/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Face Amount of Life Insurance Coverage by Program by State 2012/02/29",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4730,67 +4708,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3gps-bgbp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3gps-bgbp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3gps-bgbp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3gps-bgbp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3gps-bgbp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3gps-bgbp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3gps-bgbp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3gps-bgbp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3gps-bgbp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-003",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_Feb_2012.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program_Feb_2012.doc"
+            ],
+            "temporal": "2012-02-01T05:00:00Z/2012-02-29T05:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Face Amount of Life Insurance Coverage by Program by State 2012/02/29"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3gui-mbv5",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-08-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-20",
-            "keyword": [
-                "branch of service",
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
-            "identifier": "https://www.data.va.gov/api/views/3gui-mbv5",
             "description": "VetPop2023 branch of service distribution for male Veterans in fiscal years 2024 and 2053",
-            "title": "VetPop2023 Branch of Service Distribution for Male Veterans: FY2024 and 2053",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4798,56 +4780,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3gui-mbv5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3gui-mbv5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3gui-mbv5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3gui-mbv5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3gui-mbv5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3gui-mbv5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3gui-mbv5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3gui-mbv5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3gui-mbv5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/3gui-mbv5",
+            "issued": "2024-08-20",
+            "keyword": [
+                "branch of service",
+                "veterans",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3gui-mbv5",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-20",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 Branch of Service Distribution for Male Veterans: FY2024 and 2053"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3h3h-zutg",
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
-            "title": "Equitable Relief Reports 2001",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4855,48 +4841,43 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3h3h-zutg",
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
+            "title": "Equitable Relief Reports 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/3h48-q527",
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
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/3h48-q527",
             "description": "Data underlying the second figure of Part 1 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 2, Health Care & Disability Comp/Pen over time versus other programs",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4904,129 +4885,128 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3h48-q527/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3h48-q527/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3h48-q527/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3h48-q527/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3h48-q527/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3h48-q527/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3h48-q527/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3h48-q527/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3h48-q527/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/3h48-q527",
+            "issued": "2020-10-06",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3h48-q527",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 2, Health Care & Disability Comp/Pen over time versus other programs"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3hcp-tdvy",
-            "issued": "2023-07-25",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-17",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Oregon FY2021",
+            "identifier": "https://www.data.va.gov/api/views/3hcp-tdvy",
+            "issued": "2023-07-25",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "oregon"
             ],
-            "identifier": "https://www.data.va.gov/api/views/3hcp-tdvy",
+            "landingPage": "https://www.data.va.gov/d/3hcp-tdvy",
+            "modified": "2024-06-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Oregon FY2021",
             "title": "NCVAS State Summary Oregon FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/pension/current_rates_survivor_pen.asp",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Survivors Pension Rate Tables- effective 12/01/13- Pension Service</p>",
+            "identifier": "VA-VBA-INFO-021",
+            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
             "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
             "keyword": [
                 "pension service",
                 "survivors pension",
                 "survivors pension rates",
                 "vba benefits"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
+            "landingPage": "https://www.benefits.va.gov/pension/current_rates_survivor_pen.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-04-18",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-INFO-021",
-            "description": "<p>Survivors Pension Rate Tables- effective 12/01/13- Pension Service</p>",
-            "title": "Survivors Pension Rate Tables- effective 12/01/13- To Present",
-            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Survivors Pension Rate Tables- effective 12/01/13- To Present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Tech_Doc_for_Education_Recipients_by_Training_Type.doc",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-08-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/FY11_Aug_EDU_recp_by_Training_Type.csv"
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
-            "identifier": "VA-VBA-EDU2011-008",
+            "dataQuality": true,
             "description": "<p>FY 2011 Education Recipients by training type  and VA Education Benefit Program (Through August FY11). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2011(Through the August FY11). Training type statistics may include individuals who used their education benefits in more than one training type, therefore the total within this table may be different than the total number of beneficiaries during the fiscal year.</p>",
-            "title": "FY 2011 Use of VA Education Benefits-Recipients by Training Type and VA Education Benefit Program",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5034,50 +5014,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3icb-3epe/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3icb-3epe/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3icb-3epe/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3icb-3epe/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3icb-3epe/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3icb-3epe/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3icb-3epe/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3icb-3epe/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3icb-3epe/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2011-008",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/FY11_Aug_EDU_recp_by_Training_Type.csv"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-08-30T04:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2011 Use of VA Education Benefits-Recipients by Training Type and VA Education Benefit Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3isp-3z26",
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
+            "description": "<p>Defines whether a medical center is accreditated by Joint Commission and/or CARF, and laboratory accreditation.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset3_Hospital_Accreditation_Status.xml",
+                    "mediaType": "application/xml",
+                    "title": "Hospital Accreditation"
+                }
             ],
+            "identifier": "VA-VHA-OIA-038",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -5100,69 +5112,41 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/3isp-3z26",
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
-            "identifier": "VA-VHA-OIA-038",
-            "description": "<p>Defines whether a medical center is accreditated by Joint Commission and/or CARF, and laboratory accreditation.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Hospital Accreditation",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset3_Hospital_Accreditation_Status.xml",
-                    "mediaType": "application/xml",
-                    "title": "Hospital Accreditation"
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
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Hospital Accreditation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3j5n-7ej4",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
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
-            "identifier": "VA-OEI-OEI-79",
             "description": "<p><a href=\"http://www.va.gov/vetdata/docs/SpecialReports/Veteran_Poverty_Trends.pdf\">http://www.va.gov/vetdata/docs/SpecialReports/Veteran_Poverty_Trends.pdf</a></p>",
-            "title": "Veteran Poverty Trends",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5171,46 +5155,45 @@
                     "title": "Veteran Poverty Trends"
                 }
             ],
+            "identifier": "VA-OEI-OEI-79",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3j5n-7ej4",
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
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Veterans in Poverty"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veteran Poverty Trends"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Report.asp",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2010-01-01T05:00:00Z/2010-12-31T05:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "rural",
-                "urban"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-012",
-            "description": "<p>This report uses data from the 2010 American Community Survey to compare the demographic and socioeconomic characteristics of Veterans and non-Veterans who live in rural areas. It also compares rural and urban Veterans. The additional tables provided here show rural Veterans by state for the total population and by period of service.</p>",
-            "title": "Characteristics of Rural Veterans: 2010",
+            "dataQuality": true,
+            "describedBy": "https://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict10.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This report uses data from the 2010 American Community Survey to compare the demographic and socioeconomic characteristics of Veterans and non-Veterans who live in rural areas. It also compares rural and urban Veterans. The additional tables provided here show rural Veterans by state for the total population and by period of service.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5219,45 +5202,46 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict10.pdf",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-012",
+            "issued": "2017-07-26",
+            "keyword": [
+                "rural",
+                "urban"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/Report.asp",
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
+            "temporal": "2010-01-01T05:00:00Z/2010-12-31T05:00:00Z",
             "theme": [
                 "Rural",
                 "Urban"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Characteristics of Rural Veterans: 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3jkq-kgig",
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
-            "identifier": "https://www.data.va.gov/api/views/3jkq-kgig",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist wartime veterans in need whose non-service- connected disabilities are permanent and total preventing them from following a substantially gainful occupation. A Veteran who meets the wartime service requirements is potential eligible if he/she is: \u2022 permanently and totally disabled for reasons not necessarily due to service, \u2022 age 65 or older, or \u2022 is presumed to be totally and permanently disabled for pension purposes because: o he/she is a patient in a nursing home for long-term care due to a disability, or o being disabled, as determined by the Commissioner of Social Security (SS) for purposes of any benefits administered by the Commissioner, such as SS disability benefits or Supplemental Security Income. Income restrictions are prescribed in 38 U.S.C. 1521. Pension is not payable to those whose estates are so large that it is reasonable they use the estate for maintenance. A Veteran meets wartime service requirements if he/she served: \u2022 a total of 90 days or more during one or more periods of war; \u2022 90 or more consecutive days that began or ended during a period of war; or \u2022 for any length of time during a period of war if he/she was discharged or released for a service-connected disability. Veterans entering service after September 7, 1980, must also meet the minimum active duty requirement of 24 months of continuous service or the full period to which the Veteran was called to active duty. (38 U.S.C.5303(A)).</p>",
-            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS OCT2018",
-            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5265,61 +5249,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3jkq-kgig/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3jkq-kgig/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3jkq-kgig/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3jkq-kgig/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3jkq-kgig/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3jkq-kgig/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3jkq-kgig/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3jkq-kgig/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3jkq-kgig/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/3jkq-kgig",
+            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 104"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3jkq-kgig",
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
+            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3k5m-be4n",
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
-            "identifier": "b14692e1-a400-4779-88a0-da2f4fcba4f8",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Alaska FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5327,43 +5311,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "b14692e1-a400-4779-88a0-da2f4fcba4f8",
+            "issued": "2018-10-29",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3k5m-be4n",
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
+            "title": "State Summary Alaska FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3kei-my4p",
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
-            "identifier": "https://www.data.va.gov/api/views/3kei-my4p",
             "description": "This dataset provides within-arm results for continuous measures. Included is information on score means and variance, and pre-post comparisons (pre-post score difference, statistical test p-value, and study-reported effect sizes). Where possible, the within-arm standardized effect size (analog of Cohen\u2019s d) was calculated. For the calculated effect size, negative values indicate a lower score at follow-up compared to baseline, while positive values indicate a higher score at follow-up. Each treatment arm is presented on its own row. There are also separate rows for studies with more than one measure, time point and analysis type.",
-            "title": "PTSD Continuous Outcomes Within Arms",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5371,63 +5355,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3kei-my4p/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3kei-my4p/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3kei-my4p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3kei-my4p/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3kei-my4p/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3kei-my4p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3kei-my4p/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3kei-my4p/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3kei-my4p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "PTSD-Repository"
+            "identifier": "https://www.data.va.gov/api/views/3kei-my4p",
+            "issued": "2023-10-31",
+            "keyword": [
+                "ptsd-repository"
             ],
+            "landingPage": "https://www.data.va.gov/d/3kei-my4p",
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
+            "title": "PTSD Continuous Outcomes Within Arms"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.techstrategies.oit.va.gov/docs/CTSNotes/TS%20Note%20Vol%202%20Issue%209%2009032015%20Post_508.pdf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "encryption",
-                "it"
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
-            "identifier": "VA-OIT-ASD-TSNV2-009",
             "description": "<p>VA Executive Guide to Encryption</p>",
-            "title": "TS Note Vol 2 Issue 9",
-            "programCode": [
-                "029:078"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5436,26 +5419,55 @@
                     "title": "TS Note Vol 2 Issue 9"
                 }
             ],
+            "identifier": "VA-OIT-ASD-TSNV2-009",
+            "issued": "2017-07-26",
+            "keyword": [
+                "encryption",
+                "it"
+            ],
+            "landingPage": "https://www.techstrategies.oit.va.gov/docs/CTSNotes/TS%20Note%20Vol%202%20Issue%209%2009032015%20Post_508.pdf",
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
+            "title": "TS Note Vol 2 Issue 9"
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
-            "temporal": "2016-01-01T05:00:00Z/2016-01-01T05:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR37_012016_Pending_and_EWL_Biweekly_Desired_Date_Division_PDFReady.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 January 2016"
+                }
             ],
+            "identifier": "VA-VHA-OIA-731",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -5469,53 +5481,56 @@
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
-            "identifier": "VA-VHA-OIA-731",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 January 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR37_012016_Pending_and_EWL_Biweekly_Desired_Date_Division_PDFReady.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 January 2016"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2016-01-01T05:00:00Z/2016-01-01T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 January 1"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR32_102015_Completed_Wait_Times_Desired_Date_by_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 30 Sep 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-432",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-09-30T04:00:00Z/2015-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -5529,70 +5544,39 @@
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
-            "identifier": "VA-VHA-OIA-432",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Sep 30",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR32_102015_Completed_Wait_Times_Desired_Date_by_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 30 Sep 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-09-30T04:00:00Z/2015-09-30T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Sep 30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3m94-9zbi",
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
-            "identifier": "def1bc3c-cb84-4067-8986-42506fd836eb",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary North Dakota FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5600,46 +5584,44 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "def1bc3c-cb84-4067-8986-42506fd836eb",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3m94-9zbi",
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
+            "title": "State Summary North Dakota FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3mzd-rie4",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2022-09-15",
-            "temporal": "2021 - 2022",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-21",
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
-            "identifier": "https://www.data.va.gov/api/views/3mzd-rie4",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) data from the 2021 & 2022 AES administrations. Scores are provided at the station level and up, and the occupation level within hospitals.",
-            "title": "All Employee Survey (AES) 2021 - 2022",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5647,41 +5629,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3mzd-rie4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3mzd-rie4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3mzd-rie4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3mzd-rie4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3mzd-rie4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3mzd-rie4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3mzd-rie4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3mzd-rie4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3mzd-rie4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/3mzd-rie4",
+            "issued": "2022-09-15",
+            "keyword": [
+                "engagement",
+                "satisfaction",
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3mzd-rie4",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-03-21",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2021 - 2022",
+            "title": "All Employee Survey (AES) 2021 - 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3ny5-ne96",
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
+            "description": "The PTSD Repository includes 550 studies. This story describes the participants in these clinical trials.",
+            "identifier": "https://www.data.va.gov/api/views/3ny5-ne96",
             "issued": "2020-06-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
             "keyword": [
                 "demographic",
                 "ptsd-repository",
@@ -5689,56 +5693,32 @@
                 "sample",
                 "study participant"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for PTSD",
-                "hasEmail": "mailto:ncptsd@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/3ny5-ne96",
+            "modified": "2020-06-11",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for PTSD"
             },
-            "identifier": "https://www.data.va.gov/api/views/3ny5-ne96",
-            "description": "The PTSD Repository includes 550 studies. This story describes the participants in these clinical trials.",
-            "title": "Who has been studied in PTSD clinical trials?",
-            "programCode": [
-                "029:000"
-            ],
-            "accrualPeriodicity": "R/P1Y"
+            "rights": "All data is within the public domain and is currently available for download.",
+            "title": "Who has been studied in PTSD clinical trials?"
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
-            "identifier": "VA-VBA-ABR2012-005",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Beneficiaries Receiving DIC by Relationship at the End of Fiscal Year 2012 - ABR 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5746,47 +5726,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-005",
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
+            "title": "Beneficiaries Receiving DIC by Relationship at the End of Fiscal Year 2012 - ABR 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3q6m-6385",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "benefits",
-                "compensation",
-                "health",
-                "utilization",
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
-            "identifier": "VA-OEI-OEI-158",
             "description": "<p>The report provides demographic, socio-economic, and utilization trends of Veterans who used at least one VA benefit or service each year between FY 2005 and FY 2014. It also includes a comparison of Veterans who used VA benefits to Veterans who did not use VA benefits.</p>",
-            "title": "Unique Veteran Users Report FY 2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5795,42 +5775,46 @@
                     "title": "Unique Veteran Users Report FY 2014"
                 }
             ],
+            "identifier": "VA-OEI-OEI-158",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "compensation",
+                "health",
+                "utilization",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3q6m-6385",
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
+            "title": "Unique Veteran Users Report FY 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3si5-i8fy",
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
-            "identifier": "https://www.data.va.gov/api/views/3si5-i8fy",
+            "dataQuality": true,
             "description": "<p>VBA COMPENSTATION BENEFITS PRGOGRAM to provide vocational training and rehabilitation to certain children born with spina bifida or other covered birth defects who are children of Vietnam veterans and some Korean veterans. \u201cA child born with spina bifida or other covered birth defects, except spina bifida occulta, who is the natural child of a Vietnam veteran and some Korean veterans, regardless of the age or marital status of the child, conceived after the date on which the veteran first served in the Republic of Vietnam during the Vietnam era and in particular areas near the DMZ in the Korean conflict. VA must also determine that it is feasible for the child to achieve a vocational goal.\u201d</p>",
-            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA MAY2019",
-            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5838,62 +5822,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3si5-i8fy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3si5-i8fy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3si5-i8fy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3si5-i8fy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3si5-i8fy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3si5-i8fy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3si5-i8fy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3si5-i8fy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3si5-i8fy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/3si5-i8fy",
+            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 127"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3si5-i8fy",
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
+            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-07-01T04:00:00Z/2014-09-30T04:00:00Z",
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
-            "identifier": "VA-OM-OM-117",
             "description": "<p>FY 2014 Fourth Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2014 Fourth Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5902,44 +5884,42 @@
                     "title": "FY 2014 Fourth Quarter High-Dollar Overpayments Report"
                 }
             ],
+            "identifier": "VA-OM-OM-117",
+            "issued": "2017-07-26",
+            "keyword": [
+                "improper payments",
+                "overpayments"
+            ],
+            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-07-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "financial"
-            ]
+            ],
+            "title": "FY 2014 Fourth Quarter High-Dollar Overpayments Report"
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
-            "identifier": "VA-VBA-ABR2012-026",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Service Connected Disabilities by Body System for Veterans Who Began Receiving Compensation by FY",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5947,44 +5927,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-026",
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
+            "title": "Service Connected Disabilities by Body System for Veterans Who Began Receiving Compensation by FY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3srd-2266",
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
-            "identifier": "0b0df186-9da8-4b43-bc42-75b7788129aa",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Connecticut FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5992,8 +5976,22 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "0b0df186-9da8-4b43-bc42-75b7788129aa",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3srd-2266",
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
@@ -6001,19 +5999,25 @@
                 "Demographics",
                 "Socioeconomics",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Connecticut FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/3thx-6ke2",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Data sharing agreements contained in Repository may contain sensitive information",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The VHA Data Sharing Agreement Repository serves as a centralized location to collect and report on agreements that share VHA data with entities outside of VA. It  provides senior management an overall view of existing data sharing agreements; fosters productive sharing of health information with VHA's external partners;  and streamlines data acquisition to improve data management responsibilities overall. Agreements that VHA has established with entities within the VA are not candidates for this Repository.</p>",
+            "identifier": "VA-VHA-OIA-062",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-04-01T04:00:00Z/2014-08-19T04:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "data sharing agreement",
                 "dua",
@@ -6022,59 +6026,39 @@
                 "mou",
                 "swrl"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/3thx-6ke2",
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
-            "identifier": "VA-VHA-OIA-062",
-            "description": "<p>The VHA Data Sharing Agreement Repository serves as a centralized location to collect and report on agreements that share VHA data with entities outside of VA. It  provides senior management an overall view of existing data sharing agreements; fosters productive sharing of health information with VHA's external partners;  and streamlines data acquisition to improve data management responsibilities overall. Agreements that VHA has established with entities within the VA are not candidates for this Repository.</p>",
-            "title": "VHA Data Sharing Agreement Repository",
-            "programCode": [
-                "029:080"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1D",
+            "rights": "Data sharing agreements contained in Repository may contain sensitive information",
+            "temporal": "2014-04-01T04:00:00Z/2014-08-19T04:00:00Z",
             "theme": [
                 "Data Use Agreements"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VHA Data Sharing Agreement Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/3tty-97k5",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "transport"
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
-            "identifier": "a9c94f1a-f9ab-4d74-a2e0-d5490479cf82",
+            "dataQuality": true,
             "description": "<p>DAS receives and routes data both from external and internal VA sources and provides to intended consumers according to business rules.</p>",
-            "title": "Transport",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6083,19 +6067,48 @@
                     "title": "Transport"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "a9c94f1a-f9ab-4d74-a2e0-d5490479cf82",
+            "issued": "2018-02-23",
+            "keyword": [
+                "transport"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3tty-97k5",
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
+            "title": "Transport"
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
+                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX_FY06_Rev_090409.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-032",
             "issued": "2017-07-26",
-            "temporal": "2005-10-01T04:00:00Z/2006-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -6109,66 +6122,37 @@
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
-            "identifier": "VA-OEI-OEI-032",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2006",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX_FY06_Rev_090409.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2005-10-01T04:00:00Z/2006-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3u66-fxug",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-10-28",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-08",
-            "keyword": [
-                "national cemetery administration - gravesite locator"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCAOpendataGroup",
                 "hasEmail": "mailto:NCAOpendataGroup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/3u66-fxug",
             "description": "Data provided by the National Cemetery Administration for grave locations of Veterans and loved ones.",
-            "title": "National Cemetery Administration - Gravesite Locator",
-            "programCode": [
-                "029:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6176,57 +6160,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3u66-fxug/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3u66-fxug/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3u66-fxug/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3u66-fxug/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3u66-fxug/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3u66-fxug/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3u66-fxug/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3u66-fxug/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3u66-fxug/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/3u66-fxug",
+            "issued": "2022-10-28",
+            "keyword": [
+                "national cemetery administration - gravesite locator"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3u66-fxug",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-11-08",
+            "programCode": [
+                "029:004"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "National Cemetery Administration - Gravesite Locator"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3u7x-kehu",
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
-            "identifier": "https://www.data.va.gov/api/views/3u7x-kehu",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to encourage membership in units of the Selected Reserve of the Ready Reserve and to provide educational assistance to members of the reserve components called or ordered to active service in response to a war or national emergency declared by the President or Congress. Generally, to qualify for benefits under MGIB-SR you must (1) Have a six-year obligation to serve in the Selected Reserve signed after June 30, 1985. If you are an officer, you must have agreed to serve six years in addition to your original obligation. For some types of training, it is necessary to have a six-year commitment that begins after September 30, 1990; (2) Complete your initial active duty for training (IADT); (3) Meet the requirement to receive a high school diploma or equivalency certificate before completing IADT. You may not use 12 hours toward a college degree to meet this requirement; and (4) Remain in good standing while serving in an active Selected Reserve unit. Generally, to qualify for benefits under REAP you must have served at least 90 consecutive days on active duty as a result of a call or order to active duty from a reserve component in response to a war or national emergency declared by the President or Congress. This is not a complete list of eligibility requirements. For more information on MGIB-SR and REAP visit <a href=\"http://www.gibill.va.gov\">http://www.gibill.va.gov</a>.</p>",
-            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM JAN2019",
-            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6234,61 +6218,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3u7x-kehu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3u7x-kehu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3u7x-kehu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3u7x-kehu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3u7x-kehu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3u7x-kehu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3u7x-kehu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3u7x-kehu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3u7x-kehu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/3u7x-kehu",
+            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 032"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3u7x-kehu",
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
+            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cfm.va.gov/consulting/tech.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-01-08T05:00:00Z/2014-10-20T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "construction project management consulting support service technical topics"
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
-            "identifier": "VA-CFM-TechTopics-0015",
+            "dataQuality": true,
             "description": "<p>The Consulting Support Service's staff of architectural and engineering professionals has written brief papers discussing approaches to frequently encountered problems.</p>",
-            "title": "Technical Topics CFM",
-            "programCode": [
-                "029:090"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6297,48 +6282,44 @@
                     "title": "Technical Topics CFM"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-CFM-TechTopics-0015",
+            "issued": "2017-07-26",
+            "keyword": [
+                "construction project management consulting support service technical topics"
+            ],
+            "landingPage": "https://www.cfm.va.gov/consulting/tech.asp",
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
+            "temporal": "2014-01-08T05:00:00Z/2014-10-20T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Technical Topics CFM"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3umk-24vq",
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
-            "identifier": "https://www.data.va.gov/api/views/3umk-24vq",
             "description": "Percent Users vs Non-Users Distribution by Era - Males. Data underlying the fourth figure of Part 2 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 12, Percent Users vs Non-Users Distribution by Era - Males",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6346,92 +6327,93 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3umk-24vq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3umk-24vq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3umk-24vq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/3umk-24vq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3umk-24vq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3umk-24vq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/3umk-24vq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/3umk-24vq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/3umk-24vq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/3umk-24vq",
+            "issued": "2020-11-18",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3umk-24vq",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-12-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 12, Percent Users vs Non-Users Distribution by Era - Males"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/3vge-s486",
-            "issued": "2019-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-30",
-            "keyword": [
-                "outpatient",
-                "veterans health"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Beth Lamb",
                 "hasEmail": "mailto:beth.lamb@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/3vge-s486",
             "description": "VA analyzes what Veterans are saying about their outpatient experiences (including mental health, primary care, optometry, physical therapy, cardiology, etc.), and levels of outpatient ease, effectiveness, and emotion are anticipated to drive increases in outpatient trust using Veterans Signal survey technology.",
-            "title": "Key Indicators for Veterans Signals VHA Outpatient Survey",
+            "identifier": "https://www.data.va.gov/api/views/3vge-s486",
+            "issued": "2019-09-10",
+            "keyword": [
+                "outpatient",
+                "veterans health"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3vge-s486",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-01-30",
             "programCode": [
                 "029:000"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Key Indicators for Veterans Signals VHA Outpatient Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/3wha-bjgm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2005-10-01T04:00:00Z/2006-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-09-16",
-            "references": [
-                "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY06_Technical_Notes.doc"
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
-            "identifier": "VA-OEI-OEI-010",
-            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
-            "title": "Veterans Affairs Geographic Distribution of Expenditures FY06 by Congressional District",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY06_Technical_Notes.doc",
             "describedByType": "application/msword",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6440,50 +6422,49 @@
                     "title": "csv"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY06_Technical_Notes.doc",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-010",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3wha-bjgm",
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
+                "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY06_Technical_Notes.doc"
+            ],
+            "temporal": "2005-10-01T04:00:00Z/2006-09-30T04:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Affairs Geographic Distribution of Expenditures FY06 by Congressional District"
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
@@ -6491,47 +6472,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
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
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/3xjc-4g5r",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-17",
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
-            "identifier": "1bfda2fc-40cd-41bc-b78c-1f00ef676a6c",
+            "dataQuality": true,
             "description": "<p>Provides single sign-on solution for external facing VA applications. Authenticates users with CSP credentials and other externally-issued credentials (including mapping of credential to VA identity) (IBM tools)</p>",
-            "title": "Single Sign On External (SSOe)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6540,22 +6522,52 @@
                     "title": "Single Sign On External (SSOe)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "1bfda2fc-40cd-41bc-b78c-1f00ef676a6c",
+            "issued": "2018-02-23",
+            "keyword": [
+                "access",
+                "identity",
+                "security"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3xjc-4g5r",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-17",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Single Sign On External (SSOe)"
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
-            "temporal": "2015-03-01T05:00:00Z/2015-03-01T05:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/15_March_2015_Pending_04022015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 March 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-100",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -6569,80 +6581,45 @@
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
-            "identifier": "VA-VHA-OIA-100",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Mar 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/15_March_2015_Pending_04022015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 March 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-03-01T05:00:00Z/2015-03-01T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Mar 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.bva.va.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.bva.va.gov"
-            ],
-            "keyword": [
-                "appeals",
-                "appeals process",
-                "board hearings",
-                "bva",
-                "bva decisions",
-                "chairman s annual reports to congress",
-                "veterans law review"
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
-            "identifier": "VA-BVA-BVA-003",
+            "dataQuality": true,
+            "describedBy": "https://www.bva.va.gov",
             "description": "<p>The Board of Veterans' Appeals (also known as 'BVA' or 'the Board') is a part of the VA, located in Washington, D.C.Members of the Board review benefit claims determinations made by local VA offices and issue decision on appeals. These Law Judges, attorneys experienced in veterans law and in reviewing benefit claims, are the only ones who can issue Board decisions. Staff attorneys, also trained in veterans law, review the facts of each appeal and assist the Board members.   {38 U.S.C. \u00ef\u00bf\u00bd\u00ef\u00bf\u00bd 7103, 7104}</p>",
-            "title": "Board of Veterans' Appeals",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6651,47 +6628,53 @@
                     "title": "Board of Veterans' Appeals"
                 }
             ],
-            "describedBy": "https://www.bva.va.gov",
-            "dataQuality": true,
+            "identifier": "VA-BVA-BVA-003",
+            "issued": "2017-07-26",
+            "keyword": [
+                "appeals",
+                "appeals process",
+                "board hearings",
+                "bva",
+                "bva decisions",
+                "chairman s annual reports to congress",
+                "veterans law review"
+            ],
+            "landingPage": "https://www.bva.va.gov",
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
+            "references": [
+                "https://www.bva.va.gov"
+            ],
+            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Section 5.  Law Enforcement",
                 "Courts",
                 "and Prisons"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Board of Veterans' Appeals"
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
-            "identifier": "VA-OGC-008",
             "description": "<p>Reliance on State Law to Determine Validity of Same-Sex Marriage</p>",
-            "title": "OGC Precedent Opinion 4-2014",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6700,75 +6683,76 @@
                     "title": "VAOGCPREC 4-2014"
                 }
             ],
+            "identifier": "VA-OGC-008",
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
+            "title": "OGC Precedent Opinion 4-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/3yu2-gqbk",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-21",
-            "keyword": [
-                "new jersey",
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
-            "identifier": "https://www.data.va.gov/api/views/3yu2-gqbk",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_New Jersey",
+            "identifier": "https://www.data.va.gov/api/views/3yu2-gqbk",
+            "issued": "2021-08-26",
+            "keyword": [
+                "new jersey",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/3yu2-gqbk",
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
+            "title": "State Summaries_New Jersey"
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
-            "temporal": "2010-01-01T05:00:00Z/2010-03-31T04:00:00Z",
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
-            "identifier": "VA-OM-OM-094",
+            "dataQuality": true,
             "description": "<p>FY 2010 Second Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2010 Second Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6777,43 +6761,43 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-094",
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
+            "temporal": "2010-01-01T05:00:00Z/2010-03-31T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2010 Second Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/437j-pam6",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc"
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
-            "identifier": "VA-OGC-024",
             "description": "<p>02 Regulations Rulemaking Performance Report</p>",
-            "title": "Rulemaking Performance Report",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6822,43 +6806,41 @@
                     "title": "Rulemaking Performance Report"
                 }
             ],
+            "identifier": "VA-OGC-024",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc"
+            ],
+            "landingPage": "https://www.data.va.gov/d/437j-pam6",
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
+            "title": "Rulemaking Performance Report"
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
-                "american community survey",
-                "veteran",
-                "vietnam",
-                "vietnam war"
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
-            "identifier": "VA-OEI-OEI-166",
+            "dataQuality": true,
             "description": "<p>This report uses data from the 2014 American Community Survey and shows the demographic and socioeconomic characteristics of Veterans who belong to the Vietnam Veteran cohort. The spreadsheet includes variables like: raw numbers, gender, education, median personal income, age groups, and other variables.</p>",
-            "title": "Vietnam Veterans by State:  2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6867,42 +6849,44 @@
                     "title": "Vietnam Veterans by State:\u00a0 2014"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-166",
+            "issued": "2017-07-26",
+            "keyword": [
+                "american community survey",
+                "veteran",
+                "vietnam",
+                "vietnam war"
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
                 "Demographics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Vietnam Veterans by State:  2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/43uz-e9hr",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-11-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-11-10",
-            "keyword": [
-                "veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/43uz-e9hr",
             "description": "Projected living Veterans from VetPop",
-            "title": "Projected Living Veterans, 9/30/2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6910,57 +6894,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/43uz-e9hr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/43uz-e9hr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/43uz-e9hr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/43uz-e9hr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/43uz-e9hr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/43uz-e9hr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/43uz-e9hr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/43uz-e9hr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/43uz-e9hr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/43uz-e9hr",
+            "issued": "2021-11-10",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/43uz-e9hr",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-11-10",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Projected Living Veterans, 9/30/2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/43zv-9vme",
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
-            "identifier": "https://www.data.va.gov/api/views/43zv-9vme",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE MAR2019",
-            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6968,64 +6953,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/43zv-9vme/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/43zv-9vme/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/43zv-9vme/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/43zv-9vme/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/43zv-9vme/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/43zv-9vme/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/43zv-9vme/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/43zv-9vme/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/43zv-9vme/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/43zv-9vme",
+            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "issued": "2019-03-20",
+            "keyword": [
+                "cdfa 64.124"
+            ],
+            "landingPage": "https://www.data.va.gov/d/43zv-9vme",
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
+            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE MAR2019"
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
-            "temporal": "2003-01-01T05:00:00Z/2003-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-016",
+            "dataQuality": true,
             "description": "<p>2003 VA Performance and Accountability Report.</p>",
-            "title": "2003 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7034,44 +7017,44 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-016",
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
+            "temporal": "2003-01-01T05:00:00Z/2003-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2003 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/45h5-7g2h",
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
-            "identifier": "VA-OM-OM-178",
             "description": "<p>COIN 145 report  for June 2016</p>",
-            "title": "COIN 145 report  for June 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7080,40 +7063,40 @@
                     "title": "COIN 145 June 2016"
                 }
             ],
+            "identifier": "VA-OM-OM-178",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/45h5-7g2h",
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
+            "title": "COIN 145 report  for June 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/46j5-9dq5",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2020-06-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
-            "keyword": [
-                "ncptsd",
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
-            "identifier": "https://www.data.va.gov/api/views/46j5-9dq5",
             "description": "Definitions of abbreviations found throughout the PTSD-Repository.",
-            "title": "Abbreviations",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7121,43 +7104,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/46j5-9dq5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/46j5-9dq5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/46j5-9dq5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/46j5-9dq5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/46j5-9dq5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/46j5-9dq5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/46j5-9dq5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/46j5-9dq5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/46j5-9dq5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/46j5-9dq5",
+            "issued": "2020-06-04",
+            "keyword": [
+                "ncptsd",
+                "ptsd"
+            ],
+            "landingPage": "https://www.data.va.gov/d/46j5-9dq5",
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
+            "title": "Abbreviations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/46q6-zer4",
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
+            "description": "<p>The National Prosthetics Patient Database (NPPD) established a central database of Prosthetics data recorded at each Veterans Health Administration facility. Its objective was to enable clinical reviews to increase quality, reduce costs, and improve efficiency of the Prosthetics program. Increase the quality of the services to our Veterans by providing a means to develop consistency in services, review prescription and management practices, develop training, monitor Home Medical Equipment, and measure performance improvements. Reduce costs by comparing costs system-wide, identifying common items for consolidated contracting, identifying costs for Medical Cost Care Funds (MCCF) purposes and improving contracting cost benefit. Improve efficiency by validating the data, improving budget management, determining where coding errors occur, providing training, and comparing unique social security numbers for multiple site usage and item issue. The NPPD Menu provides patient information, patient eligibility, Prosthetic treatment, date of provision, cost, vendor, and purchasing agent information. This system tracks average cost data and its usage and provides on both a monthly and quarterly basis detailed and summary reports by station, Veterans Integrated Service Network (VISN) and agency. The NPPD Menu resides in Veterans Health Information Systems and Technology Architecture (VistA) at the medical center level. This data is updated quarterly. Data is rolled up at each facility and transmitted to Hines. The data is then loaded into the Corporate Data Warehouse (CDW) from which data extracts are done. The data is also put into a ProClarity cube and is available to VA local, regional, and national managers online. National managers have the ability to properly monitor, oversee and manage the national program and regional managers are able to effectively manage their respective areas using this tool. The primary purpose of this database is to provide financial and clinical oversight of the Prosthetics program and is used primarily by the Prosthetics and Sensory Aids (PSA) including VISN staff, VISN Prosthetics Representatives, Prosthetics Program Managers and other Prosthetics staff.</p>",
+            "identifier": "VA-VHA-PL-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1997-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "aids",
                 "cost",
@@ -7168,60 +7171,40 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/46q6-zer4",
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
-            "identifier": "VA-VHA-PL-002",
-            "description": "<p>The National Prosthetics Patient Database (NPPD) established a central database of Prosthetics data recorded at each Veterans Health Administration facility. Its objective was to enable clinical reviews to increase quality, reduce costs, and improve efficiency of the Prosthetics program. Increase the quality of the services to our Veterans by providing a means to develop consistency in services, review prescription and management practices, develop training, monitor Home Medical Equipment, and measure performance improvements. Reduce costs by comparing costs system-wide, identifying common items for consolidated contracting, identifying costs for Medical Cost Care Funds (MCCF) purposes and improving contracting cost benefit. Improve efficiency by validating the data, improving budget management, determining where coding errors occur, providing training, and comparing unique social security numbers for multiple site usage and item issue. The NPPD Menu provides patient information, patient eligibility, Prosthetic treatment, date of provision, cost, vendor, and purchasing agent information. This system tracks average cost data and its usage and provides on both a monthly and quarterly basis detailed and summary reports by station, Veterans Integrated Service Network (VISN) and agency. The NPPD Menu resides in Veterans Health Information Systems and Technology Architecture (VistA) at the medical center level. This data is updated quarterly. Data is rolled up at each facility and transmitted to Hines. The data is then loaded into the Corporate Data Warehouse (CDW) from which data extracts are done. The data is also put into a ProClarity cube and is available to VA local, regional, and national managers online. National managers have the ability to properly monitor, oversee and manage the national program and regional managers are able to effectively manage their respective areas using this tool. The primary purpose of this database is to provide financial and clinical oversight of the Prosthetics program and is used primarily by the Prosthetics and Sensory Aids (PSA) including VISN staff, VISN Prosthetics Representatives, Prosthetics Program Managers and other Prosthetics staff.</p>",
-            "title": "National Prosthetic Patient Database (NPPD (Prosthetics & Sensory Aids Service))",
-            "programCode": [
-                "029:052"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1997-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Prosthetic Patient Database (NPPD (Prosthetics & Sensory Aids Service))"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/47kg-5zwf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "veterans",
-                "virginia"
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
-            "identifier": "VA-OEI-OEI-133",
             "description": "<p>This is a summary of the programs and services provided by VA in Virginia in fiscal year 2014.</p>",
-            "title": "State Summary:  Virginia",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7230,26 +7213,49 @@
                     "title": "State Summary:  Virginia"
                 }
             ],
+            "identifier": "VA-OEI-OEI-133",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans",
+                "virginia"
+            ],
+            "landingPage": "https://www.data.va.gov/d/47kg-5zwf",
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
+            "title": "State Summary:  Virginia"
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
+            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- January 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING012014-028",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 030",
                 "face amount",
@@ -7258,43 +7264,41 @@
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
-            "identifier": "VA-VBA-USASPENDING012014-028",
-            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- January 2014.</p>",
-            "title": "USA Spending file- 01/2014-New Life Insurance Policies-Insurance -  CFDA 64.030",
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
+            "title": "USA Spending file- 01/2014-New Life Insurance Policies-Insurance -  CFDA 64.030"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/47vy-pcre",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act protected health information",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Following the death of a Veteran by suicide, BHAP receives post-mortem medical data and interviewee contact information from VHA suicide prevention coordinators. Data include relevant historical activities and related medical concerns as reviewed in the Veteran's medical record. Interviewees typically include a Veteran's family or close friends. Interviewee data includes behavioral information about the Veteran prior to their death. Data are collected at the VISN 2 Center of Excellence for Suicide Prevention and are cleaned, processed, and managed by statistical staff and program analysts on behalf of Mental Health Services.</p>",
+            "identifier": "VA-VHA-10N-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2001-01-01T05:00:00Z/2014-10-01T04:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "behavior",
                 "health",
@@ -7304,72 +7308,44 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/47vy-pcre",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:044"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-10N-002",
-            "description": "<p>Following the death of a Veteran by suicide, BHAP receives post-mortem medical data and interviewee contact information from VHA suicide prevention coordinators. Data include relevant historical activities and related medical concerns as reviewed in the Veteran's medical record. Interviewees typically include a Veteran's family or close friends. Interviewee data includes behavioral information about the Veteran prior to their death. Data are collected at the VISN 2 Center of Excellence for Suicide Prevention and are cleaned, processed, and managed by statistical staff and program analysts on behalf of Mental Health Services.</p>",
-            "title": "Behavioral Health Autopsy Program (BHAP)",
-            "programCode": [
-                "029:044"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "rights": "Health Insurance Portability and Accountability Act protected health information",
+            "temporal": "2001-01-01T05:00:00Z/2014-10-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Behavioral Health Autopsy Program (BHAP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/48gk-v6n8",
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
-            "identifier": "VA-VHA-OIA-029",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset defines if the facility has met the Joint Commission Patient Safety Standards and in which year they were surveyed.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Patient Safety",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset defines if the facility has met the Joint Commission Patient Safety Standards and in which year they were surveyed.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7377,48 +7353,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/48gk-v6n8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/48gk-v6n8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/48gk-v6n8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/48gk-v6n8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/48gk-v6n8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/48gk-v6n8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/48gk-v6n8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/48gk-v6n8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/48gk-v6n8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-029",
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
+            "landingPage": "https://www.data.va.gov/d/48gk-v6n8",
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
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Patient Safety"
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
+                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX-Hybrid-FY2002-RPD.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-028",
             "issued": "2017-07-26",
-            "temporal": "2001-10-01T04:00:00Z/2002-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -7432,52 +7445,51 @@
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
-            "identifier": "VA-OEI-OEI-028",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2002",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX-Hybrid-FY2002-RPD.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2001-10-01T04:00:00Z/2002-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2002"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN17FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 17 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-089",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -7493,103 +7505,75 @@
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
-            "identifier": "VA-VHA-OIA-089",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 17",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN17FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 17 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 17"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4ak8-sc7y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located</p>",
-            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS FY2019",
+            "identifier": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 118"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4ak8-sc7y",
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
+            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4ap7-kxhw",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "delaware"
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
-            "identifier": "VA-OEI-OEI-177",
             "description": "<p>This summary describes the programs and services VA provided in Delaware in fiscal year 2015.</p>",
-            "title": "State Summary: Delaware",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7598,54 +7582,40 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-177",
+            "issued": "2017-07-26",
+            "keyword": [
+                "delaware"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4ap7-kxhw",
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
+            "title": "State Summary: Delaware"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4aqx-2ch4",
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
-            "identifier": "https://www.data.va.gov/api/views/4aqx-2ch4",
             "description": "A subset of the FY13 National Veteran Health Equity Report, filtered by geography.\n\nThe National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. Specifically, this report is designed to provide basic comparative information on the sociodemographics, utilization patterns and rates of diagnosed health conditions among the groups over which the VHA Office of Health Equity (OHE) has responsibility with respect to monitoring, evaluating and acting on identified disparities in access, use, care, quality and outcomes. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.",
-            "title": "VA-OHE-NVHER-FY13-Diagnoses-Geography",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7653,57 +7623,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4aqx-2ch4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4aqx-2ch4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4aqx-2ch4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/4aqx-2ch4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4aqx-2ch4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4aqx-2ch4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4aqx-2ch4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4aqx-2ch4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4aqx-2ch4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4ayu-6n82",
-            "bureauCode": [
-                "029:00"
-            ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
+            "identifier": "https://www.data.va.gov/api/views/4aqx-2ch4",
+            "issued": "2019-11-12",
             "keyword": [
+                "age",
                 "demographics",
-                "veterans"
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
+            "landingPage": "https://www.data.va.gov/d/4aqx-2ch4",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA-OHE-NVHER-FY13-Diagnoses-Geography"
+        },
+        {
+            "@type": "dcat:Dataset",
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
-            "identifier": "7056fcee-7a48-4e2f-a4cc-3f6afaa7ff76",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Louisiana FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7711,43 +7695,44 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "7056fcee-7a48-4e2f-a4cc-3f6afaa7ff76",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4ayu-6n82",
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
+            "title": "State Summary Louisiana FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4cvs-huag",
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
-            "identifier": "https://www.data.va.gov/api/views/4cvs-huag",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) items also on Federal Employee Viewpoint Survey, reported as percents as required per Federal statute.",
-            "title": "AES 2022 FEVS Percents",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7755,81 +7740,99 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/4cvs-huag",
+            "issued": "2023-03-16",
+            "keyword": [
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4cvs-huag",
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
+            "title": "AES 2022 FEVS Percents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/4etu-y7d8",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Delaware FY2023",
+            "identifier": "https://www.data.va.gov/api/views/4etu-y7d8",
             "issued": "2024-05-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "de",
                 "fy2024 data",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/4etu-y7d8",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/4etu-y7d8",
-            "description": "NCVAS State Summary Delaware FY2023",
-            "title": "NCVAS State Summary Delaware FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Delaware FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4ezr-vay8",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE FY2019",
+            "identifier": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 120"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4ezr-vay8",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:003"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/4g5p-v8ys",
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
+            "description": "<p>Dental Encounter System (DES) is an automated health care application designed to capture critical data about the operations of VA Dental Services. Information on completed procedures is gathered for each patient encounter through the Dental Record Manager software, which is a VA Computerized Patient Record System Class I adjunct application. This DES information is linked and includes encounter date, patient, provider, procedures, diagnosis codes, and additional associated qualifiers. DES productivity is measured using weighted work units known as relative value units (RVUs). RVU values are determined cooperatively by the Dental Coding Committee and Decision Support System (DSS) staff. One RVU is a measure of work effort and represents one minute of the average provider's time (presuming the provider is supported with one dental assistant and one treatment room) and is reported as a value with each procedure reported to DES. DES transactions are sent to the Austin Information Technology Center (AITC) database using standard Health Level Seven (HL7) messaging and the VA Vitria Interface Engine. These batched HL7 messages are parsed at the AITC and placed in a flat database file.</p>",
+            "identifier": "VA-VHA-PCS-004",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2002-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "dental",
                 "dentist",
@@ -7841,61 +7844,41 @@
                 "veteran",
                 "vista"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/4g5p-v8ys",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:051"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PCS-004",
-            "description": "<p>Dental Encounter System (DES) is an automated health care application designed to capture critical data about the operations of VA Dental Services. Information on completed procedures is gathered for each patient encounter through the Dental Record Manager software, which is a VA Computerized Patient Record System Class I adjunct application. This DES information is linked and includes encounter date, patient, provider, procedures, diagnosis codes, and additional associated qualifiers. DES productivity is measured using weighted work units known as relative value units (RVUs). RVU values are determined cooperatively by the Dental Coding Committee and Decision Support System (DSS) staff. One RVU is a measure of work effort and represents one minute of the average provider's time (presuming the provider is supported with one dental assistant and one treatment room) and is reported as a value with each procedure reported to DES. DES transactions are sent to the Austin Information Technology Center (AITC) database using standard Health Level Seven (HL7) messaging and the VA Vitria Interface Engine. These batched HL7 messages are parsed at the AITC and placed in a flat database file.</p>",
-            "title": "Dental Encounter System (DES)",
-            "programCode": [
-                "029:051"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2002-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Dental Encounter System (DES)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4gki-4yui",
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
-            "identifier": "VA-OGC-020",
             "description": "<p>Review of Prior Decisions Involving Military Sexual Trauma  Author: Griffin, B.</p>",
-            "title": "OGC Precedent Opinion 3-2012",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7904,46 +7887,43 @@
                     "title": "OGC Precedent Opinion 3-2012"
                 }
             ],
+            "identifier": "VA-OGC-020",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4gki-4yui",
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
+            "title": "OGC Precedent Opinion 3-2012"
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
-            "identifier": "VA-VBA-ABR2012-126",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA business lines.</p>",
-            "title": "Virginia-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7951,73 +7931,71 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-126",
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
+            "title": "Virginia-FY12 Benefits Summary"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4gqv-ddx7",
-            "issued": "2023-10-19",
             "@type": "dcat:Dataset",
-            "modified": "2023-11-13",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sharon Ennis",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "Veterans Day 2023 data story which examines trends in branch of service from FY 2000 to 2023.",
+            "identifier": "https://www.data.va.gov/api/views/4gqv-ddx7",
+            "issued": "2023-10-19",
             "keyword": [
                 "branch of service",
                 "veterans day"
             ],
-            "identifier": "https://www.data.va.gov/api/views/4gqv-ddx7",
+            "landingPage": "https://www.data.va.gov/d/4gqv-ddx7",
+            "modified": "2023-11-13",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Veterans Day 2023 data story which examines trends in branch of service from FY 2000 to 2023.",
             "title": "Veterans Day 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Enrollment_by_State_as_of_June_2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-06-01T04:00:00Z/2012-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State.doc"
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
-            "identifier": "VA-VBA-INS2012-010",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of June 30, 2012.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "Number of Veterans Insured by VGLI by State as of June 30, 2012",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8025,72 +8003,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4gsg-vwvm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4gsg-vwvm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4gsg-vwvm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/4gsg-vwvm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4gsg-vwvm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4gsg-vwvm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4gsg-vwvm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4gsg-vwvm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4gsg-vwvm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-010",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Enrollment_by_State_as_of_June_2012.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State.doc"
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
+            "title": "Number of Veterans Insured by VGLI by State as of June 30, 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4h2b-2rwm",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2021-01-13",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-04",
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
-            "identifier": "https://www.data.va.gov/api/views/4h2b-2rwm",
             "description": "This is number 3 of 3 data sets that accompany Data Set for Maps Data Story on VA's Open Data Site.\nSpecifically this identifies zip codes where VA facilities could perform benefits examinations during phase 3.\nData was acquired October 2020.",
-            "title": "PAI Data Set For Maps Data Story 3 of 3",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8098,81 +8075,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4h2b-2rwm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4h2b-2rwm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4h2b-2rwm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/4h2b-2rwm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4h2b-2rwm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4h2b-2rwm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4h2b-2rwm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4h2b-2rwm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4h2b-2rwm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/4h2b-2rwm",
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
+            "landingPage": "https://www.data.va.gov/d/4h2b-2rwm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-04",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "PAI Data Set For Maps Data Story 3 of 3"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4h6y-dvd2",
-            "issued": "2023-06-19",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Connecticut FY2021",
+            "identifier": "https://www.data.va.gov/api/views/4h6y-dvd2",
+            "issued": "2023-06-19",
             "keyword": [
                 "connecticut",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/4h6y-dvd2",
+            "landingPage": "https://www.data.va.gov/d/4h6y-dvd2",
+            "modified": "2024-05-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Connecticut FY2021",
             "title": "NCVAS State Summary Connecticut FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4hte-hinn",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-10-31T04:00:00Z",
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
-            "identifier": "VA-OM-OM-103",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT Oct 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8180,40 +8163,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-103",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referral"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4hte-hinn",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
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
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT Oct 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4i32-v5gp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "washington"
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
-            "identifier": "VA-OEI-OEI-219",
             "description": "<p>This summary describes the programs and services VA provided in Washington in fiscal year 2015.</p>",
-            "title": "State Summary: Washington FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8222,48 +8206,41 @@
                     "title": "Washington"
                 }
             ],
+            "identifier": "VA-OEI-OEI-219",
+            "issued": "2017-07-26",
+            "keyword": [
+                "washington"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4i32-v5gp",
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
+            "title": "State Summary: Washington FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/PolicyholdersbyProgrambyStateJune2013.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-06-01T04:00:00Z/2013-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotesPolicyholdersbyProgramJune2013.doc"
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
-            "identifier": "VA-VBA-INS2013-003",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policyholders for each administered life insurance program listed by state. Data is current as of 06/30/13.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Provides number of life insurance policyholders for each program by state as of 06/30/13.",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8271,108 +8248,144 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4i3e-e3uy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4i3e-e3uy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4i3e-e3uy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/4i3e-e3uy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4i3e-e3uy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4i3e-e3uy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4i3e-e3uy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4i3e-e3uy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4i3e-e3uy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "theme": [
-                "Section 25. Banking",
-                "Finance",
-                "and Insurance"
+            "identifier": "VA-VBA-INS2013-003",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
             ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/PolicyholdersbyProgrambyStateJune2013.csv",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotesPolicyholdersbyProgramJune2013.doc"
+            ],
+            "temporal": "2013-06-01T04:00:00Z/2013-06-30T04:00:00Z",
+            "theme": [
+                "Section 25. Banking",
+                "Finance",
+                "and Insurance"
+            ],
+            "title": "Provides number of life insurance policyholders for each program by state as of 06/30/13."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/4jfu-n4ax",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "veterans",
-                "washingon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@Va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/4jfu-n4ax",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Washington",
+            "identifier": "https://www.data.va.gov/api/views/4jfu-n4ax",
+            "issued": "2021-08-26",
+            "keyword": [
+                "veterans",
+                "washingon"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4jfu-n4ax",
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
+            "title": "State Summaries_Washington"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/4jzh-nt23",
-            "issued": "2021-08-27",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "puerto rico",
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
-            "identifier": "https://www.data.va.gov/api/views/4jzh-nt23",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Puerto Rico",
+            "identifier": "https://www.data.va.gov/api/views/4jzh-nt23",
+            "issued": "2021-08-27",
+            "keyword": [
+                "puerto rico",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4jzh-nt23",
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
+            "title": "State Summaries_Puerto Rico"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2012.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/va-fy12-final.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-02",
             "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-03",
             "keyword": [
                 "2012",
                 "backlog",
@@ -8386,54 +8399,53 @@
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
+            "modified": "2024-06-03",
+            "programCode": [
+                "029:080"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OIT-ITIS-02",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2012.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2012",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/va-fy12-final.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2012"
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
-            "temporal": "2015-12-15T05:00:00Z/2015-12-15T05:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR36_122015_Pending_and_EWL_Biweekly_Desired_Date_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 December 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-431",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -8447,94 +8459,94 @@
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
-            "identifier": "VA-VHA-OIA-431",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 December 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR36_122015_Pending_and_EWL_Biweekly_Desired_Date_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 December 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-12-15T05:00:00Z/2015-12-15T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 December 15"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4mi2-pg8b",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "Learn about the most common PTSD treatment types and how research on them has grown over time.",
             "identifier": "https://www.data.va.gov/api/views/4mi2-pg8b",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/4mi2-pg8b",
+            "modified": "2024-09-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Learn about the most common PTSD treatment types and how research on them has grown over time.",
             "title": "What types of PTSD treatments have been studied?"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4mnk-rrqz",
-            "issued": "2022-12-14",
             "@type": "dcat:Dataset",
-            "modified": "2023-01-12",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sharon Ennis",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "Part 2 of a three-part study on Veterans who have used at least one of 22 benefits or services (referred to as \"users\") provided by VA during Fiscal Years 2010 through 2020. Part 2 compares the Veteran user population to Veterans who have not used any VA benefits or services.",
             "identifier": "https://www.data.va.gov/api/views/4mnk-rrqz",
+            "issued": "2022-12-14",
+            "landingPage": "https://www.data.va.gov/d/4mnk-rrqz",
+            "modified": "2023-01-12",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Part 2 of a three-part study on Veterans who have used at least one of 22 benefits or services (referred to as \"users\") provided by VA during Fiscal Years 2010 through 2020. Part 2 compares the Veteran user population to Veterans who have not used any VA benefits or services.",
             "title": "Use of VA Benefits and Services: 2021 (Part 2)"
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
-            "temporal": "2015-07-01T04:00:00Z/2015-07-01T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/health/docs/Data_Pending_Access_20150701RptDate_Final.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 July 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-111",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -8548,73 +8560,44 @@
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
-            "identifier": "VA-VHA-OIA-111",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 July 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/Data_Pending_Access_20150701RptDate_Final.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 July 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-07-01T04:00:00Z/2015-07-01T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 July 1"
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
-            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
-            "keyword": [
-                "annual report",
-                "franchise fund",
-                "fy 2011"
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
-            "identifier": "VA-OM-OM-034",
+            "dataQuality": true,
             "description": "<p>Franchise Fund FY 2011 Annual Report</p>",
-            "title": "Franchise Fund FY 2011 Annual Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8623,26 +8606,56 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-034",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund",
+                "fy 2011"
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
+            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Franchise Fund FY 2011 Annual Report"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2009.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/20110125-Modified-VA-FY09-FOIA-Annual-Report-FINAL.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-05",
             "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2009",
                 "appeals",
@@ -8659,52 +8672,42 @@
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
-            "identifier": "VA-OIT-ITIS-05",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2009.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2009",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/20110125-Modified-VA-FY09-FOIA-Annual-Report-FINAL.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/4pun-u2gi",
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
+            "description": "<p>Networks are able to update on an ongoing basis data originally added to the Veterans Health Administration Physician Productivity and Staffing initiative to ensure that it reflects current conditions. This data access link function is restricted to a limited number of Network representatives. All the available facility, Network, and National Primary Care Staff and Room Utilization reports are available. In addition key guidance documents are available to people without edit access.</p>",
+            "identifier": "VA-VHA-OIA-053",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "exam",
                 "network",
@@ -8715,48 +8718,51 @@
                 "veteran",
                 "visn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/4pun-u2gi",
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
-            "identifier": "VA-VHA-OIA-053",
-            "description": "<p>Networks are able to update on an ongoing basis data originally added to the Veterans Health Administration Physician Productivity and Staffing initiative to ensure that it reflects current conditions. This data access link function is restricted to a limited number of Network representatives. All the available facility, Network, and National Primary Care Staff and Room Utilization reports are available. In addition key guidance documents are available to people without edit access.</p>",
-            "title": "VHA Support Service Center Primary Care Support Staff and Exam Room Database",
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
+            "title": "VHA Support Service Center Primary Care Support Staff and Exam Room Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "www.contextualizingcare.org",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2022-03-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2009/2012",
-            "modified": "2024-08-21",
-            "references": [
-                "The current edition of the 4C coding manual is available at https://dataverse.harvard.edu/dataverse/4C and training videos on contextualization of care and how the data was coded is at: https://youtube.com/playlist?list=PL9-b6XZZMupzmVuuwn1Ipph0dpI1fxx2d.  A publication that describes the results of the analysis",
-                "along with a URL to the abstract is as follows:  Weiner SJ",
-                "Schwartz A et al. Patient-Centered Decision Making and Health Care Outcomes: An Observational Study. Annals of Internal Medicine.  2013;158:573-579. https://www.acpjournals.org/doi/10.7326/0003-4819-158-8-201304160-00001?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed."
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Contextualizing.Care@va.gov",
+                "hasEmail": "mailto:Contextualizing.Care@va.gov"
+            },
+            "dataQuality": true,
+            "description": "This dataset consists of 405 transcriptions of audio recorded physician-patient interactions conducted at Veterans Health Administration (VHA) medical center primary care clinics. The recordings were collected utilizing concealed (except where indicated) audio recorders by patients. The protocol was approved by VHA Institutional Review Boards, and participating physicians and patients consented to participate in the study. The interactions were analyzed using Content Coding for Contextualization of Care (\"4C\"). An excel spreadsheet with the coding of the original audio of each transcript is included. All data has been de-identified.  \"xxx\" indicates PHI was removed. \"@@@\" indicates transcriber did not understand audio. These transcripts are a resource to medical educators and research scientists seeking transcriptions of primary care encounters, as well as those interested in 4C coding in its early stages. Their acquisition was supported with research funding from the Department of Veterans Affairs, Veterans Health Administration, Office of Research and Development, Health Services Research & Development.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/4qbs-wgct/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
             ],
+            "identifier": "https://www.data.va.gov/api/views/4qbs-wgct",
+            "issued": "2022-03-03",
             "keyword": [
                 "4c",
                 "content coding for contextualization of care",
@@ -8769,71 +8775,46 @@
                 "veterans health administration",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Contextualizing.Care@va.gov",
-                "hasEmail": "mailto:Contextualizing.Care@va.gov"
-            },
+            "landingPage": "www.contextualizingcare.org",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-21",
+            "programCode": [
+                "029:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/4qbs-wgct",
-            "description": "This dataset consists of 405 transcriptions of audio recorded physician-patient interactions conducted at Veterans Health Administration (VHA) medical center primary care clinics. The recordings were collected utilizing concealed (except where indicated) audio recorders by patients. The protocol was approved by VHA Institutional Review Boards, and participating physicians and patients consented to participate in the study. The interactions were analyzed using Content Coding for Contextualization of Care (\"4C\"). An excel spreadsheet with the coding of the original audio of each transcript is included. All data has been de-identified.  \"xxx\" indicates PHI was removed. \"@@@\" indicates transcriber did not understand audio. These transcripts are a resource to medical educators and research scientists seeking transcriptions of primary care encounters, as well as those interested in 4C coding in its early stages. Their acquisition was supported with research funding from the Department of Veterans Affairs, Veterans Health Administration, Office of Research and Development, Health Services Research & Development.",
-            "title": "Physician-patient transcripts with 4C coding analysis from the Contextualizing Care research program",
-            "programCode": [
-                "029:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/4qbs-wgct/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
+            "references": [
+                "The current edition of the 4C coding manual is available at https://dataverse.harvard.edu/dataverse/4C and training videos on contextualization of care and how the data was coded is at: https://youtube.com/playlist?list=PL9-b6XZZMupzmVuuwn1Ipph0dpI1fxx2d.  A publication that describes the results of the analysis",
+                "along with a URL to the abstract is as follows:  Weiner SJ",
+                "Schwartz A et al. Patient-Centered Decision Making and Health Care Outcomes: An Observational Study. Annals of Internal Medicine.  2013;158:573-579. https://www.acpjournals.org/doi/10.7326/0003-4819-158-8-201304160-00001?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed."
             ],
             "spatial": "Illinois; US",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2009/2012",
             "theme": [
                 "Physician-Patient Communication",
                 "Contextualization of Care"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Physician-patient transcripts with 4C coding analysis from the Contextualizing Care research program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VBA/blob/master/Policyholders%20by%20State%20by%20Program%20December%202013.xls",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
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
-            "identifier": "VA-VBA-INS2014-004",
+            "dataQuality": true,
             "description": "<p>VBA- Insurance Lob- Policy Holders by program by State- December 2013.</p>",
-            "title": "Policy Holders by Program by State- December  2013",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8842,86 +8823,89 @@
                     "title": "xls"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
-            "theme": [
-                "USA Spending"
-            ],
-            "language": [
-                "en-US"
-            ]
+            "identifier": "VA-VBA-INS2014-004",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "2013",
+                "life insurance policies",
+                "policy holders",
+                "policy holders by state"
+            ],
+            "landingPage": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VBA/blob/master/Policyholders%20by%20State%20by%20Program%20December%202013.xls",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2013-12-01T05:00:00Z/2013-12-31T05:00:00Z",
+            "theme": [
+                "USA Spending"
+            ],
+            "title": "Policy Holders by Program by State- December  2013"
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
+            "description": "<p>USA Spending- Native American direct Loan- February 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING022014-018",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 126",
                 "lgy",
                 "native american direct loan",
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
-            "identifier": "VA-VBA-USASPENDING022014-018",
-            "description": "<p>USA Spending- Native American direct Loan- February 2014.</p>",
-            "title": "USA Spending file-Feb 2014- Native American direct Loan-  CFDA 64.126",
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
+            "title": "USA Spending file-Feb 2014- Native American direct Loan-  CFDA 64.126"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4rcf-gbi9",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-06-10",
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
-            "identifier": "81716136-99fb-4017-a8dc-9b9062850eb9",
+            "dataQuality": true,
             "description": "<p>Average Expenditures Per Patient by Healthcare Priority Group: FY2000 to FY2018</p>",
-            "title": "Average Expenditures Per Patient by Healthcare Priority Group: FY2000 to FY2018",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8929,41 +8913,37 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "81716136-99fb-4017-a8dc-9b9062850eb9",
+            "issued": "2019-06-10",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4rcf-gbi9",
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
+            "title": "Average Expenditures Per Patient by Healthcare Priority Group: FY2000 to FY2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.mentalhealth.va.gov/suicide_prevention/",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2016-08-29",
-            "temporal": "2009-01-01T00:00:00Z/2011-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-18",
-            "keyword": [
-                "prevention",
-                "suicide",
-                "synthetic",
-                "veterans",
-                "vha"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:VHAOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/4rm3-5s3y",
+            "dataQuality": false,
             "description": "<p><b>NOTE: This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>\n\nThe Veteran Health Administration, in support of the Open Data Initiative, is providing the Veterans Affairs Suicide Prevention Synthetic Dataset (VASPSD). The VASPSD was developed using a real, record-level dataset provided through the VA Office of Suicide Prevention. The VASPSD contains no real Veteran information, however, it reflects similar characteristics of the real dataset.\n\n<p><b>* NOTICE: This data is intended to appear similar to actual VASPSD data but it does not have any real predictive modeling value. It should not be used in any real world application.</b></p>",
-            "title": "Veterans Affairs Suicide Prevention Synthetic Dataset",
-            "programCode": [
-                "029:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8971,50 +8951,47 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "https://www.data.va.gov/api/views/4rm3-5s3y",
+            "issued": "2016-08-29",
+            "keyword": [
+                "prevention",
+                "suicide",
+                "synthetic",
+                "veterans",
+                "vha"
+            ],
+            "landingPage": "https://www.mentalhealth.va.gov/suicide_prevention/",
+            "language": [
+                "English"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-01-18",
+            "programCode": [
+                "029:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2009-01-01T00:00:00Z/2011-12-31T00:00:00Z",
             "theme": [
                 "Suicide Prevention"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Veterans Affairs Suicide Prevention Synthetic Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policyholders_by_State_by_Program_October2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2012-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Policyholders_by_Program_October2012.doc"
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
-            "identifier": "VA-VBA-INS2012-016",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policyholders for each administered life insurance program listed by state. Data is current as of 10/31/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Provides number of life insurance policyholders for each program by state as of 10/31/12.",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9022,90 +8999,96 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4rv5-i823/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4rv5-i823/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4rv5-i823/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/4rv5-i823/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4rv5-i823/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4rv5-i823/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4rv5-i823/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4rv5-i823/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4rv5-i823/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-016",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policyholders_by_State_by_Program_October2012.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Policyholders_by_Program_October2012.doc"
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
+            "title": "Provides number of life insurance policyholders for each program by state as of 10/31/12."
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4tib-3w4r",
-            "issued": "2023-06-19",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary District of Columbia FY2021",
+            "identifier": "https://www.data.va.gov/api/views/4tib-3w4r",
+            "issued": "2023-06-19",
             "keyword": [
                 "dc",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/4tib-3w4r",
+            "landingPage": "https://www.data.va.gov/d/4tib-3w4r",
+            "modified": "2024-06-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary District of Columbia FY2021",
             "title": "NCVAS State Summary District of Columbia FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4tn7-fjnv",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "burial",
-                "cemetery"
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
-            "identifier": "VA-NCA-MPS-002",
             "description": "<p>This fact provides some background and history of the National Cemetery Administration.</p>",
-            "title": "National Cemetery Administration Fact Sheet",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9114,73 +9097,73 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-NCA-MPS-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "burial",
+                "cemetery"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4tn7-fjnv",
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
+            "title": "National Cemetery Administration Fact Sheet"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:15"
             ],
-            "landingPage": "https://www.data.va.gov/d/4tx7-hu2d",
-            "issued": "2019-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-04",
-            "keyword": [
-                "opioids",
-                "prescribing"
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
-            "identifier": "https://www.data.va.gov/api/views/4tx7-hu2d",
             "description": "In keeping with the Department of Veterans Affairs effort to be the most transparent agency in government, VA will begin publicly posting information on opioids dispensed from VA pharmacies along with VA\u2019s strategies to appropriately and safely prescribe these pain medications.",
-            "title": "Department of Veterans Affairs Opioid Prescribing Data",
+            "identifier": "https://www.data.va.gov/api/views/4tx7-hu2d",
+            "issued": "2019-09-10",
+            "keyword": [
+                "opioids",
+                "prescribing"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4tx7-hu2d",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-02-04",
             "programCode": [
                 "029:040"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Department of Veterans Affairs Opioid Prescribing Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.osehra.org/blog/release-vista-evolution-program-plan-and-vista-4-product-roadmap",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "product",
-                "roadmap",
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
-            "identifier": "VA-OIT-ASD-006",
+            "dataQuality": true,
             "description": "<p>The VistA 4 Product Roadmap outlines how the Department of Veterans Affairs (VA), under the direction of the VistA Evolution Program, will build upon the previous success and institutional knowledge investment in Veterans Health Information Systems and Technology Architecture (VistA) Electronic Health Record (EHR). The evolution of VA\u00ef\u00bf\u00bds existing EHR product will be known as VistA 4. The updated VA EHR system will be interoperable with the EHR systems of the Department of Defense (DoD) and other healthcare partners to enhance patient-centered, team- and evidence-based care by giving healthcare providers a complete picture of a patient\u00ef\u00bf\u00bds care and treatment history.</p>",
-            "title": "VistA 4 Product Roadmap",
-            "programCode": [
-                "029:078"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9189,45 +9172,48 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OIT-ASD-006",
+            "issued": "2017-07-26",
+            "keyword": [
+                "product",
+                "roadmap",
+                "vista"
+            ],
+            "landingPage": "http://www.osehra.org/blog/release-vista-evolution-program-plan-and-vista-4-product-roadmap",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
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
+            "title": "VistA 4 Product Roadmap"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4vkb-cfgc",
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
-            "title": "Equitable Relief Reports 2008",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9235,69 +9221,67 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4vkb-cfgc",
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
+            "title": "Equitable Relief Reports 2008"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4w6z-h6wd",
-            "issued": "2023-07-13",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-14",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Nebraska FY2021",
+            "identifier": "https://www.data.va.gov/api/views/4w6z-h6wd",
+            "issued": "2023-07-13",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "nebraska"
             ],
-            "identifier": "https://www.data.va.gov/api/views/4w6z-h6wd",
+            "landingPage": "https://www.data.va.gov/d/4w6z-h6wd",
+            "modified": "2024-06-14",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Nebraska FY2021",
             "title": "NCVAS State Summary Nebraska FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4w7e-pj5h",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "oregon"
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
-            "identifier": "VA-OEI-OEI-208",
             "description": "<p>This summary describes the programs and services VA provided in Oregon in fiscal year 2015.</p>",
-            "title": "State Summary: Oregon FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9306,26 +9290,54 @@
                     "title": "Oregon"
                 }
             ],
+            "identifier": "VA-OEI-OEI-208",
+            "issued": "2017-07-26",
+            "keyword": [
+                "oregon"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4w7e-pj5h",
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
+            "title": "State Summary: Oregon FY15"
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
-            "temporal": "2014-07-01T04:00:00Z/2014-07-01T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140717.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "July 17, 2014"
+                }
             ],
+            "identifier": "VA-VHA-OIA-059",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -9339,72 +9351,41 @@
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
-            "identifier": "VA-VHA-OIA-059",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.</p>",
-            "title": "Accelerating Access to Care Initiative - Report 2014 July 17",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140717.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "July 17, 2014"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2014-07-01T04:00:00Z/2014-07-01T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative - Report 2014 July 17"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4xch-dii8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-06-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-13",
-            "keyword": [
-                "period of service",
-                "rural",
-                "urban",
-                "veteran population"
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
-            "identifier": "https://www.data.va.gov/api/views/4xch-dii8",
             "description": "The Department of Veterans Affairs provides official estimates and projections of the Veteran population using the Veteran Population Projection Model (VetPop). Based on the latest model VetPop2020 and the most recent national survey estimates from the 2022 American Community Survey 1-Year data, the projected number of Veterans living in 50 states, DC and Puerto Rico for fiscal year 2023, is allocated to Urban and Rural areas. As defined by the Census Bureau, those not residing in Urban areas are assumed to be in Rural areas (https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural/2010-urban-rural.html). \n\nThis table contains the Veteran estimates by period of service in urban and rural areas.\n\nNote, rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2020 Urban/Rural by Period of Service FY2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9412,56 +9393,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4xch-dii8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4xch-dii8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4xch-dii8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/4xch-dii8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4xch-dii8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4xch-dii8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4xch-dii8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4xch-dii8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4xch-dii8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4xj5-qh8c",
-            "bureauCode": [
-                "029:40"
-            ],
-            "issued": "2018-03-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-19",
-            "keyword": [
-                "equitable relief report"
+            "identifier": "https://www.data.va.gov/api/views/4xch-dii8",
+            "issued": "2024-06-13",
+            "keyword": [
+                "period of service",
+                "rural",
+                "urban",
+                "veteran population"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4xch-dii8",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-13",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 Urban/Rural by Period of Service FY2023"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "029:40"
             ],
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
-            "title": "Equitable Relief Reports 2016",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9469,48 +9455,44 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4xj5-qh8c",
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
+            "title": "Equitable Relief Reports 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/index.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "homeless",
-                "ncvas",
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
-            "identifier": "VA-OEI-OEI-013",
+            "dataQuality": true,
             "description": "<p>This brief uses data from the 2009 and 2010 Annual Homeless Assessment Reports (AHAR) to Congress. The reports were sponsored by the Department of Housing and Urban Development and the Department of Veterans Affairs.</p>",
-            "title": "Profile of Sheltered Homeless Veterans for Fiscal Years 2009 and 2010",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9519,42 +9501,44 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-013",
+            "issued": "2017-07-26",
+            "keyword": [
+                "homeless",
+                "ncvas",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/index.asp",
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
+            "temporal": "2008-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Homeless Veterans"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Profile of Sheltered Homeless Veterans for Fiscal Years 2009 and 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4ybf-pfc3",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "puerto rico"
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
-            "identifier": "VA-OEI-OEI-210",
             "description": "<p>This summary describes the programs and services VA provided in Puerto Rico in fiscal year 2015.</p>",
-            "title": "State Summary: Puerto Rico FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9563,41 +9547,40 @@
                     "title": "Puerto Rico"
                 }
             ],
+            "identifier": "VA-OEI-OEI-210",
+            "issued": "2017-07-26",
+            "keyword": [
+                "puerto rico"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4ybf-pfc3",
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
+            "title": "State Summary: Puerto Rico FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4z3a-2qz2",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-09-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "keyword": [
-                "healthcare",
-                "women veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/4z3a-2qz2",
             "description": "Summary level data from the National Veteran Health Equity Report - FY2013, filtered by sex.",
-            "title": "VA-OHE-NVHER-FY13-Sociodemographic-Sex",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9605,57 +9588,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4z3a-2qz2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4z3a-2qz2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4z3a-2qz2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/4z3a-2qz2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4z3a-2qz2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4z3a-2qz2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4z3a-2qz2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4z3a-2qz2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4z3a-2qz2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/4z3a-2qz2",
+            "issued": "2019-09-19",
+            "keyword": [
+                "healthcare",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4z3a-2qz2",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA-OHE-NVHER-FY13-Sociodemographic-Sex"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4z73-eybg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-18",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-23",
-            "keyword": [
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
-            "identifier": "https://www.data.va.gov/api/views/4z73-eybg",
             "description": "A Veteran user is defined as any Veteran who received or used at least one VA benefit or service during the fiscal year. Veteran spouses, Veteran dependents, and active military service members who used VA benefits and services were not included in the analysis. Each Veteran is only counted once in the overall total even if he/she used multiple programs.",
-            "title": "Veterans who used a VA Benefit",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9663,66 +9646,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4z73-eybg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4z73-eybg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4z73-eybg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/4z73-eybg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4z73-eybg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4z73-eybg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4z73-eybg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4z73-eybg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4z73-eybg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "State",
-            "license": "https://www.usa.gov/government-works",
+            "identifier": "https://www.data.va.gov/api/views/4z73-eybg",
+            "issued": "2021-02-18",
+            "keyword": [
+                "veteran",
+                "veteran benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4z73-eybg",
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
+            "title": "Veterans who used a VA Benefit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Report.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
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
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-041",
+            "dataQuality": true,
+            "describedBy": "https://www.benefits.va.gov/reports/annual_performance_reports.asp",
             "description": "<p>This report provides county-level estimates of the number of Veterans who received VA Disability Compensation or Pension benefits during FY 2013. It includes the Veterans' total disability rating, age group, and gender.</p>",
-            "title": "Compensation and pension by County: 2013",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9731,44 +9712,47 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.benefits.va.gov/reports/annual_performance_reports.asp",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-041",
+            "issued": "2017-07-26",
+            "keyword": [
+                "compensation",
+                "county",
+                "pension"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/Report.asp",
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
+                "https://www.benefits.va.gov/reports/annual_performance_reports.asp"
+            ],
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Compensation and Pension Recipient by County"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Compensation and pension by County: 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/4zsp-2xku",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-09-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-29",
-            "keyword": [
-                "vha"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OIT Open Data",
                 "hasEmail": "mailto:OITOPENDATA@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veteran Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/4zsp-2xku",
             "description": "Key Indicators for Veteran Signals VHA Outpatient Survey",
-            "title": "Key Indicators for Veteran Signals VHA Outpatient Survey",
-            "programCode": [
-                "029:040"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9776,96 +9760,95 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4zsp-2xku/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4zsp-2xku/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4zsp-2xku/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/4zsp-2xku/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4zsp-2xku/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4zsp-2xku/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/4zsp-2xku/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/4zsp-2xku/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/4zsp-2xku/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/4zsp-2xku",
+            "issued": "2019-09-19",
+            "keyword": [
+                "vha"
+            ],
+            "landingPage": "https://www.data.va.gov/d/4zsp-2xku",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-29",
+            "programCode": [
+                "029:040"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
+            "title": "Key Indicators for Veteran Signals VHA Outpatient Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/523r-mn3d",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "64971372-40a2-4207-937c-892283f391ba",
-            "description": "<p>These spreadsheets contain the percent of Veteran farmers and dairymen  by county for the state of California.</p>",
-            "title": "Veteran Farmer Data (2015)",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/data/VAOpenDataMigration2019/Data-Dictionary-Apps-for-Ag.pdf",
             "describedByType": "application/pdf",
+            "description": "<p>These spreadsheets contain the percent of Veteran farmers and dairymen  by county for the state of California.</p>",
+            "identifier": "64971372-40a2-4207-937c-892283f391ba",
+            "issued": "2017-07-07",
+            "keyword": [
+                "veterans farmer"
+            ],
+            "landingPage": "https://www.data.va.gov/d/523r-mn3d",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:086"
             ],
-            "describedBy": "https://www.va.gov/data/VAOpenDataMigration2019/Data-Dictionary-Apps-for-Ag.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
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
+            "title": "Veteran Farmer Data (2015)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5378-mxqw",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-03-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-21",
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
-            "identifier": "https://www.data.va.gov/api/views/5378-mxqw",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) data from the 2019 & 2020 AES administrations. Scores are provided at the station level and up, and the occupation level within hospitals.",
-            "title": "All Employee Survey (AES) 2019 - 2020",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9873,59 +9856,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5378-mxqw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5378-mxqw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5378-mxqw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5378-mxqw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5378-mxqw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5378-mxqw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5378-mxqw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5378-mxqw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5378-mxqw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/5378-mxqw",
+            "issued": "2021-03-30",
+            "keyword": [
+                "engagement",
+                "satisfaction",
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5378-mxqw",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-03-21",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "All Employee Survey (AES) 2019 - 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/53c7-bcvz",
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
-            "identifier": "OM-OM-179",
             "description": "<p>COIN report 0017 Feb 2017</p>",
-            "title": "COIN 0017 Feb 2017",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9933,50 +9916,44 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-179",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/53c7-bcvz",
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
+            "title": "COIN 0017 Feb 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.mentalhealth.va.gov/",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Contains Health Insurance Portability and Accountabilty Act (HIPAA) protected data.",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2001-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "health",
-                "patient",
-                "prevention",
-                "statistics",
-                "suicide",
-                "va",
-                "veteran",
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
-            "identifier": "VA-VHA-10N-016",
-            "description": "<p>This report provides information regarding suicide mortality for the years 2001\u20132014. It incorporates the most recent mortality data from the VA/Department of Defense (DoD) Joint Suicide Data Repository and includes information for deaths from suicide among all known Veterans of U.S. military service. Data for the Joint VA/DoD Suicide Data Repository were obtained from the National Center for Health Statistics\u2019 National Death Index through collaboration with the DoD, the CDC, and the VA/DoD Joint Suicide Data Repository initiative. Data available from the National Death Index include reports of mortality submitted from vital statistics systems in all 50 U.S. states, New York City, Washington D.C., Puerto Rico, and the U.S. Virgin Islands.</p>",
-            "title": "Suicide Among Veterans and Other Americans 2001\u20132014 Report",
+            "dataQuality": true,
+            "describedBy": "https://www.mentalhealth.va.gov/docs/2016suicidedatareport.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:042"
-            ],
+            "description": "<p>This report provides information regarding suicide mortality for the years 2001\u20132014. It incorporates the most recent mortality data from the VA/Department of Defense (DoD) Joint Suicide Data Repository and includes information for deaths from suicide among all known Veterans of U.S. military service. Data for the Joint VA/DoD Suicide Data Repository were obtained from the National Center for Health Statistics\u2019 National Death Index through collaboration with the DoD, the CDC, and the VA/DoD Joint Suicide Data Repository initiative. Data available from the National Death Index include reports of mortality submitted from vital statistics systems in all 50 U.S. states, New York City, Washington D.C., Puerto Rico, and the U.S. Virgin Islands.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9985,60 +9962,55 @@
                     "title": "2016SuicideDataReport"
                 }
             ],
-            "describedBy": "https://www.mentalhealth.va.gov/docs/2016suicidedatareport.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-10N-016",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health",
+                "patient",
+                "prevention",
+                "statistics",
+                "suicide",
+                "va",
+                "veteran",
+                "vha"
+            ],
+            "landingPage": "http://www.mentalhealth.va.gov/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Contains Health Insurance Portability and Accountabilty Act (HIPAA) protected data.",
+            "temporal": "2001-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suicide Among Veterans and Other Americans 2001\u20132014 Report"
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
-            "temporal": "2015-04-01T04:00:00Z/2015-04-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
-            ],
-            "keyword": [
-                "access",
-                "appointment",
-                "enrollee",
-                "ewl",
-                "health",
-                "health care",
-                "near",
-                "va",
-                "veteran",
-                "wait list",
-                "wait time"
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
-            "identifier": "VA-VHA-OIA-102",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Apr 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10047,50 +10019,59 @@
                     "title": "Pending Appointments 2015 April 1"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-102",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
+            "keyword": [
+                "access",
+                "appointment",
+                "enrollee",
+                "ewl",
+                "health",
+                "health care",
+                "near",
+                "va",
+                "veteran",
+                "wait list",
+                "wait time"
+            ],
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
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
+            ],
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
+            "temporal": "2015-04-01T04:00:00Z/2015-04-01T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Apr 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://prod.usva.nucivicdata.com/story/department-veterans-affairs-national-cemetery-association.",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2017-01-01T05:00:00Z/2017-02-03T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "burial data",
-                "cemeteries",
-                "gravesites",
-                "veterans and beneficiaries"
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
-            "identifier": "VA-NCA-MS-805",
+            "dataQuality": true,
             "description": "<p>VA Cemeteries - Address, Location, Contact Information, Burial Space</p>",
-            "title": "VA Cemeteries - Address, Location, Contact Information, Burial Space",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10098,44 +10079,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/53xn-r2pz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/53xn-r2pz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/53xn-r2pz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/53xn-r2pz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/53xn-r2pz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/53xn-r2pz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/53xn-r2pz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/53xn-r2pz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/53xn-r2pz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-MS-805",
+            "issued": "2017-07-26",
+            "keyword": [
+                "burial data",
+                "cemeteries",
+                "gravesites",
+                "veterans and beneficiaries"
+            ],
+            "landingPage": "http://prod.usva.nucivicdata.com/story/department-veterans-affairs-national-cemetery-association.",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2017-01-01T05:00:00Z/2017-02-03T05:00:00Z",
             "theme": [
                 "Cemetery and burial data"
-            ]
+            ],
+            "title": "VA Cemeteries - Address, Location, Contact Information, Burial Space"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/54fw-895k",
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
+            "description": "<p>The Former Prisoner of War (POW) Statistical Tracking System database is a registry designed to comply with Public Law 97-37, the Former Prisoner of War Benefits Act of 1981. This database contains information about the Medical Evaluation Program for ex-POWs at VA facilities. The program provides a complete medical and psychiatric evaluation of ex-POWs. Only ex-POWs who volunteer to participate in the program are included in this registry. Health examinations are given to ex-POWs at VA facilities. The findings are then recorded on a special coding sheet, VA Form 10-0048a. Quarterly, these code sheets are sent to the Austin Information Technology Center, where they are manually keyed into the database. The main users of this registry are: * The Advisory Committee on Former Prisoners of War * Congress * National Academy of Sciences * Researchers * The National Center for Veteran Analysis and Statistics.</p>",
+            "identifier": "VA-VHA-VHA-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1984-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "97-37",
                 "evaluation",
@@ -10148,61 +10151,42 @@
                 "veteran",
                 "war"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/54fw-895k",
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
-            "identifier": "VA-VHA-VHA-002",
-            "description": "<p>The Former Prisoner of War (POW) Statistical Tracking System database is a registry designed to comply with Public Law 97-37, the Former Prisoner of War Benefits Act of 1981. This database contains information about the Medical Evaluation Program for ex-POWs at VA facilities. The program provides a complete medical and psychiatric evaluation of ex-POWs. Only ex-POWs who volunteer to participate in the program are included in this registry. Health examinations are given to ex-POWs at VA facilities. The findings are then recorded on a special coding sheet, VA Form 10-0048a. Quarterly, these code sheets are sent to the Austin Information Technology Center, where they are manually keyed into the database. The main users of this registry are: * The Advisory Committee on Former Prisoners of War * Congress * National Academy of Sciences * Researchers * The National Center for Veteran Analysis and Statistics.</p>",
-            "title": "Former Prisoner of War Statistical Tracking System",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1984-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Former Prisoner of War Statistical Tracking System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/54pz-ahi4",
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
-            "identifier": "https://www.data.va.gov/api/views/54pz-ahi4",
+            "dataQuality": true,
             "description": "<p>VBA PROGRAM BENEFITS for Automobiles and Adaptive Equipment for Certain Disabled Veterans and Members of the Armed Forces. Veterans with honorable service and servicepersons on duty having a service-connected disability due to loss or permanent loss of use of one or both feet, one or both hands, or a permanent impairment of vision of both eyes to a prescribed degree. For adaptive equipment only, eligibility also exists if there is service-connected ankylosis of one or both knees or one or both hips. Personnel on active duty also qualify under the same criteria as veterans. Uses &amp; Use Restrictions:  Assistance toward purchase of an automobile or other conveyance is a one-time payment only. Necessary adaptive equipment may be furnished, repaired, replaced, or reinstalled on a conveyance which may be purchased with assistance or any other conveyance subsequently or previously acquired. Adaptive equipment will be provided for no more than two conveyances during any four-year period unless one of those two vehicles becomes unavailable to the veteran.</p>",
-            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE APR2019",
-            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10210,60 +10194,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/54pz-ahi4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/54pz-ahi4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/54pz-ahi4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/54pz-ahi4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/54pz-ahi4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/54pz-ahi4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/54pz-ahi4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/54pz-ahi4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/54pz-ahi4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/54pz-ahi4",
+            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 100"
+            ],
+            "landingPage": "https://www.data.va.gov/d/54pz-ahi4",
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
+            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/55k3-7hdc",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
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
-            "identifier": "https://www.data.va.gov/api/views/55k3-7hdc",
             "description": "Dataset from 2014 listing the count of minority and non-minorities using VBA services",
-            "title": "2014 USVETS Minority Veterans Report: Count of Minority & Non-Minority Use of VBA",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10271,57 +10255,56 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/55k3-7hdc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/55k3-7hdc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/55k3-7hdc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/55k3-7hdc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/55k3-7hdc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/55k3-7hdc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/55k3-7hdc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/55k3-7hdc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/55k3-7hdc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/55k3-7hdc",
+            "issued": "2019-10-24",
+            "keyword": [
+                "minority veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/55k3-7hdc",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
+            "title": "2014 USVETS Minority Veterans Report: Count of Minority & Non-Minority Use of VBA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/55uq-7qgs",
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
-            "identifier": "VA-OM-OM-133",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT FEB 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10329,41 +10312,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-133",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/55uq-7qgs",
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
+            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT FEB 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/56g8-5e9d",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-08-27",
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
-            "identifier": "885754ff-2ce5-4280-b186-1589680627e8",
+            "dataQuality": true,
             "description": "<p>The product displays data for FY2000 to FY2017. It includes data related to Healthcare Priority Group.</p>",
-            "title": "Average Expenditures per Patient by Healthcare Priority Group: FY2000 to FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10371,45 +10355,41 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "885754ff-2ce5-4280-b186-1589680627e8",
+            "issued": "2018-08-27",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/56g8-5e9d",
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
+            "title": "Average Expenditures per Patient by Healthcare Priority Group: FY2000 to FY2017"
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
-            "identifier": "VA-VBA-ABR2012-028",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Service Connected Disability Benefits by Combined Percent of Disability for Veterans Receiving Compensation FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10417,44 +10397,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-028",
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
+            "title": "Service Connected Disability Benefits by Combined Percent of Disability for Veterans Receiving Compensation FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/57en-26a2",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "monitoring"
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
-            "identifier": "e5218bc3-94a8-4049-8632-804784b03c69",
+            "dataQuality": true,
             "description": "<p>DAS application monitoring and control utility</p>",
-            "title": "Monitoring",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10463,36 +10447,36 @@
                     "title": "Monitoring"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "e5218bc3-94a8-4049-8632-804784b03c69",
+            "issued": "2018-02-23",
+            "keyword": [
+                "monitoring"
+            ],
+            "landingPage": "https://www.data.va.gov/d/57en-26a2",
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
+            "title": "Monitoring"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/57j8-8ueu",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "maine"
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
-            "identifier": "VA-OEI-OEI-189",
             "description": "<p>This summary describes the programs and services VA provided in Maine in fiscal year 2015.</p>",
-            "title": "State Summary: Maine",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10501,75 +10485,74 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-189",
+            "issued": "2017-07-26",
+            "keyword": [
+                "maine"
+            ],
+            "landingPage": "https://www.data.va.gov/d/57j8-8ueu",
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
+            "title": "State Summary: Maine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/57p5-4mwf",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Landing Page",
+            "identifier": "https://www.data.va.gov/api/views/57p5-4mwf",
             "issued": "2024-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-05",
             "keyword": [
                 "ncvas",
                 "ncvas landing page",
                 "state summaries",
                 "state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/57p5-4mwf",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-05",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/57p5-4mwf",
-            "description": "NCVAS State Summary Landing Page",
-            "title": "NCVAS State Summary Landing Page",
-            "programCode": [
-                "029:086"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "title": "NCVAS State Summary Landing Page"
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
-            "temporal": "2004-10-01T04:00:00Z/2005-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
-            "keyword": [
-                "annual report",
-                "franchise fund",
-                "fy 2005"
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
-            "identifier": "VA-OM-OM-040",
+            "dataQuality": true,
             "description": "<p>Franchise Fund FY 2005 Annual Report</p>",
-            "title": "Franchise Fund FY 2005 Annual Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10578,44 +10561,45 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-040",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund",
+                "fy 2005"
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
+            "temporal": "2004-10-01T04:00:00Z/2005-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Franchise Fund FY 2005 Annual Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/58he-5dej",
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
-            "identifier": "1b9e53e5-4649-425b-8144-bb277a7e5896",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Ohio FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10623,48 +10607,44 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "1b9e53e5-4649-425b-8144-bb277a7e5896",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/58he-5dej",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "theme": [
-                "Basic Statistics",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "theme": [
+                "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Ohio FY2017"
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
-            "identifier": "VA-VBA-ABR2012-054",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report( ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the benefitciaries</p>",
-            "title": "VA Home Loans Guaranteed by Fiscal Year",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10672,46 +10652,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-054",
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
+            "title": "VA Home Loans Guaranteed by Fiscal Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/58zp-ytsm",
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
-            "identifier": "https://www.data.va.gov/api/views/58zp-ytsm",
+            "dataQuality": true,
             "description": "<p>This dataset contains information on minority veteran healthcare usage, educational attainment, unemployment rates, median income, and projected population figures.</p>",
-            "title": "Benefits Utilization by Program and Minority Status: 2014 (In Percentages Relative to Total)",
-            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10719,48 +10701,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/58zp-ytsm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/58zp-ytsm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/58zp-ytsm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/58zp-ytsm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/58zp-ytsm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/58zp-ytsm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/58zp-ytsm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/58zp-ytsm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/58zp-ytsm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/58zp-ytsm",
+            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
+            "issued": "2017-03-15",
+            "keyword": [
+                "health care",
+                "income",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/58zp-ytsm",
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
+            "title": "Benefits Utilization by Program and Minority Status: 2014 (In Percentages Relative to Total)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2021-03-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-07-01T04:00:00Z/2021-03-31T00:00:00Z",
-            "modified": "2024-02-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Veterans Access to Care (OVAC)",
+                "hasEmail": "mailto:VHA15ACCOVACAction@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "**NOTICE:** VA has updated how it releases Access data. As of March 25, 2021, VA is no longer updating this page. Instead, go to accesstocare.va.gov for current wait times and other relevant access data.\n\nOn Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access. The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/59na-t7z8/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
             ],
+            "identifier": "https://www.data.va.gov/api/views/59na-t7z8",
+            "issued": "2021-03-31",
             "keyword": [
                 "electron wait list",
                 "ewl",
@@ -10772,71 +10781,44 @@
                 "vha",
                 "wait times"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Veterans Access to Care (OVAC)",
-                "hasEmail": "mailto:VHA15ACCOVACAction@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en:US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-02-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/59na-t7z8",
-            "description": "**NOTICE:** VA has updated how it releases Access data. As of March 25, 2021, VA is no longer updating this page. Instead, go to accesstocare.va.gov for current wait times and other relevant access data.\n\nOn Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access. The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package",
-            "title": "VA Access Audit & Wait Times Fact Sheets",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/59na-t7z8/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
             "spatial": "US,Puerto Rico, US Virgin Islands, Guam, American Samoa,  Philippines, Northern Mariana Islands",
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2014-07-01T04:00:00Z/2021-03-31T00:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en:US"
-            ]
+            "title": "VA Access Audit & Wait Times Fact Sheets"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/59u7-b9ha",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cemetery",
-                "gravesite locator",
-                "kiosk"
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
-            "identifier": "VA-NCA-OFP-001",
             "description": "<p>This guide describes the specifications for installing Kiosks at NCA Cemeteries</p>",
-            "title": "National Cemetery Administration Gravesite Locator Kiosk - Installation Guide",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10845,40 +10827,42 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-NCA-OFP-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cemetery",
+                "gravesite locator",
+                "kiosk"
+            ],
+            "landingPage": "https://www.data.va.gov/d/59u7-b9ha",
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
+            "title": "National Cemetery Administration Gravesite Locator Kiosk - Installation Guide"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/59xd-zfbr",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "arkansas"
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
-            "identifier": "VA-OEI-OEI-173",
             "description": "<p>This summary describes the programs and services VA provided in Arkansas in fiscal year 2015.</p>",
-            "title": "State Summary Arkansas",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10887,24 +10871,39 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-173",
+            "issued": "2017-07-26",
+            "keyword": [
+                "arkansas"
+            ],
+            "landingPage": "https://www.data.va.gov/d/59xd-zfbr",
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
+            "title": "State Summary Arkansas"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/59yt-v847",
-            "issued": "2022-12-09",
             "@type": "dcat:Dataset",
-            "modified": "2023-01-12",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
+            "description": "Part 1 of a three-part study on Veterans who have used at least one of 22 benefits or services (referred to as \"users\") provided by VA during Fiscal Years 2010 through 2021. Part 1 presents basic characteristics of the VA user population and trends in their use of benefits and services.",
+            "identifier": "https://www.data.va.gov/api/views/59yt-v847",
+            "issued": "2022-12-09",
             "keyword": [
                 "utilization",
                 "va programs",
@@ -10913,68 +10912,52 @@
                 "veterans",
                 "veterans benefits"
             ],
-            "identifier": "https://www.data.va.gov/api/views/59yt-v847",
+            "landingPage": "https://www.data.va.gov/d/59yt-v847",
+            "modified": "2023-01-12",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Part 1 of a three-part study on Veterans who have used at least one of 22 benefits or services (referred to as \"users\") provided by VA during Fiscal Years 2010 through 2021. Part 1 presents basic characteristics of the VA user population and trends in their use of benefits and services.",
             "title": "Use of VA Benefits and Services: 2021 (Part 1)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5a29-8t5q",
-            "issued": "2023-08-10",
             "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Puerto Rico FY2021",
+            "identifier": "https://www.data.va.gov/api/views/5a29-8t5q",
+            "issued": "2023-08-10",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "puerto rico"
             ],
-            "identifier": "https://www.data.va.gov/api/views/5a29-8t5q",
+            "landingPage": "https://www.data.va.gov/d/5a29-8t5q",
+            "modified": "2023-08-25",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Puerto Rico FY2021",
             "title": "NCVAS State Summary Puerto Rico FY2021"
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
-            "temporal": "2014-01-01T05:00:00Z/2014-03-31T04:00:00Z",
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
-            "identifier": "VA-OEI-OEI-053",
+            "dataQuality": true,
             "description": "<p>NCVAS Pocket Cards archives are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10983,46 +10966,47 @@
                     "title": "VA Benefits and Health Care Utilization"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-053",
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
+            "temporal": "2014-01-01T05:00:00Z/2014-03-31T04:00:00Z",
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
-            "landingPage": "https://www.data.va.gov/d/5ax5-kd33",
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
-            "identifier": "https://www.data.va.gov/api/views/5ax5-kd33",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to help servicepersons adjust to civilian life after separation from military service, assist in the recruitment and retention of highly qualified personnel in the active and reserve components in the Armed Forces by providing education benefits, and to provide educational opportunities to the dependents of certain service members and veterans. Individuals who entered active duty after September 10, 2001 may be eligible for the Post-9/11 GI Bill. Individuals can use the Post-9/11 GI Bill after serving 90 days on active duty (excluding entry level and skill training). Only periods of active duty under title 10 will be used to establish eligibility for the Post 9/11 GI Bill. A high school diploma or equivalency certificate is always required for eligibility. Individuals who are eligible for the Montgomery GI Bill \u2013 Active Duty (chapter 30), the Montgomery GI Bill \u2013 Selected Reserve (chapter 1606), or the Reserve Educational Assistance Program (REAP) will have to make an irrevocable election to relinquish eligibility under one of those benefit programs to establish eligibility under the Post-9/11 GI Bill. The dependent children of a person who died in the line of duty while serving as a member of the Armed Forces may be eligible to use benefits under the Fry Scholarship provision of the Post-9/11 GI Bill. The spouse and/or child(ren) of a veteran or service member may be eligible for the Post 9/11 GI Bill if the veteran or service member transfers entitlement to those dependents. Eligibility to transfer entitlement to dependents is determined by the Department of Defense. This is not a complete list of eligibility requirements. For more information on the latest changes to the Post-9/11 GI Bill go to the VA web-site.</p>",
-            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE JAN2019",
-            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11030,57 +11014,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5ax5-kd33/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5ax5-kd33/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5ax5-kd33/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5ax5-kd33/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5ax5-kd33/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5ax5-kd33/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5ax5-kd33/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5ax5-kd33/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5ax5-kd33/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/5ax5-kd33",
+            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 028"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5ax5-kd33",
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
+            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/5b4p-6aq2",
-            "issued": "2024-04-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-11",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/5b4p-6aq2",
             "description": "",
-            "title": "health_benefits",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11088,57 +11075,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5b4p-6aq2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5b4p-6aq2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5b4p-6aq2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5b4p-6aq2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5b4p-6aq2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5b4p-6aq2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5b4p-6aq2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5b4p-6aq2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5b4p-6aq2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/5b4p-6aq2",
+            "issued": "2024-04-19",
+            "landingPage": "https://www.data.va.gov/d/5b4p-6aq2",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-11",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "health_benefits"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/5b6x-4tvp",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "contact"
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
-            "identifier": "VA-ORCH-12",
+            "dataQuality": true,
             "description": "<p>VCIS is a web service that enables consumers to create, update, retrieve, and delete veteran contact information.</p>",
-            "title": "VIERS Contact Information Service (VCIS)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11147,42 +11131,40 @@
                     "title": "VIERS Contact Information Service (VCIS)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-12",
+            "issued": "2017-11-17",
+            "keyword": [
+                "contact"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5b6x-4tvp",
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
+            "title": "VIERS Contact Information Service (VCIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oprm.va.gov/foia/",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "foia",
-                "foia library",
-                "foia reading room",
-                "foia requests"
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
-            "identifier": "VA-NCA-OIT-001",
+            "dataQuality": true,
             "description": "<p>U.S. Department of Veterans Affairs Freedom of Information Act Service Webpage with many links to associated information.</p>",
-            "title": "VA FOIA Website",
-            "programCode": [
-                "029:078"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11191,72 +11173,75 @@
                     "title": "html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-OIT-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "foia",
+                "foia library",
+                "foia reading room",
+                "foia requests"
+            ],
+            "landingPage": "https://www.oprm.va.gov/foia/",
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
+            "title": "VA FOIA Website"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/5bh7-azn5",
-            "issued": "2019-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-22",
-            "keyword": [
-                "women",
-                "women veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/5bh7-azn5",
             "description": "On February 7, 2017, the VA Office of Enterprise Integration and the University of Southern California Center for Innovation and Research for Veterans and Military Families convened a one-day roundtable to collaborate on policy and research with a special focus on women Veterans.",
-            "title": "Women Veterans Forum",
+            "identifier": "https://www.data.va.gov/api/views/5bh7-azn5",
+            "issued": "2019-09-10",
+            "keyword": [
+                "women",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5bh7-azn5",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-01-22",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Women Veterans Forum"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5bqz-r7ak",
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
-            "identifier": "https://www.data.va.gov/api/views/5bqz-r7ak",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) items also on Federal Employee Viewpoint Survey, reported as percents as required per Federal statute.",
-            "title": "AES 2020 FEVS Percents",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11264,39 +11249,37 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5bsv-aby4",
-            "bureauCode": [
-                "029:25"
+            "identifier": "https://www.data.va.gov/api/views/5bqz-r7ak",
+            "issued": "2023-03-16",
+            "keyword": [
+                "survey",
+                "veterans affairs"
             ],
-            "issued": "2019-03-27",
+            "landingPage": "https://www.data.va.gov/d/5bqz-r7ak",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-03-20",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "AES 2020 FEVS Percents"
+        },
+        {
             "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 105",
-                "cfda 64 110"
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
-            "identifier": "https://www.data.va.gov/api/views/5bsv-aby4",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE APR2019",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11304,61 +11287,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5bsv-aby4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5bsv-aby4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5bsv-aby4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5bsv-aby4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5bsv-aby4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5bsv-aby4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5bsv-aby4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5bsv-aby4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5bsv-aby4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/5bsv-aby4",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5bsv-aby4",
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
+            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5cfs-shak",
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
-            "identifier": "VA-OGC-019",
             "description": "<p>Implementation of Public Law 112-154  Author: Simpson, J.</p>",
-            "title": "OGC Precedent Opinion 2-2012",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11367,46 +11350,41 @@
                     "title": "OGC Precedent Opinion 2-2012"
                 }
             ],
+            "identifier": "VA-OGC-019",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5cfs-shak",
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
+            "title": "OGC Precedent Opinion 2-2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5cqb-kg6x",
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
-            "identifier": "https://www.data.va.gov/api/views/5cqb-kg6x",
             "description": "Data underlying the second figure of Part 1 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Number of Users by Program, FY2010-2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11414,57 +11392,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5cqb-kg6x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5cqb-kg6x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5cqb-kg6x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5cqb-kg6x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5cqb-kg6x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5cqb-kg6x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5cqb-kg6x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5cqb-kg6x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5cqb-kg6x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/5cqb-kg6x",
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
+            "landingPage": "https://www.data.va.gov/d/5cqb-kg6x",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Number of Users by Program, FY2010-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5czf-hc7k",
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
-            "identifier": "OM-OM-167",
             "description": "<p>COIN report 146 April 2016</p>",
-            "title": "COIN 146 April 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11472,46 +11455,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-167",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5czf-hc7k",
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
+            "title": "COIN 146 April 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5d67-jyfv",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-03-17",
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
-            "identifier": "https://www.data.va.gov/api/views/5d67-jyfv",
             "description": "Trend in the number and rate of Veterans who used any VA benefit versus those who used none, FY 2010-2021. Data underlying the first figure of Part 2 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Trend in Use of Any VA Benefit, FY 2010-2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11519,97 +11497,103 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5d67-jyfv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5d67-jyfv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5d67-jyfv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5d67-jyfv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5d67-jyfv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5d67-jyfv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5d67-jyfv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5d67-jyfv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5d67-jyfv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/5d67-jyfv",
+            "issued": "2022-03-17",
+            "keyword": [
+                "utilization",
+                "va benefits",
+                "va programs",
+                "va services",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5d67-jyfv",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Trend in Use of Any VA Benefit, FY 2010-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "http://www.mclarensoftware.com/about-mclaren/client-logins.aspx",
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
-            "identifier": "VA-CFM-Paragon-001",
+            "dataQuality": true,
             "description": "<p>The Paragon and Tririga Applications are project management programs utilized by CFM for construction programs.  The contents of the databases are a compiliation of the electronic contract management system(eCMS), the financial management system(FMS), and status information provided by CFM's engineering staff.  Due to the nature of the contract and financial management system information, the systems access is restricted to CFM personnel and select contractors working for CFM.  The reason for two project management programs is because Tririga is a replacement program for Paragon.  Once training has been completed and the Paragon data has been migrated to Tririga, Paragon use will be discontinued.  Paragon and Tririga are web based applications hosted by contractors outside of the VA intranet system. Paragon will be deactivated in June of 2014.</p>",
-            "title": "Paragon",
+            "identifier": "VA-CFM-Paragon-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "construction management",
+                "project management"
+            ],
+            "landingPage": "http://www.mclarensoftware.com/about-mclaren/client-logins.aspx",
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
+            "title": "Paragon"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5e82-g3hp",
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
-            "identifier": "https://www.data.va.gov/api/views/5e82-g3hp",
+            "dataQuality": true,
             "description": "<p>VBA SPECIALLY ADAPTED HOUSING BENEFIT PROGRAMS. The Specially Adapted Housing (SAH) grant program helps Veterans with certain service-connected disabilities live independently in a barrier-free environment. SAH grants can be used in one of the following ways: (1) construct a suitable home on suitable land either already owned or to be acquired by the veteran, or (2) remodel an existing home if it can be suitably adapted, or (3) acquire a suitably adapted home or reduce the outstanding mortgage on a suitably adapted home already owned by the veteran. b. The Special Housing Adaptation (SHA) grant program helps veterans with certain service-connected disabilities adapt or purchase a home to accommodate the disability. SHA grants can be used in one of the following ways: (1) adapt an existing home the veteran or a family member already owns in which the veteran lives; (2) adapt a home the veteran or family member intends to purchase in which the veteran will live; (3) help a veteran purchase a home already adapted in which the veteran will live. c. . The Temporary Residence Adaptations (TRA) program provides adaptation assistance to veterans who are residing, but do not intend to permanently reside, in the a residence owned by a family member. If a veteran is otherwise eligible for SAH or SHA, the assistance is limited. d. SAH and SHA grants may be used up to three times, as long as the aggregate grant amount does not exceed the statutory dollar limitation. TRA grants may only be used once (and count as a grant usage for purposes of the limit of three), and the amount of assistance provided will be subtracted from the veteran's available statutory maximum.</p>",
-            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS MAY2019",
-            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11617,115 +11601,115 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5e82-g3hp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5e82-g3hp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5e82-g3hp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5e82-g3hp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5e82-g3hp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5e82-g3hp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5e82-g3hp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5e82-g3hp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5e82-g3hp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/5e82-g3hp",
+            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 106"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5e82-g3hp",
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
+            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/5ezy-r98d",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-24",
-            "keyword": [
-                "north dakota",
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
-            "identifier": "https://www.data.va.gov/api/views/5ezy-r98d",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_North Dakota",
+            "identifier": "https://www.data.va.gov/api/views/5ezy-r98d",
+            "issued": "2021-08-26",
+            "keyword": [
+                "north dakota",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5ezy-r98d",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-24",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_North Dakota"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5ff7-pu98",
-            "issued": "2023-08-11",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Wyoming FY2021",
+            "identifier": "https://www.data.va.gov/api/views/5ff7-pu98",
+            "issued": "2023-08-11",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "wyoming"
             ],
-            "identifier": "https://www.data.va.gov/api/views/5ff7-pu98",
+            "landingPage": "https://www.data.va.gov/d/5ff7-pu98",
+            "modified": "2024-06-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Wyoming FY2021",
             "title": "NCVAS State Summary Wyoming FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5fv9-mytm",
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
-            "identifier": "https://www.data.va.gov/api/views/5fv9-mytm",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located</p>",
-            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS OCT2018",
-            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11733,100 +11717,99 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5fv9-mytm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5fv9-mytm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5fv9-mytm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5fv9-mytm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5fv9-mytm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5fv9-mytm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5fv9-mytm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5fv9-mytm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5fv9-mytm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/5fv9-mytm",
+            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 118"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5fv9-mytm",
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
+            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/directory/guide/division_flsh.asp?dnum=3",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "vba",
-                "vba facilities"
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
-            "identifier": "VA-VBA-INFO-001",
+            "dataQuality": true,
             "description": "<p>Interactive map of VBA facilities locator</p>",
-            "title": "VBA Facilities locator- Interactive MAP",
+            "identifier": "VA-VBA-INFO-001",
             "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "vba",
+                "vba facilities"
+            ],
+            "landingPage": "https://www.va.gov/directory/guide/division_flsh.asp?dnum=3",
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
                 "VBA Facilities locator- MAP"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VBA Facilities locator- Interactive MAP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5hpi-eywg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-07-01T04:00:00Z/2015-07-30T04:00:00Z",
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
-            "identifier": "VA-OM-OM-138",
             "description": "<p>aged accounts receivable</p>",
-            "title": "COIN 0017 July 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11834,48 +11817,77 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-138",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5hpi-eywg",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-07-01T04:00:00Z/2015-07-30T04:00:00Z",
             "theme": [
                 "financial"
-            ]
+            ],
+            "title": "COIN 0017 July 2015"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5hpm-psc7",
-            "issued": "2023-06-15",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-16",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Arkansas FY2021",
+            "identifier": "https://www.data.va.gov/api/views/5hpm-psc7",
+            "issued": "2023-06-15",
             "keyword": [
                 "arkansas",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/5hpm-psc7",
+            "landingPage": "https://www.data.va.gov/d/5hpm-psc7",
+            "modified": "2024-05-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Arkansas FY2021",
             "title": "NCVAS State Summary Arkansas FY2021"
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
+            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_201406125a-REVISED-regular-pgs.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "July 3, 2014"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-058",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2014-06-15T04:00:00Z/2014-06-15T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
-            ],
             "keyword": [
                 "access",
                 "appointment",
@@ -11889,70 +11901,42 @@
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
-            "identifier": "VA-VHA-OIA-058",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.</p>",
-            "title": "Accelerating Access to Care Initiative - Report 2014 July 3",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_201406125a-REVISED-regular-pgs.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "July 3, 2014"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2014-06-15T04:00:00Z/2014-06-15T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative - Report 2014 July 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5i2h-wzh9",
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
-            "identifier": "5d4f7a5c-9adf-4113-99b9-9e072aeee17f",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Washington FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11960,37 +11944,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "5d4f7a5c-9adf-4113-99b9-9e072aeee17f",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5i2h-wzh9",
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
+            "title": "State Summary Washington FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5i42-xma2",
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
-            "identifier": "VA-OGC-023",
             "description": "<p>Veterans\u2019 Health Administration Quality-Assurance Records and Board of Veterans\u2019 Appeal Review Authority \u2013 38 U.S.C. \u00a7 5705; 38 C.F.R. \u00a7\u00a7 17.500-17.511</p>",
-            "title": "OGC Precedent Opinion 1-2011",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11999,77 +11982,72 @@
                     "title": "OGC Precedent Opinion 1-2011"
                 }
             ],
+            "identifier": "VA-OGC-023",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5i42-xma2",
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
+            "title": "OGC Precedent Opinion 1-2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/5ju7-gp5z",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "minnesota",
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
-            "identifier": "https://www.data.va.gov/api/views/5ju7-gp5z",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Minnesota",
+            "identifier": "https://www.data.va.gov/api/views/5ju7-gp5z",
+            "issued": "2021-08-26",
+            "keyword": [
+                "minnesota",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5ju7-gp5z",
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
+            "title": "State Summaries_Minnesota"
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
-            "identifier": "VA-VBA-INS2012-012",
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
@@ -12077,66 +12055,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5kdy-b3xh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5kdy-b3xh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5kdy-b3xh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5kdy-b3xh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5kdy-b3xh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5kdy-b3xh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5kdy-b3xh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5kdy-b3xh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5kdy-b3xh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-012",
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
-            "landingPage": "https://www.data.va.gov/d/5m57-gbgr",
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
-            "identifier": "https://www.data.va.gov/api/views/5m57-gbgr",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist States and federally recognized tribal governments in the establishment, expansion, and improvement of veterans' cemeteries. Monetary assistance is provided under this program to establish, expand, and improve State or Tribal government veterans\u2019 cemeteries. Cemeteries must be State or Tribal Government owned and operated solely for the interment of eligible veterans and their dependents and/or spouses. Construction cost means the amount found necessary to convert a tract of land to an operational cemetery. The cemetery must be used solely for the interment of veterans, their wives, husbands, surviving spouses, minor children, and unmarried adult children who were physically or mentally disabled and incapable of self-support: section 38 CFR Part 38.620.</p>",
-            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM OCT2018",
-            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12144,44 +12128,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5m57-gbgr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5m57-gbgr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5m57-gbgr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5m57-gbgr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5m57-gbgr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5m57-gbgr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5m57-gbgr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5m57-gbgr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5m57-gbgr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/5m57-gbgr",
+            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
+            "issued": "2019-03-29",
+            "keyword": [
+                "cfda 64 101"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5m57-gbgr",
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
+            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/5mfj-ceqg",
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
+            "description": "<p>The Foreign Medical Program (FMP) is a health care benefits program designed for US Veterans with Veterans Affairs-rated service-connected conditions that are residing or traveling abroad (Canada and Philippines excluded). Under FMP, VA assumes payment responsibility for certain necessary medical services associated with the treatment of these service-connected conditions. The FMP database stores necessary information about Veterans eligible for foreign payment or reimbursement. Included is information about the services used and expenses incurred. FMP shares files with CHAMPVA (Civilian Health and Medical Program of VA) Eligibility &amp; Payment Functions (CVA), and resides on the same server at the Health Administration Center (HAC) at Denver, Colorado. The HAC is a division of the Veterans Health Administration (VHA) Chief Business Office.</p>",
+            "identifier": "VA-VHA-CBO-004",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1994-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "administration",
                 "center",
@@ -12195,60 +12198,40 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/5mfj-ceqg",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:067"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-CBO-004",
-            "description": "<p>The Foreign Medical Program (FMP) is a health care benefits program designed for US Veterans with Veterans Affairs-rated service-connected conditions that are residing or traveling abroad (Canada and Philippines excluded). Under FMP, VA assumes payment responsibility for certain necessary medical services associated with the treatment of these service-connected conditions. The FMP database stores necessary information about Veterans eligible for foreign payment or reimbursement. Included is information about the services used and expenses incurred. FMP shares files with CHAMPVA (Civilian Health and Medical Program of VA) Eligibility &amp; Payment Functions (CVA), and resides on the same server at the Health Administration Center (HAC) at Denver, Colorado. The HAC is a division of the Veterans Health Administration (VHA) Chief Business Office.</p>",
-            "title": "Foreign Medical Program (FMP)",
-            "programCode": [
-                "029:067"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1994-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Foreign Medical Program (FMP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5nau-f9t6",
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
-            "identifier": "VA-OM-OM-177",
             "description": "<p>COIN 0022 report  for June 2016</p>",
-            "title": "COIN 0022 report  for June 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12257,41 +12240,41 @@
                     "title": "COIN 0022 June 2016"
                 }
             ],
+            "identifier": "VA-OM-OM-177",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5nau-f9t6",
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
+            "title": "COIN 0022 report  for June 2016"
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
-            "temporal": "2010-01-01T05:00:00Z/2010-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-006",
+            "dataQuality": true,
             "description": "<p>2010 VA Performance and Accountability Report Highlights.</p>",
-            "title": "2010 VA Performance and Accountability Report Highlights",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12300,44 +12283,44 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-006",
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
+            "title": "2010 VA Performance and Accountability Report Highlights"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5q3t-bq3q",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-12-01T05:00:00Z/2014-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-118",
             "description": "<p>Aged accounts receivable report</p>",
-            "title": "COIN 0017 CARS AGE PROFILE REPORT DEC 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12345,42 +12328,43 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-118",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5q3t-bq3q",
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
+            "title": "COIN 0017 CARS AGE PROFILE REPORT DEC 2014"
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
-            "temporal": "2013-07-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-23",
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
-            "identifier": "VA-OM-OM-084",
+            "dataQuality": true,
             "description": "<p>FY 2013 Fourth Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2013 Fourth Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12389,27 +12373,46 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-084",
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
+            "modified": "2022-02-23",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2013-07-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2013 Fourth Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/5t5i-ahbe",
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
+            "description": "<p>The Veterans Health Administration (VHA) pays for care provided to VA beneficiaries in non-VA hospitals through its contract hospitalization program as mandated by Congress in the late 1980s. The Non-VA Hospital System (NVH) software captures the patient's Demographics, Provider, Hospital Name and Location, Medicare Provider Number, Diagnoses and Procedures for which the patient received care during his/her inpatient stay. The data is received from either the patient or the medical center providing the care (normally on a UB-92 form). The billing office employee enters the information into Veterans Health Information Systems and Technology Architecture and sends information to the Austin Information Technology Center (AITC). The non-VA hospitals are reimbursed at Medicare rates based on the Prospective System (PPS). PPS uses the appropriate Diagnostic Related Groups (DRGs). Each DRG has a different rate-adjusted reimbursement based on the regional and urban/rural designation of the provider non-VA Hospitals. NVH is housed at the AITC and uses software developed by the AITC in conjunction with 3M and the Center for Medicare and Medicaid Services (CMS). It is a batch system written in Common Business Oriented Language, ALC, and Statistical Analysis Software. Processing occurs daily.</p>",
+            "identifier": "VA-VHA-CBO-008",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1975-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "basis",
                 "drg",
@@ -12423,63 +12426,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/5t5i-ahbe",
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
-            "identifier": "VA-VHA-CBO-008",
-            "description": "<p>The Veterans Health Administration (VHA) pays for care provided to VA beneficiaries in non-VA hospitals through its contract hospitalization program as mandated by Congress in the late 1980s. The Non-VA Hospital System (NVH) software captures the patient's Demographics, Provider, Hospital Name and Location, Medicare Provider Number, Diagnoses and Procedures for which the patient received care during his/her inpatient stay. The data is received from either the patient or the medical center providing the care (normally on a UB-92 form). The billing office employee enters the information into Veterans Health Information Systems and Technology Architecture and sends information to the Austin Information Technology Center (AITC). The non-VA hospitals are reimbursed at Medicare rates based on the Prospective System (PPS). PPS uses the appropriate Diagnostic Related Groups (DRGs). Each DRG has a different rate-adjusted reimbursement based on the regional and urban/rural designation of the provider non-VA Hospitals. NVH is housed at the AITC and uses software developed by the AITC in conjunction with 3M and the Center for Medicare and Medicaid Services (CMS). It is a batch system written in Common Business Oriented Language, ALC, and Statistical Analysis Software. Processing occurs daily.</p>",
-            "title": "Non-VA Hospital System (NVH)",
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
+            "title": "Non-VA Hospital System (NVH)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/5tc5-6rzq",
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
-            "identifier": "b9e1f81e-69ec-4ff0-a7d6-aa5be057267f",
+            "dataQuality": true,
             "description": "<p>Provides an enterprise-wide capability for managing individual authorizations for access to protected information. An Individual Authorization is an abstract concept and can be realized by different possible instances of concrete authorization types. Currently, the supported authorization types are Personal Representative Delegation (PR Delegation) and VA Healthcare Proxy delegation (VAHP Delegation). Delegations are a type of authorization whereby a delegator,typically a Veteran or Beneficiary, delegates specific access privileges to a delegaten such as Caregivers, Family members, Legal guardians, etc.</p>",
-            "title": "Authorization Management Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12488,54 +12470,40 @@
                     "title": "Authorization Management Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5uqy-ph6a",
-            "bureauCode": [
-                "029:00"
-            ],
-            "issued": "2024-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-23",
+            "identifier": "b9e1f81e-69ec-4ff0-a7d6-aa5be057267f",
+            "issued": "2018-02-23",
             "keyword": [
-                "2023",
-                "2023 compensation",
-                "2023 disability compensation",
-                "compensation",
-                "county",
-                "disability",
-                "disability compensation",
-                "fy2023",
-                "fy 2023",
-                "fy 2023 compensation",
-                "fy2023 compensation",
-                "fy 2023 disability compensation",
-                "fy2023 disability compensation",
-                "fy23",
-                "fy 23",
-                "fy 23 compensation",
-                "fy23 compensation",
-                "fy 23 disability compensation",
-                "fy23 disability compensation"
+                "access",
+                "identity",
+                "security"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5tc5-6rzq",
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
+            "title": "Authorization Management Service"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "029:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mike Schwaber",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/5uqy-ph6a",
+            "dataQuality": true,
             "description": "This report provides county-level estimates of the number of Veterans who were receiving VA Disability Compensation benefits as of the end of fiscal year 2023. It includes the Veterans\u2019 total service-connected disability (SCD) rating, age group, and gender. Blank values represent small cell counts that have been suppressed to protect the identity of Veterans as well as some cell counts that have been suppressed in order to prevent the determination of the values of the aforementioned small cell counts. Some categories may not sum to the total due to missing information (e.g., age, gender, etc.).\n\nThe availability of gender and age data is limited as some records have no gender or birthdate available. In the table, there are 404 Veterans whose gender is not available and 113 Veterans whose age is not available.\n\nThe number of Veterans who were disability compensation recipients during FY 2023 but were no longer disability compensation recipients at the end of FY 2023 is 138,646.  These Veterans are not included in the table.\n\nSource: Department of Veterans Affairs, Office of Enterprise Integration, Veteran Object FY23 data and Veterans Benefits Administration VETSNET FY 2023 compensation data.\n\nPrepared by National Center for Veterans Analysis & Statistics, www.va.gov/vetdata.",
-            "title": "FY 2023 Disability Compensation Recipients by County",
-            "programCode": [
-                "029:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12543,64 +12511,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5uqy-ph6a/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5uqy-ph6a/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5uqy-ph6a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5uqy-ph6a/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5uqy-ph6a/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5uqy-ph6a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5uqy-ph6a/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5uqy-ph6a/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5uqy-ph6a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/5uqy-ph6a",
+            "issued": "2024-04-23",
+            "keyword": [
+                "2023",
+                "2023 compensation",
+                "2023 disability compensation",
+                "compensation",
+                "county",
+                "disability",
+                "disability compensation",
+                "fy2023",
+                "fy 2023",
+                "fy 2023 compensation",
+                "fy2023 compensation",
+                "fy 2023 disability compensation",
+                "fy2023 disability compensation",
+                "fy23",
+                "fy 23",
+                "fy 23 compensation",
+                "fy23 compensation",
+                "fy 23 disability compensation",
+                "fy23 disability compensation"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5uqy-ph6a",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-04-23",
+            "programCode": [
+                "029:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2023 Disability Compensation Recipients by County"
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
-            "modified": "2024-03-27",
-            "keyword": [
-                "ptsd treatment",
-                "ptsd treatment coding",
-                "treatment coding"
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
-            "identifier": "https://www.data.va.gov/api/views/5vmb-i9mg",
             "description": "This table demonstrates how you might group together standardized treatments found in the PTSD Repository to progressively move toward less specificity in classification. The example provided includes psychotherapy categories and is not exhaustive to all treatments found in the PTSD Repository.",
-            "title": "Psychotherapy: Progressively Specific Grouping",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12608,26 +12590,47 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/5vmb-i9mg",
+            "issued": "2023-10-12",
+            "keyword": [
+                "ptsd treatment",
+                "ptsd treatment coding",
+                "treatment coding"
+            ],
+            "landingPage": "https://www.ptsd.va.gov/repository",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-03-27",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
             "theme": [
                 "PTSD Randomized Controlled Trials"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Psychotherapy: Progressively Specific Grouping"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/5vt8-agvs",
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
+            "description": "<p>The Disaster Emergency Medical Personnel System (DEMPS) is the Veterans Health Administrations main deployment program for clinical and non-clinical staff to an emergency or disaster. The DEMPS Program may be used for an internal VA mission, as well as supporting a mission after a Presidential Disaster Declaration under the National Response Frameworks Emergency Support Function #8 (Public Health and Medical Services). Interested, qualified VHA staff can apply online by submitting a DEMPS Application. DEMPS Coordinators and Administrators can manage volunteer data by accessing DEMPS Administration.The DEMPS Program is made up of the following entities:The DEMPS Volunteers (Full-time VHA employee, or Retiree Emergency Reserve Corps Volunteer (ERC)) VAMC DEMPS Coordinator DEMPS VAMC Facility Support Staff (Fiscal, Payroll, and Travel) DEMPS VISN Points of Contact DEMPS National Program Manager VHA Office of Emergency Management staff (Area Emergency Managers, and Regional Emergency Managers) Deputy Under Secretary for Health for Operations and Management, and The DEMPS database. In order for DEMPS to work successfully, all eight entities above must work together to deploy the DEMPS Volunteer to an emergency or disaster site.The DEMPS database was developed to collect specific information on full-time VHA medical personnel (clinical and non-clinical) and Retiree Emergency Reserve Corps (ERC) Volunteers who have volunteered and been approved by their Medical Center Director to be deployed (full-time staff or ERC Volunteers) in the event of a disaster, or to back fill a medical center (ERC Volunteers). When disasters such as hurricanes, earthquakes, floods, etc., occur and the state and local resources to handle the response/recovery process are overwhelmed, the state in which the disaster occurs may request federal assistance. In this case, a Presidential Disaster Declaration is issued and the National Response Framework (NRF) is activated. Once the damage to the area and needs have been assessed, and it is determined that medical resources are required, the Federal Emergency Management Agency (FEMA) or the Department of Health and Human Services (HHS) may task VA to provide these resources. Generally, these requests are for medical personnel (nurses, physicians, pharmacists, etc.), pharmaceutical (or other medical) supplies, and medical equipment. However, depending on the mission, VHA may deploy non-clinical staff to support the infrastructure of the deployment.</p>",
+            "identifier": "VA-VHA-EM-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2012-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "clinical",
                 "disaster",
@@ -12639,64 +12642,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/5vt8-agvs",
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
-            "identifier": "VA-VHA-EM-001",
-            "description": "<p>The Disaster Emergency Medical Personnel System (DEMPS) is the Veterans Health Administrations main deployment program for clinical and non-clinical staff to an emergency or disaster. The DEMPS Program may be used for an internal VA mission, as well as supporting a mission after a Presidential Disaster Declaration under the National Response Frameworks Emergency Support Function #8 (Public Health and Medical Services). Interested, qualified VHA staff can apply online by submitting a DEMPS Application. DEMPS Coordinators and Administrators can manage volunteer data by accessing DEMPS Administration.The DEMPS Program is made up of the following entities:The DEMPS Volunteers (Full-time VHA employee, or Retiree Emergency Reserve Corps Volunteer (ERC)) VAMC DEMPS Coordinator DEMPS VAMC Facility Support Staff (Fiscal, Payroll, and Travel) DEMPS VISN Points of Contact DEMPS National Program Manager VHA Office of Emergency Management staff (Area Emergency Managers, and Regional Emergency Managers) Deputy Under Secretary for Health for Operations and Management, and The DEMPS database. In order for DEMPS to work successfully, all eight entities above must work together to deploy the DEMPS Volunteer to an emergency or disaster site.The DEMPS database was developed to collect specific information on full-time VHA medical personnel (clinical and non-clinical) and Retiree Emergency Reserve Corps (ERC) Volunteers who have volunteered and been approved by their Medical Center Director to be deployed (full-time staff or ERC Volunteers) in the event of a disaster, or to back fill a medical center (ERC Volunteers). When disasters such as hurricanes, earthquakes, floods, etc., occur and the state and local resources to handle the response/recovery process are overwhelmed, the state in which the disaster occurs may request federal assistance. In this case, a Presidential Disaster Declaration is issued and the National Response Framework (NRF) is activated. Once the damage to the area and needs have been assessed, and it is determined that medical resources are required, the Federal Emergency Management Agency (FEMA) or the Department of Health and Human Services (HHS) may task VA to provide these resources. Generally, these requests are for medical personnel (nurses, physicians, pharmacists, etc.), pharmaceutical (or other medical) supplies, and medical equipment. However, depending on the mission, VHA may deploy non-clinical staff to support the infrastructure of the deployment.</p>",
-            "title": "Disaster Emergency Medical Personnel System (DEMPS)",
-            "programCode": [
-                "029:041"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "2012-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Disaster Emergency Medical Personnel System (DEMPS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-04-01T04:00:00Z/2014-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "burrial expenses allowances for vets",
-                "cfda 64 101",
-                "compensation and pension",
-                "usa spending"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Monica Reyes",
                 "hasEmail": "mailto:Monica.Reyes@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-USASPENDING042014-057",
+            "dataQuality": true,
             "description": "<p>USA Spending- Compensation and Pension- Burial Expenses Allowance for Vets for April 2013.</p>",
-            "title": "USA Spending file- 04/2014 Compensation and Pension-  CFDA 64.101",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12705,41 +12685,43 @@
                     "title": "USA Spending file- 04/2014 Compensation and Pension- CFDA 64.101"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-USASPENDING042014-057",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "burrial expenses allowances for vets",
+                "cfda 64 101",
+                "compensation and pension",
+                "usa spending"
+            ],
+            "landingPage": "https://www.usaspending.gov/",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
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
-            ]
+            ],
+            "title": "USA Spending file- 04/2014 Compensation and Pension-  CFDA 64.101"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5vwx-gv29",
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
-            "identifier": "VA-OEI-OEI-163",
             "description": "<p>This reports shows the services and benefits the Department of Veterans Affairs provided in 1998.</p>",
-            "title": "Annual Report 1998",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12748,40 +12730,42 @@
                     "title": "Annual Report 1998"
                 }
             ],
+            "identifier": "VA-OEI-OEI-163",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "services",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5vwx-gv29",
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
+            "title": "Annual Report 1998"
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
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "budget",
-                "fy2009"
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
-            "identifier": "VA-OM-OM-030",
+            "dataQuality": true,
             "description": "<p>FY2009 VA Budget Submission.</p>",
-            "title": "FY2009 VA Budget Submission",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12790,43 +12774,43 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-030",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "fy2009"
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
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY2009 VA Budget Submission"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5wm6-mtp3",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "montana"
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
-            "identifier": "VA-OEI-OEI-225",
             "description": "<p>This summary describes the programs and services VA provided in Montana in fiscal year 2015.</p>",
-            "title": "State Summary: Montana FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12835,41 +12819,40 @@
                     "title": "Montana"
                 }
             ],
+            "identifier": "VA-OEI-OEI-225",
+            "issued": "2017-07-26",
+            "keyword": [
+                "montana"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5wm6-mtp3",
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
+            "title": "State Summary: Montana FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5wq6-44sq",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "minorities",
-                "vetpop14"
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
-            "identifier": "https://www.data.va.gov/api/views/5wq6-44sq",
             "description": "Numbers rounded to the nearest 1,000.",
-            "title": "VETPOP2014 LIVING VETERANS BY RACE/ETHNICITY, GENDER, 2013-2043",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12877,65 +12860,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5wq6-44sq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5wq6-44sq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5wq6-44sq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5wq6-44sq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5wq6-44sq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5wq6-44sq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5wq6-44sq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5wq6-44sq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5wq6-44sq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/5wq6-44sq",
+            "issued": "2019-10-24",
+            "keyword": [
+                "minorities",
+                "vetpop14"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5wq6-44sq",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
+            "title": "VETPOP2014 LIVING VETERANS BY RACE/ETHNICITY, GENDER, 2013-2043"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5xcm-tiar",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.polytrauma.va.gov/"
-            ],
-            "keyword": [
-                "community",
-                "health",
-                "health care",
-                "polytrauma",
-                "rehabilitation",
-                "veterans affairs"
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
-            "identifier": "VA-VHA-PCS-014",
+            "dataQuality": true,
+            "describedBy": "https://www.polytrauma.va.gov/",
             "description": "<p>Provides a listing of approved VA Polytrauma Sites by their designation level to assist in contacting appropriate facilities for Polytrauma rehabilitation services.</p>",
-            "title": "VA Polytrauma Sites",
-            "programCode": [
-                "029:040"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12943,96 +12920,104 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5xcm-tiar/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5xcm-tiar/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5xcm-tiar/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5xcm-tiar/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5xcm-tiar/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5xcm-tiar/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5xcm-tiar/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5xcm-tiar/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5xcm-tiar/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.polytrauma.va.gov/",
-            "dataQuality": true,
+            "identifier": "VA-VHA-PCS-014",
+            "issued": "2017-07-26",
+            "keyword": [
+                "community",
+                "health",
+                "health care",
+                "polytrauma",
+                "rehabilitation",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5xcm-tiar",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.polytrauma.va.gov/"
+            ],
+            "temporal": "2013-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Section 10. National Security and Veterans Affairs"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Polytrauma Sites"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/5xk5-7gwk",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Alysia Blake",
+                "hasEmail": "mailto:vaconcvas@va.gov"
+            },
+            "dataQuality": true,
+            "description": "The U.S. Department of Veterans Affairs honors America\u2019s Veterans by highlighting VA benefits provided to the Survivors of those who made the ultimate sacrifice.",
+            "identifier": "https://www.data.va.gov/api/views/5xk5-7gwk",
             "issued": "2023-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-11",
             "keyword": [
                 "benefits",
                 "survivors",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Alysia Blake",
-                "hasEmail": "mailto:vaconcvas@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/5xk5-7gwk",
+            "modified": "2023-05-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/5xk5-7gwk",
-            "description": "The U.S. Department of Veterans Affairs honors America\u2019s Veterans by highlighting VA benefits provided to the Survivors of those who made the ultimate sacrifice.",
-            "title": "Memorial Day 2023",
-            "programCode": [
-                "029:086"
-            ],
-            "dataQuality": true
+            "title": "Memorial Day 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5xun-beu8",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-06-28",
-            "@type": "dcat:Dataset",
-            "modified": "2021-11-12",
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
-            "identifier": "https://www.data.va.gov/api/views/5xun-beu8",
+            "dataQuality": true,
             "description": "This dataset is comprised of 1 year estimate data from the American Community Survey published as of 2019.",
-            "title": "NCVAS State Summaries - Income Percentages (chart)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13040,59 +13025,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5xun-beu8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5xun-beu8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5xun-beu8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5xun-beu8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5xun-beu8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5xun-beu8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5xun-beu8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5xun-beu8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5xun-beu8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/5xun-beu8",
+            "issued": "2021-06-28",
+            "keyword": [
+                "ncvas",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5xun-beu8",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2021-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "NCVAS State Summaries - Income Percentages (chart)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5yag-25jz",
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
-            "identifier": "946153ea-c908-4b0c-9bba-b94227e139fc",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary West Virginia FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13100,43 +13084,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "946153ea-c908-4b0c-9bba-b94227e139fc",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5yag-25jz",
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
+            "title": "State Summary West Virginia FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5yq6-updb",
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
-            "identifier": "https://www.data.va.gov/api/views/5yq6-updb",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located</p>",
-            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS MAR2019",
-            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13144,61 +13128,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5yq6-updb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5yq6-updb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5yq6-updb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/5yq6-updb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5yq6-updb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5yq6-updb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/5yq6-updb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/5yq6-updb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/5yq6-updb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/5yq6-updb",
+            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 118"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5yq6-updb",
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
+            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/5yq7-jqeq",
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
-            "identifier": "37f830b6-74d3-4882-bb1f-c048a9e35b6e",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Massachusetts FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13206,26 +13190,45 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "37f830b6-74d3-4882-bb1f-c048a9e35b6e",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/5yq7-jqeq",
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
+            "title": "State Summary Massachusetts FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/5yvv-z4vg",
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
+            "description": "<p><b>NOTE: This dataset is Inactive and is no longer supported. Any historical knowledge regarding meta data or it's creation is no longer available. All known information is proved as part of this data set.</b></p>\n<p>The National Cardiac Device Surveillance Program Database supports the Eastern Pacemaker Surveillance Center (EPSC) staff in its function of monitoring some 11,000 Veterans Health Administration (VHA) patients who have implanted pacemakers or cardioverters. The database stores medically useful information about the patients and their pacemaker test results in order to highlight serial changes, which determine whether the pacemaker is still functioning normally, or whether the patient requires further intervention. The EPSC staff performs regular telephonic checkups, in conjunction with less frequent in-hospital clinic checkups, to determine when pacemakers need to be replaced. Patients are scheduled and called by the Pacemaker Surveillance Center, and have their electrocardiogram recorded and analyzed over the phone, using wires attached to their fingers and a VHA-supplied transmitter.  Additionally, some patients are monitored via web-based downloads of their device telemetry.  The Pacemaker Center also provides in-hospital clinic checkups for local Washington DC VHA pacemaker patients. All information obtained during the checkups is recorded in the EPSC Database. The database also contains records of pacemaker patients being monitored by VHA facilities east of the Mississippi and who are not being monitored directly by their respective VA medical centers. The VHA Department of Medical Services encourages local VHA medical centers to refer their patients for pacemaker follow-up monitoring to either the Eastern Surveillance Center or to the counterpart Western Surveillance Center in San Francisco, whichever is geographically appropriate. However, referral is optional. The database also maintains a registry of all VHA patients, living and deceased, who have had pacemakers implanted at, or who have been monitored by, VHA facilities. The EPSC receives information for the registry directly from the medical centers for patients that it does not monitor, totaling over 80,000 as of 2010.</p>",
+            "identifier": "VA-VHA-PCS-005",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1982-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2022-08-29",
             "keyword": [
                 "cardiology",
                 "electrocardiogram",
@@ -13235,65 +13238,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/5yvv-z4vg",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-08-29",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PCS-005",
-            "description": "<p><b>NOTE: This dataset is Inactive and is no longer supported. Any historical knowledge regarding meta data or it's creation is no longer available. All known information is proved as part of this data set.</b></p>\n<p>The National Cardiac Device Surveillance Program Database supports the Eastern Pacemaker Surveillance Center (EPSC) staff in its function of monitoring some 11,000 Veterans Health Administration (VHA) patients who have implanted pacemakers or cardioverters. The database stores medically useful information about the patients and their pacemaker test results in order to highlight serial changes, which determine whether the pacemaker is still functioning normally, or whether the patient requires further intervention. The EPSC staff performs regular telephonic checkups, in conjunction with less frequent in-hospital clinic checkups, to determine when pacemakers need to be replaced. Patients are scheduled and called by the Pacemaker Surveillance Center, and have their electrocardiogram recorded and analyzed over the phone, using wires attached to their fingers and a VHA-supplied transmitter.  Additionally, some patients are monitored via web-based downloads of their device telemetry.  The Pacemaker Center also provides in-hospital clinic checkups for local Washington DC VHA pacemaker patients. All information obtained during the checkups is recorded in the EPSC Database. The database also contains records of pacemaker patients being monitored by VHA facilities east of the Mississippi and who are not being monitored directly by their respective VA medical centers. The VHA Department of Medical Services encourages local VHA medical centers to refer their patients for pacemaker follow-up monitoring to either the Eastern Surveillance Center or to the counterpart Western Surveillance Center in San Francisco, whichever is geographically appropriate. However, referral is optional. The database also maintains a registry of all VHA patients, living and deceased, who have had pacemakers implanted at, or who have been monitored by, VHA facilities. The EPSC receives information for the registry directly from the medical centers for patients that it does not monitor, totaling over 80,000 as of 2010.</p>",
-            "title": "National Cardiac Device Surveillance Program Database",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1982-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Cardiac Device Surveillance Program Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6263-7mn5",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-08",
-            "keyword": [
-                "compensation",
-                "compensation and pension",
-                "county",
-                "fy20",
-                "fy 20",
-                "fy2020",
-                "fy 2020"
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
-            "identifier": "https://www.data.va.gov/api/views/6263-7mn5",
+            "dataQuality": true,
             "description": "This report provides county-level estimates of the number of Veterans who received VA Disability Compensation benefits during fiscal year 2020.  It includes the Veterans\u2019 total service-connected disability (SCD) rating, age group, and gender.  Blank values represent small cell counts that have been suppressed to protect the identity of Veterans.  In the \"Total: Disability Compensation Recipients\" column, each blank cell represents less than 10 Veterans.  Some categories may not sum to the total due to missing information (e.g., age, gender, etc.).\n\nSource: Department of Veterans Affairs, Office of Enterprise Integration, United States Veterans Eligibility Trends & Statistics (USVETS) 2020 and Veterans Benefits Administration VETSNET FY 2020 compensation data.\n\nPrepared by National Center for Veterans Analysis & Statistics, www.va.gov/vetdata.",
-            "title": "FY 2020 Disability Compensation Recipients by County",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13301,62 +13281,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6263-7mn5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6263-7mn5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6263-7mn5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/6263-7mn5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6263-7mn5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6263-7mn5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/6263-7mn5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/6263-7mn5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/6263-7mn5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/6263-7mn5",
+            "issued": "2022-02-02",
+            "keyword": [
+                "compensation",
+                "compensation and pension",
+                "county",
+                "fy20",
+                "fy 20",
+                "fy2020",
+                "fy 2020"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6263-7mn5",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-02-08",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2020 Disability Compensation Recipients by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/6263-phe6",
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
-            "identifier": "5134c20d-efc5-4c2b-8894-548aeccca7d9",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Minnesota FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13364,114 +13348,114 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "5134c20d-efc5-4c2b-8894-548aeccca7d9",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/6263-phe6",
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
+            "title": "State Summary Minnesota FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/62n6-9j8t",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Massachusetts FY2023",
+            "identifier": "https://www.data.va.gov/api/views/62n6-9j8t",
             "issued": "2024-06-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fy2024",
                 "massachusetts",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/62n6-9j8t",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/62n6-9j8t",
-            "description": "NCVAS State Summary Massachusetts FY2023",
-            "title": "NCVAS State Summary Massachusetts FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Massachusetts FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://cfm.vaco.va.gov/docrs/login.aspx?ReturnUrl=%2fdocrs%2fdefault.aspx",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Non-Public access level is warranted because of the contract and financial data and building plans aggreated in the system.  Knowledge of this information could possibly compromise contract negoiations for construction services and or building security.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dallas Hudson",
+                "hasEmail": "mailto:dennis.hudson@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Document Conversion and Retrieval System (DOCRS) is a repository of building construction and real property based documents that have been completed.  The documents are archival in nature and the system is accessed by CFM personnel and authorized station engineering personnel.  Access to these documents limited due to security concerns because many of the documents are building plans type documents for structures throughout the VA.  DOCRS is a web based system hosted within the VA intranet.</p>",
+            "identifier": "VA-CFM-DOCRS-007",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1900-01-01T05:00:00Z/2014-05-01T04:00:00Z",
-            "modified": "2024-08-26",
             "keyword": [
                 "construction management",
                 "construction plans",
                 "project management"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dallas Hudson",
-                "hasEmail": "mailto:dennis.hudson@va.gov"
-            },
+            "landingPage": "https://cfm.vaco.va.gov/docrs/login.aspx?ReturnUrl=%2fdocrs%2fdefault.aspx",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-CFM-DOCRS-007",
-            "description": "<p>The Document Conversion and Retrieval System (DOCRS) is a repository of building construction and real property based documents that have been completed.  The documents are archival in nature and the system is accessed by CFM personnel and authorized station engineering personnel.  Access to these documents limited due to security concerns because many of the documents are building plans type documents for structures throughout the VA.  DOCRS is a web based system hosted within the VA intranet.</p>",
-            "title": "Document Conversion and Retrieval System (DOCRS)",
-            "programCode": [
-                "029:086"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "rights": "Non-Public access level is warranted because of the contract and financial data and building plans aggreated in the system.  Knowledge of this information could possibly compromise contract negoiations for construction services and or building security.",
+            "temporal": "1900-01-01T05:00:00Z/2014-05-01T04:00:00Z",
             "theme": [
                 "Construction Project Management Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Document Conversion and Retrieval System (DOCRS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/63px-hq5d",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-09-14",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "american indian and alaskan native",
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
-            "identifier": "cd48f374-32ac-4ed0-956d-ea72b4f6290b",
+            "dataQuality": true,
             "description": "<p>To show demographic and socio-economic percentage of distribution of AIAN Veterans by gender, age, state, period of service, education, personal income and other important characteristics</p>",
-            "title": "AIAN Veterans Report (2015)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13479,39 +13463,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "cd48f374-32ac-4ed0-956d-ea72b4f6290b",
+            "issued": "2017-09-14",
+            "keyword": [
+                "american indian and alaskan native",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/63px-hq5d",
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
+            "title": "AIAN Veterans Report (2015)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://github.com/department-of-veterans-affairs/VBA-August-2015/raw/master/Copy%20of%20VGLI%20Enrollment%20by%20State%206-30-15.xlsx",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-06-01T04:00:00Z/2015-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "insurance",
-                "vba benefits",
-                "vgli"
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
-            "identifier": "VA-VBA-INS2015-002",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state. This report provides a snapshot of the active VGLI membership as of June 30, 2015. For members who reside outside the United States, membership is not identified by individual country. The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "FY15_Number of Veterans Insured by VGLI by State as of 6-30-15",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13519,44 +13502,44 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2015-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "insurance",
+                "vba benefits",
+                "vgli"
+            ],
+            "landingPage": "https://github.com/department-of-veterans-affairs/VBA-August-2015/raw/master/Copy%20of%20VGLI%20Enrollment%20by%20State%206-30-15.xlsx",
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
+            "title": "FY15_Number of Veterans Insured by VGLI by State as of 6-30-15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/63w8-tkj5",
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
-            "identifier": "VA-OGC-047",
             "description": "<p>General Counsel Legal Automation Workload System (GCLAWS)-VA</p>",
-            "title": "OGC Privacy Act System of Records Notice 144VA026",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13565,42 +13548,43 @@
                     "title": "OGC Privacy Act System of Records Notice 144VA026"
                 }
             ],
+            "identifier": "VA-OGC-047",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "system of records"
+            ],
+            "landingPage": "https://www.data.va.gov/d/63w8-tkj5",
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
+            "title": "OGC Privacy Act System of Records Notice 144VA026"
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
-            "modified": "2020-11-03",
-            "keyword": [
-                "minorities",
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
-            "identifier": "VA-OEI-OEI-234",
+            "dataQuality": true,
             "description": "<p>This report is the first comprehensive report that chronicles the history of racial and ethnic minorities in the military and as Veterans, profiles characteristics of minority Veterans in 2014, illustrates how minority Veterans utilized some of the major benefits and services offered by the VA.</p>",
-            "title": "Minority Veteran Report",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13608,46 +13592,46 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-234",
+            "issued": "2017-07-26",
+            "keyword": [
+                "minorities",
+                "statistics",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-11-03",
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
+            "title": "Minority Veteran Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/643w-pxhu",
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
-            "identifier": "https://www.data.va.gov/api/views/643w-pxhu",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM BENEFITS to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA\u2019s determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAR2019",
-            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13655,86 +13639,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/643w-pxhu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/643w-pxhu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/643w-pxhu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/643w-pxhu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/643w-pxhu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/643w-pxhu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/643w-pxhu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/643w-pxhu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/643w-pxhu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/643w-pxhu",
+            "isPartOf": "f9dff532-b60f-484c-aa3a-38716834d803",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 117"
+            ],
+            "landingPage": "https://www.data.va.gov/d/643w-pxhu",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
```

